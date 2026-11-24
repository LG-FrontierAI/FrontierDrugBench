---
bench_id: "SM-087-Cell-Biology-Activity-Prediction"
category: "Cell-Biology"
format: "structured_json"
---
# Prompt

Predict IC50 for suppression of stimulated IL-1beta release in the indicated cell assay. There are 50 distinct molecules. Total: 100 points.

THP-1, human PBMC and mouse macrophage assays are separate contexts. The endpoint is cytokine-release inhibition; it does not establish the absence of cytotoxicity.

Use each molecule's assay context. In the tables below, P denotes its stated IC50, EC50, DC50, qAC50 or CD, expressed in nM. Lower P means greater concentration potency.

## Assay contexts

| Context | Conditions and endpoint |
|---|---|
| C01 | Human THP-1 cells; LPS priming 3 h, compound pretreatment 40 min, then nigericin 40 min; secreted IL-1beta measured by ELISA; inhibition IC50. |
| C02 | Mouse bone-marrow-derived macrophages; LPS/ATP-triggered NLRP3 response; secreted IL-1beta measured by ELISA; inhibition IC50. The source database timing description is internally inconsistent and is not used to assign exact priming duration. |
| C03 | PMA-differentiated human THP-1 cells; LPS priming 3 h, compound 40 min, then nigericin 40 min; IL-1beta release measured by ELISA; IC50. |
| C04 | Human PBMCs; compound preincubation 30 min followed by LPS stimulation for 6 h; IL-1beta secretion measured by MSD; IC50. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `C=CCCC(=O)O[C@@H]1CC[C@]2(C)C[C@H]3OC(=O)C(=C)[C@H]3C[C@H]2C1=C` |
| M002 | C02 | `CC(C)(O)c1coc(S(=O)(=O)NC(=O)Nc2ccccc2C(=O)N2CCOCC2)c1` |
| M003 | C02 | `CN1CCC(N(C)S(=O)(=O)NC(=O)Nc2cccc3c2C(=O)c2ccccc2-3)CC1` |
| M004 | C03 | `Oc1cc(C(F)(F)F)ccc1-c1nnc(N[C@@H]2CCCN(C3CCC3)C2)c2c1C1CCC2CC1` |
| M005 | C01 | `C=C1C(=O)O[C@@H]2C[C@@]3(C)CC[C@@H](NC(=O)c4ccc(C(F)(F)F)cc4)C(=C)[C@@H]3C[C@H]12` |
| M006 | C01 | `C=C1C(=O)O[C@@H]2C[C@@]3(C)CC[C@@H](OC(=O)CCC)C(=C)[C@@H]3C[C@H]12` |
| M007 | C01 | `C=C1C(=O)O[C@@H]2C[C@@]3(C)CC[C@@H](OC(=O)/C=C/C(=O)c4ccc(C)cc4)C(=C)[C@@H]3C[C@H]12` |
| M008 | C03 | `Oc1cc(C(F)(F)F)ccc1-c1nnc(N[C@@H]2CCCNC2)c2c1C1CCC2CC1` |
| M009 | C01 | `C=C1C(=O)O[C@@H]2C[C@@]3(C)CC[C@@H](OC(=O)c4cnc(Cl)cc4Cl)C(=C)[C@@H]3C[C@H]12` |
| M010 | C03 | `[2H]C([2H])([2H])C([2H])([2H])N1CCC[C@@H](Nc2nnc(-c3ccc4occc4c3O)c3c2C2CCC3CC2)C1` |
| M011 | C02 | `O=C(Nc1c2c(cc3c1CCC3)CCC2)NS(=O)(=O)N1CCc2ccccc2C1` |
| M012 | C01 | `C=C1C(=O)O[C@@H]2C[C@@]3(C)CC[C@@H](OC(=O)c4c(Cl)ccnc4Cl)C(=C)[C@@H]3C[C@H]12` |
| M013 | C03 | `CN1C[C@H](F)C[C@@H](Nc2nnc(-c3ccc4occc4c3O)c3c2C2CCC3CC2)C1` |
| M014 | C03 | `Oc1cc(Cl)ccc1-c1nnc(N[C@@H]2CCCN(C3CC(F)(F)C3)C2)c2c1C1CCC2CC1` |
| M015 | C03 | `Oc1cc(C(F)(F)F)ccc1-c1nnc(N[C@@H]2CCCC[C@H]2O)c2c1CCCC2` |
| M016 | C01 | `C=C1C(=O)O[C@@H]2C[C@@]3(C)CC[C@@H](OC(=O)c4ccc(F)nc4)C(=C)[C@@H]3C[C@H]12` |
| M017 | C03 | `Oc1cc(C(F)(F)F)ccc1-c1nnc(N[C@@H]2CCCN(C3CC(F)(F)C3)C2)c2c1C1CCC2C1` |
| M018 | C01 | `C=C1C(=O)O[C@@H]2C[C@@]3(C)CC[C@@H](OC(=O)Cc4ccc5ccccc5c4)C(=C)[C@@H]3C[C@H]12` |
| M019 | C01 | `C=C1C(=O)O[C@@H]2C[C@@]3(C)CC[C@@H](NC(=O)/C=C/C(=O)c4ccccc4)C(=C)[C@@H]3C[C@H]12` |
| M020 | C04 | `COc1ccc(-c2nnc(N[C@@H]3CCCN(C)C3)c3nccn23)c(O)c1` |
| M021 | C02 | `O=C(Nc1c2c(cc3c1CCC3)CCC2)NS(=O)(=O)N1CCN2CCC1CC2` |
| M022 | C02 | `CN1CCC(N(C)S(=O)(=O)NC(=O)Nc2cc(C(C)(C)C)ccc2-c2ccc(C(C)(C)C)cc2)CC1` |
| M023 | C01 | `C=C1C(=O)O[C@@H]2C[C@@]3(C)CC[C@@H](OC(=O)c4cc(Cl)cnc4Cl)C(=C)[C@@H]3C[C@H]12` |
| M024 | C03 | `Oc1cc(C(F)(F)F)ccc1-c1nnc(N[C@@H]2CCCC[C@H]2O)c2c1C1CCC2CC1` |
| M025 | C03 | `Cc1ccc(-c2nnc(N[C@@H]3CCCN(C4CC(F)(F)C4)C3)c3c2C2CCC3CC2)c(O)c1` |
| M026 | C02 | `CN1CCC(n2cc(NS(=O)(=O)NC(=O)Nc3c4c(cc5c3CCC5)CCC4)cn2)CC1` |
| M027 | C02 | `CC(C)(O)c1coc(S(=O)(=O)NC(=O)Nc2ccccc2Cc2ccccc2)c1` |
| M028 | C02 | `O=C(Nc1c2c(cc3c1CCC3)CCC2)NS(=O)(=O)N1CCNC2(CC2)C1` |
| M029 | C03 | `CC(CO)N1CCC[C@@H](Nc2nnc(-c3ccc4occc4c3O)c3c2C2CCC3CC2)C1` |
| M030 | C01 | `C=C1C(=O)O[C@@H]2C[C@@]3(C)CC[C@@H](OC(=O)/C=C/C(=O)OCC)C(=C)[C@@H]3C[C@H]12` |
| M031 | C02 | `C=C(c1ccccc1)c1ccccc1NC(=O)NS(=O)(=O)c1cc(C(C)(C)O)co1` |
| M032 | C02 | `CC(C)(O)c1coc(S(=O)(=O)NC(=O)Nc2ccccc2C(=O)c2ccccc2)c1` |
| M033 | C01 | `C=C1C(=O)O[C@@H]2C[C@@]3(C)CC[C@@H](OC(=O)CCCCC)C(=C)[C@@H]3C[C@H]12` |
| M034 | C01 | `C=C1C(=O)O[C@@H]2C[C@@]3(C)CC[C@@H](OC(=O)CCCCCCC)C(=C)[C@@H]3C[C@H]12` |
| M035 | C04 | `CN1C[C@H](Nc2nnc(-c3ccc(C(F)(F)F)cc3O)c3ccnn23)CC(F)(F)C1` |
| M036 | C04 | `CN1C[C@H](F)C[C@@H](Nc2nnc(-c3ccc(C(F)(F)F)cc3O)c3ccnn23)C1` |
| M037 | C02 | `CN1CCC(NS(=O)(=O)NC(=O)Nc2c3c(cc4c2CCC4)CCC3)CC1` |
| M038 | C02 | `CC(=O)N1CCC(NS(=O)(=O)NC(=O)Nc2c3c(cc4c2CCC4)CCC3)CC1` |
| M039 | C04 | `CN1CCC[C@@H](Nc2nnc(-c3ccc(C(F)(F)F)cc3O)c3c2CCC3)C1` |
| M040 | C04 | `CN1CCC[C@@H](Nc2nnc(-c3ccc(C(F)(F)F)cc3O)c3c2CCCC3)C1` |
| M041 | C03 | `CCN1CCC[C@@H](Nc2nnc(-c3ccc4occc4c3O)c3c2C2CCC3CC2)C1` |
| M042 | C03 | `OCCN1CCC[C@@H](Nc2nnc(-c3ccc4occc4c3O)c3c2C2CCC3CC2)C1` |
| M043 | C04 | `CCN1CCC[C@@H](Nc2nnc(-c3ccc(C(F)(F)F)cc3O)n3ccnc23)C1` |
| M044 | C04 | `CN1C[C@@H](F)C[C@H](Nc2nnc(-c3ccc(C(F)(F)F)cc3O)n3ccnc23)C1` |
| M045 | C04 | `CN1C[C@H](F)C[C@@H](Nc2nnc(-c3ccc(C(F)(F)F)cc3O)n3ccnc23)C1` |
| M046 | C04 | `CN1CCC[C@@H](N(C)c2nnc(-c3ccc(C(F)(F)F)cc3O)n3ccnc23)C1` |
| M047 | C04 | `CN1CCC[C@@H](Nc2nnc(-c3ccc(C(F)(F)F)cc3)n3ccnc23)C1` |
| M048 | C04 | `CN1CCC[C@@H](Nc2nnc(-c3ccc(C(F)(F)F)cc3O)n3ccnc23)C1` |
| M049 | C04 | `Cc1ccc(-c2nnc(N[C@@H]3CCCN(C)C3)c3nccn23)c(O)c1` |
| M050 | C04 | `CN1CCC[C@@H](Nc2nnc(-c3ccccc3O)n3ccnc23)C1` |

