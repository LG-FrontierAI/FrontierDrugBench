---
bench_id: "PROT-V4-QUANT-011"
category: "Disease-Biology"
title: "TIMP1 variant function prediction (A,B,C,D)"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "TIMP1",
  "experimental_system": "Human TIMP-1 N-terminal inhibitory domain and MMP1; determine the inhibition constant K_i using enzyme inhibition assays with a fluorescent substrate.",
  "sequence_region": "UniProt P01033, residues 24–149 in full-length protein numbering",
  "wild_type_sequence": "CTCVPPHPQTAFCNSDLVIRAKFVGTPEVNQTTLYQRYEIKMTKMYKGFQALGDAADIRFVYTPAMESVCGYFHRSHNRSEEFLIAGKLQDGLLHITTCSFVAPWNSLSLAQRRGFTKTYTVGCEE",
  "variants": {
    "A": "position 91 S→Y",
    "B": "position 25 T→R",
    "C": "position 27 V→A",
    "D": "position 91 S→A"
  }
}
```

## Question

Rank these TIMP-1 variants by MMP1 inhibitory potency, from strongest to weakest, equivalently from lowest to highest K_i. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"]; do not use ties.

## Options
