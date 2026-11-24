---
bench_id: "SM-044-Cell-Biology-ADMET-Classification"
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

## BIN-02 (100 points)

Predict the hERG current-inhibition IC50 bin for each molecule: H1, H2, H3 or H4.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M011 | `CS(=O)(=O)c1ccc(-c2nnc(NCCCO)c3ccccc23)c(O)c1` |
| M012 | `[2H]C([2H])([2H])N(c1cnc(-c2ccccc2)c(-c2ccccc2)n1)[C@H]1CC[C@@H](OCC(=O)O)CC1` |
| M013 | `COc1ccn2c(-c3ccnc(N[C@H]4CNCC[C@@H]4F)n3)cnc2c1` |
| M014 | `[2H]C1([2H])c2ncccc2C(=O)N1Cc1c(F)cc(-c2cccc3nn(C([2H])([2H])[2H])cc23)cc1F` |
| M015 | `CC(C)Oc1ccn2c(-c3nsc(N[C@H]4CNCC[C@@H]4F)n3)cnc2c1` |
| M016 | `Oc1cc(C(F)(F)F)ccc1-c1nnc(N[C@@H]2CCC[C@H](O)C2)c2ccccc12` |
| M017 | `COc1ccc2[nH]c(C(=O)N(Cc3cccnc3)CC3CCNC3)cc2c1` |
| M018 | `CC(C)Oc1ccn2c(-c3ccnc(N[C@H]4CNCC[C@@H]4F)n3)cnc2c1` |
| M019 | `Nc1cc2c(c(C(F)(F)F)n1)C(=O)N(CC1(O)CCC(F)(F)CC1)C2` |
| M020 | `Oc1cc(C(F)(F)F)ccc1-c1nnc(N[C@@H]2CCCC[C@@H]2O)c2cnccc12` |

Assay context:

- M011, M016, M020: Automated patch clamp; CHO hKv11.1; room temperature.
- M012: Manual patch clamp; 25.0 °C.
- M013, M014, M015, M018: Manual patch clamp.
- M017: Automated patch clamp; CHO hERG DUO.
- M019: Automated patch clamp; CHO-hERG; Reported material is trans/racemic; the supplied structure retains the reported stereochemical representation..
