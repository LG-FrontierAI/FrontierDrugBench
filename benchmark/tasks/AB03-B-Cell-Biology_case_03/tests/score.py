"""Organizer-side single-case scorer; no contestant tools are used."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1] / "_packages"  # shared scorer library
sys.path.insert(0, str(ROOT))

from frontier_benchkit.antibody.sequence_case_eval import evaluate_question  # noqa: E402

QUESTION = HERE.parent
CASE_ID = "03"


def evaluate(prediction, case_id=None, **kwargs):
    return evaluate_question(prediction, QUESTION, CASE_ID, **kwargs)


def score(prediction, case_id=None, **kwargs):
    report = evaluate(prediction, **kwargs)
    value = report.get("score")
    # Design cases stay unscored until AF3 results are frozen; the harness needs a
    # float, so keep the protocol-zero in the trace instead of raising.
    return 0.0 if value is None else float(value)
