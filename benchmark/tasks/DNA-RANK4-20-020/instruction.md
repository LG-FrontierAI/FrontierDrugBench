---
bench_id: "DNA-RANK4-20-020"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with lung cancer in a combined analysis of European- and African-ancestry populations. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs1056562: GRCh38 chr11:118254910, plus-strand alleles T/C, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
TAAAAGAAATACGTGAAAGGAAATGTAACAGACAAATTGGCTTTTATCCCTTTTGATACC
AATATATGTGTATACAAGTCATAACACTGTAAGTAGTGTCT
```

rs329122: GRCh38 chr5:134528909, plus-strand alleles G/A, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
TGTTTTCCCGTCCAAAATGCTTTTCCTTTCCCTAAATTGCCTGGCTAAAGGGCCAGTAAC
AGTGGTCCAAGAGGTTGTCAGAAATCTCCACTTAGCTTTCA
```

rs3131856: GRCh38 chr6:29639324, plus-strand alleles T/C, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GCCATAACAAAATCTCTTGCACCGGGTAACTTATGAACAACAGAAATGTATTTCTGACAG
TTCTGGAGGCCGGGAAATCCAAGATTAAGGCACTGGCAGAT
```

rs2036527: GRCh38 chr15:78559273, plus-strand alleles G/A, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GAAAGATTGTGTCTTGTGTGAGACAGCTGTGGAACTGGAAATTACCAAACGATTTCCAAT
TTTAAGAGATTTGGATCAGGTGGCTTAGAATTAGATTAAAG
```

## Question

Rank the following variants by their association OR for lung cancer, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs1056562(specified allele T)
B. rs329122(specified allele A)
C. rs3131856(specified allele T)
D. rs2036527(specified allele A)
