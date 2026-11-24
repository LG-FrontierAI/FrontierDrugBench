---
bench_id: "SM-085-Cell-Biology-Activity-Prediction"
category: "Cell-Biology"
format: "structured_json"
---
# Prompt

Predict NRF2 nuclear-translocation EC50, NRF2-ARE reporter EC50, or HO-1 induction CD in the indicated cell context. There are 50 distinct molecules. Total: 100 points.

These are distinct cellular pathway readouts. HO-1 CD is the concentration that doubles protein expression; it is not EC50. Each context has explicit interval cutoffs. Comparisons and ordering never mix readouts. Activity does not by itself establish direct KEAP1 binding or therapeutic benefit.

Use each molecule's assay context. In the tables below, P denotes its stated IC50, EC50, DC50, qAC50 or CD, expressed in nM. Lower P means greater concentration potency.

## Assay contexts

| Context | Conditions and endpoint |
|---|---|
| C01 | HEK293 cells transfected with pGL4.37 ARE-luciferase reporter; 24 h compound treatment; NRF2-ARE reporter activation EC50. |
| C02 | Engineered human U2OS PathHunter Keap1-NRF2 nuclear-translocation cells; 6 h compound treatment at room temperature; enzyme-complementation chemiluminescence EC50. |
| C03 | Human PathHunter U2OS Keap1-NRF2 nuclear-translocation cells; 3 h treatment; enzyme-complementation luminescence; NRF2 translocation EC50. |
| C04 | Human renal mesangial cells (HRMCs); 18 h compound treatment; HO-1 protein measured by ELISA. Endpoint CD is the concentration that doubles HO-1 expression, not a half-maximal EC50. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `COc1cc(C(CC(=O)O)c2cccc3c2CCN(C(=O)c2ccc(C(F)(F)F)cc2Cl)C3)cc2nnn(C)c12` |
| M002 | C01 | `CCCCOc1ccc(C(=O)N2CCc3c(cccc3C(CC(=O)O)c3cc(OC)c4c(c3)nnn4C)C2)c(Cl)c1` |
| M003 | C01 | `COc1cc(C(CC(=O)O)c2cccc3c2CCN(C(=O)c2ccc(OCC4CC4)cc2Cl)C3)cc2nnn(C)c12` |
| M004 | C02 | `COc1ccccc1[Se](=O)(=O)/C=C/c1ccccc1C(F)(F)F` |
| M005 | C03 | `CCS(=O)(=O)c1nc(S(=O)(=O)c2ccc(C)cc2Cl)c(N2CCN(C)C(=O)C2)s1` |
| M006 | C04 | `CCCOc1cc([C@@H](NC(=O)Cc2ccc(C)cc2)[C@@H](C)C(=O)O)ccc1C` |
| M007 | C02 | `COc1ccccc1/C=C/[Se](=O)(=O)c1ccccc1OC` |
| M008 | C03 | `C=Cc1nc(S(=O)(=O)c2ccccc2Cl)c(N2CCN(C)C(=O)C2)s1` |
| M009 | C02 | `COc1ccccc1[Se](=O)(=O)/C=C/c1ccccc1OC(F)(F)F` |
| M010 | C01 | `COc1cc([C@H](CC(=O)O)c2cccc3c2CCN(C(=O)c2ccc(OC(C)C)cc2Cl)C3)cc2nnn(C)c12` |
| M011 | C02 | `O=[Se](=O)(/C=C/c1ncccc1F)c1cccc(Cl)c1` |
| M012 | C01 | `COc1cc(C(CC(=O)O)c2cccc3c2CCN(C(=O)c2ccccc2Cl)C3)cc2nnn(C)c12` |
| M013 | C01 | `COc1ccc(C(=O)N2CCc3c(cccc3C(CC(=O)O)c3cc(OC)c4c(c3)nnn4C)C2)c(F)c1` |
| M014 | C03 | `CCP1(=O)CCN(c2sc(S(=O)(=O)CC)nc2S(=O)(=O)c2cccc(Cl)c2Cl)CC1` |
| M015 | C04 | `Cc1ccc([C@@H](NC(=O)Cc2ccc(CC3CCCCC3)cc2)[C@@H](C)C(=O)O)cc1` |
| M016 | C02 | `O=[Se](=O)(/C=C/c1ncccc1C(F)(F)F)c1ccccc1F` |
| M017 | C03 | `CCS(=O)(=O)c1nc(S(=O)(=O)c2ccccc2Cl)c(N2CCn3nc(C)nc3C2)s1` |
| M018 | C04 | `Cc1ccc([C@@H](NC(=O)Cc2ccc(Cc3cc(C)ccn3)cc2)[C@@H](C)C(=O)O)cc1.Cl` |
| M019 | C03 | `CCS(=O)(=O)c1nc(S(=O)(=O)c2ccc(C)cc2)c(N2CCN(C)C(=O)C2)s1` |
| M020 | C01 | `COc1cc([C@@H](CC(=O)O)c2cccc3c2CCN(C(=O)c2ccc(OC(C)C)cc2Cl)C3)cc2nnn(C)c12` |
| M021 | C03 | `CN1CCN(c2sc(S(=O)(=O)CCO)nc2S(=O)(=O)c2ccccc2Cl)CC1=O` |
| M022 | C04 | `CCOc1cccnc1Cc1ccc([C@H](F)C(=O)N[C@H](c2ccc(C)cc2)[C@@H](C)C(=O)O)cc1` |
| M023 | C01 | `COc1ccc(C(=O)N2CCc3c(cccc3C(CC(=O)O)c3cc(OC)c4c(c3)nnn4C)C2)cc1Cl` |
| M024 | C03 | `CCS(=O)(=O)c1nc(S(=O)(=O)c2ccccc2Cl)c(N2CCP(C)(=O)CC2)s1` |
| M025 | C02 | `COc1ccc([Se](=O)(=O)/C=C/c2ccccc2OC)cc1` |
| M026 | C03 | `CCS(=O)(=O)c1nc(S(=O)(=O)c2ccccc2Cl)c(N2CC3(CC3)C2)s1` |
| M027 | C01 | `COc1cc(Cl)ccc1C(=O)N1CCc2c(cccc2C(CC(=O)O)c2cc(OC)c3c(c2)nnn3C)C1` |
| M028 | C01 | `COc1cc(C(CC(=O)O)c2cccc3c2CCN(C(=O)c2ccc(C#N)cc2Cl)C3)cc2nnn(C)c12` |
| M029 | C02 | `O=[Se](=O)(/C=C/c1ncccc1C(F)(F)F)c1ccccc1Cl` |
| M030 | C03 | `CCN(CC(=O)NC)c1sc(S(=O)(=O)CC)nc1S(=O)(=O)c1ccccc1Cl` |
| M031 | C03 | `CCS(=O)(=O)c1nc(S(=O)(=O)c2ccc(Cl)cc2C)c(N2CCN(C)C(=O)C2)s1` |
| M032 | C03 | `CCS(=O)(=O)c1nc(S(=O)(=O)c2cc(Cl)ccc2Cl)c(N2CCN(C)C(=O)C2)s1` |
| M033 | C03 | `CN1CCN(c2sc(S(=O)(=O)C3CC3)nc2S(=O)(=O)c2ccccc2Cl)CC1=O` |
| M034 | C03 | `CN1CCN(c2sc(S(=O)(=O)C3CCC3)nc2S(=O)(=O)c2ccccc2Cl)CC1=O` |
| M035 | C01 | `COc1ccc(Cl)c(C(=O)N2CCc3c(cccc3C(CC(=O)O)c3cc(OC)c4c(c3)nnn4C)C2)c1` |
| M036 | C01 | `COc1cc(C(CC(=O)O)c2cccc3c2CCN(C(=O)c2ccc(OC(C)C)cc2Cl)C3)cc2nnn(C)c12` |
| M037 | C02 | `O=[Se](=O)(/C=C/c1ncccc1Cl)c1ccc(Cl)cc1` |
| M038 | C02 | `O=[Se](=O)(/C=C/c1ncccc1Cl)c1ccc(F)cc1` |
| M039 | C04 | `Cc1ccc(CC(=O)N[C@H](c2ccc(C)c(OCC3CCCCC3)c2)[C@@H](C)C(=O)O)cc1` |
| M040 | C04 | `Cc1ccc(CC(=O)N[C@H](c2ccc(C)c(OCC3CCCC3)c2)[C@@H](C)C(=O)O)cc1` |
| M041 | C04 | `Cc1ccc(CC(=O)N[C@H](c2ccc(C)c(OCC(C)(C)F)c2)[C@@H](C)C(=O)O)cc1` |
| M042 | C04 | `Cc1ccc(CC(=O)N[C@H](c2ccc(C)c(OCC(C)(C)O)c2)[C@@H](C)C(=O)O)cc1` |
| M043 | C04 | `Cc1ccc([C@@H](NC(=O)Cc2ccc(Cc3ccccc3)cc2)[C@@H](C)C(=O)O)cc1` |
| M044 | C04 | `Cc1ccc([C@@H](NC(=O)Cc2ccc(Cc3ccccn3)cc2)[C@@H](C)C(=O)O)cc1.Cl` |
| M045 | C04 | `Cc1ccc([C@@H](NC(=O)Cc2ccc(Cc3ncccc3C)cc2)[C@@H](C)C(=O)O)cc1.Cl` |
| M046 | C04 | `CCOc1cccnc1Cc1ccc(CC(=O)N[C@H](c2ccc(C)cc2)[C@@H](C)C(=O)O)cc1` |
| M047 | C02 | `COc1ccccc1[Se](=O)(=O)/C=C/c1ccccc1Cl` |
| M048 | C02 | `O=[Se](=O)(/C=C/c1ccccc1F)c1ccccc1Cl` |
| M049 | C02 | `COc1ccccc1/C=C/[Se](=O)(=O)c1ccccc1Cl` |
| M050 | C02 | `O=[Se](=O)(/C=C/c1ccccc1C(F)(F)F)c1ccccc1Cl` |

## 1. Concentration intervals

| Label | P (nM) |
|---|---|
| L | < 100 |
| M | 100 to < 1000 |
| H | >= 1000 |

These are assay-specific concentration intervals, not universal clinical or development criteria.

Context-specific exception: use the following cutoffs instead of the general table for these contexts.

| Context | L | M | H |
|---|---|---|---|
| C01 | P < 1000 nM | 1000 <= P < 10000 nM | P >= 10000 nM |
| C04 | P < 1000 nM | 1000 <= P < 10000 nM | P >= 10000 nM |

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
