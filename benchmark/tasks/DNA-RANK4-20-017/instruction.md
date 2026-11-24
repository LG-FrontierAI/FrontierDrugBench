---
bench_id: "DNA-RANK4-20-017"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with age-related macular degeneration in a predominantly European-ancestry combined analysis that also includes Asian populations. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs10490924: GRCh38 chr10:122454932, plus-strand alleles G/T, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GTGACAAGCAGAGGAGCAAACTGTCTTTATCACACTCCATGATCCCAGCTGCTAAAATCC
ACACTGAGCTCTGCTTACCAGCCTTCTTCTCTCCTGCTGGA
```

rs10737680: GRCh38 chr1:196710325, plus-strand alleles A/C, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GTGCCCTTGTGTTGATTAAAGCCTTTCTTTGCTGCAAACCCTACTGTCTCAGCGTATTGG
TCTATTGCTAAACAGTGGGCATGTGAACCTGATAGTCTTAT
```

rs429608: GRCh38 chr6:31962685, plus-strand alleles G/A, specified allele G.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
CCGTTGTGGAGAGTGTGCTGTCTGAGGAGGGGGTGGAGACGAGCCACTGGGGAGTCAATC
CTTGGCCTCTTCTCCCCAGCTCCATGCTGTACAGTGGCTCA
```

rs8017304: GRCh38 chr14:68318360, plus-strand alleles G/A, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
CCCTTGAAACATTGGTTGCTAACCTTTGAAAGAGTAGTCACTGCACCTGAGTAGCCTTAG
GAAATGAATAGGAGGTCTGAGAAAAAGAAAAAAAAGAAGAG
```

## Question

Rank the following variants by their association OR for age-related macular degeneration, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs10490924(specified allele T)
B. rs10737680(specified allele A)
C. rs429608(specified allele G)
D. rs8017304(specified allele A)
