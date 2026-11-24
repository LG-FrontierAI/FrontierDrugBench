---
bench_id: "SM-060-In-vivo-Study-ADMET-Classification"
category: "In-vivo-Study"
format: "structured_json"
---
# Prompt

Predict total systemic clearance after intravenous administration under the stated study conditions. This task contains 45 distinct molecules and is worth 100 points.

Predict total IV clearance on the stated blood or plasma basis. This is not intrinsic clearance, unbound clearance, or oral apparent clearance (CL/F).

In an optimization program seeking longer systemic exposure, a reduction in total clearance may be useful. These absolute bins are not hepatic extraction-ratio classes: species, blood/plasma partitioning and nonhepatic elimination matter.

Use the study context assigned to each molecule. PO means oral administration; IV means intravenous administration. Conditions not listed are unspecified.

## Study contexts

| Context | Conditions |
|---|---|
| C01 | dog; Beagle; male. 0.5 mg/kg IV. Matrix: systemic matrix unspecified. Vehicle/formulation: 30%HP-beta-CD/70%water. |
| C02 | rat. 2 mg/kg IV. Matrix: systemic matrix unspecified. |
| C03 | mouse. 25 mg/kg IV. Matrix: plasma. Vehicle/formulation: 10% ethanol + 10% Cremophor EL; remaining vehicle not specified in method. |
| C04 | rat. 2 mg/kg IV. Matrix: plasma. Vehicle/formulation: 10% DMSO/40% PEG400/50% water. |
| C05 | rat; Sprague-Dawley; male. 0.5 mg/kg IV. Matrix: plasma. |
| C06 | rat; Sprague-Dawley; male. 1 mg/kg IV. Matrix: plasma. |
| C07 | rat; Sprague-Dawley. 1 mg/kg IV. Matrix: plasma. |
| C08 | rat; Wistar; male. 0.3 mg/kg IV. Matrix: blood. |
| C09 | rat; Wistar; male. 0.5 mg/kg IV. Matrix: blood. Vehicle/formulation: solution with PEG400/Solutol/EtOH; proportions not specified. |
| C10 | mouse; CD-1; male. 1 mg/kg IV. Matrix: plasma. Cassette dosing. |
| C11 | mouse. 20 mg/kg IV. Matrix: plasma. Vehicle/formulation: 10% ethanol + 10% Cremophor EL; remaining vehicle not specified in method. |
| C12 | mouse; BALB/c; male. 2 mg/kg IV. Matrix: plasma. Vehicle/formulation: 30% Captisol. |
| C13 | rat; Sprague-Dawley; male. 0.1 mg/kg IV cassette. Matrix: plasma. Vehicle/formulation: 10% DMSO in 0.1 M phosphate buffer pH8.5. Cassette dosing. |
| C14 | mouse. 5 mg/kg IV. Matrix: plasma. Vehicle/formulation: 10% ethanol + 10% Cremophor EL; remaining vehicle not specified in method. |
| C15 | dog. 2 mg/kg IV. Matrix: blood. Vehicle/formulation: 20%DMSO/60%PEG400/water. |
| C16 | rat; Wistar; male. 0.5 mg/kg IV. Matrix: blood. |
| C17 | mouse. 3 mg/kg IV. Matrix: systemic matrix unspecified. |
| C18 | rat; Sprague-Dawley; male. 0.5 mg/kg IV. Matrix: systemic matrix unspecified. Vehicle/formulation: 100%DMSO. |
| C19 | rat; Sprague-Dawley; male. 1 mg/kg IV. Matrix: plasma. Feeding: overnight fasted. |
| C20 | mouse. 2 mg/kg IV. Matrix: systemic matrix unspecified. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `CS(=O)(=O)c1cncc(C(=O)N2[C@@H](C(=O)N[C@@H](c3cc(F)c(C(F)(F)F)cc3F)C3CC3)C[C@H]3C[C@H]32)c1` |
| M002 | C02 | `Cc1cc(S(=O)(=O)N[C@H]2C[C@H](N3CCN(CC4CCN(c5cccc6c5n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)CC3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M003 | C03 | `COc1c(OC[C@H]2CCCO2)cc(N2C[C@@H](C)n3c(c(CCCOc4cc(C)c(Cl)c(C)c4)c4ccc(Cl)c(-c5c(C)ncnc5C)c43)C2=O)c2c1cc(C(=O)O)n2C` |
| M004 | C04 | `Nc1cccc2c1C(=O)N(C1CCC(=O)NC1=O)C2=O` |
| M005 | C05 | `O=C1CCc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc2N1` |
| M006 | C06 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3C)c1` |
| M007 | C07 | `C=C(F)C(=O)N[C@H](c1cn2ncc([C@@H](COC)N3C[C@@H](C(F)(F)F)NC3=O)cc2n1)C1CCC(F)(F)CC1` |
| M008 | C07 | `C/C=C(/F)C(=O)N[C@H](c1cn2ncc([C@@H](COC)N3C[C@@H](C(F)(F)F)NC3=O)cc2n1)C1CCC(F)(F)CC1` |
| M009 | C08 | `CC1(CO)CN=C(Nc2cc(F)c(Oc3ccnc4[nH]cc(C(F)(F)F)c34)c(F)c2)OC1` |
| M010 | C02 | `C[C@]1(O)CCCN(c2nc(Nc3ccc(S(=O)(=O)N[C@@H]4CCN(CC5CCN(c6ccc(C7CCC(=O)NC7=O)cc6F)CC5)C[C@H]4F)cc3F)ncc2C(F)(F)F)C1` |
| M011 | C02 | `Cc1cc(S(=O)(=O)N[C@@H](C)CO[C@H]2CC[C@H](CN3CCN(c4ccc5c(c4F)n(C)c(=O)n5C4CCC(=O)NC4=O)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c([C@H]2CC[C@@](C)(O)CC2)n1` |
| M012 | C09 | `COCCCn1cc2cc(NC(=O)c3cccc(C(F)(F)F)n3)c(C(C)(C)O)cc2n1` |
| M013 | C10 | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)Cc2ccccc2)c1=O` |
| M014 | C10 | `CC(C)(C)OC(=O)Nc1cccn([C@@H](CC2CC2)C(=O)N[C@@H](C[C@@H]2CCNC2=O)C(=O)C(=O)NC2CC2)c1=O` |
| M015 | C08 | `Fc1cc(NC2=NC[C@]3(CCOC3)CO2)cc(F)c1Oc1ccnc2[nH]cc(C3(C(F)(F)F)CC3)c12` |
| M016 | C11 | `COc1c(O[C@@H]2CCOC2)cc(N2C[C@@H](C)n3c(c(CCCOc4cc(C)c(Cl)c(C)c4)c4ccc(Cl)c(-c5c(C)nc(C)nc5C)c43)C2=O)c2c1cc(C(=O)O)n2C` |
| M017 | C12 | `C[C@@H]1CN(c2ccc(Cl)nn2)CCN1C(=O)Cc1ccc(C2CC2)cc1` |
| M018 | C13 | `CCc1oc2cccc(I)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M019 | C14 | `COc1c(O[C@H]2CCOC2)cc(N2C[C@@H](C)n3c(c(CCCOc4cc(C)c(Cl)c(C)c4)c4ccc(Cl)c(-c5c(C)nc(C)nc5C)c43)C2=O)c2c1cc(C(=O)O)n2C` |
| M020 | C15 | `COc1c(Cl)cccc1Nc1c(-c2ccncc2C#C[C@@]2(C)CCCN2C(=O)/C=C/CN(C)C)[nH]c2c1C(=O)NCC2` |
| M021 | C12 | `CN(C)c1ccc(CC(=O)N2CCN(c3ccc(Cl)nn3)CC2)cc1` |
| M022 | C11 | `COc1c(OCC2CCOCC2)cc(N2C[C@@H](C)n3c(c(CCCOc4cc(C)c(Cl)c(C)c4)c4ccc(Cl)c(-c5c(C)ncnc5C)c43)C2=O)c2c1cc(C(=O)O)n2C` |
| M023 | C07 | `COC[C@H](c1cnn2cc([C@@H](Nc3nnc(C(C)(F)F)o3)C3CCC(F)(F)CC3)nc2c1)N1C[C@@H](C(F)(F)F)NC1=O` |
| M024 | C06 | `Cc1cc(F)c(C(=O)Nc2cccc(-c3nncn3C(C)C)n2)cc1-n1cnc(C2CC2)c1` |
| M025 | C16 | `OC[C@@]1(F)CN=C(Nc2cc(F)c(Oc3ccnc4[nH]cc(C(F)(F)F)c34)c(F)c2)OC1` |
| M026 | C17 | `Cn1cc(-c2oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c3c2-c2cccc(N)c2)cn1` |
| M027 | C04 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(CCCOC3CCN(C[C@H]4CC[C@H](n5cc(NC(=O)c6cnn7ccc(N8C[C@H]9C[C@@H]8CO9)nc67)c(C(F)F)n5)CC4)CC3)c21` |
| M028 | C18 | `CS(=O)(=O)c1cccc(C(=O)N2[C@@H](C(=O)N[C@@H](c3ccc(C(F)(F)F)cc3F)C3CC3)C[C@H]3C[C@H]32)c1` |
| M029 | C19 | `CC[C@@](N)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ncn(C3CC3)c(=O)c2nn1C` |
| M030 | C06 | `O=C(Nc1cccc(-c2nncn2CC2CC2)n1)c1cc2c(cc1F)OCc1cncn1-2` |
| M031 | C04 | `O=C1CCC(n2c(=O)[nH]c3ccccc32)C(=O)N1` |
| M032 | C06 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3C)n1` |
| M033 | C06 | `O=C(Nc1cccc(-c2nncn2CC2CC2)c1)c1cc2c(cc1F)OCc1cncn1-2` |
| M034 | C20 | `CN1CCN(c2cccc(-c3c(-c4cnn(C)c4)oc4ncnc(Oc5ccc(NC(=O)c6cccn(-c7ccc(F)cc7)c6=O)cc5)c34)c2)CC1` |
| M035 | C20 | `CNc1cccc(-c2c(-c3cnn(C)c3)oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c23)c1` |
| M036 | C06 | `O=C1CCCc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc2N1` |
| M037 | C06 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCC(=O)N3)c1` |
| M038 | C10 | `CC(C)(C)OC(=O)Nc1cccn([C@@H](CC2CC2)C(=O)N[C@@H](C[C@@H]2CCNC2=O)C(=O)C(N)=O)c1=O` |
| M039 | C10 | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)OC(C)(C)C)c1=O` |
| M040 | C03 | `COc1cc(N2C[C@@H](C)n3c(c(CCCOc4cc(C)c(Cl)c(C)c4)c4ccc(Cl)c(-c5c(C)nc(C)nc5C)c43)C2=O)c2c(cc(C(=O)O)n2C)c1OC` |
| M041 | C03 | `COCCOc1cc(N2C[C@@H](C)n3c(c(CCCOc4cc(C)c(Cl)c(C)c4)c4ccc(Cl)c(-c5c(C)nc(C)nc5C)c43)C2=O)c2c(cc(C(=O)O)n2C)c1OC` |
| M042 | C18 | `CS(=O)(=O)c1cccc(C(=O)N2CCC[C@@H]2C(=O)N[C@@H](c2cc(F)c(C(F)(F)F)cc2F)C2CC2)c1` |
| M043 | C18 | `CS(=O)(=O)c1cccc(C(=O)N2CCC[C@@H]2C(=O)N[C@@H](c2ccc(C(F)(F)F)cc2)C2CC2)c1` |
| M044 | C18 | `CS(=O)(=O)c1cccc(C(=O)N2[C@@H](C(=O)N[C@@H](c3ccc(C(F)(F)F)cc3F)C3COC3)C[C@H]3C[C@H]32)c1` |
| M045 | C18 | `CS(=O)(=O)c1cncc(C(=O)N2[C@@H](C(=O)N[C@@H](c3ccc(C(F)(F)F)cc3F)C3CC3)C[C@H]3C[C@H]32)c1` |

