---
bench_id: "SM-040-In-vivo-Study-ADMET-Top-k-Selection"
category: "In-vivo-Study"
format: "structured_json"
---

# Prompt

Predict experimental unbound brain/plasma partitioning (Kp,uu) from the supplied molecular structures. Total: 100 points.
Structures are listed in each question. The same molecule ID always denotes the same structure.
Use the supplied assay context; unreported conditions remain unspecified.
All required inputs are included in this Markdown; inputs/ contains no additional material.
Kp,uu is the unbound tissue/plasma ratio for the specified brain region and time basis. Use the stated species, route and sampling context. Brain and cerebellum, single-time-point and AUC measurements, and different species or dosing regimens must retain their stated distinctions.

Relative comparisons are confined to each listed candidate group. For each question return exactly two distinct candidate IDs as an array. Each question is worth 25 points; each correct selection earns 12.5 points. Order does not matter.

Return ONLY one strict JSON object keyed by the question IDs below. Do not include Markdown fences or explanations.
Unanswered questions or molecules may be omitted or set to null and earn zero. Arrays must contain distinct, valid options.
Unknown question IDs or duplicate JSON keys invalidate the entire response. Unknown molecule IDs in a binning object
make that question score zero; other invalid answers lose only the affected question or molecule points.
The scoring interface returns total points divided by 100, a number from 0 to 1.

## TOP-01 (25 points)

Select the TWO molecules with the highest Kp,uu.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M041 | `CC(C)Oc1cc2nc(C34COC(C)(C3)C4)cn2cc1C(=O)Nc1cccc(C(F)F)n1` |
| M042 | `CC(C)Oc1cc2nc(C34COC(C)(C3)C4)cn2cc1C(=O)Nc1cnn2cccnc12` |
| M043 | `CC(C)Oc1nc2nc(C34COC(C)(C3)C4)cn2cc1C(=O)Nc1cnn2cccnc12` |
| M044 | `CC(C)Oc1nc2nc(C34COC(C)(C3)C4)cn2cc1C(=O)Nc1cnn2cc(F)cnc12` |
| M045 | `Cc1cnc2c(NC(=O)c3cn4cc(C56COC(C)(C5)C6)nc4c(F)c3OC(C)C)cnn2c1` |

Assay context (all candidates): rat; constant IV infusion; sampling: 4–24 h infusion; exact duration per analogue not reported; end of infusion; unbound brain/plasma ratio.

## TOP-02 (25 points)

Select the TWO molecules with the highest Kp,uu.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M046 | `C=CC(=O)N(C)[C@@H]1CCC[C@H](Oc2nc(-c3cnn(C)c3)cn3nccc23)C1` |
| M047 | `C=CC(=O)N(C)[C@H]1C[C@@](C)(Oc2nc(-c3cnn(C)c3)cn3nccc23)C1` |
| M048 | `C=CC(=O)N1CC[C@H]2[C@H]1C[C@]2(C)Oc1nc(-c2cnn(C)c2)cn2nccc12` |
| M049 | `C=CC(=O)N1C[C@@H]2C[C@H](Oc3nc(-c4cnn(C)c4)cn4nccc34)C[C@H]1C2` |
| M050 | `C=CC(=O)N1C[C@@H]2[C@@H](COc3nc(-c4cnn(C)c4)cn4nccc34)[C@@H]2C1` |

Assay context (all candidates): rat; constant IV infusion; sampling: 24 h infusion study; end of infusion; unbound brain/plasma ratio.

## TOP-03 (25 points)

Select the TWO molecules with the highest Kp,uu.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M051 | `Cc1cc(-c2cc(Nc3ccn(C)n3)ncn2)ccc1CNC(=O)c1noc(C(C)(C)C)n1` |
| M052 | `Cc1cc(-c2cc(Nc3ccn(C)n3)ncn2)ccc1CNC(=O)c1coc(C(C)(C)C)n1` |
| M053 | `Cn1ccc(Nc2cc(-c3ccc(CNC(=O)c4nc(C(C)(C)C)no4)c(C(F)F)c3)ncn2)n1` |
| M054 | `Cc1cc(-c2ccnc(Nc3ccn(C)n3)n2)ccc1CNC(=O)c1noc(C(C)(C)C)n1` |
| M055 | `Cn1ccc(Nc2cc(-c3ccc(CNC(=O)c4nc(C(C)(C)C)no4)c(Cl)c3)ncn2)n1` |

Assay context (all candidates): rat; constant IV infusion; sampling: 24 h; end of infusion; unbound brain/plasma ratio.

## TOP-04 (25 points)

Select the TWO molecules with the highest Kp,uu.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M056 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)C2CCN(S(C)(=O)=O)CC2)c(OC(F)F)n1` |
| M057 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)[C@H]2CC[C@@H](S(C)(=O)=O)CC2)c(OC(F)F)n1` |
| M058 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)C2CCN(C3COC3)CC2)c(OC(F)F)n1` |
| M059 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)C2CCN(C(C)=O)CC2)c(OC(F)F)n1` |
| M060 | `CC(=O)N1CCC(N(C(=O)Nc2ccc(C)nc2OC(F)F)c2ccccc2C(C)C)CC1` |

Assay context (all candidates): rat; PO; 10 mg/kg; sampling: 2 h; single time point, 2 h postdose; unbound brain/plasma ratio.

The CXSMILES |a:…| extension specifies enhanced stereochemistry. Preserve it and use a CXSMILES-compatible reader.
