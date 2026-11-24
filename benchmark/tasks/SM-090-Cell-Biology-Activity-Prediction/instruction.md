---
bench_id: "SM-090-Cell-Biology-Activity-Prediction"
category: "Cell-Biology"
format: "structured_json"
---
# Prompt

Predict viability IC50 in human AsPC-1 pancreatic cancer cells under each stated exposure time and readout. There are 50 distinct molecules. Total: 100 points.

The four source-specific contexts include CCK-8, CellTiter-Glo and MTT readouts; comparisons and ordering stay within one source and assay. Metabolic viability does not uniquely determine cytostatic versus cytotoxic mechanism.

Use each molecule's assay context. In the tables below, P denotes its stated IC50, EC50, DC50, qAC50 or CD, expressed in nM. Lower P means greater concentration potency; for viability-liability tasks it means a stronger effect on cell viability.

## Assay contexts

| Context | Conditions and endpoint |
|---|---|
| C01 | Human AsPC-1 pancreatic cancer cells; 48 h compound exposure; MTT metabolic viability IC50. |
| C02 | Human AsPC-1 pancreatic cancer cells; 7 days compound exposure; CellTiter-Glo luminescent viability IC50. |
| C03 | Human AsPC-1 pancreatic cancer cells; 72 h compound treatment; CCK-8 metabolic viability IC50. |
| C04 | Human AsPC-1 pancreatic cancer cells; 72 h compound treatment; CCK-8 metabolic viability IC50. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `Cc1ccc(/C=C/C(=O)[C@](C)(O)C2CC[C@H]3[C@@H]4CCc5cc(O)ccc5[C@H]4CC[C@]23C)s1` |
| M002 | C02 | `CC[C@H](C)[C@@H]1NC(=O)[C@H](CC(C)C)N(C)C(=O)C[C@@H](C(=O)N2CCCCC2)N(C)C(=O)[C@H](C(C)C)N(C)C(=O)C2(CCCC2)NC(=O)[C@@H]2CCCN2C(=O)[C@H](CCc2ccc(C(F)(F)F)c(Cl)c2)NC(=O)CN(C)C(=O)[C@H](CC2CCCCC2)N(C)C(=O)CN(C)C(=O)CN(C)C1=O` |
| M003 | C03 | `CNS(=O)(=O)Nc1cccc(Oc2cc(=O)n(C)c(Nc3ccc(I)cc3F)c2C(N)=O)c1C` |
| M004 | C04 | `C#CCN(Cc1ccc(S(=O)(=O)NC)cc1)c1ccc(-c2nc3ccccc3s2)cc1` |
| M005 | C01 | `COc1ccc2c(c1)CC[C@@H]1[C@@H]2CC[C@]2(C)C([C@@](C)(O)C(=O)/C=C/c3ccc(Cl)o3)CC[C@@H]12` |
| M006 | C04 | `C#CN(C)S(=O)(=O)c1ccc(CN2CCOCC2)cc1` |
| M007 | C01 | `C[C@](O)(C(=O)/C=C/c1ccc(Cl)o1)C1CC[C@H]2[C@@H]3CCc4cc(O)ccc4[C@H]3CC[C@]12C` |
| M008 | C01 | `C[C@](O)(C(=O)/C=C/c1ccc(Cl)s1)C1CC[C@H]2[C@@H]3CCc4cc(OS(N)(=O)=O)ccc4[C@H]3CC[C@]12C` |
| M009 | C01 | `Nc1ccn([C@@H]2O[C@H](CO)[C@@H](O)C2(F)F)c(=O)n1` |
| M010 | C04 | `C#CCN(Cc1ccc(S(=O)(=O)NC)cc1)c1ccc(C(F)(F)F)cc1` |
| M011 | C04 | `C#CN(C)S(=O)(=O)c1ccc(COc2ccc(N(C)C)cc2)cc1` |
| M012 | C01 | `COc1ccc2c(c1)CC[C@@H]1[C@@H]2CC[C@]2(C)C([C@@](C)(O)C(=O)/C=C/c3cccs3)CC[C@@H]12` |
| M013 | C03 | `CNC(=O)c1c(Oc2cccc(NS(=O)(=O)NC)c2C)cc(=O)n(C)c1Nc1ccc(Br)cc1F` |
| M014 | C02 | `CC[C@H](C)[C@@H]1NC(=O)[C@H](C)N(C)C(=O)C[C@@H](C(=O)n2cccc2)N(C)C(=O)[C@H](CC(C)C)N(C)C(=O)[C@H](Cc2ccccc2)N(C)C(=O)[C@H](Cc2ccccc2)NC(=O)[C@H](Cc2cccc(Cl)c2)NC(=O)CN(C)C(=O)[C@H](Cc2ccc(Cl)cc2)N(C)C(=O)CN(C)C(=O)CN(C)C1=O` |
| M015 | C01 | `C[C@](O)(C(=O)/C=C/c1ccc(Cl)s1)C1CC[C@H]2[C@@H]3CCc4cc(O)ccc4[C@H]3CC[C@]12C` |
| M016 | C02 | `CC[C@H](C)[C@@H]1NC(=O)[C@H](CC(C)C)N(C)C(=O)C[C@@H](C(=O)N2CCCCC2)N(C)C(=O)[C@H](C)N(C)C(=O)C2(CCCC2)NC(=O)[C@@H]2CCCN2C(=O)[C@H](CCc2ccc(C(F)(F)F)c(Cl)c2)NC(=O)CN(C)C(=O)[C@H](CC2CCCCC2)N(C)C(=O)[C@@H]2CCN2C(=O)[C@H](C)N(C)C1=O` |
| M017 | C03 | `CNC(=O)c1c(Oc2cccc(NS(=O)(=O)NC)c2C)cc(=O)n(C)c1Nc1ccc(C2CC2)cc1F` |
| M018 | C04 | `CNS(=O)(=O)c1ccc(CN(C)c2ccc(Cl)cc2)cc1` |
| M019 | C03 | `CCc1ccc(Nc2c(C(=O)NC)c(Oc3cccc(NS(=O)(=O)NC)c3C)cc(=O)n2C)c(F)c1` |
| M020 | C04 | `C#CN(C)S(=O)(=O)c1ccc(CN2CCN(C(=O)OC(C)(C)C)CC2)cc1` |
| M021 | C03 | `CNS(=O)(=O)Nc1cccc(Oc2cc(=O)n(C)c(Nc3ccc(Br)cc3F)c2C(N)=O)c1C` |
| M022 | C02 | `CC[C@H](C)[C@@H]1NC(=O)[C@H](CC2CCCCC2)N(C)C(=O)C[C@@H](C(=O)N2CCCCC2)N(C)C(=O)[C@H](C2CCCCC2)N(C)C(=O)C2(CCCC2)NC(=O)[C@@H]2CCCN2C(=O)[C@H](CCc2ccc(C(F)(F)F)c(Cl)c2)NC(=O)CN(C)C(=O)[C@H](CC2CCCCC2)N(C)C(=O)CN(C)C(=O)CN(C)C1=O` |
| M023 | C04 | `C#CN(C)S(=O)(=O)c1ccc(Cn2ccc3c(Cl)nc(Cl)nc32)cc1` |
| M024 | C03 | `CNC(=O)c1c(Oc2cccc(NS(=O)(=O)NC)c2OC)cc(=O)n(C)c1Nc1ccc(C2CC2)cc1F` |
| M025 | C03 | `CNS(=O)(=O)Nc1cccc(Oc2cc(=O)n(C)c(Nc3ccc(Br)cc3F)c2C(N)=O)c1Cl` |
| M026 | C01 | `COc1ccc2c(c1)CC[C@@H]1[C@@H]2C(=O)C[C@]2(C)C([C@@](C)(O)C(=O)/C=C/c3ccc(C(F)(F)F)cc3)CC[C@@H]12` |
| M027 | C01 | `COc1ccc2c(c1)CC[C@@H]1[C@@H]2CC[C@]2(C)C([C@@](C)(O)C(=O)/C=C/c3ccc(Cl)s3)CC[C@@H]12` |
| M028 | C01 | `C[C@](O)(C(=O)/C=C/c1cccs1)C1CC[C@H]2[C@@H]3CCc4cc(OS(N)(=O)=O)ccc4[C@H]3CC[C@]12C` |
| M029 | C01 | `COc1ccc2c(c1)CC[C@@H]1[C@@H]2[C@H](O)C[C@]2(C)C([C@@](C)(O)C(=O)/C=C/C(C)(C)O)CC[C@@H]12` |
| M030 | C01 | `C[C@](O)(C(=O)/C=C/c1cccs1)C1CC[C@H]2[C@@H]3CCc4cc(O)ccc4[C@H]3CC[C@]12C` |
| M031 | C02 | `CC[C@H](C)[C@@H]1NC(=O)[C@H](CC2CCCC2)N(C)C(=O)C[C@@H](C(=O)N2CCCCC2)N(C)C(=O)[C@H](C(C)C)N(C)C(=O)C2(CCCC2)NC(=O)[C@@H]2CCCN2C(=O)[C@H](CCc2ccc(C(F)(F)F)c(Cl)c2)NC(=O)CN(C)C(=O)[C@H](CC2CCCCC2)N(C)C(=O)CN(C)C(=O)CN(C)C1=O` |
| M032 | C02 | `CC[C@H](C)[C@@H]1NC(=O)[C@H](CC2CCCCC2)N(C)C(=O)C[C@@H](C(=O)N2CCCCC2)N(C)C(=O)[C@H](C(C)C)N(C)C(=O)C2(CCCC2)NC(=O)[C@@H]2CCCN2C(=O)[C@H](CCc2ccc(C(F)(F)F)c(Cl)c2)NC(=O)CN(C)C(=O)[C@H](CC2CCCCC2)N(C)C(=O)CN(C)C(=O)CN(C)C1=O` |
| M033 | C02 | `CC[C@H](C)[C@@H]1NC(=O)[C@H](C2CCCCC2)N(C)C(=O)C[C@@H](C(=O)N2CCCCC2)N(C)C(=O)[C@H](C(C)C)N(C)C(=O)C2(CCCC2)NC(=O)[C@@H]2CCCN2C(=O)[C@H](CCc2ccc(C(F)(F)F)c(Cl)c2)NC(=O)CN(C)C(=O)[C@H](CC2CCCCC2)N(C)C(=O)CN(C)C(=O)CN(C)C1=O` |
| M034 | C02 | `CC[C@H](C)[C@@H]1NC(=O)[C@H](C2CCC2)N(C)C(=O)C[C@@H](C(=O)N2CCCCC2)N(C)C(=O)[C@H](C(C)C)N(C)C(=O)C2(CCCC2)NC(=O)[C@@H]2CCCN2C(=O)[C@H](CCc2ccc(C(F)(F)F)c(Cl)c2)NC(=O)CN(C)C(=O)[C@H](CC2CCCCC2)N(C)C(=O)CN(C)C(=O)CN(C)C1=O` |
| M035 | C02 | `CC[C@H](C)[C@@H]1NC(=O)[C@H](CC(C)C)N(C)C(=O)C[C@@H](C(=O)N2CCCCC2)N(C)C(=O)[C@H](C2CCCC2)N(C)C(=O)C2(CCCC2)NC(=O)[C@@H]2CCCN2C(=O)[C@H](CCc2ccc(C(F)(F)F)c(Cl)c2)NC(=O)CN(C)C(=O)[C@H](CC2CCCCC2)N(C)C(=O)[C@@H]2CCN2C(=O)[C@H](C)N(C)C1=O` |
| M036 | C02 | `CC[C@H](C)[C@@H]1NC(=O)[C@H](CC(C)C)N(C)C(=O)C[C@@H](C(=O)N2CCCCC2)N(C)C(=O)[C@H](C2CCCCC2)N(C)C(=O)C2(CCCC2)NC(=O)[C@@H]2CCCN2C(=O)[C@H](CCc2ccc(C(F)(F)F)c(Cl)c2)NC(=O)CN(C)C(=O)[C@H](CC2CCCCC2)N(C)C(=O)[C@@H]2CCN2C(=O)[C@H](C)N(C)C1=O` |
| M037 | C04 | `C#CCN(Cc1ccc(S(=O)(=O)N(C)C#C)cc1)c1ccc(-c2nc3ccccc3s2)cc1` |
| M038 | C04 | `C#CN(C)S(=O)(=O)c1ccc(CN(Cc2ccccc2)c2ccc(-c3nc4ccccc4s3)cc2)cc1` |
| M039 | C02 | `CC[C@H](C)[C@@H]1NC(=O)[C@H](CC(C)C)N(C)C(=O)C[C@@H](C(=O)N2CCCCC2)N(C)C(=O)[C@H](CC2CCCCC2)N(C)C(=O)C2(CCCC2)NC(=O)[C@@H]2CCCN2C(=O)[C@H](CCc2ccc(C(F)(F)F)c(Cl)c2)NC(=O)CN(C)C(=O)[C@H](CC2CCCCC2)N(C)C(=O)[C@@H]2CCN2C(=O)[C@H](C)N(C)C1=O` |
| M040 | C02 | `CC[C@H](C)[C@@H]1NC(=O)[C@H](CC(C)C)N(C)C(=O)C[C@@H](C(=O)N2CCCCC2)N(C)C(=O)[C@H](CC(C)C)N(C)C(=O)C2(CCCC2)NC(=O)[C@@H]2CCCN2C(=O)[C@H](CCc2ccc(C(F)(F)F)c(Cl)c2)NC(=O)CN(C)C(=O)[C@H](CC2CCCCC2)N(C)C(=O)[C@@H]2CCN2C(=O)[C@H](C)N(C)C1=O` |
| M041 | C03 | `CNS(=O)(=O)Nc1cccc(Oc2cc(=O)n(C)c(Nc3ccc(C4CC4)cc3F)c2C(N)=O)c1Cl` |
| M042 | C03 | `CNC(=O)c1c(Oc2cccc(NS(=O)(=O)NC)c2Cl)cc(=O)n(C)c1Nc1ccc(C2CC2)cc1F` |
| M043 | C03 | `CNS(=O)(=O)Nc1cccc(Oc2cc(=O)n(C)c(Nc3ccc(C4CC4)cc3F)c2C(N)=O)c1C` |
| M044 | C03 | `CCNS(=O)(=O)Nc1cccc(Oc2cc(=O)n(C)c(Nc3ccc(C4CC4)cc3F)c2C(=O)NC)c1C` |
| M045 | C03 | `CNS(=O)(=O)Nc1cccc(Oc2cc(=O)n(C)c(Nc3ccc(C4CC4)cc3F)c2C(=O)NC2CC2)c1C` |
| M046 | C03 | `CNC(=O)c1c(Oc2cccc(NS(=O)(=O)NC)c2F)cc(=O)n(C)c1Nc1ccc(C2CC2)cc1F` |
| M047 | C04 | `C#CN(C)S(=O)(=O)c1ccc(CN(C)c2ccc(Cl)cc2)cc1` |
| M048 | C04 | `C#CN(C)S(=O)(=O)c1ccc(CN(C)c2ccc(-c3ccccc3)cc2)cc1` |
| M049 | C04 | `C#CN(C)S(=O)(=O)c1ccc(CN(C)Cc2ccccc2)cc1` |
| M050 | C04 | `C#CN(C)S(=O)(=O)c1ccc(CN(C)c2ccc(-c3nc4ccccc4s3)cc2)cc1` |

## 1. Concentration intervals

| Label | P (nM) |
|---|---|
| L | < 1000 |
| M | 1000 to < 10000 |
| H | >= 10000 |

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
