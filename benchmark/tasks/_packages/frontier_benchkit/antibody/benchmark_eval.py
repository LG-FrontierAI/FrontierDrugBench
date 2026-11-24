"""Organizer evaluation and complete-denominator summaries for 30 tasks.

No model/network calls occur unless an explicitly configured rubric judge is
requested. AF3 execution is external; this module consumes bound results only.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
import math
from pathlib import Path

from .benchmark_config import CATEGORY_ZH, TASKS, THRESHOLD_VERSION, task_metadata

ROOT = Path(__file__).resolve().parents[1]


def _score(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or not 0 <= value <= 1:
        raise ValueError("A score must be a finite number in [0, 1]")
    return float(value)


def decorate(report, item, *, case_level=False):
    """Case diagnostics do not become independent task pass/fail decisions."""
    result = {**report, **task_metadata(item)}
    value = result.get("score")
    if value is not None:
        result["score"] = _score(value)
    result["passed"] = None if case_level or value is None else value >= result["pass_threshold"]
    result["decision_level"] = "item_after_all_required_cases" if case_level else "item"
    return result


def _rubric_module(directory):
    name = "benchmark_rubric_" + directory.name.replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, directory / "tests/score.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _design_runtime_pending(spec, directory):
    if spec.get("evaluator_type") != "alphafold3_ranking":
        return False
    for entry in spec.get("cases", []):
        gold = json.loads((directory / entry["answer"]).read_text())
        if gold.get("external_config", {}).get("frozen") is not True:
            return True
    return False


def evaluate(item, prediction, *, case_id=None, root=ROOT, external_results=None, judgment=None, judge=None):
    if item not in TASKS:
        raise ValueError("Unknown active task")
    directory = Path(root) / "questions" / item
    spec = json.loads((directory / "tests/evaluation_spec.json").read_text())
    if spec.get("input_mode") == "single_case_csv":
        if case_id is None:
            raise ValueError("Independent-case evaluation requires case_id")
        from .sequence_case_eval import evaluate_question
        report = evaluate_question(prediction, directory, case_id, external_results=external_results)
        return decorate(report, item, case_level=True)
    if case_id is not None or external_results is not None:
        raise ValueError("This task does not accept case_id or external_results")
    if spec.get("format") == "open_rubric" or (
        spec.get("input_mode") == "original_workbooks" and (directory / "tests/rubric.json").is_file()):
        module = _rubric_module(directory)
        try:
            report = module.score_from_judgment(prediction, judgment) if judgment is not None else module.judge_response(prediction, judge=judge)
        except RuntimeError as exc:
            report = {"status": "pending_adjudication", "score": None, "reason": str(exc)}
    else:
        from .objective_report_eval import evaluate_item
        report = evaluate_item(prediction, directory / "tests/answer.json")
    return decorate(report, item)


def aggregate(item, reports, *, root=ROOT):
    """Missing contestant cases count zero; infrastructure-pending cases remain null."""
    if isinstance(reports, list):
        if any(not isinstance(row, dict) or "case_id" not in row for row in reports):
            raise ValueError("Case reports require case_id")
        if len({row["case_id"] for row in reports}) != len(reports):
            raise ValueError("Duplicate case ID")
        reports = {row["case_id"]: row for row in reports}
    if item not in TASKS or not isinstance(reports, dict):
        raise ValueError("Expected an active task and a case-report mapping")
    directory = Path(root) / "questions" / item
    spec = json.loads((directory / "tests/evaluation_spec.json").read_text())
    if spec.get("input_mode") != "single_case_csv":
        raise ValueError("Only independent-case tasks use case aggregation")
    required = [entry["case_id"] for entry in spec["cases"]]
    from .sequence_case_eval import normalize_case_id
    normalized = {}
    for key, report in reports.items():
        cid = normalize_case_id(key)
        if cid not in required or cid in normalized:
            raise ValueError("Unknown or duplicate case ID")
        if not isinstance(report, dict) or report.get("item_id", item) != item or report.get("case_id", cid) != cid:
            raise ValueError("Case report identity mismatch")
        normalized[cid] = report
    rows, pending = {}, []
    strata = {}
    for entry in spec["cases"]:
        cid = entry["case_id"]
        report = normalized.get(cid, {"score": 0.0, "status": "missing_submission"})
        value = report.get("score")
        if value is None:
            if report.get("status") not in {"external_evaluation_not_frozen", "external_evaluation_pending", "awaiting_external_results", "infrastructure_failure", "pending_external_evaluation", "pending_adjudication"}:
                raise ValueError("Null scores require an explicit pending/infrastructure status")
            pending.append(cid)
        else:
            value = _score(value)
        provenance = entry.get("data_status", spec.get("data_status", "unknown"))
        rows[cid] = {**report, "score": value, "data_status": provenance}
        strata.setdefault(provenance, []).append(value)
    runtime_pending = _design_runtime_pending(spec, directory)
    result = {"status": "pending_evaluation" if pending or runtime_pending else "scored",
              "score": None if pending else math.fsum(r["score"] for r in rows.values()) / len(required),
              "case_count": len(required), "submitted_case_count": len(normalized),
              "pending_cases": pending, "case_reports": rows,
              "case_scores": {cid: row["score"] for cid, row in rows.items()},
              "aggregation": "equal_weight_mean_all_required_cases",
              "data_strata": {key: {"case_count": len(values), "score": None if None in values else math.fsum(values) / len(values)}
                              for key, values in strata.items()}}
    if runtime_pending:
        result["protocol_score"] = result["score"]
        result["score"] = None
        result["reason"] = "AF3 runtime is not frozen; invalid/missing submissions retain protocol-zero diagnostics only"
        for data in result["data_strata"].values():
            data["score"] = None
    return decorate(result, item)


def _summary_group(items):
    pending = [row["item_id"] for row in items if row["score"] is None]
    complete = not pending
    return {"item_count": len(items), "score": math.fsum(r["score"] for r in items) / len(items) if complete else None,
            "pass_rate": sum(r["passed"] for r in items) / len(items) if complete else None,
            "pending_items": pending}


def summarize(reports, *, root=ROOT):
    """Return all 30 scores, categories, original 20 families and data strata."""
    if not isinstance(reports, dict) or set(reports) - set(TASKS):
        raise ValueError("Summary accepts only active task IDs")
    rows = {}
    for item in TASKS:
        directory = Path(root) / "questions" / item
        spec = json.loads((directory / "tests/evaluation_spec.json").read_text())
        if spec.get("input_mode") == "single_case_csv":
            if item not in reports:
                report = aggregate(item, {}, root=root)
            else:
                supplied = reports[item]
                if not isinstance(supplied, dict) or supplied.get("case_id") or supplied.get("decision_level") == "item_after_all_required_cases" or "case_reports" not in supplied:
                    raise ValueError("Independent tasks require an aggregated item report, never a single case or scalar score")
                # Recompute the frozen denominator and data strata instead of
                # trusting caller-supplied means or provenance counts.
                report = aggregate(item, supplied["case_reports"], root=root)
        else:
            report = reports.get(item, {"score": 0.0, "status": "missing_submission"})
        if isinstance(report, (int, float)) and not isinstance(report, bool):
            report = {"score": report, "status": "scored"}
        if not isinstance(report, dict) or report.get("item_id", item) != item:
            raise ValueError("Invalid item report")
        if report.get("score") is None and not str(report.get("status", "")).startswith(("pending", "external_", "infrastructure", "awaiting_", "incomplete_external")):
            raise ValueError("Null item scores require explicit pending evaluation")
        if _design_runtime_pending(spec, directory):
            report = {**report, "protocol_score": report.get("protocol_score", report.get("score")), "score": None,
                      "status": "pending_evaluation", "reason": "AF3 runtime is not frozen"}
        rows[item] = {**decorate(report, item), "data_status": spec.get("data_status", "unknown")}
    categories = {category: _summary_group([r for r in rows.values() if r["category"] == category]) for category in CATEGORY_ZH}
    families = {f"AB{i:02d}": _summary_group([r for r in rows.values() if r["parent_item_id"] == f"AB{i:02d}"]) for i in range(1, 21)}
    family_values = [r["score"] for r in families.values()]
    strata = {}
    for row in rows.values():
        if row.get("data_strata"):
            for key, data in row["data_strata"].items():
                strata.setdefault(key, []).append({"item_id": row["item_id"], "score": data["score"], "passed": None if data["score"] is None else data["score"] >= row["pass_threshold"]})
        else:
            strata.setdefault(row["data_status"], []).append(row)
    return {"threshold_version": THRESHOLD_VERSION, "item_reports": rows,
            "overall": _summary_group(list(rows.values())), "category_summaries": categories,
            "original_family_summaries": families,
            "family_balanced_mean": None if None in family_values else math.fsum(family_values) / 20,
            "data_summaries": {key: _summary_group(values) for key, values in strata.items()},
            "follow_up_score_changes": {part: None if rows[f"AB19-{part}"]["score"] is None or rows[f"AB20-{part}"]["score"] is None else rows[f"AB20-{part}"]["score"] - rows[f"AB19-{part}"]["score"] for part in ("A", "B")}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["evaluate", "aggregate", "summary"])
    parser.add_argument("--item")
    parser.add_argument("--case")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--external-results", type=Path)
    parser.add_argument("--judgment", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = args.input.read_text()
    if args.action == "evaluate":
        result = evaluate(args.item, data, case_id=args.case,
                          external_results=json.loads(args.external_results.read_text()) if args.external_results else None,
                          judgment=json.loads(args.judgment.read_text()) if args.judgment else None)
    elif args.action == "aggregate":
        result = aggregate(args.item, json.loads(data))
    else:
        result = summarize(json.loads(data))
    rendered = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
