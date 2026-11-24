---
bench_id: "PROT-V4-QUANT-013"
category: "Disease-Biology"
title: "RNH1 variant function prediction (A,B,C,D)"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "RNH1",
  "experimental_system": "Formation of an inhibitory complex between human ribonuclease inhibitor RNH1 and angiogenin ANG, measured at 298 K by solution fluorescence binding kinetics.",
  "sequence_region": "UniProt P13489, residues 2–461 in full-length protein numbering",
  "wild_type_sequence": "SLDIQSLDIQCEELSDARWAELLPLLQQCQVVRLDDCGLTEARCKDISSALRVNPALAELNLRSNELGDVGVHCVLQGLQTPSCKIQKLSLQNCCLTGAGCGVLSSTLRTLPTLQELHLSDNLLGDAGLQLLCEGLLDPQCRLEKLQLEYCSLSAASCEPLASVLRAKPDFKELTVSNNDINEAGVRVLCQGLKDSPCQLEALKLESCGVTSDNCRDLCGIVASKASLRELALGSNKLGDVGMAELCPGLLHPSSRLRTLWIWECGITAKGCGDLCRVLRAKESLKELSLAGNELGDEGARLLCETLLEPGCQLESLWVKSCSFTAACCSHFSSVLAQNRFLLELQISNNRLEDAGVRELCQGLGQPGSVLRVLWLADCDVSDSSCSSLAATLLANHSLRELDLSNNCLGDAGILQLVESVRQPGCLLEQLVLYDIYWSEEMEDRLQALEKDKPSLRVIS",
  "variants": {
    "A": "position 262 W→A",
    "B": "position 458 R→A",
    "C": "position 319 W→A",
    "D": "position 376 W→A"
  }
}
```

## Question

After ANG has bound RNH1, rank the complexes by dissociation rate, from slowest to fastest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"]; do not use ties.

## Options
