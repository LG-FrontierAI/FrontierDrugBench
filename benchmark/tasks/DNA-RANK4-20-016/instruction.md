---
bench_id: "DNA-RANK4-20-016"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with Parkinson's disease in individuals of European ancestry. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs12637471: GRCh38 chr3:183044649, plus-strand alleles G/A, specified allele G.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GCCCTGATCTGAAACCGAATGATGGCCTGGCCCAGAATGCTGTGGCCTTAGGTAGACCAT
GAGGCTTTGACCTTGAGGTGATGTGGTTGTGAGCAAGCCCC
```

rs17649553: GRCh38 chr17:45917282, plus-strand alleles C/T, specified allele C.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GTGCGAGCTCTGCCTTGCAGGGTTCGCATCTGCCTGTGCTGAGTAACCAACGCTAAGGTC
GAGTGGTCGGTCACCTCTCATAAGAGCTAGGGTTGTCTCAT
```

rs2414739: GRCh38 chr15:61701935, plus-strand alleles G/A, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
TCAAATAGAACAGTGAGGGCAAAGCCCCTCGAGTGGGAATCAGTTGGCATGTACTAGGGA
CACGGAGAAGGTCTTTATTTGTAAGGAGAAAAGTCCTGACT
```

rs117896735: GRCh38 chr10:119776815, plus-strand alleles G/A, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
TTTAGAGACATAGTCTTGCTCTGTCATCCAGGCTGGAGTACAGTGATCCAGTCATAGCTC
ACTGCAGCCTTGAACTCCTGGGCTCAAATGATCCTCCCACC
```

## Question

Rank the following variants by their association OR for Parkinson's disease, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs12637471(specified allele G)
B. rs17649553(specified allele C)
C. rs2414739(specified allele A)
D. rs117896735(specified allele A)
