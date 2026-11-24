"""Score categorical, analogue-comparison and within-series ordering items.

Only Python's standard library is required. score(prediction) returns 0–1.
"""
import argparse
import json
from pathlib import Path

KEY = json.loads(Path(__file__).with_name('answer.json').read_text(encoding='utf-8'))


def unique_object(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError('Duplicate JSON key')
        obj[key] = value
    return obj


def reject_constant(value):
    raise ValueError('Nonfinite JSON constant')


def ordering_score(response, expected):
    if (not isinstance(response, list) or len(response) != len(expected)
            or any(not isinstance(x, str) for x in response)
            or len(set(response)) != len(response) or set(response) != set(expected)):
        return None
    positions = {mid: i for i, mid in enumerate(response)}
    n = len(expected)
    rho = 1 - 6 * sum((i - positions[mid]) ** 2 for i, mid in enumerate(expected)) / (n * (n * n - 1))
    return max(0.0, rho)


def score_details(prediction):
    try:
        obj = (json.loads(prediction, object_pairs_hook=unique_object, parse_constant=reject_constant)
               if isinstance(prediction, str) else prediction)
    except (ValueError, TypeError, RecursionError):
        obj = None
    gold = KEY['answer']
    if not isinstance(obj, dict) or not set(obj).issubset(gold):
        return dict(score=0.0, points=0.0, total_points=100, details={},
                    error='Expected a JSON object containing only the listed question IDs.')
    details = {}
    for qid, item in KEY['scoring']['items'].items():
        value, expected = obj.get(qid), gold[qid]
        if item['type'] == 'ordering':
            fraction = ordering_score(value, expected)
            valid = fraction is not None
            fraction = fraction if valid else 0.0
        else:
            valid = isinstance(value, str) and value in item['options']
            fraction = float(valid and value == expected)
        details[qid] = dict(type=item['type'], valid=valid, fraction=fraction,
                            points=fraction * item['points'], max_points=item['points'])
    points = sum(item['points'] for item in details.values())
    return dict(score=points / 100, points=points, total_points=100, details=details)


def score(prediction):
    return score_details(prediction)['score']


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('response', type=Path)
    args = parser.parse_args()
    print(json.dumps(score_details(args.response.read_text(encoding='utf-8')), indent=2))
