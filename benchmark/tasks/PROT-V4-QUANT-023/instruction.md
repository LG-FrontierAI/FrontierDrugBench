---
bench_id: "PROT-V4-QUANT-023"
category: "Disease-Biology"
title: "LYZ variant function prediction (A,B,C,D)"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "LYZ",
  "experimental_system": "Mature human lysozyme at pH 2.7, measured by differential scanning calorimetry, with unfolding free energy evaluated at 338.05 K. Compare ΔΔG_unfold = ΔG_unfold(variant) − ΔG_unfold(WT); positive values indicate greater stability. Numbering refers to the precursor including its signal peptide.",
  "sequence_region": "UniProt P61626, residues 19–148 in full-length protein numbering",
  "wild_type_sequence": "KVFERCELARTLKRLGMDGYRGISLANWMCLAKWESGYNTRATNYNAGDRSTDYGIFQINSRYWCNDGKTPGAVNACHLSCSALLQDNIADAVACAKRVVRDPQGIRAWVAWRNRCQNRDVRQYVQGCGV",
  "variants": {
    "A": "position 74 I→L",
    "B": "position 74 I→M",
    "C": "position 74 I→V",
    "D": "position 74 I→F"
  }
}
```

## Question

Rank these substitutions at the same position by ΔΔG_unfold, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"]; do not use ties.

## Options
