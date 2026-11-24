"""Offline case scoring for the exported structure benchmark."""

import csv
import json
from pathlib import Path
from typing import Any

from .response import resolve_prediction


# Source: analyse_pocket/run_pocket_benchmark.py

def validate_model_output(payload: Any, target: dict[str, Any]) -> list[dict[str, Any]]:
    complex_type = target["complex_type"]
    output_key = "pockets" if complex_type == "PL" else "epitopes"
    if not isinstance(payload, dict) or set(payload) != {output_key}:
        raise ValueError(f"top-level JSON must contain exactly the key {output_key!r}")
    sites = payload[output_key]
    if not isinstance(sites, list):
        raise ValueError(f"{output_key} must be an array")
    normalized = []
    expected_keys = (
        {"rank", "residues"}
        if complex_type == "PL"
        else {"rank", "protein_id", "residues"}
    )
    lengths_by_protein = {
        protein["protein_id"]: protein["sequence_length"]
        for protein in target["proteins"]
    }
    seen_sites = set()
    for index, site in enumerate(sites, 1):
        label = "pocket" if complex_type == "PL" else "epitope"
        if not isinstance(site, dict) or set(site) != expected_keys:
            required = ", ".join(sorted(expected_keys))
            raise ValueError(
                f"{label} {index} must contain exactly these keys: {required}"
            )
        if type(site["rank"]) is not int or site["rank"] != index:
            raise ValueError(f"{label} {index} has a non-consecutive rank")
        protein_id = "protein_1" if complex_type == "PL" else site.get("protein_id")
        if protein_id not in lengths_by_protein:
            raise ValueError(
                f"{label} {index} has an unknown protein_id: {protein_id!r}"
            )
        residues = site["residues"]
        if not isinstance(residues, list) or not residues:
            raise ValueError(f"{label} {index} residues must be a nonempty array")
        if any(type(position) is not int for position in residues):
            raise ValueError(f"{label} {index} contains a non-integer position")
        if residues != sorted(set(residues)):
            raise ValueError(f"{label} {index} residues must be unique and ascending")
        invalid = [
            position
            for position in residues
            if not 1 <= position <= lengths_by_protein[protein_id]
        ]
        if invalid:
            raise ValueError(f"{label} {index} has out-of-range positions: {invalid}")
        site_key = (protein_id, *residues)
        if site_key in seen_sites:
            raise ValueError(f"{label} {index} duplicates an earlier prediction")
        seen_sites.add(site_key)
        normalized.append(
            {"rank": index, "protein_id": protein_id, "residues": residues}
        )
    return normalized


def maximum_weight_assignment(weights: list[list[float]]) -> list[tuple[int, int]]:
    """Return a maximum-weight one-to-one assignment using Hungarian O(n^3)."""
    row_count = len(weights)
    column_count = len(weights[0]) if row_count else 0
    size = max(row_count, column_count)
    if size == 0:
        return []
    padded = [
        [
            weights[row][column] if row < row_count and column < column_count else 0.0
            for column in range(size)
        ]
        for row in range(size)
    ]
    maximum = max((value for row in padded for value in row), default=0.0)
    costs = [[maximum - value for value in row] for row in padded]

    u = [0.0] * (size + 1)
    v = [0.0] * (size + 1)
    p = [0] * (size + 1)
    way = [0] * (size + 1)
    for row in range(1, size + 1):
        p[0] = row
        column0 = 0
        minimum = [float("inf")] * (size + 1)
        used = [False] * (size + 1)
        while True:
            used[column0] = True
            row0 = p[column0]
            delta = float("inf")
            column1 = 0
            for column in range(1, size + 1):
                if used[column]:
                    continue
                current = costs[row0 - 1][column - 1] - u[row0] - v[column]
                if current < minimum[column]:
                    minimum[column] = current
                    way[column] = column0
                if minimum[column] < delta:
                    delta = minimum[column]
                    column1 = column
            for column in range(size + 1):
                if used[column]:
                    u[p[column]] += delta
                    v[column] -= delta
                else:
                    minimum[column] -= delta
            column0 = column1
            if p[column0] == 0:
                break
        while True:
            column1 = way[column0]
            p[column0] = p[column1]
            column0 = column1
            if column0 == 0:
                break
    assignment = []
    for column in range(1, size + 1):
        row = p[column] - 1
        predicted = column - 1
        if row < row_count and predicted < column_count:
            assignment.append((row, predicted))
    return sorted(assignment)


