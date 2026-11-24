"""Deterministic single-case scoring for the converted benchmark tasks.

`tests/answer.json` holds both the gold value and a `scoring` spec; this module
is the only place those specs are interpreted. Every converted task keeps its
task-native contract, so the spec differs per item:

    option_letter      gold is one option letter; exact match after normalisation.
    option_set         gold is the set of correct letters; exact set equality.
    ranking_concordant gold is the ordered id list; fraction of candidate pairs
                       ordered the way gold orders them (the benchmark source
                       metric: ``concordant pairs / C(n, 2)``).
    top_k_overlap      gold is the correct id set of size k; |intersect| / k.
    numeric_gaussian  gold is a finite number; exp(-|pred - gold| / tolerance).
    label_exact       gold is a scalar class label; exact match.

Submissions arrive either as already-parsed handler output (dict / list / str)
or as raw text; every parser below accepts both, so `harness validate
--score-check` (which replays the gold value itself) and a live run agree.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

FENCE = re.compile(r"^```(?:json|text)?\s*\n?([\s\S]*?)\s*```$", re.IGNORECASE)


def _strip_fence(text):
    match = FENCE.match(str(text).strip())
    return (match.group(1) if match else str(text)).strip()


def _json_object(value):
    """Best-effort JSON object from a dict or a (possibly fenced) JSON string."""
    if isinstance(value, dict):
        return value
    text = _strip_fence(value)
    if text.startswith("{"):
        try:
            parsed = json.loads(text)
        except (ValueError, TypeError):
            match = re.search(r"\{[\s\S]*\}", text)
            if not match:
                return None
            try:
                parsed = json.loads(match.group(0))
            except (ValueError, TypeError):
                return None
        return parsed if isinstance(parsed, dict) else None
    return None


def _json_array(value):
    if isinstance(value, (list, tuple)):
        return list(value)
    text = _strip_fence(value)
    start = text.find("[")
    if start < 0:
        return None
    try:
        parsed = json.JSONDecoder().raw_decode(text, start)[0]
    except (ValueError, TypeError, RecursionError):
        return None
    return parsed if isinstance(parsed, list) else None


def _allowed(options):
    return {str(x).strip().upper()[:1] for x in options if str(x).strip()}


def parse_letter(value, options):
    """One option letter (A/B/C/...) or None."""
    allowed = _allowed(options)
    if value is None:
        return None
    if isinstance(value, dict):
        for key in ("answer", "letter", "choice", "label", "prediction"):
            if key in value:
                got = parse_letter(value[key], options)
                if got:
                    return got
        return None
    text = str(value).strip()
    if not text:
        return None
    obj = _json_object(text)
    if obj is not None:
        got = parse_letter(obj, options)
        if got:
            return got
    if len(text) == 1 and text.upper() in allowed:
        return text.upper()
    match = re.search(
        r"(?i)(?:final\s+)?(?:answer|choice|option|label|答案|选项)\s*"
        r"(?:is\s*|[=:：\-.\s]\s*)([A-Za-z])\b",
        text,
    )
    if match and match.group(1).upper() in allowed:
        return match.group(1).upper()
    match = re.match(r"^[\s*_`>'\"\[(]*([A-Za-z])[)\].:：]", text)
    if match and match.group(1).upper() in allowed:
        return match.group(1).upper()
    hits = [x.upper() for x in re.findall(r"\b([A-Z])\b", text) if x.upper() in allowed]
    return hits[-1] if hits else None


def parse_letters(value, options):
    """A set of option letters (sorted list) or None."""
    allowed = _allowed(options)
    if value is None:
        return None
    if isinstance(value, dict):
        for key in ("selected", "answers", "letters", "answer", "label"):
            if key in value:
                got = parse_letters(value[key], options)
                if got:
                    return got
        return None
    if isinstance(value, (list, tuple, set)):
        out = set()
        for item in value:
            got = parse_letter(item, options)
            if not got:
                return None
            out.add(got)
        return sorted(out) or None
    text = _strip_fence(value)
    if not text:
        return None
    array = _json_array(text)
    if array is not None:
        return parse_letters(array, options)
    tokens = [t for t in re.split(r"[,\;\s/|&]+|and", text) if t]
    letters = []
    for token in tokens:
        if len(token) == 1 and token.upper() in allowed:
            letters.append(token.upper())
        elif len(token) > 1 and all(ch.upper() in allowed for ch in token):
            letters.extend(ch.upper() for ch in token)
    return sorted(set(letters)) or None


def parse_ids(value):
    """Ordered id list from a list, a JSON array, or a separated string."""
    if value is None:
        return None
    if isinstance(value, (list, tuple)):
        return [str(x).strip() for x in value if str(x).strip()]
    if isinstance(value, dict):
        for key in ("order", "ranking", "ranked", "answer", "prediction", "ids", "selected"):
            if key in value:
                got = parse_ids(value[key])
                if got:
                    return got
        return None
    text = _strip_fence(value)
    if not text:
        return None
    array = _json_array(text)
    if array is not None:
        return [str(x).strip() for x in array if str(x).strip()]
    return [x.strip() for x in re.split(r"[,;\n>]+", text) if x.strip()]


def parse_number(value):
    """One finite float or None."""
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        number = float(value)
        return number if math.isfinite(number) else None
    if isinstance(value, dict):
        for key in ("value", "answer", "prediction", "pred", "number"):
            if key in value:
                got = parse_number(value[key])
                if got is not None:
                    return got
        return None
    text = _strip_fence(value)
    obj = _json_object(text)
    if obj is not None:
        return parse_number(obj)
    match = re.search(r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?", text)
    if not match:
        return None
    try:
        number = float(match.group(0))
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def parse_label(value):
    """A scalar class label as a canonical string or None."""
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, dict):
        for key in ("label", "answer", "class", "prediction"):
            if key in value:
                got = parse_label(value[key])
                if got is not None:
                    return got
        return None
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    text = _strip_fence(value)
    obj = _json_object(text)
    if obj is not None:
        return parse_label(obj)
    match = re.search(r"-?\d+(?:\.\d+)?", text)
    if match:
        number = float(match.group(0))
        return str(int(number)) if number.is_integer() else str(number)
    return text.strip() or None


def concordant_fraction(gold_ids, pred_ids):
    """Fraction of candidate pairs that ``pred_ids`` orders like ``gold_ids``.

    This is the metric the benchmark sources themselves use for four-candidate
    rankings: ``DNA_Protein_From_KeWang/private/build.py`` asserts
    ``sum(perm.index(a) < perm.index(b) ...) / 6`` over all 960 permutations,
    and replaying its frozen history reproduces 139/139 DNA and 39/39 Protein
    recorded scores. It is bounded in [0, 1], scores 0.5 for a random order,
    and needs no clipping, unlike Spearman rho.
    """
    n = len(gold_ids)
    if n < 2 or len(pred_ids) != n:
        return 0.0
    position = {name: i for i, name in enumerate(pred_ids)}
    pairs = n * (n - 1) / 2.0
    concordant = 0
    for i, first in enumerate(gold_ids):
        for second in gold_ids[i + 1:]:
            if position[first] < position[second]:
                concordant += 1
    return concordant / pairs


def score_case(prediction, tests_dir):
    """Score one submission against the case's stored gold + spec."""
    key = json.loads((Path(tests_dir) / "answer.json").read_text(encoding="utf-8"))
    gold = key["answer"]
    spec = key.get("scoring") or {}
    kind = str(spec.get("type") or "").strip()
    detail = {"scoring": kind, "status": "scored"}
    score = 0.0

    if kind == "option_letter":
        options = spec.get("options") or []
        gold_letter = parse_letter(gold, options)
        pred_letter = parse_letter(prediction, options)
        detail.update(gold=gold_letter, prediction=pred_letter)
        score = 1.0 if pred_letter and pred_letter == gold_letter else 0.0
        if pred_letter is None:
            detail["status"] = "invalid_submission"

    elif kind == "option_set":
        options = spec.get("options") or []
        gold_set = parse_letters(gold, options) or []
        pred_set = parse_letters(prediction, options)
        detail.update(gold=gold_set, prediction=pred_set)
        if pred_set is None:
            detail["status"] = "invalid_submission"
        else:
            score = 1.0 if pred_set == gold_set else 0.0

    elif kind == "ranking_concordant":
        gold_ids = parse_ids(gold) or []
        pred_ids = parse_ids(prediction)
        detail.update(gold=gold_ids, prediction=pred_ids)
        if pred_ids is None:
            detail["status"] = "invalid_submission"
        elif len(pred_ids) != len(gold_ids) or set(pred_ids) != set(gold_ids):
            detail["status"] = "invalid_submission"
            detail["error"] = "prediction must list every candidate exactly once"
        else:
            score = concordant_fraction(gold_ids, pred_ids)
            detail["concordant_pairs"] = round(score * len(gold_ids) * (len(gold_ids) - 1) / 2.0)

    elif kind == "top_k_overlap":
        gold_ids = parse_ids(gold) or []
        pred_ids = parse_ids(prediction)
        k = int(spec.get("k") or len(gold_ids) or 1)
        detail.update(gold=gold_ids, prediction=pred_ids, k=k)
        if pred_ids is None:
            detail["status"] = "invalid_submission"
        elif len(pred_ids) != k or len(set(pred_ids)) != k:
            detail["status"] = "invalid_submission"
            detail["error"] = "prediction must contain exactly %d distinct candidate ids" % k
        else:
            hit = len(set(pred_ids) & set(gold_ids))
            detail["matched"] = hit
            score = hit / float(k)

    elif kind == "numeric_gaussian":
        truth = parse_number(gold)
        pred = parse_number(prediction)
        tolerance = float(spec.get("tolerance") or 1.0)
        detail.update(gold=truth, prediction=pred, tolerance=tolerance)
        if pred is None or truth is None or tolerance <= 0:
            detail["status"] = "invalid_submission"
        else:
            delta = abs(pred - truth)
            detail["absolute_error"] = delta
            score = math.exp(-delta / tolerance)

    elif kind == "label_exact":
        gold_label = parse_label(gold)
        pred_label = parse_label(prediction)
        detail.update(gold=gold_label, prediction=pred_label)
        if pred_label is None:
            detail["status"] = "invalid_submission"
        else:
            score = 1.0 if pred_label == gold_label else 0.0

    else:
        raise ValueError("unknown scoring spec: %r" % (kind,))

    return {"score": max(0.0, min(1.0, float(score))), "detail": detail}
