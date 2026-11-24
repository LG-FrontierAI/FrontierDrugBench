---
bench_id: "PROT-V4-QUANT-005"
category: "Disease-Biology"
title: "IFNA2 variant function prediction (A,B,C,D)"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "IFNA2",
  "experimental_system": "Surface-sensor binding assays of human IFN-α2 and the IFNAR2 extracellular domain, using a WT IFN-α2 background.",
  "sequence_region": "UniProt P01563, residues 24–188 in full-length protein numbering",
  "wild_type_sequence": "CDLPQTHSLGSRRTLMLLAQMRRISLFSCLKDRHDFGFPQEEFGNQFQKAETIPVLHEMIQQIFNLFSTKDSSAAWDETLLDKFYTELYQQLNDLEACVIQGVGVTETPLMKEDSILAVRKYFQRITLYLKEKKYSPCAWEVVRAEIMRSFSLSTNLQESLRSKE",
  "variants": {
    "A": "position 48 S→A",
    "B": "position 176 L→A",
    "C": "position 50 F→A",
    "D": "position 168 A→G"
  }
}
```

## Question

Rank the IFN-α2–IFNAR2 complexes by dissociation rate, from fastest to slowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"]; do not use ties.

## Options
