"""Offline case scoring for the exported structure benchmark."""

import math

import numpy as np


# Source: analyse_ca/evaluate_ca_predictions.py

LDDT_THRESHOLDS = (0.5, 1.0, 2.0, 4.0)


def validate_prediction(result, sequence):
    sequence_length = len(sequence)
    if result is None:
        return None, "missing_prediction"
    if not isinstance(result, list):
        return None, "result_is_not_an_array"
    if len(result) != sequence_length:
        return None, f"expected_{sequence_length}_residues_found_{len(result)}"

    coordinates = []
    required_fields = {"residue_index", "residue_name", "ca"}
    for expected_index, item in enumerate(result, 1):
        if not isinstance(item, dict):
            return None, f"residue_{expected_index}_is_not_an_object"
        if set(item) != required_fields:
            return None, f"residue_{expected_index}_has_invalid_fields"
        residue_index = item["residue_index"]
        if (
            isinstance(residue_index, bool)
            or not isinstance(residue_index, int)
            or residue_index != expected_index
        ):
            return None, f"invalid_residue_index_at_position_{expected_index}"
        if item["residue_name"] != sequence[expected_index - 1]:
            return None, f"residue_name_mismatch_at_position_{expected_index}"
        coordinate = item["ca"]
        if not isinstance(coordinate, list) or len(coordinate) != 3:
            return None, f"invalid_ca_shape_at_position_{expected_index}"
        if any(
            isinstance(value, bool) or not isinstance(value, (int, float))
            for value in coordinate
        ):
            return None, f"nonnumeric_ca_at_position_{expected_index}"
        if not all(math.isfinite(float(value)) for value in coordinate):
            return None, f"nonfinite_ca_at_position_{expected_index}"
        coordinates.append([float(value) for value in coordinate])
    return np.asarray(coordinates, dtype=np.float64), ""


def sequence_match_statistics(result, sequence):
    """Count exact, index-aware residue matches independently of XYZ validity.

    Each reference position can match at most once. Missing positions and
    incorrect residue names remain unmatched; extra, duplicate, malformed, or
    out-of-range output objects are counted as nonmatching model outputs.
    """
    sequence_length = len(sequence)
    if not isinstance(result, list):
        return {
            "model_sequence_length": 0,
            "sequence_match_count": 0,
            "sequence_match_rate": 0.0,
            "sequence_unmatched_expected_count": sequence_length,
            "sequence_nonmatching_output_count": 0,
        }

    matched_positions = set()
    for item in result:
        if not isinstance(item, dict):
            continue
        residue_index = item.get("residue_index")
        residue_name = item.get("residue_name")
        if (
            isinstance(residue_index, bool)
            or not isinstance(residue_index, int)
            or not 1 <= residue_index <= sequence_length
            or residue_index in matched_positions
            or residue_name != sequence[residue_index - 1]
        ):
            continue
        matched_positions.add(residue_index)

    match_count = len(matched_positions)
    return {
        "model_sequence_length": len(result),
        "sequence_match_count": match_count,
        "sequence_match_rate": match_count / sequence_length if sequence_length else 0.0,
        "sequence_unmatched_expected_count": sequence_length - match_count,
        "sequence_nonmatching_output_count": len(result) - match_count,
    }


def lddt_ca(predicted, gold, cutoff=15.0):
    gold_distances = np.linalg.norm(gold[:, None, :] - gold[None, :, :], axis=-1)
    predicted_distances = np.linalg.norm(
        predicted[:, None, :] - predicted[None, :, :], axis=-1
    )
    pair_mask = np.triu(
        (gold_distances < cutoff) & (gold_distances > 0.0), k=1
    )
    pair_count = int(pair_mask.sum())
    if pair_count == 0:
        return 0.0, {threshold: 0.0 for threshold in LDDT_THRESHOLDS}, 0
    errors = np.abs(predicted_distances[pair_mask] - gold_distances[pair_mask])
    fractions = {
        threshold: float(np.mean(errors < threshold))
        for threshold in LDDT_THRESHOLDS
    }
    return float(np.mean(list(fractions.values()))), fractions, pair_count


