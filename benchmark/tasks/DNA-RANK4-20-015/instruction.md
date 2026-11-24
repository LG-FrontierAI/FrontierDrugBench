---
bench_id: "DNA-RANK4-20-015"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with colorectal cancer in individuals of European ancestry. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs12979278: GRCh38 chr19:48715345, plus-strand alleles C/T, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
CACAGAGATGGCCCAGGAGGACCCAGGGCGGACCCCTCGGCTTGGGGGTCCGCCCTGGAT
CCCTGTCTCGGCTCTGGGGGCATGTACTGGTGGTATGTCAA
```

rs4944940: GRCh38 chr11:74704207, plus-strand alleles G/A, specified allele G.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
TCCATTTCCCATCTATCTGTTCTGTCTGCCCCTCTTCCCAGCAAAGACTCGGTAGATGCT
AAAAAAAATCTTGTACTGTTCCAGAACTAGTTGTCTCTTAC
```

rs7894531: GRCh38 chr10:8692798, plus-strand alleles G/A, specified allele G.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
TTTGCCAGATCCAGACATCAGACTTAGCTTTACAACCGTCTATCAGAAGCGCCATACAGT
ATAATATTTCTTTCCTTCTTTTCTTTGGAATACCATTTTCT
```

rs6983267: GRCh38 chr8:127401060, plus-strand alleles G/T, specified allele G.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
TGTAGCCAGAGTTAATACCCTCATCGTCCTTTGAGCTCAGCAGATGAAAGGCACTGAGAA
AAGTACAAAGAATTTTTATGTGCTATTGACTTTATTTTATT
```

## Question

Rank the following variants by their association OR for colorectal cancer, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs12979278(specified allele T)
B. rs4944940(specified allele G)
C. rs7894531(specified allele G)
D. rs6983267(specified allele G)
