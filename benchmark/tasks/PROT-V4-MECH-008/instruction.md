---
bench_id: "PROT-V4-MECH-008"
category: "Disease-Biology"
title: "APP variant function prediction (position 673 A→T)"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "APP",
  "species": "Homo sapiens",
  "sequence_region": "WT residues 660–690; positions use full-length numbering",
  "wild_type_sequence": "NIKTEEISEVKMDAEFRHDSGYEVHHQKLVF",
  "variant": "position 673 A→T",
  "experiment": "Measure BACE1 cleavage using a FRET substrate containing APP residues 668–675. Use matched substrate concentration series, enzyme amounts, and reaction conditions to fit apparent Km and Vmax separately. The nearby WT sequence is supplied, with APP770 numbering."
}
```

## Question

Which kinetic combination is most likely to result from this substitution? Output only the letter(s) corresponding to your answer.

## Options

A. Vmax increases markedly, while Km is unchanged
B. Both Vmax and Km increase markedly
C. Vmax decreases, with no marked change in Km
D. Vmax is unchanged, while Km decreases markedly
