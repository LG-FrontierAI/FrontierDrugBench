"""the harness scorer for LNP-021-Molecular-Biology-design-lipid-pka-il (generation, computational proxy).

Metric specs do not apply: the package grades the designs with model tools
(QupKake basic micro-pKa + IL classifier). ``lnp_scoring.auto_prepare`` builds
the evaluator-side tool results and ``lnp_scoring.design_lib`` is the package's
legacy ``scoring_tools/score.py`` generation branch.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
TASK = HERE.parent
ROOT = HERE.parents[1] / "_packages"  # shared scorer library
sys.path.insert(0, str(ROOT))

from frontier_benchkit.lnp.auto_prepare import MolecularPending, ensure_tool_results  # noqa: E402
from frontier_benchkit.lnp.design_lib import evaluate, read  # noqa: E402

GOLD = HERE / "answer.json"


def _as_pred(prediction: Any) -> Any:
    if isinstance(prediction, str):
        try:
            return json.loads(prediction)
        except json.JSONDecodeError as exc:
            return {"_parse_error": str(exc), "_raw": prediction}
    return prediction


def score(prediction: Any):
    gold = read(GOLD)["reference"]
    pred = _as_pred(prediction)
    if not isinstance(pred, dict) or pred.get("_parse_error"):
        return {"score": 0.0, "detail": {"error": "invalid_prediction", "prediction": pred}}
    try:
        tool_file = ensure_tool_results(pred, gold, task_dir=TASK)
    except MolecularPending as exc:
        return {
            "score": 0.0,
            "detail": {
                "error": "molecular_pending",
                "message": str(exc),
                "question_id": gold.get("id"),
                "molecular_predictions_run": False,
            },
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "score": 0.0,
            "detail": {
                "error": "tool_prepare_failed",
                "message": str(exc),
                "question_id": gold.get("id"),
            },
        }
    try:
        result = evaluate(pred, gold, tool_file=tool_file)
    except (ValueError, TypeError, KeyError) as exc:
        result = {
            "question_id": gold.get("id"),
            "score": 0.0,
            "errors": [str(exc)],
            "molecular_predictions_run": False,
        }
    result = dict(result)
    result["tool_results"] = str(tool_file)
    result["molecular_predictions_run"] = True
    return {"score": float(result.get("score", 0.0)) / 100.0, "detail": result}
