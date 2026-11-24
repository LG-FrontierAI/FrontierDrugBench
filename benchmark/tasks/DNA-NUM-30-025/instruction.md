---
bench_id: "DNA-NUM-30-025"
category: "Disease-Biology"
title: "Endogenous RNA expression prediction"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

## Context

In a BRCA1 saturation genome editing assay in haploid HAP1-Lig4KO cells, consider NM_007294.3:c.5112T>G; genomic position: GRCh37/hg19 chr17:41215931, A→C; BRCA1 is on the minus strand. Variants share the editing background used for their respective exon. The sequence below is the genomic plus strand, 5′→3′.

Reference DNA (5′→3′, 201 bp; positions are 1-based):

```text
GTGTAAAAATGCAATTCTGAGGTGTTAAAGGGAGGAGGGGAGAAATAGTATTATACTTAC
AGAAATAGCTAACTACCCATTTTCCTCCCGCAATTCCTAGAAAATATTTCAGTGTCCGTT
CACACACAAACTCAGCATCTGCAGAATGAAAAACACTCAAAGGATTAGAAGTTGAAAACA
AAATCAGGAAGTGCTGTCCTA
```

Variant: position 101 A→C.

On day 5, measure the ratio of the variant frequencies in cDNA and gDNA, average the ratios across two replicates, normalize by the median ratio of synonymous controls in the same exon, and take log₂ to obtain the RNA expression score.

## Question

What is the RNA expression score of this variant? Return one JSON object {"value": <number>} holding that single finite number.
Use the sequence and experimental conditions to provide your most likely numerical estimate. Even if uncertain, return a finite numerical value.
