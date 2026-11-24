"""Deterministic evaluation primitives for hidden antibody assay outcomes.

The functions keep ranking, numerical error, calibration, and decision utility
separate. They are intentionally dependency-free; project-specific assay
adapters should normalize their packets into the documented row schema before
calling these functions.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Iterable


def _finite(x: Any) -> bool:
    try:
        return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(float(x))
    except (OverflowError, ValueError):
        return False


def _check_numeric_metrics(metrics: dict[str, Any]) -> dict[str, Any]:
    for key, value in metrics.items():
        if isinstance(value, (int, float)) and not isinstance(value, bool) and not _finite(value):
            raise ValueError(f'Computed metric {key} is nonfinite; review endpoint scaling')
    return metrics


def _rank(values: list[float]) -> list[float]:
    order = sorted(range(len(values)), key=lambda i: values[i])
    result = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i + 1
        while j < len(order) and values[order[j]] == values[order[i]]:
            j += 1
        r = (i + j - 1) / 2.0 + 1.0
        for k in order[i:j]:
            result[k] = r
        i = j
    return result


def spearman(actual: list[float], predicted: list[float]) -> float | None:
    if len(actual) != len(predicted) or len(actual) < 2:
        return None
    ar, pr = _rank(actual), _rank(predicted)
    am, pm = sum(ar) / len(ar), sum(pr) / len(pr)
    num = sum((a - am) * (p - pm) for a, p in zip(ar, pr))
    den_a = math.sqrt(sum((a - am) ** 2 for a in ar))
    den_p = math.sqrt(sum((p - pm) ** 2 for p in pr))
    if den_a == 0:
        return None
    if den_p == 0:
        return 0.0
    return max(-1.0, min(1.0, num / (den_a * den_p)))


def top_k_hit(actual: list[float], predicted: list[float], k: int, higher_is_better: bool) -> float | None:
    if not actual or len(actual) != len(predicted):
        return None
    if not isinstance(k, int) or isinstance(k, bool) or k < 1:
        raise ValueError("k must be a positive integer")
    if any(not _finite(v) for v in actual + predicted):
        raise ValueError("top-k inputs must be finite numbers")
    k = min(k, len(actual))
    ga, gt = _top_sets(actual, k, higher_is_better)
    pa, pt = _top_sets(predicted, k, higher_is_better)
    # Gold ties at the cutoff are interchangeable; strictly better gold rows
    # still occupy mandatory slots. Prediction ties receive the expectation
    # over uniformly selected boundary members, never a row-order advantage.
    draws, total = k - len(pa), len(pt)
    strict_hits = len(pa & ga) + draws * len(pt & ga) / total
    boundary_fixed, successes = len(pa & gt), len(pt & gt)
    capacity = k - len(ga)
    denominator = math.comb(total, draws)
    boundary_hits = 0.0
    for x in range(max(0, draws - (total-successes)), min(draws, successes)+1):
        probability = math.comb(successes, x) * math.comb(total-successes, draws-x) / denominator
        boundary_hits += probability * min(capacity, boundary_fixed+x)
    return max(0.0, min(1.0, (strict_hits + boundary_hits) / k))


def _top_sets(values: list[float], k: int, higher: bool) -> tuple[set[int], set[int]]:
    cutoff = sorted(values, reverse=higher)[k-1]
    better = {i for i, v in enumerate(values) if v > cutoff} if higher else {i for i, v in enumerate(values) if v < cutoff}
    return better, {i for i, v in enumerate(values) if v == cutoff}


def interval_coverage(actual: list[float], low: list[float], high: list[float]) -> float | None:
    if not actual or len(actual) != len(low) or len(actual) != len(high):
        return None
    if any(not _finite(v) for v in actual + low + high) or any(lo > hi for lo, hi in zip(low, high)):
        raise ValueError("Intervals require finite ordered bounds and outcomes")
    return sum(lo <= y <= hi for y, lo, hi in zip(actual, low, high)) / len(actual)


def _indexed(rows: list[dict[str, Any]], name: str) -> dict[str, dict[str, Any]]:
    if not isinstance(rows, list):
        raise ValueError(f"{name} must be a list")
    result = {}
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"].strip() or row['id'] != row['id'].strip():
            raise ValueError(f"{name}: every row needs a nonempty string id")
        if row["id"] in result:
            raise ValueError(f"{name}: duplicate id {row['id']}")
        result[row["id"]] = row
    return result


def evaluate_rows(gold_rows: list[dict[str, Any]], predictions: list[dict[str, Any]], *, outcome: str = "outcome", higher_is_better: bool = True, transform: str = "identity", interval_probability: float = 0.9, binary_event: bool = False, strictly_positive: bool = False) -> dict[str, Any]:
    """Evaluate predictions by hidden row id.

    Prediction rows require ``id`` and ``prediction``. ``lower`` and ``upper``
    are optional uncertainty bounds. Rows absent from either side are reported,
    never silently scored as zero.
    """
    gold = _indexed(gold_rows, "gold")
    supplied = _indexed(predictions, "predictions")
    if not gold or any(not _finite(r.get(outcome)) for r in gold.values()):
        raise ValueError("gold must contain finite numeric outcomes for every required id")
    if any(r.get('status', 'ready') != 'ready' for r in gold.values()):
        raise ValueError("Every gold row must be ready, without pending outcomes")
    if any(not isinstance(v, bool) for v in (higher_is_better, binary_event, strictly_positive)):
        raise ValueError("direction, binary_event and strictly_positive must be booleans")
    if set(supplied) - set(gold):
        raise ValueError("unknown prediction ids: " + ", ".join(sorted(set(supplied) - set(gold))))
    if transform not in {"identity", "log10"}:
        raise ValueError("transform must be identity or log10")
    if not _finite(interval_probability) or not 0 < interval_probability < 1:
        raise ValueError("interval_probability must lie strictly between 0 and 1")
    positive = strictly_positive or transform == 'log10'
    if binary_event and (transform != 'identity' or positive):
        raise ValueError("binary_event requires identity scale and no strict-positive constraint")
    if binary_event and any(r[outcome] not in (0, 1) for r in gold.values()):
        raise ValueError("binary-event gold must contain only 0 or 1")
    if positive and any(r[outcome] <= 0 for r in gold.values()):
        raise ValueError("strictly-positive/log10 gold outcomes must be positive")
    invalid = sorted(i for i, r in supplied.items() if not _finite(r.get("prediction")) or (positive and r["prediction"] <= 0) or (binary_event and not 0 <= r['prediction'] <= 1))
    pred = {i: r for i, r in supplied.items() if i not in invalid}
    for i, row in supplied.items():
        if "lower" in row or "upper" in row:
            if not _finite(row.get("lower")) or not _finite(row.get("upper")):
                raise ValueError(f"{i}: both interval bounds must be finite")
            if row["lower"] > row["upper"]:
                raise ValueError(f"{i}: reversed interval")
            if positive and row["lower"] <= 0:
                raise ValueError(f"{i}: strictly-positive/log10 interval bounds must be positive")
            if binary_event and not 0 <= row['lower'] <= row['upper'] <= 1:
                raise ValueError(f"{i}: probability interval must be in [0, 1]")
    ids = sorted(set(gold) & set(pred))
    scale = math.log10 if transform == "log10" else float
    y = [scale(gold[i][outcome]) for i in ids]
    p = [scale(pred[i]["prediction"]) for i in ids]
    errors = [abs(a-b) for a, b in zip(y, p)]
    if any(not _finite(error) for error in errors):
        raise ValueError('Prediction errors overflow; review endpoint scaling')
    mean_error = sum(error / len(errors) for error in errors) if errors else None
    complete = len(ids) == len(gold)
    metrics: dict[str, Any] = {
        "n_gold": len(gold), "n_pred": len(supplied), "n_scored": len(ids),
        "submission_complete": complete, "prediction_coverage": len(ids) / len(gold),
        "missing_predictions": sorted(set(gold) - set(supplied)),
        "invalid_predictions": invalid, "unknown_prediction_ids": [],
        "transform": transform,
        "strictly_positive": positive,
        "top_k_tie_policy": "interchangeable gold cutoff ties; expected credit over predicted cutoff ties",
        "spearman": spearman(y, p) if complete else None,
        "top1_hit": top_k_hit(y, p, 1, higher_is_better) if complete else 0.0,
        "top3_hit": top_k_hit(y, p, 3, higher_is_better) if complete else 0.0,
        "mae": mean_error if complete else None,
        "partial_mae_diagnostic": mean_error,
        "missing_policy": "fixed required-id denominator; incomplete submissions receive zero aggregate score",
    }
    metrics["log_mae"] = metrics["mae"] if transform == "log10" else None
    metrics["rmse"] = math.hypot(*(error/math.sqrt(len(errors)) for error in errors)) if complete else None
    bounded = [i for i in ids if _finite(pred[i].get("lower")) and _finite(pred[i].get("upper"))]
    metrics["interval_submission_coverage"] = len(bounded) / len(gold)
    metrics["interval_coverage"] = sum(pred[i]["lower"] <= gold[i][outcome] <= pred[i]["upper"] for i in bounded) / len(gold) if bounded else None
    if len(bounded) == len(gold):
        lows = [scale(pred[i]["lower"]) for i in ids]
        highs = [scale(pred[i]["upper"]) for i in ids]
        alpha = 1 - interval_probability
        metrics["mean_interval_width"] = sum(hi-lo for lo,hi in zip(lows,highs))/len(ids)
        metrics["mean_interval_score"] = sum(hi-lo + (2/alpha)*(lo-a if a<lo else a-hi if a>hi else 0) for a,lo,hi in zip(y,lows,highs))/len(ids)
    else:
        metrics["mean_interval_width"] = metrics["mean_interval_score"] = None
    if binary_event and complete:
        metrics["brier_score"] = sum((gold[i][outcome]-pred[i]["prediction"])**2 for i in ids)/len(ids)
    elif binary_event:
        metrics['brier_score'] = None
    return _check_numeric_metrics(metrics)


def selection_metrics(gold_rows: list[dict[str, Any]], selected_ids: Iterable[str], *, utility: str = "utility", budget: int | None = None, higher_is_better: bool = True) -> dict[str, Any]:
    gold = _indexed(gold_rows, "selection gold")
    if not gold or any(not _finite(r.get(utility)) for r in gold.values()):
        raise ValueError("selection gold requires finite utility for every id")
    if any(r.get('status', 'ready') != 'ready' for r in gold.values()):
        raise ValueError('Selection gold contains pending rows')
    if not isinstance(higher_is_better, bool):
        raise ValueError('higher_is_better must be a boolean')
    if isinstance(selected_ids, (str, bytes, dict)) or selected_ids is None:
        raise ValueError('selected_ids must be an iterable of string ids')
    selected = list(selected_ids)
    if any(not isinstance(x, str) or not x or x != x.strip() for x in selected):
        raise ValueError('Every selected id must be a nonempty canonical string')
    if len(set(selected)) != len(selected):
        raise ValueError("duplicate selected ids")
    if not isinstance(budget, int) or isinstance(budget, bool) or not 1 <= budget <= len(gold):
        raise ValueError("A frozen positive integer budget within the gold pool is required")
    if len(selected) > budget:
        raise ValueError("selection exceeds frozen budget")
    valid = [x for x in selected if x in gold]
    missing = [x for x in selected if x not in gold]
    if missing:
        raise ValueError("unknown selected ids: " + ", ".join(missing))
    best = sorted(gold, key=lambda x: gold[x][utility], reverse=higher_is_better)
    k = budget
    missing_slots = k - len(valid)
    try:
        optimal = math.fsum(float(gold[x][utility]) for x in best[:k])
        obtained = math.fsum([float(gold[x][utility]) for x in valid] +
                             [float(gold[best[-1]][utility])] * missing_slots)
    except OverflowError as error:
        raise ValueError('Computed selection utility is nonfinite; review endpoint scaling') from error
    regret = max(0.0, (optimal - obtained) if higher_is_better else (obtained - optimal))
    values = [float(gold[x][utility]) for x in gold]
    mandatory, tied = _top_sets(values, k, higher_is_better)
    chosen = {i for i, x in enumerate(gold) if x in valid}
    credit = len(chosen & mandatory) + min(k-len(mandatory), len(chosen & tied))
    return _check_numeric_metrics({
        "status": "scored", "selected": selected, "valid_selected": valid,
        "submission_complete": len(valid) == budget, "budget": budget,
        "missing": missing, "unfilled_budget_slots": missing_slots, "top1_hit": bool(valid and gold[valid[0]][utility] == gold[best[0]][utility]),
        "contains_optimal_item": any(gold[x][utility] == gold[best[0]][utility] for x in valid),
        "topk_recall": credit / k,
        "top1_policy": "first submitted selection; any gold item tied for best receives credit",
        "utility": obtained, "oracle_utility": optimal, "regret": regret,
    })


def score_pending_guard(item_id: str, gold_path: Path) -> float:
    """Prevent a pending question from being mistaken for a zero-score item."""
    if not gold_path.exists():
        raise RuntimeError(f"{item_id}: hidden gold is not installed")
    data = json.loads(gold_path.read_text(encoding="utf-8"))
    if data.get("status") != "ready":
        raise RuntimeError(f"{item_id}: hidden gold status is {data.get('status', 'missing')}")
    raise RuntimeError(f"{item_id}: item-specific scoring adapter has not been generated")
