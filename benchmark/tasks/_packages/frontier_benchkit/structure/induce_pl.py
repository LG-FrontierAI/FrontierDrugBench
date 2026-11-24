"""Offline case scoring for the exported structure benchmark."""

from typing import Any


# Source: analyse_pocket_induce/test_pl_prompt.py

def validate_output(payload: Any, sequence_length: int) -> list[dict[str, Any]]:
    if not isinstance(payload, dict) or set(payload) != {"pockets"}:
        raise ValueError("top-level JSON must contain exactly the key 'pockets'")
    pockets = payload["pockets"]
    if not isinstance(pockets, list):
        raise ValueError("pockets must be an array")
    if len(pockets) > 20:
        raise ValueError(f"pockets contains {len(pockets)} candidates; maximum is 20")

    used_positions = set()
    normalized = []
    for index, pocket in enumerate(pockets, 1):
        if not isinstance(pocket, dict) or set(pocket) != {"rank", "residues"}:
            raise ValueError(
                f"pocket {index} must contain exactly rank and residues"
            )
        if type(pocket["rank"]) is not int or pocket["rank"] != index:
            raise ValueError(f"pocket {index} has a non-consecutive rank")
        residues = pocket["residues"]
        if not isinstance(residues, list) or not residues:
            raise ValueError(f"pocket {index} residues must be a nonempty array")
        if any(type(position) is not int for position in residues):
            raise ValueError(f"pocket {index} contains a non-integer position")
        if residues != sorted(set(residues)):
            raise ValueError(
                f"pocket {index} residue positions must be unique and ascending"
            )
        invalid = [
            position for position in residues if position < 1 or position > sequence_length
        ]
        if invalid:
            raise ValueError(f"pocket {index} has out-of-range positions: {invalid}")
        overlap = used_positions & set(residues)
        if overlap:
            raise ValueError(
                f"pocket {index} overlaps earlier candidates at {sorted(overlap)}"
            )
        used_positions.update(residues)
        normalized.append({"rank": index, "residues": residues})
    return normalized


def candidate_metrics(predicted: list[int], gold: list[int]) -> dict[str, Any]:
    predicted_set = set(predicted)
    gold_set = set(gold)
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
        "gold_count": len(gold_set),
        "true_positive_count": true_positive,
        "precision": round(precision, 6),
        "recall": round(recall, 6),
        "f1": round(f1, 6),
        "jaccard": round(true_positive / union if union else 0.0, 6),
    }


# Source: analyse_pocket_induce/run_pl_benchmark.py

def metrics_for_pockets(
    pockets: list[dict[str, Any]], gold: list[int]
) -> tuple[dict[str, Any], dict[str, Any], Any]:
    ranked = [
        {"rank": pocket["rank"], **candidate_metrics(pocket["residues"], gold)}
        for pocket in pockets
    ]
    empty = candidate_metrics([], gold)
    top1 = ranked[0] if ranked else {"rank": "", **empty}
    best = (
        max(
            ranked,
            key=lambda item: (
                item["f1"],
                -item["rank"],
            ),
        )
        if ranked
        else {"rank": "", **empty}
    )
    return top1, best, ranked
