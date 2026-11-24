---
bench_id: "DNA33-007"
category: "Disease-Biology"
title: "Regulatory activity increase prediction"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

## Context

Reporter activity of this enhancer is measured in HepG2 cells (24 hours). The following is the GRCh38 reference sequence of the region containing the test variants (plus strand, 5′→3′, 600 bp). Positions are 1-based; consider each variant independently. The effect is the single-variant activity ratio fitted in the saturation mutagenesis reporter assay.

```text
GAACTGGAAAAGCCCTGTCCGGTGAGGGGGCAGAAGGACTCAGCGCCCCTGGACCCCCAA
ATGCTGCATGAACACATTTTCAGGGGAGCCTGTGCCCCCAGGCGGGGGTCGGGCAGCCCC
AGCCCCTCTCCTTTTCCTGGACTCTGGCCGTGCGCGGCAGCCCAGGTGTTTGCTCAGTTG
CTGACCCAAAAGTGCTTCATTTTTCGTGCCCGCCCCGCGCCCCGGGCAGGCCAGTCATGT
GTTAAGTTGCGCTTCTTTGCTGTGATGTGGGTGGGGGAGGAAGAGTAAACACAGTGCTGG
CTCGGCTGCCCTGAGGGTGCTCAATCAAGCACAGGTTTCAAGTCTGGGTTCTGGTGTCCA
CTCACCCACCCCACCCCCCAAAATCAGACAAATGCTACTTTGTCTAACCTGCTGTGGCCT
CTGAGACATGTTCTATTTTTAACCCCTTCTTGGAATTGGCTCTCTTCTTCAAAGGACCAG
GTCCTGTTCCTCTTTCTCCCCGACTCCACCCCAGCTCCCTGTGAAGAGAGAGTTAATATA
TTTGTTTTATTTATTTGCTTTTTGTGTTGGGATGGGTTCGTGTCCAGTCCCGGGGGTCTG
```

## Question

Which variants increase the reporter activity of this regulatory region? Return one JSON object {"selected": ["<option letter>", ...]} listing every option letter that applies.

## Options

A. position 273 G→A
B. position 181 C→T
C. position 210 C→T
D. position 381 A→C
