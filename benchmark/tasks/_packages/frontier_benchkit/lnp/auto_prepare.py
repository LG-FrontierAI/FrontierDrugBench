"""Prepare evaluator ``tool_results.json`` (aligned with raw ``run_benchmark``).

- Extraction (P20-17): RDKit ``collect`` only.
- Generation (design tasks): IL + QupKake **on by default** (same effect as
  ``bash run_model.sh --run-molecular``). Set ``TLNP_RUN_MOLECULAR=0`` to skip
  and leave ``molecular_pending`` (writes ``molecular_commands.json`` for a
  later rescore once ``il_results.csv`` / ``pka_results.json`` exist).
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any


class MolecularPending(Exception):
    """Generation tools not run; mirrors raw ``status=molecular_pending``."""


def _pkg() -> Path:
    return Path(__file__).resolve().parent


def _lnp_root() -> Path:
    return _pkg().parent


def scoring_tools_root() -> Path:
    env = os.environ.get("LNP_SCORING_TOOLS") or os.environ.get("TLNP_SCORING_TOOLS")
    if env:
        return Path(env).expanduser().resolve()
    return (
        _lnp_root().parents[1]
        / "raw"
        / "lnp"
        / "20261026"
        / "final_package_20261026"
        / "scoring_tools"
    ).resolve()


_OLD_SCORING_TOOLS = (
    _lnp_root().parents[1]
    / "raw"
    / "lnp"
    / "20261023"
    / "final_package_20261023"
    / "scoring_tools"
).resolve()


def tools_python() -> str:
    """Interpreter that can import torch/rdkit for the IL + QupKake models.

    Order: ``LNP_TOOLS_PYTHON`` override -> this package's
    ``linux_submission/.venv`` -> the 20261023 package venv (same dependency
    set; ``run.py doctor`` passes) -> this interpreter.
    """
    env = os.environ.get("LNP_TOOLS_PYTHON")
    if env and Path(env).expanduser().is_file():
        return str(Path(env).expanduser())
    for candidate in (scoring_tools_root(), _OLD_SCORING_TOOLS):
        venv = candidate / "linux_submission" / ".venv" / "bin" / "python"
        if venv.is_file():
            return str(venv)
    return sys.executable


def run_molecular_enabled() -> bool:
    """Whether to run IL + QupKake for generation scoring.

    Default **on** (the harness score path). Opt out with ``TLNP_RUN_MOLECULAR=0``
    (or ``false`` / ``no`` / ``off``) to mirror raw README without ``--run-molecular``.
    """
    raw = os.environ.get("TLNP_RUN_MOLECULAR")
    if raw is None or not str(raw).strip():
        return True
    return str(raw).strip().lower() not in {"0", "false", "no", "off"}


def work_dir(question_id: str, pred: dict) -> Path:
    digest = hashlib.sha1(
        json.dumps(pred, ensure_ascii=False, sort_keys=True, allow_nan=False).encode("utf-8")
    ).hexdigest()[:12]
    item = os.environ.get("POLARIS_ITEM_DIR")
    out = os.environ.get("POLARIS_OUT_DIR")
    candidates: list[Path] = []
    if item:
        candidates.append(Path(item).expanduser().resolve() / "work" / digest)
    if out:
        base = Path(out).expanduser().resolve()
        candidates.append(base / "items" / question_id / "work" / digest)
        candidates.append(base / "tlnp_tools" / question_id / digest)
    candidates.append(_lnp_root() / ".tool_cache" / question_id / digest)

    def _ready(path: Path) -> bool:
        return (path / "tool_results.json").is_file() or (
            (path / "il_results.csv").is_file() and (path / "pka_results.json").is_file()
        )

    for path in candidates:
        if _ready(path):
            return path
    root = candidates[0]
    root.mkdir(parents=True, exist_ok=True)
    return root


def _save(path: Path, data: Any) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def _run(
    cmd: list[str],
    log: Path,
    *,
    cwd: Path | None = None,
    env: dict[str, str] | None = None,
) -> None:
    log.parent.mkdir(parents=True, exist_ok=True)
    work = Path(cwd) if cwd else log.parent
    work.mkdir(parents=True, exist_ok=True)
    with log.open("w", encoding="utf-8") as stream:
        stream.write("$ " + " ".join(cmd) + "\n\n")
        stream.flush()
        proc = subprocess.run(
            cmd,
            cwd=str(work),
            stdout=stream,
            stderr=subprocess.STDOUT,
            env=env,
        )
    if proc.returncode != 0:
        raise RuntimeError(f"command failed ({proc.returncode}): {' '.join(cmd)}; see {log}")


def _pka_workers(n_mols: int) -> int:
    """How many molecule-level pKa jobs to run at once.

    Default: one worker per design molecule (``n_mols``).
    Override with ``TLNP_PKA_WORKERS`` (``1`` = serial).
    """
    raw = os.environ.get("TLNP_PKA_WORKERS")
    if raw is not None and str(raw).strip():
        return max(1, min(n_mols, int(str(raw).strip())))
    return max(1, n_mols)


def _merge_sdfs(paths: list[Path], dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("wb") as out:
        for path in paths:
            if not path.is_file():
                raise RuntimeError(f"missing pKa SDF: {path}")
            out.write(path.read_bytes())


def _run_pka_parallel(
    *,
    python: str,
    tool: Path,
    eligible: list[dict[str, str]],
    folder: Path,
    pka_root: Path,
    pka_out: Path,
) -> None:
    """Run one QupKake job per molecule (parallel), then merge SDFs + summarize."""
    workers = _pka_workers(len(eligible))
    safe_pka = _pkg() / "safe_pka.py"
    shards = folder / "pka_shards"
    if shards.exists():
        shutil.rmtree(shards)
    shards.mkdir(parents=True, exist_ok=True)
    if pka_root.exists():
        shutil.rmtree(pka_root)

    # Per-job xtb threads: keep low when several molecules run together.
    job_env = os.environ.copy()
    if workers > 1 and "TLNP_XTB_THREADS" not in job_env:
        job_env["TLNP_XTB_THREADS"] = "1"

    jobs: list[tuple[str, list[str], Path, Path]] = []
    for row in eligible:
        name = str(row["name"])
        shard = shards / name
        shard.mkdir(parents=True, exist_ok=True)
        csv_path = shard / "molecules.csv"
        with csv_path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=["name", "smiles"])
            writer.writeheader()
            writer.writerow({"name": name, "smiles": row["smiles"]})
        shard_root = shard / "pka_run"
        log = shard / "pka.log"
        cmd = [
            python,
            str(safe_pka),
            str(shard),
            str(tool),
            "pka",
            "file",
            str(csv_path),
            "-r",
            str(shard_root),
            "-s",
            "smiles",
            "-n",
            "name",
            "-o",
            "prediction.sdf",
        ]
        jobs.append((name, cmd, log, shard_root / "output" / "prediction.sdf"))

    (folder / "pka.log").write_text(
        f"parallel pKa: {len(jobs)} molecules, workers={workers}, "
        f"TLNP_XTB_THREADS={job_env.get('TLNP_XTB_THREADS', '(unset)')}\n",
        encoding="utf-8",
    )

    def _one(job: tuple[str, list[str], Path, Path]) -> str:
        name, cmd, log, _sdf = job
        _run(cmd, log, cwd=Path(cmd[2]), env=job_env)
        return name

    if workers == 1:
        for job in jobs:
            _one(job)
    else:
        errors: list[str] = []
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(_one, job): job[0] for job in jobs}
            for fut in as_completed(futures):
                name = futures[fut]
                try:
                    fut.result()
                except Exception as exc:  # noqa: BLE001
                    errors.append(f"{name}: {exc}")
        if errors:
            raise RuntimeError("parallel pKa failed:\n" + "\n".join(errors))

    sdf_paths = [j[3] for j in jobs]
    merged = pka_root / "output" / "prediction.sdf"
    _merge_sdfs(sdf_paths, merged)
    _run(
        [
            python,
            str(tool),
            "summarize",
            "--sdf",
            str(merged),
            "--output",
            str(pka_out),
        ],
        folder / "summarize.log",
        cwd=folder,
    )


def _ensure_xtb_executable() -> None:
    xtb = (
        scoring_tools_root()
        / "linux_submission"
        / "QupKake"
        / "qupkake"
        / "xtb-641"
        / "bin"
        / "xtb"
    )
    if xtb.is_file() and not os.access(xtb, os.X_OK):
        xtb.chmod(xtb.stat().st_mode | 0o111)


def ensure_tool_results(pred: dict, gold: dict, *, task_dir: Path) -> Path:
    """Build or reuse ``tool_results.json``.

    Raises :class:`MolecularPending` when generation scoring needs IL/pKa but
    molecular tools are disabled (``TLNP_RUN_MOLECULAR=0``) and cached outputs
    are missing.
    """
    mode = gold.get("mode")
    if mode not in ("generation", "extraction"):
        raise ValueError(f"unsupported mode for auto_prepare: {mode!r}")

    folder = work_dir(str(gold["id"]), pred)
    tools_path = folder / "tool_results.json"
    if tools_path.is_file():
        cached = json.loads(tools_path.read_text(encoding="utf-8-sig"))
        if cached.get("question_id") == gold["id"] and cached.get("prediction") == pred:
            return tools_path

    pred_path = folder / "prediction.json"
    _save(pred_path, pred)
    python = tools_python()
    helper = str(_pkg() / "prepare_tools.py")
    question = str(task_dir.resolve())

    if mode == "extraction":
        _run(
            [
                python,
                helper,
                "collect",
                "--question",
                question,
                "--prediction",
                str(pred_path),
                "--output",
                str(tools_path),
            ],
            folder / "collect.log",
        )
        return tools_path

    # generation — same stages as run_benchmark.prepare_generation
    molecules = folder / "molecules.csv"
    _run(
        [
            python,
            helper,
            "prepare",
            "--question",
            question,
            "--prediction",
            str(pred_path),
            "--output",
            str(molecules),
        ],
        folder / "prepare.log",
    )
    with molecules.open(encoding="utf-8-sig", newline="") as stream:
        eligible = list(csv.DictReader(stream))

    il = folder / "il_results.csv"
    pka = folder / "pka_results.json"
    root = scoring_tools_root()
    tool = root / "linux_submission" / "run.py"
    pka_root = folder / "pka_run"
    commands = [
        [
            python,
            str(tool),
            "il",
            "--input",
            str(molecules),
            "--smiles-column",
            "smiles",
            "--output",
            str(il),
        ],
        [
            python,
            str(_pkg() / "safe_pka.py"),
            str(folder),
            str(tool),
            "pka",
            "file",
            str(molecules),
            "-r",
            str(pka_root),
            "-s",
            "smiles",
            "-n",
            "name",
            "-o",
            "prediction.sdf",
        ],
        [
            python,
            str(tool),
            "summarize",
            "--sdf",
            str(pka_root / "output" / "prediction.sdf"),
            "--output",
            str(pka),
        ],
    ]

    if not eligible:
        il.write_text("status,smiles,il_likeness\n", encoding="utf-8")
        _save(pka, [])
    elif not (il.is_file() and pka.is_file()):
        if not run_molecular_enabled():
            _save(folder / "molecular_commands.json", [[str(x) for x in cmd] for cmd in commands])
            raise MolecularPending(
                "Supply il_results.csv and pka_results.json, then rescore; "
                "or unset TLNP_RUN_MOLECULAR / set TLNP_RUN_MOLECULAR=1 "
                "(molecular tools are on by default)"
            )
        if sys.platform != "linux":
            raise RuntimeError(
                "Automatic molecular reference execution requires Linux; "
                "provide il_results.csv / pka_results.json and rescore"
            )
        if not tool.is_file():
            raise FileNotFoundError(f"missing molecular tools: {tool}")
        _ensure_xtb_executable()
        if not il.is_file():
            _run(commands[0], folder / "il.log", cwd=folder)
        if not pka.is_file():
            _run_pka_parallel(
                python=python,
                tool=tool,
                eligible=eligible,
                folder=folder,
                pka_root=pka_root,
                pka_out=pka,
            )

    _run(
        [
            python,
            helper,
            "collect",
            "--question",
            question,
            "--prediction",
            str(pred_path),
            "--il-results",
            str(il),
            "--pka-results",
            str(pka),
            "--output",
            str(tools_path),
        ],
        folder / "collect.log",
    )
    return tools_path
