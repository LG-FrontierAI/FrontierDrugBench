"""Score ready gold using organizer-owned fixed objects and metric weights.

Submission data cannot change ids, transformations, budgets, normalization
bounds or weights. Design compliance does not represent experimental success.
"""
from __future__ import annotations
import json
import math
from pathlib import Path
from typing import Any
from .design_eval import evaluate_design
from .prediction_eval import _finite, _indexed, evaluate_rows, selection_metrics

PREDICTION_METRICS = {'spearman', 'top1_hit', 'top3_hit', 'mae', 'log_mae', 'rmse',
    'interval_coverage', 'mean_interval_width', 'mean_interval_score', 'brier_score'}
SELECTION_METRICS = {'top1_hit', 'topk_recall', 'utility', 'regret', 'contains_optimal_item'}
DESIGN_METRICS = {'hard_constraint_pass_rate'}

def _decode(prediction: Any) -> dict[str, Any]:
    value = json.loads(prediction) if isinstance(prediction, str) else prediction
    if not isinstance(value, dict):
        raise ValueError('prediction must be an object or JSON object string')
    return value

def _frozen_spec(gold: dict[str, Any]) -> list[dict[str, Any]]:
    specs = gold.get('score_components')
    if not isinstance(specs, list) or not specs:
        raise RuntimeError('A reviewed, frozen score_components specification is required')
    seen = set()
    for spec in specs:
        if not isinstance(spec, dict) or spec.get('status', 'ready') != 'ready':
            raise ValueError('Every frozen score component must be a ready object')
        if any(not isinstance(spec.get(k), str) or not spec[k].strip() for k in ('component', 'metric')):
            raise ValueError('Frozen component and metric names must be nonempty strings')
        key = (spec['component'], spec['metric'])
        if key in seen:
            raise ValueError(f'Duplicate frozen component metric: {key}')
        seen.add(key)
        if any(not _finite(spec.get(k)) for k in ('weight', 'minimum', 'maximum')):
            raise ValueError('Frozen weights and normalization bounds must be finite numbers')
        if not 0 <= spec['weight'] <= 1:
            raise ValueError('Frozen score weights must lie in [0, 1]')
        if not spec['maximum'] > spec['minimum']:
            raise ValueError('Frozen metric maximum must exceed minimum')
        if not math.isfinite(float(spec['maximum'])-float(spec['minimum'])):
            raise ValueError('Frozen normalization range overflows')
        if spec.get('direction', 'higher') not in ('higher', 'lower'):
            raise ValueError('Metric direction must be higher or lower')
    if not math.isclose(math.fsum(s['weight'] for s in specs), 1.0, rel_tol=0.0, abs_tol=1e-9):
        raise ValueError('Frozen score weights must sum to one')
    return specs

def _prediction_component(config: dict[str, Any], rows: Any, submitted: Any) -> dict[str, Any]:
    if config.get('status', 'ready') != 'ready':
        raise ValueError('Prediction component is pending')
    return evaluate_rows(rows, submitted, outcome=config.get('outcome_field', 'outcome'),
        higher_is_better=config.get('higher_is_better', True), transform=config.get('transform', 'identity'),
        interval_probability=config.get('interval_probability', .9), binary_event=config.get('binary_event', False),
        strictly_positive=config.get('strictly_positive', False))

