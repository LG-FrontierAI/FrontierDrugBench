"""Offline case scoring for the exported structure benchmark."""

from __future__ import annotations

import csv
import json
import math
from functools import lru_cache
from pathlib import Path
from typing import Any

import numpy as np

from .response import resolve_prediction


# Source: analyse_docking/evaluate_docking_predictions.py

LDDT_THRESHOLDS = (0.5, 1.0, 2.0, 4.0)


DEFAULT_COMPLEX_CUTOFF = 15.0


DEFAULT_INTERFACE_CUTOFF = 15.0


DOCKQ_CA_CONTACT_CUTOFF = 8.0


DOCKQ_CA_INTERFACE_CUTOFF = 10.0


DOCKQ_CA_IRMSD_SCALE = 1.5


DOCKQ_CA_LRMSD_SCALE = 8.5


def _coordinate_array(
    value: Any,
    expected_ids: list[Any],
    label: str,
    *,
    allow_legacy_coordinates: bool,
) -> np.ndarray:
    if not isinstance(value, list):
        raise ValueError(f"{label} must be an array")
    expected_length = len(expected_ids)
    if len(value) != expected_length:
        raise ValueError(
            f"{label} expected {expected_length} coordinates, found {len(value)}"
        )
    coordinates = []
    for index, (entry, expected_id) in enumerate(zip(value, expected_ids), 1):
        if not isinstance(entry, list):
            raise ValueError(f"{label} entry {index} must be an array")
        if len(entry) == 4:
            actual_id = entry[0]
            identifiers_match = (
                not isinstance(actual_id, bool)
                and type(actual_id) is type(expected_id)
                and actual_id == expected_id
            )
            if not identifiers_match:
                raise ValueError(
                    f"{label} entry {index} expected identifier {expected_id!r}, "
                    f"found {actual_id!r}"
                )
            coordinate = entry[1:]
        elif allow_legacy_coordinates and len(entry) == 3:
            coordinate = entry
        else:
            raise ValueError(
                f"{label} entry {index} must be [identifier, x, y, z]"
            )
        if any(
            isinstance(component, bool)
            or not isinstance(component, (int, float))
            for component in coordinate
        ):
            raise ValueError(f"{label} coordinate {index} is not numeric")
        converted = [float(component) for component in coordinate]
        if not all(math.isfinite(component) for component in converted):
            raise ValueError(f"{label} coordinate {index} is not finite")
        coordinates.append(converted)
    return np.asarray(coordinates, dtype=np.float64)


def validate_prediction(
    payload: Any,
    entry: dict[str, Any],
    task: str,
    *,
    allow_legacy_coordinates: bool = False,
) -> dict[str, dict[str, np.ndarray]]:
    """Validate the exact prompt contract and return normalized arrays."""
    expected_top = {"protein", "ligand"} if task == "pl" else {"antigen", "antibody"}
    if not isinstance(payload, dict) or set(payload) != expected_top:
        raise ValueError(f"top-level JSON must contain exactly {sorted(expected_top)}")

    normalized: dict[str, dict[str, np.ndarray]] = {}
    for role in expected_top:
        predicted_role = payload[role]
        gold_role = entry.get(role)
        if not isinstance(predicted_role, dict):
            raise ValueError(f"{role} must be an object")
        if not isinstance(gold_role, dict) or not gold_role:
            raise ValueError(f"ground truth has no {role} records")
        if set(predicted_role) != set(gold_role):
            missing = sorted(set(gold_role) - set(predicted_role))
            unexpected = sorted(set(predicted_role) - set(gold_role))
            raise ValueError(
                f"{role} IDs do not match input; missing={missing}, "
                f"unexpected={unexpected}"
            )
        normalized[role] = {}
        for object_id, gold_record in gold_role.items():
            if role == "ligand":
                expected_ids = list(gold_record.get("atom_ids", []))
            else:
                expected_length = int(gold_record.get("sequence_length", 0))
                expected_ids = list(range(1, expected_length + 1))
            if not expected_ids:
                raise ValueError(f"ground truth {role}.{object_id} is empty")
            normalized[role][object_id] = _coordinate_array(
                predicted_role[object_id],
                expected_ids,
                f"{role}.{object_id}",
                allow_legacy_coordinates=allow_legacy_coordinates,
            )
    return normalized


