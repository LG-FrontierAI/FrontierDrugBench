---
bench_id: "SM-035-Molecular-Biology-ADMET-Profile-Prediction"
category: "Molecular-Biology"
format: "structured_json"
---

# Prompt

Predict the experimental CYP inhibition profile for each supplied molecule from the supplied molecular structures. Total: 100 points.
Structures are listed in each question. The same molecule ID always denotes the same structure.
Use the supplied assay context; unreported conditions remain unspecified.
All required inputs are included in this Markdown; inputs/ contains no additional material.
Higher CYP IC50 means weaker inhibition. Enzyme preparations, probes and preincubation conditions can differ between the listed assay contexts; retain those distinctions.

For each molecule, select only its listed CYP isoforms with inhibition IC50 <10 μM; do not select IC50 ≥10 μM. Return [] when no listed isoform meets the cutoff. Each of the 10 molecules earns 10 points only when its complete selection set is correct. Array order does not matter. Do not infer results for unlisted isoforms.

Return ONLY one strict JSON object keyed by the question IDs below. Do not include Markdown fences or explanations.
Unanswered questions or molecules may be omitted or set to null and earn zero. Arrays must contain distinct, valid options.
Unknown question IDs or duplicate JSON keys invalidate the entire response. Unknown molecule IDs in a binning/profile object
make that question score zero; other invalid answers lose only the affected question or molecule points.
The scoring interface returns total points divided by 100, a number from 0 to 1.

## CYP-PROFILE01 (100 points)

For each molecule, select all listed CYP isoforms with inhibition IC50 <10 μM under the specified assay conditions. Only assess that molecule's listed options. Return [] if none are inhibited. Each molecule earns 10 points only when the complete selection set is correct.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M081 | `O=S(=O)(NC1CCCOc2c1nn(-c1ccccc1Cl)c2-c1ccc(Cl)cc1)c1ccc(Cl)cc1` |
| M082 | `COc1cc2c(cc1OCc1ccccc1)N(C(=O)c1cc3cnccc3[nH]1)CC21CCN(C)CC1` |
| M083 | `Cn1ccc(Nc2cc(-c3ccc(CNC(=O)c4nc(C(C)(C)C)no4)c(C(F)(F)F)c3F)ncn2)n1` |
| M084 | `Cn1c2nc(N)ncc2c(=O)n1CC1CCCCC1` |
| M085 | `CN(C[C@H]1Cc2c(cccc2N2C[C@H]3C[C@@H]2CO3)CN1)[C@H]1CCCc2cccnc21` |
| M086 | `CC(=O)N(C[C@H]1CN(c2ccc(N3CCOCC3=O)cc2)C(=O)O1)C(F)(F)F` |
| M087 | `CCCS(=O)(=O)Nc1c(F)ccc(C(=O)c2n[nH]c3ncc(-c4ccncc4)cc23)c1F` |
| M088 | `C[C@@H]1CN(c2cccc3c2C[C@H](CN(C)[C@H]2CCCc4cccnc42)NC3)CCO1` |
| M089 | `CCCS(=O)(=O)Nc1c(F)ccc(C(=O)c2n[nH]c3ncc(-c4cnc(C5CC5)nc4)cc23)c1F` |
| M090 | `COc1cc2cc(C(=O)NCCc3c(C)[nH]c4ccccc34)n(C)c2cn1` |

| Molecule ID | CYP isoform options |
|---|---|
| M081 | CYP1A2, CYP2C9, CYP2C19, CYP2D6, CYP3A4 |
| M082 | CYP2C9, CYP2C19, CYP2D6, CYP3A4 |
| M083 | CYP2C9, CYP3A4 |
| M084 | CYP1A2, CYP2C9, CYP2C19, CYP2D6, CYP3A4 |
| M085 | CYP2D6, CYP3A4 |
| M086 | CYP1A2, CYP2C9, CYP2C19, CYP2D6, CYP3A4 |
| M087 | CYP1A2, CYP2B6, CYP2C8, CYP2C9, CYP2C19, CYP2D6, CYP3A4 |
| M088 | CYP2D6, CYP3A4 |
| M089 | CYP1A2, CYP2B6, CYP2C8, CYP2C9, CYP2C19, CYP2D6, CYP3A4 |
| M090 | CYP2B6, CYP2D6, CYP3A4 |

Isoform-specific assay context:

- M081 (CYP1A2): human liver microsomes 0.2 mg/mL; probe: phenacetin.
- M081 (CYP2C9): human liver microsomes 0.2 mg/mL; probe: diclofenac.
- M081 (CYP2C19): human liver microsomes 0.2 mg/mL; probe: S-mephenytoin.
- M081 (CYP2D6): human liver microsomes 0.2 mg/mL; probe: dextromethorphan.
- M081 (CYP3A4): human liver microsomes 0.2 mg/mL; probe: midazolam.
- M082 (CYP2C9): human liver microsomes, 0.16 mg/mL; probe: diclofenac.
- M082 (CYP2C19): human liver microsomes, 0.5 mg/mL; probe: mephenytoin.
- M082 (CYP2D6): human liver microsomes, 0.16 mg/mL; probe: dextromethorphan.
- M082 (CYP3A4): human liver microsomes, 0.16 mg/mL; probe: midazolam.
- M083 (CYP2C9, CYP3A4): probe: not reported.
- M084 (CYP1A2, CYP2C9, CYP2C19, CYP2D6): probe: not reported.
- M084 (CYP3A4): probe: DEF.
- M085 (CYP2D6): recombinant human CYP2D6 expressed in insect cells; probe: AMMC; preincubation: 30 min.
- M085 (CYP3A4): fluorogenic CYP3A4 assay; enzyme preparation unspecified; probe: fluorogenic probe unspecified.
- M086 (CYP1A2, CYP2C9, CYP2C19, CYP2D6, CYP3A4): CYP inhibition assay; probe: not reported.
- M087 (CYP1A2, CYP2B6, CYP2C8, CYP2C9, CYP2C19, CYP2D6): probe: not reported; no preincubation.
- M087 (CYP3A4): probe: midazolam; no preincubation.
- M088 (CYP2D6): recombinant human CYP2D6 expressed in insect cells; probe: AMMC; preincubation: 30 min.
- M088 (CYP3A4): fluorogenic CYP3A4 assay; enzyme preparation unspecified; probe: fluorogenic probe unspecified.
- M089 (CYP1A2, CYP2B6, CYP2C8, CYP2C9, CYP2C19, CYP2D6): probe: not reported; no preincubation.
- M089 (CYP3A4): probe: midazolam; no preincubation.
- M090 (CYP2B6, CYP2D6): probe: not reported.
- M090 (CYP3A4): probe: midazolam.
