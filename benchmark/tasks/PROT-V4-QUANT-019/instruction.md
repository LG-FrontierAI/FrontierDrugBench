---
bench_id: "PROT-V4-QUANT-019"
category: "Disease-Biology"
title: "UBE3A variant function prediction (A,B,C,D)"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "UBE3A",
  "experimental_system": "Binding of the HECT domain of the Angelman syndrome-associated human E3 ubiquitin ligase UBE3A to human UbcH7 (UBE2L3), quantified by fluorescence polarization.",
  "sequence_region": "UniProt Q05086, residues 518–875 in full-length protein numbering",
  "wild_type_sequence": "QLNPYLRLKVRRDHIIDDALVRLEMIAMENPADLKKQLYVEFEGEQGVDEGGVSKEFFQLVVEEIFNPDIGMFTYDESTKLFWFNPSSFETEGQFTLIGIVLGLAIYNNCILDVHFPMVVYRKLMGKKGTFRDLGDSHPVLYQSLKDLLEYEGNVEDDMMITFQISQTDLFGNPMMYDLKENGDKIPITNENRKEFVNLYSDYILNKSVEKQFKAFRRGFHMVTNESPLKYLFRPEEIELLICGSRNLDFQALEETTEYDGGYTRDSVLIREFWEIVHSFTDEQKRLFLQFTTGTDRAPVGGLGKLKMIIAKNGPDTERLPTSHTCFNVLLLPEYSSKEKLKERLLKAITYAKGFGML",
  "variants": {
    "A": "position 675 D→R",
    "B": "position 665 L→A",
    "C": "position 657 V→A",
    "D": "position 693 M→A"
  }
}
```

## Question

Rank these UBE3A variants by affinity for the E2 enzyme UbcH7, from strongest to weakest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"]; do not use ties.

## Options