def _gold_arrays(record: dict[str, Any], role: str) -> tuple[np.ndarray, np.ndarray]:
    coordinate_key = "coordinates" if role == "ligand" else "ca_coordinates"
    mask_key = "atom_mask" if role == "ligand" else "ca_mask"
    raw_coordinates = record.get(coordinate_key)
    raw_mask = record.get(mask_key)
    if not isinstance(raw_coordinates, list) or not isinstance(raw_mask, list):
        raise ValueError(f"ground truth {role} coordinates or mask is missing")
    if len(raw_coordinates) != len(raw_mask):
        raise ValueError(f"ground truth {role} coordinate/mask length mismatch")
    coordinates = np.zeros((len(raw_coordinates), 3), dtype=np.float64)
    mask = np.asarray(raw_mask, dtype=bool)
    for index, (coordinate, valid) in enumerate(zip(raw_coordinates, mask)):
        if not valid:
            continue
        if not isinstance(coordinate, list) or len(coordinate) != 3:
            raise ValueError(f"valid ground-truth {role} coordinate is malformed")
        converted = np.asarray(coordinate, dtype=np.float64)
        if not np.all(np.isfinite(converted)):
            raise ValueError(f"valid ground-truth {role} coordinate is nonfinite")
        coordinates[index] = converted
    return coordinates, mask


def _flatten_role(
    entry: dict[str, Any],
    prediction: dict[str, dict[str, np.ndarray]],
    role: str,
    chain_mapping: dict[str, str] | None = None,
    atom_permutations: dict[str, tuple[int, ...]] | None = None,
) -> tuple[np.ndarray, np.ndarray, list[tuple[str, int]]]:
    gold_parts = []
    predicted_parts = []
    identities = []
    for object_id, record in entry[role].items():
        gold, mask = _gold_arrays(record, role)
        predicted_id = (chain_mapping or {}).get(object_id, object_id)
        predicted = prediction[role][predicted_id]
        permutation = (atom_permutations or {}).get(object_id)
        if permutation is not None:
            predicted = predicted[np.asarray(permutation, dtype=int)]
        if len(predicted) != len(gold):
            raise ValueError(f"mapped {role}.{object_id} length mismatch")
        valid_indices = np.flatnonzero(mask)
        gold_parts.append(gold[valid_indices])
        predicted_parts.append(predicted[valid_indices])
        identities.extend((object_id, int(index) + 1) for index in valid_indices)
    if not gold_parts:
        return np.empty((0, 3)), np.empty((0, 3)), []
    return np.vstack(gold_parts), np.vstack(predicted_parts), identities


