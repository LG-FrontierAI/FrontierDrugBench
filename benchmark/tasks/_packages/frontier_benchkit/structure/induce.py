"""Offline case scoring for the exported structure benchmark."""

import csv
import json
from pathlib import Path
from typing import Any

from .induce_pl import metrics_for_pockets, validate_output as validate_pl_output
from .response import resolve_prediction


# Source: analyse_pocket_induce/run_abag_benchmark.py

def validate_output(
    payload: Any, antigen_lengths: dict[str, int]
) -> list[dict[str, Any]]:
    if not isinstance(payload, dict) or set(payload) != {"epitopes"}:
        raise ValueError("top-level JSON must contain exactly the key 'epitopes'")
    epitopes = payload["epitopes"]
    if not isinstance(epitopes, list):
        raise ValueError("epitopes must be an array")
    if len(epitopes) > 20:
        raise ValueError(
            f"epitopes contains {len(epitopes)} candidates; maximum is 20"
        )

    normalized = []
    expected_ids = set(antigen_lengths)
    for index, epitope in enumerate(epitopes, 1):
        if not isinstance(epitope, dict) or set(epitope) != {"rank", "entities"}:
            raise ValueError(
                f"epitope {index} must contain exactly rank and entities"
            )
        if type(epitope["rank"]) is not int or epitope["rank"] != index:
            raise ValueError(f"epitope {index} has a non-consecutive rank")
        entities = epitope["entities"]
        if not isinstance(entities, dict):
            raise ValueError(f"epitope {index} entities must be an object")
        if set(entities) != expected_ids:
            missing = sorted(expected_ids - set(entities))
            unexpected = sorted(set(entities) - expected_ids)
            raise ValueError(
                f"epitope {index} entity IDs do not match antigen input; "
                f"missing={missing}, unexpected={unexpected}"
            )

        normalized_entities: dict[str, list[int]] = {}
        residue_count = 0
        for entity_id in antigen_lengths:
            positions = entities[entity_id]
            if not isinstance(positions, list):
                raise ValueError(
                    f"epitope {index} entity {entity_id} positions must be an array"
                )
            if any(type(position) is not int for position in positions):
                raise ValueError(
                    f"epitope {index} entity {entity_id} has a non-integer position"
                )
            if positions != sorted(set(positions)):
                raise ValueError(
                    f"epitope {index} entity {entity_id} positions must be unique "
                    "and ascending"
                )
            invalid = [
                position
                for position in positions
                if position < 1 or position > antigen_lengths[entity_id]
            ]
            if invalid:
                raise ValueError(
                    f"epitope {index} entity {entity_id} has out-of-range "
                    f"positions: {invalid}"
                )
            normalized_entities[entity_id] = positions
            residue_count += len(positions)
        if residue_count == 0:
            raise ValueError(f"epitope {index} must contain at least one residue")
        normalized.append({"rank": index, "entities": normalized_entities})
    return normalized


def residue_pairs(mapping: dict[str, list[int]]) -> set[tuple[str, int]]:
    return {
        (str(entity_id), position)
        for entity_id, positions in mapping.items()
        for position in positions
    }


def candidate_metrics(
    predicted: dict[str, list[int]], gold: dict[str, list[int]]
) -> dict[str, Any]:
    predicted_set = residue_pairs(predicted)
    gold_set = residue_pairs(gold)
    true_positive = len(predicted_set & gold_set)
    union = len(predicted_set | gold_set)
    precision = true_positive / len(predicted_set) if predicted_set else 0.0
    recall = true_positive / len(gold_set) if gold_set else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall
        else 0.0
    )
    return {
        "predicted_count": len(predicted_set),
        "true_positive_count": true_positive,
        "precision": round(precision, 6),
        "recall": round(recall, 6),
        "f1": round(f1, 6),
        "jaccard": round(true_positive / union if union else 0.0, 6),
    }


