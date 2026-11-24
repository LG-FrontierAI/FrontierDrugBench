---
bench_id: "SM-049-Cell-Biology-ADMET-Top-k-Selection"
category: "Cell-Biology"
format: "structured_json"
---

# Prompt

Predict experimental hERG current inhibition from the supplied molecular structures. Total: 100 points.
Structures are listed in each question. The same molecule ID always denotes the same structure.
Use the supplied assay context; unreported conditions remain unspecified.
All required inputs are included in this Markdown; inputs/ contains no additional material.
The endpoint is hERG current-inhibition IC50 measured by patch clamp; higher IC50 means weaker inhibition. Retain each stated manual/automated method, cell system, temperature and material representation.

Relative comparisons are confined to each listed candidate group. For each question return an array of exactly two distinct candidate IDs. TOP-01 asks for the weakest inhibitors (highest IC50); TOP-02 asks for the strongest inhibitors (lowest IC50). Each question is worth 50 points; each correct selection earns 25 points. Order does not matter.

Return ONLY one strict JSON object keyed by the question IDs below. Do not include Markdown fences or explanations.
Unanswered questions or molecules may be omitted or set to null and earn zero. Arrays must contain distinct, valid options.
Unknown question IDs or duplicate JSON keys invalidate the entire response. Unknown molecule IDs in a binning object
make that question score zero; other invalid answers lose only the affected question or molecule points.
The scoring interface returns total points divided by 100, a number from 0 to 1.

## TOP-01 (50 points)

Select the TWO weakest hERG inhibitors (highest IC50).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M061 | `OC[C@H](O)CNc1nnc(-c2ccc(C(F)(F)F)cc2O)c2ccccc12` |
| M062 | `Oc1cc(C(F)(F)F)ccc1-c1nnc(N[C@H]2CCC[C@H](O)C2)c2ccccc12` |
| M063 | `CCN1CCC[C@@H](Nc2nnc(-c3ccc(S(C)(=O)=O)cc3O)c3ccccc23)C1` |
| M064 | `OCCCNc1nnc(-c2ccc(C(F)(F)F)cc2O)c2ccccc12` |
| M065 | `Oc1cc(C(F)(F)F)ccc1-c1nnc(N[C@@H]2CCC[C@@H](O)C2)c2ccccc12` |

Assay context (all candidates): Automated patch clamp; CHO hKv11.1; room temperature.

## TOP-02 (50 points)

Select the TWO strongest hERG inhibitors (lowest IC50).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M066 | `Nc1nc2c(c(C(F)(F)F)n1)C(=O)N(CC1(CCN3CCN(C4COC4)CC3)CCCC(C(F)(F)F)C1)C2` |
| M067 | `CCN1CCC12CCN(CCC1(CN3Cc4nc(N)nc(C(F)(F)F)c4C3=O)CCCC(C(F)(F)F)C1)CC2` |
| M068 | `Nc1nc2c(c(C(F)(F)F)n1)C(=O)N(CC1(CCN3CCNCC3)CCCC(C(F)(F)F)C1)C2` |
| M069 | `Nc1nc2c(c(C(F)(F)F)n1)C(=O)N(CC1(CCN3CCN(C4CC4)CC3)CCCC(C(F)(F)F)C1)C2` |
| M070 | `Nc1nc2c(c(C(F)(F)F)n1)C(=O)N(CC1(CCN3CCC4(CCN4)CC3)CCCC(C(F)(F)F)C1)C2` |

Assay context (all candidates): Automated patch clamp; CHO-hERG.
