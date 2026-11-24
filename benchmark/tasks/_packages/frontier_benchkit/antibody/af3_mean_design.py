"""AB04/AB05 design score: mean AF3 ranking_score over ten candidates.

Ported from the v1 harness (``
af3_mean_design.py``); runtime behaviour is unchanged so operators can reuse
the same docker images, GPU discovery and caches.

Pipeline (peptide-style, simplified):
  1. Validate the design CSV against the released gold templates/constraints.
  2. MSA-search the target only; binder chains use empty MSA.
  3. Inference with modelSeeds=[20261023], 5 diffusion samples.
  4. Per candidate: clip(max ranking_score across the 5 samples, 0, 1);
     case score = mean over 10 candidates.

Scoring alignment (``ab_design_af3_ranking_v1``): the seed, sample budget,
selection rule, transform and aggregations are asserted against the gold
``external_config`` through ``scoring.sequence_case_eval._af3_config`` before
any GPU work, so this runtime cannot silently drift from the released
protocol. ``_mean_ranking_scores`` mirrors the arithmetic of
``sequence_case_eval._af3_metrics`` (max -> clip -> mean / 10).

No developability / novelty / diversity gates. Set POLARIS_AF3_AUTO=0 to
stage inputs and print docker commands without running them (score 0.0).

Multi-GPU inference via ``POLARIS_AF3_GPUS=auto|all|0,1,2`` (see scoring.af3_gpus).
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

_SCORING_DIR_BOOT = Path(__file__).resolve().parent
_ANTIBODY_ROOT_BOOT = _SCORING_DIR_BOOT.parents[1]
if str(_ANTIBODY_ROOT_BOOT) not in sys.path:
    sys.path.insert(0, str(_ANTIBODY_ROOT_BOOT))

from frontier_benchkit.antibody.af3_gpus import discover_af3_gpus, run_inference_multi_gpu
from frontier_benchkit.antibody.sequence_case_eval import (
    _af3_config,
    _design_rows,
    _gold,
    evaluate_question,
    normalize_case_id,
)

PROTOCOL_VERSION = "ab_design_af3_ranking_v1"
MODEL_SEEDS = [20261023]
NUM_DIFFUSION_SAMPLES = 5
SAMPLE_SELECTION = "max_raw_ranking_score"
SCORE_TRANSFORM = "clip_0_1"
CANDIDATE_AGGREGATION = "mean_all_10"
CASE_AGGREGATION = "equal_weight_all_10"

_AF3_IMAGE = os.environ.get("POLARIS_AF3_IMAGE", "alphafold3:latest-migration")
# The AF3 checkpoint and public-database trees are bulky operator-side fixtures,
# so there is deliberately no built-in default: resolving them on demand makes a
# missing configuration fail loudly instead of silently naming a directory that
# only exists on the machine this benchmark was assembled on.
_AF3_MODEL_DIR_ENV = "AF3_MODEL_DIR"
_AF3_DATABASE_DIR_ENV = "AF3_DATABASE_DIR"


def _af3_asset_dir(env_name: str, asset: str) -> str:
    """Return the configured AF3 ``asset`` directory, or fail with a fix hint."""
    value = os.environ.get(env_name, "").strip()
    if not value:
        raise RuntimeError(
            f"{env_name} is not set; AlphaFold 3 scoring needs the AF3 {asset}. "
            f"Point {env_name} at a directory holding {asset} before scoring this task."
        )
    return value
_AF3_GPU = os.environ.get("POLARIS_AF3_GPU", "0")
_AF3_AUTO = os.environ.get("POLARIS_AF3_AUTO", "1").strip().lower() not in {
    "0",
    "false",
    "no",
    "off",
}
_AF3_JACKHMMER_N_CPU = os.environ.get("POLARIS_AF3_JACKHMMER_N_CPU", "16")
_AF3_NHMMER_N_CPU = os.environ.get("POLARIS_AF3_NHMMER_N_CPU", "16")
_AF3_DOCKER_USER = os.environ.get("POLARIS_AF3_DOCKER_USER", f"{os.getuid()}:{os.getgid()}")
_AF3_FORCE_MSA = os.environ.get("POLARIS_AF3_FORCE_MSA", "0").strip().lower() in {
    "1",
    "true",
    "yes",
    "on",
}
_SCORING_DIR = _SCORING_DIR_BOOT
_SHARED_MSA_DIR = Path(
    os.environ.get("POLARIS_AB_AF3_MSA_DIR", str(_SCORING_DIR.parents[1] / "assets" / "antibody" / "af3_target_msa"))
)


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _protocol(gold: dict[str, Any]) -> dict[str, Any]:
    """Return the gold ``external_config`` after the released protocol check.

    ``_af3_config`` pins protocol_version / model_seeds / samples_per_seed /
    sample_selection / score_transform / aggregations, chain order and the
    antigen hash. Running AF3 against a drifted protocol is an organizer bug,
    so fail closed instead of producing a plausible-looking score.
    """
    config = gold.get("external_config")
    if not isinstance(config, dict):
        raise ValueError("Design gold is missing external_config; AF3 scoring is unavailable")
    if config.get("evaluator_type") != "alphafold3_ranking":
        raise ValueError("Design gold does not select the AlphaFold 3 ranking evaluator")
    config = _af3_config(gold, config)
    if config["model_seeds"] != MODEL_SEEDS or config["samples_per_seed"] != NUM_DIFFUSION_SAMPLES:
        raise ValueError("AF3 runtime seed/sample budget differs from the gold protocol")
    return config


def _reset_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def _work_dir(question_dir: Path) -> Path:
    explicit = os.environ.get("POLARIS_DESIGN_WORK_DIR")
    rep = os.environ.get("POLARIS_SCORE_REPEAT", "0")
    if explicit:
        path = Path(explicit) / question_dir.name / f"repeat_{rep}"
    else:
        item = os.environ.get("POLARIS_ITEM_DIR")
        if item:
            path = Path(item) / "work" / f"repeat_{rep}"
        else:
            out = os.environ.get("POLARIS_OUT_DIR")
            if out:
                path = Path(out) / "items" / question_dir.name / "work" / f"repeat_{rep}"
            else:
                path = Path(tempfile.gettempdir()) / "frontier_af3_ab" / question_dir.name / f"repeat_{rep}"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _load_input_row(question_dir: Path, case: str) -> dict[str, str]:
    path = question_dir / "inputs" / f"{case}.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 1:
        raise ValueError(f"Expected one input row in {path}")
    return rows[0]


def _prediction_csv(prediction: Any) -> str:
    if isinstance(prediction, str):
        return prediction
    if isinstance(prediction, dict) and isinstance(prediction.get("_raw"), str):
        return prediction["_raw"]
    raise ValueError("Design response must be CSV text")


def _job_name(candidate_name: str, sequences: tuple[str, ...] | list[str]) -> str:
    """Content-addressed job name.

    v1 keyed the AF3 output dir on the candidate name alone, so a re-run with a
    different sequence under the same name could reuse stale structures. The
    digest suffix makes reuse safe.
    """
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", candidate_name).strip("._-")[:120] or "ab_candidate"
    digest = _sha256_text("\n".join(sequences))[:10]
    return f"ab_{safe}_{digest}"[:200]


def _resolve_gpus() -> list[str]:
    if discover_af3_gpus is None:
        return [str(_AF3_GPU)]
    return discover_af3_gpus(log=lambda m: print(m, flush=True))


def _af3_docker_argv(
    input_dir: Path,
    output_dir: Path,
    *,
    name: str,
    run_data_pipeline: bool,
    run_inference: bool,
    gpu: str | None = None,
) -> list[str]:
    device = str(gpu) if gpu is not None else str(_AF3_GPU)
    argv = [
        "docker",
        "run",
        "--rm",
        "--name",
        name,
        "--gpus",
        f"device={device}",
        "--shm-size",
        "8g",
        "--ulimit",
        "memlock=-1",
    ]
    in_m, out_m, models_m, dbs_m = (
        "/tmp/af_input",
        "/tmp/af_output",
        "/tmp/models",
        "/tmp/public_databases",
    )
    if _AF3_DOCKER_USER:
        argv.extend(["--user", _AF3_DOCKER_USER, "-e", "HOME=/tmp"])
    argv.extend(
        [
            "--volume",
            f"{input_dir}:{in_m}",
            "--volume",
            f"{output_dir}:{out_m}",
            "--volume",
            f"{_af3_asset_dir(_AF3_MODEL_DIR_ENV, 'checkpoints')}:{models_m}:ro",
            "--volume",
            f"{_af3_asset_dir(_AF3_DATABASE_DIR_ENV, 'public_databases')}:{dbs_m}:ro",
            _AF3_IMAGE,
            "python",
            "/app/alphafold/run_alphafold.py",
            f"--db_dir={dbs_m}",
            f"--model_dir={models_m}",
            f"--input_dir={in_m}",
            f"--output_dir={out_m}",
            f"--run_data_pipeline={'True' if run_data_pipeline else 'False'}",
            f"--run_inference={'True' if run_inference else 'False'}",
        ]
    )
    if run_data_pipeline:
        argv.extend(
            [
                f"--jackhmmer_n_cpu={_AF3_JACKHMMER_N_CPU}",
                f"--nhmmer_n_cpu={_AF3_NHMMER_N_CPU}",
            ]
        )
    if run_inference:
        argv.append(f"--num_diffusion_samples={NUM_DIFFUSION_SAMPLES}")
    return argv


def _run_docker(argv: list[str], label: str) -> None:
    print(f"[ab-af3] {label}", flush=True)
    print(f"[ab-af3]   {' '.join(argv)}", flush=True)
    subprocess.run(argv, check=True)


def _write_target_msa_input(msa_inputs: Path, target_seq: str, job_name: str) -> None:
    _reset_dir(msa_inputs)
    job = {
        "name": job_name,
        "modelSeeds": list(MODEL_SEEDS),
        "sequences": [
            {"protein": {"id": "A", "sequence": target_seq, "templates": []}},
        ],
        "dialect": "alphafold3",
        "version": 1,
    }
    _write_json(msa_inputs / f"{job_name}.json", job)


def _load_target_msa(msa_output: Path, job_name: str, target_seq: str) -> dict[str, Any]:
    data_path = msa_output / job_name / f"{job_name}_data.json"
    if not data_path.is_file():
        raise FileNotFoundError(f"MSA output missing: {data_path}")
    data = _read_json(data_path)
    protein = data["sequences"][0]["protein"]
    if protein.get("sequence") != target_seq:
        raise ValueError("Target MSA sequence mismatch")
    unpaired = protein.get("unpairedMsa")
    if not isinstance(unpaired, str) or not unpaired.strip():
        raise ValueError("Target MSA search result missing")
    return {
        "id": "A",
        "sequence": target_seq,
        "templates": [],
        "unpairedMsa": unpaired,
        "pairedMsa": protein.get("pairedMsa", "") or "",
    }


def _msa_job_name(target_seq: str) -> str:
    return f"target_msa_{_sha256_text(target_seq)[:16]}"


def _cache_roots(question_dir: Path | None) -> list[Path]:
    """Shared cache first; optional per-case ``tests/af3_target_msa`` fallback."""
    roots = [_SHARED_MSA_DIR]
    if question_dir is not None:
        local = Path(question_dir) / "tests" / "af3_target_msa"
        if local.resolve() != _SHARED_MSA_DIR.resolve():
            roots.append(local)
    return roots


def _cache_paths_in(root: Path, target_seq: str) -> tuple[Path, Path, str]:
    name = _msa_job_name(target_seq)
    return root / f"{name}_data.json", root / f"{name}.meta.json", name


def _cache_paths(question_dir: Path | None, target_seq: str) -> tuple[Path, Path, str]:
    """Primary (shared) cache paths used for writes."""
    return _cache_paths_in(_SHARED_MSA_DIR, target_seq)


def _try_precomputed_msa(question_dir: Path | None, target_seq: str) -> dict[str, Any] | None:
    if _AF3_FORCE_MSA:
        return None
    for root in _cache_roots(question_dir):
        data_path, meta_path, _name = _cache_paths_in(root, target_seq)
        if not data_path.is_file() or not meta_path.is_file():
            continue
        try:
            meta = _read_json(meta_path)
            # The AF3 data pipeline is deterministic and seed-independent:
            # ``modelSeeds`` only selects inference samples. A cache is valid
            # when it describes this exact sequence, so v1 caches recorded
            # under another seed stay reusable.
            if meta.get("schema_version") not in {1, 2}:
                continue
            if meta.get("sequence_sha256") != _sha256_text(target_seq):
                continue
            if meta.get("sequence_length") != len(target_seq):
                continue
            return _load_from_cached(data_path, target_seq)
        except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError):
            continue
    return None


def _load_from_cached(data_path: Path, target_seq: str) -> dict[str, Any]:
    data = _read_json(data_path)
    protein = data["sequences"][0]["protein"]
    if protein.get("sequence") != target_seq:
        raise ValueError("Cached target MSA sequence mismatch")
    unpaired = protein.get("unpairedMsa")
    if not isinstance(unpaired, str) or not unpaired.strip():
        raise ValueError("Cached target MSA missing")
    return {
        "id": "A",
        "sequence": target_seq,
        "templates": [],
        "unpairedMsa": unpaired,
        "pairedMsa": protein.get("pairedMsa", "") or "",
    }


def _save_precomputed_msa(
    question_dir: Path | None, target_seq: str, msa_output: Path, job_name: str
) -> Path:
    data_path, meta_path, cache_name = _cache_paths(question_dir, target_seq)
    src = msa_output / job_name / f"{job_name}_data.json"
    if not src.is_file():
        raise FileNotFoundError(f"MSA output missing for cache: {src}")
    data_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, data_path)
    _write_json(
        meta_path,
        {
            "schema_version": 2,
            "name": cache_name,
            "sequence_sha256": _sha256_text(target_seq),
            "sequence_length": len(target_seq),
            "pipeline": "alphafold3_data_pipeline",
            "msa_seed_independent": True,
            # Provenance only: the cache validates on sequence identity, not on
            # the inference seed of the run that produced it.
            "produced_with_model_seeds": list(MODEL_SEEDS),
        },
    )
    print(f"[ab-af3] cached target MSA -> {data_path}", flush=True)
    return data_path


def _write_complex_jobs(
    rows: list[dict[str, str]],
    columns: list[str],
    target_seq: str,
    af3_inputs: Path,
) -> list[dict[str, Any]]:
    _reset_dir(af3_inputs)
    records = []
    for row in rows:
        name = _job_name(row["name"], [row[column] for column in columns])
        sequences = [
            {"protein": {"id": "A", "sequence": target_seq, "templates": []}},
        ]
        binder_ids = ["B", "C", "D", "E"]
        for index, column in enumerate(columns):
            sequences.append(
                {
                    "protein": {
                        "id": binder_ids[index],
                        "sequence": row[column],
                        "templates": [],
                    }
                }
            )
        job = {
            "name": name,
            "modelSeeds": list(MODEL_SEEDS),
            "sequences": sequences,
            "dialect": "alphafold3",
            "version": 1,
        }
        rel = f"{name}.json"
        path = af3_inputs / rel
        _write_json(path, job)
        records.append(
            {
                "candidate": row["name"],
                "name": name,
                "input_file": rel,
                "input_sha256": _sha256_file(path),
                "binder_columns": list(columns),
            }
        )
    return records


def _assemble_infer_inputs(
    records: list[dict[str, Any]],
    af3_inputs: Path,
    target_msa: dict[str, Any],
    infer_inputs: Path,
    columns: list[str],
) -> None:
    _reset_dir(infer_inputs)
    for record in records:
        job = _read_json(af3_inputs / record["input_file"])
        n_binders = len(columns)
        if len(job["sequences"]) != 1 + n_binders:
            raise ValueError(f"{record['name']}: unexpected chain count")
        target = job["sequences"][0]["protein"]
        if target.get("sequence") != target_msa["sequence"]:
            raise ValueError(f"{record['name']}: target sequence mismatch")
        target["unpairedMsa"] = target_msa["unpairedMsa"]
        target["pairedMsa"] = target_msa.get("pairedMsa", "")
        target["templates"] = []
        for entity in job["sequences"][1:]:
            binder = entity["protein"]
            binder["unpairedMsa"] = ""
            binder["pairedMsa"] = ""
            binder["templates"] = []
        _write_json(infer_inputs / f"{job['name']}.json", job)


def _ranking_score_matches_summary(summary_score, full_score) -> bool:
    """Same AF3 rounding tolerance as peptide design ``benchmark.py``.

    Some AF3 builds round ``*_summary_confidences.json`` ranking scores to two
    decimals while ``ranking_scores.csv`` keeps full precision (e.g. 0.26 vs
    0.2590). Allow half of 1e-2 so rounding alone does not invalidate a job.
    """
    return math.isclose(float(summary_score), float(full_score), abs_tol=5e-3, rel_tol=0.0)


def _read_candidate_ranking(af3_output: Path, name: str) -> float:
    run = af3_output / name
    summary = run / f"{name}_summary_confidences.json"
    if not summary.is_file():
        raise FileNotFoundError(f"missing summary for {name}")
    conf = _read_json(summary)
    score = conf.get("ranking_score")
    if not isinstance(score, (int, float)) or not math.isfinite(score):
        raise ValueError(f"invalid ranking_score for {name}")
    ranking_path = next(
        (p for p in (run / "ranking_scores.csv", run / f"{name}_ranking_scores.csv") if p.is_file()),
        None,
    )
    if ranking_path is None:
        raise FileNotFoundError(f"missing ranking_scores for {name}")
    with ranking_path.open(newline="", encoding="utf-8") as handle:
        rankings = list(csv.DictReader(handle))
    wanted = {(s, n) for s in MODEL_SEEDS for n in range(NUM_DIFFUSION_SAMPLES)}
    observed = {(int(r["seed"]), int(r["sample"])) for r in rankings}
    if observed != wanted:
        raise ValueError(f"wrong sampling budget for {name}")
    csv_scores = [float(r["ranking_score"]) for r in rankings]
    best = max(csv_scores)
    if not _ranking_score_matches_summary(score, best):
        raise ValueError(f"summary ranking_score is not best sample for {name}")
    return float(best)


def _mean_ranking_scores(
    af3_output: Path, records: list[dict[str, Any]]
) -> tuple[float, dict[str, float], dict[str, float]]:
    """Protocol arithmetic: max over the five samples, clip to [0,1], mean / 10.

    Mirrors ``sequence_case_eval._af3_metrics`` for the released protocol; a
    missing candidate is an organizer error and is never dropped from the
    denominator.
    """
    raw: dict[str, float] = {}
    clipped: dict[str, float] = {}
    for record in records:
        value = _read_candidate_ranking(af3_output, record["name"])
        raw[record["candidate"]] = value
        clipped[record["candidate"]] = min(1.0, max(0.0, value))
    if len(clipped) != 10:
        raise ValueError("AF3 scoring requires all ten candidates; none is dropped from the denominator")
    mean = math.fsum(clipped.values()) / len(clipped)
    return mean, raw, clipped


def _print_commands(work: Path, msa_inputs: Path, msa_output: Path, infer_inputs: Path, af3_output: Path) -> None:
    gpus = _resolve_gpus()
    msa_gpu = gpus[0]
    bar = "-" * 72
    print(bar, flush=True)
    print("[ab-af3] AF3 auto-run disabled (POLARIS_AF3_AUTO=0)", flush=True)
    print(f"  work: {work}", flush=True)
    print(f"  GPUs: {','.join(gpus)}", flush=True)
    print(flush=True)
    print("  [1] MSA-only on target", flush=True)
    print(
        "    "
        + " ".join(
            _af3_docker_argv(
                msa_inputs,
                msa_output,
                name=f"datapro_{msa_gpu}",
                run_data_pipeline=True,
                run_inference=False,
                gpu=msa_gpu,
            )
        ),
        flush=True,
    )
    print(flush=True)
    print("  [2] Inference-only on complexes", flush=True)
    print(
        "    "
        + " ".join(
            _af3_docker_argv(
                infer_inputs,
                af3_output,
                name=f"infer_{msa_gpu}",
                run_data_pipeline=False,
                run_inference=True,
                gpu=msa_gpu,
            )
        ),
        flush=True,
    )
    print(bar, flush=True)


def evaluate_af3_mean(prediction: Any, question_dir, case_id: str, **kwargs) -> dict[str, Any]:
    """Validate CSV, run AF3 auto-pipeline, return mean ranking_score."""
    directory = Path(question_dir)
    case = normalize_case_id(case_id)
    # Organizer hash / inventory / template checks. The design score stays
    # None here (gold runtime identities are not frozen), so AF3 fills it in.
    base = evaluate_question(prediction, directory, case, **kwargs)
    if base.get("status") == "invalid_submission":
        return {
            "score": 0.0,
            "detail": {
                "status": "invalid_submission",
                "error": base.get("error"),
                "item_id": base.get("item_id"),
                "case_id": base.get("case_id"),
                "metric": "mean_af3_ranking_score",
            },
        }

    gold_path = directory / "tests" / "cases" / f"{case}.answer.json"
    gold = _gold(gold_path)
    protocol = _protocol(gold)
    csv_text = _prediction_csv(prediction)
    rows = _design_rows(csv_text, gold)
    columns = list(gold["sequence_columns"])
    input_row = _load_input_row(directory, case)
    target_seq = input_row.get("target_sequence") or ""
    if not isinstance(target_seq, str) or not target_seq.strip():
        raise ValueError("Organizer input is missing target_sequence")

    work = _work_dir(directory)
    candidates_path = work / "candidates.csv"
    candidates_path.write_text(csv_text if csv_text.endswith("\n") else csv_text + "\n", encoding="utf-8")

    af3_inputs = work / "af3_inputs"
    msa_inputs = work / "af3_msa" / "inputs"
    msa_output = work / "af3_msa" / "outputs"
    infer_inputs = work / "af3_infer" / "inputs"
    af3_output = work / "af3_output"
    report_path = work / "af3_report.json"

    records = _write_complex_jobs(rows, columns, target_seq, af3_inputs)
    manifest = {
        "item_id": gold["item_id"],
        "case_id": case,
        "metric": "mean_af3_ranking_score",
        "protocol_version": protocol["protocol_version"],
        "model_seeds": list(MODEL_SEEDS),
        "num_diffusion_samples": NUM_DIFFUSION_SAMPLES,
        "sample_selection": SAMPLE_SELECTION,
        "score_transform": SCORE_TRANSFORM,
        "candidate_aggregation": CANDIDATE_AGGREGATION,
        "case_aggregation": CASE_AGGREGATION,
        "target_sequence_sha256": _sha256_text(target_seq),
        "candidates_sha256": _sha256_file(candidates_path),
        "jobs": records,
    }
    _write_json(af3_inputs / "manifest.json", manifest)

    protocol_detail = {
        "protocol_version": protocol["protocol_version"],
        "model_seeds": list(MODEL_SEEDS),
        "num_diffusion_samples": NUM_DIFFUSION_SAMPLES,
        "sample_selection": SAMPLE_SELECTION,
        "score_transform": SCORE_TRANSFORM,
        "candidate_aggregation": CANDIDATE_AGGREGATION,
        "case_aggregation": CASE_AGGREGATION,
        "target_sequence_sha256": _sha256_text(target_seq),
    }

    _, _, cache_name = _cache_paths(directory, target_seq)
    target_msa = _try_precomputed_msa(directory, target_seq)

    if not _AF3_AUTO:
        # Still write MSA input + empty-MSA infer stubs for manual follow-up.
        _write_target_msa_input(msa_inputs, target_seq, cache_name)
        if target_msa is not None:
            _assemble_infer_inputs(records, af3_inputs, target_msa, infer_inputs, columns)
        else:
            # Placeholder infer inputs without MSA so operators see job shapes.
            _reset_dir(infer_inputs)
            for record in records:
                shutil.copy2(af3_inputs / record["input_file"], infer_inputs / record["input_file"])
        _print_commands(work, msa_inputs, msa_output, infer_inputs, af3_output)
        detail = {
            "status": "awaiting_af3",
            "metric": "mean_af3_ranking_score",
            "item_id": gold["item_id"],
            "case_id": case,
            **protocol_detail,
            "work_dir": str(work),
            "candidates_file": str(candidates_path),
            "af3_inputs_dir": str(af3_inputs),
            "target_msa_precomputed": target_msa is not None,
            "note": "POLARIS_AF3_AUTO=0; score is 0 until AF3 is run",
        }
        _write_json(report_path, {"score": 0.0, **detail})
        return {"score": 0.0, "detail": detail}

    gpus = _resolve_gpus()
    msa_gpu = gpus[0]
    print(
        f"[ab-af3] {gold['item_id']}/{case}: mean AF3 ranking_score pipeline "
        f"(GPUs={','.join(gpus)})",
        flush=True,
    )

    # Reuse prior AF3 outputs when the same candidates were already inferred.
    try:
        mean_score, raw_scores, clipped_scores = _mean_ranking_scores(af3_output, records)
        detail = {
            "status": "af3_reused",
            "metric": "mean_af3_ranking_score",
            "item_id": gold["item_id"],
            "case_id": case,
            "score": mean_score,
            **protocol_detail,
            "n_candidates": len(clipped_scores),
            "candidate_raw_ranking_score": raw_scores,
            "candidate_clipped_score": clipped_scores,
            "work_dir": str(work),
            "af3_output_dir": str(af3_output),
            "af3_gpus": list(gpus),
            "score_definition": (
                "mean over 10 candidates of clip(max ranking_score across the 5 samples, 0, 1) "
                "(target MSA + empty binder MSA; no developability/novelty/diversity)"
            ),
        }
        _write_json(report_path, detail)
        print(
            f"[ab-af3] {gold['item_id']}/{case}: reused AF3 output; "
            f"mean ranking_score = {mean_score:.4f}",
            flush=True,
        )
        return {"score": float(mean_score), "detail": detail}
    except (ValueError, FileNotFoundError, OSError, KeyError, TypeError) as exc:
        print(f"[ab-af3] cannot reuse prior AF3 output ({exc}); running pipeline", flush=True)

    if target_msa is None:
        print("[ab-af3] [1/3] target MSA search", flush=True)
        _write_target_msa_input(msa_inputs, target_seq, cache_name)
        _reset_dir(msa_output)
        _run_docker(
            _af3_docker_argv(
                msa_inputs,
                msa_output,
                name=f"datapro_{msa_gpu}",
                run_data_pipeline=True,
                run_inference=False,
                gpu=msa_gpu,
            ),
            f"MSA docker (GPU {msa_gpu})",
        )
        target_msa = _load_target_msa(msa_output, cache_name, target_seq)
        try:
            _save_precomputed_msa(directory, target_seq, msa_output, cache_name)
        except OSError as exc:
            print(f"[ab-af3] warning: could not cache MSA ({exc})", flush=True)
    else:
        print("[ab-af3] [1/3] reusing precomputed target MSA", flush=True)

    print("[ab-af3] [2/3] assemble infer inputs (target MSA + empty binder MSA)", flush=True)
    _assemble_infer_inputs(records, af3_inputs, target_msa, infer_inputs, columns)

    print("[ab-af3] [3/3] inference", flush=True)
    _reset_dir(af3_output)
    if run_inference_multi_gpu is not None:
        def _build_infer_argv(
            input_dir: Path, output_dir: Path, gpu: str, name: str
        ) -> list[str]:
            return _af3_docker_argv(
                input_dir,
                output_dir,
                name=name,
                run_data_pipeline=False,
                run_inference=True,
                gpu=gpu,
            )

        infer_meta = run_inference_multi_gpu(
            infer_inputs=infer_inputs,
            af3_output=af3_output,
            gpus=gpus,
            build_argv=_build_infer_argv,
            run_docker=_run_docker,
            work_root=work / "af3_infer",
            log=lambda m: print(m, flush=True),
        )
    else:
        _run_docker(
            _af3_docker_argv(
                infer_inputs,
                af3_output,
                name=f"infer_{msa_gpu}",
                run_data_pipeline=False,
                run_inference=True,
                gpu=msa_gpu,
            ),
            f"inference docker (GPU {msa_gpu})",
        )
        infer_meta = {"n_jobs": None, "n_gpus": 1, "gpus": [msa_gpu], "shards": []}

    mean_score, raw_scores, clipped_scores = _mean_ranking_scores(af3_output, records)
    detail = {
        "status": "af3_auto_scored",
        "metric": "mean_af3_ranking_score",
        "item_id": gold["item_id"],
        "case_id": case,
        "score": mean_score,
        **protocol_detail,
        "n_candidates": len(clipped_scores),
        "candidate_raw_ranking_score": raw_scores,
        "candidate_clipped_score": clipped_scores,
        "work_dir": str(work),
        "af3_output_dir": str(af3_output),
        "af3_gpus": list(gpus),
        "af3_inference_shards": infer_meta,
        "score_definition": (
            "mean over 10 candidates of clip(max ranking_score across the 5 samples, 0, 1) "
            "(target MSA + empty binder MSA; no developability/novelty/diversity)"
        ),
    }
    _write_json(report_path, detail)
    print(
        f"[ab-af3] {gold['item_id']}/{case}: mean ranking_score = {mean_score:.4f}",
        flush=True,
    )
    return {"score": float(mean_score), "detail": detail}


def score_af3_mean(prediction: Any, question_dir, case_id: str, **kwargs) -> dict[str, Any]:
    return evaluate_af3_mean(prediction, question_dir, case_id, **kwargs)


def collect_unique_targets(
    antibody_root: Path, *, items: tuple[str, ...] = ("AB04", "AB05")
) -> list[dict[str, Any]]:
    """One entry per unique target_sequence across expanded case dirs."""
    antibody_root = Path(antibody_root)
    by_seq: dict[str, dict[str, Any]] = {}
    for item in items:
        # Accept both layouts: ``AB04_case_01`` (v1) and
        # ``AB04-Molecular-Biology_case_01`` (phase 2 category names).
        pattern = re.compile(rf"^{re.escape(item)}(?:-[^_]+)?_case_(\d+)$")
        for directory in sorted(p for p in antibody_root.iterdir() if p.is_dir()):
            match = pattern.match(directory.name)
            if match is None:
                continue
            case = normalize_case_id(match.group(1))
            path = directory / "inputs" / f"{case}.csv"
            if not path.is_file():
                continue
            with path.open(newline="", encoding="utf-8") as handle:
                row = next(csv.DictReader(handle))
            seq = row["target_sequence"]
            if seq not in by_seq:
                by_seq[seq] = {
                    "target_sequence": seq,
                    "target_name": row.get("target_name", ""),
                    "job_name": _msa_job_name(seq),
                    "cases": [],
                    "items": set(),
                }
            by_seq[seq]["cases"].append(directory.name)
            by_seq[seq]["items"].add(item)
    out = []
    for entry in by_seq.values():
        entry["items"] = sorted(entry["items"])
        out.append(entry)
    return out


def precompute_target_msa(
    target_seq: str,
    *,
    label: str = "",
    work: Path | None = None,
    force: bool = False,
) -> Path:
    """Run AF3 MSA-only for one target; write shared cache. Returns data.json path."""
    data_path, meta_path, job_name = _cache_paths(None, target_seq)
    if not force and not _AF3_FORCE_MSA:
        cached = _try_precomputed_msa(None, target_seq)
        if cached is not None:
            print(f"[ab-af3] skip existing MSA cache: {data_path}", flush=True)
            return data_path

    tag = label or job_name
    work = Path(work) if work else Path(tempfile.gettempdir()) / "frontier_af3_ab_msa" / job_name
    msa_inputs = work / "inputs"
    msa_output = work / "outputs"
    print(f"[ab-af3] precompute MSA: {tag} (len={len(target_seq)})", flush=True)
    print(f"[ab-af3]   work: {work}", flush=True)
    _write_target_msa_input(msa_inputs, target_seq, job_name)
    _reset_dir(msa_output)
    msa_gpu = _resolve_gpus()[0]
    _run_docker(
        _af3_docker_argv(
            msa_inputs,
            msa_output,
            name=f"datapro_{msa_gpu}_{job_name[-8:]}",
            run_data_pipeline=True,
            run_inference=False,
            gpu=msa_gpu,
        ),
        f"MSA docker ({tag}, GPU {msa_gpu})",
    )
    _load_target_msa(msa_output, job_name, target_seq)  # validate
    return _save_precomputed_msa(None, target_seq, msa_output, job_name)


def precompute_ab0405_target_msas(
    antibody_root: Path,
    *,
    force: bool = False,
    work_root: Path | None = None,
) -> list[Path]:
    """Precompute shared MSA caches for all unique AB04/AB05 targets."""
    targets = collect_unique_targets(antibody_root)
    print(
        f"[ab-af3] unique targets: {len(targets)}; cache dir: {_SHARED_MSA_DIR}",
        flush=True,
    )
    paths = []
    for entry in targets:
        work = None
        if work_root is not None:
            work = Path(work_root) / entry["job_name"]
        label = f"{entry['target_name'] or 'target'} ({','.join(entry['items'])})"
        paths.append(
            precompute_target_msa(
                entry["target_sequence"],
                label=label,
                work=work,
                force=force,
            )
        )
    return paths


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--antibody-root",
        type=Path,
        default=_SCORING_DIR.parent,
        help="processed/antibody root (default: parent of scoring/)",
    )
    parser.add_argument(
        "--work-root",
        type=Path,
        default=None,
        help="scratch dir for AF3 MSA docker I/O (default: under /tmp)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="re-run MSA even when a valid shared cache exists",
    )
    args = parser.parse_args()
    written = precompute_ab0405_target_msas(
        args.antibody_root, force=args.force, work_root=args.work_root
    )
    for path in written:
        print(f"[ab-af3] ready: {path}", flush=True)
