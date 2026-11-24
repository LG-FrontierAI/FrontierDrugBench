"""Organizer-side T3 pocket-induce scorer; no contestant tools are used.

Input: a JSON response with `pockets` (PL) or `epitopes` (AbAg).
Output: best-candidate F1 as `score`; Top-1 and best-candidate precision,
recall, F1 and Jaccard are also reported.
"""

from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from frontier_benchkit.structure.induce import evaluate_case  # noqa: E402

CASE_ID = "09"


def evaluate(prediction, case_id=None, **kwargs):
    if case_id not in (None, CASE_ID, f"case-{CASE_ID}"):
        raise ValueError(f"unexpected case_id: {case_id}")
    return evaluate_case(prediction, HERE, CASE_ID)


def score(prediction, case_id=None, **kwargs):
    return float(evaluate(prediction, case_id=case_id, **kwargs)["score"])


if __name__ == "__main__":
    from frontier_benchkit.structure.cli import main

    main(evaluate, HERE, CASE_ID)
