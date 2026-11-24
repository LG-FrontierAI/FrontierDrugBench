---
bench_id: "DNA-NUM-30-030"
category: "Disease-Biology"
title: "Endogenous variant function prediction"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

## Context

In a BRCA1 saturation genome editing assay in haploid HAP1-Lig4KO cells, consider NM_007294.3:c.5428G>C; genomic position: GRCh37/hg19 chr17:41199699, C→G; BRCA1 is on the minus strand. Variants share the editing background used for their respective exon. The sequence below is the genomic plus strand, 5′→3′.

Reference DNA (5′→3′, 201 bp; positions are 1-based):

```text
GTGATAAACCAAACCCATGCAAAAGGACCCCATATAGCACAGGTACATGCAGGCACCTTA
CCATGGAAGCCATTGTCCTCTGTCCAGGCATCTGGCTGCACAACCACAATTGGGTGGACA
CCCTGGATCCCCAGGAAGGAAAGAGCATTCAAAGTGTCAAAGTAGGACTACTGGAACTGT
CACTTCATCATTTTTTTTGTT
```

Variant: position 101 C→G.

The functional readout is variant log₂ enrichment on day 11 relative to the initial library. Two replicates are combined after correcting for editing-position bias and differences between exons. The scores are then linearly calibrated so that the median synonymous-control score is 0 and the median nonsense-control score is −1.

## Question

What is the calibrated functional score of this variant? Return one JSON object {"value": <number>} holding that single finite number.
Use the sequence and experimental conditions to provide your most likely numerical estimate. Even if uncertain, return a finite numerical value.
