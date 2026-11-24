---
bench_id: "PROT-V4-QUANT-003"
category: "Disease-Biology"
title: "GH1 variant function prediction (A,B,C,D)"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "GH1",
  "experimental_system": "Mature human growth hormone binding to the human GHR extracellular binding domain, measured at 298 K by SPR; input numbering follows the full-length precursor sequence.",
  "sequence_region": "UniProt P01241, residues 27–217 in full-length protein numbering",
  "wild_type_sequence": "FPTIPLSRLFDNAMLRAHRLHQLAFDTYQEFEEAYIPKEQKYSFLQNPQTSLCFSESIPTPSNREETQQKSNLELLRISLLLIQSWLEPVQFLRSVFANSLVYGASDSNVYDLLKDLEEGIQTLMGRLEDGSPRTGQIFKQTYSKFDTNSHNDDALLKNYGLLYCFRKDMDKVETFLRIVQCRSVEGSCGF",
  "variants": {
    "A": "position 200 E→A",
    "B": "position 198 K→A",
    "C": "position 193 R→A",
    "D": "position 197 D→A"
  }
}
```

## Question

At the same receptor concentration, rank these growth hormone variants by the second-order association rate constant k_on, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"]; do not use ties.

## Options