def kabsch_align(mobile, target, weights=None):
    if weights is None:
        weights = np.ones(len(mobile), dtype=np.float64)
    weights = np.asarray(weights, dtype=np.float64)
    weights = weights / weights.sum()
    mobile_center = np.sum(mobile * weights[:, None], axis=0)
    target_center = np.sum(target * weights[:, None], axis=0)
    mobile_centered = mobile - mobile_center
    target_centered = target - target_center
    covariance = (mobile_centered * weights[:, None]).T @ target_centered
    left, _, right_transposed = np.linalg.svd(covariance)
    if np.linalg.det(left @ right_transposed) < 0:
        left[:, -1] *= -1
    rotation = left @ right_transposed
    return mobile_centered @ rotation + target_center


def tm_score_fixed_correspondence(predicted, gold, iterations=20):
    length = len(gold)
    if length < 2:
        return 0.0
    d0 = 0.5 if length <= 15 else max(
        0.5, 1.24 * ((length - 15) ** (1.0 / 3.0)) - 1.8
    )
    weights = np.ones(length, dtype=np.float64)
    best_score = 0.0
    for _ in range(iterations):
        aligned = kabsch_align(predicted, gold, weights)
        distances = np.linalg.norm(aligned - gold, axis=1)
        terms = 1.0 / (1.0 + (distances / d0) ** 2)
        score = float(np.mean(terms))
        best_score = max(best_score, score)
        new_weights = terms * terms
        if np.allclose(new_weights, weights, rtol=1e-5, atol=1e-7):
            break
        weights = new_weights
    return best_score


def evaluate_target(gold_record, prediction):
    sequence_length = gold_record["sequence_length"]
    sequence_statistics = sequence_match_statistics(
        prediction, gold_record["sequence"]
    )
    try:
        predicted_ca_count = len(prediction) if prediction is not None else 0
    except TypeError:
        predicted_ca_count = 0
    predicted_all, prediction_error = validate_prediction(
        prediction, gold_record["sequence"]
    )
    base = {
        "target_id": gold_record["target_id"],
        "pdb_id": gold_record["pdb_id"],
        "assembly_id": gold_record["assembly_id"],
        "chain_id": gold_record["chain_id"],
        "entity_id": gold_record["entity_id"],
        "sequence_length": sequence_length,
        "gold_ca_count": gold_record["gold_ca_count"],
        "gold_ca_coverage": gold_record["gold_ca_coverage"],
        "predicted_ca_count": predicted_ca_count,
        "prediction_complete": not prediction_error,
        **sequence_statistics,
        "lddt_ca": 0.0,
        "lddt_p0_5": 0.0,
        "lddt_p1": 0.0,
        "lddt_p2": 0.0,
        "lddt_p4": 0.0,
        "lddt_pair_count": 0,
        "tm_score": 0.0,
        "ca_rmsd": "",
        "error": prediction_error,
    }
    if prediction_error:
        return base

    mask = np.array(
        [coordinate is not None for coordinate in gold_record["gold_ca"]],
        dtype=bool,
    )
    gold = np.asarray(
        [coordinate for coordinate in gold_record["gold_ca"] if coordinate is not None],
        dtype=np.float64,
    )
    predicted = predicted_all[mask]
    lddt, fractions, pair_count = lddt_ca(predicted, gold)
    aligned = kabsch_align(predicted, gold)
    rmsd = float(np.sqrt(np.mean(np.sum((aligned - gold) ** 2, axis=1))))
    base.update(
        {
            "lddt_ca": lddt,
            "lddt_p0_5": fractions[0.5],
            "lddt_p1": fractions[1.0],
            "lddt_p2": fractions[2.0],
            "lddt_p4": fractions[4.0],
            "lddt_pair_count": pair_count,
            "tm_score": tm_score_fixed_correspondence(predicted, gold),
            "ca_rmsd": rmsd,
            "error": "",
        }
    )
    return base
