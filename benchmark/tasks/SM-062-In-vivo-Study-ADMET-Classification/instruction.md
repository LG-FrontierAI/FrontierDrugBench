---
bench_id: "SM-062-In-vivo-Study-ADMET-Classification"
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
| C01 | rat; Sprague-Dawley; male. 0.5 mg/kg IV. Matrix: plasma. |
| C02 | rat; Sprague-Dawley. 0.5 mg/kg IV. Matrix: plasma. Vehicle/formulation: 20%DMSO/40%PEG400/water. Cassette dosing. |
| C03 | rat; Sprague-Dawley; male. 1 mg/kg IV. Matrix: plasma. Feeding: overnight fasted. |
| C04 | mouse; CD-1; male. 1 mg/kg IV. Matrix: plasma. Cassette dosing. |
| C05 | mouse; CD1. 1 mg/kg IV. Matrix: plasma. Vehicle/formulation: DMSO. |
| C06 | rat. 2 mg/kg IV. Matrix: systemic matrix unspecified. |
| C07 | rat; Han Wistar. IV 30min infusion; mg/kg not reported in inspected method. Matrix: blood. |
| C08 | rat; Wistar; male. 0.5 mg/kg IV. Matrix: blood. Vehicle/formulation: solution with PEG400/Solutol/EtOH; proportions not specified. |
| C09 | rat; Wistar; male. 0.3 mg/kg IV bolus. Matrix: systemic matrix unspecified. |
| C10 | rat; Sprague-Dawley; male. 0.5 mg/kg IV. Matrix: systemic matrix unspecified. Vehicle/formulation: 100%DMSO. |
| C11 | rat; Sprague-Dawley. 0.5 mg/kg IV cassette. Matrix: plasma. Vehicle/formulation: 20% DMSO + 40% PEG400 + water. Cassette dosing. |
| C12 | rat; Sprague-Dawley. 1 mg/kg IV. Matrix: plasma. |
| C13 | rat; Wistar; male. 0.3 mg/kg IV. Matrix: blood. |
| C14 | dog; Beagle; male/female. 0.5 mg/kg IV. Matrix: blood. Vehicle/formulation: solution with PEG400/Solutol/EtOH; proportions not specified. |
| C15 | rat; Sprague-Dawley; male. 0.1 mg/kg IV cassette. Matrix: plasma. Vehicle/formulation: 10% DMSO in 0.1 M phosphate buffer pH8.5. Cassette dosing. |
| C16 | rat; Sprague-Dawley; male. 1 mg/kg IV. Matrix: plasma. |
| C17 | mouse; ICR. 2.0 mg/kg IV. Matrix: plasma. Vehicle/formulation: 5%DMSO+10%solutol+85%saline. |
| C18 | dog; Beagle. 0.5 mg/kg IV. Matrix: plasma. Vehicle/formulation: 20% DMSO + 60% PEG400 + water. |
| C19 | mouse. 20 mg/kg IV. Matrix: plasma. Vehicle/formulation: 10% ethanol + 10% Cremophor EL; remaining vehicle not specified in method. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OC(C)(C)C(=O)N3C)n1` |
| M002 | C02 | `C=CC(=O)N1CCC[C@@H]1C#Cc1cnccc1-c1[nH]c2c(c1Nc1cccc(Cl)c1OC)C(=O)NCC2` |
| M003 | C03 | `CCn1cc(C2CC2)c2c(Cc3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M004 | C04 | `CC(C)(C)OC(=O)Nc1cc(F)cn([C@@H](CC2CC2)C(=O)N[C@@H](C[C@@H]2CCNC2=O)C(=O)C(N)=O)c1=O` |
| M005 | C05 | `C=CC(=O)N1CCN(C2CN(c3cc(N4CCC(c5nccs5)CC4)nc(C(F)(F)F)n3)C2)CC1` |
| M006 | C06 | `Cc1cc(S(=O)(=O)N[C@H]2CC[C@H](CN3CCN(c4ccc(C5CCC(=O)NC5=O)c(Cl)c4)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M007 | C07 | `CC[C@@H]1CN(Cc2cc([C@@H](CC(=O)O)c3ccc4c(nnn4C)c3C)ccc2C)S(=O)(=O)c2ccccc2O1` |
| M008 | C06 | `Cc1cc(S(=O)(=O)N[C@]2(C)C[C@@H](N3CCN(CC4CCN(c5ccc6c(c5F)n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)CC3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M009 | C08 | `CC(C)(O)CCn1cc2cc(NC(=O)c3cccc(C(F)(F)F)n3)c(C(C)(C)O)cc2n1` |
| M010 | C07 | `CC[C@@H]1CN(Cc2cc([C@H](CC(=O)O)c3ccc4c(nnn4CC)c3C)ccc2C)S(=O)(=O)c2cccnc2O1` |
| M011 | C09 | `COc1cn([C@@H](C[C@@H]2CCCCO2)C(=O)Nc2ccc(C(=O)O)cc2)c(=O)cc1-c1cc(Cl)ccc1C#N` |
| M012 | C10 | `CS(=O)(=O)c1cccc(C(=O)N2CCC[C@@H]2C(=O)N[C@@H](c2ccc(C(F)(F)F)c(F)c2)C2CC2)c1` |
| M013 | C11 | `COCC[C@@]1(C)CNC(=O)c2c1[nH]c(-c1ccncc1F)c2Nc1cccc(Cl)c1OC` |
| M014 | C07 | `CC[C@@H]1CN(Cc2cc([C@H](CC(=O)O)c3ccc4c(nnn4C)c3C)ccc2C)S(=O)(=O)c2ccccc2O1` |
| M015 | C12 | `COC[C@H](c1cnn2cc([C@@H](NC(=O)/C(F)=C3\CCOC3)C3CCC(F)(F)CC3)nc2c1)N1C[C@@H](C(F)(F)F)NC1=O` |
| M016 | C13 | `Fc1cc(NC2=NCC3(CCC3)CO2)cc(F)c1Oc1ccnc2[nH]cc(C3(C(F)(F)F)CC3)c12` |
| M017 | C14 | `CC(C)(O)c1cc2nn(CCS(C)(=O)=O)cc2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M018 | C06 | `C[C@H]1CN(c2ccc(C3CCC(=O)NC3=O)cc2F)CCN1CC12CCC(NS(=O)(=O)c3ccc(Nc4ncc(C(F)(F)F)c(N5CCC[C@](C)(O)C5)n4)c(F)c3)(CC1)CO2` |
| M019 | C03 | `CCn1cc(C)c2c([C@H](O)c3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M020 | C15 | `CCc1oc2c(Cl)ccc(Cl)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M021 | C13 | `CC1(C)CN=C(Nc2cc(F)c(Oc3ccnc4[nH]cc(C5(C(F)(F)F)CC5)c34)c(F)c2)OC1` |
| M022 | C16 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3)c1` |
| M023 | C03 | `Cc1nn(C2CC2)c(=O)c2nn(C)c(Cc3ccc(C(F)(F)F)c(C#N)c3)c12` |
| M024 | C06 | `Cc1cc(S(=O)(=O)N[C@H]2CC[C@H](CN3CCN(c4cccc(NC5CCC(=O)NC5=O)c4)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M025 | C17 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@@](C)(O)C5)nc(OCC5(CN6CCC(F)(CN7CCN(c8ccc9c(c8)n(C)c(=O)n9C8CCC(=O)NC8=O)CC7)CC6)CC5)nc4c3F)c12` |
| M026 | C18 | `COc1c(Cl)cccc1Nc1c(-c2ccnc(C)n2)[nH]c2c1C(=O)NC[C@H]2C[C@@H]1COCCO1` |
| M027 | C15 | `CCc1oc2cccc(C)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M028 | C04 | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)NC2CCCCC2)c1=O` |
| M029 | C10 | `CS(=O)(=O)c1cc(C(=O)N2[C@@H](C(=O)N[C@@H](c3ccc(C(F)(F)F)cc3F)C3CC3)C[C@H]3C[C@H]32)ccn1` |
| M030 | C11 | `COc1c(Cl)cccc1Nc1c(-c2ccncc2F)[nH]c2c1C(=O)NC[C@@H]2C[C@@H]1CCO1` |
| M031 | C16 | `O=C1COc2cc(F)c(C(=O)Nc3cccc(-c4nncn4-c4ccccc4)n3)cc2N1` |
| M032 | C06 | `CNS(=O)(=O)c1ccc(Nc2ncc(C(F)(F)F)c([C@H]3CC[C@@](C)(O)CC3)n2)c(C)c1` |
| M033 | C08 | `COCCCn1cc2cc(NC(=O)c3cccc(C(F)(F)F)n3)c(OC)cc2n1` |
| M034 | C13 | `COCCNC(=O)Nc1cc(F)c(Oc2ccnc3[nH]cc(C(F)(F)F)c23)c(F)c1` |
| M035 | C19 | `COc1c(OC[C@@H]2CCCO2)cc(N2C[C@@H](C)n3c(c(CCCOc4cc(C)c(Cl)c(C)c4)c4ccc(Cl)c(-c5c(C)nc(C)nc5C)c43)C2=O)c2c1cc(C(=O)O)n2C` |
| M036 | C19 | `CCOc1c(O[C@H]2CCOC2)cc(N2C[C@@H](C)n3c(c(CCCOc4cc(C)c(Cl)c(C)c4)c4ccc(Cl)c(-c5c(C)nc(C)nc5C)c43)C2=O)c2c1cc(C(=O)O)n2C` |
| M037 | C12 | `CC(F)(F)c1nnc(N[C@H](c2cn3ncc([C@@H](C4CC4)N4C[C@@H](C(F)(F)F)NC4=O)cc3n2)C2CCC(F)(F)CC2)o1` |
| M038 | C12 | `COC[C@H](c1cnn2cc([C@@H](NC(=O)/C(F)=C\C3(F)CC3)C3CCC(F)(F)CC3)nc2c1)N1C[C@@H](C(F)(F)F)NC1=O` |
| M039 | C06 | `Cc1cc(S(=O)(=O)N[C@H](C)CO[C@H]2CC[C@H](CN3CCN(c4ccc5c(c4F)n(C)c(=O)n5C4CCC(=O)NC4=O)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c([C@H]2CC[C@@](C)(O)CC2)n1` |
| M040 | C06 | `Cc1cc(S(=O)(=O)NCCO[C@H]2CC[C@H](CN3CCC(c4ccc5c(c4)n(C)c(=O)n5C4CCC(=O)NC4=O)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c([C@H]2CC[C@@](C)(O)CC2)n1` |
| M041 | C03 | `CC[C@@](O)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ccn(C3CC3)c(=O)c2nn1C` |
| M042 | C03 | `CC[C@@](N)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ccn(C3CC3)c(=O)c2nn1C` |
| M043 | C16 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCC(=O)N3C)n1` |
| M044 | C16 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCC(=O)N3C)n1` |
| M045 | C16 | `CC(CO)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3C)n1` |

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
