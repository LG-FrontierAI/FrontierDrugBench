---
bench_id: "SM-030-Cell-Biology-ADMET-Comparison"
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

Answer format and scoring:

- Top2: an array of exactly two distinct molecule IDs. Each correct selection earns half the question points; order does not matter.
- Pair: one molecule ID string. A correct choice earns all question points.
- Ranking: an array containing every candidate ID exactly once, in the stated direction. Points equal the fraction of correct scored pairwise relations.

Top2, pairwise comparison and ranking each contribute exactly 100/3 points across their questions. Fractional question allocations below are exact; no rounding is applied to scoring.

Return ONLY one strict JSON object keyed by the question IDs below. Do not include Markdown fences or explanations.
Unanswered questions or molecules may be omitted or set to null and earn zero. Arrays must contain distinct, valid options.
Unknown question IDs or duplicate JSON keys invalidate the entire response. Unknown molecule IDs in a binning object
make that question score zero; other invalid answers lose only the affected question or molecule points.
The scoring interface returns total points divided by 100, a number from 0 to 1.

## Papp-T01 (25/3 points)

Select the TWO molecules with the highest Papp; their internal order does not matter.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M011 | `Cc1ccc(NC(=O)c2ccc(S(=O)(=O)N(C)C)cc2)cc1Nc1nccc(-c2cccnc2)n1` |
| M012 | `Cc1ccc(NC(=O)c2ccc(S(C)(=O)=O)cc2)cc1Nc1nccc(-c2cccnc2)n1` |
| M031 | `Cc1ccc(NC(=O)c2ccc(S(C)(=N)=O)cc2)cc1Nc1nccc(-c2cccnc2)n1` |
| M069 | `Cc1ccc(NC(=O)c2ccc(S(C)=O)cc2)cc1Nc1nccc(-c2cccnc2)n1` |
| M070 | `Cc1ccc(NC(=O)c2ccc(/S(=N/C(=O)C(C)(C)C)C3CC3)cc2)cc1Nc1nccc(-c2cccnc2)n1` |

Assay context (all candidates): pH 7.2; general method specifies 10 μM, but individual concentrations are not confirmed; no efflux inhibitor.

## Papp-T02 (25/3 points)

Select the TWO molecules with the highest Papp; their internal order does not matter.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M009 | `Cc1cn2nc(Cl)cc(C(=O)NC34CCCCC(C(=O)Nc5c(C)n(C)n(-c6ccccc6)c5=O)(C3)C4)c2n1` |
| M035 | `Cc1cc2cc(Cl)cc(C(=O)NC34CCCCC(C(=O)Nc5c(C)n6n(c5=O)-c5ccccc5OCC6)(C3)C4)c2o1` |
| M036 | `Cc1cc2cc(Cl)cc(C(=O)NC34CCCC(C(=O)Nc5c(C)n6n(c5=O)-c5ccccc5OCC6)(C3)C4)c2o1` |
| M071 | `Cc1cc2cc(Cl)cc(C(=O)NC34CCCCC(C(=O)Nc5c(C)n(C)n(-c6ccccc6)c5=O)(C3)C4)c2o1` |
| M072 | `Cc1cc2cc(Cl)cc(C(=O)NC34CCC(C(=O)Nc5c(C)n6n(c5=O)-c5ccccc5OCC6)(C3)C4)c2o1` |

Assay context (all candidates): pH 7.4; 5 μM, 37 °C, 2 h; no efflux inhibitor. The method includes conditions with and without 1% BSA; the condition for each compound is not specified.

## Papp-T03 (25/3 points)

Select the TWO molecules with the highest Papp; their internal order does not matter.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M001 | `CNC(=O)c1c2c(nn1Cc1ccccc1)C(=O)N(Cc1ccccc1)CC2` |
| M002 | `CN1C(=O)[C@@H](N2CCc3c(nn(Cc4ccccc4)c3C(N)=O)C2=O)COc2ccccc21` |
| M038 | `NC(=O)c1c2c(nn1Cc1ccccc1)C(=O)N(C(CCO)c1ccccc1)CC2` |
| M073 | `O=C1c2nn(Cc3ccccc3)c(-c3nnco3)c2CCN1Cc1ccccc1` |
| M074 | `NC(=O)c1c2c(nn1Cc1ccccc1)C(=O)N(Cc1ccccc1)CC2` |

Assay context (all candidates): HBSS, pH 7.4; 10 μM, 2 h; no efflux inhibitor.

