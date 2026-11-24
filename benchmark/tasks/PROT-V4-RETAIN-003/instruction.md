---
bench_id: "PROT-V4-RETAIN-003"
category: "Disease-Biology"
title: "TP53 variant function prediction (A,B,C,D)"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "TP53",
  "wild_type_sequence": "MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPRVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD",
  "experimental_setting": "Nutlin-3 screening in p53-null A549 cells; the score is defined as the negative of the original screening Z-score in this background. The original Z-score describes allele enrichment during selection; after sign reversal, a higher score indicates stronger growth suppression under Nutlin-3.",
  "variants": {
    "A": "position 36 P→S",
    "B": "position 136 Q→W",
    "C": "position 21 D→R",
    "D": "position 98 P→T"
  }
}
```

## Question

In the p53-null Nutlin-3 experiment, rank the four substitutions by the defined negative Z-score, from lowest to highest. Return one JSON array containing the four letters in ranked order, e.g. ["A", "B", "C", "D"].

## Options
