"""Score classification (55), analogue comparison (30) and top-one (15).

score(prediction) returns a float in [0, 1]. No dependencies.
"""
import argparse
import json
from pathlib import Path

KEY = json.loads(Path(__file__).with_name("answer.json").read_text(encoding="utf-8"))
TOTAL_POINTS = KEY["scoring"]["total_points"]


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("Duplicate JSON key")
        out[key] = value
    return out


def reject_constant(value):
    raise ValueError("Nonfinite JSON constant")


def score_details(prediction):
    try:
        pred = json.loads(prediction, object_pairs_hook=unique_object,
                          parse_constant=reject_constant) if isinstance(prediction, str) else prediction
    except (ValueError, TypeError, RecursionError):
        pred = None
    if not isinstance(pred, dict) or not set(pred).issubset(KEY["answer"]):
        return {"score": 0.0, "points": 0.0, "total_points": TOTAL_POINTS,
                "details": {}, "error": "Expected strict JSON using only listed question IDs"}
    details = {}
    for qid, expected in KEY["answer"].items():
        config = KEY["scoring"]["items"][qid]
        value = pred.get(qid)
        valid = isinstance(value, str) and value in config["options"]
        points = config["points"] if valid and value == expected else 0
        details[qid] = {"valid": valid, "earned": points, "possible": config["points"]}
    points = sum(row["earned"] for row in details.values())
    return {"score": points / TOTAL_POINTS, "points": points, "total_points": TOTAL_POINTS, "details": details}


def score(prediction) -> float:
    return score_details(prediction)["score"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("response", type=Path)
    args = parser.parse_args()
    print(json.dumps(score_details(args.response.read_text(encoding="utf-8")), indent=2))
