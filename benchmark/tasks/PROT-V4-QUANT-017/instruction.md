---
bench_id: "PROT-V4-QUANT-017"
category: "Disease-Biology"
title: "CSF2 variant function prediction (A,B,C,D)"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "CSF2",
  "experimental_system": "Competitive binding of human GM-CSF variants to CHO cells expressing WT GM-CSFRα; 277 K, with only the receptor α chain present.",
  "sequence_region": "UniProt P04141, residues 18–144 in full-length protein numbering",
  "wild_type_sequence": "APARSPSPSTQPWEHVNAIQEARRLLNLSRDTAAEMNETVEVISEMFDLQEPTCLQTRLELYKQGLRGSLTKLKGPLTMMASHYKQHCPPTPETSCATQIITFESFKENLKDFLLVIPFDCWEPVQE",
  "variants": {
    "A": "position 128 K→A",
    "B": "position 129 D→K",
    "C": "position 129 D→R",
    "D": "position 126 N→A"
  }
}
```

## Question

Considering only binding to GM-CSFRα, rank these GM-CSF variants by affinity, from strongest to weakest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"]; do not use ties.

## Options
