---
bench_id: "DNA-NUM-30-005"
category: "Disease-Biology"
title: "5′UTR ribosome loading prediction"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

## Context

In HEK293T cells, the following 50 bp fragment serves as the variable 5′UTR of an EGFP reporter RNA. It is preceded by the fixed sequence GGGACATCGTAGAGAGTCGTACTTA and followed by the EGFP coding region. MRL denotes mean ribosome load measured by polysome fractionation. The reference and variant use the same reporter backbone.

Reference DNA (5′→3′, 50 bp; positions are 1-based):

```text
AGGGCGCCGGCCCACCCTTCCCTCCGCCGCCCCCCGGCCGCGGGGAGGAC
```

Variant: position 49 A→T.

## Question

What is the change in MRL for this variant relative to the reference sequence? Express it as log₂(MRL_variant/MRL_reference). Return one JSON object {"value": <number>} holding that single finite number.
Use the sequence and experimental conditions to provide your most likely numerical estimate. Even if uncertain, return a finite numerical value.
