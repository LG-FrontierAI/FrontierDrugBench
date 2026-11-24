---
bench_id: "DNA-NUM-30-015"
category: "Disease-Biology"
title: "Poly (A) site usage prediction"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

## Context

In a dual-poly(A) reporter assay in HEK293T cells, the following 164 bp fragment contains the test proximal site. The reference and variant use the same reporter backbone. Proximal and distal RNA products are measured after 36–48 hours, pooling barcode counts separately for each product.

Reference DNA (5′→3′, 164 bp; positions are 1-based):

```text
ATATACTTTGGAATGTTTCCCAAAATTAAAGTTGTACTGTTGTGATAAATAGTAAAGTTG
ACATGTCTATGACTACAGCCAACTTGTCGATTTTCCCTATGTGTAGATAGTATACTTTTA
AGTGTACTGATTCTAAATACATGTACTTGGTAAGGTGTGGGTGA
```

Variant: position 83 C→G.

Fixed linker and distal poly(A) region following the fragment (5′→3′):

```text
GGAGCAGATACTGGCTTAACTATGCGCCTCGACTGTGCCTTCTAGTTGCCAGCCATCTGT
TGTTTGCCCCTCCCCCGTGCCTTCCTTGACCCTGGAAGGTGCCACTCCCACTGTCCTTTC
CTAATAAAATGAGGAAATTGCA
```

## Question

How much does this variant change the proximal/distal RNA product ratio? Express it as ln[(proximal/distal)_variant/(proximal/distal)_reference], where ln is the natural logarithm. Return one JSON object {"value": <number>} holding that single finite number.
Use the sequence and experimental conditions to provide your most likely numerical estimate. Even if uncertain, return a finite numerical value.
