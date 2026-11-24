"""Frozen real-patent cases, with strict submissions and bound adjudication.

This module shares the original rank/MCC definitions without changing the
original thirty question files. Source/gold/input corruption is an organizer
error; contestant format errors are zeroes. No network calls occur here.
"""
from __future__ import annotations
import csv
import hashlib
import json
import math
import re
import unicodedata
from pathlib import Path
from .sequence_case_eval import _decode, _finite, _ranking, _binary, _ranking_gold, normalize_case_id, canonical_hash


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


# Formatting an LLM judge drops or rewrites when re-quoting a Markdown answer:
# emphasis markers, code fences, list bullets/numbers, blockquote arrows, rules.
# ``^`` is included because superscripts are flattened by NFKC, so ``10^5`` and
# ``10⁵`` must reach the same key.
_MARKUP = re.compile(r"[*`_~#>|^]")
# Sentence punctuation the judge substitutes when it truncates a quotation and
# closes it off itself ("high-dose downturn" -> "high-dose downturn.").
_TRAILING = ".;:,!?\u2026"
# Explicit elision. An LLM judge abbreviating a long answer writes "..." and
# keeps verbatim fragments on either side; that is honest citation, not a rewrite.
_ELLIPSIS = re.compile(r"\.\.\.|\u2026")
# LaTeX symbol commands flattened to the glyph the judge types instead.
_LATEX = {
    "\\approx": "\u2248", "\\times": "\u00d7", "\\cdot": "\u00b7", "\\pm": "\u00b1",
    "\\leq": "\u2264", "\\le": "\u2264", "\\geq": "\u2265", "\\ge": "\u2265",
    "\\rightarrow": "\u2192", "\\to": "\u2192", "\\mu": "\u00b5",
}
# \text{Bottom}, \mathrm{EC50}: wrappers whose argument is literal text.
_LATEX_WRAP = re.compile(r"\\(?:text|mathrm|mathit|mathbf|operatorname)\{([^{}]*)\}")