## Papp-T04 (25/3 points)

Select the TWO molecules with the highest Papp; their internal order does not matter.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M026 | `Cn1c(=O)oc2cc(-n3cc(C(=O)O)c(=O)n([C@@H]4CCc5c4cccc5C(F)(F)F)c3=O)ccc21` |
| M027 | `Cn1c(=O)n(C)c2cc(-n3cc(C(=O)O)c(=O)n([C@@H]4CCc5c4cccc5C(F)(F)F)c3=O)ccc21` |
| M028 | `Cc1c(Cn2c(=O)c(C(=O)O)cn(-c3ccc(N4CCNC4=O)cc3)c2=O)cccc1C(F)(F)F` |
| M029 | `COc1ccc(-n2cc(C(=O)O)c(=O)n(Cc3cccc(C(F)(F)F)c3C)c2=O)cc1` |
| M030 | `Cc1c(Cn2c(=O)c(C(=O)O)cn(-c3ccc4c(c3)n(C)c(=O)n4C)c2=O)cccc1C(F)(F)F` |

Assay context (all candidates): pH 7.2; 2 μM, 37 °C, 2 h; 1.25% DMSO; no efflux inhibitor.

## Papp-P01 (10/3 points)

Select the molecule with the higher Papp.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M075 | `Cc1ccc(S(=N)C2CC2)cc1` |
| M076 | `Cc1ccc(/S(=N\C(=O)C(C)(C)C)C2CC2)cc1` |

Assay context (all candidates): pH 7.2; general method specifies 10 μM, but individual concentrations are not confirmed; no efflux inhibitor.

## Papp-P02 (10/3 points)

Select the molecule with the higher Papp.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M018 | `C[C@H]1CN(C)CCCN1c1nccc(-c2noc([C@@]3(C)CCCc4sc(N)c(C#N)c43)n2)n1` |
| M019 | `C[C@H]1CNCCCN1c1nccc(-c2noc([C@@]3(C)CCCc4sc(N)c(C#N)c43)n2)n1` |

Assay context (all candidates): pH, concentration, duration and efflux-inhibitor conditions not reported.

## Papp-P03 (10/3 points)

Select the molecule with the higher Papp.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M024 | `Cc1c(NC(=O)CC(C)(C)CNC(=O)c2cc(Cl)cc3cc(C(F)F)oc23)c(=O)n2n1CCOc1ccccc1-2` |
| M025 | `Cc1nc2cc(Cl)cc(C(=O)NCC(C)(C)CC(=O)Nc3c(C)n4n(c3=O)-c3ccccc3OCC4)c2o1` |

Assay context (all candidates): pH 7.4; 5 μM, 37 °C, 2 h; no efflux inhibitor. The method includes conditions with and without 1% BSA; the condition for each compound is not specified.

## Papp-P04 (10/3 points)

Select the molecule with the higher Papp.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M077 | `NC(=O)c1c2c(nn1Cc1ccccc1)C(=O)N(CCOc1ccccc1)CC2` |
| M078 | `COCCN1CCc2c(nn(Cc3ccccc3)c2C(N)=O)C1=O` |

Assay context (all candidates): HBSS, pH 7.4; 10 μM, 2 h; no efflux inhibitor.

## Papp-P05 (10/3 points)

Select the molecule with the higher Papp.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M039 | `NS(=O)(=O)c1nnc(NC(=O)CCC2CC3CCC2C3)s1` |
| M040 | `NS(=O)(=O)c1nnc(NC(=O)CCC2CCC(F)(F)CC2)s1` |

Assay context (all candidates): Apical pH 6.5/basolateral pH 7.4; no efflux inhibitor; concentration and duration not reported.

## Papp-P06 (10/3 points)

Select the molecule with the higher Papp.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M079 | `CSc1ccccc1[C@H]1CCCN1C(=O)CNC(=O)N(Cc1cnc(N)nc1)Cc1ncc(C)s1` |
| M080 | `CSc1ccccc1[C@H]1CCCN1C(=O)CNC(=O)N(Cc1ccc(N)c(Cl)c1)Cc1nnn(C)n1` |

Assay context (all candidates): pH, concentration, duration and efflux-inhibitor conditions not reported.

## Papp-P07 (10/3 points)

