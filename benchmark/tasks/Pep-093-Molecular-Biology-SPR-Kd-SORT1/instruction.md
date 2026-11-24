---
bench_id: Pep-093-Molecular-Biology-SPR-Kd-SORT1
category: "Molecular-Biology"
format: ranking
---
# Prompt

Target: **Sortilin/SORT1**  
Assay: **Biacore 8K SPR; steady-state affinity model**  
Property to rank: **Sortilin SPR KD**

Rank the listed candidates from lower to higher measured Sortilin SPR KD. Use only the candidate identifiers and assay context. The measured values are withheld from the model and used only by the evaluator.

{
  "target": "Sortilin/SORT1",
  "assay": "Biacore 8K SPR; steady-state affinity model",
  "endpoint": "Sortilin SPR KD",
  "direction_to_rank": "lower to higher",
  "context": {
    "target": "Sortilin/SORT1",
    "system": "purified protein SPR",
    "unit": "nM"
  },
  "candidates": [
    {
      "id": "SEQ ID NO.92",
      "value_unit": "nM",
      "sequence": "Ac-PYRIKGAVRQMYKPYIL-COOH"
    },
    {
      "id": "SEQ ID NO.223",
      "value_unit": "nM",
      "sequence": "Ac-CTKSKRYICIL-COOH"
    },
    {
      "id": "SEQ ID NO.228",
      "value_unit": "nM",
      "sequence": "Ac-CTRKKRYICIL-COOH"
    },
    {
      "id": "SEQ ID NO.229",
      "value_unit": "nM",
      "sequence": "Ac-CTWKKRYICIL-COOH"
    },
    {
      "id": "SEQ ID NO.230",
      "value_unit": "nM",
      "sequence": "Ac-CTRKAKRYICIL-COOH"
    },
    {
      "id": "SEQ ID NO.231",
      "value_unit": "nM",
      "sequence": "Ac-CTRKPKPRYICIL-COOH"
    },
    {
      "id": "SEQ ID NO.232",
      "value_unit": "nM",
      "sequence": "Ac-CKSKPPCYIL-COOH"
    }
  ]
}

Return one JSON array of candidate IDs in the requested order. Do not include explanations. For equal values, sort IDs ascending.