def _quote_key(text):
    """Normalise text for quotation fidelity checks.

    Only formatting is discarded. Word order, every word, and every internal
    punctuation mark that carries meaning are preserved, so a paraphrased or
    recombined quotation still fails the check.

    Deliberately NOT normalised away:
      * words and their order (a rewrite must not pass)
      * ``.`` and ``:`` -- ending or splitting a sentence differently is a
        rewrite, not a quoting artefact
      * ``-`` and ``/`` -- meaningful inside ranges and ratios
      * digit runs -- ``0.390625`` must not decay into ``0390625``
    """
    s = unicodedata.normalize("NFKC", text)
    for src, dst in (("\u2018", "'"), ("\u2019", "'"), ("\u201c", '"'),
                     ("\u201d", '"'), ("\u2212", "-"), ("\u2013", "-"), ("\u2014", "-")):
        s = s.replace(src, dst)
    for cmd, glyph in _LATEX.items():
        s = s.replace(cmd, glyph)
    # \text{Bottom}, \mathrm{EC50}: wrappers around literal text.
    s = _LATEX_WRAP.sub(lambda m: m.group(1), s)
    # LaTeX delimiters around symbols: \(K_D\) re-quoted as K_D.
    s = s.replace("\\(", "").replace("\\)", "").replace("\\[", "").replace("\\]", "")
    s = s.replace("$", "")
    # Bullets / ordered-list markers at line start, then remaining markup.
    # A judge collapsing a bullet list onto one line keeps the marker inline
    # ("are: - NT_024: 1.11 nM - NT_R: 1.94 nM"), so strip "- "/"* "/"1. " both
    # at line start and after the colon/space that preceded each item.
    s = re.sub(r"(?m)^\s*(?:[-+*]|\d+[.)])\s+", " ", s)
    s = re.sub(r"(?<=[:;])\s*[-+*]\s+", " ", s)
    s = re.sub(r"(?<=\s)[-+*]\s+(?=[^\d\s])", " ", s)
    s = _MARKUP.sub("", s)
    # Quotation marks around a quoted term are formatting, not content.
    s = s.replace('"', "")
    # Thousands separators: "1,000" and "1000" are the same quantity.
    s = re.sub(r"(?<=\d),(?=\d)", "", s)
    # Clause separators. A judge quoting a bulleted list writes "; " or ", "
    # where the response had a line break, so both are whitespace. Periods are
    # kept: they are how the gate notices a sentence was recut.
    s = re.sub(r"[,;]", " ", s)
    s = s.replace("\u00a0", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def is_faithful_quotation(quote, prediction):
    """True when ``quote`` occurs in ``prediction`` up to formatting differences.

    The judge must still quote the candidate, not the reference: a quote that
    merely restates the rubric, or recombines fragments out of order, does not
    satisfy this. Fragments separated by an explicit ``...`` elision must each
    occur verbatim, and in the same order as the response.
    """
    if not isinstance(quote, str) or not quote.strip():
        return False
    pred_key = _quote_key(prediction)
    fragments = [
        f.strip().rstrip(_TRAILING).strip()
        for f in _ELLIPSIS.split(_quote_key(quote))
    ]
    fragments = [f for f in fragments if f]
    if not fragments:
        return False
    pos = 0
    for fragment in fragments:
        found = pred_key.find(fragment, pos)
        if found < 0:
            return False
        pos = found + len(fragment)
    return True


def numeric(prediction, ids, truth):
    prediction = _decode(prediction)
    if not isinstance(prediction, dict) or set(prediction) != set(ids):
        raise ValueError("Numerical response must contain exactly all target IDs")
    if any(not _finite(v) or v <= 0 for v in prediction.values()):
        raise ValueError("Predictions must be finite positive numbers, not booleans")
    errors = {k: abs(math.log(prediction[k]) - math.log(truth[k])) for k in ids}
    error = math.fsum(errors.values()) / len(ids)
    return {"score": math.exp(-error), "mean_absolute_log_error": error,
            "absolute_log_errors": errors, "n_scored": len(ids),
            "score_definition": "exp(-mean(abs(log(prediction/truth))))"}


def _validate(gold):
    if gold.get("data_status") != "patent_experimental" or gold.get("admission_status") != "admitted":
        raise ValueError("Case is not an admitted experimental patent case")
    kind = gold.get("task_type")
    if kind not in {"ranking", "binary", "numeric", "review"}:
        raise ValueError("Unsupported frozen patent task type")
    if kind == "review":
        rubric = gold.get("rubric")
        if not isinstance(rubric, list) or not rubric or len({r['id'] for r in rubric}) != len(rubric):
            raise ValueError("Review requires distinct rubric criteria")
        if any(type(r.get('points')) is not int or r['points'] <= 0 or not r.get('required_finding') for r in rubric) or sum(r['points'] for r in rubric) != 100:
            raise ValueError("Review rubric must have evidence-based criteria totaling 100")
        return
    ids, truth = gold.get('target_ids'), gold.get('truth')
    if not isinstance(ids, list) or not ids or len(ids) != len(set(ids)) or any(not isinstance(x,str) or not x for x in ids):
        raise ValueError("Invalid frozen target IDs")
    if not isinstance(truth,dict) or set(truth) != set(ids):
        raise ValueError("Frozen truth must cover all targets")
    if kind == 'ranking':
        if len(ids) < 6 or type(gold.get('higher_is_better')) is not bool or any(not _finite(v) for v in truth.values()) or len(set(truth.values())) < 2:
            raise ValueError("New rankings require >=6 targets with varying finite values")
        checked = gold
        if 'measurement_intervals' in gold:
            if gold.get('ranking_metric') != 'resolvable_pair_concordance' or 'digitization_intervals' in gold:
                raise ValueError('Measurement intervals require a distinct frozen pair policy')
            if not gold.get('uncertainty_policy'):
                raise ValueError('Reported measurement intervals require an explicit interpretation')
            # Reuse the bound-separation checks, keeping the public record's
            # measurement uncertainty distinct from digitization uncertainty.
            checked = {**gold,'digitization_intervals':gold['measurement_intervals']}
        _ranking_gold(checked)
    elif kind == 'binary':
        if any(type(v) is not int or v not in (0,1) for v in truth.values()) or set(truth.values()) != {0,1}:
            raise ValueError("New MCC tasks require both classes as integer labels")
    elif any(not _finite(v) or v <= 0 for v in truth.values()):
        raise ValueError("Log-error targets must be finite and positive")


def _same_case_id(left, right):
    """Compare case spellings: '01' and 'case_01' denote the same case.

    The frozen gold stores the canonical ``case_NN`` form while a case scorer's
    ``CASE_ID`` constant is the bare number it was generated from, so a judge
    echoing the constant it was handed back is correct, not mismatched. Any
    other string still fails.
    """
    if left == right:
        return True
    try:
        return normalize_case_id(left) == normalize_case_id(right)
    except ValueError:
        return False


def review(prediction, gold, judgment):
    if not isinstance(prediction,str):
        raise ValueError("Review submission must be text")
    if not prediction.strip():
        return {"score": 0.0, "status": "empty_submission"}
    if judgment is None:
        return {"score": None, "status": "pending_adjudication", "reason": "A complete bound evidence judgment is required"}
    judgment = _decode(judgment)
    expected = {'item_id','case_id','response_sha256','rubric_sha256','criteria'}
    if not isinstance(judgment,dict) or set(judgment) != expected:
        raise RuntimeError("Organizer judgment fields are invalid")
    if judgment['item_id'] != gold['item_id']:
        raise RuntimeError("Organizer judgment does not match response, case or rubric: item_id "
                           + repr(judgment['item_id']) + " is not " + repr(gold['item_id']))
    if not _same_case_id(judgment['case_id'], gold['case_id']):
        raise RuntimeError("Organizer judgment does not match response, case or rubric: case_id "
                           + repr(judgment['case_id']) + " is not " + repr(gold['case_id']))
    if judgment['response_sha256'] != hashlib.sha256(prediction.encode()).hexdigest():
        raise RuntimeError("Organizer judgment does not match response, case or rubric: "
                           "response_sha256 does not bind this response")
    if judgment['rubric_sha256'] != canonical_hash(gold['rubric']):
        raise RuntimeError("Organizer judgment does not match response, case or rubric: "
                           "rubric_sha256 does not bind this rubric")
    entries = judgment['criteria']
    if not isinstance(entries,dict) or set(entries) != {r['id'] for r in gold['rubric']}:
        raise RuntimeError("Organizer must judge every criterion exactly once")
    points = 0
    for criterion in gold['rubric']:
        entry = entries[criterion['id']]
        if not isinstance(entry,dict) or set(entry) != {'met','evidence','reason'} or type(entry['met']) is not bool or not isinstance(entry['reason'],str) or not entry['reason'].strip():
            raise RuntimeError("Invalid organizer criterion judgment")
        quotes = entry['evidence']
        if not isinstance(quotes,list) or any(not isinstance(q,str) or not q.strip() for q in quotes) or (entry['met'] and not quotes):
            raise RuntimeError("Awarded criteria require response quotations")
        if any(not is_faithful_quotation(q, prediction) for q in quotes):
            raise RuntimeError("Awarded criteria require exact response quotations")
        points += criterion['points'] if entry['met'] else 0
    return {'score': points/100, 'status':'scored', 'awarded_points': points, 'criteria':entries}


def evaluate_question(prediction, question_dir, case_id, *, judgment=None, **kwargs):
    if kwargs:
        raise ValueError("Patent cases do not accept external structure results")
    directory = Path(question_dir)
    spec = _decode((directory/'tests/evaluation_spec.json').read_text())
    cid = normalize_case_id(case_id)
    entries = [e for e in spec['cases'] if e['case_id'] == cid]
    if spec.get('status') != 'ready' or spec.get('evaluator_type') != 'patent_experimental_case' or len(entries) != 1:
        raise ValueError("Patent case is not formally released")
    entry = entries[0]
    if entry.get('input') != f'inputs/{cid}.csv' or entry.get('answer') != f'tests/cases/{cid}.answer.json':
        raise ValueError("Invalid frozen patent paths")
    for key, field in [('input','input_sha256'),('answer','answer_sha256')]:
        path = directory/entry[key]
        if path.is_symlink() or sha256(path) != entry[field]:
            raise ValueError("Frozen patent file hash mismatch")
    gold = _decode((directory/entry['answer']).read_text())
    if gold['item_id'] != spec['item_id'] or gold['case_id'] != cid or gold.get('input_sha256') != entry['input_sha256']:
        raise ValueError("Gold identity/input hash mismatch")
    study_hash = hashlib.sha256(entry['study_information'].encode()).hexdigest()
    if entry.get('study_information_sha256') != study_hash or gold.get('study_information_sha256') != study_hash:
        raise ValueError("Frozen study information mismatch")
    _validate(gold)
    report = {'item_id':gold['item_id'],'case_id':cid,'task_type':gold['task_type'],
              'data_status':'patent_experimental','source_family_ids':gold['source_family_ids'],
              'study_id':gold['study_id'],'score':0.0,'status':'invalid_submission','submission_complete':False}
    try:
        if gold['task_type'] == 'ranking':
            result = _ranking(prediction,gold['target_ids'],gold['truth'],gold['higher_is_better'],metric=gold.get('ranking_metric','spearman'),pairs=gold.get('resolvable_pairs'))
        elif gold['task_type'] == 'binary':
            result = _binary(prediction,gold['target_ids'],gold['truth'])
        elif gold['task_type'] == 'numeric':
            result = numeric(prediction,gold['target_ids'],gold['truth'])
        else:
            result = review(prediction,gold,judgment)
    except (ValueError,TypeError,OverflowError,RecursionError) as exc:
        return {**report,'error':str(exc)}
    return {**report,'status':'scored','submission_complete':True,**result}
