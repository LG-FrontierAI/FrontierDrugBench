---
bench_id: "SM-055-In-vivo-Study-ADMET-Classification"
category: "In-vivo-Study"
format: "structured_json"
---
# Prompt

Predict absolute oral bioavailability (F) under the stated study conditions. This task contains 45 distinct molecules and is worth 100 points.

F compares dose-normalized oral and intravenous exposure. Predict the reported systemic bioavailability, not the fraction absorbed.

Higher F means a larger fraction of the administered oral dose reaches systemic circulation. An observed F estimate can exceed 100%; retain the reported estimate for interval prediction.

Use the study context assigned to each molecule. PO means oral administration; IV means intravenous administration. Conditions not listed are unspecified.

## Study contexts

| Context | Conditions |
|---|---|
| C01 | rat. PO 10 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: IV10%EtOH/40%PEG400/50%saline; PO10%Tween80water; not assigned. |
| C02 | rat; Sprague-Dawley; male. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: plasma. |
| C03 | rat. PO 10 mg/kg; IV reference 2 mg/kg. Matrix: plasma. |
| C04 | rat; Sprague-Dawley; male. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: IVPEG200/water60/40; POSolutolHS15/0.5%MC2/98. |
| C05 | rat; Wistar; male. PO 0.6 mg/kg; IV reference 0.3 mg/kg. Matrix: reported blood basis. |
| C06 | cynomolgus monkey. PO 10 mg/kg; IV reference 2 mg/kg. Matrix: plasma. Vehicle/formulation: EtOH/PEG300/water1:4:5v/v. |
| C07 | rat; Wistar-Han; male. PO 10 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: IV10%DMSO/50%PEG400/40%water; PO2%Tween80 in0.5%MC water; amorphous solution. Feeding: fed. |
| C08 | rat; Sprague-Dawley; male. PO 2 mg/kg; IV reference .5 mg/kg. Matrix: plasma. Vehicle/formulation: IV10/50/40DMSO/PEG400/water;POMCT. Feeding: PO fast16h;IVfed. |
| C09 | cynomolgus monkey; cynomolgus. PO dose unspecified; IV reference dose unspecified. Matrix: plasma. |
| C10 | rat. PO 1 mg/kg; IV reference .3 mg/kg. Matrix: unspecified. |
| C11 | mouse; CD1. PO 5 mg/kg; IV reference dose unspecified. Matrix: plasma. |
| C12 | rat; Sprague-Dawley. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: 20%HP-beta-CD solution. Feeding: fed. |
| C13 | rat; Sprague-Dawley; male. PO .1 mg/kg; IV reference .1 mg/kg. Matrix: plasma. Vehicle/formulation: 10%DMSO/0.1M phosphate buffer pH8.5. F based on AUC0-8 h. Cassette dosing. |
| C14 | rat; Sprague-Dawley; male. PO 3 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: PO: 0.5% w/v HPMC,0.5% v/v benzyl alcohol,0.4% v/v polysorbate80 in water; IV:5-10% w/v Trappsol with5-10% DMSO. Feeding: overnight fast; food restored4 h. |
| C15 | mouse; Balb/c; male. PO 10 mg/kg; IV reference 2 mg/kg. Matrix: plasma. Vehicle/formulation: IV30%Captisol; PO formulation not separately assigned. |
| C16 | rat. PO 3 mg/kg; IV reference dose unspecified. Matrix: unspecified. |
| C17 | rat. PO 5 mg/kg; IV reference 2 mg/kg. Matrix: unspecified. Vehicle/formulation: PO20%HP-beta-CD/80%water; IV10%DMSO/40%PEG400/50%water. |
| C18 | mouse; CD-1; male. PO 10 mg/kg; IV reference 10 mg/kg. Matrix: plasma. Vehicle/formulation: DMSO/Cremophor/PBS10/10/80. |
| C19 | mouse. PO 10 mg/kg; IV reference 2 mg/kg. Matrix: plasma. |
| C20 | mouse; CD-1. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: IV DMSO; PO1%Tween80/2%HPMC/97%water. |
| C21 | cynomolgus monkey; cynomolgus. PO 1 mg/kg; IV reference 0.5 mg/kg. Matrix: reported blood basis. Vehicle/formulation: PO50mM citrate buffer pH3.0. |
| C22 | mouse; ICR; male. PO 10 mg/kg; IV reference 2.5 mg/kg. Matrix: plasma. |
| C23 | mouse; C57BL/6; male. PO 10 mg/kg; IV reference 3 mg/kg. Matrix: plasma. |
| C24 | rat. PO 1 mg/kg; IV reference 0.3 mg/kg. Matrix: reported blood basis. Vehicle/formulation: POwater50%/PEG40040%/EtOH10%; IVplasma99%/DMSO1% for mouse/rat, water50%/PEG40040%/EtOH10% dog. |
| C25 | mouse; CD1; male. PO 3 mg/kg; IV reference 3 mg/kg. Matrix: plasma. Vehicle/formulation: 10%NMP/5%Solutol/85%normal saline. |
| C26 | rat; Wistar Han; male. PO dose unspecified; IV reference dose unspecified. Matrix: blood. |
| C27 | mouse; C57BL/6J; female. PO 30 mg/kg; IV reference 2 mg/kg. Matrix: plasma. |
| C28 | rat; Sprague-Dawley; male. PO 3 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: PO1%MC400aqueous,10mL/kg; IVvehicle not specified in inspected SI. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `Cc1ncc(S(=O)(=O)N2CCC(c3cn4ncnc4cc3Cl)CC2)o1` |
| M002 | C02 | `CN1C(=O)CCCc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc21` |
| M003 | C03 | `Cc1cc(S(=O)(=O)N[C@H]2C[C@H](N3CCN(CC4CCN(c5cccc6c5n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)CC3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M004 | C03 | `Cc1cc(S(=O)(=O)N[C@H]2C[C@H](N3CC[C@@H](OC4CN(c5cccc6c5n(C)c(=O)n6C5CCC(=O)NC5=O)C4)[C@H](F)C3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M005 | C04 | `Cc1cc(C#N)ncc1Oc1cc(Nc2ccc(N3CCOCC3)nn2)c2ncn(C)c2n1` |
| M006 | C05 | `CC1(C)CN=C(Nc2cc(F)c(Oc3ccnc4[nH]cc(C5(C(F)(F)F)CC5)c34)c(F)c2)OC1` |
| M007 | C06 | `CC(C)C[C@@H](O)C(=O)N1CC2(CC2)C[C@H]1C(=O)N[C@@H](C[C@@H]1CCNC1=O)C(=O)COC(F)(F)F` |
| M008 | C07 | `COC(=O)N[C@H](C(=O)N1C[C@H](OC(F)(F)F)C[C@H]1C(=O)N[C@H](C#N)C[C@@H]1CCNC1=O)C(C)(C)C` |
| M009 | C08 | `Cc1c(-c2cc3cc(NC(=O)OC4CCOCC4)ncc3c(N)c2F)cnc2c1NCCO2` |
| M010 | C09 | `C=CC(=O)N1CCC[C@@H](Oc2nc(-c3cnn(C)c3)cn3nccc23)CC1` |
| M011 | C10 | `CCC[C@@H](C(=O)Nc1ccc(C(N)=O)c(F)c1)n1cc(OC)c(-c2cc(Cl)ccc2-n2cc(Cl)nn2)cc1=O` |
| M012 | C11 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@]6(C5)C[C@@H](O)C6)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3F)c12` |
| M013 | C12 | `Cn1cc(-c2ccnc3[nH]ccc23)c(-c2ccc(F)cn2)n1` |
| M014 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3)n1` |
| M015 | C13 | `CCc1oc2cccc(C)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M016 | C14 | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1ccc(C(F)(F)F)nc1)C1CC1` |
| M017 | C15 | `O=C(Cc1ccc(C2CC2)cc1)N1CCN(c2ccc(Cl)nn2)CC1` |
| M018 | C16 | `COC[C@H](c1cnn2cc([C@@H](Nc3nnc(C4CC4)o3)C3CCC(F)(F)CC3)nc2c1)N1C[C@@H](C(F)(F)F)NC1=O` |
| M019 | C03 | `Cc1cc(S(=O)(=O)NCCO[C@H]2CC[C@H](CN3CCC(c4ccc5c(c4F)n(C)c(=O)n5C4CCC(=O)NC4=O)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c([C@H]2CC[C@@](C)(O)CC2)n1` |
| M020 | C17 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc([C@H]3C[C@H](COC4CCN(C[C@H]5CC[C@H](n6cc(NC(=O)c7cnn8ccc(N9C[C@H]%10C[C@@H]9CO%10)nc78)c(C(F)F)n6)CC5)CC4)C3)c21` |
| M021 | C18 | `Nc1cc(-c2cnco2)ccc1NC1CCC1` |
| M022 | C19 | `CC(C)C[C@@H]1NC(=O)[C@@H](N(C)C(=O)[C@@H](NC(=O)[C@@H]2C[C@@H](F)CN2C(=O)C2(C(F)(F)F)CC(F)(F)C2)C2CC2)CC=CCCCCN(C)C(=O)[C@H](Cc2cc(Cl)ccc2Cl)N(C)C1=O` |
| M023 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)C(C)(C)CC(=O)N3C)n1` |
| M024 | C20 | `C=CC(=O)N1CCN(C2CN(c3cc(N4CCC(c5scnc5C)CC4)nc(C(F)(F)F)n3)C2)CC1` |
| M025 | C21 | `COc1c(Cl)cccc1Nc1c(-c2ccncc2C#C[C@@]2(C)CCCN2C(=O)/C=C/CN(C)C)[nH]c2c1C(=O)NCC2` |
| M026 | C03 | `CNS(=O)(=O)c1ccc(Nc2ncc(C(F)(F)F)c(N3CCC[C@](C)(O)C3)n2)c(C)c1` |
| M027 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3C)n1` |
| M028 | C05 | `Fc1cc(NC2=NCC3(CCC3)CO2)cc(F)c1Oc1ccnc2[nH]cc(C3(C(F)(F)F)CC3)c12` |
| M029 | C22 | `N#Cc1ccnc(N2C(=O)CC[C@H]2C(=O)N(c2cncc(F)c2)[C@H](C(=O)NC2CC(F)(F)C2)c2ccccc2Cl)c1` |
| M030 | C23 | `Cc1cc(N)nc(COc2cc(CCN(C)C)cc(F)c2F)c1` |
| M031 | C24 | `Cn1nccc1[C@]1(CNC(=O)c2ccc(F)c(F)c2-c2ccc(C(F)(F)F)cc2)NC(=O)NC1=O` |
| M032 | C15 | `N#Cc1ccc(N2CCN(C(=O)Cc3ccc(C4CC4)c(F)c3)CC2)nn1` |
| M033 | C25 | `CN1CCN(Cc2ccc(-c3cn([C@H]4CC[C@@H](O)CC4)c4nc(Nc5cc(C(F)(F)F)cc(C(F)(F)F)c5)ncc34)cc2)CC1` |
| M034 | C02 | `O=C(Nc1cccc(-c2nncn2CC2CC2)c1)c1cc2c(cc1F)OCc1cncn1-2` |
| M035 | C14 | `Cc1nn(C2CC2)c(=O)c2nn(C)c(Cc3ccc(C(F)(F)F)c(C#N)c3)c12` |
| M036 | C26 | `COc1ccc(F)c([C@H](CC(=O)O)CN2CC(C(F)(F)CCc3ccc4c(n3)NCCC4)C2)c1` |
| M037 | C27 | `Cc1nc(-c2onc(C)c2NC(=O)O[C@H](C)c2ccccc2Cl)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M038 | C27 | `Cc1nc(-c2nnn(C)c2NC(=O)O[C@H](C)c2ccccc2Cl)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M039 | C28 | `CNC(=O)c1ncn2cc(-c3c(F)ccc(NS(=O)(=O)c4cc(Cl)cnc4OC)c3F)ccc12` |
| M040 | C28 | `CNC(=O)c1ncn2cc(-c3c(F)ccc(NS(=O)(=O)c4cc(Cl)cnc4OC)c3F)ncc12` |
| M041 | C03 | `[2H]C(C)(CO[C@H]1CC[C@H](CN2CCN(c3ccc4c(c3F)n(C)c(=O)n4C3CCC(=O)NC3=O)CC2)CC1)NS(=O)(=O)c1ccc(Nc2ncc(C(F)(F)F)c([C@H]3CC[C@@](C)(O)CC3)n2)c(C)c1` |
| M042 | C03 | `Cc1cc(S(=O)(=O)N[C@@H](C)CO[C@H]2CC[C@H](CN3CCN(c4ccc5c(c4F)n(C)c(=O)n5C4CCC(=O)NC4=O)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c([C@H]2CC[C@@](C)(O)CC2)n1` |
| M043 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3C)c1` |
| M044 | C02 | `CC(CO)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3C)n1` |
| M045 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCC(=O)N3C)n1` |

