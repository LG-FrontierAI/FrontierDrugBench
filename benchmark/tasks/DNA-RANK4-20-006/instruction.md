---
bench_id: "DNA-RANK4-20-006"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with asthma in a predominantly European-ancestry population. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs174562: GRCh38 chr11:61817672, plus-strand alleles A/G, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
AAGCCTGGGTCTTCAAGCTGAGGCATTTCTGTTCTAGCCTGGAGGCGCCTAGGAGCCCTG
GGAGACTTTTTAAGCAGAGAGATTTGGCATTTAGATCTCTG
```

rs149045797: GRCh38 chr9:6252690, plus-strand alleles T/G, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
ACATGGCCTCCCAGGGCCTTCATGCAGGACACTAGCACCTTTAATCCCATTCAAGGGTCA
CATCTCAGCCTTTTAGCTATGTAAAACTTGTATCAAAGGCT
```

rs12722502: GRCh38 chr10:6051176, plus-strand alleles C/T, specified allele C.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GTTCTTTTTGTTCTAAATCAGGCTGTAAACAGAGGTGCTACCACAAGGACCGGAAGCAGA
GACCACACTGGTGCTCAGCTGGGTTGCAGGCTCTGCCTGGT
```

rs117710327: GRCh38 chr19:33235672, plus-strand alleles C/A, specified allele C.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
CGGCTCAGGCTCTTTTCTGCTGTAGCCCGAGAGAAGAGATGCAGGGGAGGCCCCAGGGAC
TGTGGGTGCTGGCCTGGGTCAGGACATTCATAGTGAAACCA
```

## Question

Rank the following variants by their association OR for asthma, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs174562(specified allele A)
B. rs149045797(specified allele T)
C. rs12722502(specified allele C)
D. rs117710327(specified allele C)
