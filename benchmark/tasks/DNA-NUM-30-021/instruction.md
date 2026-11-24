---
bench_id: "DNA-NUM-30-021"
category: "Disease-Biology"
title: "Relative RNA retention prediction"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

## Context

In SH-SY5Y cells, the following DNA fragment corresponds to the test region in the 3′UTR of an EGFP reporter RNA. The reference and variant share all other sequences. The abundance of both RNAs is measured 20 and 60 minutes after reporter RNA delivery. The log₂ change is calculated for each replicate and then averaged across three replicates.

Reference DNA (5′→3′, 136 bp; positions are 1-based):

```text
AAATGTTATAAATGTCATCATAAAAATCATTAGAAAACTCATTTCTCCTTATGTTGTCGT
TGTACCATTGGGTATTGTATAGAGACCAATTTCTAAGAGATTTTTTCACCTCTGTTGCGG
CCGCGCAATAACTAGC
```

Variant: position 59 G→A.

## Question

From 20 to 60 minutes, what is the change in RNA retention for the variant relative to the reference? Express it as log₂[(variant/reference)_60min/(variant/reference)_20min]. Return one JSON object {"value": <number>} holding that single finite number.
Use the sequence and experimental conditions to provide your most likely numerical estimate. Even if uncertain, return a finite numerical value.
