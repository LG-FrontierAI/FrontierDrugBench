"""MCQ: require exactly one answer letter, ignoring surrounding whitespace/case."""

import json
from pathlib import Path

GOLD = json.loads((Path(__file__).resolve().parent / "answer.json").read_text(encoding="utf-8"))[
    "answer"
]
if not isinstance(GOLD, str) or GOLD.strip().upper() not in {"A", "B", "C", "D"}:
    raise ValueError("answer.json must contain exactly one answer letter A, B, C, or D")
GOLD = GOLD.strip().upper()


def score(prediction: str) -> float:
    if not isinstance(prediction, str):
        return 0.0
    pred = prediction.strip().upper()
    return 1.0 if pred in {"A", "B", "C", "D"} and pred == GOLD else 0.0


if __name__ == "__main__":
    print({"gold": GOLD, "score": score(GOLD)})
