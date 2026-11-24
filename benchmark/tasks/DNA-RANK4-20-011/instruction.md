---
bench_id: "DNA-RANK4-20-011"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with systemic lupus erythematosus in individuals of European ancestry. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs10036748: GRCh38 chr5:151078585, plus-strand alleles C/T, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
ATAAGATTCTTTCATAGCATGATACACGTATGAGAAAAATAAAATAGTAACGTGACAGAA
AGTGAAAAAAGGGGCTGCTTTGCATAAAAAGATCAGGGAAG
```

rs1059312: GRCh38 chr12:128794319, plus-strand alleles A/G, specified allele G.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GAAATAATGAGGAAAAGCAGGAGGGTAGCTCCTTGAATAGCAGCCAGAAGAAAAAAGTAA
TAGTTCAAATAGCAGCCGTTAATATTACCTGGAGAAAACAA
```

rs17849501: GRCh38 chr1:183573188, plus-strand alleles C/T, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GGCCCGGGCCACAGGAGACTCAGGGGAAGCTGAGCAATCCCACCTACCGTCGCCTTGCCT
AGGTAATCCTTCTTGGCCAGCTGAGCCACTTGTCTCTCATT
```

rs34572943: GRCh38 chr16:31261032, plus-strand alleles G/A, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
TTCTGTCTTGTTATATAAGTACTTGTACAACATATTCTATCAGCCTCTTGGTCTGCAAAA
CCTAAAATTTACTATCTGGCTGTTTACAGAATAAGTGTGCT
```

## Question

Rank the following variants by their association OR for systemic lupus erythematosus, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs10036748(specified allele T)
B. rs1059312(specified allele G)
C. rs17849501(specified allele T)
D. rs34572943(specified allele A)