Select the molecule with the higher Papp.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M043 | `Cc1cccnc1-c1csc(C(=O)Nc2cc(Cl)cc(NS(C)(=O)=O)c2)c1` |
| M044 | `CS(=O)(=O)Nc1cc(Br)cc(NC(=O)c2cc(-c3ccccc3)cs2)c1` |

Assay context (all candidates): pH, concentration, duration and efflux-inhibitor conditions not reported.

## Papp-P08 (10/3 points)

Select the molecule with the higher Papp.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M046 | `CC(C)C[C@@H]1NC(=O)[C@@H](N(C)C(=O)[C@@H](NC(=O)[C@@H]2C[C@@H](F)CN2C(=O)C2(C(F)(F)F)CC3(CCC3)C2)C2CC2)CCCCNC(=O)C(C)(C)NC(=O)[C@H](Cc2cc(Cl)ccc2Cl)N(C)C1=O` |
| M081 | `CC(C)C[C@@H]1NC(=O)[C@@H](N(C)C(=O)[C@@H](NC(=O)[C@@H]2C[C@@H](F)CN2C(=O)C2(C(F)(F)F)CC2)C2CC2)CCCCNC(=O)C(C)(C)NC(=O)[C@H](Cc2cc(Cl)ccc2Cl)N(C)C1=O` |

Assay context (all candidates): 10 μM, 37 °C, 1 h; HBSS/5 mM HEPES; no efflux inhibitor; pH not reported.

## Papp-P09 (10/3 points)

Select the molecule with the higher Papp.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M047 | `Cc1ccc(N2CCN(C)CC2)cc1C(=O)NC1(c2cc(C#Cc3cnn(C)c3)cc(-c3cnn(C)c3)c2)CC1` |
| M048 | `Cc1ccc(N2CCN(C)CC2)cc1C(=O)N[C@H](C)c1cc(C#Cc2cnn(C)c2)cc(-c2cnn(C)c2)c1` |

Assay context (all candidates): pH, concentration, duration and efflux-inhibitor co-treatment not reported.

## Papp-P10 (10/3 points)

Select the molecule with the higher Papp.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M082 | `COc1cc(-c2cncc3c2COCc2cc(N4CCN(C)CC4)ccc2-3)cc(OC)c1OC` |
| M083 | `COc1cc(-c2cncc3c2COCc2cc(N4CCNCC4)ccc2-3)cc(OC)c1OC` |

Assay context (all candidates): Caco-2 C2BBe1; pH 7.4; 5 μM, 37 °C, 2 h; receiver compartment contains 1% BSA; no efflux inhibitor.

## Papp-R01 (50/3 points)

Rank all molecules from highest to lowest Papp.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M084 | `CCS(=N)c1ccc(C(F)(F)F)cc1` |
| M085 | `CC(C)(C)C(=O)/N=S(\c1ccc(C(F)(F)F)cc1)C1CCC1` |
| M086 | `CS(=O)c1ccc(C(F)(F)F)cc1` |
| M087 | `N=S(c1ccc(C(F)(F)F)cc1)C1CC1` |
| M088 | `CS(=N)c1ccc(C(F)(F)F)cc1` |

Assay context (all candidates): pH 7.2; general method specifies 10 μM, but individual concentrations are not confirmed; no efflux inhibitor.

## Papp-R02 (50/3 points)

Rank all molecules from highest to lowest Papp.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M021 | `Cc1cc2cc(Cl)cc(C(=O)NCC(C)(C)CC(=O)Nc3cn4n(c3=O)-c3ccccc3OCC4)c2o1` |
| M056 | `Cc1cc2cc(Cl)cc(C(=O)NCC(C)(C)CC(=O)Nc3c(C)nn4c3OCCOc3ccccc3-4)c2o1` |
| M058 | `Cc1c(NC(=O)CC(C)(C)CNC(=O)c2cc(Cl)cc3ccoc23)c(=O)n2n1CCOc1ccccc1-2` |
| M059 | `Cc1cc2cc(Cl)cc(C(=O)NCC(C)(C)CC(=O)Nc3c(C)n4n(c3=O)-c3ccccc3OCC4)c2o1` |
| M060 | `Cc1cc2cc(Cl)cc(C(=O)NCC(C)(O)CC(=O)Nc3c(C)n4n(c3=O)-c3ccccc3OCC4)c2o1` |

Assay context (all candidates): pH 7.4; 5 μM, 37 °C, 2 h; no efflux inhibitor. The method includes conditions with and without 1% BSA; the condition for each compound is not specified.
