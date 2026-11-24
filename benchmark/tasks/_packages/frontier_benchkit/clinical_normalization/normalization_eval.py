"""Organizer-side scorer for the H7-50 clinical procedure normalization suite.

    score = 0.25 * partial_f1 + 0.25 * joint_record_f1 + 0.50 * question_exact

Two task shapes, both from ``H2_Scoring_Criteria.md``:

``H7A`` (target-conditioned normalization, 001-025)
    partial_f1   multiset F1 over ``target_id`` -- did the reply name the right
                 target set?
    joint_f1     multiset F1 over ``(target_id, code, system)``
``H7B`` (free-text procedure structuring, 026-050)
    partial_f1   multiset F1 over ``(surface, encounter_id)`` -- the mention and
                 its encounter, character offsets ignored
    joint_f1     multiset F1 over ``(surface, start, end, encounter_id, code,
                 system)``

``question_exact`` is 1.0 only when the complete answer matches, i.e. when
``joint_f1`` reaches 1.0; it is the all-or-nothing half of the weight and is what
separates "nearly right" from "right".

``procedure_name`` is excluded from every comparison. Both prompts call it
descriptive and auxiliary and state that release-specific exact preferred wording
is not required, so scoring it would penalise a correct normalization for a
synonym.

Matching is one-to-one over multisets: a duplicated record is a false positive,
an omitted record is a false negative, and a record whose code/system/target is
malformed can never match, so invalid JSON or schema-invalid output earns zero
matching credit rather than raising.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

SYSTEM = "http://snomed.info/sct"
WEIGHTS = {"partial_f1": 0.25, "joint_record_f1": 0.25, "question_exact": 0.50}
_DIGITS = re.compile(r"^[0-9]+$")


def _load(tests_dir):
    key = json.loads((Path(tests_dir) / "answer.json").read_text(encoding="utf-8"))
    return key, key.get("scoring") or {}


def _strip_fence(text):
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if len(lines) >= 3 and lines[-1].strip().startswith("```"):
            return "\n".join(lines[1:-1]).strip()
    return text


def _payload(prediction):
    """A submission as a dict; raises ``ValueError`` if it cannot be read."""
    if isinstance(prediction, dict):
        payload = prediction
    elif isinstance(prediction, str):
        try:
            payload = json.loads(_strip_fence(prediction))
        except json.JSONDecodeError as exc:
            raise ValueError(f"submission is not valid JSON: {exc.msg}") from exc
    else:
        raise ValueError(f"unsupported submission type: {type(prediction).__name__}")
    if not isinstance(payload, dict):
        raise ValueError("submission JSON must be an object")
    if set(payload) == {"answer"} and isinstance(payload["answer"], dict):
        payload = payload["answer"]
    return payload


def _text(value):
    return value.strip() if isinstance(value, str) and value.strip() else None


def _code(value):
    return value if isinstance(value, str) and _DIGITS.match(value) else None


def _system(value):
    return value if value == SYSTEM else None


def _index(value):
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str) and re.fullmatch(r"-?[0-9]+", value.strip()):
        return int(value.strip())
    return None


def _task(spec, payload):
    declared = str(spec.get("task") or "").upper()
    if declared in ("H7A", "H7B"):
        return declared
    return "H7A" if "procedures" in payload else "H7B"


def _rows(payload, task):
    """Flatten a submission to a list of records; ``None`` marks an unreadable one."""
    if task == "H7A":
        procs = payload.get("procedures")
        if not isinstance(procs, list):
            raise ValueError("missing 'procedures' array")
        return procs
    encounters = payload.get("encounters")
    if not isinstance(encounters, list):
        raise ValueError("missing 'encounters' array")
    rows = []
    for enc in encounters:
        if not isinstance(enc, dict):
            rows.append(None)
            continue
        inner = enc.get("procedures")
        if not isinstance(inner, list):
            rows.append(None)
            continue
        for proc in inner:
            if isinstance(proc, dict) and proc.get("encounter_id") is None:
                proc = dict(proc, encounter_id=enc.get("encounter_id"))
            rows.append(proc)
    return rows


def keys(rows, task):
    """``(partial_keys, joint_keys)``; unreadable records map to ``None``."""
    partial, joint = [], []
    for row in rows:
        if not isinstance(row, dict):
            partial.append(None)
            joint.append(None)
            continue
        if task == "H7A":
            target = _text(row.get("target_id"))
            partial.append(target)
            joint.append(
                None if target is None else (target, _code(row.get("code")), _system(row.get("system")))
            )
        else:
            surface = _text(row.get("surface"))
            encounter = _text(row.get("encounter_id"))
            partial.append(None if surface is None or encounter is None else (surface, encounter))
            start, end = _index(row.get("start")), _index(row.get("end"))
            joint.append(
                None
                if surface is None or encounter is None or start is None or end is None
                else (surface, start, end, encounter, _code(row.get("code")), _system(row.get("system")))
            )
    return partial, joint


def _matched(pred_keys, ref_keys):
    """``(true_positive, false_positive, false_negative)`` over multisets."""
    pred = Counter(k for k in pred_keys if k is not None)
    ref = Counter(k for k in ref_keys if k is not None)
    tp = sum(min(count, ref[key]) for key, count in pred.items() if key in ref)
    fp = len([k for k in pred_keys if k is not None]) - tp
    fn = len([k for k in ref_keys if k is not None]) - tp
    return tp, fp, fn


def _f1(pred_keys, ref_keys):
    tp, fp, fn = _matched(pred_keys, ref_keys)
    if tp == 0:
        return 0.0, tp, fp, fn
    return 2.0 * tp / (2.0 * tp + fp + fn), tp, fp, fn


def score_case(prediction, tests_dir, **kwargs):
    """Score one submission against the frozen normalization gold."""
    key, spec = _load(tests_dir)
    gold = key.get("answer")
    if not isinstance(gold, dict):
        raise ValueError("answer.json has no normalization gold object")
    try:
        payload = _payload(prediction)
    except ValueError as exc:
        return {
            "score": 0.0,
            "detail": {"scoring": "h2_normalization_composite", "status": "invalid_submission",
                       "error": str(exc), "errors": [str(exc)]},
        }

    task = _task(spec, payload)
    try:
        pred_rows = _rows(payload, task)
    except ValueError as exc:
        return {
            "score": 0.0,
            "detail": {"scoring": "h2_normalization_composite", "task": task,
                       "status": "invalid_submission", "error": str(exc), "errors": [str(exc)]},
        }
    ref_rows = _rows(gold, task)

    pred_partial, pred_joint = keys(pred_rows, task)
    ref_partial, ref_joint = keys(ref_rows, task)
    partial_f1, _, _, _ = _f1(pred_partial, ref_partial)
    joint_f1, tp, fp, fn = _f1(pred_joint, ref_joint)
    exact = 1.0 if joint_f1 >= 1.0 else 0.0
    score = (
        WEIGHTS["partial_f1"] * partial_f1
        + WEIGHTS["joint_record_f1"] * joint_f1
        + WEIGHTS["question_exact"] * exact
    )

    detail = {
        "scoring": "h2_normalization_composite",
        "task": task,
        "status": "scored",
        "partial_f1": round(partial_f1, 6),
        "joint_record_f1": round(joint_f1, 6),
        "question_exact": exact,
        "weights": dict(WEIGHTS),
        "partial_metric": "target_id" if task == "H7A" else "surface+encounter",
        "n_predicted": len(pred_rows),
        "n_reference": len(ref_rows),
        "n_matched": tp,
        "n_false_positive": fp,
        "n_false_negative": fn,
        "n_unreadable": sum(1 for k in pred_joint if k is None),
        "procedure_name_scored": False,
    }
    if detail["n_unreadable"]:
        detail["errors"] = [f"{detail['n_unreadable']} submission record(s) could not be normalized"]
    return {"score": max(0.0, min(1.0, score)), "detail": detail}
