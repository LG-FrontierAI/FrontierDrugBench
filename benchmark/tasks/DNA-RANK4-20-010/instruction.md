---
bench_id: "DNA-RANK4-20-010"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with rheumatoid arthritis in individuals of European ancestry. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs1696466: GRCh38 chr12:57722614, plus-strand alleles T/C, specified allele C.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GCCCATAATCCCAGCTACACGGGAGGCTGAGCAGGAGAATCGCTTGAACCTGGGAGGCGG
AGGTTGTGGTGAGCTGAGATCACACCACTGCACTCCAACCT
```

rs1953126: GRCh38 chr9:120878222, plus-strand alleles T/C, specified allele C.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GTGCACAGAAATACATGGTACAATCGCAAATATATACCACACGCACAACATGTCATGTAA
ATAAAGGGCACACAATGAAAGACAACATGCACAGAGTCATA
```

rs8026898: GRCh38 chr15:69699078, plus-strand alleles G/A, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
TGATGAAATTTGTCTTTCAGAACCGCTTCTGGAGTCTTCCTCCCAAGAGCGAGGCACTGG
TGCTGCTCTGTCAAACTGTTCAAGTGCCTTCATGTAACTGC
```

rs16903108: GRCh38 chr8:128564231, plus-strand alleles T/C, specified allele C.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GATTTTACTGTGATTTGTTTTCTAGAATTAATCTCATCATGAACTTACTGTGCTCTGTGA
TGGCCAATGTAGTAGCATCGTGGAAAAATGGCCCTGTGTAG
```

## Question

Rank the following variants by their association OR for rheumatoid arthritis, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs1696466(specified allele C)
B. rs1953126(specified allele C)
C. rs8026898(specified allele A)
D. rs16903108(specified allele C)
