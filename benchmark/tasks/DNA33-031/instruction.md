---
bench_id: "DNA33-031"
category: "Disease-Biology"
title: "Clinical pathogenicity five-class prediction"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Context

Disease: GCK-related monogenic diabetes. Inheritance: autosomal dominant.
Variant status: germline heterozygous.
Variant: NM_000162.5(GCK):c.566T>C (p.Ile189Thr).
Genomic position: GRCh38, chr7:44149982, A→G; the gene is on the minus strand.

Additional evidence:
- Population data: this variant was not observed in the gnomAD snapshot used.
- Computational predictions: REVEL is 0.969.
- Clinical observations: laboratory-contributed records describe 7 unrelated cases.
- Family data: segregation evidence spans 5 meioses in two families.
- Phenotype records: one carrier had fasting glucose of 125 mg/dL and HbA1c of 6.5%.

Reference DNA (genomic plus strand, 5′→3′, 201 bp; brackets enclose the reference base at position 101):

```text
CAGTGCTGGAAGCCAAGGAGAAAGGCAGGCAGTGCTGGGGTGGGTGGCCC
AGGGCAGCCCCCCCGGCAGGTACAGGTGCCCCCTCACCCCTCTCCGTTTG[A]TAGCGTCTCGCAGAAGCCCCACGACATTGTTCCCTTCTGCTCCTGAGGCC
TTGAAGCCCTTGGTCCAGTTGAGAAGGATGCCCTGTGGGGAGAGATAGGC
```

## Question

Which clinical pathogenicity category is most likely for this variant in the disease context above? Output only the letter(s) corresponding to your answer.

## Options

A. Pathogenic
B. Likely pathogenic
C. VUS (variant of uncertain significance)
D. Likely benign
E. Benign
