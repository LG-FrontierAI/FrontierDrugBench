---
bench_id: "SM-027-Cell-Biology-ADMET-Classification"
category: "Cell-Biology"
format: "structured_json"
---

# Prompt

Predict experimental Caco-2 efflux ratio (ER) from the supplied molecular structures. Total: 100 points.
Structures are listed in each question. The same molecule ID always denotes the same structure.
Relative comparisons are within the question's candidate group. Use the supplied assay context;
unreported conditions remain unspecified.
All required inputs are included in this Markdown; inputs/ contains no additional material.
ER is the efflux ratio, Papp(B→A)/Papp(A→B).
ER bins: B1 <2; B2 2–<10; B3 10–<50; B4 ≥50.

Answer format and scoring:

- Binning: an object {"molecule_id": "bin"}. Each of the 10 molecules earns 10 points for its correct bin.

Return ONLY one strict JSON object keyed by the question IDs below. Do not include Markdown fences or explanations.
Unanswered questions or molecules may be omitted or set to null and earn zero. Arrays must contain distinct, valid options.
Unknown question IDs or duplicate JSON keys invalidate the entire response. Unknown molecule IDs in a binning object
make that question score zero; other invalid answers lose only the affected question or molecule points.
The scoring interface returns total points divided by 100, a number from 0 to 1.

## ER-I01 (100 points)

Predict the ER bin for each molecule: B1, B2, B3 or B4.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M001 | `CNC(=O)c1c2c(nn1Cc1ccccc1)C(=O)N(Cc1ccccc1)CC2` |
| M002 | `CN1C(=O)[C@@H](N2CCc3c(nn(Cc4ccccc4)c3C(N)=O)C2=O)COc2ccccc21` |
| M003 | `CS(=O)(=O)c1cccc(-c2ccc3nccc(-c4ccc(C(=O)N5CCC(O)C5)cc4)c3n2)c1` |
| M004 | `COc1cc(-c2cncc3c2oc2cc(N4CCN(C)CC4)ccc23)cc(OC)c1OC` |
| M005 | `NS(=O)(=O)c1nnc(NC(=O)CC2[C@H]3C[C@@H]4C[C@@H](C[C@H]2C4)C3)s1` |
| M006 | `Cc1ccc(-c2ccc(F)c3c2C=C(c2ccc(-c4ccc(C(=O)O)cc4)[nH]2)CO3)cc1` |
| M007 | `C/N=S(\c1ccc(C(F)(F)F)cc1)C1CC1` |
| M008 | `Cc1ccc(NC(=O)c2ccc(S(N)(=O)=O)cc2)cc1Nc1nccc(-c2cccnc2)n1` |
| M009 | `Cc1cn2nc(Cl)cc(C(=O)NC34CCCCC(C(=O)Nc5c(C)n(C)n(-c6ccccc6)c5=O)(C3)C4)c2n1` |
| M010 | `Cc1ccc(N2CC3CC(C2)N3C)cc1C(=O)N[C@H](C)c1cc(C#Cc2cnn(C)c2)cc(C2=CCOCC2)c1` |

Assay context:

- M001, M002: HBSS, pH 7.4; 10 μM, 2 h; no efflux inhibitor.
- M003: pH, concentration, duration and efflux-inhibitor conditions not reported.
- M004: Caco-2 C2BBe1; pH 7.4; 5 μM, 37 °C, 2 h; receiver compartment contains 1% BSA; no efflux inhibitor.
- M005: Apical pH 6.5/basolateral pH 7.4; no efflux inhibitor; concentration and duration not reported.
- M006: Measured as the sodium salt; the structure shows the parent free acid. pH, concentration, duration and efflux-inhibitor co-treatment not reported.
- M007, M008: pH 7.2; general method specifies 10 μM, but individual concentrations are not confirmed; no efflux inhibitor.
- M009: pH 7.4; 5 μM, 37 °C, 2 h; no efflux inhibitor. The method includes conditions with and without 1% BSA; the condition for each compound is not specified.
- M010: pH, concentration, duration and efflux-inhibitor co-treatment not reported.
