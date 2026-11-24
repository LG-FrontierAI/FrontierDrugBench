---
bench_id: "PROT-V4-QUANT-020"
category: "Disease-Biology"
title: "UBE3A variant function prediction (position 668 Y→A)"
format: "structured_json"
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
  "variant": "position 668 Y→A"
}
```

## Question

Predict K_D of this UBE3A HECT variant for UbcH7 (μM). Return one JSON object {"value": <number>} holding that single finite number.
