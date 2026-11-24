"""Organizer-side rubric scorer; a judge is mandatory (LLM_* from the harness)."""
from pathlib import Path
import importlib.util
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1] / "_packages" / "frontier_benchkit" / "clinical_inquiry"

# Content-hashed module name: the path, not the package name, decides the copy.
_NAME = "frontier_rubric_eval_d39bd70c"
if _NAME not in sys.modules:
    _spec = importlib.util.spec_from_file_location(_NAME, ROOT / "rubric_eval.py")
    _module = importlib.util.module_from_spec(_spec)
    sys.modules[_NAME] = _module
    _spec.loader.exec_module(_module)
score_case = sys.modules[_NAME].score_case


def evaluate(prediction, case_id=None, **kwargs):
    return score_case(prediction, HERE, **kwargs)


def score(prediction, case_id=None, **kwargs):
    return float(evaluate(prediction, **kwargs)["score"])