def _kabsch_transform(mobile: np.ndarray, target: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    if len(mobile) != len(target) or len(mobile) < 3:
        raise ValueError("reference requires at least three corresponding points")
    mobile_center = mobile.mean(axis=0)
    target_center = target.mean(axis=0)
    mobile_centered = mobile - mobile_center
    target_centered = target - target_center
    if np.linalg.matrix_rank(mobile_centered) < 2:
        raise ValueError("reference points cannot uniquely determine a 3D rotation")
    covariance = mobile_centered.T @ target_centered
    left, _, right_transposed = np.linalg.svd(covariance)
    rotation = left @ right_transposed
    if np.linalg.det(rotation) < 0:
        left[:, -1] *= -1
        rotation = left @ right_transposed
    translation = target_center - mobile_center @ rotation
    return rotation, translation


def _lddt_from_errors(errors: np.ndarray) -> tuple[float | None, dict[str, float | None]]:
    if errors.size == 0:
        return None, {str(threshold): None for threshold in LDDT_THRESHOLDS}
    fractions = {
        str(threshold): float(np.mean(errors < threshold))
        for threshold in LDDT_THRESHOLDS
    }
    return float(np.mean(list(fractions.values()))), fractions


def _pair_errors(
    gold: np.ndarray, predicted: np.ndarray, cutoff: float
) -> tuple[np.ndarray, int]:
    gold_distances = np.linalg.norm(gold[:, None, :] - gold[None, :, :], axis=-1)
    predicted_distances = np.linalg.norm(
        predicted[:, None, :] - predicted[None, :, :], axis=-1
    )
    pair_mask = np.triu(gold_distances < cutoff, k=1)
    return np.abs(predicted_distances[pair_mask] - gold_distances[pair_mask]), int(
        pair_mask.sum()
    )


def _cross_pair_errors(
    gold_a: np.ndarray,
    predicted_a: np.ndarray,
    gold_b: np.ndarray,
    predicted_b: np.ndarray,
    cutoff: float,
) -> tuple[np.ndarray, int]:
    gold_distances = np.linalg.norm(gold_a[:, None, :] - gold_b[None, :, :], axis=-1)
    predicted_distances = np.linalg.norm(
        predicted_a[:, None, :] - predicted_b[None, :, :], axis=-1
    )
    pair_mask = gold_distances < cutoff
    return np.abs(predicted_distances[pair_mask] - gold_distances[pair_mask]), int(
        pair_mask.sum()
    )


def _dockq_ca(
    gold_a: np.ndarray,
    predicted_a: np.ndarray,
    gold_b: np.ndarray,
    predicted_b: np.ndarray,
    ligand_rmsd: float,
) -> dict[str, Any]:
    """C-alpha-only DockQ analogue for the complete antigen/antibody assembly.

    Native contacts are C-alpha pairs, not the heavy-atom contacts of standard
    DockQ. The interface RMSD is fitted on the union of native interface C-alpha
    residues; ligand RMSD reuses antibody pose RMSD after antigen alignment.
    """
    gold_distances = np.linalg.norm(
        gold_a[:, None, :] - gold_b[None, :, :], axis=-1
    )
    predicted_distances = np.linalg.norm(
        predicted_a[:, None, :] - predicted_b[None, :, :], axis=-1
    )
    native_contacts = gold_distances < DOCKQ_CA_CONTACT_CUTOFF
    native_contact_count = int(native_contacts.sum())
    recovered_contact_count = int(
        np.count_nonzero(native_contacts & (predicted_distances < DOCKQ_CA_CONTACT_CUTOFF))
    )
    interface_pairs = gold_distances < DOCKQ_CA_INTERFACE_CUTOFF
    interface_a = np.any(interface_pairs, axis=1)
    interface_b = np.any(interface_pairs, axis=0)
    interface_residue_count = int(interface_a.sum() + interface_b.sum())
    result = {
        "dockq_ca": None,
        "dockq_ca_fnat": None,
        "dockq_ca_irmsd": None,
        "dockq_ca_lrmsd": ligand_rmsd,
        "dockq_ca_native_contact_count": native_contact_count,
        "dockq_ca_recovered_contact_count": recovered_contact_count,
        "dockq_ca_interface_residue_count": interface_residue_count,
        "dockq_ca_unscorable_reason": "",
    }
    if native_contact_count == 0:
        result["dockq_ca_unscorable_reason"] = "no_native_ca_contacts"
        return result
    if interface_residue_count < 3:
        result["dockq_ca_unscorable_reason"] = "insufficient_native_interface_ca"
        return result

    gold_interface = np.vstack((gold_a[interface_a], gold_b[interface_b]))
    predicted_interface = np.vstack(
        (predicted_a[interface_a], predicted_b[interface_b])
    )
    try:
        rotation, translation = _kabsch_transform(
            predicted_interface, gold_interface
        )
    except ValueError as exc:
        result["dockq_ca_unscorable_reason"] = str(exc)
        return result
    aligned_interface = predicted_interface @ rotation + translation
    irmsd = float(
        np.sqrt(np.mean(np.sum((aligned_interface - gold_interface) ** 2, axis=1)))
    )
    fnat = recovered_contact_count / native_contact_count
    result.update(
        {
            "dockq_ca": (
                fnat
                + 1.0 / (1.0 + (irmsd / DOCKQ_CA_IRMSD_SCALE) ** 2)
                + 1.0 / (1.0 + (ligand_rmsd / DOCKQ_CA_LRMSD_SCALE) ** 2)
            )
            / 3.0,
            "dockq_ca_fnat": fnat,
            "dockq_ca_irmsd": irmsd,
        }
    )
    return result


def _atom_signatures(record: dict[str, Any]) -> tuple[list[tuple[Any, ...]], dict[tuple[int, int], tuple[str, str]]]:
    atom_ids = list(record.get("atom_ids", []))
    elements = list(record.get("elements", []))
    if len(atom_ids) != len(elements):
        raise ValueError("ligand atom_ids/elements length mismatch")
    id_to_index = {int(atom_id): index for index, atom_id in enumerate(atom_ids)}
    atom_metadata = {
        int(item["atom_id"]): (
            bool(item.get("aromatic", False)),
            str(item.get("stereo", "")),
        )
        for item in record.get("coordinate_mapping", [])
        if isinstance(item, dict) and "atom_id" in item
    }
    edges: dict[tuple[int, int], tuple[str, str]] = {}
    neighbors: list[list[tuple[int, tuple[str, str]]]] = [[] for _ in atom_ids]
    for bond in record.get("bonds", []):
        first = id_to_index[int(bond["atom_id_1"])]
        second = id_to_index[int(bond["atom_id_2"])]
        label = (str(bond.get("order", "")), str(bond.get("stereo", "")))
        edges[tuple(sorted((first, second)))] = label
        neighbors[first].append((second, label))
        neighbors[second].append((first, label))
    signatures = []
    for index, element in enumerate(elements):
        local = sorted((elements[neighbor], label) for neighbor, label in neighbors[index])
        metadata = atom_metadata.get(int(atom_ids[index]), (False, ""))
        signatures.append(
            (str(element), metadata, len(neighbors[index]), tuple(local))
        )
    return signatures, edges


def ligand_automorphisms(
    record: dict[str, Any], max_automorphisms: int = 10000
) -> list[tuple[int, ...]]:
    """Enumerate graph automorphisms preserving element, bond order and stereo."""
    signatures, edges = _atom_signatures(record)
    size = len(signatures)
    candidates = [
        [other for other in range(size) if signatures[other] == signatures[index]]
        for index in range(size)
    ]
    order = sorted(range(size), key=lambda index: (len(candidates[index]), index))
    mapping = [-1] * size
    used: set[int] = set()
    results: list[tuple[int, ...]] = []

    def compatible(source: int, target: int) -> bool:
        for assigned_source, assigned_target in enumerate(mapping):
            if assigned_target < 0:
                continue
            source_edge = edges.get(tuple(sorted((source, assigned_source))))
            target_edge = edges.get(tuple(sorted((target, assigned_target))))
            if source_edge != target_edge:
                return False
        return True

    def search(depth: int) -> None:
        if len(results) >= max_automorphisms:
            raise ValueError(
                f"ligand has more than {max_automorphisms} graph automorphisms"
            )
        if depth == size:
            results.append(tuple(mapping))
            return
        source = order[depth]
        for target in candidates[source]:
            if target in used or not compatible(source, target):
                continue
            mapping[source] = target
            used.add(target)
            search(depth + 1)
            used.remove(target)
            mapping[source] = -1

    search(0)
    return results or [tuple(range(size))]


def _best_ligand_permutations(
    entry: dict[str, Any],
    prediction: dict[str, dict[str, np.ndarray]],
    rotation: np.ndarray,
    translation: np.ndarray,
) -> tuple[dict[str, tuple[int, ...]], int]:
    selected: dict[str, tuple[int, ...]] = {}
    total_automorphisms = 0
    for ligand_id, record in entry["ligand"].items():
        gold, mask = _gold_arrays(record, "ligand")
        automorphisms = ligand_automorphisms(record)
        total_automorphisms += len(automorphisms)
        best = None
        for permutation in automorphisms:
            predicted = prediction["ligand"][ligand_id][np.asarray(permutation)]
            aligned = predicted @ rotation + translation
            squared_error = float(np.sum((aligned[mask] - gold[mask]) ** 2))
            candidate = (squared_error, permutation)
            if best is None or candidate < best:
                best = candidate
        assert best is not None
        selected[ligand_id] = best[1]
    return selected, total_automorphisms


def _minimum_assignment(costs: np.ndarray) -> tuple[int, ...]:
    """Solve a small square assignment problem without a SciPy dependency."""
    size = len(costs)
    if costs.shape != (size, size):
        raise ValueError("assignment cost matrix must be square")

    @lru_cache(maxsize=None)
    def solve(row: int, used_mask: int) -> tuple[float, tuple[int, ...]]:
        if row == size:
            return 0.0, ()
        best: tuple[float, tuple[int, ...]] | None = None
        for column in range(size):
            if used_mask & (1 << column):
                continue
            tail_cost, tail = solve(row + 1, used_mask | (1 << column))
            candidate = (float(costs[row, column]) + tail_cost, (column,) + tail)
            if best is None or candidate < best:
                best = candidate
        assert best is not None
        return best

    return solve(0, 0)[1]


def _antibody_unit_groups(entry: dict[str, Any]) -> list[list[tuple[str, ...]]]:
    """Group exchangeable antibody binding units while preserving H/L pairing."""
    pairs = entry.get("antibody_pairs", {})
    if not isinstance(pairs, dict):
        return []
    by_signature: dict[tuple[tuple[str, str], ...], list[tuple[str, ...]]] = {}
    for pair in pairs.values():
        if not isinstance(pair, dict):
            continue
        labelled = []
        for role in ("heavy", "light"):
            for chain_id in pair.get(role, []):
                sequence = entry["antibody"][chain_id]["sequence"]
                labelled.append((role, sequence, chain_id))
        labelled.sort()
        signature = tuple((role, sequence) for role, sequence, _ in labelled)
        members = tuple(chain_id for _, _, chain_id in labelled)
        by_signature.setdefault(signature, []).append(members)
    return [sorted(units) for units in by_signature.values() if len(units) > 1]


def _chain_mapping_groups(entry: dict[str, Any], task: str) -> list[list[tuple[str, ...]]]:
    equivalence = entry.get("equivalence", {})
    groups: list[list[tuple[str, ...]]] = []
    key = "protein_chain_groups" if task == "pl" else "antigen_chain_groups"
    for group in equivalence.get(key, []):
        if len(group) > 1:
            groups.append([(chain_id,) for chain_id in sorted(group)])
    if task == "abag":
        groups.extend(_antibody_unit_groups(entry))
    return groups


def _chain_cost(
    entry: dict[str, Any],
    prediction: dict[str, dict[str, np.ndarray]],
    role: str,
    gold_chain_id: str,
    predicted_chain_id: str,
    rotation: np.ndarray,
    translation: np.ndarray,
) -> float:
    gold, mask = _gold_arrays(entry[role][gold_chain_id], role)
    predicted = prediction[role][predicted_chain_id]
    aligned = predicted @ rotation + translation
    if not np.any(mask):
        return 0.0
    return float(np.sum((aligned[mask] - gold[mask]) ** 2))


def _chain_role(task: str, chain_id: str) -> str:
    if task == "pl":
        return "protein"
    return "antigen" if chain_id.startswith("AG") else "antibody"


def _mapping_alignment_arrays(
    entry: dict[str, Any],
    prediction: dict[str, dict[str, np.ndarray]],
    task: str,
    mapping: dict[str, str],
) -> tuple[np.ndarray, np.ndarray]:
    roles = ("protein", "ligand") if task == "pl" else ("antigen", "antibody")
    gold_parts = []
    predicted_parts = []
    for role in roles:
        gold, predicted, _ = _flatten_role(
            entry, prediction, role, chain_mapping=mapping
        )
        gold_parts.append(gold)
        predicted_parts.append(predicted)
    return np.vstack(gold_parts), np.vstack(predicted_parts)


def _equivalent_chain_mapping(
    entry: dict[str, Any],
    prediction: dict[str, dict[str, np.ndarray]],
    task: str,
    max_iterations: int = 20,
) -> tuple[dict[str, str], int]:
    """Choose one assembly-aware chain mapping shared by all three metrics.

    Exchangeable PL protein and antigen chains are assigned as individual
    chains. Exchangeable antibodies are assigned as whole heavy/light binding
    units, so independent permutations cannot break pairing relationships.
    """
    roles = ("protein",) if task == "pl" else ("antigen", "antibody")
    mapping = {
        chain_id: chain_id for role in roles for chain_id in entry[role]
    }
    groups = _chain_mapping_groups(entry, task)
    if not groups:
        return mapping, 0

    for iteration in range(1, max_iterations + 1):
        gold_all, predicted_all = _mapping_alignment_arrays(
            entry, prediction, task, mapping
        )
        rotation, translation = _kabsch_transform(predicted_all, gold_all)
        updated = dict(mapping)
        for units in groups:
            size = len(units)
            costs = np.zeros((size, size), dtype=np.float64)
            for gold_index, gold_unit in enumerate(units):
                for predicted_index, predicted_unit in enumerate(units):
                    if len(gold_unit) != len(predicted_unit):
                        costs[gold_index, predicted_index] = float("inf")
                        continue
                    costs[gold_index, predicted_index] = sum(
                        _chain_cost(
                            entry,
                            prediction,
                            _chain_role(task, gold_chain_id),
                            gold_chain_id,
                            predicted_chain_id,
                            rotation,
                            translation,
                        )
                        for gold_chain_id, predicted_chain_id in zip(
                            gold_unit, predicted_unit
                        )
                    )
            assignment = _minimum_assignment(costs)
            for gold_index, predicted_index in enumerate(assignment):
                for gold_chain_id, predicted_chain_id in zip(
                    units[gold_index], units[predicted_index]
                ):
                    updated[gold_chain_id] = predicted_chain_id
        if updated == mapping:
            return mapping, iteration
        mapping = updated
    return mapping, max_iterations


def evaluate_prediction(
    entry: dict[str, Any],
    prediction: dict[str, dict[str, np.ndarray]],
    task: str,
    complex_cutoff: float = DEFAULT_COMPLEX_CUTOFF,
    interface_cutoff: float = DEFAULT_INTERFACE_CUTOFF,
) -> dict[str, Any]:
    if task == "pl":
        role_a, role_b = "protein", "ligand"
    elif task == "abag":
        role_a, role_b = "antigen", "antibody"
    else:
        raise ValueError(f"unsupported docking task: {task}")

    chain_mapping, chain_mapping_iterations = _equivalent_chain_mapping(
        entry, prediction, task
    )
    gold_a, predicted_a, _ = _flatten_role(
        entry, prediction, role_a, chain_mapping=chain_mapping
    )
    if len(gold_a) < 3:
        raise ValueError("Partner A has fewer than three valid GT coordinates")
    rotation, translation = _kabsch_transform(predicted_a, gold_a)

    atom_permutations: dict[str, tuple[int, ...]] = {}
    automorphism_count = 0
    if task == "pl":
        atom_permutations, automorphism_count = _best_ligand_permutations(
            entry, prediction, rotation, translation
        )
    gold_b, predicted_b, _ = _flatten_role(
        entry,
        prediction,
        role_b,
        chain_mapping=chain_mapping,
        atom_permutations=atom_permutations,
    )
    if len(gold_b) == 0:
        raise ValueError("Partner B has no valid GT coordinates")

    gold_all = np.vstack((gold_a, gold_b))
    predicted_all = np.vstack((predicted_a, predicted_b))
    complex_errors, complex_pair_count = _pair_errors(
        gold_all, predicted_all, complex_cutoff
    )
    complex_lddt, complex_fractions = _lddt_from_errors(complex_errors)

    interface_errors, interface_pair_count = _cross_pair_errors(
        gold_a,
        predicted_a,
        gold_b,
        predicted_b,
        interface_cutoff,
    )
    interface_lddt, interface_fractions = _lddt_from_errors(interface_errors)

    _, aa_pair_count = _pair_errors(gold_a, predicted_a, complex_cutoff)
    _, bb_pair_count = _pair_errors(gold_b, predicted_b, complex_cutoff)
    _, ab_pair_count = _cross_pair_errors(
        gold_a, predicted_a, gold_b, predicted_b, complex_cutoff
    )
    aligned_b = predicted_b @ rotation + translation
    binding_pose_rmsd = float(np.sqrt(np.mean(np.sum((aligned_b - gold_b) ** 2, axis=1))))
    dockq_ca_metrics = (
        _dockq_ca(gold_a, predicted_a, gold_b, predicted_b, binding_pose_rmsd)
        if task == "abag"
        else {}
    )

    unscorable = []
    if complex_lddt is None:
        unscorable.append("empty_complex_pair_set")
    if interface_lddt is None:
        unscorable.append("empty_interface_pair_set")

    return {
        "complex_lddt": complex_lddt,
        "interface_lddt": interface_lddt,
        "binding_pose_rmsd": binding_pose_rmsd,
        **dockq_ca_metrics,
        "complex_pair_count": complex_pair_count,
        "interface_pair_count": interface_pair_count,
        "aa_pair_count": aa_pair_count,
        "bb_pair_count": bb_pair_count,
        "ab_pair_count": ab_pair_count,
        "partner_a_valid_count": len(gold_a),
        "partner_b_valid_count": len(gold_b),
        "complex_threshold_fractions": complex_fractions,
        "interface_threshold_fractions": interface_fractions,
        "ligand_automorphism_count": automorphism_count,
        "identity_mapping_policy": (
            "assembly_aware_equivalent_chain_assignment_and_best_ligand_graph_automorphism"
        ),
        "chain_mapping_iterations": chain_mapping_iterations,
        "unscorable_reasons": unscorable,
    }


# Source: analyse_docking/score_exported_case.py



METRIC_NAMES = (
    "complex_lddt",
    "interface_lddt",
    "binding_pose_rmsd",
    "dockq_ca",
    "dockq_ca_fnat",
    "dockq_ca_irmsd",
    "dockq_ca_lrmsd",
    "dockq_ca_unscorable_reason",
)


def evaluate_case(prediction, question_dir: Path, case_id: str):
    """Return AbAg C-alpha DockQ or PL interface lDDT as the primary score."""
    with (question_dir / "input" / f"case_{case_id}.csv").open(
        newline="", encoding="utf-8"
    ) as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 1 or rows[0]["name"] != f"case_{case_id}":
        raise ValueError("invalid case input CSV")
    row = rows[0]
    payload = json.loads((question_dir / "test" / "answer.json").read_text(encoding="utf-8"))
    if payload["case_id"] != f"case-{case_id}":
        raise ValueError("answer case ID mismatch")
    if payload["item_id"] == "Docking-PL":
        task = "pl"
        roles = ("protein", "ligand")
    elif payload["item_id"] == "Docking-AbAg":
        task = "abag"
        roles = ("antigen", "antibody")
    else:
        raise ValueError("unsupported docking item ID")
    answer = payload["answer"]
    entry = {role: answer[role] for role in roles}
    entry["equivalence"] = answer["equivalence"]
    if task == "abag":
        entry["antibody_pairs"] = answer["antibody_pairs"]

    def attach_sequences(column, role):
        groups = json.loads(row[column + "_sequences"])
        ids = json.loads(row[column + "_entity_ids"])
        if len(groups) != int(row[column + "_entity_count"]) or ids != [g["entity_id"] for g in groups]:
            raise ValueError(f"{column} entity count or ID mismatch")
        seen_chains = set()
        for group in groups:
            if len(group["sequence"]) != group["length"]:
                raise ValueError(f"{column} sequence length mismatch")
            for chain_id in group["chain_ids"]:
                if chain_id in seen_chains or chain_id not in entry[role]:
                    raise ValueError(f"{column} chain ID mismatch")
                seen_chains.add(chain_id)
                entry[role][chain_id]["sequence"] = group["sequence"]
                entry[role][chain_id]["sequence_length"] = group["length"]
        if seen_chains != set(entry[role]):
            raise ValueError(f"{column} chain set mismatch")

    attach_sequences("antigen", "protein" if task == "pl" else "antigen")
    if task == "abag":
        attach_sequences("antibody", "antibody")
        if row["ligand_smiles"] or int(row["ligand_heavy_atom_count"]) != 0:
            raise ValueError("AbAg input has unexpected ligand data")
    else:
        if json.loads(row["antibody_entity_ids"]) != [] or int(row["antibody_entity_count"]) != 0:
            raise ValueError("PL input has unexpected antibody data")
        if len(entry["ligand"]) != 1:
            raise ValueError("expected one PL ligand")
        ligand = next(iter(entry["ligand"].values()))
        if len(ligand["atom_ids"]) != int(row["ligand_heavy_atom_count"]) or not row["ligand_smiles"]:
            raise ValueError("ligand heavy-atom count or SMILES mismatch")

    prediction = resolve_prediction(prediction, lambda value: validate_prediction(value, entry, task))
    try:
        normalized = validate_prediction(prediction, entry, task)
        metrics = evaluate_prediction(entry, normalized, task)
        if task == "abag":
            score = metrics["dockq_ca"]
            error = metrics["dockq_ca_unscorable_reason"]
        else:
            score = metrics["interface_lddt"]
            error = "empty_interface_pair_set" if score is None else ""
    except (ValueError, KeyError, TypeError) as exc:
        metrics = {}
        score = None
        error = str(exc)
    return {
        "score": float(score) if score is not None and not error else 0.0,
        "metrics": {
            **{name: metrics[name] for name in METRIC_NAMES if name in metrics},
            **({"unscorable_reasons": ";".join(metrics["unscorable_reasons"])} if metrics else {}),
        },
        "error": error,
    }
