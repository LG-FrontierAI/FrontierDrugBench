---
bench_id: "PROT-V4-MECH-004"
category: "Disease-Biology"
title: "SNCA variant function prediction (M1,M2)"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "SNCA",
  "species": "Homo sapiens",
  "wild_type_sequence": "MDVFMKGLSKAKEGVVAAAEKTKQGVAEAAGKTKEGVLYVGSKTKEGVVHGVATVAEKTKEQVTNVGGAVVTGVTAVAQKTVEGAGSIAAATGFVKKDQLGKNEEGAPQEGILEDMPVDPDNEAYEMPSEEGYQDYEPEA",
  "variants": {
    "M1": "position 30 A→P",
    "M2": "position 53 A→T"
  },
  "experiment": "Incubate each purified recombinant α-synuclein protein at 200 μM under the same buffer conditions; define the fibril-formation lag time as the time until a sustained increase in Thioflavin T fluorescence."
}
```

## Question

Which option predicts the lag times of M1, M2, and WT from shortest to longest, given the sequence effects of these substitutions? Output only the letter(s) corresponding to your answer.

## Options

A. M2 < WT < M1
B. WT < M1 < M2
C. M1 < M2 < WT
D. M1 < WT < M2
