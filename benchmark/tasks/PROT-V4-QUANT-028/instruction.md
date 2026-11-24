---
bench_id: "PROT-V4-QUANT-028"
category: "Disease-Biology"
title: "FKBP1A variant function prediction (position 77 I→A)"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "FKBP1A",
  "experimental_system": "Human FKBP12 (FKBP1A), an immunosuppressant-binding protein, at pH 7.5 and 298.15 K. Measure conformational stability by urea denaturation monitored by fluorescence. ΔΔG_unfold = ΔG_unfold(variant) − ΔG_unfold(WT); positive values indicate stabilization.",
  "sequence_region": "UniProt P62942, residues 1–108 in full-length protein numbering",
  "wild_type_sequence": "MGVQVETISPGDGRTFPKRGQTCVVHYTGMLEDGKKFDSSRDRNKPFKFMLGKQEVIRGWEEGVAQMSVGQRAKLTISPDYAYGATGHPGIIPPHATLVFDVELLKLE",
  "variant": "position 77 I→A"
}
```

## Question

Predict ΔΔG_unfold for this substitution (kcal/mol). Return one JSON object {"value": <number>} holding that single finite number.
