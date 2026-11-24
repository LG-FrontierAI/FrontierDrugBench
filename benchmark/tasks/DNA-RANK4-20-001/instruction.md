---
bench_id: "DNA-RANK4-20-001"
category: "Disease-Biology"
title: "Genotype risk ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare Alzheimer's disease risk in individuals of European ancestry. Cases were confirmed by clinical diagnosis or autopsy; controls had no dementia. For each chromosome, the plus-strand alleles at rs429358 and rs7412 are listed in that order, with a slash separating the two chromosomes.

The two sites are GRCh38 chr19:44908684 (T/C) and chr19:44908822 (C/T).
Reference DNA (plus strand, 5′→3′, chr19:44908635–44908872; the two sites are at positions 50 and 188):

```text
GGAGCTGCAGGCGGCGCAGGCCCGGCTGGGCGCGGACATGGAGGACGTGTGCGGCCGCCT
GGTGCAGTACCGCGGCGAGGTGCAGGCCATGCTCGGCCAGAGCACCGAGGAGCTGCGGGT
GCGCCTCGCCTCCCACCTGCGCAAGCTGCGTAAGCGGCTCCTCCGCGATGCCGATGACCT
GCAGAAGCGCCTGGCAGTGTACCAGGCCGGGGCCCGCGAGGGCGCCGAGCGCGGCCTC
```

## Question

Rank the following genotypes by Alzheimer's disease risk, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. (T,C)/(C,C)
B. (T,T)/(T,C)
C. (T,C)/(T,C)
D. (C,C)/(C,C)
