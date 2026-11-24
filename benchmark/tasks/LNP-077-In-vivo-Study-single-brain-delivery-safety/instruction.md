---
bench_id: LNP-077-In-vivo-Study-single-brain-delivery-safety
category: "In-vivo-Study"
title: "Acoustic-pressure matrix for one SM102 formulation: delivery intensity, spatial width and acute damage"
format: structured_json
---

# Prompt

Predict separately: (1) order_width covers only P400/P220/P180, from largest to smallest opening X width; (2) order_intensity covers all five groups, from high to low brain-region Cy5 intensity; only source-supported strict relations are scored; (3) histology_map covers only P400/P180, with the value reported_damage or no_damage_observed, describing the result reported for that time window and not implying zero long-term risk. Do not equate fluorescence with functional silencing; NS is not equivalence. Output JSON with a non-empty reason. The permutation covers every ID declared for that field; only source-supported pairwise orders are scored and unknown relationships are not scored.

## Input

The structured model input is below (JSON).

```json
{
  "candidates": [
    {
      "id": "P400",
      "PNP_kPa": 400,
      "formulation": "SM102/DSPC/cholesterol/PEG-DMG50/10/38.5/1.5"
    },
    {
      "id": "P330",
      "PNP_kPa": 330,
      "formulation": "SM102/DSPC/cholesterol/PEG-DMG50/10/38.5/1.5"
    },
    {
      "id": "P220",
      "PNP_kPa": 220,
      "formulation": "SM102/DSPC/cholesterol/PEG-DMG50/10/38.5/1.5"
    },
    {
      "id": "P180",
      "PNP_kPa": 180,
      "formulation": "SM102/DSPC/cholesterol/PEG-DMG50/10/38.5/1.5"
    },
    {
      "id": "LNP_only",
      "PNP_kPa": null,
      "formulation": "Same SM102 LNP; no MB/FUS"
    }
  ],
  "conditions": {
    "context_key": "Ex5:SM102:siRNA:PNP:2.5h",
    "endpoint": "Brain fluorescence, opening width and reported acute histological damage",
    "animal": "Healthy 8-12-week-old female C57BL/j6 mice, 19-23 g (source spelling p34; do not silently change to a particular substrain)",
    "cargo": "Non-template siRNA,50%Cy5-labelled fraction",
    "dose": "1mg/kg systemic injection; exact vein not specified in methods",
    "harvest": "2.5h; unperfused brain",
    "FUS": "850kHz,1ms bursts,1Hz PRF,0.1%duty; MB thenFUS within60s; LNP immediately afterFUS",
    "MB": "DSPC/DSPE-PEG2K90/10,perfluorobutane core;50uL per20g;count exponent unresolved",
    "LNP_properties": "~70nm,zeta-0.426mV,encapsulation>95%",
    "replicates": "N3 perarm,total15",
    "missing_protocol_inputs": "Total sonication duration, exact MB count exponent, exact siRNA sequence"
  },
  "submission_fields": [
    {
      "type": "Ranking_constraints",
      "key": "Order_width",
      "candidate_ids": [
        "P400",
        "P220",
        "P180"
      ]
    },
    {
      "type": "Ranking_constraints",
      "key": "Order_intensity",
      "candidate_ids": [
        "P400",
        "P330",
        "P220",
        "P180",
        "LNP_only"
      ]
    },
    {
      "type": "Mapping_choice",
      "key": "Histology_map",
      "candidate_ids": [
        "P400",
        "P180"
      ],
      "choices": [
        "Reported_damage",
        "No_damage_observed"
      ]
    }
  ],
  "scope": "No result figures, source PDFs, target values or gold supplied. Named fixed ingredients are defined; structure graph is not varied in this formulation/physical-exposure subset."
}
```

## Output

Output only the JSON fields specified in the prompt; reason is required.

A missing or empty `reason` scores zero for the whole task.

Scoring fields: `order_width`: array containing these 3 IDs exactly once, in the order required by the task (P400, P220, P180); `order_intensity`: array containing these 5 IDs exactly once, in the order required by the task (P400, P330, P220, P180, LNP_only); `histology_map`: object whose keys are all candidate IDs and whose values are one of (reported_damage / no_damage_observed).
