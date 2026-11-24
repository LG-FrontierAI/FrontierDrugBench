---
bench_id: "SM-061-In-vivo-Study-ADMET-Classification"
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
| C01 | rat. 2 mg/kg IV. Matrix: systemic matrix unspecified. |
| C02 | rat; Wistar; male. IV; dose unspecified. Matrix: blood. Vehicle/formulation: unspecified. |
| C03 | mouse; CD1. 1 mg/kg IV. Matrix: plasma. Vehicle/formulation: DMSO. |
| C04 | rat; Sprague-Dawley; male. 0.5 mg/kg IV. Matrix: systemic matrix unspecified. Vehicle/formulation: 100%DMSO. |
| C05 | rat; Han Wistar. IV 30min infusion; mg/kg not reported in inspected method. Matrix: blood. |
| C06 | rat; Sprague-Dawley; male. 1 mg/kg IV. Matrix: plasma. Feeding: overnight fasted. |
| C07 | rat. 2 mg/kg IV. Matrix: plasma. Vehicle/formulation: 10% DMSO/40% PEG400/50% water. |
| C08 | mouse. 2 mg/kg IV. Matrix: systemic matrix unspecified. |
| C09 | mouse; CD-1; male. 1 mg/kg IV. Matrix: plasma. Cassette dosing. |
| C10 | mouse. 20 mg/kg IV. Matrix: plasma. Vehicle/formulation: 10% ethanol + 10% Cremophor EL; remaining vehicle not specified in method. |
| C11 | rat; Sprague-Dawley; male. 1 mg/kg IV. Matrix: plasma. |
| C12 | rat; Sprague-Dawley; male. 0.5 mg/kg IV. Matrix: plasma. |
| C13 | rat; Sprague-Dawley; male. 0.1 mg/kg IV cassette. Matrix: plasma. Vehicle/formulation: 10% DMSO in 0.1 M phosphate buffer pH8.5. Cassette dosing. |
| C14 | mouse; BALB/c; male. 2 mg/kg IV. Matrix: plasma. Vehicle/formulation: 30% Captisol. |
| C15 | rat; Wistar; male. 0.5 mg/kg IV. Matrix: blood. Vehicle/formulation: solution with PEG400/Solutol/EtOH; proportions not specified. |
| C16 | rat; Wistar; male. 0.4 mg/kg IV. Matrix: blood. |
| C17 | dog; Beagle. 0.5 mg/kg IV. Matrix: plasma. Vehicle/formulation: 20% DMSO + 60% PEG400 + water. |
| C18 | rat; Sprague-Dawley. 2 mg/kg IV. Matrix: plasma. Vehicle/formulation: 20% DMSO + 40% PEG400 + water. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `CNS(=O)(=O)c1ccc(Nc2ncc(C(F)(F)F)c(N3CCC(C)(O)CC3)n2)c(C)c1` |
| M002 | C02 | `Cn1nccc1[C@]1(CNC(=O)c2ccccc2-c2ccc(C(F)(F)F)cc2)NC(=O)NC1=O` |
| M003 | C03 | `C=CC(=O)N1CCN(C2CN(c3cc(N4CCC(c5c(C)cnn5C)CC4)nc(C(F)(F)F)n3)C2)CC1` |
| M004 | C04 | `CS(=O)(=O)c1cccc(C(=O)N2CCC[C@@H]2C(=O)N[C@@H](c2cc(F)c(Cl)cc2F)C2COC2)c1` |
| M005 | C05 | `COc1cc([C@@H](CC(=O)O)c2ccc(C)c(CN3C[C@@H](C)Oc4ccccc4S3(=O)=O)c2)cc2nnn(C)c12` |
| M006 | C06 | `CC[C@@](O)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2cnn(C3CC3)c(=O)c2nn1C` |
| M007 | C07 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2ccccc21` |
| M008 | C08 | `CN(C)Cc1ccc(-c2c(-c3cnn(C)c3)oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c23)cc1` |
| M009 | C06 | `CCn1ccc2c([C@@](O)(CC)c3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M010 | C09 | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)C2CCCCC2)c1=O` |
| M011 | C03 | `C=CC(=O)N1CCN([C@@H]2CN(c3cc(N4CCC(c5c(C)cnn5C)CC4)nc(C(F)(F)F)n3)[C@@H]2C)CC1` |
| M012 | C02 | `Cn1nccc1[C@]1(CNC(=O)c2ccc(F)cc2-c2ccc(C(F)(F)F)cc2)NC(=O)NC1=O` |
| M013 | C10 | `COc1c(OC[C@H]2CCCO2)cc(N2C[C@@H](C)n3c(c(CCCOc4cc(C)c(Cl)c(C)c4)c4ccc(Cl)c(-c5c(C)nc(C)nc5C)c43)C2=O)c2c1cc(C(=O)O)n2C` |
| M014 | C11 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)C(C)(C)CC(=O)N3C)n1` |
| M015 | C12 | `O=C1COc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc2N1` |
| M016 | C06 | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1ccc(C(F)(F)F)nc1)C1CC1` |
| M017 | C02 | `Cc1scnc1[C@@]1(CNC(=O)c2ccccc2-c2ccc(C(F)(F)F)cc2)NC(=O)NC1=O` |
| M018 | C11 | `CC(CO)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCC(=O)N3)n1` |
| M019 | C13 | `CCc1oc2cccc(Br)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M020 | C06 | `Cn1nc2c(=O)n(C3CC3)ncc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M021 | C01 | `C[C@H]1CN(CC2CCN(c3ccc(C4CCC(=O)NC4=O)cc3F)CC2)CC[C@H]1NS(=O)(=O)c1ccc(Nc2ncc(C(F)(F)F)c(N3CCC[C@](C)(O)C3)n2)c(F)c1` |
| M022 | C13 | `CCc1oc2cccc(Cl)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M023 | C14 | `C[C@@H]1CN(c2ccc(Cl)nn2)CCN1C(=O)Cc1ccc(C2CC2)c(F)c1` |
| M024 | C10 | `CCOc1c(OCC2CCOCC2)cc(N2C[C@@H](C)n3c(c(CCCOc4cc(C)c(Cl)c(C)c4)c4ccc(Cl)c(-c5c(C)nc(C)nc5C)c43)C2=O)c2c1cc(C(=O)O)n2C` |
| M025 | C15 | `COc1cc2nn(CC(=O)N3CCOCC3)cc2cc1NC(=O)c1cccc(C(F)F)n1` |
| M026 | C06 | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M027 | C11 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCc2cncn2-3)c1` |
| M028 | C09 | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)CCc2ccccc2)c1=O` |
| M029 | C05 | `CC[C@@H]1CN(Cc2cc([C@@H](CC(=O)O)c3ccc4c(nnn4CC)c3C)ccc2C)S(=O)(=O)c2cccnc2O1` |
| M030 | C16 | `O=C(NCCCN1CCOCC1)Nc1cc(F)c(Oc2ccnc3[nH]cc(C(F)(F)F)c23)c(F)c1` |
| M031 | C01 | `CNS(=O)(=O)c1ccc(Nc2ncc3cc(Cl)c(=O)n(C4CCCC4)c3n2)c(C)c1` |
| M032 | C14 | `O=C(Cc1ccc(C2CC2)cc1)N1CCN(c2ccc(Cl)nn2)CC1` |
| M033 | C11 | `O=C1COc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CCCC4)n3)cc2N1` |
| M034 | C17 | `COc1c(Cl)cccc1Nc1c(-c2ccncc2F)[nH]c2c1C(=O)NC[C@@H]2C[C@@H]1COCCO1` |
| M035 | C06 | `CCn1ccc2c([C@](O)(c3cnc(C(F)(F)F)c(Cl)c3)C3CC3)n(C)nc2c1=O` |
| M036 | C06 | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C1CC1` |
| M037 | C11 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)C(C)(C)CC(=O)N3)n1` |
| M038 | C11 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3)n1` |
| M039 | C18 | `COc1c(Cl)cccc1Nc1c(-c2ccncc2F)[nH]c2c1C(=O)NC[C@@H]2C[C@H]1COCCO1` |
| M040 | C18 | `COc1c(Cl)cccc1Nc1c(-c2ccncn2)[nH]c2c1C(=O)NC[C@@H]2C[C@@H]1COCCO1` |
| M041 | C14 | `O=C(Cc1ccc(C2CC2)cc1F)N1CCN(c2ccc(Cl)nn2)CC1` |
| M042 | C14 | `O=C(Cc1ccc(C2CC2)c(F)c1)N1CCN(c2ccc(Cl)nn2)CC1` |
| M043 | C01 | `Cc1cc(S(=O)(=O)N[C@H]2C[C@H](N3CCN(CC4CCN(c5ccc6c(c5F)n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)CC3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCCC(C)(O)C2)n1` |
| M044 | C01 | `Cc1cc(S(=O)(=O)N[C@]2(C)C[C@H](N3CCN(CC4CCN(c5ccc6c(c5F)n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)CC3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M045 | C01 | `[2H]C(C)(CO[C@H]1CC[C@H](CN2CCN(c3ccc4c(c3F)n(C)c(=O)n4C3CCC(=O)NC3=O)CC2)CC1)NS(=O)(=O)c1ccc(Nc2ncc(C(F)(F)F)c([C@H]3CC[C@@](C)(O)CC3)n2)c(C)c1` |

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
| Q034 | M034 |

## 2. Analogue comparisons

Compare total IV clearance. Let R = value(left) / value(right). Choose A if R > 3; B if 1/3 <= R <= 3; C if R < 1/3. Thus A means the left compound clears faster and C means it clears more slowly, on the stated systemic-matrix basis.

Each pair belongs to one literature analogue family and one study context. B denotes only the specified numerical difference category; it does not establish statistical equivalence. No cross-species or cross-dose comparison is requested.

| Item | Left molecule | Right molecule | Points |
|---|---|---|---|
| Q035 | M035 | M036 | 6 |
| Q036 | M037 | M038 | 6 |
| Q037 | M039 | M040 | 6 |
| Q038 | M041 | M042 | 6 |

## 3. Within-series ordering

Order each group from lowest to highest total IV clearance, as a prioritization step for reducing clearance under this study protocol.

Each group shares one study context. Its score is the listed points multiplied by max(0, Spearman rho) between the submitted and reference orders.

| Item | Molecules to order | Points |
|---|---|---|
| Q039 | M043, M044, M045 | 8 |

## Response format and scoring

Return ONLY a strict JSON object mapping each listed Q identifier to L/M/H for interval items, A/B/C for comparisons, or an ordered array of the listed molecule IDs for ordering items.

Syntax example only; these values do not imply answers:

`{"Q001": "L", "Q035": "B", "Q039": ["M043", "M044", "M045"]}`

Each molecule is assessed in one item. Missing or invalid items earn zero. An ordering array must contain every specified molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0–1 scale.
