---
bench_id: "DNA-RANK4-20-007"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with chronic obstructive pulmonary disease in male UK Biobank participants. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs572473905: GRCh38 chr2:64060874, plus-strand alleles T/C, specified allele C.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
ACTCTCATCTCAAAAAAAAAAAAAAAAAAAAAAAAAGAAATATATATATATACACACACA
CACACACATACACACACACACACACACACGTATATATATAC
```

rs1903003: GRCh38 chr4:88965146, plus-strand alleles C/T, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
AGACTAAGGCAAGACCTTACCAAATATGATAAATGGTACAATTTGAGCAGCTGTAGCATT
CCTGTTACAGACAATGAGCATTAGGCCATTCCTCACCAAGT
```

rs7753012: GRCh38 chr6:142424746, plus-strand alleles T/G, specified allele G.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
AGGGAGGATTCCCTCTTTTTCTATTGATTGGAATAATTTTTTCTCTTTTTTATATTTGTC
ATTCCAGCAAAAATCATGATGTGGTCCCTCTGCCTCATGGA
```

rs2119568: GRCh38 chr15:71373485, plus-strand alleles T/C, specified allele C.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
ATTTTAGGGTCTAATACACAGGATATCCCGGTGGCTGAAACAAAGACATTTTGGAGGTGC
TTATGACTCAAATAGCAAATCATCATTGAAACACATTGACA
```

## Question

Rank the following variants by their association OR for chronic obstructive pulmonary disease, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs572473905(specified allele C)
B. rs1903003(specified allele T)
C. rs7753012(specified allele G)
D. rs2119568(specified allele C)
