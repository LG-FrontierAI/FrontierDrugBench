"""AF3 GPU discovery and multi-GPU inference sharding (peptide design scorers).

Environment
-----------
``POLARIS_AF3_GPUS``
    Comma-separated host GPU indices (``0,1,2``), ``auto`` (free GPUs via
    nvidia-smi; **default when unset**), or ``all``. Set to a single index
    (e.g. ``0``) to force one GPU.
``POLARIS_AF3_GPU``
    Fallback single-GPU index when nvidia-smi is unavailable (default ``0``).
``POLARIS_AF3_MAX_GPUS``
    Cap on how many GPUs may be used (default: ``4``). Applies to ``auto``,
    ``all``, and explicit lists.
``POLARIS_AF3_GPU_MEM_FREE_MB``
    Minimum free memory (MiB) for a GPU to count as available under ``auto``
    (default: ``8000``). If none qualify, fall back to least-loaded cards.
``POLARIS_AF3_GPU_UTIL_MAX``
    Maximum ``utilization.gpu`` (%) for ``auto`` (default: ``10``). Busy cards
    are skipped even if they still have free VRAM.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Callable, Sequence

_DEFAULT_MAX_GPUS = 4


def _parse_max_gpus() -> int:
    raw = os.environ.get("POLARIS_AF3_MAX_GPUS", "").strip()
    if not raw:
        return _DEFAULT_MAX_GPUS
    try:
        n = int(raw)
    except ValueError as e:
        raise ValueError(f"POLARIS_AF3_MAX_GPUS must be an int; got {raw!r}") from e
    if n < 1:
        raise ValueError(f"POLARIS_AF3_MAX_GPUS must be >= 1; got {n}")
    return n


def _mem_free_threshold_mb() -> int:
    raw = os.environ.get("POLARIS_AF3_GPU_MEM_FREE_MB", "8000").strip()
    try:
        return max(0, int(raw))
    except ValueError as e:
        raise ValueError(f"POLARIS_AF3_GPU_MEM_FREE_MB must be an int; got {raw!r}") from e


def _util_max_pct() -> int:
    raw = os.environ.get("POLARIS_AF3_GPU_UTIL_MAX", "10").strip()
    try:
        return max(0, min(100, int(raw)))
    except ValueError as e:
        raise ValueError(f"POLARIS_AF3_GPU_UTIL_MAX must be an int; got {raw!r}") from e


def query_nvidia_gpus() -> list[dict[str, int]]:
    """Return ``[{index, memory_free_mb, memory_total_mb, utilization}, ...]``.

    Empty list when ``nvidia-smi`` is missing or fails.
    """
    try:
        out = subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=index,memory.free,memory.total,utilization.gpu",
                "--format=csv,noheader,nounits",
            ],
            text=True,
            stderr=subprocess.DEVNULL,
            timeout=30,
        )
    except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return []

    gpus: list[dict[str, int]] = []
    for line in out.splitlines():
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 4:
            continue
        try:
            gpus.append(
                {
                    "index": int(parts[0]),
                    "memory_free_mb": int(float(parts[1])),
                    "memory_total_mb": int(float(parts[2])),
                    "utilization": int(float(parts[3])),
                }
            )
        except ValueError:
            continue
    return gpus


def _cap(gpus: list[str]) -> list[str]:
    return gpus[: _parse_max_gpus()]


def discover_af3_gpus(*, log: Callable[[str], None] | None = None) -> list[str]:
    """Resolve the GPU list for AF3 docker ``--gpus device=N``.

    Default (unset ``POLARIS_AF3_GPUS``) is ``auto``: pick idle GPUs up to
    ``POLARIS_AF3_MAX_GPUS``. Returns at least ``["0"]`` when discovery fails.
    """
    def _print(msg: str) -> None:
        if log is not None:
            log(msg)
        else:
            print(msg, flush=True)

    raw_gpus = os.environ.get("POLARIS_AF3_GPUS")
    legacy = os.environ.get("POLARIS_AF3_GPU", "0")

    # Unset → multi-GPU auto (capped). Explicit "0" / "1,2" still forces a list.
    if raw_gpus is None or not str(raw_gpus).strip():
        mode = "auto"
        _print(
            f"[af3-gpus] POLARIS_AF3_GPUS unset → auto "
            f"(max={_parse_max_gpus()}; set POLARIS_AF3_GPUS=0 for single GPU)"
        )
    else:
        mode = str(raw_gpus).strip()

    if mode.lower() not in {"auto", "all"}:
        gpus = [g.strip() for g in mode.split(",") if g.strip()]
        if not gpus:
            gpus = ["0"]
        gpus = _cap(gpus)
        _print(f"[af3-gpus] using POLARIS_AF3_GPUS={','.join(gpus)}")
        return gpus

    info = query_nvidia_gpus()
    if not info:
        fallback = [str(legacy).strip()] if legacy and str(legacy).strip() else ["0"]
        _print(
            f"[af3-gpus] nvidia-smi unavailable; falling back to GPU {fallback[0]}"
        )
        return fallback

    if mode.lower() == "all":
        gpus = _cap([str(g["index"]) for g in info])
        _print(f"[af3-gpus] POLARIS_AF3_GPUS=all → {','.join(gpus)}")
        return gpus

    thresh = _mem_free_threshold_mb()
    util_max = _util_max_pct()
    free = [
        g
        for g in info
        if g["memory_free_mb"] >= thresh and g["utilization"] <= util_max
    ]
    if free:
        free.sort(key=lambda g: (g["utilization"], -g["memory_free_mb"], g["index"]))
        gpus = _cap([str(g["index"]) for g in free])
        detail = ", ".join(
            f"{g['index']}(free={g['memory_free_mb']}MiB,util={g['utilization']}%)"
            for g in info
            if str(g["index"]) in set(gpus)
        )
        _print(
            f"[af3-gpus] auto-selected {len(gpus)} GPU(s): {detail} "
            f"(mem≥{thresh}MiB, util≤{util_max}%, max={_parse_max_gpus()})"
        )
        return gpus

    mem_ok = [g for g in info if g["memory_free_mb"] >= thresh]
    pool = mem_ok or info
    pool.sort(key=lambda g: (g["utilization"], -g["memory_free_mb"], g["index"]))
    gpus = _cap([str(g["index"]) for g in pool])
    detail = ", ".join(
        f"{g['index']}(free={g['memory_free_mb']}MiB,util={g['utilization']}%)"
        for g in info
        if str(g["index"]) in set(gpus)
    )
    _print(
        f"[af3-gpus] no idle GPU (mem≥{thresh}MiB & util≤{util_max}%); "
        f"falling back to least-loaded: {detail}"
    )
    return gpus


def shard_round_robin(items: Sequence[Path], n: int) -> list[list[Path]]:
    """Split ``items`` into ``n`` buckets (some may be empty)."""
    if n < 1:
        raise ValueError("n must be >= 1")
    buckets: list[list[Path]] = [[] for _ in range(n)]
    for i, item in enumerate(items):
        buckets[i % n].append(item)
    return buckets


def run_inference_multi_gpu(
    *,
    infer_inputs: Path,
    af3_output: Path,
    gpus: Sequence[str],
    build_argv: Callable[[Path, Path, str, str], list[str]],
    run_docker: Callable[[list[str], str], None],
    work_root: Path | None = None,
    log: Callable[[str], None] | None = None,
) -> dict[str, object]:
    """Shard ``infer_inputs/*.json`` across ``gpus`` and run AF3 inference in parallel."""
    def _print(msg: str) -> None:
        if log is not None:
            log(msg)
        else:
            print(msg, flush=True)

    jobs = sorted(infer_inputs.glob("*.json"))
    if not jobs:
        _print("[af3-gpus] no inference JSON jobs; skipping")
        return {"n_jobs": 0, "n_gpus": 0, "gpus": [], "shards": []}

    gpu_list = [str(g) for g in gpus if str(g).strip()]
    if not gpu_list:
        gpu_list = ["0"]

    n_workers = min(len(gpu_list), len(jobs))
    gpu_list = gpu_list[:n_workers]
    buckets = shard_round_robin(jobs, n_workers)

    shard_root = (work_root or infer_inputs.parent) / "shards"
    if shard_root.exists():
        shutil.rmtree(shard_root)
    shard_root.mkdir(parents=True, exist_ok=True)
    af3_output.mkdir(parents=True, exist_ok=True)

    shard_meta: list[dict[str, object]] = []
    for gpu, bucket in zip(gpu_list, buckets):
        if not bucket:
            continue
        shard_in = shard_root / f"gpu_{gpu}" / "inputs"
        shard_in.mkdir(parents=True, exist_ok=True)
        for src in bucket:
            dest = shard_in / src.name
            if dest.exists() or dest.is_symlink():
                dest.unlink()
            # Copy (not symlink): docker only mounts shard_in, so absolute
            # symlinks to the parent infer_inputs tree are broken inside the
            # container and AF3 exits with empty af3_output.
            shutil.copy2(src, dest)
        shard_meta.append({"gpu": gpu, "n_jobs": len(bucket), "input_dir": str(shard_in)})

    shard_summary = ", ".join(f"gpu{s['gpu']}:{s['n_jobs']}" for s in shard_meta)
    _print(
        f"[af3-gpus] inference: {len(jobs)} job(s) across {len(shard_meta)} GPU(s) "
        f"[{shard_summary}]"
    )

    def _one(meta: dict[str, object]) -> None:
        gpu = str(meta["gpu"])
        shard_in = Path(str(meta["input_dir"]))
        name = f"infer_{gpu}_{os.getpid()}"
        argv = build_argv(shard_in, af3_output, gpu, name)
        run_docker(argv, f"inference docker (GPU {gpu}, {meta['n_jobs']} jobs)")

    if len(shard_meta) == 1:
        _one(shard_meta[0])
    else:
        with ThreadPoolExecutor(max_workers=len(shard_meta)) as ex:
            futs = {ex.submit(_one, m): m for m in shard_meta}
            errors: list[str] = []
            for fut in as_completed(futs):
                meta = futs[fut]
                try:
                    fut.result()
                except Exception as exc:  # noqa: BLE001
                    errors.append(f"gpu={meta['gpu']}: {type(exc).__name__}: {exc}")
            if errors:
                raise RuntimeError(
                    "AF3 multi-GPU inference failed on " + "; ".join(errors)
                )

    # AF3 writes one subdirectory per job name; empty output usually means the
    # container never saw the inputs (e.g. broken mounts) but still exited 0.
    produced = [p for p in af3_output.iterdir() if p.is_dir()] if af3_output.is_dir() else []
    if not produced:
        raise RuntimeError(
            f"AF3 inference produced no outputs under {af3_output} "
            f"({len(jobs)} input job(s) on GPU(s) {[s['gpu'] for s in shard_meta]})"
        )
    _print(f"[af3-gpus] inference outputs: {len(produced)}/{len(jobs)} job dir(s) under {af3_output}")

    return {
        "n_jobs": len(jobs),
        "n_gpus": len(shard_meta),
        "gpus": [str(s["gpu"]) for s in shard_meta],
        "shards": shard_meta,
        "n_output_dirs": len(produced),
    }
