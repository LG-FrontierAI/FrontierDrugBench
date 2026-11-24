"""Prepare RDKit comparisons and merge molecular tool outputs. Never invent pKa."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from rdkit import Chem

AMINE = Chem.MolFromSmarts("[N;X3;!$(N-[C,S,P]=[O,S,N]);!$(N-[N,O,S]);!$(N~[!#6;!#1])]")
PYRIDINE = Chem.MolFromSmarts("[nH0;+0;X2]")
QUAT = Chem.MolFromSmarts("[N+;X4;H0]([#6])([#6])([#6])[#6]")
ESTER = Chem.MolFromSmarts("[#6][CX3](=O)[OX2][#6]")
UREA = Chem.MolFromSmarts("[NX3][CX3](=O)[NX3]")


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def load_gold(question: Path) -> dict:
    """Support the harness processed layout and raw package layout."""
    ans = question / "tests" / "answer.json"
    if ans.is_file():
        obj = read(ans)
        if isinstance(obj, dict) and isinstance(obj.get("reference"), dict):
            return obj["reference"]
        return obj
    ref = question / "scoring" / "reference_answer.json"
    if ref.is_file():
        return read(ref)
    raise FileNotFoundError(f"no gold under {question}")


def canonical(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError("Invalid SMILES")
    return Chem.MolToSmiles(mol, isomericSmiles=False), mol


def tails_and_head(mol):
    carbons = {
        a.GetIdx()
        for a in mol.GetAtoms()
        if a.GetAtomicNum() == 6
        and not a.GetIsAromatic()
        and all(b.GetBondType() == Chem.BondType.SINGLE for b in a.GetBonds())
    }
    adjacency = {
        i: [a.GetIdx() for a in mol.GetAtomWithIdx(i).GetNeighbors() if a.GetIdx() in carbons]
        for i in carbons
    }
    paths = []
    for start in carbons:
        if len(adjacency[start]) != 1:
            continue
        path = [start]
        previous = None
        current = start
        while True:
            nxt = [i for i in adjacency[current] if i != previous]
            if not nxt:
                break
            if len(nxt) > 1:
                break
            previous, current = current, nxt[0]
            if current in path:
                break
            path.append(current)
            if len(adjacency[current]) != 2:
                break
        if len(path) >= 8 and frozenset(path) not in [frozenset(p) for p in paths]:
            paths.append(path)
    remove = {i for path in paths for i in path[:-1]}
    core = Chem.RWMol(mol)
    for i in sorted(remove, reverse=True):
        core.RemoveAtom(i)
    return len(paths), Chem.MolToSmiles(core, isomericSmiles=False)


def amine_head_signature(mol):
    sites = {match[0] for query in (AMINE, PYRIDINE) for match in mol.GetSubstructMatches(query)}
    signatures = []
    for site in sites:
        selected = {site}
        frontier = {site}
        for _ in range(2):
            frontier = {
                a.GetIdx() for i in frontier for a in mol.GetAtomWithIdx(i).GetNeighbors()
            } - selected
            selected.update(frontier)
        changed = True
        while changed:
            size = len(selected)
            for ring in mol.GetRingInfo().AtomRings():
                if set(ring) & selected:
                    selected.update(ring)
            changed = len(selected) != size
        signatures.append(
            Chem.MolFragmentToSmiles(mol, atomsToUse=sorted(selected), isomericSmiles=False)
        )
    return "|".join(sorted(signatures))


def generated(pred, gold):
    seen = set()
    inspired = {canonical(s)[0] for s in gold["inspiration_smiles"]}
    rows = []
    for item in pred["designs"]:
        row = {"id": item["id"], "smiles": item.get("smiles"), "eligible": False, "issues": []}
        try:
            key, mol = canonical(item["smiles"])
            row["canonical_smiles"] = key
            if key in seen:
                row["issues"].append("duplicate molecular graph")
            seen.add(key)
            if key in inspired:
                row["issues"].append("copied inspiration structure")
            if len(Chem.GetMolFrags(mol)) != 1:
                row["issues"].append("must be one connected molecule")
            if mol.HasSubstructMatch(QUAT):
                row["issues"].append("permanent quaternary ammonium")
            if not (mol.HasSubstructMatch(AMINE) or mol.HasSubstructMatch(PYRIDINE)):
                row["issues"].append("no protonatable amine")
            if not mol.HasSubstructMatch(ESTER):
                row["issues"].append("no carboxylate ester")
            if gold.get("required_urea") and not mol.HasSubstructMatch(UREA):
                row["issues"].append("no urea linker")
            if gold.get("forbidden_urea") and mol.HasSubstructMatch(UREA):
                row["issues"].append("urea linker forbidden by this task")
            tails, head = tails_and_head(mol)
            row["head_scaffold"] = head
            if gold.get("head_signature_mode") == "amine_local_2_bonds":
                row["head_scaffold"] = amine_head_signature(mol)
            if tails < 2:
                row["issues"].append("fewer than two C8 saturated alkyl paths")
            row["eligible"] = not row["issues"]
        except (ValueError, TypeError, KeyError) as exc:
            row["issues"].append(str(exc))
        rows.append(row)
    return rows


def extraction_rows(pred, gold):
    rows = []
    refs = {x["id"]: x["canonical_smiles"] for x in gold["reference_rows"]}
    for item in pred["molecules"]:
        row = {"id": item.get("id"), "matched_id": None}
        try:
            key, _ = canonical(item["smiles"])
            row["canonical_smiles"] = key
            if refs.get(item.get("id")) == key:
                row["matched_id"] = item["id"]
        except (ValueError, TypeError, KeyError):
            pass
        rows.append(row)
    return rows


def merge_generation(rows, il_results: Path, pka_results: Path):
    with il_results.open(encoding="utf-8-sig", newline="") as f:
        il = list(csv.DictReader(f))
    il_by_graph = {}
    for x in il:
        if x["status"] != "ok":
            continue
        il_by_graph[canonical(x["smiles"])[0]] = float(x["il_likeness"])
    pkas = {x["name"]: x for x in read(pka_results)}
    for x in rows:
        if not x["eligible"]:
            continue
        if x["canonical_smiles"] not in il_by_graph or x["id"] not in pkas:
            raise ValueError("Incomplete evaluator output for " + x["id"])
        value = pkas[x["id"]].get("max_basic_micro_pka")
        if value is None:
            raise ValueError("Missing basic pKa output for " + x["id"])
        x["il_likeness"] = il_by_graph[x["canonical_smiles"]]
        x["max_basic_micro_pka"] = value
    return rows


def write_tool_results(path: Path, question_id: str, pred: dict, rows: list) -> Path:
    path.write_text(
        json.dumps(
            {"question_id": question_id, "prediction": pred, "rows": rows},
            ensure_ascii=False,
            indent=2,
            allow_nan=False,
        )
        + "\n",
        encoding="utf-8",
    )
    return path


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=["prepare", "collect"])
    p.add_argument("--question", type=Path, required=True)
    p.add_argument("--prediction", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--il-results", type=Path)
    p.add_argument("--pka-results", type=Path)
    args = p.parse_args()
    pred = read(args.prediction)
    gold = load_gold(args.question)
    if args.output.resolve() == args.prediction.resolve():
        p.error("Output must differ from prediction")
    if gold["mode"] == "extraction":
        if args.action != "collect":
            p.error("Extraction only needs collect")
        rows = extraction_rows(pred, gold)
    elif gold["mode"] == "generation":
        rows = generated(pred, gold)
        if args.action == "prepare":
            with args.output.open("w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=["name", "smiles"])
                w.writeheader()
                w.writerows({"name": x["id"], "smiles": x["smiles"]} for x in rows if x["eligible"])
            print("Prepared", sum(x["eligible"] for x in rows), "eligible molecules.")
            return
        if args.il_results is None or args.pka_results is None:
            p.error("collect needs --il-results and --pka-results")
        rows = merge_generation(rows, args.il_results, args.pka_results)
    else:
        p.error("Only generation and extraction are supported")
    write_tool_results(args.output, gold["id"], pred, rows)
    print("Saved", args.output)


if __name__ == "__main__":
    main()
