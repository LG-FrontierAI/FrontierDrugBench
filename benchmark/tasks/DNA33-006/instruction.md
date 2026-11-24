---
bench_id: "DNA33-006"
category: "Disease-Biology"
title: "Regulatory activity decrease prediction"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

## Context

Reporter activity of this enhancer is measured in SK-MEL-28 cells (24 hours). The following is the GRCh38 reference sequence of the region containing the test variants (plus strand, 5′→3′, 451 bp). Positions are 1-based; consider each variant independently. The effect is the single-variant activity ratio fitted in the saturation mutagenesis reporter assay.

```text
GGCGTGTCCGCCTGTTGGAATATGCTTCTCAGGTCTTCTGGGAAACAGATGTTTTGTGGA
AGTGGAAGATTTTGGAAGTAGTGCCTTATCATGTGAAACCACAGGGCAGCTGATCTCTTC
AGGCTTTCTTGATGTGAATGACAGCTTTGTTTCATCCACTTTGGTGGGTAAAAGAAGGCA
AATTCCCCTGTGGTACTTTTGGTGCCAGGTTTAGCCATATGACGAAGCTTTACATAAAAC
AGTACAAGTATCTCCATTGTCCTTTATGATCCTCCATGAGTGTTTTCACTTAGTCTGATG
AAGGGTTCACTCCAGTCTTTTCGGATGATAAAATGCTTCGGCTGTCAGTCTAATAAGGGA
TTCCCTGAGGAGTTTGGAGGCTGTAAGAGCACCCCCCGTCTCAATGCCAGTGCTTCTTAT
CTCAGCCTCTCCTGCACTCCTTTACCCCCGT
```

## Question

Which variants decrease the reporter activity of this regulatory region? Return one JSON object {"selected": ["<option letter>", ...]} listing every option letter that applies.

## Options

A. position 246 A→T
B. position 234 A→G
C. position 90 C→A
D. position 364 C→A
