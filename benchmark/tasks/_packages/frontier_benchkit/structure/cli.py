"""Command-line adapter shared by the exported per-case score.py files."""

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory

from .response import APIResponseError, RawReply, is_refusal_evidence


GENERATION_FIELDS = (
    "target_id", "case_id", "reply", "status", "api_style", "run_count",
    "schema_valid", "schema_error", "strict_json_document", "output_contract_valid",
    "parse_mode", "input_tokens", "output_tokens", "total_tokens",
    "api_response_path", "model_output_path", "model_response_path",
)


def reply_files(path, name):
    if path.is_file() and path.suffix.lower() == ".json" and name is None:
        return [path]
    if not path.is_dir():
        raise ValueError("Supply a reply JSON file or a directory containing replies for this case.")
    raw_dir = path / "api_responses" if (path / "api_responses").is_dir() else path
    if name:
        reply = raw_dir / name
        if name != Path(name).name or not reply.is_file() or reply.suffix.lower() != ".json":
            raise ValueError("--reply must name a JSON file in the reply directory.")
        return [reply]
    manifest_path = raw_dir.parent / "run_manifest.json"
    if raw_dir.name == "api_responses" and manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if (manifest.get("target_count") or len(manifest.get("target_ids") or [])) > 1:
            raise ValueError("This run covers multiple cases. Select this case's JSON file with --reply.")
    files = sorted(p for p in raw_dir.glob("*.json") if p.is_file()
                   and not p.name.endswith(".meta.json")
                   and p.name not in {"run_manifest.json", "run_summary.json", "evaluation_summary.json"})
    if not files:
        raise ValueError(f"No raw reply JSON files found in {raw_dir}")
    return files


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_tsv(path, rows, fields):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def evaluation_metrics(metrics):
    flattened = {}
    for key, value in metrics.items():
        if isinstance(value, dict):
            prefix = {"post_2026": "post2026", "best_candidate": "best"}.get(key, key)
            flattened.update({f"{prefix}_{metric}": score for metric, score in value.items()})
        else:
            flattened[key] = value
    return flattened


def evaluate_reply(evaluate, source, api_style, case_dir, case_id, stage, output):
    reply = RawReply(source.read_bytes(), api_style)
    name = source.stem
    raw = Path("api_responses") / source.name
    (stage / raw).write_bytes(reply.raw)
    try:
        report = evaluate(reply)
        error = report.get("error", "")
        status = ("failed_schema_validation" if error else
                  "passed" if reply.strict else "passed_with_output_contract_violation")
    except (ValueError, TypeError, KeyError, AttributeError, APIResponseError) as exc:
        error = str(exc)
        status = "refusal" if isinstance(exc, APIResponseError) and is_refusal_evidence(error) else "error"
        report = {"score": 0.0, "metrics": {}, "error": error}

    text_path = ""
    if reply.text is not None:
        text = Path("model_outputs") / f"{name}.txt"
        (stage / text).write_text(reply.text, encoding="utf-8")
        text_path = str(output / text)
    parsed_path = ""
    if reply.parsed is not None:
        parsed = Path("model_responses") / f"{name}.json"
        write_json(stage / parsed, reply.parsed)
        parsed_path = str(output / parsed)

    key = {"target_id": case_dir.name, "case_id": f"case-{case_id}", "reply": source.name}
    valid = not error and reply.parsed is not None
    generation = {
        **key, "status": status, "api_style": reply.api_style, "run_count": 1,
        "schema_valid": valid, "schema_error": error, "strict_json_document": reply.strict,
        "output_contract_valid": valid and reply.strict, "parse_mode": reply.parse_mode,
        "input_tokens": reply.input_tokens, "output_tokens": reply.output_tokens,
        "total_tokens": reply.input_tokens + reply.output_tokens, "api_response_path": str(output / raw),
        "model_output_path": text_path, "model_response_path": parsed_path,
    }
    evaluation = {**key, "status": status, "score": report["score"],
                  "error": error, **evaluation_metrics(report["metrics"])}
    prediction = {**key, "prediction": reply.parsed} if valid else None
    return generation, evaluation, prediction


def main(evaluate, case_dir, case_id):
    parser = argparse.ArgumentParser(description=f"Parse and score raw LLM replies for {case_dir.name}.")
    parser.add_argument("raw_output", type=Path, help="Raw reply JSON file or a reply directory for this case")
    parser.add_argument("--reply", help="Filename to select from a directory containing other cases")
    parser.add_argument("--output-dir", required=True, type=Path, help="New directory for scoring artifacts")
    parser.add_argument("--api-style", choices=("chat_completions", "responses", "anthropic_messages"))
    args = parser.parse_args()
    output = args.output_dir.resolve()
    try:
        if output.exists():
            raise FileExistsError(f"Output directory already exists: {output}")
        files = reply_files(args.raw_output.resolve(), args.reply)
        output.parent.mkdir(parents=True, exist_ok=True)
        with TemporaryDirectory(prefix=".score-", dir=output.parent) as work:
            stage = Path(work) / "result"
            for directory in ("api_responses", "model_outputs", "model_responses"):
                (stage / directory).mkdir(parents=True)
            rows = [evaluate_reply(evaluate, file, args.api_style, case_dir, case_id, stage, output)
                    for file in files]
            generation, evaluation, predictions = zip(*rows)
            write_tsv(stage / "generation.tsv", generation, GENERATION_FIELDS)
            fields = list(dict.fromkeys(key for row in evaluation for key in row))
            write_tsv(stage / "evaluation.tsv", evaluation, fields)
            with (stage / "predictions.jsonl").open("w", encoding="utf-8") as handle:
                for prediction in predictions:
                    if prediction is not None:
                        handle.write(json.dumps(prediction, ensure_ascii=False) + "\n")
            counts = Counter(row["status"] for row in generation)
            summary = {
                "bench_id": case_dir.name,
                "case_id": f"case-{case_id}",
                "reply_count": len(rows),
                "status_counts": dict(counts),
                "mean_score": sum(row["score"] for row in evaluation) / len(rows),
            }
            write_json(stage / "evaluation_summary.json", summary)
            stage.rename(output)
    except (OSError, ValueError) as exc:
        parser.exit(2, f"{exc}\n")
    print(f"{output}: {dict(counts)}")
