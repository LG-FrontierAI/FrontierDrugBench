---
bench_id: "SM-051-Cell-Biology-ADMET-Ranking"
category: "Cell-Biology"
format: "structured_json"
---

# Prompt

Predict experimental hERG current inhibition from the supplied molecular structures. Total: 100 points.
Structures are listed in each question. The same molecule ID always denotes the same structure.
Use the supplied assay context; unreported conditions remain unspecified.
All required inputs are included in this Markdown; inputs/ contains no additional material.
The endpoint is hERG current-inhibition IC50 measured by patch clamp; higher IC50 means weaker inhibition. Retain each stated manual/automated method, cell system, temperature and material representation.

Relative comparisons are confined to each listed candidate group. Return every candidate ID exactly once in an array ordered from weakest to strongest inhibition (highest to lowest IC50). Each question is worth 50 points. Ranking points use equally weighted experimental pairwise relations separated by at least 1.5-fold; the order of closer values does not affect the score.

Return ONLY one strict JSON object keyed by the question IDs below. Do not include Markdown fences or explanations.
Unanswered questions or molecules may be omitted or set to null and earn zero. Arrays must contain distinct, valid options.
Unknown question IDs or duplicate JSON keys invalidate the entire response. Unknown molecule IDs in a binning object
make that question score zero; other invalid answers lose only the affected question or molecule points.
The scoring interface returns total points divided by 100, a number from 0 to 1.

## RANK-01 (50 points)

Rank all molecules from weakest to strongest hERG inhibition (IC50 from highest to lowest).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M081 | `CC(C)Oc1ccn2c(-c3cccc(N[C@H]4CNCC[C@@H]4F)n3)cnc2c1` |
| M082 | `CC(C)Oc1ccn2c(-c3cc(F)cc(N[C@H]4CNCC[C@@H]4F)n3)cnc2c1` |
| M083 | `CC(C)Oc1ccn2c(-c3nc(N[C@H]4CNCC[C@@H]4F)ccc3F)cnc2c1` |
| M084 | `CC(C)Oc1ccn2c(-c3nc(N[C@H]4CNCC[C@@H]4F)c(F)cc3F)cnc2c1` |
| M085 | `CC(C)Oc1ccn2c(-c3ccc(F)c(N[C@H]4CNCC[C@@H]4F)n3)cnc2c1` |

Assay context (all candidates): Manual patch clamp.

## RANK-02 (50 points)

Rank all molecules from weakest to strongest hERG inhibition (IC50 from highest to lowest).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M086 | `CCn1c(=O)c(-c2ccc(-c3cncc(C)n3)cc2Cl)cc2cnc(NCCC3CCN(C)OC3)nc21` |
| M087 | `CCn1c(=O)c(-c2ccc(-c3cncc(C)n3)cc2Cl)cc2cnc(NCCN3CCN(C)CCO3)nc21` |
| M088 | `CCn1c(=O)c(-c2ccc(-c3cncc(C)n3)cc2Cl)cc2cnc(NCCN3CCN(OC)CC3)nc21` |
| M089 | `CCn1c(=O)c(-c2ccc(-c3cncc(C)n3)cc2Cl)cc2cnc(NCCCN3CCN(OC)CC3)nc21` |
| M090 | `CCn1c(=O)c(-c2ccc(-c3cncc(C)n3)cc2Cl)cc2cnc(NCCON3CCN(C)CC3)nc21` |

Assay context (all candidates): Manual patch clamp; HEK293.
