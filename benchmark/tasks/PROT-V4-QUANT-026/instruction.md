---
bench_id: "PROT-V4-QUANT-026"
category: "Disease-Biology"
title: "AGXT variant function prediction (A,B,C,D)"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "AGXT",
  "experimental_system": "Purified human AGXT, associated with primary hyperoxaluria type I, at 25°C in 0.1 M sodium phosphate, pH 8.0, with 150 μM PLP. Fit two-substrate kinetics using L-alanine and glyoxylate. WT is the major allele; each candidate lists all amino acid substitutions relative to WT.",
  "sequence_region": "UniProt P21549, residues 1–392 in full-length protein numbering",
  "wild_type_sequence": "MASHKLLVTPPKALLKPLSIPNQLLLGPGPSNLPPRIMAAGGLQMIGSMSKDMYQIMDEIKEGIQYVFQTRNPLTLVISGSGHCALEAALVNVLEPGDSFLVGANGIWGQRAVDIGERIGARVHPMTKDPGGHYTLQEVEEGLAQHKPVLLFLTHGESSTGVLQPLDGFGELCHRYKCLLLVDSVASLGGTPLYMDRQGIDILYSGSQKALNAPPGTSLISFSDKAKKKMYSRKTKPFSFYLDIKWLANFWGCDDQPRMYHHTIPVISLYSLRESLALIAEQGLENSWRQHREAAAYLHGRLQALGLQLFVKDPALRLPTVTTVAVPAGYDWRDIVSYVIDHFDIEIMGGLGPSTGKVLRIGLLGCNATRENVDRVTEALRAALQHCPKKKL",
  "variants": {
    "A": "position 11 P→L + position 340 I→M + position 83 H→R",
    "B": "position 340 I→M",
    "C": "position 11 P→L",
    "D": "position 11 P→L + position 340 I→M + position 319 P→L"
  }
}
```

## Question

At saturating substrate concentrations, rank the constructs by maximum reaction rate per unit protein mass, V_max, from highest to lowest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"]; do not use ties.

## Options
