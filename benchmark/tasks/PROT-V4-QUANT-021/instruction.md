---
bench_id: "PROT-V4-QUANT-021"
category: "Disease-Biology"
title: "MYOC variant function prediction (A,B,C,D)"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "MYOC",
  "experimental_system": "The olfactomedin domain (OLF) of human myocilin, associated with glaucoma, assayed by thermal denaturation at pH 6.0; ΔT_m = T_m(variant) − T_m(WT).",
  "sequence_region": "UniProt Q99972, residues 244–504 in full-length protein numbering",
  "wild_type_sequence": "GCGELVWVGEPLTLRTAETITGKYGVWMRDPKPTYPYTQETTWRIDTVGTDVRQVFEYDLISQFMQGYPSKVHILPRPLESTGAVVYSGSLYFQGAESRTVIRYELNTETVKAEKEIPGAGYHGQFPYSWGGYTDIDLAVDEAGLWVIYSTDEAKGAIVLSKLNPENLELEQTWETNIRKQSVANAFIICGTLYTVSSYTSADATVNFAYDTGTGISKTLTIPFKNRYKYSSMIDYNPLEKKLFAWDNLNMVTYDIKLSKM",
  "variants": {
    "A": "position 273 D→A",
    "B": "position 385 E→A",
    "C": "position 427 A→T",
    "D": "position 423 K→E"
  }
}
```

## Question

Rank these OLF variants by the thermal denaturation midpoint T_m, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"]; do not use ties.

## Options
