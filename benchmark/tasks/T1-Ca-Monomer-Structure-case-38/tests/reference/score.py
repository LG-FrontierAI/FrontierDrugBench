"""Organizer-side single-case scorer; no contestant tools are used.

Input: the model's JSON response, ``{"result": [...]}``.
Output: a report whose ``score`` is lDDT-Cα (0 to 1). The report also
contains output validity, sequence match rate, TM-score, and aligned Cα RMSD.
Requires NumPy.
"""

import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from frontier_benchkit.structure.ca import evaluate_target, validate_prediction  # noqa: E402
from frontier_benchkit.structure.response import RawReply, resolve_prediction  # noqa: E402

CASE_ID = "38"


def evaluate(prediction, case_id=None, **kwargs):
    """Return the single-case score and diagnostic evaluation metrics."""
    if case_id not in (None, CASE_ID, f"case-{CASE_ID}"):
        raise ValueError(f"unexpected case_id: {case_id}")
    with (HERE / "input" / "case_38.csv").open(newline="", encoding="utf-8") as handle:
        input_row = next(csv.DictReader(handle))
    sequence = input_row["sequence"]
    if int(input_row["length"]) != len(sequence):
        raise ValueError("input sequence length mismatch")

    answer = json.loads((HERE / "test" / "answer.json").read_text(encoding="utf-8"))
    gold_ca = answer["answer"]
    if len(gold_ca) != len(sequence):
        raise ValueError("answer length mismatch")
    observed_count = sum(point is not None for point in gold_ca)
    gold_record = {
        "target_id": f"case-{CASE_ID}",
        "pdb_id": f"case-{CASE_ID}",
        "assembly_id": "",
        "chain_id": "",
        "entity_id": "",
        "sequence": sequence,
        "sequence_length": len(sequence),
        "gold_ca_count": observed_count,
        "gold_ca_coverage": observed_count / len(sequence),
        "gold_ca": gold_ca,
    }
    def validate_payload(payload):
        if set(payload) != {"result"}:
            raise ValueError("model JSON must contain exactly one top-level key: result")
        _, error = validate_prediction(payload["result"], sequence)
        if error:
            raise ValueError(error)

    parsed = resolve_prediction(prediction, validate_payload)
    if isinstance(prediction, RawReply) and set(parsed) != {"result"}:
        raise ValueError("model JSON must contain exactly one top-level key: result")
    result = parsed.get("result") if isinstance(parsed, dict) else parsed
    metrics = evaluate_target(gold_record, result)
    return {
        "score": float(metrics["lddt_ca"]),
        "metrics": {
            "prediction_complete": metrics["prediction_complete"],
            "sequence_match_rate": metrics["sequence_match_rate"],
            "lddt_ca": metrics["lddt_ca"],
            "lddt_p0_5": metrics["lddt_p0_5"],
            "lddt_p1": metrics["lddt_p1"],
            "lddt_p2": metrics["lddt_p2"],
            "lddt_p4": metrics["lddt_p4"],
            "tm_score": metrics["tm_score"],
            "ca_rmsd": metrics["ca_rmsd"],
            "gold_ca_coverage": metrics["gold_ca_coverage"],
        },
        "error": metrics["error"],
    }


def score(prediction, case_id=None, **kwargs):
    """Return the primary lDDT-Cα score as a float."""
    return evaluate(prediction, case_id=case_id, **kwargs)["score"]


if __name__ == "__main__":
    from frontier_benchkit.structure.cli import main

    main(evaluate, HERE, CASE_ID)
