---
bench_id: "DNA-RANK4-20-005"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with atrial fibrillation in a combined analysis of prevalent and incident cases in European-ancestry, Japanese, and African American populations. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs4743034: GRCh38 chr9:106870072, plus-strand alleles G/A, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
ATAAAATTTATCTTTTTTCTAAGTCCTCCTATTCTCATCAGCTGAAGCACGTACAGGATT
TTTAAAGTGTTTGGATGTGTGATTCCAACACAAAGTTAATT
```

rs608930: GRCh38 chr1:170648165, plus-strand alleles G/T, specified allele G.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GTTAAGAGTCCAAGCCTGGTCATCAGAGGGAACCAGATTCTAATCATGCCGGGGTGATCC
CCTGGGAAAACTACTTGTTTGATTTTCTTATCTGTAAAAGA
```

rs2129977: GRCh38 chr4:110791276, plus-strand alleles A/G, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
CATAACCAGCATGAGTGCAGGGGACACACATACCATTTGGTACAAGCCTTATTTGTCTTG
CCTTGGGTCTGGAACCACTTTTGCAGTAACACATTTAGAAA
```

rs11598047: GRCh38 chr10:103582915, plus-strand alleles A/G, specified allele G.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
AAGGCTTCAATAAACAAGGAGAGTCTGGAAGTGAAGAATGCGGCATTAGGAGTTGGACAG
ACCTTTTTTTCAATCCTGGATCTGCCACATGGCGGCTGTCA
```

## Question

Rank the following variants by their association OR for atrial fibrillation, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs4743034(specified allele A)
B. rs608930(specified allele G)
C. rs2129977(specified allele A)
D. rs11598047(specified allele G)
