---
bench_id: "DNA33-030"
category: "Disease-Biology"
title: "Clinical pathogenicity five-class prediction"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Context

Disease: BRCA1-related hereditary cancer predisposition. Inheritance: autosomal dominant.
Variant status: germline heterozygous.
Variant: NM_007294.4(BRCA1):c.121C>A (p.His41Asn).
Genomic position: GRCh38, chr17:43115739, G→T; the gene is on the minus strand.

Additional evidence:
- Population data: this variant was not observed in gnomAD v2.1 exomes or the v3.1 non-cancer subset; sequencing depth at the site was at least 25.
- Computational predictions: BayesDel (noAF) is 0.32, and SpliceAI is 0.02.
- Protein location: this missense variant lies in a critical functional domain of BRCA1.
- Functional studies: two calibrated studies observed impaired protein function comparable to pathogenic control variants.

Reference DNA (genomic plus strand, 5′→3′, 201 bp; brackets enclose the reference base at position 101):

```text
AAGCTTCTATAAAGTTAGGTGTTTCCTGGGTTATGAAGGACAAAAACAAA
AGCTAATAATGGAGCCACATAACACATTCAAACTTACTTGCAAAATATGT[G]GTCACACTTTGTGGAGACAGGTTCCTTGATCAACTCCAGACTAGCAGGGT
AGGGGGGGAGAAAAAGAAAATAAATGAGGCTCAATAATTTATTTAAAAAT
```

## Question

Which clinical pathogenicity category is most likely for this variant in the disease context above? Output only the letter(s) corresponding to your answer.

## Options

A. Pathogenic
B. Likely pathogenic
C. VUS (variant of uncertain significance)
D. Likely benign
E. Benign
