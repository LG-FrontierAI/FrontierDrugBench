---
bench_id: "SM-045-Cell-Biology-ADMET-Classification"
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

## BIN-03 (100 points)

Predict the hERG current-inhibition IC50 bin for each molecule: H1, H2, H3 or H4.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M021 | `Oc1cc(C(F)(F)F)ccc1-c1nnc(N[C@@H]2CCC[C@H](O)C2)c2ncccc12` |
| M022 | `Nc1cc2c(c(F)n1)C(=O)N(CC1(O)CCC(F)(F)CC1)C2` |
| M023 | `Cn1ccc(Nc2cc(-c3ccc(CNC(=O)c4nc(C(C)(C)C)no4)c(C(F)F)c3F)ncn2)n1` |
| M024 | `OCCCNc1nnc(-c2ccc(C(F)(F)F)cc2)c2cccn12` |
| M025 | `COc1cc2c(cc1OCc1ccccc1)N(C(=O)c1cc3ccccc3[nH]1)CC21CCN(C)CC1` |
| M026 | `Nc1nc2c(c(C(F)(F)F)n1)C(=O)N(CC1(O)CCCC(F)(F)C1)C2` |
| M027 | `C[C@H](c1ccc(C(F)(F)F)cc1)N(C)C(=O)C(=O)Nc1cnc(N)c2cn[nH]c12` |
| M028 | `OCCCNc1cnc(-c2ccc(C(F)(F)F)cc2O)c2ccccc12` |
| M029 | `CC(C)N1CCc2cc3cc(-n4ccc(OCc5ccc(Cl)cn5)cc4=O)ccc3n2CC1` |
| M030 | `O=C(c1cc2cc(Cl)ccc2[nH]1)N(Cc1cccnc1)CC1CCNCC1` |

Assay context:

- M021, M024, M028: Automated patch clamp; CHO hKv11.1; room temperature.
- M022, M026: Automated patch clamp; CHO-hERG; Reported material is trans/racemic; the supplied structure retains the reported stereochemical representation..
- M023: Patch clamp; manual/automated method not specified.
- M025: Automated patch clamp.
- M027: Automated patch clamp; CHO-hERG; room temperature.
- M029: Manual patch clamp; HEK293 stably expressing human Kv11.1; 36±1 °C; Measured as the maleate salt; the supplied structure shows the reported parent compound..
- M030: Automated patch clamp; CHO hERG DUO.
