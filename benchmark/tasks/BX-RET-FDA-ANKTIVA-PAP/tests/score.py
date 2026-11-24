"""Organizer-side single-case scorer; no contestant tools are used."""
from pathlib import Path
import importlib.util
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1] / "_packages" / "frontier_benchkit" / "live_forecast"

# Load the shared implementation by path under a content-hashed name.
# The path, not ``frontier_benchkit.common``, keeps this scorer pinned to the
# copy shipped beside it when several benchmark trees share one process.
_NAME = "frontier_forecast_eval_f2cc6bac"
if _NAME not in sys.modules:
    _spec = importlib.util.spec_from_file_location(_NAME, ROOT / "forecast_eval.py")
    _module = importlib.util.module_from_spec(_spec)
    sys.modules[_NAME] = _module
    _spec.loader.exec_module(_module)
score_case = sys.modules[_NAME].score_case


def evaluate(prediction, case_id=None, **kwargs):
    return score_case(prediction, HERE, **kwargs)


def score(prediction, case_id=None, **kwargs):
    return float(evaluate(prediction, **kwargs)["score"])
