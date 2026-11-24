---
bench_id: "DNA-RANK4-20-004"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with coronary artery disease in a predominantly European-ancestry population. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs7133378: GRCh38 chr12:123924955, plus-strand alleles G/A, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
AATGACAGATCTGACCAGGTGGCCTTCAGTTAGTACACCTATGGATTCTCGTCCCTTTCC
AGTGGCTTTTGCCACCTTCACACATAAATGGGGACCTATGT
```

rs184278183: GRCh38 chr6:160756724, plus-strand alleles C/T, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
ATATTAGCTTTCCTTGTACACTATTTGCCTCCAAAACTCAATCTCTCTTTCTTTTCTCTG
TCTACTTACCTCTATTACCTATCTATCATCTATTATCTATT
```

rs2891168: GRCh38 chr9:22098620, plus-strand alleles A/G, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
ATAGCACAGGATGTTCCAGTCACTCTAACAAAAGATGTCCTGTTTGGAACACCAACTCTG
TATCAGTTACTTCAGACACTTTCTCTCATTGAGTCCCTTCA
```

rs3918226: GRCh38 chr7:150993088, plus-strand alleles C/T, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GGGAAGCGTGCGTCACTGAATGACAGGGTGGGGGTGGAGGCACTGGAAGGCAGCTTCCTG
CTCTTTTGTGTCCCCCACTTGAGTCATGGGGGTGTGGGGGT
```

## Question

Rank the following variants by their association OR for coronary artery disease, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs7133378(specified allele A)
B. rs184278183(specified allele T)
C. rs2891168(specified allele A)
D. rs3918226(specified allele T)
