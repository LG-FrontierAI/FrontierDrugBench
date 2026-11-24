---
bench_id: "PROT-V4-QUANT-001"
category: "Disease-Biology"
title: "IL4 variant function prediction (A,B,C,D)"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "IL4",
  "experimental_system": "Binding of allergy- and inflammation-associated IL-4 to the IL-4Rα extracellular domain, measured at 298 K by surface plasmon resonance.",
  "sequence_region": "UniProt P05112, residues 25–153 in full-length protein numbering",
  "wild_type_sequence": "HKCDITLQEIIKTLNSLTEQKTLCTELTVTDIFAASKNTTEKETFCRAATVLRQFYSHHEKDTRCLGATAQQFHRHKQLIRFLKRLDRNLWGLAGLNSCPVKEANQSTLENFLERLKTIMREKYSKCSS",
  "variants": {
    "A": "position 106 F→D",
    "B": "position 77 R→Q",
    "C": "position 112 R→Q",
    "D": "position 112 R→A"
  }
}
```

## Question

After complex formation, rank these IL-4 variants by dissociation rate k_off, from fastest to slowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"]; do not use ties.

## Options
