---
bench_id: "PROT-V4-QUANT-027"
category: "Disease-Biology"
title: "AGXT variant function prediction (position 11 P→L + position 340 I→M + pos)"
format: "structured_json"
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
  "variant": "position 11 P→L + position 340 I→M + position 197 R→Q"
}
```

## Question

Predict the Michaelis constant K_m of this AGXT construct for L-alanine (mM). Return one JSON object {"value": <number>} holding that single finite number.
