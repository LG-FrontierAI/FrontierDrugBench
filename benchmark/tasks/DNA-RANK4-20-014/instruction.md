---
bench_id: "DNA-RANK4-20-014"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with prostate cancer in a Japanese population. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs4620729: GRCh38 chr11:69212868, plus-strand alleles C/A, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
TGTCGGTGGCTGTGTAGCTCATACTCACTCCATCTGGCAGTTTCCACCCACCGAGGACCA
CTCAAGTTTGCCCCACTCCATGTCTGCTGTTGGGAGGGGAT
```

rs13255059: GRCh38 chr8:127518371, plus-strand alleles A/G, specified allele G.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GTATCAGCCAGCCCCAGAGAGATCTATAAATATATGACTGACAGTAAGTCACCAAGTGTA
TTGGGTAACAGCTAAGTGATATAAAGTAATATTTATAAACT
```

rs149272765: GRCh38 chr3:128385626, plus-strand alleles C/T, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
AGTCCCGATGAGAACAACAGTGGACACTAACATTTACTACATGCCCAGCACGTGCTGACT
GTTTTATATGAGTTACCTCATTGACTTATGAGTTCCATTCC
```

rs339331: GRCh38 chr6:116888889, plus-strand alleles T/C, specified allele C.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
TGAGATGAAAAATTTATGTACACTTTGCATGAACTCTCTCTCCCCAGTTTTATGAGGTTT
ATCTTTAGTGACTAGGAGGACAGAAAGCTGCTCATTTATTA
```

## Question

Rank the following variants by their association OR for prostate cancer, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs4620729(specified allele A)
B. rs13255059(specified allele G)
C. rs149272765(specified allele T)
D. rs339331(specified allele C)
