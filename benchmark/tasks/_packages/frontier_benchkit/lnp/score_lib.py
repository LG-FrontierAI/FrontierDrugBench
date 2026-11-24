"""Standard-library scorers for evidence-backed LNP expansion tasks (scoring v2).

v2 goals
--------
* No integer steps or large atoms: every metric returns a fraction in [0, 1] with
  partial credit for near-misses where the underlying quantity is graded.
* A no-skill answer scores 0; a perfect answer scores the full metric weight.
  Order-based metrics use pairwise concordance rather than clipped Spearman, so an
  ordering that is closer than a random shuffle keeps proportional credit.
* Numeric prediction counts both rank information and absolute calibration; the old
  scale rewarded copying a visible proxy that had good correlation but poor values.
* Schema tolerance matches what questions actually ask (per-field reasons, declared
  choice aliases, a single wrapper object around a numeric answer).

This module contains no experimental data. Four-turn tasks retain the
runner-compatible turns_answers.json contract; metric keys and weights are declared
in each gold file.
"""
from __future__ import annotations
import argparse
import json
import math
import re
from pathlib import Path

SCORING_VERSION = 'v2'


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def finite(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError('Expected a finite numeric value, got ' + type(value).__name__)
    return float(value)


def unwrap_number(value, key):
    """Accept the number itself or exactly one wrapper object holding it.

    Several questions ask for a named statistic; models sometimes return
    {"correlation": {"correlation": 0.63, "reason": "..."}}. Only a unique numeric
    field is accepted: anything ambiguous stays an error.
    """
    if isinstance(value, dict):
        candidates = []
        for name in dict.fromkeys((key, key + '_value', 'value', 'result')):
            if name in value and not isinstance(value[name], (dict, list)):
                candidates.append(value[name])
        if len(candidates) == 1:
            return candidates[0]
        numeric = [v for v in value.values()
                   if isinstance(v, (int, float)) and not isinstance(v, bool)]
        if len(numeric) == 1 and len(candidates) <= 1:
            return numeric[0]
        raise ValueError('Expected a number but received an object with '
                         + str(len(value)) + ' fields')
    return value


def _reason_fields(answer):
    if not isinstance(answer, dict):
        return []
    return [v for k, v in answer.items()
            if isinstance(k, str) and k.lower().startswith('reason')
            and isinstance(v, str) and v.strip()]


def reason(answer):
    """Require justification, accepting the per-field reason form some tasks ask for."""
    if not isinstance(answer, dict):
        raise ValueError('Answer must be a JSON object')
    if isinstance(answer.get('reason'), str) and answer['reason'].strip():
        return
    fields = _reason_fields(answer)
    if fields:
        return
    raise ValueError('A nonempty reason string is required')


def identifiers(value, universe=None):
    if not isinstance(value, list) or any(not isinstance(x, str) for x in value):
        raise ValueError('Expected an array of identifier strings')
    if len(value) != len(set(value)):
        raise ValueError('Duplicate identifiers are invalid')
    if universe is not None and not set(value) <= set(universe):
        raise ValueError('Unknown identifier')
    return value


def correlate(x, y):
    if len(x) != len(y) or len(x) < 2:
        raise ValueError('At least two aligned pairs are required')
    x = [finite(v) for v in x]
    y = [finite(v) for v in y]
    mx, my = sum(x) / len(x), sum(y) / len(y)
    vx = sum((v - mx) ** 2 for v in x)
    vy = sum((v - my) ** 2 for v in y)
    if vy == 0:
        raise ValueError('Reference has no variance')
    if vx == 0:
        return 0.0
    return max(-1.0, min(1.0, sum((a - mx) * (b - my) for a, b in zip(x, y)) / math.sqrt(vx * vy)))


def gold_ranks(tiers):
    ranks, offset = {}, 0
    for tier in tiers:
        for mid in tier:
            ranks[mid] = offset + (len(tier) - 1) / 2
        offset += len(tier)
    return ranks


def concordance(order, ranks):
    """Fraction of decisively ordered gold pairs the submission places correctly.

    Pairs tied in the gold are not counted, so a partial-order gold cannot punish an
    ordering the source never determined.
    """
    agreed = total = 0
    for i, a in enumerate(order):
        for b in order[i + 1:]:
            if ranks[a] == ranks[b]:
                continue
            total += 1
            if ranks[a] < ranks[b]:
                agreed += 1
    if not total:
        raise ValueError('Gold contains no strictly ordered pair')
    return agreed / total, agreed, total


def ranking(order, spec):
    ids = spec['candidate_ids']
    order = identifiers(order, ids)
    if set(order) != set(ids):
        raise ValueError('A full ranking must contain each candidate once')
    truth = spec['expected']
    tiers = truth if truth and isinstance(truth[0], list) else [[x] for x in truth]
    flattened = [x for tier in tiers for x in tier]
    if len(flattened) != len(ids) or set(flattened) != set(ids):
        raise ValueError('Malformed gold ranking')
    ranks = gold_ranks(tiers)
    fraction, agreed, total = concordance(order, ranks)
    rho = correlate(list(range(len(order))), [ranks[x] for x in order])
    # 0 at chance, 1 at a perfect order; near-misses keep proportional credit.
    skill = max(0.0, 2 * fraction - 1)
    return skill, {'spearman_rho': rho, 'concordant_pairs': agreed, 'comparable_pairs': total,
                   'pair_concordance': fraction,
                   'metric': 'max(0, 2*concordance-1)'}


def ranking_projected(order, spec):
    """Score only the candidates that carry data; extra pool members just have to appear.

    The submission must cover the whole candidate pool, but positions of molecules without
    reference data cannot help or hurt: they are removed before comparison.
    """
    ids = spec['candidate_ids']
    scored = spec['scored_ids']
    order = identifiers(order, ids)
    if set(order) != set(ids):
        raise ValueError('A full ranking must contain every pool member once')
    if not set(scored) <= set(ids) or len(scored) < 2:
        raise ValueError('scored_ids must be a subset of at least two pool members')
    projected = [mid for mid in order if mid in set(scored)]
    truth = spec['expected']
    tiers = truth if truth and isinstance(truth[0], list) else [[x] for x in truth]
    flattened = [x for tier in tiers for x in tier]
    if len(flattened) != len(scored) or set(flattened) != set(scored):
        raise ValueError('Malformed gold ranking')
    ranks = gold_ranks(tiers)
    fraction, agreed, total = concordance(projected, ranks)
    rho = correlate(list(range(len(projected))), [ranks[x] for x in projected])
    return max(0.0, 2 * fraction - 1), {'spearman_rho': rho, 'concordant_pairs': agreed,
                                        'comparable_pairs': total,
                                        'projected_order': projected,
                                        'ignored_pool_members': sorted(set(ids) - set(scored)),
                                        'metric': 'max(0, 2*concordance-1) on the scored subset only'}


def ranking_constraints(order, spec):
    ids = spec['candidate_ids']
    order = identifiers(order, ids)
    if set(order) != set(ids):
        raise ValueError('A full submitted ranking must contain each candidate once')
    pairs = spec['expected_pairs']
    if not pairs or any(not isinstance(pair, list) or len(pair) != 2 or pair[0] == pair[1]
                        or not set(pair) <= set(ids) for pair in pairs):
        raise ValueError('Gold must contain valid supported higher/lower pairs')
    if len({tuple(pair) for pair in pairs}) != len(pairs):
        raise ValueError('Repeated gold pair')
    successors = {mid: set() for mid in ids}
    for higher, lower in pairs:
        successors[higher].add(lower)
    visiting, done = set(), set()

    def visit(mid):
        if mid in visiting:
            raise ValueError('Gold constraints contain a cycle')
        if mid in done:
            return
        visiting.add(mid)
        for child in successors[mid]:
            visit(child)
        visiting.remove(mid)
        done.add(mid)

    for mid in ids:
        visit(mid)
    positions = {mid: i for i, mid in enumerate(order)}
    correct = sum(positions[a] < positions[b] for a, b in pairs)
    accuracy = correct / len(pairs)
    return max(0.0, 2 * accuracy - 1), {
        'supported_pairs': len(pairs), 'correct_pairs': correct, 'pair_accuracy': accuracy,
        'unreported_comparisons_scored': False,
        'metric': 'max(0, 2*supported-pair accuracy - 1)'}


def pearson(value, spec):
    ids = spec['candidate_ids']
    if not isinstance(value, list) or any(not isinstance(row, dict) for row in value):
        raise ValueError('Expected predictions [{id,pka,reason}]')
    keys = identifiers([row.get('id') for row in value], ids)
    if set(keys) != set(ids):
        raise ValueError('Predictions must cover every candidate exactly once')
    rows = {row['id']: row for row in value}
    field = spec.get('value_field', 'pka')
    if spec.get('per_candidate_reason_required', True):
        for row in value:
            reason(row)
    x = [finite(unwrap_number(rows[mid].get(field), field)) for mid in ids]
    y = [finite(spec['expected'][mid]) for mid in ids]
    r = correlate(x, y)
    mae = sum(abs(a - b) for a, b in zip(x, y)) / len(ids)
    mean_y = sum(y) / len(y)
    baseline = sum(abs(v - mean_y) for v in y) / len(y)
    accuracy = max(0.0, min(1.0, 1 - mae / baseline)) if baseline > 0 else 0.0
    skill = 0.5 * max(0.0, r) + 0.5 * accuracy
    return skill, {'pearson_r': r, 'mae': mae, 'mean_absolute_deviation_gold': baseline,
                   'accuracy_credit': accuracy, 'rank_credit': max(0.0, r),
                   'pair_count': len(ids),
                   'metric': '0.5*max(0,r) + 0.5*clip(1-mae/MAD_gold)'}


def _atol(spec, want):
    return max(finite(spec.get('atol', 0.0)), finite(spec.get('rtol', 0.0)) * abs(want))


def metric(value, spec):
    kind = spec['type']
    expected = spec.get('expected')
    if kind == 'ranking':
        return ranking(value, spec)
    if kind == 'ranking_constraints':
        return ranking_constraints(value, spec)
    if kind == 'ranking_projected':
        return ranking_projected(value, spec)
    if kind == 'pearson':
        return pearson(value, spec)
    if kind == 'set':
        got = set(identifiers(value, spec.get('candidate_ids')))
        want = set(expected)
        union = got | want
        result = len(got & want) / len(union) if union else 1.0
        return result, {'jaccard': result}
    if kind == 'ordered_subset':
        got = identifiers(value, spec['candidate_ids'])
        if len(got) != len(expected):
            raise ValueError('Wrong subset length')
        if not expected:
            raise ValueError('Ordered subset gold cannot be empty')
        union = set(got) | set(expected)
        overlap = len(set(got) & set(expected)) / len(union)
        # Partial credit for a right set in a nearly right order, as a smooth function
        # of adjacent swaps rather than an all-or-nothing exact-match term.
        inversions = sum(1 for i in range(len(got)) for j in range(i + 1, len(got))
                         if got[i] in expected and got[j] in expected
                         and expected.index(got[i]) > expected.index(got[j]))
        worst = len(expected) * (len(expected) - 1) / 2
        order_credit = 1.0 - (inversions / worst if worst else 0.0)
        exact = float(got == expected)
        fraction = 0.5 * overlap + 0.5 * order_credit
        return fraction, {'set_jaccard': overlap, 'order_credit': order_credit,
                          'inversions': inversions, 'exact_order': bool(exact)}
    if kind == 'choice':
        if not isinstance(value, str):
            raise ValueError('Expected one of the declared choices')
        chosen = canonical_choice(value, spec['choices'])
        target = canonical_choice(expected, spec['choices'])
        return float(chosen == target), {'correct': chosen == target,
                                         'matched_alias': value != chosen}
    if kind == 'number':
        want = finite(expected)
        got = finite(unwrap_number(value, spec['key']))
        tolerance = _atol(spec, want)
        error = abs(got - want)
        if tolerance <= 0:
            fraction = 1.0 if error == 0 else 0.0
        else:
            # Full credit inside tolerance, linear decay to zero at ten tolerances.
            fraction = max(0.0, min(1.0, 1 - max(0.0, error - tolerance) / (9 * tolerance)))
        return fraction, {'absolute_error': error, 'tolerance': tolerance,
                          'metric': 'linear decay to 0 at 10*tolerance'}
    if kind == 'mapping_choice':
        ids = spec['candidate_ids']
        if not isinstance(value, dict) or set(value) != set(ids):
            raise ValueError('Mapping must cover every candidate exactly once')
        mapped = {}
        aliases = 0
        for mid, raw in value.items():
            if not isinstance(raw, str):
                raise ValueError('Mapping values must be strings')
            canonical = canonical_choice(raw, spec['choices'])
            aliases += int(canonical != raw)
            mapped[mid] = canonical
        want = {mid: canonical_choice(expected[mid], spec['choices']) for mid in ids}
        correct = sum(mapped[mid] == want[mid] for mid in ids)
        return correct / len(ids), {'correct': correct, 'count': len(ids), 'alias_resolved': aliases}
    raise ValueError('Unsupported metric type: ' + str(kind))


def canonical_choice(value, choices):
    """Case/underscore-insensitive alias resolution against the declared vocabulary."""
    def norm(text):
        return re.sub(r'[^a-z0-9]', '', text.lower())
    table = {}
    for choice in choices:
        table.setdefault(norm(choice), choice)
    key = norm(value)
    if key in table:
        return table[key]
    raise ValueError('Value ' + repr(value) + ' is not one of the declared choices')


def validate_gold(gold):
    specs = gold['turns'] if gold['mode'] == 'evidence_followup' else {'single': gold}
    if gold['mode'] == 'evidence_followup' and list(specs) != ['T1', 'T2', 'T3', 'T4']:
        raise ValueError('Follow-up cases must have four ordered turns')
    total = 0.0
    for turn in specs.values():
        for spec in turn['metrics']:
            if finite(spec['weight']) <= 0:
                raise ValueError('Metric weights must be positive')
            if not isinstance(spec['key'], str) or not spec['key']:
                raise ValueError('Metric must name a prediction field')
            total += spec['weight']
    if abs(total - 100) > 1e-8:
        raise ValueError('Metric weights must sum to 100')
    if gold['mode'] == 'evidence_followup':
        last_weight = sum(x['weight'] for x in gold['turns']['T4']['metrics'])
        if last_weight < 55:
            raise ValueError('Hidden-result final-turn weight must be at least 55')


def evaluate(prediction, gold, turns=None):
    validate_gold(gold)
    specs = gold['turns'] if gold['mode'] == 'evidence_followup' else {'single': gold}
    answers = turns if gold['mode'] == 'evidence_followup' else {'single': prediction}
    answers = answers if isinstance(answers, dict) else {}
    result = {'question_id': gold['id'], 'score': 0.0, 'turns': {}, 'errors': [],
              'scoring_version': SCORING_VERSION,
              'molecular_predictions_run': False, 'reason_scored': False}
    for tid, turn_spec in specs.items():
        answer = answers.get(tid)
        turn_result = {'score': 0.0, 'metrics': {}}
        try:
            reason(answer)
        except ValueError as exc:
            result['errors'].append(tid + ': ' + str(exc))
            result['turns'][tid] = turn_result
            continue
        for spec in turn_spec['metrics']:
            key = spec['key']
            try:
                fraction, details = metric(answer.get(key), spec)
                fraction = max(0.0, min(1.0, fraction))
                points = spec['weight'] * fraction
                turn_result['metrics'][key] = {'score': round(points, 6), 'weight': spec['weight'],
                                               'fraction': round(fraction, 6), **details}
                turn_result['score'] += points
            except (ValueError, KeyError, TypeError) as exc:
                result['errors'].append(tid + '.' + key + ': ' + str(exc))
                turn_result['metrics'][key] = {'score': 0.0, 'weight': spec['weight'], 'error': str(exc)}
        result['score'] += turn_result['score']
        turn_result['score'] = round(turn_result['score'], 6)
        result['turns'][tid] = turn_result
    result['score'] = round(min(100.0, max(0.0, result['score'])), 6)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--question', type=Path, required=True)
    parser.add_argument('--prediction', type=Path, required=True)
    parser.add_argument('--turns-answers', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    gold = read(args.question / 'scoring/reference_answer.json')
    pred = read(args.prediction)
    path = args.turns_answers or args.prediction.parent / 'turns_answers.json'
    turns = read(path) if path.is_file() else None
    result = evaluate(pred, gold, turns)
    text = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + '\n'
    if args.output:
        if args.output.resolve() in (args.prediction.resolve(), path.resolve()):
            parser.error('Output must not overwrite model answers')
        args.output.write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    main()
