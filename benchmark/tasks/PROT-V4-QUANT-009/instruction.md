---
bench_id: "PROT-V4-QUANT-009"
category: "Disease-Biology"
title: "HRAS variant function prediction (A,B,C,D)"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "HRAS",
  "experimental_system": "Activated human H-Ras GTPase domain binding to the RAF1 Ras-binding domain, measured at 308 K by isothermal titration calorimetry.",
  "sequence_region": "UniProt P01112, residues 1–166 in full-length protein numbering",
  "wild_type_sequence": "MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAGQEEYSAMRDQYMRTGEGFLCVFAINNTKSFEDIHQYREQIKRVKDSDDVPMVLVGNKCDLAARTVESRQAQDLARSYGIPYIETSAKTRQGVEDAFYTLVREIRQH",
  "variants": {
    "A": "position 37 E→A",
    "B": "position 38 D→A",
    "C": "position 31 E→A",
    "D": "position 41 R→A"
  }
}
```

## Question

Predict the affinities of these H-Ras variants for RAF1 RBD and rank them from strongest to weakest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"]; do not use ties.

## Options
