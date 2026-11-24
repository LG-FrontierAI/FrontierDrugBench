---
bench_id: "PROT-V4-QUANT-008"
category: "Disease-Biology"
title: "PLAUR variant function prediction (position 71 E→A)"
format: "structured_json"
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
  "variant": "position 71 E→A"
}
```

## Question

Predict k_on of this uPAR variant binding pro-uPA (M⁻¹·s⁻¹). Return one JSON object {"value": <number>} holding that single finite number.
