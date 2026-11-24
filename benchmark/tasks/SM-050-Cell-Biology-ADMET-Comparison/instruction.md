---
bench_id: "SM-050-Cell-Biology-ADMET-Comparison"
category: "Cell-Biology"
format: "structured_json"
---

# Prompt

Predict experimental hERG current inhibition from the supplied molecular structures. Total: 100 points.
Structures are listed in each question. The same molecule ID always denotes the same structure.
Use the supplied assay context; unreported conditions remain unspecified.
All required inputs are included in this Markdown; inputs/ contains no additional material.
The endpoint is hERG current-inhibition IC50 measured by patch clamp; higher IC50 means weaker inhibition. Retain each stated manual/automated method, cell system, temperature and material representation.

Relative comparisons are confined to each listed pair. Return one molecule ID string for the weaker inhibitor (higher IC50). Each correct choice earns 20 points.

Return ONLY one strict JSON object keyed by the question IDs below. Do not include Markdown fences or explanations.
Unanswered questions or molecules may be omitted or set to null and earn zero. Arrays must contain distinct, valid options.
Unknown question IDs or duplicate JSON keys invalidate the entire response. Unknown molecule IDs in a binning object
make that question score zero; other invalid answers lose only the affected question or molecule points.
The scoring interface returns total points divided by 100, a number from 0 to 1.

## PAIR-01 (20 points)

Select the weaker hERG inhibitor (higher IC50).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M071 | `CCN1CCC[C@@H](Nc2nnc(-c3ccc(C(F)(F)F)cc3)c3cccn23)C1` |
| M072 | `CCN1CCC[C@@H](Nc2nnc(-c3ccc(S(C)(=O)=O)cc3)c3cccn23)C1` |

Assay context (all candidates): Automated patch clamp; CHO hKv11.1; room temperature.

## PAIR-02 (20 points)

Select the weaker hERG inhibitor (higher IC50).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M073 | `Cc1ccc(S(=O)(=O)N[C@H]2CCCOc3c2nn(-c2ccccc2Cl)c3-c2ccc(Cl)cc2)cc1` |
| M074 | `O=S(=O)(NC1CCCOc2c1nn(-c1ccccc1Cl)c2-c1ccc(Cl)cc1)c1ccc(Cl)cc1` |

Assay context (all candidates): Automated patch clamp.

## PAIR-03 (20 points)

Select the weaker hERG inhibitor (higher IC50).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M075 | `CN(C[C@H]1Cc2c(cccc2N2CCO[C@H](CO)C2)CN1)[C@H]1CCCc2cccnc21` |
| M076 | `CN(C[C@H]1Cc2c(cccc2N2CCOCC2=O)CN1)[C@H]1CCCc2cccnc21` |

Assay context (all candidates): Automated patch clamp.

## PAIR-04 (20 points)

Select the weaker hERG inhibitor (higher IC50).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M077 | `COc1cc2c(cc1OCc1ccccc1)N(c1ccncc1)CC21CCN(C)CC1` |
| M078 | `COc1cc2c(cc1OCc1ccccc1)N(C(=O)c1cc3cnccc3[nH]1)CC21CCN(C)CC1` |

Assay context (all candidates): Automated patch clamp.

## PAIR-05 (20 points)

Select the weaker hERG inhibitor (higher IC50).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M079 | `CCCS(=O)(=O)Nc1c(F)ccc(C(=O)c2c[nH]c3ncc(-c4cnc(C5CC5)nc4)cc23)c1F` |
| M080 | `CCCS(=O)(=O)Nc1c(F)ccc(C(=O)c2c[nH]c3ncc(-c4cnc(SC)nc4C)cc23)c1F` |

Assay context (all candidates): Patch clamp; manual/automated method not specified.