def residue_micro_metrics(
    predicted_sites: list[dict[str, Any]], gold_sites: list[dict[str, Any]]
) -> dict[str, Any]:
    """Pool residue counts after the benchmark's one-to-one assignment."""
    predicted = [{(site["protein_id"], residue) for residue in site["residues"]}
                 for site in predicted_sites]
    gold = [{(site["protein_id"], residue) for residue in site["residues"]}
            for site in gold_sites]
    overlaps = [[len(reference & candidate) for candidate in predicted] for reference in gold]
    weights = []
    for reference, counts in zip(gold, overlaps):
        row = []
        for candidate, count in zip(predicted, counts):
            precision = count / len(candidate) if candidate else 0.0
            recall = count / len(reference) if reference else 0.0
            row.append(2 * precision * recall / (precision + recall) if precision + recall else 0.0)
        weights.append(row)
    true_positive = sum(overlaps[row][column] for row, column in maximum_weight_assignment(weights))
    total_predicted = sum(map(len, predicted))
    total_gold = sum(map(len, gold))
    micro_precision = true_positive / total_predicted if total_predicted else 0.0
    micro_recall = true_positive / total_gold if total_gold else 0.0
    micro_f1 = (
        2 * micro_precision * micro_recall / (micro_precision + micro_recall)
        if micro_precision + micro_recall
        else 0.0
    )
    micro_union = total_predicted + total_gold - true_positive
    return {
        "micro_true_positive_count": true_positive,
        "micro_predicted_residue_count": total_predicted,
        "micro_correct_residue_count": total_gold,
        "micro_precision": micro_precision,
        "micro_recall": micro_recall,
        "micro_f1": micro_f1,
        "micro_jaccard": true_positive / micro_union if micro_union else 0.0,
    }


# Source: analyse_pocket/score_exported_case.py



def evaluate_case(prediction, question_dir: Path, case_id: str):
    """Return post-2026 residue micro-F1 and auxiliary residue metrics."""
    with (question_dir / "input" / f"case_{case_id}.csv").open(
        newline="", encoding="utf-8"
    ) as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 1 or rows[0]["name"] != f"case_{case_id}":
        raise ValueError("invalid case input CSV")
    row = rows[0]
    antigen = json.loads(row["antigen_sequences"])
    if len(antigen) != int(row["antigen_entity_count"]):
        raise ValueError("antigen entity count mismatch")
    if json.loads(row["antigen_entity_ids"]) != [item["entity_id"] for item in antigen]:
        raise ValueError("antigen entity IDs mismatch")
    if (
        json.loads(row["antibody_entity_ids"]) != []
        or int(row["antibody_entity_count"]) != 0
        or json.loads(row["antibody_sequences"]) != []
    ):
        raise ValueError("T2 pocket questions must not contain antibody sequences")
    proteins = []
    for item in antigen:
        if len(item["sequence"]) != item["length"]:
            raise ValueError("antigen sequence length mismatch")
        proteins.append(
            {
                "protein_id": item["protein_id"],
                "sequence_length": item["length"],
            }
        )

    payload = json.loads((question_dir / "test" / "answer.json").read_text(encoding="utf-8"))
    if payload["case_id"] != f"case-{case_id}":
        raise ValueError("answer case ID mismatch")
    answer = payload["answer"]
    entity_to_protein = {item["entity_id"]: item["protein_id"] for item in antigen}
    for collection in ("post_2026_sites", "historical_sites", "combined_scoring_sites"):
        for site in answer[collection]:
            if entity_to_protein.get(site["entity_id"]) != site["protein_id"]:
                raise ValueError(f"{collection} entity ID does not match input")

    if payload["item_id"] not in {"Pocket-PL", "Pocket-AbAg"}:
        raise ValueError("unsupported pocket item ID")
    complex_type = "PL" if payload["item_id"] == "Pocket-PL" else "ABAG"
    target = {"complex_type": complex_type, "proteins": proteins}
    prediction = resolve_prediction(prediction, lambda value: validate_model_output(value, target))
    try:
        normalized = validate_model_output(prediction, target)
        error = ""
    except ValueError as exc:
        normalized = []
        error = str(exc)

    post = residue_micro_metrics(normalized, answer["post_2026_sites"])
    combined = residue_micro_metrics(normalized, answer["combined_scoring_sites"])
    return {
        "score": float(post["micro_f1"]),
        "metrics": {"post_2026": post, "combined": combined},
        "error": error,
    }
