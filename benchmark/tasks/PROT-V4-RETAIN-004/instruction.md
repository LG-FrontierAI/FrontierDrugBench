---
bench_id: "PROT-V4-RETAIN-004"
category: "Disease-Biology"
title: "KCNE1 variant function prediction (A,B,C,D)"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "KCNE1",
  "wild_type_sequence": "MILSNTTAVTPFLTKLWQETVQQGGNMSGLARRSPRSGDGKLEALYVLMVLGFFGFFTLGIMLSYIRSKKLEHSNDPFNVYIESDAWQEKDKAYVQARVLESYRSCYVVENHLAIEQPNTHLPETKPSP",
  "experimental_setting": "A single-variant expression system in HEK293T cells, with WT KCNQ1 coexpression. Measure KCNE1 surface trafficking by HA labeling and flow sorting. Scores are calibrated to a median of 0 for early nonsense variants and 1 for synonymous variants.",
  "variants": {
    "A": "position 124 E→V",
    "B": "position 107 Y→S",
    "C": "position 16 L→Q",
    "D": "position 121 H→G"
  }
}
```

## Question

With WT KCNQ1 coexpressed, which KCNE1 substitutions reach the cell surface more efficiently? Rank A–D by surface-trafficking score from highest to lowest, and Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options
