---
bench_id: "SM-043-Cell-Biology-ADMET-Classification"
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

## BIN-01 (100 points)

Predict the hERG current-inhibition IC50 bin for each molecule: H1, H2, H3 or H4.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M001 | `COc1ccn2c(-c3cncc(N[C@H]4CNCC[C@@H]4F)n3)cnc2c1` |
| M002 | `CCCCCCNc1ncc(C(=O)Nc2c(C)cccc2Cl)s1` |
| M003 | `Cc1cc(-c2ccnc(Nc3ccn(C)n3)n2)ccc1CNC(=O)c1noc(C(C)(C)C)n1` |
| M004 | `O=C(c1cc2cc(Cl)ccc2[nH]1)N(Cc1ccc(C(F)(F)F)nc1)CC1CCNC1` |
| M005 | `Oc1cc(C(F)(F)F)ccc1-c1nnc(N[C@@H]2CCC[C@H](O)C2)c2cnccc12` |
| M006 | `CCOC(=O)CCC(=O)Nc1ncc(C(=O)Nc2c(C)cccc2Cl)s1` |
| M007 | `CCCNc1nnc(-c2ccc(C(F)(F)F)cc2O)c2cccn12` |
| M008 | `Nc1nc2cc(-c3nn(Cc4ccnc(Cl)c4)c4ncnc(N)c34)ccc2o1` |
| M009 | `C[C@@H](NC(=O)c1cc(C2CC2)cnc1NC1CNC1)c1cccc(C(F)F)c1F` |
| M010 | `Nc1nc2cc(-c3nn(Cc4ccc(Cl)c(F)c4)c4ncnc(N)c34)ccc2o1` |

Assay context:

- M001: Manual patch clamp.
- M002, M006, M009: Manual patch clamp; HEK293-hERG; 25.0 °C.
- M003: Patch clamp; manual/automated method not specified.
- M004: Automated patch clamp; CHO hERG DUO.
- M005, M007: Automated patch clamp; CHO hKv11.1; room temperature.
- M008, M010: Automated patch clamp; CHO-hERG; room temperature (19–30 C).
