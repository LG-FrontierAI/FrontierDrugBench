---
bench_id: "SM-046-Cell-Biology-ADMET-Classification"
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

## BIN-04 (100 points)

Predict the hERG current-inhibition IC50 bin for each molecule: H1, H2, H3 or H4.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M031 | `COc1nc(NC2CNC2)c(C(=O)N[C@H](C)c2cccc(C(F)F)c2F)cc1-c1cnn(C)c1` |
| M032 | `Cc1cccc(Cl)c1NC(=O)c1cnc(NCC2CCC2)s1` |
| M033 | `COc1ccn2c(-c3nc(N[C@H]4CNCC[C@@H]4F)c(F)cc3F)cnc2c1` |
| M034 | `O=C(c1cc2cc(C(F)(F)F)ccc2[nH]1)N(Cc1cccnc1)CC1CCNC1` |
| M035 | `O=C(O)c1ccc2c(c1)nc(OCCOCCCCNCc1cc(F)c(OC(F)(F)F)c(F)c1)c1ccncc12` |
| M036 | `CCCS(=O)(=O)Nc1c(F)ccc(C(=O)c2n[nH]c3ncc(-c4ccncc4)cc23)c1F` |
| M037 | `Cn1ccc(Nc2nccc(-c3ccc4c(c3)CCCC[C@H]4NC(=O)c3noc(C(C)(C)C)n3)n2)n1` |
| M038 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)C2CCN(C(C)=O)CC2)c(OC(F)F)n1` |
| M039 | `Cc1ncccc1-c1ccc2ncc3c(c2c1)n(C1CCOCC1)c(=O)n3C` |
| M040 | `CC(C)Oc1ccn2c(-c3csc(N[C@H]4CNCC[C@@H]4F)n3)cnc2c1` |

Assay context:

- M031: Manual patch clamp; HEK293-hERG; 25.0 °C.
- M032: Manual patch clamp; HEK293-hERG; 25 °C.
- M033, M040: Manual patch clamp.
- M034: Automated patch clamp; CHO hERG DUO.
- M035: Manual patch clamp; HEK293-hERG; 35-37 °C.
- M036, M037: Patch clamp; manual/automated method not specified.
- M038: Manual patch clamp; HEK293-hERG; 34 °C.
- M039: Patch clamp; manual/automated method not specified; CHO-hERG.
