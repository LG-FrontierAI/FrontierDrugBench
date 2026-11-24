"""Live Benchmark (prospective forecasting) scoring for the converted benchmark tasks.

The organiser reports two task-native metrics for this family and never fuses
them into a single total: ``Accuracy`` over the binary items and ``Relative
WIS`` over the numeric items (the organiser workbook, notes sheet). This
module reproduces both definitions exactly as the organiser states them.

Relative WIS
------------
For a seven-quantile forecast ``q05..q95`` and realised truth ``y``:

    IS_alpha(l, u; y) = (u - l)
                      + (2/alpha) * (l - y) * 1[y < l]
                      + (2/alpha) * (y - u) * 1[y > u]

    numerator = 0.5 * |q50 - y|
              + sum over alpha in {0.10, 0.20, 0.50} of (alpha/2) * IS_alpha

    WIS = numerator / denominator,   denominator = 0.5 + sum(alpha/2)

The organiser uses ``denominator = 3.5`` for the prospective cycle and
``denominator = 0.9`` for the retrospective cycle. The value is carried per
item in ``tests/answer.json`` (``scoring.wis_denominator``) because it is not
interchangeable: the point-reference items below carry no interval terms, so
the denominator scales the reference instead of cancelling out.

    Relative WIS = WIS(forecast) / WIS(reference)

Three reference constructions appear in this family, and each item records the
one the organiser used:

    uniform      reference quantiles are evenly spaced on the pre-declared
                 ``[lower, upper]`` support (22 items).
    point 1.0    the "HR = 1" reference, i.e. a degenerate forecast at 1.0 for
                 the five ESMO effect-size items. A degenerate forecast makes
                 every interval collapse, so the same WIS formula returns
                 exactly ``|1 - y|``.
    persistence  the previous released observation, i.e. a degenerate forecast
                 at the last pre-cutoff value (five items).

``scoring.reference_wis`` stores the resulting denominator so a score can be
reproduced without re-reading the source package. It regenerates every
organiser cell exactly.

Reported score
--------------
the harness aggregates ``score`` as a higher-is-better mean, while Relative WIS is
lower-is-better, so this module reports the affine image

    score = 1 - Relative WIS

which keeps the aggregation invertible: ``mean_score = 1 - mean(Relative WIS)``.
The exact Relative WIS is always available as ``detail["relative_wis"]``. An
invalid numeric answer falls back to ``Relative WIS = 1.0``, hence
``score = 0.0``, matching the organiser rule that unusable numeric forecasts
still occupy their slot in the fixed 32-item denominator.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

FENCE = re.compile(r"^```(?:json|text)?\s*\n?([\s\S]*?)\s*```$", re.IGNORECASE)
_NUMBER = re.compile(r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")

# alpha, index of the lower quantile, index of the upper quantile
INTERVALS = ((0.10, 0, 6), (0.20, 1, 5), (0.50, 2, 4))


def _load(tests_dir):
    path = Path(tests_dir) / "answer.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _strip_fence(value):
    text = str(value).strip()
    match = FENCE.match(text)
    return (match.group(1) if match else text).strip()


def _as_float(value):
    """First finite number in a value; permissive by design.

    Only used for the seven quantile slots, where the surrounding structure
    (exactly seven values) already rules out prose. Scalar probabilities go
    through :func:`_scalar_probability` instead, which refuses to guess.
    """
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value) if math.isfinite(float(value)) else None
    text = _strip_fence(value)
    match = _NUMBER.search(text)
    if not match:
        return None
    try:
        number = float(match.group(0))
    except ValueError:
        return None
    return number if math.isfinite(number) else None


def _scalar_probability(value):
    """One probability from a binary submission, or ``None`` if unusable.

    The prompt asks for "a single JSON number between 0 and 1", and the
    organiser rejects an object wrapper outright — ``{"prediction": 0.4}`` is
    flagged "the probability must be a finite number in [0,1]" and counted as a miss, exactly like
    an echoed response schema. So an object or array payload is not unwrapped:
    only a bare number (or a bare numeric string) is accepted.

    The ``[0, 1]`` range check happens in :func:`_binary`, where the organiser
    applies it.
    """
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value) if math.isfinite(float(value)) else None
    if isinstance(value, (dict, list, tuple)):
        return None
    text = _strip_fence(value).strip().strip("\"'").strip()
    if not text:
        return None
    tokens = _NUMBER.findall(text)
    if len(tokens) != 1:
        return None
    try:
        number = float(tokens[0])
    except ValueError:
        return None
    if not math.isfinite(number):
        return None
    # A trailing percent sign is unambiguous and commonly written by models.
    if re.search(r"\d\s*%", text):
        number /= 100.0
    return number


def _quantiles(prediction):
    """Seven quantiles from the frozen answer contract, or ``None``.

    The prompt is explicit: "Return only a JSON array of length 7 ... Do not
    include Markdown, explanations, units, or additional fields." The organiser
    enforces that literally — its format-check notes for a wrapped reply state "exactly 7 quantiles must be returned", and it scores the cell as Relative WIS = 1. Verified
    against the published per-cell scores, ``{"prediction": [...]}`` and
    ``{"0.05": ..., ...}`` are both rejected, not unwrapped. This parser
    therefore accepts only a seven-element array.

    A surrounding code fence is the one tolerated deviation: it is transport
    noise around an otherwise well-formed array and does not add or reorder
    values. Any other text before or after the array is a contract violation.
    """
    value = prediction
    if isinstance(value, str):
        text = _strip_fence(value).strip()
        start, end = text.find("["), text.rfind("]")
        if start < 0 or end <= start:
            return None
        if text[:start].strip() or text[end + 1 :].strip():
            return None
        try:
            value = json.loads(text[start : end + 1])
        except (ValueError, TypeError):
            return None
    if not isinstance(value, (list, tuple)) or len(value) != 7:
        return None
    out = []
    for item in value:
        number = _as_float(item)
        if number is None:
            return None
        out.append(number)
    return out


def _wis_numerator(quantiles, truth):
    """Weighted-interval-score numerator; the caller divides by the denominator."""
    total = 0.5 * abs(quantiles[3] - truth)
    for alpha, lower, upper in INTERVALS:
        low, high = quantiles[lower], quantiles[upper]
        interval = high - low
        if truth < low:
            interval += (2.0 / alpha) * (low - truth)
        elif truth > high:
            interval += (2.0 / alpha) * (truth - high)
        total += (alpha / 2.0) * interval
    return total


def _wis(quantiles, truth, denominator):
    return _wis_numerator(quantiles, truth) / denominator


def reference_quantiles(spec):
    """Reference quantiles for a ``uniform`` or degenerate ``point`` reference."""
    kind = str(spec.get("kind") or "").strip().lower()
    levels = spec.get("quantile_levels") or [0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95]
    if kind == "uniform":
        lower, upper = float(spec["lower"]), float(spec["upper"])
        return [lower + (upper - lower) * float(level) for level in levels]
    if kind in ("point", "persistence"):
        return [float(spec["point"])] * len(levels)
    raise ValueError(f"unknown reference kind {kind!r}")


def _binary(prediction, spec, truth):
    threshold = float(spec.get("threshold", 0.5))
    probability = _scalar_probability(prediction)
    if probability is None:
        return {
            "score": 0.0,
            "detail": {
                "metric": "Accuracy",
                "status": "invalid_submission",
                "error": "expected one finite probability in [0, 1]",
                "truth": truth,
            },
        }
    if not 0.0 <= probability <= 1.0:
        # Matches the organiser's validity rule: a finite number in [0,1].
        return {
            "score": 0.0,
            "detail": {
                "metric": "Accuracy",
                "status": "invalid_submission",
                "error": "probability outside [0, 1]",
                "probability": probability,
                "truth": truth,
            },
        }
    predicted = int(probability >= threshold)
    correct = 1.0 if predicted == int(truth) else 0.0
    return {
        "score": correct,
        "detail": {
            "metric": "Accuracy",
            "probability": probability,
            "threshold": threshold,
            "predicted_class": predicted,
            "truth": int(truth),
            "correct": bool(correct),
        },
    }


def _relative_wis(prediction, spec, truth):
    denominator = float(spec["wis_denominator"])
    reference_wis = float(spec["reference_wis"])
    if reference_wis <= 0:
        raise ValueError("reference_wis must be positive")
    reference_kind = (spec.get("reference") or {}).get("kind")
    quantiles = _quantiles(prediction)
    if quantiles is None:
        # Organiser rule: an unusable numeric forecast falls back to Relative
        # WIS = 1 and still occupies its slot in the fixed 32-item denominator.
        return {
            "score": 0.0,
            "detail": {
                "metric": "Relative WIS",
                "status": "invalid_submission",
                "error": "expected seven quantiles q05..q95",
                "relative_wis": 1.0,
                "reference_wis": reference_wis,
                "reference_kind": reference_kind,
                "fallback": "reference",
                "truth": truth,
            },
        }
    notes = []
    ordered = sorted(quantiles)
    if ordered != quantiles:
        # The frozen schema requires a nondecreasing vector. Keep the forecast
        # usable but record that ordering had to be enforced.
        notes.append("quantiles_reordered_to_nondecreasing")
        quantiles = ordered
    raw_wis = _wis(quantiles, truth, denominator)
    relative = raw_wis / reference_wis
    coverage = {
        label: bool(quantiles[lower] <= truth <= quantiles[upper])
        for label, lower, upper in (("50", 2, 4), ("80", 1, 5), ("90", 0, 6))
    }
    detail = {
        "metric": "Relative WIS",
        "relative_wis": relative,
        "raw_wis": raw_wis,
        "reference_wis": reference_wis,
        "reference_kind": reference_kind,
        "wis_denominator": denominator,
        "quantiles": quantiles,
        "q50": quantiles[3],
        "truth": truth,
        "absolute_error_q50": abs(quantiles[3] - truth),
        "interval_coverage": coverage,
        "direction": "minimize",
    }
    if notes:
        detail["notes"] = notes
    # 1 - Relative WIS keeps the harness' higher-is-better mean invertible:
    # mean_score == 1 - mean(Relative WIS).
    return {"score": 1.0 - relative, "detail": detail}


def score_case(prediction, tests_dir, **kwargs):
    payload = _load(tests_dir)
    spec = payload.get("scoring") or {}
    truth = payload.get("truth")
    if truth is None:
        # Legacy shape: truth nested inside the answer object. ``answer`` is now
        # the submission itself (a list or a number), so only look inside it
        # when it is still an object.
        answer = payload.get("answer")
        if isinstance(answer, dict):
            truth = answer.get("truth")
    if truth is None:
        raise ValueError(f"{tests_dir}: answer.json carries no truth")
    kind = str(spec.get("type") or "").strip().lower()
    if kind == "binary_accuracy":
        return _binary(prediction, spec, truth)
    if kind == "relative_wis":
        return _relative_wis(prediction, spec, float(truth))
    raise ValueError(f"{tests_dir}: unsupported scoring type {kind!r}")
