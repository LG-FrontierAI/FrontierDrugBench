---
bench_id: "DNA-RANK4-20-013"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with breast cancer in a combined analysis of European- and East Asian-ancestry populations. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs75915166: GRCh38 chr11:69564393, plus-strand alleles C/A, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
AAAGACCTTTGCAGTGAAGTGAAGGCTCTTAAGAGATGAGATCATCCAGGCTTAACAGGG
TGGGCCCTAAATCCCCCGACAAGTGTCCTAGGAAGAGGAAA
```

rs4808801: GRCh38 chr19:18460331, plus-strand alleles A/G, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
ACAGCTGCTTGGGGGGAAGCAGCTGCATAATGAATATAGAAGCAAGAAGCAGACGAGCTG
TCCAGGGGAAGTCACAGTGGCACAGGAAGGGACAATCTGCC
```

rs11814448: GRCh38 chr10:22026914, plus-strand alleles A/C, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
TAAAATGTTCTGTTGAGCCCCAGAAGCTAATTTTCTTTTCAGTTATTATGATTTTCAGCT
TTAGAATTTATTTTTTTAATATAATTTCTACCTCTTTTTTA
```

rs10760444: GRCh38 chr9:126634155, plus-strand alleles G/A, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
CTGCTCCAGGCAGGACTGGAATAACGCCAGGACTCCAAATGAGCAAGATAGTCCCAGCCT
GGCCTGCCTGGGATAAGGAGCGGGCAGGGAAACCCAGAGGA
```

## Question

Rank the following variants by their association OR for breast cancer, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs75915166(specified allele A)
B. rs4808801(specified allele A)
C. rs11814448(specified allele A)
D. rs10760444(specified allele A)