def metrics_for_epitopes(
    epitopes: list[dict[str, Any]], gold: dict[str, list[int]]
) -> tuple[dict[str, Any], dict[str, Any], list[dict[str, Any]]]:
    ranked = [
        {"rank": epitope["rank"], **candidate_metrics(epitope["entities"], gold)}
        for epitope in epitopes
    ]
    empty_metrics = candidate_metrics({}, gold)
    top1 = ranked[0] if ranked else {"rank": "", **empty_metrics}
    best = (
        max(ranked, key=lambda item: (item["f1"], -item["rank"]))
        if ranked
        else {"rank": "", **empty_metrics}
    )
    return top1, best, ranked


# Source: analyse_pocket_induce/score_exported_case.py



METRIC_NAMES = ("precision", "recall", "f1", "jaccard")


def evaluate_case(prediction, question_dir: Path, case_id: str):
    """Return best-candidate F1 and Top-1/best diagnostic metrics."""
    with (question_dir / "input" / f"case_{case_id}.csv").open(
        newline="", encoding="utf-8"
    ) as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 1 or rows[0]["name"] != f"case_{case_id}":
        raise ValueError("invalid case input CSV")
    row = rows[0]
    antigen = json.loads(row["antigen_sequences"])
    antibody = json.loads(row["antibody_sequences"])
    if len(antigen) != int(row["antigen_entity_count"]) or len(antibody) != int(row["antibody_entity_count"]):
        raise ValueError("input entity count mismatch")
    for role, entities in (("antigen", antigen), ("antibody", antibody)):
        if json.loads(row[f"{role}_entity_ids"]) != [entity["entity_id"] for entity in entities]:
            raise ValueError(f"{role} entity ID mismatch")
        if any(entity["length"] != len(entity["sequence"]) for entity in entities):
            raise ValueError(f"{role} sequence length mismatch")

    payload = json.loads((question_dir / "test" / "answer.json").read_text(encoding="utf-8"))
    if payload["case_id"] != f"case-{case_id}":
        raise ValueError("answer case ID mismatch")
    answer = payload["answer"]
    gold = answer["binding_site"]["entities"]
    lengths = {entity["entity_id"]: entity["length"] for entity in antigen}
    if set(gold) != set(lengths):
        raise ValueError("answer antigen entity IDs do not match input")

    if payload["item_id"] == "Pocket-Induce-PL":
        if len(antigen) != 1 or antibody or not row["ligand_smiles"] or int(row["ligand_heavy_atom_count"]) <= 0:
            raise ValueError("invalid PL input")
        prediction = resolve_prediction(prediction, lambda value: validate_pl_output(value, antigen[0]["length"]))
        try:
            normalized = validate_pl_output(prediction, antigen[0]["length"])
            error = ""
        except ValueError as exc:
            normalized = []
            error = str(exc)
        top1, best, _ = metrics_for_pockets(normalized, gold[antigen[0]["entity_id"]])
    elif payload["item_id"] == "Pocket-Induce-AbAg":
        if not antibody or row["ligand_smiles"] or int(row["ligand_heavy_atom_count"]) != 0:
            raise ValueError("invalid AbAg input")
        prediction = resolve_prediction(prediction, lambda value: validate_output(value, lengths))
        try:
            normalized = validate_output(prediction, lengths)
            error = ""
        except ValueError as exc:
            normalized = []
            error = str(exc)
        top1, best, _ = metrics_for_epitopes(normalized, gold)
    else:
        raise ValueError("unsupported pocket-induce item ID")

    return {
        "score": float(best["f1"]),
        "metrics": {
            "correct_residue_count": len(residue_pairs(gold)),
            "best_true_positive_count": best["true_positive_count"],
            "top1": {name: top1[name] for name in METRIC_NAMES},
            "best_candidate": {name: best[name] for name in METRIC_NAMES},
        },
        "error": error,
    }
