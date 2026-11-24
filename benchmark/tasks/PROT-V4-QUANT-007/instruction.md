---
bench_id: "PROT-V4-QUANT-007"
category: "Disease-Biology"
title: "PLAUR variant function prediction (A,B,C,D)"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "PLAUR",
  "experimental_system": "Binding of the human uPAR extracellular domain, associated with cancer invasion, to pro-urokinase pro-uPA, measured at 293 K by SPR.",
  "sequence_region": "UniProt Q03405, residues 23–303 in full-length protein numbering",
  "wild_type_sequence": "LRCMQCKTNGDCRVEECALGQDLCRTTIVRLWEEGEELELVEKSCTHSEKTNRTLSYRTGLKITSLTEVVCGLDLCNQGNSGRAVTYSRSRYLECISCGSSDMSCERGRHQSLQCRSPEEQCLDVVTHWIQEGEEGRPKDDRHLRGCGYLPGCPGSNGFHNNDTFHFLKCCNTTKCNEGPILELENLPQNGRQCYSCKGNSTHGCSSEETFLIDCRGPMNQCLVATGTHEPKNQSYMVRGCATASMCQHAHLGDAFSMNHIDVSCCTKSGCNHPDLDVQYR",
  "variants": {
    "A": "position 47 R→A",
    "B": "position 124 D→A",
    "C": "position 121 G→A",
    "D": "position 23 L→A"
  }
}
```

## Question

Rank these uPAR variants by binding affinity for pro-uPA, from strongest to weakest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"]; do not use ties.

## Options
