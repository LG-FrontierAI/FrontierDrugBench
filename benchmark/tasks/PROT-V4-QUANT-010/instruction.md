---
bench_id: "PROT-V4-QUANT-010"
category: "Disease-Biology"
title: "HRAS variant function prediction (position 36 I→A)"
format: "structured_json"
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
  "variant": "position 36 I→A"
}
```

## Question

Predict the equilibrium K_D of this H-Ras variant for RAF1 RBD (μM). Return one JSON object {"value": <number>} holding that single finite number.
