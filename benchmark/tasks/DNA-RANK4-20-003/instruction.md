---
bench_id: "DNA-RANK4-20-003"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with type 2 diabetes in individuals of European ancestry. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs10811660: GRCh38 chr9:22134069, plus-strand alleles G/A, specified allele G.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
ATAACCTTTCCGGCCCATTTTCTTTGTCAATAAGCGTTCTTGCCCTGTCAGCAGCTCACC
TCCAGCTTTAGTTTTCTCATGACAGTAAGTCTATTACCCTC
```

rs2197973: GRCh38 chr12:95534784, plus-strand alleles C/T, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GGTGCGATCTCAGCTCACTGCAACCCCTGCCTCCTGGGCTCACGTGATTGCTGTGCCTCA
GCCTCCCGGGTAGCTGGGATTATAGGAGTGCACCACCACAT
```

rs67254669: GRCh38 chr11:17448596, plus-strand alleles A/G, specified allele G.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
CAAGAAGAAAAACCACATGAGCTGATTGGTGTCGATGGCAACCAGATTACAGATCTGTCC
AGCAGTCATTTCTCCCATGGACAGGTTGGAGGTGGACAGGT
```

rs184660829: GRCh38 chr1:114602278, plus-strand alleles T/C, specified allele C.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
AAACAATTACTTATGGCATTCTCCATGGAACAAACAATTGAAAACTAGAGTCCAACAGTA
GTCATTTTGTGATCTAGTTAGGATCCAAACAACCACTTACG
```

## Question

Rank the following variants by their association OR for type 2 diabetes, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs10811660(specified allele G)
B. rs2197973(specified allele T)
C. rs67254669(specified allele G)
D. rs184660829(specified allele C)
