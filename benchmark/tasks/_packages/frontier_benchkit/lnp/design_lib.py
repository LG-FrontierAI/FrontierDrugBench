"""Score P20-05 through P20-20 using Python's standard library. No inference."""
import argparse
from collections import Counter
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def require_reason(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('A nonempty reason string is required')


def number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError('Expected a finite number')
    return value


def rows_by_id(rows, ids, field='id'):
    if not isinstance(rows, list) or any(not isinstance(x, dict) for x in rows):
        raise ValueError('Expected an array of objects')
    keys = [x.get(field) for x in rows]
    if any(not isinstance(x, str) for x in keys) or len(set(keys)) != len(keys):
        raise ValueError('Missing or duplicate IDs')
    if set(keys) != set(ids):
        raise ValueError('All candidate IDs must occur exactly once')
    return dict(zip(keys, rows))


def pka_reference(gold, pka_file):
    if pka_file is None:
        raise ValueError('Reference pKa is not available. Supply evaluator --pka-results')
    batch = read(pka_file)
    values = {}
    for row in batch:
        name = row.get('name')
        if name in values:
            raise ValueError('Duplicate pKa result name: ' + name)
        values[name] = row.get('max_basic_micro_pka')
    if gold.get('pka_result_names'):
        mapping = {}
        for mid, name in gold['pka_result_names'].items():
            mapping.setdefault(name, []).append({'question': gold['id'], 'candidate_id': mid})
    else:
        mapping = read(ROOT / 'share/pka_prediction_mapping.json')['mapping']
    result = {}
    for name, targets in mapping.items():
        for item in targets:
            if item['question'] == gold['id']:
                if name not in values or values[name] is None:
                    raise ValueError('Missing basic pKa prediction for ' + name)
                result[item['candidate_id']] = number(values[name])
    for row in gold.get('reference_rows', []):
        if not row['has_basic_site']:
            result[row['id']] = None
    return result


def ranking(order, answer, ids):
    if not isinstance(order, list) or len(order) != len(ids) or set(order) != set(ids):
        raise ValueError('order must contain every candidate ID exactly once')
    # Tied pKa references use midranks and Pearson correlation of ranks.
    def ranks(tiers):
        out = {}; offset = 0
        for tier in tiers:
            for mid in tier:
                out[mid] = offset + (len(tier) - 1) / 2
            offset += len(tier)
        return out
    tiers = answer if answer and isinstance(answer[0], list) else [[x] for x in answer]
    ref = ranks(tiers); n = len(ids); mean = (n - 1) / 2
    numerator = sum((i - mean) * (ref[x] - mean) for i, x in enumerate(order))
    denominator = math.sqrt(sum((i - mean) ** 2 for i in range(n)) * sum((ref[x] - mean) ** 2 for x in order))
    if denominator == 0:
        raise ValueError('Reference has no rank variation; ranking cannot be scored')
    rho = numerator / denominator
    return 100 * max(0, rho), {'rho': rho}


def pearson(predicted, reference):
    if len(predicted) != len(reference) or len(reference) < 2:
        raise ValueError('Pearson requires at least two aligned numeric pairs')
    x = [number(v) for v in predicted]; y = [number(v) for v in reference]
    mx = sum(x) / len(x); my = sum(y) / len(y)
    vx = sum((v - mx) ** 2 for v in x); vy = sum((v - my) ** 2 for v in y)
    if vy == 0: raise ValueError('Reference values have zero variance; Pearson is undefined')
    mae = sum(abs(a - b) for a, b in zip(x, y)) / len(x)
    if vx == 0:
        return 0.0, {'pearson_r': None, 'mae': mae, 'pair_count': len(x), 'issue': 'Constant predictions: Pearson undefined, score 0'}
    r = sum((a - mx) * (b - my) for a, b in zip(x, y)) / math.sqrt(vx * vy)
    r = min(1.0, max(-1.0, r))
    return 100 * max(0, r), {'pearson_r': r, 'mae': mae, 'pair_count': len(x)}


def reaction_graph(steps, allowed):
    if not isinstance(steps, list) or not steps or any(not isinstance(x, dict) for x in steps):
        raise ValueError('steps must be reaction-node objects')
    ids = [x.get('id') for x in steps]
    if any(not isinstance(x, str) or not x for x in ids) or len(set(ids)) != len(ids):
        raise ValueError('Reaction node IDs must be unique strings')
    nodes = dict(zip(ids, steps)); depths = {}; visiting = set(); edges = Counter()
    for node in steps:
        require_reason(node.get('reason'))
        if node.get('reaction_type') not in allowed: raise ValueError('Unknown reaction_type')
        if type(node.get('pdf_page')) is not int or node['pdf_page'] < 1: raise ValueError('Reaction pdf_page must be positive')
        deps = node.get('depends_on')
        if not isinstance(deps, list) or any(not isinstance(x, str) or x not in nodes for x in deps) or len(set(deps)) != len(deps):
            raise ValueError('depends_on must list distinct existing node IDs')
        for dep in deps: edges[(nodes[dep]['reaction_type'], node['reaction_type'])] += 1
    def depth(mid):
        if mid in depths: return depths[mid]
        if mid in visiting: raise ValueError('Reaction graph contains a cycle')
        visiting.add(mid)
        depths[mid] = 1 + max((depth(x) for x in nodes[mid]['depends_on']), default=0)
        visiting.remove(mid); return depths[mid]
    return Counter(x['reaction_type'] for x in steps), edges, len(steps), max(depth(x) for x in ids)


def multiset_f1(predicted, reference):
    total = sum(predicted.values()) + sum(reference.values())
    return 2 * sum((predicted & reference).values()) / total if total else 1.0


def evaluate(pred, gold, pka_file=None, tool_file=None):
    require_reason(pred.get('reason'))
    mode = gold['mode']; ids = gold.get('candidate_ids', [])
    details = {}
    if mode == 'pka_pearson':
        rows = rows_by_id(pred.get('predictions'), ids)
        if gold.get('per_candidate_reason_required'):
            for row in rows.values(): require_reason(row.get('reason'))
        values = gold['answer']['pka'] if gold['answer'] is not None else pka_reference(gold, pka_file)
        score, details = pearson([rows[mid]['pka'] for mid in ids], [values[mid] for mid in ids])
    elif mode == 'ranking':
        answer = gold['answer']
        if answer is None:
            values = pka_reference(gold, pka_file)
            tiers = []
            for value in sorted(set(values.values())):
                tiers.append([x for x in ids if values[x] == value])
            answer = {'order': tiers}
        score, details = ranking(pred.get('order'), answer['order'], ids)
    elif mode == 'classification_pka':
        rows = rows_by_id(pred.get('predictions'), ids)
        values = pka_reference(gold, pka_file); labels = []; predicted_pka = []; reference_pka = []
        pka_errors = []
        for ref in gold['reference_rows']:
            row = rows[ref['id']]; require_reason(row.get('reason'))
            if type(row.get('is_il')) is not bool:
                raise ValueError('is_il must be a JSON boolean')
            label = 1 if row['is_il'] == ref['is_il'] else 0
            target = values[ref['id']]
            labels.append(label)
            if target is None:
                if row.get('pka', 'missing') is not None:
                    pka_errors.append(ref['id'] + ': no basic site; pka must be null')
            else:
                try: value = number(row.get('pka'))
                except ValueError as exc: pka_errors.append(ref['id'] + ': ' + str(exc))
                else:
                    if gold.get('pka_scoring_population') != 'ionizable_lipids' or ref['is_il']:
                        predicted_pka.append(value); reference_pka.append(target)
            details[ref['id']] = {'classification_correct': bool(label)}
        classification_score = gold.get('classification_weight', 40) * sum(labels) / len(ids)
        if pka_errors:
            pka_score = 0.0; pka_details = {'pearson_r': None, 'errors': pka_errors}
        else:
            pka_score, pka_details = pearson(predicted_pka, reference_pka)
            pka_score *= gold.get('pka_weight', 60) / 100
        details.update(classification_score=classification_score, pka_score=pka_score, pka_pearson=pka_details)
        score = classification_score + pka_score
    elif mode == 'quotation':
        tiers = pred.get('difficulty_tiers')
        if not isinstance(tiers, list) or any(not isinstance(t, list) or not t for t in tiers):
            raise ValueError('difficulty_tiers must be nonempty groups')
        flat = [x for t in tiers for x in t]
        if len(flat) != len(ids) or set(flat) != set(ids):
            raise ValueError('difficulty_tiers must contain all candidate IDs once')
        rows = rows_by_id(pred.get('analysis'), ids)
        for row in rows.values(): require_reason(row.get('reason'))
        ranks = {mid: i for i, tier in enumerate(tiers) for mid in tier}
        refs = sorted(gold['scored_rows'], key=lambda x: x['quotation_rmb']); correct = 0; pairs = 0
        for i, left in enumerate(refs):
            for right in refs[i + 1:]:
                if left['quotation_rmb'] == right['quotation_rmb']:
                    if not gold.get('score_quote_ties'): continue
                    correct += int(ranks[left['id']] == ranks[right['id']])
                else:
                    tie_credit = 0 if gold.get('score_quote_ties') else .5
                    correct += 1 if ranks[left['id']] < ranks[right['id']] else tie_credit if ranks[left['id']] == ranks[right['id']] else 0
                pairs += 1
        score = 100 * correct / pairs
        details = {'scored_pairs': pairs, 'pair_credit': correct, 'decoy_positions_scored': False}
    elif mode == 'route_steps':
        rows = rows_by_id(pred.get('routes'), ids); scores = []
        for ref in gold['reference_rows']:
            row = rows[ref['id']]; require_reason(row.get('reason'))
            graph = gold.get('score_reaction_graph', False)
            if graph:
                predicted_nodes, predicted_edges, count, depth = reaction_graph(row.get('steps'), gold['reaction_types'])
                reference_nodes, reference_edges, _, _ = reaction_graph(ref['reaction_steps'], gold['reaction_types'])
                if count != row.get('total_steps') or depth != row.get('longest_linear_steps'):
                    raise ValueError('Route counts must agree with the submitted reaction graph')
            else:
                if not isinstance(row.get('steps'), list) or not row['steps']:
                    raise ValueError('Each route needs a nonempty steps array')
                for step in row['steps']: require_reason(step)
            parts = []
            weights = [('total_steps', 15), ('longest_linear_steps', 15)] if graph else [('total_steps', 70), ('longest_linear_steps', 30)]
            for field, weight in weights:
                value = row.get(field)
                if type(value) is not int or value < 0: raise ValueError(field + ' must be a nonnegative integer')
                parts.append(weight * max(0, 1 - abs(value - ref[field]) / 2))
            if row['longest_linear_steps'] > row['total_steps']:
                raise ValueError('Longest linear steps cannot exceed total steps')
            details[ref['id']] = {'total_steps_score': parts[0], 'linear_steps_score': parts[1]}
            if graph:
                parts += [40 * multiset_f1(predicted_nodes, reference_nodes), 30 * multiset_f1(predicted_edges, reference_edges)]
                details[ref['id']].update(reaction_nodes_score=parts[2], dependency_edges_score=parts[3])
            scores.append(sum(parts))
        score = sum(scores) / len(ids)
    elif mode in ('generation', 'extraction'):
        if tool_file is None: raise ValueError('Supply evaluator --tool-results prepared by prepare_tools.py')
        tool = read(tool_file)
        if tool.get('question_id') != gold['id'] or tool.get('prediction') != pred:
            raise ValueError('Evaluator tool results belong to a different submission')
        if mode == 'generation':
            rows = pred.get('designs')
            if not isinstance(rows, list) or len(rows) > 10: raise ValueError('Submit no more than ten designs')
            names = [x.get('id') for x in rows]
            if any(not isinstance(x, str) or not x for x in names) or len(set(names)) != len(names):
                raise ValueError('Design IDs must be unique nonempty strings')
            tools = rows_by_id(tool['rows'], names)
            total = 0; heads = set()
            for row in rows:
                require_reason(row.get('reason')); value = tools[row['id']]; pka_score = il_score = 0
                if value['eligible']:
                    pka = number(value['max_basic_micro_pka']); il = number(value['il_likeness'])
                    if not 0 <= il <= 1: raise ValueError('il_likeness must be in [0,1]')
                    distance = max(6.5 - pka, pka - 7.5, 0)
                    pka_score = gold.get('pka_design_weight', 5) * max(0, 1 - distance / gold.get('pka_outside_tolerance', 1))
                    il_score = gold.get('il_design_weight', 5) * il
                    heads.add(value['head_scaffold'])
                details[row['id']] = {'eligible': value['eligible'], 'pka_score': pka_score, 'il_score': il_score, 'issues': value['issues']}
                total += pka_score + il_score
            factor = min(1, len(heads) / gold['head_scaffold_min'])
            score = total * factor; details['head_diversity_factor'] = factor
        else:
            rows = pred.get('molecules')
            if not isinstance(rows, list): raise ValueError('molecules must be an array')
            matched = set(); features = 0; pages = 0
            feature_names = gold.get('extraction_features', ['has_protonatable_amine', 'is_permanent_quaternary_ammonium', 'ester_count'])
            for row, value in zip(rows, tool['rows']):
                require_reason(row.get('reason'))
                if type(row.get('pdf_page')) is not int or row['pdf_page'] < 1:
                    raise ValueError('pdf_page must be a positive integer')
                mid = value.get('matched_id')
                if mid and mid not in matched:
                    matched.add(mid)
                    ref = next(x for x in gold['reference_rows'] if x['id'] == mid)
                    for field in feature_names:
                        expected_type = int if field in ('ester_count', 'protonatable_amine_count') else str if field == 'molecular_formula' else bool
                        features += int(type(row.get(field)) is expected_type and row[field] == ref[field])
                    pages += int(row['pdf_page'] in ref.get('pdf_pages', [ref.get('pdf_page')]))
            f1 = 2 * len(matched) / (len(ids) + len(rows)) if rows else 0
            weights = gold.get('extraction_weights', {'structures': 50, 'features': 50, 'pages': 0})
            score = weights['structures'] * f1 + weights['features'] * features / (len(feature_names) * len(ids)) + weights['pages'] * pages / len(ids)
            details = {'correct_unique_molecules': len(matched), 'extraction_f1': f1, 'correct_feature_count': features, 'correct_page_count': pages}
    else:
        raise ValueError('Unsupported scoring mode: ' + mode)
    return {'question_id': gold['id'], 'score': round(score, 6), 'details': details, 'reason_scored': False, 'molecular_predictions_run': False}