## 1. Interval prediction

Assign L, M, or H using the following ranges (mL/min/kg). These are numerical endpoint ranges under the listed animal-study conditions, rather than universal development criteria.

| Label | Interval | Interpretation |
|---|---|---|
| L | value < 10 | Smaller absolute total-clearance range |
| M | 10 <= value < 30 | Intermediate absolute total-clearance range |
| H | value >= 30 | Larger absolute total-clearance range |

Each correct interval item earns 2 points.

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
| Q031 | M031 |
| Q032 | M032 |
| Q033 | M033 |

## 2. Analogue comparisons

Compare total IV clearance. Let R = value(left) / value(right). Choose A if R > 3; B if 1/3 <= R <= 3; C if R < 1/3. Thus A means the left compound clears faster and C means it clears more slowly, on the stated systemic-matrix basis.

Each pair belongs to one literature analogue family and one study context. B denotes only the specified numerical difference category; it does not establish statistical equivalence. No cross-species or cross-dose comparison is requested.

| Item | Left molecule | Right molecule | Points |
|---|---|---|---|
| Q034 | M034 | M035 | 6 |
| Q035 | M036 | M037 | 6 |
| Q036 | M038 | M039 | 6 |
| Q037 | M040 | M041 | 6 |

## 3. Within-series ordering

Order each group from lowest to highest total IV clearance, as a prioritization step for reducing clearance under this study protocol.

Each group shares one study context. Its score is the listed points multiplied by max(0, Spearman rho) between the submitted and reference orders.

| Item | Molecules to order | Points |
|---|---|---|
| Q038 | M042, M043, M044, M045 | 10 |

## Response format and scoring

Return ONLY a strict JSON object mapping each listed Q identifier to L/M/H for interval items, A/B/C for comparisons, or an ordered array of the listed molecule IDs for ordering items.

Syntax example only; these values do not imply answers:

`{"Q001": "L", "Q034": "B", "Q038": ["M042", "M043", "M044", "M045"]}`

Each molecule is assessed in one item. Missing or invalid items earn zero. An ordering array must contain every specified molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0–1 scale.
