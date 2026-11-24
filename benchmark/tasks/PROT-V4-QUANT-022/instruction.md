---
bench_id: "PROT-V4-QUANT-022"
category: "Disease-Biology"
title: "MYOC variant function prediction (position 364 G→V)"
format: "structured_json"
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
  "variant": "position 364 G→V"
}
```

## Question

Predict ΔT_m of this OLF variant relative to WT (°C; a decrease is negative). Return one JSON object {"value": <number>} holding that single finite number.
