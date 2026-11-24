"""the harness entry point for one held-out benchmark structure case.

The organizer scorer is vendored unchanged at ``tests/reference/score.py`` and
resolves its ``input/``, ``case/`` and ``test/`` payload relative to itself. This
wrapper only puts the family ``_scoring`` package on ``sys.path`` and re-exports
the organizer's ``evaluate`` / ``score``; no grading logic is reimplemented.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FAMILY = HERE.parents[1] / "_packages"
REFERENCE = HERE / "reference"

if str(FAMILY) not in sys.path:
    sys.path.insert(0, str(FAMILY))

_NAME = "_frontier_structure_" + HERE.parent.name.replace("-", "_")
_spec = importlib.util.spec_from_file_location(_NAME, REFERENCE / "score.py")
_impl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_impl)

CASE_ID = _impl.CASE_ID


def evaluate(prediction, case_id=None, **kwargs):
    return _impl.evaluate(prediction, case_id=case_id, **kwargs)


def score(prediction, case_id=None, **kwargs):
    return float(_impl.score(prediction, case_id=case_id, **kwargs))
