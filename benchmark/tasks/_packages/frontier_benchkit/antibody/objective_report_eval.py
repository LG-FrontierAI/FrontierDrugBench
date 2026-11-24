"""Frozen, organizer-side scoring for the original-report prediction tasks.

No model judge, network, curve fit, or submission-selected metric is used.
Invalid submissions score zero as a whole; defective organizer gold raises.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


def _invalid_constant(value):
    raise ValueError("nonfinite JSON constant: " + value)


def _decode(value):
    if isinstance(value, str):
        return json.loads(value, object_pairs_hook=_unique_object,
                          parse_constant=_invalid_constant)
    return value


def _decode_ranking(value):
    """The published interface is one comma-separated line; arrays also work."""
    if not isinstance(value, str):
        return value
    text = value.strip()
    if text.startswith(("[", "{")):
        return _decode(text)
    # Whitespace around comma-delimited IDs is immaterial, including line
    # wrapping. Missing commas or explanatory text remain invalid ID tokens.
    return [token.strip() for token in text.split(",")]


def _positive_finite(value):
    if type(value) not in (int, float):
        return False
    try:
        return math.isfinite(value) and value > 0
    except (OverflowError, TypeError):
        return False


def _finite(value):
    if type(value) not in (int, float):
        return False
    try:
        return math.isfinite(value)
    except (OverflowError, TypeError):
        return False


def _midranks(values):
    ordered = sorted(range(len(values)), key=values.__getitem__)
    ranks = [0.0] * len(values)
    start = 0
    while start < len(values):
        end = start + 1
        while end < len(values) and values[ordered[end]] == values[ordered[start]]:
            end += 1
        midpoint = (start + end - 1) / 2.0
        for i in ordered[start:end]:
            ranks[i] = midpoint
        start = end
    return ranks


def _numeric_spearman(predicted, observed):
    if len(predicted) < 2:
        return None
    x, y = _midranks(predicted), _midranks(observed)
    center = (len(x) - 1) / 2.0
    xc, yc = [v - center for v in x], [v - center for v in y]
    denominator = math.sqrt(math.fsum(v * v for v in xc) * math.fsum(v * v for v in yc))
    if denominator == 0:
        return None
    return math.fsum(a * b for a, b in zip(xc, yc)) / denominator


def _load_gold(path):
    gold = _decode(Path(path).read_text(encoding="utf-8"))
    if not isinstance(gold, dict) or gold.get("status") != "ready":
        raise ValueError("organizer gold must have status ready")
    if not isinstance(gold.get("item_id"), str) or not gold["item_id"]:
        raise ValueError("organizer gold requires item_id")
    response_type, answer = gold.get("response_type"), gold.get("answer")
    if response_type == "ranking":
        if (not isinstance(answer, list) or len(answer) < 2
                or any(not isinstance(x, str) or not x for x in answer)
                or len(set(answer)) != len(answer)):
            raise ValueError("ranking gold must be a complete unique ordered ID list")
        values = gold.get("endpoint_values")
        if (not isinstance(values, dict) or set(values) != set(answer)
                or any(not _finite(x) for x in values.values())):
            raise ValueError("ranking gold requires finite endpoint values for every ID")
        if len(set(values.values())) != len(values):
            raise ValueError("strict-ranking gold cannot contain tied endpoint values")
        if answer != sorted(values, key=values.get, reverse=True):
            raise ValueError("ranking gold must order the endpoint values from largest to smallest")
    elif response_type == "positive_fraction":
        if (not isinstance(answer, dict) or not answer
                or any(not isinstance(k, str) or not k for k in answer)
                or any(not _positive_finite(x) for x in answer.values())):
            raise ValueError("fraction gold must contain positive finite values for every ID")
    else:
        raise ValueError("unsupported organizer response_type")
    return gold


def evaluate_item(prediction: Any, gold_path: Path) -> dict[str, Any]:
    gold = _load_gold(gold_path)
    report = {"item_id": gold["item_id"], "response_type": gold["response_type"],
              "score": 0.0, "status": "invalid_submission", "submission_complete": False}
    try:
        submitted = (_decode_ranking(prediction) if gold["response_type"] == "ranking"
                     else _decode(prediction))
        answer = gold["answer"]
        if gold["response_type"] == "ranking":
            if not isinstance(submitted, list):
                raise ValueError("response must be one comma-separated line or an array of molecule IDs")
            if any(not isinstance(x, str) for x in submitted):
                raise ValueError("every ranked ID must be a string")
            if len(submitted) != len(answer) or len(set(submitted)) != len(submitted):
                raise ValueError("ranking must contain every required ID exactly once")
            if set(submitted) != set(answer):
                raise ValueError("ranking has missing or unknown molecule IDs")
            rank = {molecule: i for i, molecule in enumerate(submitted)}
            squared_distance = sum((rank[molecule] - i) ** 2
                                   for i, molecule in enumerate(answer))
            n = len(answer)
            rho = 1.0 - 6.0 * squared_distance / (n * (n * n - 1))
            report.update(score=max(0.0, rho), raw_spearman=rho,
                          n_scored=n, squared_rank_distance=squared_distance,
                          score_definition="max(0, raw Spearman rho)")
        else:
            if not isinstance(submitted, dict) or set(submitted) != set(answer):
                raise ValueError("response must be a JSON object with exactly the required molecule IDs")
            if any(not _positive_finite(value) for value in submitted.values()):
                raise ValueError("every fraction must be a positive finite JSON number; booleans are invalid")
            # Subtract logs instead of dividing: finite inputs can have an
            # overflowing ratio even though both logarithms are well defined.
            errors = {key: abs(math.log(submitted[key]) - math.log(value))
                      for key, value in answer.items()}
            log_mae = math.fsum(errors.values()) / len(errors)
            rho = _numeric_spearman([submitted[key] for key in answer], list(answer.values()))
            report.update(score=math.exp(-log_mae), mean_absolute_log_error=log_mae,
                          per_molecule_absolute_log_error=errors, n_scored=len(errors),
                          raw_spearman=rho, spearman_defined=rho is not None,
                          spearman_note=("Average ranks are used for tied predictions; diagnostic only."
                                         if rho is not None else
                                         "Undefined: constant ranks or fewer than two values; numerical score is unchanged."),
                          score_definition="exp(-mean(abs(log(prediction) - log(gold))))")
        report.update(status="scored", submission_complete=True)
    except (ValueError, TypeError, OverflowError, RecursionError) as exc:
        report["error"] = str(exc)
    return report


def score_item(prediction: Any, gold_path: Path) -> float:
    return float(evaluate_item(prediction, gold_path)["score"])
