"""Organizer-side single-case scorer; AF3 mean ranking_score."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1] / "_packages"  # shared scorer library
sys.path.insert(0, str(ROOT))

from frontier_benchkit.antibody.af3_mean_design import evaluate_af3_mean  # noqa: E402

QUESTION = HERE.parent
CASE_ID = "07"


def evaluate(prediction, case_id=None, **kwargs):
    return evaluate_af3_mean(prediction, QUESTION, CASE_ID, **kwargs)


def score(prediction, case_id=None, **kwargs):
    return float(evaluate(prediction, **kwargs)["score"])
