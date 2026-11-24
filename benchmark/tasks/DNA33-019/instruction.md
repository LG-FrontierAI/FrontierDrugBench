---
bench_id: "DNA33-019"
category: "Disease-Biology"
title: "Tissue-specific expression effect prediction"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Context

Expression associations for gene ENSG00000013573.17 are studied in human sigmoid colon. The following are independent single-nucleotide variants at different loci. All coordinates are 1-based on the GRCh38 plus strand. Brackets indicate the reference/alternate bases.

X: chr12:31059482 alleles T/G
TTCACAGCCTCCCTCGAGTTTTTGGCTTCCTGAATGTAGCTAACTTTCCC[T/G]TTCACCAACATTTGTCTCTAGACTTTTGGCTTTCAAGCAACAAGTGGCCT

Y: chr12:31073901 alleles T/A
GCGGCGGGGGTTGTTCCGGCTGCCTTTCACTGAGGGGACCCGCCAGTTTC[T/A]AACTCAGTGGCGTTTGCCCTGATTCCCGGGGCCTGGCTTTCAGCGTAGCA

Z: chr12:31119661 alleles G/A
CCCCCCCGGCTCTTAGGACACCCAACGCAGAGGGGGGAGGCACCCCCTGC[G/A]AGGCAGGAACTGAGAGCCAGACCCACTTCTCCCCGGCTCTTGGGATCCCC

W: chr12:31223754 alleles A/G
TTAACTCCTCCCCTTGATGCCACTAAAGCAGGAATCACACTGCAGATGGC[A/G]CTGATTTGATTGGCAAGAGACATGCCAGGAAGAATATTAAGGGACCAGGC

## Question

Which variant has the largest absolute expression association effect? Output only the letter(s) corresponding to your answer.

## Options

A. X
B. Y
C. Z
D. W
