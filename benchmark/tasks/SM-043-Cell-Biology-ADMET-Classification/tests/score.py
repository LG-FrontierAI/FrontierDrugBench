"""Portable ADMET composite scorer; Python standard library only."""
import argparse
import json
from pathlib import Path

KEY = json.loads((Path(__file__).resolve().parent / 'answer.json').read_text(encoding='utf-8'))
GOLD = KEY['answer']
CONFIG = KEY['scoring']


def unique_object(pairs):
    result = {}
    for k, v in pairs:
        if k in result:
            raise ValueError('Duplicate JSON key')
        result[k] = v
    return result


def parse(value):
    if isinstance(value, str):
        try:
            return json.loads(value, object_pairs_hook=unique_object,
                              parse_constant=lambda _: (_ for _ in ()).throw(ValueError('Nonfinite JSON')))
        except (ValueError, TypeError, RecursionError):
            return None
    return value


def valid_list(value, candidates, length):
    return (isinstance(value, list) and len(value) == length
            and all(isinstance(v, str) for v in value)
            and len(set(value)) == length and set(value) <= set(candidates))


def score_details(prediction):
    pred = parse(prediction)
    total = CONFIG['raw_total_points']
    if not isinstance(pred, dict) or not set(pred) <= set(GOLD):
        return dict(score=0.0, points=0.0, raw_points=0.0, raw_total_points=total,
                    total_points=100, details={}, error='Expected JSON object using only listed question IDs')
    details = {}
    for qid, item in CONFIG['items'].items():
        p, a = pred.get(qid), GOLD[qid]
        candidates = item['candidates']
        kind = item['type']
        fraction, valid = 0.0, False
        if kind in ('interval', 'profile'):
            valid = isinstance(p, dict) and set(p) <= set(candidates)
            if valid:
                hits = 0
                for mid, expected in a.items():
                    value = p.get(mid)
                    if kind == 'interval':
                        hits += isinstance(value, str) and value == expected
                    elif valid_list(value, item['isoform_options'][mid], len(value) if isinstance(value, list) else -1):
                        hits += set(value) == set(expected)
                fraction = hits / len(a)
        elif kind == 'pair':
            valid = isinstance(p, str) and p in candidates
            fraction = float(valid and p == a)
        elif kind == 'top2':
            valid = valid_list(p, candidates, 2)
            if valid:
                fraction = len(set(p) & set(a)) / 2
        elif kind == 'rank':
            valid = valid_list(p, candidates, len(candidates))
            if valid:
                positions = {mid: i for i, mid in enumerate(p)}
                pairs = item['scored_relations']
                fraction = sum(positions[x] < positions[y] for x, y in pairs) / len(pairs)
        else:
            raise ValueError('Unsupported question type')
        earned = item['raw_points'] * fraction
        details[qid] = dict(valid=valid, raw_earned=earned, raw_possible=item['raw_points'],
                            earned=earned * 100 / total, possible=item['raw_points'] * 100 / total)
    raw = sum(row['raw_earned'] for row in details.values())
    normalized = max(0.0, min(1.0, raw / total))
    return dict(score=normalized, points=normalized * 100, total_points=100,
                raw_points=raw, raw_total_points=total, details=details)


def score(prediction) -> float:
    return score_details(prediction)['score']


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('response', type=Path)
    args = ap.parse_args()
    print(json.dumps(score_details(args.response.read_text(encoding='utf-8')),
                     ensure_ascii=False, indent=2, allow_nan=False))
