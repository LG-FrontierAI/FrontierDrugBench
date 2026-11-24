---
bench_id: "DNA-RANK4-20-012"
category: "Disease-Biology"
title: "GWAS association effect ranking"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

Compare the genetic associations of the following four variants with psoriasis in individuals of European ancestry. Use the disease odds ratio (OR) per additional copy of the specified allele; the other allele at each site is the comparator.

rs61839660: GRCh38 chr10:6052734, plus-strand alleles C/T, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
GTTTTTTTATTGCTGAGAGTACAGAAAGCAGCGGCTTCTGAAGGAGGTATCTATTTTGGT
CCCAAACAGAAAAGAGTGGGTGATTCTGTGGGCAGAGGTGG
```

rs4728141: GRCh38 chr7:128926978, plus-strand alleles T/C, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
ATTTATTTTTATTTTATTGTTATTTTTTGGAGATAAGATGTCTTTCTTTGTTGTCCAGGC
TGGAGTGCTGTGGTTCATCACGTTAGCCGTAACCTTGAACT
```

rs79611018: GRCh38 chr12:94150744, plus-strand alleles G/A, specified allele A.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
CGCTGTGGTCGCCAGCCGCCGGGAGAGGCTGGGCGGGAGGTGGCCTTGTGGTAAAAGCCT
CATCCTAGAGGGGAGTGCAAGGGAAAGTGTTGGGGGTGCTA
```

rs2212434: GRCh38 chr11:76570549, plus-strand alleles C/T, specified allele T.
Reference DNA (plus strand, 5′→3′, 101 bp; the site is at position 51):
```text
CATCAGCTCCTTCCTGAGTTTCCAGCCTGTTGGCCTGCCCTACAAATTTCCGACTTGCCA
GCCCCTACAGTCATGTGAGCCAATTCCTTTCAATCTCTTCC
```

## Question

Rank the following variants by their association OR for psoriasis, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options

A. rs61839660(specified allele T)
B. rs4728141(specified allele T)
C. rs79611018(specified allele A)
D. rs2212434(specified allele T)