def evaluate_item(prediction: Any, gold_path: Path) -> dict[str, Any]:
    gold_path = Path(gold_path)
    if not gold_path.exists():
        raise RuntimeError(f'hidden gold is not installed: {gold_path}')
    gold = json.loads(gold_path.read_text(encoding='utf-8'))
    if not isinstance(gold, dict) or gold.get('status') != 'ready':
        raise RuntimeError('hidden gold must be an object with status ready')
    pred, specs = _decode(prediction), _frozen_spec(gold)
    report: dict[str, Any] = {'status': 'scored', 'components': {}}
    allowed: dict[str, set[str]] = {}
    is_design = gold.get('response_type', 'prediction') in {'vhh_design', 'paired_design'}
    if is_design:
        if any(k in gold for k in ('rows', 'prediction_groups', 'selection_rows')):
            raise ValueError('Design gold cannot also declare unrelated prediction/selection rows')
        report['components']['design'] = evaluate_design(gold.get('task'), pred.get('candidates', []))
        allowed['design'] = DESIGN_METRICS
    else:
        if 'prediction_groups' in gold and 'rows' in gold:
            raise ValueError('Use prediction_groups or rows, not both')
        if 'prediction_groups' in gold:
            groups = gold['prediction_groups']
            if not isinstance(groups, list) or not groups:
                raise ValueError('prediction_groups must be a nonempty list')
            names, required = set(), set()
            for group in groups:
                if not isinstance(group, dict) or not isinstance(group.get('name'), str) or not group['name'].strip():
                    raise ValueError('Every prediction group needs a nonempty name')
                if group['name'] in names or group['name'] in {'selection', 'design'}:
                    raise ValueError('Prediction group names must be unique and not reserved')
                names.add(group['name'])
                ids = set(_indexed(group.get('rows'), 'group gold'))
                if required & ids:
                    raise ValueError('Prediction ids must be unique across endpoint groups')
                required.update(ids)
            submitted = pred.get('predictions', [])
            supplied = _indexed(submitted, 'predictions')
            if set(supplied) - required:
                raise ValueError('Unknown prediction ids')
            for group in groups:
                ids = {r['id'] for r in group['rows']}
                name = group['name']
                report['components'][name] = _prediction_component(group, group['rows'], [r for r in submitted if r['id'] in ids])
                allowed[name] = PREDICTION_METRICS
        if 'rows' in gold:
            report['components']['prediction'] = _prediction_component(gold, gold['rows'], pred.get('predictions', []))
            allowed['prediction'] = PREDICTION_METRICS
        if 'selection_rows' in gold:
            report['components']['selection'] = selection_metrics(gold['selection_rows'], pred.get('selected_ids', []),
                utility=gold.get('utility_field', 'utility'), budget=gold.get('budget'),
                higher_is_better=gold.get('higher_is_better', True))
            allowed['selection'] = SELECTION_METRICS
    if not report['components']:
        raise ValueError('Ready gold must install at least one fixed evaluation component')
    for spec in specs:
        component, metric = spec['component'], spec['metric']
        if metric not in allowed.get(component, set()):
            raise ValueError(f'Unsupported frozen scoring metric: {component}.{metric}')
        if metric not in report['components'][component]:
            raise ValueError(f'Frozen metric is not defined for this task: {component}.{metric}')
    if any(c.get('submission_complete') is False for c in report['components'].values()):
        report.update(score=0.0, score_interpretation='incomplete or invalid required predictions/selections; partial diagnostics are not a leaderboard score')
        return report
    score = 0.0
    for spec in specs:
        value = report['components'][spec['component']][spec['metric']]
        if isinstance(value, bool):
            value = int(value)
        if not _finite(value):
            raise ValueError(f"Frozen metric is unavailable or nonfinite: {spec['component']}.{spec['metric']}")
        lo, hi = float(spec['minimum']), float(spec['maximum'])
        scaled = 0.0 if value <= lo else 1.0 if value >= hi else (float(value)-lo)/(hi-lo)
        if spec.get('direction', 'higher') == 'lower':
            scaled = 1.0-scaled
        score += float(spec['weight'])*scaled
    report['score'] = min(1.0, max(0.0, score))
    report['score_interpretation'] = ('frozen constraint-compliance mapping only; affinity and biological success are not evaluated'
        if is_design else 'frozen organizer metric mapping; raw endpoint metrics remain separate')
    return report

def score_item(prediction: Any, gold_path: Path) -> float:
    return float(evaluate_item(prediction, gold_path)['score'])
