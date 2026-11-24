---
bench_id: "DNA-RANK4-20-009"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with ulcerative colitis in individuals of European ancestry. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs6017342: GRCh38 chr20:44436388, plus-strand alleles A/C, specified allele C.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GGAGGAGAGAGGAAGGGACTTGCCCAAGGTCCACACACAGCTGGTCACCAATCCATACCT
GGTGTGGCCGCTGATCTGATGCTCATTGTCTGACTCCAGGG
```

rs6927022: GRCh38 chr6:32644620, plus-strand alleles A/G, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
AAAACATTGTGGTTATATTTATAATTAATTTATTTAAAAGAATGGATCATATTATATGAA
AAGCACTTTTGTTTTTCTCAGCCTCTTAATGATTTAGGAGA
```

rs4380874: GRCh38 chr7:107839870, plus-strand alleles T/C, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
ATTCATCCGGCACATATTTAGTGATCTCCTACTGTGTGCCAGGCACTGTTTTAGGCCCTA
GAGATATAATAGTAAATAAAAGAGTTTAAAAAACCATCTTT
```

rs254560: GRCh38 chr5:135107916, plus-strand alleles G/A, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
CCTACTGGAAGCTGGTTAAGGGCCAGGCTCACAACTTGAACCCAGGACAGGACTGTTTCA
TTTCCTGCAGAAGATCAAGGCCTCTCTGGCCACCCTTGAGG
```

## Question

Rank the following variants by their association OR for ulcerative colitis, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs6017342(specified allele C)
B. rs6927022(specified allele A)
C. rs4380874(specified allele T)
D. rs254560(specified allele A)
