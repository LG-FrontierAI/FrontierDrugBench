"""Objective, independent-case scoring for sequence prediction/design tasks.

Organizer gold is validated before parsing submissions. Synthetic scores are
always labelled as fixtures. A missing frozen external evaluator never becomes
a fabricated design-quality score.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import re
from pathlib import Path
from typing import Any

AA = "ACDEFGHIKLMNPQRSTVWY"
DATA_STATUSES = {"synthetic_fixture", "patent_experimental", "internal_experimental"}


def _unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON key: " + key)
        result[key] = value
    return result


def _constant(value):
    raise ValueError("Nonfinite JSON constant: " + value)


def _decode(value):
    return json.loads(value, object_pairs_hook=_unique, parse_constant=_constant) if isinstance(value, str) else value


def _finite(value):
    try:
        return type(value) in (int, float) and math.isfinite(value)
    except OverflowError:
        return False


def normalize_case_id(value):
    if not isinstance(value, str):
        raise ValueError("Case ID must be text")
    match = re.fullmatch(r"(?:case_)?(0?[1-9]|[1-9][0-9]*)", value)
    if not match:
        raise ValueError("Invalid case ID")
    return "case_" + str(int(match[1])).zfill(2)


def _ranks(values):
    order = sorted(range(len(values)), key=values.__getitem__)
    result = [0.0] * len(values)
    start = 0
    while start < len(values):
        end = start + 1
        while end < len(values) and values[order[start]] == values[order[end]]:
            end += 1
        for index in order[start:end]:
            result[index] = (start + end - 1) / 2
        start = end
    return result


def _correlation(x, y):
    mx, my = math.fsum(x) / len(x), math.fsum(y) / len(y)
    dx, dy = [v - mx for v in x], [v - my for v in y]
    denominator = math.sqrt(math.fsum(v*v for v in dx) * math.fsum(v*v for v in dy))
    if not denominator:
        return None
    return min(1.0, max(-1.0, math.fsum(a*b for a, b in zip(dx, dy)) / denominator))


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def _ranking_gold(value):
    """Validate frozen ranking policy before any contestant answer is parsed.

    ``ranking_metric`` defaults to ``spearman``. Figure-derived endpoints may
    instead freeze ``resolvable_pair_concordance`` with ``resolvable_pairs``
    containing directed {winner, loser} objects. Optional
    ``digitization_intervals`` maps every target ID to [lower, upper]; these
    are digitization bounds, not biological confidence intervals. Strictly
    separated marginal bounds or an explicit positive paired-difference bound
    can support a scored pair. The latter preserves shared-control covariance.
    The scorer never derives or
    changes the frozen pair set based on the contestant's answer.
    """
    ids, truth = value["target_ids"], value["truth"]
    higher = value["higher_is_better"]
    metric = value.get("ranking_metric", "spearman")
    if not isinstance(metric, str) or metric not in {"spearman", "resolvable_pair_concordance"}:
        raise ValueError("Organizer ranking_metric is unsupported")
    if metric == "spearman":
        if any(k in value for k in ("resolvable_pairs", "digitization_intervals", "pairwise_difference_intervals")):
            raise ValueError("Organizer pair fields require resolvable_pair_concordance")
        return
    pairs = value.get("resolvable_pairs")
    if not isinstance(pairs, list) or not pairs:
        raise ValueError("Organizer must freeze at least one resolvable pair")
    intervals = value.get("digitization_intervals")
    if intervals is not None:
        if not isinstance(intervals, dict) or set(intervals) != set(ids):
            raise ValueError("Organizer digitization intervals must cover every target ID")
        for name, bounds in intervals.items():
            if not isinstance(bounds, list) or len(bounds) != 2 or any(not _finite(x) for x in bounds):
                raise ValueError("Organizer digitization intervals require two finite bounds")
            if not bounds[0] <= truth[name] <= bounds[1]:
                raise ValueError("Organizer digitization bounds must enclose each central truth")
    seen, outgoing = set(), {name: [] for name in ids}
    indegree = dict.fromkeys(ids, 0)
    for pair in pairs:
        if not isinstance(pair, dict) or set(pair) != {"winner", "loser"}:
            raise ValueError("Organizer pair must contain exactly winner and loser")
        winner, loser = pair["winner"], pair["loser"]
        if not isinstance(winner, str) or not isinstance(loser, str) or winner not in truth or loser not in truth or winner == loser:
            raise ValueError("Organizer pair requires two distinct target IDs")
        key = frozenset((winner, loser))
        if key in seen:
            raise ValueError("Organizer pairs must not repeat or reverse an existing pair")
        seen.add(key)
        outgoing[winner].append(loser)
        indegree[loser] += 1
    available = [name for name in ids if not indegree[name]]
    visited = 0
    while available:
        name = available.pop()
        visited += 1
        for loser in outgoing[name]:
            indegree[loser] -= 1
            if not indegree[loser]:
                available.append(loser)
    if visited != len(ids):
        raise ValueError("Organizer resolvable pairs contain a directed cycle")
    differences = value.get("pairwise_difference_intervals")
    paired = {}
    if differences is not None:
        if not isinstance(differences, list) or len(differences) != len(pairs):
            raise ValueError("Organizer paired difference bounds must cover frozen pairs exactly")
        for record in differences:
            if not isinstance(record, dict) or set(record) != {"winner", "loser", "lower", "upper", "method"}:
                raise ValueError("Malformed organizer paired difference bound")
            winner, loser = record["winner"], record["loser"]
            if not isinstance(winner, str) or not isinstance(loser, str) or winner not in truth or loser not in truth:
                raise ValueError("Unknown paired difference IDs")
            key = (winner, loser)
            if key in paired or record["method"] not in {"same_parent_same_panel_background_cancels", "independent_parent_marginal_bounds"}:
                raise ValueError("Invalid paired difference method or duplicate pair")
            lo, hi = record["lower"], record["upper"]
            central = (truth[winner] - truth[loser]) * (1 if higher else -1)
            if not _finite(lo) or not _finite(hi) or not 0 < lo <= central <= hi:
                raise ValueError("Paired difference must be strictly positive and enclose central difference")
            paired[key] = record
        if set(paired) != {(p["winner"], p["loser"]) for p in pairs}:
            raise ValueError("Organizer paired difference IDs do not match frozen pairs")
    for pair in pairs:
        winner, loser = pair["winner"], pair["loser"]
        if not (truth[winner] > truth[loser] if higher else truth[winner] < truth[loser]):
            raise ValueError("Organizer pair direction contradicts central truth or a gold tie")
        if intervals is not None and (winner, loser) not in paired and not (
            intervals[winner][0] > intervals[loser][1] if higher
            else intervals[winner][1] < intervals[loser][0]
        ):
            raise ValueError("Organizer scored pair has overlapping or touching digitization bounds")


def _gold(path):
    value = _decode(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict) or value.get("task_type") not in {"ranking", "binary", "design"}:
        raise ValueError("Organizer gold requires a supported task_type")
    if value.get("data_status") not in DATA_STATUSES:
        raise ValueError("Organizer gold requires explicit experimental or synthetic provenance")
    if not re.fullmatch(r"AB(?:0[1-9]|1[0-3])(?:-[AB])?", value.get("item_id", "")):
        raise ValueError("Organizer gold requires item_id AB01–AB13")
    if normalize_case_id(value.get("case_id")) != value["case_id"]:
        raise ValueError("Organizer case_id must be canonical")
    kind = value["task_type"]
    if kind == "design":
        columns, templates = value.get("sequence_columns"), value.get("templates")
        if columns not in (["sequence1"], ["sequence1", "sequence2"]) or not isinstance(templates, dict) or set(templates) != set(columns):
            raise ValueError("Organizer design requires sequence templates for each chain")
        if value.get("expected_candidates") != 10:
            raise ValueError("Organizer design requires exactly ten candidates")
        constraints = value.get("constraints", {})
        alphabet = constraints.get("allowed_alphabet", AA)
        if not isinstance(alphabet, str) or set(alphabet) != set(AA):
            raise ValueError("Organizer alphabet must contain the twenty standard amino acids")
        positions = constraints.get("designable_positions")
        for column in columns:
            template = templates[column]
            if not isinstance(template, str) or not template or not set(template) <= set(AA + "X") or "X" not in template:
                raise ValueError("Organizer template must contain amino acids and at least one X design position")
            if positions is not None:
                stated = positions.get(column) if isinstance(positions, dict) else positions if len(columns) == 1 else None
                if stated != [i+1 for i, aa in enumerate(template) if aa == "X"]:
                    raise ValueError("Organizer designable positions must match X masks exactly")
    else:
        ids, truth = value.get("target_ids"), value.get("truth")
        if not isinstance(ids, list) or len(ids) < 2 or any(not isinstance(x, str) or not x for x in ids) or len(set(ids)) != len(ids):
            raise ValueError("Organizer target_ids must be unique nonempty IDs")
        if not isinstance(truth, dict) or set(truth) != set(ids):
            raise ValueError("Organizer truth must cover every target ID")
        if kind == "binary":
            metric = value.get("binary_metric", "mcc")
            if not isinstance(metric, str) or metric not in {"mcc", "accuracy"}:
                raise ValueError("Organizer binary_metric is unsupported")
            if any(type(x) is not int or x not in (0, 1) for x in truth.values()):
                raise ValueError("Organizer binary gold must contain integer labels 0 or 1")
            if metric == "mcc" and set(truth.values()) != {0, 1}:
                raise ValueError("Organizer MCC gold must contain both classes as integers")
        elif any(not _finite(x) for x in truth.values()) or len(set(truth.values())) < 2 or type(value.get("higher_is_better")) is not bool:
            raise ValueError("Organizer ranking needs varying finite values and higher_is_better")
        if kind == "ranking":
            _ranking_gold(value)
    return value


def _ranking(prediction, ids, truth, higher, *, metric="spearman", pairs=None):
    if isinstance(prediction, str):
        text = prediction.strip()
        prediction = _decode(text) if text.startswith(("[", "{")) else [part.strip() for part in text.split(",")]
    if not isinstance(prediction, list) or any(not isinstance(x, str) for x in prediction):
        raise ValueError("Ranking must be a comma-separated line of candidate IDs")
    if len(prediction) != len(ids) or len(set(prediction)) != len(prediction) or set(prediction) != set(ids):
        raise ValueError("Ranking must include every target ID exactly once")
    positions = {name: index for index, name in enumerate(prediction)}
    expected = _ranks([-truth[name] if higher else truth[name] for name in ids])
    rho = _correlation([positions[name] for name in ids], expected)
    if metric == "resolvable_pair_concordance":
        correct = sum(positions[pair["winner"]] < positions[pair["loser"]] for pair in pairs)
        wrong = len(pairs) - correct
        concordance = (correct-wrong)/len(pairs)
        return {"score": max(0.0, concordance), "raw_pair_concordance": concordance,
                "ranking_metric": metric, "correct_pairs": correct, "wrong_pairs": wrong,
                "n_resolvable_pairs": len(pairs), "n_ignored_pairs": len(ids)*(len(ids)-1)//2-len(pairs),
                "raw_spearman": rho, "n_scored": len(ids),
                "gold_ties": len(set(truth.values())) != len(ids),
                "score_definition": "max(0, (correct - wrong) / frozen resolvable pairs); Spearman is secondary"}
    best_order = sorted(ids, key=truth.get, reverse=higher)
    best_positions = {name: index for index, name in enumerate(best_order)}
    maximum = _correlation([best_positions[name] for name in ids], expected)
    return {"score": max(0.0, rho), "raw_spearman": rho, "n_scored": len(ids),
            "maximum_attainable_score": maximum,
            "gold_ties": len(set(truth.values())) != len(ids),
            "score_definition": "max(0, Spearman rho); average ranks for gold ties"}


def _binary(prediction, ids, truth, *, metric="mcc"):
    prediction = _decode(prediction)
    if not isinstance(prediction, dict) or set(prediction) != set(ids):
        raise ValueError("Binary response must contain exactly every target ID")
    if any(type(x) is not int or x not in (0, 1) for x in prediction.values()):
        raise ValueError("Binary labels must be JSON integers 0 or 1; booleans are invalid")
    tp = sum(prediction[k] == truth[k] == 1 for k in ids)
    tn = sum(prediction[k] == truth[k] == 0 for k in ids)
    fp = sum(prediction[k] == 1 and truth[k] == 0 for k in ids)
    fn = sum(prediction[k] == 0 and truth[k] == 1 for k in ids)
    den = math.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))
    mcc = (tp*tn-fp*fn)/den if den else 0.0
    accuracy = (tp+tn)/len(ids)
    balanced_accuracy = (tp/(tp+fn) + tn/(tn+fp))/2 if tp+fn and tn+fp else None
    return {"score": accuracy if metric == "accuracy" else max(0.0, mcc),
            "binary_metric": metric, "raw_mcc": mcc, "accuracy": accuracy,
            "balanced_accuracy": balanced_accuracy,
            "balanced_accuracy_available": balanced_accuracy is not None,
            "confusion_matrix": {"tp": tp, "tn": tn, "fp": fp, "fn": fn},
            "n_scored": len(ids),
            "score_definition": "correct labels / all target labels" if metric == "accuracy" else "max(0, MCC); constant predictions have MCC zero"}


def _design_rows(prediction, gold):
    if not isinstance(prediction, str):
        raise ValueError("Design response must be CSV text")
    reader = csv.DictReader(io.StringIO(prediction.strip()))
    columns = ["name"] + gold["sequence_columns"]
    if reader.fieldnames != columns:
        raise ValueError("Design CSV header must be " + ",".join(columns))
    rows = list(reader)
    if len(rows) != gold["expected_candidates"]:
        raise ValueError("Design response must contain exactly ten candidates")
    names, sequences = set(), set()
    for row in rows:
        if set(row) != set(columns) or any(value is None for value in row.values()):
            raise ValueError("Every design row must have the exact declared columns")
        name = row["name"]
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", name) or name in names:
            raise ValueError("Candidate names must be unique safe identifiers")
        names.add(name)
        pair = tuple(row[column] for column in gold["sequence_columns"])
        if pair in sequences:
            raise ValueError("Duplicate candidate sequences are invalid")
        sequences.add(pair)
        for column in gold["sequence_columns"]:
            sequence, template = row[column], gold["templates"][column]
            if len(sequence) != len(template) or not set(sequence) <= set(AA):
                raise ValueError("Candidate has an invalid amino acid or chain length")
            if any(fixed != "X" and aa != fixed for aa, fixed in zip(sequence, template)):
                raise ValueError("Candidate changed a fixed framework or constrained position")
    return rows


def _af3_config(gold, config):
    """Validate the approved protocol even while runtime versions are pending."""
    if type(config.get("frozen")) is not bool:
        raise ValueError("Organizer AF3 frozen state must be boolean")
    required = {
        "protocol_version": "ab_design_af3_ranking_v1",
        "input_dialect": "alphafold3", "input_version": 3,
        "model_seeds": [20261023], "samples_per_seed": 5,
        "sample_selection": "max_raw_ranking_score",
        "score_transform": "clip_0_1",
        "candidate_aggregation": "mean_all_10",
        "case_aggregation": "equal_weight_all_10",
    }
    if any(config.get(key) != value for key, value in required.items()):
        raise ValueError("Organizer AF3 protocol must use the frozen seed, five samples, max, clip and means")
    if type(config["input_version"]) is not int or type(config["samples_per_seed"]) is not int or any(type(seed) is not int for seed in config["model_seeds"]):
        raise ValueError("Organizer AF3 sample and seed values must be integers")
    expected = ["antigen", "VHH"] if gold["sequence_columns"] == ["sequence1"] else ["antigen", "VH", "VL"]
    if config.get("chain_order") != expected or config.get("copies_per_chain") != [1]*len(expected):
        raise ValueError("Organizer AF3 chains must be one antigen plus the submitted variable domains")
    target = gold.get("target_sequence")
    if not isinstance(target, str) or not target or not set(target) <= set(AA):
        raise ValueError("Organizer AF3 antigen sequence is missing or invalid")
    target_hash = hashlib.sha256(target.encode("ascii")).hexdigest()
    if gold.get("target_sequence_sha256") != target_hash or config.get("target_sequence_sha256") != target_hash:
        raise ValueError("Organizer AF3 antigen hash does not match the supplied target sequence")
    if "metric_gates" in config:
        raise ValueError("Organizer AF3 ranking evaluation does not use metric_gates")
    if config["frozen"]:
        versions = config.get("tool_versions")
        if not isinstance(versions, dict) or "alphafold3" not in versions or any(not isinstance(v, str) or not v.strip() or "latest" in v.lower() for v in versions.values()):
            raise ValueError("Organizer AF3 requires immutable tool versions")
        for field in ("model_parameters_sha256", "database_snapshot_sha256"):
            if not isinstance(config.get(field), str) or not re.fullmatch(r"[0-9a-f]{64}", config[field]):
                raise ValueError("Organizer AF3 requires frozen model and database hashes")
        if not isinstance(config.get("container_image_digest"), str) or not re.fullmatch(r"sha256:[0-9a-f]{64}", config["container_image_digest"]):
            raise ValueError("Organizer AF3 requires an immutable container digest")
        for field in ("msa_policy", "template_policy", "max_template_date", "protocol_basis"):
            if not isinstance(config.get(field), str) or not config[field].strip():
                raise ValueError("Organizer AF3 requires explicit pipeline policies and protocol basis")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", config["max_template_date"]):
            raise ValueError("Organizer AF3 max_template_date must be an explicit date")
    return config


def af3_complex_sha256(row, gold):
    """Bind an AF3 result to exact antigen/antibody chains and their order."""
    roles = ["VHH"] if gold["sequence_columns"] == ["sequence1"] else ["VH", "VL"]
    chains = [{"chain_id": "A", "role": "antigen", "sequence": gold["target_sequence"]}]
    chains.extend({"chain_id": chr(66+i), "role": role, "sequence": row[column]}
                  for i, (role, column) in enumerate(zip(roles, gold["sequence_columns"])))
    return canonical_hash(chains)


def _external_config(gold, config):
    frozen = gold.get("external_config")
    if frozen is None:
        if config is not None:
            raise ValueError("Organizer must freeze external_config in gold before scoring")
        return None
    if not isinstance(frozen, dict):
        raise ValueError("Organizer external_config must be embedded frozen JSON")
    if config is not None and config != frozen:
        raise ValueError("External configuration differs from organizer frozen gold")
    evaluator = frozen.get("evaluator_type", "metric_gates")
    if evaluator == "alphafold3_ranking":
        return _af3_config(gold, frozen)
    if evaluator != "metric_gates":
        raise ValueError("Organizer external evaluator type is unsupported")
    if frozen.get("frozen") is not True or not isinstance(frozen.get("tool_versions"), dict) or not frozen["tool_versions"] or not isinstance(frozen.get("calibration_basis"), str) or not frozen["calibration_basis"].strip():
        raise ValueError("Organizer external_config requires frozen tool versions and calibration basis")
    if any(not isinstance(k, str) or not isinstance(v, str) or not v.strip() for k, v in frozen["tool_versions"].items()):
        raise ValueError("Organizer tool versions must be nonempty strings")
    gates = frozen.get("metric_gates")
    if not isinstance(gates, dict) or not gates:
        raise ValueError("Organizer external_config requires metric_gates")
    categories = set()
    for name, gate in gates.items():
        if not isinstance(name, str) or not isinstance(gate, dict) or gate.get("direction") not in {"min", "max"} or not _finite(gate.get("threshold")) or not isinstance(gate.get("category"), str):
            raise ValueError("Organizer metric gate requires category, min/max direction and finite threshold")
        categories.add(gate["category"])
    if not {"binding_proxy", "developability", "novelty", "diversity"} <= categories:
        raise ValueError("Organizer gates must cover binding, developability, novelty and diversity")
    return frozen


def _af3_metrics(rows, gold, config, results):
    submission_hash = canonical_hash(rows)
    config_hash = canonical_hash(config)
    base = {"evaluator_type": "alphafold3_ranking", "sequence_validity": 1.0,
            "submission_sha256": submission_hash, "config_sha256": config_hash,
            "target_sequence_sha256": config["target_sequence_sha256"],
            "formal_design_score_available": False}
    if not config["frozen"]:
        return {**base, "score": None, "status": "external_evaluation_not_frozen"}
    if results is None:
        return {**base, "score": None, "status": "awaiting_external_results"}
    results = _decode(results)
    if not isinstance(results, dict) or any(results.get(key) != base[key] for key in ("config_sha256", "submission_sha256", "target_sequence_sha256")):
        raise ValueError("AF3 results are not bound to this configuration, submission and antigen")
    if results.get("status") == "infrastructure_failure":
        return {**base, "score": None, "status": "infrastructure_failure", "error": results.get("error", "AF3 evaluator failed")}
    if results.get("status") != "completed" or results.get("tool_versions") != config["tool_versions"]:
        raise ValueError("AF3 results require completed status and matching tool versions")
    candidates = results.get("candidates")
    if not isinstance(candidates, dict) or set(candidates) != {row["name"] for row in rows}:
        raise ValueError("AF3 results must include every submitted candidate exactly once")
    raw, clipped, sample_metrics, failures = {}, {}, {}, []
    for row in rows:
        name = row["name"]
        result = candidates[name]
        if not isinstance(result, dict) or result.get("complex_sha256") != af3_complex_sha256(row, gold):
            raise ValueError("AF3 candidate complex hash does not match its antigen and antibody chains")
        if result.get("status") in {"infrastructure_failure", "inference_failure"}:
            failures.append(name)
            continue
        if result.get("status") != "completed":
            raise ValueError("AF3 candidate status is missing or invalid")
        samples = result.get("samples")
        if not isinstance(samples, list) or len(samples) != 5:
            raise ValueError("AF3 requires all five samples for every candidate; missing samples are organizer errors")
        indices = set()
        for sample in samples:
            if not isinstance(sample, dict) or type(sample.get("seed")) is not int or sample["seed"] != 20261023 or type(sample.get("sample_index")) is not int or sample["sample_index"] not in range(5) or sample["sample_index"] in indices:
                raise ValueError("AF3 samples require the frozen seed and distinct sample indices 0 through 4")
            indices.add(sample["sample_index"])
            if sample.get("status") in {"infrastructure_failure", "inference_failure"}:
                failures.append(name)
                continue
            if sample.get("status") != "completed" or not _finite(sample.get("ranking_score")):
                raise ValueError("AF3 samples require completed status and finite ranking_score")
        if name in failures:
            continue
        raw[name] = max(sample["ranking_score"] for sample in samples)
        clipped[name] = min(1.0, max(0.0, raw[name]))
        sample_metrics[name] = samples
    if failures:
        return {**base, "score": None, "status": "infrastructure_failure",
                "failed_candidates": sorted(set(failures)), "error": "AF3 evaluation incomplete; no candidate is dropped from the denominator"}
    return {**base, "score": math.fsum(clipped.values())/10, "raw_ranking_score_mean": math.fsum(raw.values())/10,
            "status": "scored", "formal_design_score_available": True, "n_scored": 10,
            "candidate_raw_ranking_scores": raw, "candidate_scores": clipped, "sample_metrics": sample_metrics,
            "tool_versions": results["tool_versions"], "resource_usage": results.get("resource_usage"),
            "score_definition": "mean over all 10 candidates of clip(max ranking_score across 5 samples at seed 20261023, 0, 1); computational proxy only"}


def _design_metrics(rows, config, results, *, gold=None):
    submission_hash = canonical_hash(rows)
    if config is None:
        return {"score": None, "status": "external_evaluation_not_frozen", "sequence_validity": 1.0,
                "submission_sha256": submission_hash, "formal_design_score_available": False}
    if config.get("evaluator_type") == "alphafold3_ranking":
        return _af3_metrics(rows, gold, config, results)
    config_hash = canonical_hash(config)
    if results is None:
        return {"score": None, "status": "awaiting_external_results", "sequence_validity": 1.0,
                "submission_sha256": submission_hash, "config_sha256": config_hash,
                "formal_design_score_available": False}
    results = _decode(results)
    if not isinstance(results, dict) or results.get("config_sha256") != config_hash or results.get("submission_sha256") != submission_hash:
        raise ValueError("External results are not bound to this frozen configuration and submission")
    if results.get("status") == "infrastructure_failure":
        return {"score": None, "status": "infrastructure_failure", "error": results.get("error", "External evaluator failed"), "formal_design_score_available": False}
    if results.get("status") != "completed" or results.get("tool_versions") != config["tool_versions"]:
        raise ValueError("External results require completed status and matching tool versions")
    metrics = results.get("candidates")
    names = {row["name"] for row in rows}
    gates = config["metric_gates"]
    if not isinstance(metrics, dict) or set(metrics) != names:
        raise ValueError("External evaluator must return every submitted candidate")
    passed = {}
    for name, values in metrics.items():
        if not isinstance(values, dict) or set(values) != set(gates) or any(not _finite(value) for value in values.values()):
            raise ValueError("External evaluator must supply every finite frozen metric")
        passed[name] = all(values[key] >= gate["threshold"] if gate["direction"] == "min" else values[key] <= gate["threshold"] for key, gate in gates.items())
    return {"score": sum(passed.values()) / 10, "status": "scored", "sequence_validity": 1.0,
            "formal_design_score_available": True, "candidate_passes": passed, "proxy_metrics": metrics,
            "tool_versions": results["tool_versions"], "config_sha256": config_hash,
            "submission_sha256": submission_hash, "n_scored": 10,
            "resource_usage": results.get("resource_usage"),
            "score_definition": "candidates passing every frozen gate / 10; not experimental success probability"}


def evaluate_case(prediction: Any, gold_path, *, external_results=None, external_config=None):
    gold = _gold(gold_path)
    kind = gold["task_type"]
    config = _external_config(gold, external_config) if kind == "design" else None
    report = {"item_id": gold["item_id"], "case_id": gold["case_id"], "task_type": kind,
              "data_status": gold["data_status"], "score": 0.0, "status": "invalid_submission",
              "is_experimental_performance": kind != "design" and gold["data_status"] != "synthetic_fixture",
              "submission_complete": False}
    if kind == "design":
        report["formal_design_score_available"] = False
        report["design_evaluator_frozen"] = config is not None and config.get("frozen") is True
    try:
        if kind == "ranking":
            result = _ranking(prediction, gold["target_ids"], gold["truth"], gold["higher_is_better"],
                              metric=gold.get("ranking_metric", "spearman"), pairs=gold.get("resolvable_pairs"))
        elif kind == "binary":
            result = _binary(prediction, gold["target_ids"], gold["truth"], metric=gold.get("binary_metric", "mcc"))
        else:
            result = _design_rows(prediction, gold)
    except (ValueError, TypeError, OverflowError, RecursionError, csv.Error) as error:
        report["error"] = str(error)
        return report
    # External errors are organizer/infrastructure errors, not contestant zeroes.
    if kind == "design":
        report.update(_design_metrics(result, config, external_results, gold=gold))
    else:
        report.update(result, status="scored")
    report["submission_complete"] = True
    return report


def score_case(prediction, gold_path, **kwargs):
    return evaluate_case(prediction, gold_path, **kwargs)["score"]


def aggregate_cases(reports, expected_case_ids, *, item_id=None):
    """No skipping missing or unscored cases; use explicit invalid submissions."""
    expected = [normalize_case_id(value) for value in expected_case_ids]
    if not expected or len(set(expected)) != len(expected):
        raise ValueError("Expected case IDs must be unique and nonempty")
    if not isinstance(reports, list) or any(not isinstance(r, dict) for r in reports):
        raise ValueError("Reports must be a list")
    if len(reports) != len(expected) or {r.get("case_id") for r in reports} != set(expected):
        raise ValueError("Exactly one report for every expected case is required")
    items = {r.get("item_id") for r in reports}
    if len(items) != 1 or None in items or (item_id is not None and items != {item_id}):
        raise ValueError("Case reports must belong to the same item")
    statuses = {r.get("data_status") for r in reports}
    if not statuses <= DATA_STATUSES:
        raise ValueError("Case reports lack valid data provenance")
    pending = [r["case_id"] for r in reports if r.get("score") is None or (
        r.get("task_type") == "design" and r.get("design_evaluator_frozen") is not True)]
    if any(r.get("score") is not None and (not _finite(r["score"]) or not 0 <= r["score"] <= 1) for r in reports):
        raise ValueError("Case scores must be finite in [0,1] or unavailable")
    summaries = {}
    for data_status in sorted(statuses):
        members = [r for r in reports if r["data_status"] == data_status]
        unavailable = [r["case_id"] for r in members if r["case_id"] in pending]
        summaries[data_status] = {
            "score": None if unavailable else math.fsum(r["score"] for r in members)/len(members),
            "case_count": len(members), "case_ids": [r["case_id"] for r in members],
            "pending_cases": unavailable,
        }
    return {"item_id": next(iter(items)), "score": None if pending else math.fsum(r["score"] for r in reports)/len(reports),
            "status": "incomplete_external_evaluation" if pending else "scored",
            "case_count": len(reports), "pending_cases": pending, "data_statuses": sorted(statuses),
            "data_status_summaries": summaries,
            "is_experimental_performance": "synthetic_fixture" not in statuses and all(r.get("task_type") != "design" for r in reports),
            "interpretation": "Computational design quality is not experimental success probability." if any(r.get("task_type") == "design" for r in reports) else "Synthetic fixture results are not real biological performance." if "synthetic_fixture" in statuses else "Observed experimental endpoint prediction.",
            "case_scores": {r["case_id"]: r["score"] for r in reports}}


def evaluate_question(prediction, question_dir, case_id, **kwargs):
    case = normalize_case_id(case_id)
    directory = Path(question_dir)
    spec = _decode((directory / "tests/evaluation_spec.json").read_text(encoding="utf-8"))
    if spec.get("input_mode") != "single_case_csv" or spec.get("status") not in {"ready", "fixture_ready"}:
        raise ValueError("Organizer item is not released for independent-case scoring")
    entries = spec.get("cases", [])
    if not isinstance(entries, list) or any(not isinstance(entry, dict) for entry in entries):
        raise ValueError("Organizer case inventory is invalid")
    selected = [entry for entry in entries if entry.get("case_id") == case]
    if len(selected) != 1:
        raise ValueError("Organizer has not released this case")
    entry = selected[0]
    if entry.get("input") != f"inputs/{case}.csv":
        raise ValueError("Organizer case input reference is invalid")
    observed_hash = hashlib.sha256((directory / entry["input"]).read_bytes()).hexdigest()
    path = directory / "tests" / "cases" / f"{case}.answer.json"
    item = spec.get("item_id", directory.name)
    if item.split("-")[0] in {"AB01", "AB02", "AB03"}:
        if entry.get("answer") != f"tests/cases/{case}.answer.json":
            raise ValueError("Organizer patent answer reference is invalid")
        if entry.get("answer_sha256") != hashlib.sha256(path.read_bytes()).hexdigest():
            raise ValueError("Organizer patent answer does not match its frozen specification hash")
    gold = _gold(path)
    if entry.get("input_sha256") != observed_hash or gold.get("input_sha256") != observed_hash:
        raise ValueError("Organizer input and gold hashes no longer match")
    if gold["task_type"] == "design" and isinstance(gold.get("external_config"), dict) and gold["external_config"].get("evaluator_type") == "alphafold3_ranking":
        if entry.get("answer_sha256") != hashlib.sha256(path.read_bytes()).hexdigest():
            raise ValueError("Organizer AF3 answer does not match its frozen specification hash")
        with (directory/entry["input"]).open(newline="", encoding="utf-8-sig") as handle:
            input_rows = list(csv.DictReader(handle))
        if len(input_rows) != 1 or input_rows[0].get("target_sequence") != gold.get("target_sequence") or any(input_rows[0].get(column) != gold["templates"][column] for column in gold["sequence_columns"]):
            raise ValueError("Organizer AF3 antigen or sequence templates differ from the model input")
    if item.split("-")[0] in {"AB01", "AB02", "AB03"}:
        study_information = entry.get("study_information")
        if not isinstance(study_information, str) or not study_information.strip():
            raise ValueError("Organizer patent study information is missing")
        study_hash = hashlib.sha256(study_information.encode("utf-8")).hexdigest()
        if entry.get("study_information_sha256") != study_hash or gold.get("study_information_sha256") != study_hash:
            raise ValueError("Organizer study information and gold hashes no longer match")
    if gold["case_id"] != case or gold["item_id"] != item:
        raise ValueError("Organizer gold belongs to another case or question")
    return evaluate_case(prediction, path, **kwargs)


def aggregate_question(reports, question_dir):
    """Use the frozen case inventory, never a caller-selected scored subset."""
    directory = Path(question_dir)
    spec = _decode((directory / "tests/evaluation_spec.json").read_text(encoding="utf-8"))
    cases = spec.get("cases")
    if spec.get("input_mode") != "single_case_csv" or not isinstance(cases, list) or not cases:
        raise ValueError("Organizer has not released an independent-case inventory")
    return aggregate_cases(reports, [case["case_id"] for case in cases], item_id=spec.get("item_id", directory.name))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gold", type=Path, required=True)
    parser.add_argument("--prediction", type=Path, required=True)
    parser.add_argument("--external-results", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    results = args.external_results.read_text() if args.external_results else None
    report = evaluate_case(args.prediction.read_text(), args.gold, external_results=results)
    text = json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
