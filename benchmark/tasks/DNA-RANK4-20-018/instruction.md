---
bench_id: "DNA-RANK4-20-018"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with gout in individuals of European ancestry. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs7675964: GRCh38 chr4:9939810, plus-strand alleles C/T, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
CACCCTCCCTCACTCCTGGGGGGCAGGAATGTCATCTCATACCACTGTCTCACCCTGTCA
CCTGGCAGAACACCCAACATGCTAAATATCCATTGCTTGCT
```

rs77542162: GRCh38 chr17:69085137, plus-strand alleles A/G, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
CAGGTGTTCCCTCAACGTCAGCATGGGCCACAGCACGTTCTCTTGAGGGCAGTACCCCAG
GTGGCCCAAAACTGAACTGCAGCCTTTCAGTTCCACCTAAA
```

rs190676167: GRCh38 chr19:49003428, plus-strand alleles G/A, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
TCTTGGGTAGTGGGTACCCAGGGTCCTGGGGAGTGTGGGGACTATGTTACGGTCTTCTGG
ACCTTTGGCTACATACCCATAAACTTCAACCACATGTGGGT
```

rs10851885: GRCh38 chr15:76012162, plus-strand alleles A/G, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
TGTAATACCAAGGTCTTCTCTCAAAGCCAACAGCTCTTTCTTAGACAAGCAGAGAGGCAG
AGAAAGCGAGCAAGCAATCGAGAGAAACACACACGAGCGAG
```

## Question

Rank the following variants by their association OR for gout, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs7675964(specified allele T)
B. rs77542162(specified allele A)
C. rs190676167(specified allele A)
D. rs10851885(specified allele A)
