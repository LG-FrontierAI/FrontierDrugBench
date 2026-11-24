---
bench_id: "SM-059-In-vivo-Study-ADMET-Classification"
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
| C01 | rat. 2 mg/kg IV. Matrix: plasma. Vehicle/formulation: 10% DMSO/40% PEG400/50% water. |
| C02 | rat; Sprague-Dawley; male. 1 mg/kg IV. Matrix: plasma. Feeding: overnight fasted. |
| C03 | rat; Wistar; male. 0.4 mg/kg IV. Matrix: blood. |
| C04 | mouse; BALB/c; male. 2 mg/kg IV. Matrix: plasma. Vehicle/formulation: 30% Captisol. |
| C05 | mouse. 2 mg/kg IV. Matrix: systemic matrix unspecified. |
| C06 | rat; Wistar; male. 0.5 mg/kg IV. Matrix: blood. Vehicle/formulation: solution with PEG400/Solutol/EtOH; proportions not specified. |
| C07 | dog; Beagle; female. 0.5 mg/kg IV 10min infusion. Matrix: blood. Vehicle/formulation: water/PEG400/EtOH 50/40/10. |
| C08 | rat; Sprague-Dawley. 1 mg/kg IV. Matrix: plasma. Vehicle/formulation: DMSO. Feeding: fed. |
| C09 | mouse; ICR. 2.0 mg/kg IV. Matrix: plasma. Vehicle/formulation: 5%DMSO+10%solutol+85%saline. |
| C10 | dog; Beagle. 0.5 mg/kg IV. Matrix: plasma. Vehicle/formulation: 20% DMSO + 60% PEG400 + water. |
| C11 | rat; Wistar; male. IV; dose unspecified. Matrix: blood. Vehicle/formulation: unspecified. |
| C12 | mouse. 25 mg/kg IV. Matrix: plasma. Vehicle/formulation: 10% ethanol + 10% Cremophor EL; remaining vehicle not specified in method. |
| C13 | rat. 2 mg/kg IV. Matrix: systemic matrix unspecified. |
| C14 | dog; Beagle; male. 0.5 mg/kg IV. Matrix: systemic matrix unspecified. Vehicle/formulation: 30%HP-beta-CD/70%water. |
| C15 | rat; Sprague-Dawley; male. 1 mg/kg IV. Matrix: plasma. |
| C16 | rat; Sprague-Dawley. 1 mg/kg IV. Matrix: plasma. |
| C17 | dog; Beagle; female. 0.3 mg/kg IV infusion. Matrix: systemic matrix unspecified. |
| C18 | mouse; CD1. 1 mg/kg IV. Matrix: plasma. Vehicle/formulation: DMSO. |
| C19 | mouse; CD-1; male. 1 mg/kg IV. Matrix: plasma. Cassette dosing. |
| C20 | cynomolgus monkey. 2 mg/kg IV. Matrix: plasma. Vehicle/formulation: 10% HP-beta-CD/90% water. |
| C21 | rat; Sprague-Dawley; male. 0.5 mg/kg IV. Matrix: systemic matrix unspecified. Vehicle/formulation: 100%DMSO. |
| C22 | rat; Wistar; male. 0.3 mg/kg IV. Matrix: blood. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `CN(CCCOCCCc1cccc2c1n(C)c(=O)n2C1CCC(=O)NC1=O)C[C@H]1CC[C@H](n2cc(NC(=O)c3cnn4ccc(N5C[C@H]6C[C@@H]5CO6)nc34)c(C(F)F)n2)CC1` |
| M002 | C02 | `Cn1nc2c(=O)n(C3CC3)cnc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M003 | C03 | `O=C(NCC(=O)N1CCOCC1)Nc1cc(F)c(Oc2ccnc3[nH]cc(C(F)(F)F)c23)c(F)c1` |
| M004 | C02 | `CCn1cc(C)c2c([C@H](N)c3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M005 | C04 | `N#Cc1ccc(N2CCN(C(=O)Cc3ccc(C4CC4)c(F)c3)CC2)nn1` |
| M006 | C02 | `CCn1ccc2c([C@](O)(c3ccc(C(F)(F)F)nc3)C3CC3)n(C)nc2c1=O` |
| M007 | C05 | `Cn1cc(-c2oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c3c2-c2cccc(N3CCNCC3)c2)cn1` |
| M008 | C06 | `COc1cc2nn(CC(=O)N3CCN(C)CC3)cc2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M009 | C01 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc([C@H]3C[C@H](COC4CCN(C[C@H]5CC[C@H](n6cc(NC(=O)c7cnn8ccc(N9C[C@H]%10C[C@@H]9CO%10)nc78)c(C(F)F)n6)CC5)CC4)C3)c21` |
| M010 | C07 | `Fc1cc(NC2=NCC3(CCOCC3)CO2)cc(F)c1Oc1ccnc2[nH]cc(C3(C(F)(F)F)CC3)c12` |
| M011 | C08 | `C=CC(=O)N1CCN([C@@H]2CN(c3cc(N4CCC(c5c(C)ccnc5C5(OC)COC5)CC4)nc(C(F)(F)F)n3)[C@@H]2C)CC1` |
| M012 | C09 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@@](C)(O)C5)nc(OCC5(CN6CCC(F)(CN7CCN(c8cccc9c8n(C)c(=O)n9C8CCC(=O)NC8=O)CC7)CC6)CC5)nc4c3F)c12` |
| M013 | C01 | `CN(CCCOCCCc1cccc2c1n(C)c(=O)n2C1CCC(=O)NC1=O)C[C@H]1CC[C@H](n2cc(NC(=O)c3cnn4ccc(N5C[C@H](N)CC(F)(F)C5)nc34)c(C(F)F)n2)CC1` |
| M014 | C10 | `COCC[C@H]1CNC(=O)c2c1[nH]c(-c1ccncc1F)c2Nc1cccc(Cl)c1OC` |
| M015 | C11 | `CCn1nccc1[C@@]1(CNC(=O)c2ccccc2-c2ccc(C(F)(F)F)cc2)NC(=O)NC1=O` |
| M016 | C02 | `Cn1nc2c(=O)n(C3CC3)ncc2c1[C@](N)(c1ccc(C(F)(F)F)c(Cl)c1)C1CC1` |
| M017 | C12 | `COc1cc(N2C[C@@H](C)n3c(c(CCCOc4cc(C)c(Cl)c(C)c4)c4ccc(Cl)c(-c5c(C)ncnc5C)c43)C2=O)c2c(cc(C(=O)O)n2C)c1OC` |
| M018 | C13 | `Cc1cc(S(=O)(=O)N[C@H]2C[C@H](N3CCN(CC4CCN(c5cccc6c5n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)C4(CC4)C3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M019 | C06 | `CCOc1cc2nn(CC(=O)N3CCOCC3)cc2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M020 | C09 | `CCc1c(F)ccc2cc(O)cc(-c3nc4c5c(nc(OCC6(CN7CCC(F)(CN8CCC9(CC8)COc8cc%10c(cc89)n(C)c(=O)n%10C8CCC(=O)NC8=O)CC7)CC6)nc5c3F)N3CCCOC[C@H]3CO4)c12` |
| M021 | C06 | `COc1cc2nn(CCC(C)(C)O)cc2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M022 | C13 | `Cc1cc(S(=O)(=O)N[C@H]2CC[C@H](N3CCN(CC4CCN(c5cccc6c5n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M023 | C11 | `O=C1NC(=O)[C@](CNC(=O)c2ccccc2-c2ccc(C(F)(F)F)cc2)(C2CC2)N1` |
| M024 | C14 | `CS(=O)(=O)c1cncc(C(=O)N2[C@@H](C(=O)N[C@@H](c3cc(F)c(Cl)cc3F)C3CC3)C[C@H]3C[C@H]32)c1` |
| M025 | C15 | `CN1C(=O)CCCc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc21` |
| M026 | C13 | `Cc1cc(S(=O)(=O)NCCO[C@H]2CC[C@H](CN3CCC(c4ccc5c(c4F)n(C)c(=O)n5C4CCC(=O)NC4=O)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c([C@H]2CC[C@@](C)(O)CC2)n1` |
| M027 | C15 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCC(=O)N3)n1` |
| M028 | C09 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@]6(CCO6)C5)nc(OCC5(CN6CCC(F)(CN7CCC8(CC7)COc7cc9c(cc78)n(C)c(=O)n9C7CCC(=O)NC7=O)CC6)CC5)nc4c3F)c12` |
| M029 | C16 | `COC[C@H](c1cnn2cc([C@@H](Nc3nnc(C4CC4)o3)C3CCC(F)(F)CC3)nc2c1)N1C[C@@H](C(F)(F)F)NC1=O` |
| M030 | C17 | `CC[C@@H](C(=O)Nc1ccc(C(=O)O)cc1)n1cc(OC)c(-c2cc(Cl)ccc2C#N)cc1=O` |
| M031 | C18 | `C=CC(=O)N1CCN(C2CN(c3cc(N4CCC(c5scnc5C)CC4)nc(C(F)(F)F)n3)C2)CC1` |
| M032 | C19 | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)Nc2ccccc2)c1=O` |
| M033 | C20 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(C#CCOC3CCN(C[C@H]4CC[C@H](n5cc(NC(=O)c6cnn7ccc(N8C[C@H]9C[C@@H]8CO9)nc67)c(C(F)F)n5)CC4)CC3)c21` |
| M034 | C21 | `CS(=O)(=O)c1cccc(C(=O)N2CCC[C@@H]2C(=O)N[C@@H](c2ccc(C(F)(F)F)cc2)C2COC2)c1` |
| M035 | C21 | `CS(=O)(=O)c1cccc(C(=O)N2CCC[C@@H]2C(=O)NCc2ccc(C(F)(F)F)cc2)c1` |
| M036 | C16 | `COC[C@H](c1cnn2cc([C@@H](NC(=O)/C(F)=C\C3CC3)C3CCC(F)(F)CC3)nc2c1)N1C[C@@H](C(F)(F)F)NC1=O` |
| M037 | C16 | `COC[C@H](c1cnn2cc([C@@H](NC(=O)c3nonc3C)C3CCC(F)(F)CC3)nc2c1)N1C[C@@H](C(F)(F)F)NC1=O` |
| M038 | C12 | `COc1c(OCC2CCOCC2)cc(N2C[C@@H](C)n3c(c(CCCOc4cc(C)c(Cl)c(C)c4)c4ccc(Cl)c(-c5c(C)nc(C)nc5C)c43)C2=O)c2c1cc(C(=O)O)n2C` |
| M039 | C12 | `COCCOc1cc(N2C[C@@H](C)n3c(c(CCCOc4cc(C)c(Cl)c(C)c4)c4ccc(Cl)c(-c5c(C)ncnc5C)c43)C2=O)c2c(cc(C(=O)O)n2C)c1OC` |
| M040 | C22 | `O=C(NCc1ccncc1)Nc1cc(F)c(Oc2ccnc3[nH]cc(C(F)(F)F)c23)c(F)c1` |
| M041 | C22 | `Cc1nnc(Nc2cc(F)c(Oc3ccnc4[nH]cc(Cl)c34)c(F)c2)[nH]1` |
| M042 | C13 | `Cc1cc(S(=O)(=O)N[C@H]2C[C@H](N3CC[C@@H](OC4CN(c5cccc6c5n(C)c(=O)n6C5CCC(=O)NC5=O)C4)[C@H](F)C3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M043 | C13 | `C[C@]1(O)CCCN(c2nc(Nc3ccc(S(=O)(=O)N[C@H]4CC[C@H](CN5CCN(c6ccc(C7CCC(=O)NC7=O)cc6F)CC5)CC4)cc3F)ncc2C(F)(F)F)C1` |
| M044 | C13 | `C[C@]1(O)CCCN(c2nc(Nc3ccc(S(=O)(=O)N[C@H]4CC[C@H](CN5CCN(c6ccc(C7CCC(=O)NC7=O)c(F)c6)CC5)CC4)cc3F)ncc2C(F)(F)F)C1` |
| M045 | C13 | `Cc1cc(S(=O)(=O)N[C@H]2C[C@H](N3CCN(CC4CCN(c5ccc(NC6CCC(=O)NC6=O)cc5C)CC4)CC3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |

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
