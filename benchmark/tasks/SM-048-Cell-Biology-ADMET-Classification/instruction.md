---
bench_id: "SM-048-Cell-Biology-ADMET-Classification"
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

## BIN-06 (100 points)

Predict the hERG current-inhibition IC50 bin for each molecule: H1, H2, H3 or H4.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M051 | `CC(C)Oc1ccn2c(-c3nc(N[C@H]4CNCC[C@@H]4F)no3)cnc2c1` |
| M052 | `CC(C)Oc1ccn2c(-c3cncc(N[C@H]4CNCC[C@@H]4F)n3)cnc2c1` |
| M053 | `CCCS(=O)(=O)Nc1c(F)ccc(C(=O)c2n[nH]c3ncc(-c4cnc(OC)nc4)cc23)c1F` |
| M054 | `Nc1nc2cc(-c3nn(Cc4ccc(Cl)c(Cl)c4)c4ncnc(N)c34)ccc2o1` |
| M055 | `c1cnc2c(c1)CCC[C@@H]2N(CCCC1CCNCC1)C[C@H]1Cc2c(cccc2N2CCOCC2)CN1` |
| M056 | `Cc1nsc(-c2nc(C#N)c3n2CCN(C(=O)c2ccc(Cl)c(F)c2)C3C)n1` |
| M057 | `CC(C)Oc1ccn2c(-c3nc(N[C@H]4CNCC[C@@H]4F)ns3)cnc2c1` |
| M058 | `Cc1nsc(-c2nc(C#N)c3n2CCN(C(=O)c2ccc(F)cc2)[C@@H]3C)n1` |
| M059 | `Cc1cncc(Cn2nc(-c3ccc4oc(N)nc4c3)c3c(N)ncnc32)c1` |
| M060 | `CNCCN(Cc1cccnc1)C(=O)c1cc2cc(Cl)ccc2[nH]1` |

Assay context:

- M051, M052, M057: Manual patch clamp.
- M053: Patch clamp; manual/automated method not specified.
- M054, M059: Automated patch clamp; CHO-hERG; room temperature (19–30 C).
- M055: Automated patch clamp.
- M056, M058: Automated patch clamp; CHO-hERG.
- M060: Automated patch clamp; CHO hERG DUO.
