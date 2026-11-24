---
bench_id: "PROT-V4-QUANT-025"
category: "Disease-Biology"
title: "CRYGD variant function prediction (A,B,C,D)"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "CRYGD",
  "experimental_system": "Human γD-crystallin, associated with cataract, at pH 3.0 and 298.15 K; estimate unfolding free energy by urea denaturation monitored by fluorescence. ΔΔG_unfold = ΔG_unfold(variant) − ΔG_unfold(WT).",
  "sequence_region": "UniProt P07320, residues 1–174 in full-length protein numbering",
  "wild_type_sequence": "MGKITLYEDRGFQGRHYECSSDHPNLQPYLSRCNSARVDSGCWMLYEQPNYSGLQYFLRRGDYADHQQWMGLSDSVRSCRLIPHSGSHRIRLYEREDYRGQMIEFTEDCSCLQDRFRFNEIHSLNVLEGSWVLYELSNYRGRQYLLMPGDYRRYQDWGATNARVGSLRRVIDFS",
  "variants": {
    "A": "position 54 L→E",
    "B": "position 70 M→W",
    "C": "position 42 C→T",
    "D": "position 23 H→T"
  }
}
```

## Question

Rank the variants by their change in unfolding free energy ΔΔG_unfold, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"]; do not use ties.

## Options
