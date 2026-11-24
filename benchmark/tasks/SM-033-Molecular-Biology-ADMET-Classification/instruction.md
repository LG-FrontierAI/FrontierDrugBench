---
bench_id: "SM-033-Molecular-Biology-ADMET-Classification"
category: "Molecular-Biology"
format: "structured_json"
---

# Prompt

Predict inhibition IC50 intervals in the recombinant human CYP2D6/AMMC assay from the supplied molecular structures. Total: 100 points.
Structures are listed in each question. The same molecule ID always denotes the same structure.
Use the supplied assay context; unreported conditions remain unspecified.
All required inputs are included in this Markdown; inputs/ contains no additional material.
Higher CYP IC50 means weaker inhibition. Enzyme preparations, probes and preincubation conditions can differ between the listed assay contexts; retain those distinctions.

Return a bin label for every molecule. Each of the 10 molecules earns 10 points for its correct bin. Bin definitions and units are specified in the question below.

Return ONLY one strict JSON object keyed by the question IDs below. Do not include Markdown fences or explanations.
Unanswered questions or molecules may be omitted or set to null and earn zero. Arrays must contain distinct, valid options.
Unknown question IDs or duplicate JSON keys invalidate the entire response. Unknown molecule IDs in a binning/profile object
make that question score zero; other invalid answers lose only the affected question or molecule points.
The scoring interface returns total points divided by 100, a number from 0 to 1.

## CYP-INTERVAL01 (100 points)

Predict the inhibition IC50 bin for each molecule in the recombinant human CYP2D6/AMMC assay: I1 <1; I2 1–<10; I3 ≥10 μM.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M051 | `NCCCCN(C[C@H]1Cc2cc(Cl)ccc2CN1)[C@H]1CCCc2cccnc21` |
| M052 | `NCCCCN(C[C@H]1Cc2c(cccc2N2CCOCC2)CN1)[C@H]1CCCc2cccnc21` |
| M053 | `CN(C[C@H]1Cc2c(cccc2N2CCOCC2)CN1)[C@H]1CCCc2cccnc21` |
| M054 | `Cc1cnc2c(c1)CCC[C@@H]2N(C)C[C@H]1Cc2c(cccc2N2CCOCC2=O)CN1` |
| M055 | `Cc1cnc(CN(C)C[C@H]2Cc3c(cccc3N3CCOCC3)CN2)c(C)c1` |
| M056 | `NCCCCN(C[C@H]1Cc2c(Br)cccc2CN1)[C@H]1CCCc2cccnc21` |
| M057 | `CCCCN(C[C@H]1Cc2c(cccc2N2CCOCC2)CN1)[C@H]1CCCc2cccnc21` |
| M058 | `NCCCCN(C[C@H]1Cc2c(Cl)cccc2CN1)[C@H]1CCCc2cccnc21` |
| M059 | `NCCCCN(C[C@H]1Cc2c(cccc2N2CCC(F)(F)CC2)CN1)[C@H]1CCCc2cccnc21` |
| M060 | `NCCCCN(C[C@@H]1Cc2c(cccc2N2CCNCC2)CN1)[C@H]1CCCc2cccnc21` |

Assay context (all candidates): Human CYP2D6; probe: AMMC.