## 1. Concentration intervals

| Label | P (nM) |
|---|---|
| L | < 10 |
| M | 10 to < 100 |
| H | >= 100 |

These are assay-specific concentration intervals, not universal clinical or development criteria.

Each correct item earns 2 points (30 items; 60 points).

| Item | Molecule |
|---|---|
| Q001 | M001 |
| Q002 | M002 |
| Q003 | M003 |
| Q004 | M004 |
| Q005 | M005 |
| Q006 | M006 |
| Q007 | M007 |
| Q008 | M008 |
| Q009 | M009 |
| Q010 | M010 |
| Q011 | M011 |
| Q012 | M012 |
| Q013 | M013 |
| Q014 | M014 |
| Q015 | M015 |
| Q016 | M016 |
| Q017 | M017 |
| Q018 | M018 |
| Q019 | M019 |
| Q020 | M020 |
| Q021 | M021 |
| Q022 | M022 |
| Q023 | M023 |
| Q024 | M024 |
| Q025 | M025 |
| Q026 | M026 |
| Q027 | M027 |
| Q028 | M028 |
| Q029 | M029 |
| Q030 | M030 |

## 2. Analogue comparisons

Compare concentration potency within each pair. Define R = P(right)/P(left).

| Answer | Criterion | Interpretation |
|---|---|---|
| A | R > 3 | Left has greater concentration potency |
| B | 1/3 <= R <= 3 | Concentration potencies are within threefold |
| C | R < 1/3 | Right has greater concentration potency |

B is a numerical comparison category, not a claim of statistical equivalence. Each pair uses one assay context.

Each correct item earns 4 points (6 items; 24 points).

| Item | Left molecule | Right molecule |
|---|---|---|
| Q031 | M031 | M032 |
| Q032 | M033 | M034 |
| Q033 | M035 | M036 |
| Q034 | M037 | M038 |
| Q035 | M039 | M040 |
| Q036 | M041 | M042 |

## 3. Within-series ordering

Order each group from lowest to highest P (strongest to weakest concentration potency). All four molecules share one assay context. Use every listed molecule exactly once.

Each group earns 8 * max(0, Spearman rho) points for the submitted versus reference order (2 groups; 16 points).

| Item | Molecules to order |
|---|---|
| Q037 | M043, M044, M045, M046 |
| Q038 | M047, M048, M049, M050 |

## Response format and scoring

Return ONLY one strict JSON object mapping Q001-Q038 to responses: L/M/H for classification, A/B/C for comparisons, and an ordered array of molecule IDs for ordering.

Syntax example only; the values do not imply answers:

`{"Q001": "L", "Q031": "B", "Q037": ["M043", "M044", "M045", "M046"]}`

Missing or invalid items earn zero. An ordering array must contain every listed molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0-1 scale.
