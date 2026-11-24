---
bench_id: "SM-041-In-vivo-Study-ADMET-Comparison"
category: "In-vivo-Study"
format: "structured_json"
---

# Prompt

Predict experimental unbound brain/plasma partitioning (Kp,uu) from the supplied molecular structures. Total: 100 points.
Structures are listed in each question. The same molecule ID always denotes the same structure.
Use the supplied assay context; unreported conditions remain unspecified.
All required inputs are included in this Markdown; inputs/ contains no additional material.
Kp,uu is the unbound tissue/plasma ratio for the specified brain region and time basis. Use the stated species, route and sampling context. Brain and cerebellum, single-time-point and AUC measurements, and different species or dosing regimens must retain their stated distinctions.

Relative comparisons are confined to each listed pair. For each question return one molecule ID string. Each correct choice earns 20 points.

Return ONLY one strict JSON object keyed by the question IDs below. Do not include Markdown fences or explanations.
Unanswered questions or molecules may be omitted or set to null and earn zero. Arrays must contain distinct, valid options.
Unknown question IDs or duplicate JSON keys invalidate the entire response. Unknown molecule IDs in a binning object
make that question score zero; other invalid answers lose only the affected question or molecule points.
The scoring interface returns total points divided by 100, a number from 0 to 1.

## PAIR-01 (20 points)

Select the molecule with the higher Kp,uu.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M061 | `C=CC(=O)N(C)[C@H]1CC[C@@H](Oc2nc(-c3cnn(C)c3)cn3nccc23)C1` |
| M062 | `C=CC(=O)N(C)[C@H]1C[C@@H](Oc2nc(-c3cnn(C)c3)cn3nccc23)C1` |

Assay context (all candidates): rat; constant IV infusion; sampling: 24 h infusion study; end of infusion; unbound brain/plasma ratio.

## PAIR-02 (20 points)

Select the molecule with the higher Kp,uu.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M063 | `Cn1ncc(Nc2nccc(-c3ccc4c(c3)CCCC[C@H]4NC(=O)c3noc(C(C)(C)C)n3)n2)n1` |
| M064 | `Cn1cc(Nc2nccc(-c3ccc4c(c3)CCCC[C@H]4NC(=O)c3noc(C(C)(C)C)n3)n2)cn1` |

Assay context (all candidates): rat; constant IV infusion; sampling: 24 h; end of infusion; unbound brain/plasma ratio.

## PAIR-03 (20 points)

Select the molecule with the higher Kp,uu.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M065 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)[C@H]2CC[C@@]3(C(=O)O)C[C@H]3C2)c(OC(F)F)n1` |
| M066 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)[C@H]2CC[C@](C)(C(=O)O)CC2)c(OC(F)F)n1` |

Assay context (all candidates): rat; PO; 10 mg/kg; sampling: 2 h; single time point, 2 h postdose; unbound brain/plasma ratio.

## PAIR-04 (20 points)

Select the molecule with the higher Kp,uu.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M067 | `C=CC(=O)N1CCN([C@@H]2CN(c3cc(N4CCC(c5c(C)cnn5C5COC5)CC4)nc(C(F)(F)F)n3)[C@@H]2C)CC1` |
| M068 | `C=CC(=O)N1CCN([C@@H]2CN(c3cc(N4CCC(c5c(C)cnn5CCOC)CC4)nc(C(F)(F)F)n3)[C@@H]2C)CC1` |

Assay context (all candidates): mouse CD1; PO; single time point; unbound brain/plasma ratio.

## PAIR-05 (20 points)

Select the molecule with the higher Kp,uu.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M069 | `CC(=O)N1CC[C@@H](n2ncc(Cl)c2C(=O)Nc2ncc(C#Cc3ccc(F)cc3)cc2C)[C@H](F)C1` |
| M070 | `CC(=O)N1CCC(n2ncc(Cl)c2C(=O)Nc2ncc(C#Cc3ccccc3)cc2C)CC1` |

Assay context (all candidates): Sprague-Dawley rat; IV; sampling: 0.25 h; unbound brain/plasma ratio.

The CXSMILES |a:…| extension specifies enhanced stereochemistry. Preserve it and use a CXSMILES-compatible reader.
