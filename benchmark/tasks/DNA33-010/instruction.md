---
bench_id: "DNA33-010"
category: "Disease-Biology"
title: "Activity comparison between variants"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

## Context

Reporter activity of this promoter is measured in HEK293T cells (24 hours). The following is the GRCh38 reference sequence of the region containing the test variants (plus strand, 5′→3′, 259 bp). Positions are 1-based; consider each variant independently. The effect is the single-variant activity ratio fitted in the saturation mutagenesis reporter assay.

```text
TCGCGGGGGTGGCCGGGGCCAGGGCTTCCCACGTGCGCAGCAGGACGCAGCGCTGCCTGA
AACTCGCGCCGCGAGGAGAGGGCGGGGCCGCGGAAAGGAAGGGGAGGGGCTGGGAGGGCC
CGGAGGGGGCTGGGCCGGGGACCCGGGAGGGGTCGGGACGGGGCGGGGTCCGCGCGGAGG
AGGCGGAGCTGGAAGGTGAAGGGGCAGGACGGGTGCCCGGGTCCCCAGTCCCTCCGCCAC
GTGGGAAGCGCGGTCCTGG
```

## Question

In each option, X and Y represent separate variants. In which options does X have higher reporter activity than Y? Return one JSON object {"selected": ["<option letter>", ...]} listing every option letter that applies.

## Options

A. X: position 259 G→A; Y: position 147 G→A
B. X: position 107 G→A; Y: position 252 G→T
C. X: position 259 G→C; Y: position 237 C→G
D. X: position 125 G→T; Y: position 257 T→G
