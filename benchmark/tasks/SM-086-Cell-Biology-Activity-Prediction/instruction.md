---
bench_id: "SM-086-Cell-Biology-Activity-Prediction"
category: "Cell-Biology"
format: "structured_json"
---
# Prompt

Predict cellular IC50 or author-reported qAC50 for suppression of ERK1/2 phosphorylation in the indicated cancer-cell context. There are 50 distinct molecules. Total: 100 points.

Each comparison and ordering group uses one cell line and assay. The p-ERK endpoint is distinct from biochemical RAS inhibition and long-term viability.

Use each molecule's assay context. In the tables below, P denotes its stated IC50, EC50, DC50, qAC50 or CD, expressed in nM. Lower P means greater concentration potency.

## Assay contexts

| Context | Conditions and endpoint |
|---|---|
| C01 | Human CAPAN-1 pancreatic cancer cells bearing KRAS G12V; 4 h compound exposure; ERK1/2 phosphorylation by AlphaLISA; author-reported geometric-mean qAC50. |
| C02 | AsPC-1 human pancreatic cancer cells bearing KRAS G12D; 2 h compound exposure; p-ERK1/2 MSD immunoassay IC50. |
| C03 | MIA PaCa-2 human pancreatic cancer cells; 2 h compound exposure; p-ERK1/2 MSD immunoassay IC50. |
| C04 | NCI-H358 human lung cancer cells; 2 h compound exposure; p-ERK1/2 Thr202/Thr204 HTRF IC50. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `CCn1c(-c2cc(N3CCN(C)CC3)cnc2[C@H](C)OC)c2c3cc(ccc31)-c1csc(n1)C[C@H](NC(=O)[C@H]1CCO1)C(=O)N1CCC[C@H](N1)C(=O)OCC(C)(C)C2` |
| M002 | C02 | `Nc1nc2c(-c3c(Cl)cc4c(N5CCNCC5)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3F)cccc2s1` |
| M003 | C01 | `CCn1c(-c2cccnc2[C@H](C)OC)c2c3cc(ccc31)-c1csc(n1)C[C@H](NC(=O)[C@H]1CCO1)C(=O)N1CCC[C@H](N1)C(=O)OCC(C)(C)C2` |
| M004 | C02 | `Nc1nc2c(-c3c(Cl)cc4c(N5[C@@H]6CC[C@H]5CNC6)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3Cl)ccc(F)c2s1` |
| M005 | C02 | `CN1CCC[C@H]1COc1nc(N2CCNCC2)c2cc(Cl)c(-c3cccc4sc(N)nc34)c(F)c2n1` |
| M006 | C02 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC(O)CC5)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3F)c12` |
| M007 | C02 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@]6(C5)C[C@@H](O)C6)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3F)c12` |
| M008 | C02 | `Nc1nc2c(-c3c(Cl)cc4c(N5CCNCC5)ncnc4c3F)cccc2s1` |
| M009 | C01 | `CCn1c(-c2cccnc2[C@H](C)OC)c2c3cc(ccc31)-c1cccc(c1)C[C@H](NC(=O)[C@H](C(C)C)N(C)C(C)=O)C(=O)N1CCC[C@H](N1)C(=O)OCC(C)(C)C2` |
| M010 | C02 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@]6(CNC(=O)O6)C5)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3F)c12` |
| M011 | C03 | `C=CC(=O)N1CC2(CCN(c3nc4c(c(-c5cc(O)cc6ccccc56)c3C)COC(C)(C)C4)C2)C1` |
| M012 | C04 | `C=CC(=O)N1CCN(c2c(C#N)c(=O)n(-c3c(C)ccnc3C(C)C)c3nc(-c4c(O)c(Cl)cc(Cl)c4F)c(F)cc23)CC1` |
| M013 | C04 | `C=CC(=O)N1CCN(c2c(C#N)c(=O)n(-c3c(C)ccnc3C(C)C)c3nc(-c4c(O)cccc4F)c(F)cc23)CC1CC#N` |
| M014 | C04 | `C=CC(=O)N1[C@H](C)CN(c2c(C#N)c(=O)n(-c3c(C)ccnc3C(C)C)c3nc(-c4c(O)cccc4F)c(F)cc23)C[C@@H]1C` |
| M015 | C01 | `CCn1c(-c2cccnc2[C@H](C)OC)c2c3cc(ccc31)-c1cccc(c1)C[C@H](NC(=O)[C@H](C(C)C)N(C)C(=O)[C@H]1CCN(C(C)=O)C1)C(=O)N1CCC[C@H](N1)C(=O)OCC(C)(C)C2` |
| M016 | C03 | `C=CC(=O)N1CC2(CCN(c3nc4c(c(N[C@H](CC(=O)NC)CC(C)C)n3)CCCC4)C2)C1` |
| M017 | C03 | `C=CC(=O)N1CC2(CCN(c3nc4c(c(-c5cc(O)cc6ccccc56)c3F)C[C@H]3C[C@@H]4C3(C)C)C2)C1` |
| M018 | C03 | `C=CC(=O)N1CC2(CCN(c3nc4c(c(-c5c(C)ccc6[nH]ncc56)n3)CCC(C)(C)C4)C2)C1` |
| M019 | C03 | `C=CC(=O)N1CC2(CCN(c3nc4c(c(-c5cc(O)cc6ccccc56)c3C#N)C[C@H]3C[C@@H]4C3(C)C)C2)C1` |
| M020 | C04 | `C=CC(=O)N1CCN(c2nc(=O)n(-c3c(C)ccnc3C(C)C)c3nc(-c4c(N)c(F)c(F)c(F)c4F)c(F)cc23)CC1` |
| M021 | C01 | `CCn1c(-c2cccnc2[C@H](C)OC)c2c3cc(ccc31)-c1csc(n1)C[C@H](NC(=O)[C@H]1[C@@H]3COC[C@@H]31)C(=O)N1CCC[C@H](N1)C(=O)OCC(C)(C)C2` |
| M022 | C01 | `CCn1c(-c2cc(N3CCN(CCOC)CC3)cnc2[C@H](C)OC)c2c3cc(ccc31)-c1csc(n1)C[C@H](NC(=O)[C@H]1C[C@@H]1C)C(=O)N1CCC[C@H](N1)C(=O)OCC(C)(C)C2` |
| M023 | C01 | `CCn1c(-c2cc(N3CCN(C)CC3)cnc2[C@H](C)OC)c2c3cc(ccc31)[C@@H]1CCCN(C1)C[C@H](NC(=O)[C@H]1C[C@@H]1C)C(=O)N1CCC[C@H](N1)C(=O)OCC(C)(C)C2` |
| M024 | C02 | `Oc1cc(-c2ncc3c(N4C[C@H]5CC[C@@H](C4)N5)nc(OC[C@@]45CCCN4C[C@H](F)C5)nc3c2F)c2ccccc2c1` |
| M025 | C02 | `Oc1cc(-c2c(F)cc3c(N4C[C@H]5CC[C@@H](C4)N5)nc(OC[C@@]45CCCN4C[C@H](F)C5)nc3c2F)c2ccccc2c1` |
| M026 | C01 | `CCn1c(-c2cc(N3CCN(C)CC3)cnc2[C@H](C)OC)c2c3cc(ccc31)N1CCO[C@@H](C[C@H](NC(=O)[C@H]3C[C@@H]3C)C(=O)N3CCC[C@H](N3)C(=O)OCC(C)(C)C2)C1` |
| M027 | C04 | `C=CC(=O)N1CCN(c2c(C#N)c(=O)n(-c3c(C)ccnc3C(C)C)c3nc(-c4c(O)cccc4F)c(F)cc23)C[C@@H]1C` |
| M028 | C03 | `C=CC(=O)N1CC2(CCN(c3nc4c(c(N[C@H](CC(=O)NC)CC(C)C)n3)CCC(C)(C)C4)C2)C1` |
| M029 | C02 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCCOCC5)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3F)c12` |
| M030 | C02 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCCCC5)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3F)c12` |
| M031 | C01 | `CCn1c(-c2cccnc2[C@H](C)OC)c2c3cc(ccc31)-c1csc(n1)C[C@H](NC(=O)C1CC1)C(=O)N1CCC[C@H](N1)C(=O)OCC(C)(C)C2` |
| M032 | C01 | `CCn1c(-c2cccnc2[C@H](C)OC)c2c3cc(ccc31)-c1csc(n1)C[C@H](NC(=O)[C@H]1C[C@@H]1C)C(=O)N1CCC[C@H](N1)C(=O)OCC(C)(C)C2` |
| M033 | C03 | `C=CC(=O)N1CC2(CCN(c3nc4c(c(-c5cc(O)cc6ccccc56)c3Cl)COC(C)(C)C4)C2)C1` |
| M034 | C03 | `C=CC(=O)N1CC2(CCN(c3nc4c(c(-c5cc(O)cc6ccccc56)c3F)COC(C)(C)C4)C2)C1` |
| M035 | C04 | `C=CC(=O)N1CCN(c2c(C#N)c(=O)n(-c3c(C)ccnc3C(C)C)c3nc(-c4c(N)c(Cl)c(F)c(Cl)c4F)c(Cl)cc23)CC1` |
| M036 | C04 | `C=CC(=O)N1CCN(c2c(C#N)c(=O)n(-c3c(C)ccnc3C(C)C)c3nc(-c4c(N)c(Cl)c(F)c(F)c4F)c(Cl)cc23)CC1` |
| M037 | C04 | `C=CC(=O)N1CCN(c2c(C#N)c(=O)n(-c3c(C)ccnc3C(C)C)c3nc(-c4c(Cl)c(N)c(F)c(F)c4Cl)c(Cl)cc23)CC1` |
| M038 | C04 | `C=CC(=O)N1CCN(c2c(C#N)c(=O)n(-c3c(C)ccnc3C(C)C)c3nc(-c4c(N)c(F)c(F)c(Cl)c4F)c(Cl)cc23)CC1` |
| M039 | C01 | `CCn1c(-c2cccnc2[C@H](C)OC)c2c3cc(ccc31)-c1csc(n1)C[C@H](NC(=O)[C@H](C(C)C)N(C)C(C)=O)C(=O)N1CCC[C@H](N1)C(=O)OCC(C)(C)C2` |
| M040 | C01 | `CCn1c(-c2cccnc2[C@H](C)OC)c2c3cc(ccc31)-c1csc(n1)C[C@H](NC(=O)[C@H](C(C)C)N(C)C(=O)OC)C(=O)N1CCC[C@H](N1)C(=O)OCC(C)(C)C2` |
| M041 | C02 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@@H](O)C5)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3F)c12` |
| M042 | C02 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@H](O)C5)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3F)c12` |
| M043 | C04 | `C=CC(=O)N1CCN(c2c(C#N)c(=O)n(-c3c(C)ccnc3C(C)C)c3nc(-c4c(N)c(Cl)cc(Cl)c4F)c(F)cc23)CC1` |
| M044 | C04 | `C=CC(=O)N1CCN(c2c(C#N)c(=O)n(-c3c(C)ccnc3C(C)C)c3nc(-c4c(F)c(N)c(F)c(F)c4F)c(Cl)cc23)CC1` |
| M045 | C04 | `C=CC(=O)N1CCN(c2c(C#N)c(=O)n(-c3c(C)ccnc3C(C)C)c3nc(-c4c(N)c(Cl)cc(Cl)c4F)c(Cl)cc23)CC1` |
| M046 | C04 | `C=CC(=O)N1CCN(c2c(C#N)c(=O)n(-c3c(C)ccnc3C(C)C)c3nc(-c4c(N)cccc4F)c(F)cc23)CC1` |
| M047 | C03 | `C=CC(=O)N1CC2(CCN(c3nc4c(c(-c5c(C)ccc6[nH]ncc56)n3)CCCC4)C2)C1` |
| M048 | C03 | `C=CC(=O)N1CC2(CCN(c3nc4c(c(-c5c(C)ccc6[nH]ncc56)c3C#N)COC(C)(C)C4)C2)C1` |
| M049 | C03 | `C=CC(=O)N1CC2(CCN(c3nc4c(c(-c5c(C)ccc6[nH]ncc56)c3C#N)CCC(C)C4)C2)C1` |
| M050 | C03 | `C=CC(=O)N1CC2(CCN(c3nc4c(c(-c5c(C)ccc6[nH]ncc56)c3C#N)C[C@H]3C[C@@H]4C3(C)C)C2)C1` |

## 1. Concentration intervals

| Label | P (nM) |
|---|---|
| L | < 100 |
| M | 100 to < 1000 |
| H | >= 1000 |

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
