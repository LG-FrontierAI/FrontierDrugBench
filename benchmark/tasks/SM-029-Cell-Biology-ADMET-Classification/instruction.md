---
bench_id: "SM-029-Cell-Biology-ADMET-Classification"
category: "Cell-Biology"
format: "structured_json"
---

# Prompt

Predict experimental Caco-2 apical-to-basolateral permeability, Papp(A→B) from the supplied molecular structures. Total: 100 points.
Structures are listed in each question. The same molecule ID always denotes the same structure.
Relative comparisons are within the question's candidate group. Use the supplied assay context;
unreported conditions remain unspecified.
All required inputs are included in this Markdown; inputs/ contains no additional material.
Papp(A→B) is apical-to-basolateral permeability in 10^-6 cm/s.
Papp(A→B) bins: B1 <1; B2 1–<5; B3 5–<15; B4 ≥15.

Answer format and scoring:

- Binning: an object {"molecule_id": "bin"}. Each of the 10 molecules earns 10 points for its correct bin.

Return ONLY one strict JSON object keyed by the question IDs below. Do not include Markdown fences or explanations.
Unanswered questions or molecules may be omitted or set to null and earn zero. Arrays must contain distinct, valid options.
Unknown question IDs or duplicate JSON keys invalidate the entire response. Unknown molecule IDs in a binning object
make that question score zero; other invalid answers lose only the affected question or molecule points.
The scoring interface returns total points divided by 100, a number from 0 to 1.

## Papp-I01 (100 points)

Predict the Papp bin for each molecule: B1, B2, B3 or B4.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M041 | `Cn1nnc(CN(Cc2ccc(N)c(Cl)c2)C(=O)NCC(=O)N2CCC[C@@H]2c2ccccc2Br)n1` |
| M053 | `Cc1c(-c2ccnn2C)cc(C(=O)NCc2ccc(S(C)=N)cc2)c(=O)n1-c1cccc(C(F)(F)F)c1` |
| M061 | `CCCc1nc2ccccc2n1Cc1ccc(-c2cccc(C(N)=O)c2)cc1` |
| M062 | `CS(=N)(=O)c1ccc(C(F)(F)F)cc1` |
| M063 | `CCOC(=O)/C(C#N)=S(\NC(=O)C(C)(C)C)c1ccccc1` |
| M064 | `CSc1ccccc1[C@H]1CCCN1C(=O)CNC(=O)N(Cc1ccc2c(c1)[C@H]1C[C@@H](N2)[C@H](O)CO1)Cc1nnn(C)n1` |
| M065 | `Cc1ccc(CCC(=O)Nc2nnc(S(N)(=O)=O)s2)cc1` |
| M066 | `CC(C)C[C@@H]1NC(=O)[C@@H](N(C)C(=O)[C@@H](NC(=O)[C@@H]2C[C@@H](F)CN2C(=O)C2(C(F)(F)F)CCC(F)(F)CC2)C2CC2)CCCCNC(=O)C(C)(C)NC(=O)[C@H](Cc2cc(Cl)ccc2Cl)N(C)C1=O` |
| M067 | `Cc1cc2cc(Cl)cc(NC(=O)CC(C)(C)CC(=O)Nc3c(C)n4n(c3=O)-c3ccccc3OCC4)c2o1` |
| M068 | `Cc1c(-c2ccnn2C)cc(C(=O)NCc2ccc(S(C)(=O)=NC#N)cc2)c(=O)n1-c1cccc(C(F)(F)F)c1` |

Assay context:

- M041, M064: pH, concentration, duration and efflux-inhibitor conditions not reported.
- M053, M062, M063, M068: pH 7.2; general method specifies 10 μM, but individual concentrations are not confirmed; no efflux inhibitor.
- M061: pH 7.4; efflux-inhibitor co-treatment, concentration and duration not reported.
- M065: Apical pH 6.5/basolateral pH 7.4; no efflux inhibitor; concentration and duration not reported.
- M066: 10 μM, 37 °C, 1 h; HBSS/5 mM HEPES; no efflux inhibitor; pH not reported.
- M067: pH 7.4; 5 μM, 37 °C, 2 h; no efflux inhibitor. The method includes conditions with and without 1% BSA; the condition for each compound is not specified.
