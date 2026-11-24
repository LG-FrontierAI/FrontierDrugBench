---
bench_id: LNP-039-Cell-Biology-single-targeting-switch-cd7
category: "Cell-Biology"
title: "Targeting switch and CD7 receptor background rewrite helper-lipid preference across four contexts"
format: structured_json
---

# Prompt

Does the same helper series keep its original order across genuinely different targeting/receptor backgrounds? Predict the functional relations in four independent experimental contexts; do not split the same five-molecule reverse ranking into several tasks. Output order_targeted_T, order_untargeted_T, order_untargeted_HEK, CD7_HEK_targeting_gain and a non-empty reason. Each order must list every candidate specified for that field; only source-supported pairwise relations count and unknown comparisons are not scored. Order each ordering field from the highest value to the lowest: the first element is the largest, the last element the smallest.

## Input

The structured model input is below (JSON).

```json
{
  "candidates": [
    {
      "id": "DSPC",
      "chemical_name": "1,2-distearoyl-sn-glycero-3-phosphocholine",
      "CAS": "816-94-4",
      "headgroup": "PC",
      "acyl_chains": "18:0/18:0"
    },
    {
      "id": "DPPC",
      "chemical_name": "1,2-dipalmitoyl-sn-glycero-3-phosphocholine",
      "CAS": "63-89-8",
      "headgroup": "PC",
      "acyl_chains": "16:0/16:0"
    },
    {
      "id": "DMPC",
      "chemical_name": "1,2-dimyristoyl-sn-glycero-3-phosphocholine",
      "CAS": "18194-24-6",
      "headgroup": "PC",
      "acyl_chains": "14:0/14:0"
    },
    {
      "id": "DAPC",
      "chemical_name": "1,2-diarachidoyl-sn-glycero-3-phosphatidylcholine",
      "CAS": "61596-53-0",
      "headgroup": "PC",
      "acyl_chains": "20:0/20:0"
    },
    {
      "id": "DOPC",
      "chemical_name": "1,2-di-(9Z-octadecenoyl)-sn-glycero-3-phosphocholine",
      "CAS": "4235-95-4",
      "headgroup": "PC",
      "acyl_chains": "18:1cis9/18:1cis9"
    },
    {
      "id": "DOPE",
      "chemical_name": "1,2-di-(9Z-octadecenoyl)-sn-glycero-3-phosphoethanolamine",
      "CAS": "4004-05-1",
      "headgroup": "PE",
      "acyl_chains": "18:1cis9/18:1cis9"
    },
    {
      "id": "EggPC",
      "chemical_name": "L-alpha-phosphatidylcholine from egg",
      "CAS": "97281-44-2",
      "headgroup": "PC",
      "acyl_chains": "Naturalmixture;notasinglemolecularspecies"
    },
    {
      "id": "DSPE",
      "chemical_name": "1,2-dioctadecanoyl-sn-glycero-3-phosphoethanolamine",
      "CAS": "1069-79-0",
      "headgroup": "PE",
      "acyl_chains": "18:0/18:0"
    },
    {
      "id": "DSPG",
      "chemical_name": "1,2-dioctadecanoyl-sn-glycero-3-phospho-(1prime-rac-glycerol)",
      "CAS": "200880-42-8",
      "headgroup": "PG",
      "acyl_chains": "18:0/18:0"
    }
  ],
  "formulation": {
    "base": "SM-102/helper/cholesterol/DMG-PEG2000,40:20:39:1molar",
    "NP": "Generalmethod5.6–6.6",
    "SM102_identity": "SM-102CAS2089251-47-6",
    "targeting": "AntiCD3scFv+antiCD7VHH;DSPE-PEG2000-maleimidepost-insertion;exactdensitynotrepeatedperhelperexperiment",
    "binder_density": null,
    "control": "Otherwiseidenticalnon-targetedLNPwhereindicated"
  },
  "contexts": [
    {
      "id": "Targeted_T",
      "cells": "ActivatedprimaryhumanTcells",
      "reporters": "EGFPmcDNA+BFPmRNA",
      "candidate_ids": [
        "DSPC",
        "DPPC",
        "DMPC",
        "DOPC",
        "DSPE",
        "DSPG"
      ],
      "dose": "Fig11series75/150/300ng;DSPC/DSPE/DSPGareseparateFig15doseseries,notpooledatidenticaldose;onlywithin-experimentrelationsscored"
    },
    {
      "id": "Untargeted_T",
      "cells": "ActivatedprimaryhumanTcells",
      "reporter": "GFPmcDNA",
      "candidate_ids": [
        "DSPC",
        "DOPC",
        "DOPE"
      ],
      "dose": "Highdose>1200ng;notdosematchedtotargetedgroup"
    },
    {
      "id": "Untargeted_HEK",
      "cells": "WildtypeHEK293",
      "reporters": "EGFPmcDNA+mCherrymRNA",
      "candidate_ids": [
        "DSPC",
        "DPPC",
        "DAPC",
        "DOPC",
        "DOPE",
        "EggPC"
      ],
      "dose": "Notreportedintheendpointprose"
    },
    {
      "id": "CD7_HEK_targeting_gain",
      "cells": "CD7-GFPengineeredHEK293",
      "reporter": "MCherrymRNAonly;GFPmcDNAunreliablebecauseCD7-GFPfusion",
      "candidate_ids": [
        "DSPC",
        "DOPC",
        "DOPE"
      ],
      "prediction": "Largevsmodestfoldgainfromnon-targetedtotargeted;notabsoluteexpressionrank"
    }
  ],
  "endpoint_time": "Notrecoveredintheendpointprose;donotcompareabsolutevaluesacrosscontexts",
  "submission_keys": {
    "order_targeted_T": [
      "DSPC",
      "DPPC",
      "DMPC",
      "DOPC",
      "DSPE",
      "DSPG"
    ],
    "order_untargeted_T": [
      "DSPC",
      "DOPC",
      "DOPE"
    ],
    "order_untargeted_HEK": [
      "DSPC",
      "DPPC",
      "DAPC",
      "DOPC",
      "DOPE",
      "EggPC"
    ],
    "CD7_HEK_targeting_gain": {
      "DSPC": "Large|modest",
      "DOPC": "Large|modest",
      "DOPE": "Large|modest"
    }
  },
  "scope": "CommercialstructuresarechemicallyidentifiedbyCAS+fullstereochemicalnames/acylchains;EggPCisamixture. Noresulttextorfigureprovidedtothemodel."
}
```

## Output

Output only the JSON fields specified in the prompt; reason is required.

A missing or empty `reason` scores zero for the whole task.

Scoring fields: `order_targeted_T`: array containing these 6 IDs exactly once, in the order required by the task (DSPC, DPPC, DMPC, DOPC, DSPE, DSPG); `order_untargeted_T`: array containing these 3 IDs exactly once, in the order required by the task (DSPC, DOPC, DOPE); `order_untargeted_HEK`: array containing these 6 IDs exactly once, in the order required by the task (DSPC, DPPC, DAPC, DOPC, DOPE, EggPC); `CD7_HEK_targeting_gain`: object whose keys are all candidate IDs and whose values are one of (large / modest).
