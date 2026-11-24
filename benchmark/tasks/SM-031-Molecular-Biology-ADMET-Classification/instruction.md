---
bench_id: "SM-031-Molecular-Biology-ADMET-Classification"
category: "Molecular-Biology"
format: "structured_json"
---

# Prompt

Predict experimental human liver microsomal (HLM) metabolic stability from the supplied molecular structures. Total: 100 points.
Structures are listed in each question. The same molecule ID always denotes the same structure.
Use the supplied assay context; unreported conditions remain unspecified.
All required inputs are included in this Markdown; inputs/ contains no additional material.
Lower total HLM intrinsic clearance (CLint, μL/min/mg) means greater stability.

Return a bin label for every molecule. Each of the 10 molecules earns 10 points for its correct bin. Bin definitions and units are specified in the question below.

Return ONLY one strict JSON object keyed by the question IDs below. Do not include Markdown fences or explanations.
Unanswered questions or molecules may be omitted or set to null and earn zero. Arrays must contain distinct, valid options.
Unknown question IDs or duplicate JSON keys invalidate the entire response. Unknown molecule IDs in a binning/profile object
make that question score zero; other invalid answers lose only the affected question or molecule points.
The scoring interface returns total points divided by 100, a number from 0 to 1.

## HLM-INTERVAL01 (100 points)

Predict the total HLM CLint bin for each molecule: S1 ≤10; S2 >10–30; S3 >30–100; S4 >100 μL/min/mg.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M001 | `C[C@@H](COCCCCNCc1ccc(OC(F)(F)F)c(Cl)c1)Nc1nc2cc(C(=O)O)ccc2c2cnccc12` |
| M002 | `C[C@@H]1CN(c2ccc(-c3c(NCc4ccccn4)c(=O)c3=O)cc2)C[C@H](C)O1` |
| M003 | `O=S(=O)(NCCO)c1ccc(-c2ccnc3[nH]ccc23)cc1` |
| M004 | `NC(=O)c1c2c(nn1Cc1ccccc1)C(=O)N([C@@H](c1ccccc1)C1CC1)CC2` |
| M005 | `Cn1cc(-c2ccc3c(C#N)cn(CC(=O)Nc4ccccc4Cl)c3c2)cn1` |
| M006 | `CSc1ccccc1[C@H]1CCCN1C(=O)CNC(=O)N(Cc1ccc2c(c1)[C@H]1C[C@@H](N2)[C@H](O)CO1)Cc1nnn(C)n1` |
| M007 | `COc1cc(-c2cnc3cc(-c4ccc5cnn(C)c5c4)ccn23)cc(OC)c1C(=O)NCC(F)(F)F` |
| M008 | `Cc1ccc(-c2ccc(C)c3c2C=C(c2ccc(-c4ccc(C(=O)O)cc4)[nH]2)[C@H](C)O3)cc1` |
| M009 | `COc1ccnc(OCCNCC2(F)CCN(C(=O)c3ccc(F)c(Cl)c3)CC2)c1` |
| M010 | `O=C1OCCC1N(C(=O)OCc1cccnc1)C(F)(F)F` |

Assay context (all candidates): Human liver microsomes; total CLint (μL/min/mg).
