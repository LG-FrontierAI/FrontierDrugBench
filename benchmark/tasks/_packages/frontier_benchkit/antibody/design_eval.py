"""Tool-free contestant sequence submission checks and organizer proxies.

This evaluator is deliberately transparent about its boundary. It can validate
sequences and calculate reproducible sequence proxies. Versioned affinity or
interface predictors may be attached by an organizer adapter, but their raw
scores must remain separate from biological success.
"""

from __future__ import annotations

import itertools
from collections import Counter
from typing import Any

AA = set("ACDEFGHIKLMNPQRSTVWY")
HYDRO = set("AILMFWVY")
CHARGED = set("DEKR")


def levenshtein(a: str, b: str) -> int:
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(cur[-1] + 1, prev[j] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def sequence_proxies(seq: str) -> dict[str, Any]:
    if not isinstance(seq, str) or not seq or any(x not in AA for x in seq):
        return {"valid": False}
    n = len(seq)
    return {
        "valid": True,
        "length": n,
        "hydrophobic_fraction": sum(x in HYDRO for x in seq) / n,
        "charged_fraction": sum(x in CHARGED for x in seq) / n,
        "net_charge_proxy": sum(1 if x in "KR" else -1 if x in "DE" else 0 for x in seq),
        "cysteine_count": seq.count("C"),
        "n_glyco_motifs": sum(seq[i] == "N" and seq[i + 1] != "P" and seq[i + 2] in "ST" for i in range(n - 2)),
        "deamidation_motifs": sum(seq[i:i + 2] in {"NG", "NS"} for i in range(n - 1)),
        "oxidation_motifs": sum(x in "MW" for x in seq),
    }


def evaluate_design(task: dict[str, Any], candidates: list[dict[str, Any]]) -> dict[str, Any]:
    if not isinstance(task, dict) or task.get('status', 'ready') != 'ready':
        raise ValueError('A ready design task object is required')
    refs = task.get("reference_chains", {})
    if not isinstance(refs, dict) or not refs or any(not isinstance(k, str) or not k.strip() or k != k.strip() for k in refs) or any(not sequence_proxies(s).get("valid") for s in refs.values()):
        raise ValueError("Nonempty, valid reference chains must be installed before evaluation")
    if not isinstance(candidates, list) or len(candidates) != 10:
        raise ValueError("Exactly ten candidates are required")
    if any(not isinstance(r, dict) or not isinstance(r.get("id"), str) or not r["id"].strip() or r['id'] != r['id'].strip() for r in candidates):
        raise ValueError("Every candidate needs a nonempty string id")
    if len({r["id"] for r in candidates}) != 10:
        raise ValueError("Candidate ids must be unique")
    if any(not isinstance(r.get("rank"), int) or isinstance(r["rank"], bool) for r in candidates) or sorted(r["rank"] for r in candidates) != list(range(1, 11)):
        raise ValueError("Ranks must be the integers 1 through 10 exactly once")
    raw_positions = task.get('designable_positions')
    if not isinstance(raw_positions, dict) or set(raw_positions) != set(refs):
        raise ValueError("Explicit designable positions are required for every reference chain")
    positions = {}
    for chain, ps in raw_positions.items():
        if not isinstance(ps, list) or any(not isinstance(i, int) or isinstance(i, bool) or not 1 <= i <= len(refs[chain]) for i in ps):
            raise ValueError("Designable positions must be valid 1-based sequence indices")
        if len(ps) != len(set(ps)):
            raise ValueError('Designable positions cannot contain duplicate indices')
        positions[chain] = set(ps)
    if not any(positions.values()):
        raise ValueError('At least one explicit designable position is required')
    chain_names = tuple(refs)
    rows = []
    keys = [tuple(r.get('chains', {}).get(k) for k in chain_names)
            if isinstance(r.get('chains'), dict) and all(isinstance(r['chains'].get(k), str) for k in chain_names) else None
            for r in candidates]
    duplicate_counts = Counter(k for k in keys if k is not None)
    for row in sorted(candidates, key=lambda r: r['rank']):
        cid = str(row.get("id", ""))
        chains = row.get("chains", {})
        errors = []
        proxy = {}
        if not isinstance(chains, dict):
            chains = {}
            errors.append("chains_must_be_an_object")
        if set(chains) != set(chain_names):
            errors.append("chain_set_mismatch")
        else:
            for chain in chain_names:
                seq = chains.get(chain)
                p = sequence_proxies(seq)
                proxy[chain] = p
                if not p.get("valid"):
                    errors.append(f"{chain}:invalid_sequence")
                elif len(seq) != len(refs[chain]):
                    errors.append(f"{chain}:length_not_allowed")
                else:
                    for i, aa in enumerate(refs[chain], 1):
                        if i not in positions.get(chain, set()) and seq[i - 1] != aa:
                            errors.append(f"{chain}:framework_changed")
        key = tuple(chains.get(k) if isinstance(chains.get(k), str) else None for k in chain_names)
        if duplicate_counts.get(key, 0) > 1:
            errors.append("duplicate_candidate")
        rows.append({"id": cid, 'rank': row['rank'], "hard_constraints_passed": not errors, "errors": sorted(set(errors)), "proxies": proxy, "chains": chains})
    valid = [r for r in rows if r["hard_constraints_passed"]]
    pairs = []
    for a, b in itertools.combinations(valid, 2):
        dist = 0
        denom = 0
        for chain in chain_names:
            sa, sb = a["chains"][chain], b["chains"][chain]
            dist += levenshtein(sa, sb)
            denom += max(len(sa), len(sb))
        pairs.append({"candidate_ids": [a["id"], b["id"]], "normalized_edit_distance": dist / denom if denom else None, "normalization_length": denom, "edit_distance": dist})
    return {
        "status": "sequence_and_proxy_evaluated",
        "submitted": len(candidates),
        "expected": 10,
        "hard_constraint_pass_rate": len(valid) / 10,
        "rows": rows,
        "diversity": {"pairs": pairs, "status": "normalized_edit_distance_computed"},
        "affinity_proxy": {"status": "not_run", "reason": "versioned organizer predictor not attached"},
        "biological_success": {"status": "not_evaluated"},
    }
