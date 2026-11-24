---
bench_id: LNP-076-In-vivo-Study-single-spleen-marrow-selectivity
category: "In-vivo-Study"
title: "Six formulations with a fixed ionizable lipid: spleen/liver and bone-marrow/liver selectivity"
format: structured_json
---

# Prompt

Predict the spleen/liver and bone-marrow/liver expression ratios of the six formulations from high to low and output order_spleen_liver and order_bm_liver. The two organ targets are not interchangeable; a high ratio does not mean high absolute expression in the target organ or low hepatotoxicity. Output JSON with a non-empty reason. The permutation covers every ID declared for that field; only source-supported pairwise orders are scored and unknown relationships are not scored.

## Input

The structured model input is below (JSON).

```json
{
  "candidates": [
    {
      "id": "F03",
      "components": "Ionizable/DSPC/triolein/cholesterol/PEG2000-DMG",
      "molar_percent": [
        29.62,
        19.62,
        29.26,
        19.62,
        1.5
      ],
      "ionizable_lipid": "Identical lipid1 in every candidate; analogue of US12121591 lipid24 with C8 rather than C7 chains distal to esters"
    },
    {
      "id": "F04",
      "components": "Ionizable/DSPC/triolein/cholesterol",
      "molar_percent": [
        30,
        20,
        30,
        20
      ],
      "ionizable_lipid": "Identical lipid1 in every candidate; analogue of US12121591 lipid24 with C8 rather than C7 chains distal to esters"
    },
    {
      "id": "F07",
      "components": "Ionizable/DSPC/triolein/cholesterol",
      "molar_percent": [
        30,
        30,
        20,
        20
      ],
      "ionizable_lipid": "Identical lipid1 in every candidate; analogue of US12121591 lipid24 with C8 rather than C7 chains distal to esters"
    },
    {
      "id": "F08",
      "components": "Ionizable/DSPC/triolein/cholesterol",
      "molar_percent": [
        30,
        25,
        25,
        20
      ],
      "ionizable_lipid": "Identical lipid1 in every candidate; analogue of US12121591 lipid24 with C8 rather than C7 chains distal to esters"
    },
    {
      "id": "F09",
      "components": "Ionizable/DSPC/triolein/cholesterol",
      "molar_percent": [
        25,
        25,
        25,
        25
      ],
      "ionizable_lipid": "Identical lipid1 in every candidate; analogue of US12121591 lipid24 with C8 rather than C7 chains distal to esters"
    },
    {
      "id": "F10",
      "components": "Ionizable/DSPC/triolein/cholesterol",
      "molar_percent": [
        35,
        25,
        15,
        25
      ],
      "ionizable_lipid": "Identical lipid1 in every candidate; analogue of US12121591 lipid24 with C8 rather than C7 chains distal to esters"
    }
  ],
  "conditions": {
    "context_key": "Table6:lipid1:CD1:1mgkg:24h",
    "endpoint": "Spleen/liver and bone-marrow/liver luciferase-expression ratios",
    "animal": "CD-1 mice; sex/age/n not reported in checked cohort text",
    "cargo": "Luciferase mRNA",
    "dose": "1mg/kg RNA",
    "route": "IV per tissue-homogenate method p52",
    "harvest": "24h",
    "preparation": "MRNA in 25 mM sodium acetate pH 4.0, lipids in ethanol; ethanol:aqueous 1:3, T-junction 20 mL/min total (5+15), overnight dialysis against >=~100 volumes PBS pH 7.4. Modified method adds buffer after mixing before dialysis. Exact method variant must be matched per formulation; not all entries resolve it.",
    "NP": "Not resolved for this cohort; do not assume constant numerical N/P",
    "ingredient_scope": "Lipid1 is constant across all six candidates. This task predicts formulation-fraction effects only, not generalization across ionizable structures."
  },
  "submission_fields": [
    {
      "type": "Ranking_constraints",
      "key": "Order_spleen_liver",
      "candidate_ids": [
        "F03",
        "F04",
        "F07",
        "F08",
        "F09",
        "F10"
      ]
    },
    {
      "type": "Ranking_constraints",
      "key": "Order_bm_liver",
      "candidate_ids": [
        "F03",
        "F04",
        "F07",
        "F08",
        "F09",
        "F10"
      ]
    }
  ],
  "scope": "No result figures, source PDFs, target values or gold supplied. Named fixed ingredients are defined; structure graph is not varied in this formulation/physical-exposure subset."
}
```

## Output

Output only the JSON fields specified in the prompt; reason is required.

A missing or empty `reason` scores zero for the whole task.

Scoring fields: `order_spleen_liver`: array containing these 6 IDs exactly once, in the order required by the task (F03, F04, F07, F08, F09, F10); `order_bm_liver`: array containing these 6 IDs exactly once, in the order required by the task (F03, F04, F07, F08, F09, F10).
