---
bench_id: "DNA-RANK4-20-008"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with Crohn's disease in individuals of European ancestry. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs2076756: GRCh38 chr16:50722970, plus-strand alleles A/G, specified allele G.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
ATCTGTAAATTGAAGATATTGGGCTGGATCAGGTACATTTTATCTTAAGGACCAATTCCA
ATCCATTGGTAGTGGGTGCCCAGTGCACCACATTAAAAAGA
```

rs7927997: GRCh38 chr11:76590331, plus-strand alleles C/T, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GATGTGTATGAAGTCACAAAATCCTCAGAAATCTGGGGTCAAGGGTCAAACACATCACCT
CCCCCCCACTGCCTTACCATGAGGAAACTGAGGCTCAGAGA
```

rs11742570: GRCh38 chr5:40410482, plus-strand alleles T/C, specified allele C.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
AAGTGTACTCCCTATCACCAGGGTAGCAGCCGTGACCTACATTTTCTTCATGTTCTGATG
CTGTTTGTGGCTTCCTCTTCCCTTCAGGCAGCGCATGATGT
```

rs13428812: GRCh38 chr2:25269598, plus-strand alleles A/G, specified allele G.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
TAGTGAAAGTGGGGTGGGCTGATTGTGGAGGTCGAAGGGTTGAAGACTTGAGAAATAGCC
AGAGGGTATCTGACATGATGGGGGAGACAATGGGGAGCCAT
```

## Question

Rank the following variants by their association OR for Crohn's disease, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs2076756(specified allele G)
B. rs7927997(specified allele T)
C. rs11742570(specified allele C)
D. rs13428812(specified allele G)
