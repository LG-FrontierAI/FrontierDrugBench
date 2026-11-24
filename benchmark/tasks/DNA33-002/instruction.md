---
bench_id: "DNA33-002"
category: "Disease-Biology"
title: "Strong splice-disrupting variant identification"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

## Context

In a splicing reporter assay in HEK293T cells, the following 170 bp fragment is inserted into a DHFR intron backbone. The sequence is shown 5′→3′ in the direction of transcription; positions 46–135 span the test exon. An inclusion index of 0 indicates complete skipping, and 1 indicates complete inclusion. Positions are 1-based, and each option changes a single base independently.

```text
ATGAGCCCAGTACTAACTACAGATGTCCGGACAATCCCCTTTTAGGCGGGCTGTGTTGCC
AACAATGCGGTCATCAGAAAGAACGCCGTGATGGGGCAGCCCACCGAGGGTGCATTGATG
GCCCTGGCGATGAAGGTAGGAGGTCCTGGGGTGGCTCTGCGGGGAATTCT
```

## Question

Which variants cause strong splicing disruption (a decrease in exon inclusion index of at least 0.50 relative to the reference sequence)? Return one JSON object {"selected": ["<option letter>", ...]} listing every option letter that applies.

## Options

A. position 84 C→T
B. position 78 A→G
C. position 64 A→G
D. position 84 C→A
