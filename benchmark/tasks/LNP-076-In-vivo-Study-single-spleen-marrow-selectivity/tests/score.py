"""the harness scorer for LNP-076-In-vivo-Study-single-spleen-marrow-selectivity (evidence_single).

The reference lives in ``tests/answer.json["reference"]``: metric keys, weights
and expected values are declared there, so the prompt and the grader cannot
drift apart. ``lnp_scoring.score_lib`` is the package's
``scoring_tools/score_expanded.py`` (scoring v2) vendored unchanged.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1] / "_packages"  # shared scorer library
sys.path.insert(0, str(ROOT))

from frontier_benchkit.lnp.score_lib import evaluate, read  # noqa: E402

GOLD = HERE / "answer.json"


def _as_pred(prediction: Any) -> Any:
    if isinstance(prediction, str):
        try:
            return json.loads(prediction)
        except json.JSONDecodeError as exc:
            return {"_parse_error": str(exc), "_raw": prediction}
    return prediction


def _turns(prediction: Any) -> dict:
    """Accept the T1-T4 object directly or a wrapped ``turns`` map."""
    if not isinstance(prediction, dict):
        return {}
    if any(key in prediction for key in ("T1", "T2", "T3", "T4")):
        return prediction
    nested = prediction.get("turns")
    return nested if isinstance(nested, dict) else {}


def score(prediction: Any):
    gold = read(GOLD)["reference"]
    pred = _as_pred(prediction)
    if not isinstance(pred, dict) or pred.get("_parse_error"):
        return {"score": 0.0, "detail": {"error": "invalid_prediction", "prediction": pred}}
    if gold.get("mode") == "evidence_followup":
        result = evaluate(pred, gold, _turns(pred))
    else:
        result = evaluate(pred, gold)
    return {"score": float(result.get("score", 0.0)) / 100.0, "detail": result}