## 1. Interval prediction

Assign L, M, or H using the following ranges (%). These are numerical endpoint ranges under the listed animal-study conditions, rather than universal development criteria.

| Label | Interval | Interpretation |
|---|---|---|
| L | value < 20 | Less than one fifth of the dose is systemically bioavailable |
| M | 20 <= value < 50 | Between one fifth and one half is systemically bioavailable |
| H | value >= 50 | At least one half is systemically bioavailable |

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
| Q035 | M035 |
| Q036 | M036 |

## 2. Analogue comparisons

Compare the left and right absolute oral bioavailabilities. Choose A if F(left) - F(right) > 20 percentage points; B if the difference lies between -20 and +20 percentage points, inclusive; C if F(left) - F(right) < -20 percentage points. Percentage points describe the difference between two percentages, rather than a fold ratio.

Each pair belongs to one literature analogue family and one study context. B denotes only the specified numerical difference category; it does not establish statistical equivalence. No cross-species or cross-dose comparison is requested.

| Item | Left molecule | Right molecule | Points |
|---|---|---|---|
| Q037 | M037 | M038 | 6 |
| Q038 | M039 | M040 | 6 |
| Q039 | M041 | M042 | 6 |

## 3. Within-series ordering

Order each group from highest to lowest absolute oral bioavailability.

Each group shares one study context. Its score is the listed points multiplied by max(0, Spearman rho) between the submitted and reference orders.

| Item | Molecules to order | Points |
|---|---|---|
| Q040 | M043, M044, M045 | 10 |

## Response format and scoring

Return ONLY a strict JSON object mapping each listed Q identifier to L/M/H for interval items, A/B/C for comparisons, or an ordered array of the listed molecule IDs for ordering items.

Syntax example only; these values do not imply answers:

`{"Q001": "L", "Q037": "B", "Q040": ["M043", "M044", "M045"]}`

Each molecule is assessed in one item. Missing or invalid items earn zero. An ordering array must contain every specified molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0–1 scale.
