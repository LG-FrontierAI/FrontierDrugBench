---
bench_id: "DNA-RANK4-20-019"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with hypothyroidism in individuals of European ancestry. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs4835534: GRCh38 chr4:148715236, plus-strand alleles T/C, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
CTTGGTTTTAGGGAGACATAAGACATCAGTCAATACATGTTACATGTCCATTGGTTGGTC
CAGAAAAGTGGAACACTTTGAAGGGGAGTGGGGTTAGAGTG
```

rs182787262: GRCh38 chr16:50377862, plus-strand alleles T/C, specified allele C.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
ATTTTATACATTGGAAATGAATAACACATTGACATTTGGGTCTTCATTGATTGTAAAAAG
TAAATGTTAAGAACTTTTTTTTTCTTTTTTTTTTTTTTAAG
```

rs17020127: GRCh38 chr1:107815461, plus-strand alleles A/G, specified allele G.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
TGCCAAGTGACACGGACAGTGCCCCTGGCCAACTCTCATCACCAAATTCAATGATGTGAT
TTTACGCACTGTTCCAGGCTGCCTGGTTCTAAGGCCCTTGC
```

rs9298749: GRCh38 chr9:16214342, plus-strand alleles A/C, specified allele C.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
CAGAAACTGTGGTAAGCACTTTGTAAGCACTTTCTCATGTAATCTTTATGAAAACTCTGT
GATGTAGGTACCGTTCTTACTCCTGTTTGCAGATGGGCAAG
```

## Question

Rank the following variants by their association OR for hypothyroidism, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs4835534(specified allele T)
B. rs182787262(specified allele C)
C. rs17020127(specified allele G)
D. rs9298749(specified allele C)
