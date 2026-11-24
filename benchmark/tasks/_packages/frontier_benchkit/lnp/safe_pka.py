"""Launch QupKake pKa without leaving the process cwd on a deleted temp dir.

QupKake's ``xtbp.RunXTB._run_xtb`` does ``os.chdir(tmp)`` inside
``TemporaryDirectory``. On some exception paths the temp dir is removed while
it is still the process cwd; later ``os.getcwd()`` (e.g. Lightning Trainer)
raises ``FileNotFoundError``. Keep a stable cwd and restore it around temp dirs.
"""
from __future__ import annotations

import os
import runpy
import sys
import tempfile
from pathlib import Path


def _cap_xtb_threads(n: int = 4) -> None:
    """QupKake passes ``cpu_count()`` into xtb ``-P`` even when ``mp=False``."""
    import multiprocessing

    n = max(1, int(os.environ.get("TLNP_XTB_THREADS", n)))
    os.environ.setdefault("OMP_NUM_THREADS", str(n))
    os.environ.setdefault("MKL_NUM_THREADS", str(n))
    multiprocessing.cpu_count = lambda: n  # type: ignore[assignment]


def _install_cwd_guards(stable: Path) -> None:
    stable_s = str(stable.resolve())
    os.makedirs(stable_s, exist_ok=True)
    os.chdir(stable_s)
    _cap_xtb_threads()

    real_getcwd = os.getcwd
    real_chdir = os.chdir

    def safe_getcwd() -> str:
        try:
            return real_getcwd()
        except FileNotFoundError:
            real_chdir(stable_s)
            return stable_s

    def safe_chdir(path: os.PathLike[str] | str) -> None:
        try:
            real_chdir(path)
        except FileNotFoundError:
            real_chdir(stable_s)
            real_chdir(path)

    os.getcwd = safe_getcwd  # type: ignore[assignment]
    os.chdir = safe_chdir  # type: ignore[assignment]

    orig_td = tempfile.TemporaryDirectory

    class _SafeTemporaryDirectory(orig_td):  # type: ignore[misc,valid-type]
        def __exit__(self, *args):
            try:
                real_chdir(stable_s)
            except Exception:  # noqa: BLE001
                pass
            return orig_td.__exit__(self, *args)

    tempfile.TemporaryDirectory = _SafeTemporaryDirectory  # type: ignore[misc,assignment]


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) < 2:
        print("usage: safe_pka.py STABLE_CWD RUN_PY [run.py args...]", file=sys.stderr)
        return 2
    stable = Path(args[0])
    run_py = Path(args[1])
    _install_cwd_guards(stable)
    sys.argv = [str(run_py), *args[2:]]
    try:
        runpy.run_path(str(run_py), run_name="__main__")
    except SystemExit as exc:
        code = exc.code
        if code is None:
            return 0
        if isinstance(code, int):
            return code
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
