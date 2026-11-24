---
bench_id: "SM-080-Cell-Biology-Activity-Prediction"
category: "Cell-Biology"
format: "structured_json"
---
# Prompt

Predict HEK293T viability CC50 or viability IC50 under the indicated assay conditions. There are 50 distinct molecules. Total: 100 points.

A higher viability-effect concentration indicates less viability loss at a given concentration in that assay. Exposure duration and readout remain context-specific.

Use each molecule's assay context. In the tables below, P denotes its stated IC50, EC50, DC50, qAC50 or CD, expressed in nM. Lower P means greater concentration potency; for viability-liability tasks it means a stronger effect on cell viability.

## Assay contexts

| Context | Conditions and endpoint |
|---|---|
| C01 | HEK293T; 24 h exposure; CCK-8 viability CC50. |
| C02 | HEK293T; 48 h exposure; CCK-8 viability CC50. |
| C03 | HEK293T; 48 h exposure; MTT viability CC50. |
| C04 | HEK293T; 72 h exposure; CCK-8 growth/viability IC50. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `CCOc1ccccc1NC(=O)CSc1c(SCC(=O)NCc2ccccc2)[nH]c2ccccc12` |
| M002 | C02 | `CC(C)(C)OC(=O)NCCCC[C@H](NC(=O)OC(C)(C)C)C(=O)NCCCCCCCCCC(=O)Nc1ccc(NC(=S)NC(=O)c2ccc(C(C)(C)C)cc2)cc1` |
| M003 | C03 | `C[C@@H]1[C@H]2C[C@@H](C[C@H]1OC(=O)CCCN1CCCCC1)C2(C)C` |
| M004 | C04 | `Cl.O=C(NO)c1cnc(N[C@H]2CC[C@@H](NCc3ccccc3)CC2)nc1` |
| M005 | C02 | `CC(C)(C)OC(=O)N[C@@H](Cc1c[nH]c2ccccc12)C(=O)Nc1ccc(NC(=S)NC(=O)c2ccc(C(C)(C)C)cc2)cc1` |
| M006 | C02 | `CC(C)(C)OC(=O)N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NCCCCCCCCCCCC(=O)Nc1ccc(NC(=S)NC(=O)c2ccc(C(C)(C)C)cc2)cc1` |
| M007 | C02 | `CC(C)(C)OC(=O)N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NCCCC(=O)Nc1ccc(NC(=S)NC(=O)c2ccc(C(C)(C)C)cc2)cc1` |
| M008 | C01 | `CCOc1ccccc1NC(=O)CSc1c(SCC(=O)NCc2ccccc2C)[nH]c2ccccc12` |
| M009 | C02 | `CC(C)(C)OC(=O)NCCCC[C@H](NC(=O)OC(C)(C)C)C(=O)NCCCCCCC(=O)Nc1ccc(NC(=S)NC(=O)c2ccc(C(C)(C)C)cc2)cc1` |
| M010 | C01 | `O=C(CSc1[nH]c2ccccc2c1SCC(=O)Nc1ccc(Cl)c(Cl)c1)NCc1cccc(Cl)c1` |
| M011 | C02 | `CC(C)(C)OC(=O)NCCCC[C@H](NC(=O)OC(C)(C)C)C(=O)NCCCCCCCCC(=O)Nc1ccc(NC(=S)NC(=O)c2ccc(C(C)(C)C)cc2)cc1` |
| M012 | C01 | `COc1ccccc1CNC(=O)CSc1[nH]c2ccccc2c1SCC(=O)Nc1ccc(Cl)c(Cl)c1` |
| M013 | C04 | `Cl.O=C(NO)c1cnc(N[C@H]2CC[C@@H](NCc3csc4ccccc34)CC2)nc1` |
| M014 | C01 | `CCOc1ccccc1NC(=O)CSc1c(SCC(=O)NCc2ccc(Cl)cc2)[nH]c2ccccc12` |
| M015 | C02 | `CC(C)(C)OC(=O)NCCCC[C@H](NC(=O)OC(C)(C)C)C(=O)NCCCCCCCCCCCC(=O)Nc1ccc(NC(=S)NC(=O)c2ccc(C(C)(C)C)cc2)cc1` |
| M016 | C04 | `Cl.O=C(NO)c1cnc(N[C@H]2CC[C@@H](NCc3ccc4cc(F)ccc4n3)CC2)nc1` |
| M017 | C02 | `CC(C)(C)OC(=O)N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NCCCCCCCC(=O)Nc1ccc(NC(=S)NC(=O)c2ccc(C(C)(C)C)cc2)cc1` |
| M018 | C01 | `O=C(CSc1[nH]c2ccccc2c1SCC(=O)Nc1ccc(Cl)c(Cl)c1)NCc1ccccc1Cl` |
| M019 | C04 | `Cl.O=C(NO)c1cnc(N[C@H]2CC[C@@H](NCc3ccc4ccccc4n3)CC2)nc1` |
| M020 | C04 | `Cl.Cn1cc(CN[C@H]2CC[C@@H](Nc3ncc(C(=O)NO)cn3)CC2)c2ccc(Cl)cc21` |
| M021 | C02 | `CC(C)(C)c1ccc(C(=O)NC(=S)Nc2ccc(NC(=O)CCCCCCCCCN)cc2)cc1` |
| M022 | C02 | `CC(C)(C)OC(=O)N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NCCCCCCCCCCC(=O)Nc1ccc(NC(=S)NC(=O)c2ccc(C(C)(C)C)cc2)cc1` |
| M023 | C01 | `O=C(CSc1[nH]c2ccccc2c1SCC(=O)Nc1ccc(Cl)c(Cl)c1)NCc1ccc(Cl)cc1` |
| M024 | C01 | `O=C(CSc1[nH]c2ccccc2c1SCC(=O)Nc1ccc(Cl)c(Cl)c1)NCc1ccc(Cl)c(Cl)c1` |
| M025 | C04 | `Cl.O=C(NO)c1cnc(N[C@H]2CC[C@@H](NCc3cnc4ccccc4c3)CC2)nc1` |
| M026 | C01 | `O=C(CSc1[nH]c2ccccc2c1SCC(=O)Nc1ccc(Cl)c(Cl)c1)Nc1ccc(Cl)c(Cl)c1` |
| M027 | C04 | `Cl.O=C(NO)c1cnc(N[C@H]2CC[C@@H](NCc3ccc4ccc5cccc6ccc3c4c56)CC2)nc1` |
| M028 | C02 | `NC(=O)c1nc(F)cnc1O` |
| M029 | C04 | `Cl.O=C(NO)c1cnc(N[C@H]2CC[C@@H](NCc3coc4ccccc34)CC2)nc1` |
| M030 | C01 | `CCOc1ccccc1NC(=O)CSc1c(SCC(=O)NCc2cccc(Cl)c2)[nH]c2ccccc12` |
| M031 | C03 | `C[C@@H]1[C@H]2C[C@@H](C[C@H]1OC(=O)CN1CCN(c3ccccc3)CC1)C2(C)C` |
| M032 | C03 | `C[C@@H]1[C@H]2C[C@@H](C[C@H]1OC(=O)CN1CCCCC1)C2(C)C` |
| M033 | C03 | `C[C@@H]1[C@H]2C[C@@H](C[C@H]1OC(=O)CCCN1CCN(C)CC1)C2(C)C` |
| M034 | C03 | `C[C@@H]1[C@H]2C[C@@H](C[C@H]1OC(=O)CN1CCN(C)CC1)C2(C)C` |
| M035 | C04 | `Cc1ccc2c(CN[C@H]3CC[C@@H](Nc4ncc(C(=O)NO)cn4)CC3)cn(C)c2c1.Cl` |
| M036 | C04 | `Cl.O=C(NO)c1cnc(N[C@H]2CC[C@@H](NCc3cc4ccccc4c4ccccc34)CC2)nc1` |
| M037 | C04 | `Cl.Cn1cc(CN[C@H]2CC[C@@H](Nc3ncc(C(=O)NO)cn3)CC2)c2ccc(F)cc21` |
| M038 | C04 | `Cl.Cn1cc(CN[C@H]2CC[C@@H](Nc3ncc(C(=O)NO)cn3)CC2)c2ccc(Br)cc21` |
| M039 | C02 | `CC(C)(C)c1ccc(C(=O)NC(=S)Nc2ccc(N)cc2)cc1` |
| M040 | C02 | `CC(C)(C)c1ccc(C(=O)NC(=S)Nc2ccc(NC(=O)CCCCCCCCN)cc2)cc1` |
| M041 | C01 | `O=C(CSc1[nH]c2ccccc2c1SCC(=O)Nc1ccc(Cl)c(Cl)c1)NCc1ccccc1` |
| M042 | C01 | `O=C(CSc1[nH]c2ccccc2c1SCC(=O)Nc1ccc(Cl)c(Cl)c1)NCc1ccc(-c2ccccc2)cc1` |
| M043 | C03 | `CC1(C)[C@H]2CC[C@](C)(C2)[C@H]1OC(=O)CCN1CCOCC1` |
| M044 | C03 | `CC1(C)[C@H]2CC[C@](C)(C2)[C@H]1OC(=O)CCCN1CCN(c2ccccc2)CC1` |
| M045 | C03 | `CN1CCN(CC(=O)O[C@H]2C(C)(C)[C@H]3CC[C@]2(C)C3)CC1` |
| M046 | C03 | `CC1(C)[C@H]2CC[C@](C)(C2)[C@H]1OC(=O)CN1CCN(c2ccccc2)CC1` |
| M047 | C03 | `CCN1CCN(CCC(=O)O[C@H]2C(C)(C)[C@H]3CC[C@]2(C)C3)CC1` |
| M048 | C03 | `CC1CCN(CCCC(=O)O[C@H]2C(C)(C)[C@H]3CC[C@]2(C)C3)CC1` |
| M049 | C03 | `CC1(C)[C@H]2CC[C@](C)(C2)[C@H]1OC(=O)CCN1CCN(c2ccccc2)CC1` |
| M050 | C03 | `CCN1CCN(CC(=O)O[C@H]2C(C)(C)[C@H]3CC[C@]2(C)C3)CC1` |

## 1. Concentration intervals

| Label | P (nM) |
|---|---|
| L | < 10000 |
| M | 10000 to < 50000 |
| H | >= 50000 |

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

For viability assays, greater potency means stronger viability liability. B is a numerical comparison category, not a claim of statistical equivalence. Each pair uses one assay context.

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
