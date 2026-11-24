---
bench_id: "SM-047-Cell-Biology-ADMET-Classification"
category: "Cell-Biology"
format: "structured_json"
---

# Prompt

Predict experimental hERG current inhibition from the supplied molecular structures. Total: 100 points.
Structures are listed in each question. The same molecule ID always denotes the same structure.
Use the supplied assay context; unreported conditions remain unspecified.
All required inputs are included in this Markdown; inputs/ contains no additional material.
The endpoint is hERG current-inhibition IC50 measured by patch clamp; higher IC50 means weaker inhibition. Retain each stated manual/automated method, cell system, temperature and material representation.

Bins (μM): H1 <3; H2 3–<10; H3 10–<30; H4 ≥30. Return a binning object {"molecule_id": "bin"} under the question ID. Each of the 10 molecules earns 10 points for its correct bin.

Return ONLY one strict JSON object keyed by the question IDs below. Do not include Markdown fences or explanations.
Unanswered questions or molecules may be omitted or set to null and earn zero. Arrays must contain distinct, valid options.
Unknown question IDs or duplicate JSON keys invalidate the entire response. Unknown molecule IDs in a binning object
make that question score zero; other invalid answers lose only the affected question or molecule points.
The scoring interface returns total points divided by 100, a number from 0 to 1.

## BIN-05 (100 points)

Predict the hERG current-inhibition IC50 bin for each molecule: H1, H2, H3 or H4.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M041 | `CCn1c(=O)c(-c2ccc(-c3cncc(C)n3)cc2Cl)cc2cnc(NCCN3CCON(C)CC3)nc21` |
| M042 | `Oc1cc(C(F)(F)F)ccc1-c1nnc(N[C@@H]2CCCC[C@H]2O)c2cnccc12` |
| M043 | `Cc1cccc(Cl)c1NC(=O)c1cnc(NCc2ccnn2-c2ccccc2)s1` |
| M044 | `Oc1cc(C(F)(F)F)ccc1-c1nnc(N[C@H]2CCC[C@@H](O)C2)c2ccccc12` |
| M045 | `CCN1CCC[C@@H](Nc2nnc(-c3ccc(S(C)(=O)=O)cc3)c3ccccc23)C1` |
| M046 | `CCCS(=O)(=O)Nc1c(F)ccc(C(=O)c2n[nH]c3ncc(-c4cnc(C5CC5)nc4)cc23)c1F` |
| M047 | `CCN1CCC[C@@H](Nc2ncc(-c3ccc(C(F)(F)F)cc3)c3ccccc23)C1` |
| M048 | `Oc1cc(C(F)(F)F)ccc1-c1nnc(N[C@@H]2CCC[C@H](O)C2)c2ccncc12` |
| M049 | `Cl.O=C(c1cc2cc(Cl)ccc2[nH]1)N(Cc1cccnc1)C1CCNCC1` |
| M050 | `CS(=O)(=O)N1CCC(C(=O)NC2CCCOc3c2nn(-c2ccccc2Cl)c3-c2ccc(Cl)cc2)CC1` |

Assay context:

- M041: Manual patch clamp; HEK293.
- M042, M044, M045, M047, M048: Automated patch clamp; CHO hKv11.1; room temperature.
- M043: Manual patch clamp; HEK293-hERG; 25 °C.
- M046: Patch clamp; manual/automated method not specified.
- M049: Automated patch clamp; CHO hERG DUO; Measured as the hydrochloride; the supplied structure retains this material representation..
- M050: Automated patch clamp.
