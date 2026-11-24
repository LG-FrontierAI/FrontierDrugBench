---
bench_id: "PROT-V4-QUANT-015"
category: "Disease-Biology"
title: "TGFBR2 variant function prediction (A,B,C,D)"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "TGFBR2",
  "experimental_system": "Human TGF-β type II receptor extracellular domain binding to TGF-β3, measured at 298 K by SPR.",
  "sequence_region": "UniProt P37173, residues 38–159 in full-length protein numbering",
  "wild_type_sequence": "VTDNNGAVKFPQLCKFCDVRFSTCDNQKSCMSNCSITSICEKPQEVCVAVWRKNDENITLETVCHDPKLPYHDFILEDAASPKCIMKEKKKPGETFFMCSCSSDECNDNIIFSEEYNTSNPD",
  "variants": {
    "A": "position 75 S→A",
    "B": "position 55 D→N",
    "C": "position 75 S→L",
    "D": "position 53 F→A"
  }
}
```

## Question

Rank these receptor variants by affinity for TGF-β3, from strongest to weakest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"]; do not use ties.

## Options
