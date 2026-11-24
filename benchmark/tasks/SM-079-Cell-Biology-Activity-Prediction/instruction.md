---
bench_id: "SM-079-Cell-Biology-Activity-Prediction"
category: "Cell-Biology"
format: "structured_json"
---
# Prompt

Predict the concentration causing a 50% reduction in the stated HEK293T viability assay (the source calls this CC50 or viability IC50). There are 50 distinct molecules. Total: 100 points.

Lower concentration means greater viability liability. These readouts do not identify a cell-death mechanism or establish safety.

Use each molecule's assay context. In the tables below, P denotes its stated IC50, EC50, DC50, qAC50 or CD, expressed in nM. Lower P means greater concentration potency; for viability-liability tasks it means a stronger effect on cell viability.

## Assay contexts

| Context | Conditions and endpoint |
|---|---|
| C01 | HEK293T; 48 h exposure; compound:HSA molar ratio 5:1. CC50 from metabolic viability readout (MTS or resazurin; the source does not resolve the readout per molecule). |
| C02 | HEK293T; 72 h compound exposure; MTT viability IC50. |
| C03 | HEK293T; 72 h exposure; CCK-8 growth/viability IC50. |
| C04 | HEK293T; 48 h exposure; MTT viability IC50. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `CCCCCCCCCCCCCSCCCCCCOP(=O)(O)CO[C@H](C)Cn1cnc2c(N)ncnc21.N` |
| M002 | C02 | `COc1cc(NC(C)CCCNC(=O)NCc2cc3c([nH]c4ccccc43)c(C)n2)c2ncccc2c1` |
| M003 | C02 | `COc1cc(NC(C)CCCn2cc(COc3ccc4[nH]c5c(C)nccc5c4c3)nn2)c2ncccc2c1` |
| M004 | C01 | `C#CCCCCCCCCCCCCCCSCCCOP(=O)(O)CO[C@H](C)Cn1cnc2c(N)ncnc21` |
| M005 | C02 | `COc1cc(NC(C)CCCn2cc(-c3cc4c([nH]c5ccccc54)c(C)n3)nn2)c2ncccc2c1` |
| M006 | C03 | `Cl.Cn1cc(CN[C@H]2CC[C@@H](Nc3ncc(C(=O)NO)cn3)CC2)c2ncccc21` |
| M007 | C02 | `COc1cc(NC(C)CCCn2cc(COc3ccc4[nH]c5c(C)nccc5c4c3)nn2)c2ncccc2c1-c1c(OC)cc(NC(C)CCCn2cc(COc3ccc4[nH]c5c(C)nccc5c4c3)nn2)c2ncccc12` |
| M008 | C01 | `CCCCCCCCCCCCCCCCOCCCOP(=O)(O)CO[C@H](C)Cn1cnc2c(N)ncnc21` |
| M009 | C01 | `C[C@H](Cn1cnc2c(N)ncnc21)OCP(=O)(O)OCCCSCCCCCCCCCCCCC#CC(C)(C)C.N` |
| M010 | C01 | `CCCCCCCSCCCCCCCCCCCCOP(=O)(O)CO[C@H](C)Cn1cnc2c(N)ncnc21.N` |
| M011 | C04 | `COc1cc(-c2nc3cc(N4CCOCC4)c(C#Cc4ccccc4F)cc3[nH]2)cc(OC)c1OC` |
| M012 | C01 | `CC(C)[Si](C#CCCCCCCCCCCCSCCCOP(=O)(O)CO[C@H](C)Cn1cnc2c(N)ncnc21)(C(C)C)C(C)C.N` |
| M013 | C01 | `CCCCCCCCCCSCCCCCCCCCOP(=O)(O)CO[C@H](C)Cn1cnc2c(N)ncnc21.N` |
| M014 | C01 | `C[C@H](Cn1cnc2c(N)ncnc21)OCP(=O)(O)OCCCSCCCCCCCCCCCCCCC(C)(C)C.N` |
| M015 | C02 | `COc1ccc2c(c1)[nH]c1c(C)nccc12` |
| M016 | C01 | `C[C@H](Cn1cnc2c(N)ncnc21)OCP(=O)(O)OCCCSCCCCCCCCCCC#Cc1ccccc1.N` |
| M017 | C02 | `COc1cc(NC(C)CCCn2cc(Cn3c4cc(OC)ccc4c4ccnc(C)c43)nn2)c2ncccc2c1` |
| M018 | C01 | `CCCCSCCCCCCCCCCCCCCCOP(=O)(O)CO[C@H](C)Cn1cnc2c(N)ncnc21.N` |
| M019 | C02 | `COc1cc(NC(C)CCCNC(=O)NCCn2c3cc(OC)ccc3c3ccnc(C)c32)c2ncccc2c1` |
| M020 | C03 | `Cl.O=C(NO)c1cnc(N[C@H]2CC[C@@H](NCc3cc4ccccc4s3)CC2)nc1` |
| M021 | C02 | `COc1cc(NC(C)CCCNC(=O)NCCOc2ccc3c(c2)[nH]c2c(C)nccc23)c2ncccc2c1` |
| M022 | C01 | `CCCCCCCCCCCCSCCCOP(=O)(O)CO[C@H](C)Cn1cnc2c(N)ncnc21.N` |
| M023 | C03 | `Cl.Cn1nc(CN[C@H]2CC[C@@H](Nc3ncc(C(=O)NO)cn3)CC2)c2ccccc21` |
| M024 | C04 | `COc1cc(OC)c(-c2nc3cc(N4CCN(C)CC4)c(C#Cc4ccccc4)cc3[nH]2)cc1OC` |
| M025 | C02 | `COc1cc(NC(C)CCCn2cc(COc3ccc4c(c3)[nH]c3c(C)nccc34)nn2)c2ncccc2c1` |
| M026 | C04 | `COc1cc(OC)c(-c2nc3cc(N4CCOCC4)c(C#Cc4ccc(C(F)(F)F)cc4)cc3[nH]2)cc1OC` |
| M027 | C03 | `Cl.Cn1cc(CN[C@H]2CC[C@@H](Nc3ncc(C(=O)NO)cn3)CC2)c2ccccc21` |
| M028 | C03 | `Cl.O=C(NO)c1cnc(N[C@H]2CC[C@@H](NCc3c4ccccc4cc4ccccc34)CC2)nc1` |
| M029 | C02 | `COc1cc(NC(C)CCCN)c2ncccc2c1` |
| M030 | C03 | `Cn1cc(CNCC2CCN(c3ncc(C(=O)NO)cn3)CC2)c2ccccc21` |
| M031 | C04 | `COc1cc(-c2nc3cc(N4CCN(C)CC4)c(C#Cc4ccccc4Cl)cc3[nH]2)cc(OC)c1OC` |
| M032 | C04 | `COc1cc(-c2nc3cc(N4CCOCC4)c(C#Cc4ccccc4Cl)cc3[nH]2)cc(OC)c1OC` |
| M033 | C03 | `Cl.O=C(NO)c1cnc(N[C@H]2CC[C@@H](NCc3cccc4ccncc34)CC2)nc1` |
| M034 | C03 | `Cl.O=C(NO)c1cnc(N[C@H]2CC[C@@H](NCc3cccc4ccccc34)CC2)nc1` |
| M035 | C03 | `Cl.O=C(NO)c1cnc(N[C@H]2CC[C@@H](NCc3ccc4ccccc4c3)CC2)nc1` |
| M036 | C03 | `Cl.O=C(NO)c1cnc(N[C@H]2CC[C@@H](NCc3ccc4ncccc4c3)CC2)nc1` |
| M037 | C02 | `COc1cc(NC(C)CCCNC(=O)NCCOc2ccc3[nH]c4c(C)nccc4c3c2)c2ncccc2c1` |
| M038 | C02 | `COc1cc(NC(C)CCCNC(=O)NCc2nccc3c2[nH]c2ccccc23)c2ncccc2c1` |
| M039 | C01 | `CCCCCCCCCCCCCCCCSCCCOP(=O)(O)CO[C@H](C)Cn1cnc2c(N)ncnc21.N` |
| M040 | C01 | `CCCCCCCCCCCCCCCCCSCCOP(=O)(O)CO[C@H](C)Cn1cnc2c(N)ncnc21.N` |
| M041 | C03 | `Cl.O=C(NO)c1cnc(N[C@H]2CC[C@@H](NCC3CCCC3)CC2)nc1` |
| M042 | C03 | `Cl.O=C(NO)c1cnc(N[C@H]2CC[C@@H](NCC3CCCCC3)CC2)nc1` |
| M043 | C04 | `COc1cc(OC)c(-c2nc3cc(N4CCOCC4)c(C#Cc4ccccc4)cc3[nH]2)cc1OC` |
| M044 | C04 | `COc1cc(OC)c(-c2nc3cc(N4CCOCC4)c(C#Cc4ccccc4Cl)cc3[nH]2)cc1OC` |
| M045 | C04 | `COc1cc(OC)c(-c2nc3cc(N4CCOCC4)c(C#Cc4ccccc4F)cc3[nH]2)cc1OC` |
| M046 | C04 | `COc1cc(OC)c(-c2nc3cc(N4CCOCC4)c(C#Cc4ccc(Cl)cc4)cc3[nH]2)cc1OC` |
| M047 | C04 | `COc1ccc(C#Cc2cc3[nH]c(-c4cc(OC)c(OC)c(OC)c4)nc3cc2N2CCN(C)CC2)cc1` |
| M048 | C04 | `COc1cc(-c2nc3cc(N4CCN(C)CC4)c(C#Cc4ccccc4)cc3[nH]2)cc(OC)c1OC` |
| M049 | C04 | `COc1cc(-c2nc3cc(N4CCOCC4)c(C#Cc4ccccc4)cc3[nH]2)cc(OC)c1OC` |
| M050 | C04 | `COc1cc(-c2nc3cc(N4CCOCC4)c(C#Cc4ccc(Cl)cc4)cc3[nH]2)cc(OC)c1OC` |

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
