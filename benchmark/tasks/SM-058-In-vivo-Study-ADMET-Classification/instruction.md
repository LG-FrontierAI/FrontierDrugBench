---
bench_id: "SM-058-In-vivo-Study-ADMET-Classification"
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
| C01 | mouse. PO 30 mg/kg; IV reference 2 mg/kg. Matrix: plasma. Vehicle/formulation: PEG400/SolutolHS15/Phosal53MCT30:20:50v/v/v. |
| C02 | mouse; CD1. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: plasma. |
| C03 | rat; Sprague-Dawley; male. PO 3 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: PO: 0.5% w/v HPMC,0.5% v/v benzyl alcohol,0.4% v/v polysorbate80 in water; IV:5-10% w/v Trappsol with5-10% DMSO. Feeding: overnight fast; food restored4 h. |
| C04 | rat. PO 10 mg/kg; IV reference 2 mg/kg. Matrix: plasma. |
| C05 | mouse; C57BL/6J; female. PO 30 mg/kg; IV reference 2 mg/kg. Matrix: plasma. |
| C06 | mouse; CD-1. PO 50 mg/kg; IV reference 1 mg/kg. Matrix: whole blood. Vehicle/formulation: IV10%DMSO/35%PEG400(remainder unspecified);PO70%PEG/30%D5W. |
| C07 | dog; Beagle; female. PO 1 mg/kg; IV reference 0.5 mg/kg. Matrix: reported blood basis. Vehicle/formulation: IVwater/PEG400/EtOH50/40/10; POwater/Solutol/EtOH50/40/10. |
| C08 | mouse; CD-1. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: IV DMSO; PO1%Tween80/2%HPMC/97%water. |
| C09 | mouse; CD-1; male. PO 10 mg/kg; IV reference 10 mg/kg. Matrix: plasma. Vehicle/formulation: DMSO/Cremophor/PBS10/10/80. |
| C10 | mouse. PO 3 mg/kg; IV reference 3 mg/kg. Matrix: plasma. Vehicle/formulation: 10%NMP/5%Solutol/85%normal saline. |
| C11 | rat; Sprague-Dawley; male. PO 3 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: PO1%MC400aqueous,10mL/kg; IVvehicle not specified in inspected SI. |
| C12 | dog. PO 0.3 mg/kg; IV reference dose unspecified. Matrix: unspecified. |
| C13 | rat; Wistar; male. PO 0.8 mg/kg; IV reference 0.4 mg/kg. Matrix: reported blood basis. |
| C14 | rat; Sprague-Dawley; male. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: plasma. |
| C15 | rat; Sprague-Dawley. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: IVDMSO; PO1%Tween80/2%HPMC/97%water. Feeding: fed. |
| C16 | mouse; CD1. PO 5 mg/kg; IV reference dose unspecified. Matrix: plasma. |
| C17 | rat; Wistar-Han; male. PO 10 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: IV10%DMSO/50%PEG400/40%water; PO2%Tween80 in0.5%MC water; 50%ASD. Feeding: fed. |
| C18 | rat; Han Wistar; male. PO 1 mg/kg; IV reference 0.5 mg/kg. Matrix: plasma. Vehicle/formulation: IV5%DMSO/95%SBE-beta-CD(30%w/v); PO0.5%HPMC/0.1%Tween in water. Cassette dosing. |
| C19 | mouse; Balb/c; male. PO 10 mg/kg; IV reference 2 mg/kg. Matrix: plasma. Vehicle/formulation: IV30%Captisol; PO formulation not separately assigned. |
| C20 | rat; Sprague-Dawley. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: 20%HP-beta-CD solution. Feeding: fed. |
| C21 | cynomolgus monkey; cynomolgus. PO 3 mg/kg; IV reference 1 mg/kg. Matrix: plasma. |
| C22 | rat. PO dose unspecified; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: IV10%EtOH/40%PEG/50%saline;PO10%Tween80water. |
| C23 | rat. PO 5 mg/kg; IV reference 2 mg/kg. Matrix: unspecified. Vehicle/formulation: PO20%HP-beta-CD/80%water; IV10%DMSO/40%PEG400/50%water. |
| C24 | rat. PO 3 mg/kg; IV reference dose unspecified. Matrix: unspecified. |
| C25 | rat; Wistar; male. PO 0.6 mg/kg; IV reference 0.3 mg/kg. Matrix: reported blood basis. |
| C26 | rat; Sprague-Dawley; male. PO 2.5 mg/kg; IV reference 0.5 mg/kg. Matrix: plasma. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `COc1ncc(Cl)cc1C[C@H]1C(=O)N(C)CCCCCCC[C@H](N(C)C(=O)[C@@H](NC(=O)[C@@H]2C[C@@H](F)CN2C(=O)C2(C(F)(F)F)CC(F)(F)C2)C2CC2)C(=O)N[C@@H](CC(C)C)C(=O)N1C` |
| M002 | C02 | `N#Cc1c(N)sc2c(F)ccc(-c3c(Cl)cc4c(N5[C@@H]6CC[C@H]5CNC6)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3F)c12` |
| M003 | C03 | `CCn1ccc2c([C@](O)(c3cnc(C(F)(F)F)c(Cl)c3)C3CC3)n(C)nc2c1=O` |
| M004 | C04 | `Cc1cc(S(=O)(=O)N[C@H]2C[C@H](N3CCN(CC4CCN(c5ccc(NC6CCC(=O)NC6=O)cc5C)CC4)CC3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M005 | C05 | `Cc1noc(-c2ccc(NC(=O)[C@H]3CCCC[C@@H]3C(=O)O)cn2)c1NC(=O)O[C@H](C)c1ccccc1Cl` |
| M006 | C04 | `CNS(=O)(=O)c1ccc(Nc2ncc3cc(Cl)c(=O)n(C4CCCC4)c3n2)c(C)c1` |
| M007 | C06 | `CNS(=O)(=O)c1ccc(Nc2ncc3ccc(C(=O)N4C[C@@H](C#N)[C@@H]4C)nc3n2)c(F)c1` |
| M008 | C03 | `CCn1cc(Cl)c2c(Cc3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M009 | C07 | `Fc1cc(NC2=NCC3(CCOCC3)CO2)cc(F)c1Oc1ccnc2[nH]cc(C3(C(F)(F)F)CC3)c12` |
| M010 | C04 | `Cc1cc(S(=O)(=O)N[C@H]2CC[C@H](CN3CCN(c4ccc(C5CCC(=O)NC5=O)c(Cl)c4)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M011 | C04 | `CNS(=O)(=O)c1ccc(Nc2ncc(C(F)(F)F)c([C@H]3CC[C@@](C)(O)CC3)n2)c(C)c1` |
| M012 | C08 | `C=CC(=O)N1CCN(C2CN(c3cc(N4CCC(c5c(C)cnn5C)CC4)nc(C(F)(F)F)n3)C2)CC1` |
| M013 | C09 | `Nc1cc(-c2cnco2)ccc1NC1CCCCC1` |
| M014 | C10 | `COC1CCN(Cc2ccc(-c3cn([C@H]4CC[C@H](O)CC4)c4nc(Nc5cc(C(F)(F)F)cc(C(F)(F)F)c5)ncc34)cc2)CC1` |
| M015 | C11 | `COc1ncc(Cl)cc1S(=O)(=O)Nc1ccc(F)c(-c2ccc3c(-c4ncc[nH]4)ncn3c2)c1F` |
| M016 | C12 | `COC[C@H](c1cnn2cc([C@@H](NC(=O)/C(F)=C\C3CC3)C3CCC(F)(F)CC3)nc2c1)N1C[C@@H](C(F)(F)F)NC1=O` |
| M017 | C13 | `O=C(NCCCN1CCOCC1)Nc1cc(F)c(Oc2ccnc3[nH]cc(C(F)(F)F)c23)c(F)c1` |
| M018 | C03 | `CC[C@@](N)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ccn(C3CC3)c(=O)c2nn1C` |
| M019 | C13 | `O=C(NCC(=O)N1CCOCC1)Nc1cc(F)c(Oc2ccnc3[nH]cc(C(F)(F)F)c23)c(F)c1` |
| M020 | C11 | `CNC(=O)c1n[nH]c2c(F)c(-c3c(F)ccc(NS(=O)(=O)c4cc(Cl)cnc4OC)c3F)ccc12` |
| M021 | C14 | `O=C1CCCc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc2N1` |
| M022 | C15 | `C=CC(=O)N1CCN([C@@H]2CN(c3cc(N4CCC(c5c(C)ccnc5C5(OC)COC5)CC4)nc(C(F)(F)F)n3)[C@@H]2C)CC1` |
| M023 | C16 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCCOCC5)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3F)c12` |
| M024 | C17 | `CC(C)(C)[C@H](NC(=O)C(F)(F)F)C(=O)N1C[C@H](OC(F)F)C[C@H]1C(=O)N[C@H](C#N)C[C@@H]1CCNC1=O` |
| M025 | C14 | `Cc1cc(F)c(C(=O)Nc2cccc(-c3nncn3C(C)C)n2)cc1-n1cnc(C2CC2)c1` |
| M026 | C18 | `O=C(O)c1cn(C2CC2)c2cc(N3CCN(C(=O)N(C4CC4)C(F)(F)F)CC3)c(F)cc2c1=O` |
| M027 | C14 | `O=C1COc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CCCC4)n3)cc2N1` |
| M028 | C19 | `C[C@@H]1CN(c2ccc(Cl)nn2)CCN1C(=O)Cc1ccc(C2CC2)c(F)c1` |
| M029 | C04 | `Cc1cc(S(=O)(=O)N[C@]2(C)C[C@@H](N3CCN(CC4CCN(c5ccc6c(c5F)n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)CC3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M030 | C20 | `Cn1cc(-c2ccnc3[nH]ncc23)c(-c2ccc(F)cc2)n1` |
| M031 | C21 | `CCc1cc(NC(=O)C(=O)N2C[C@@H](C)CC[C@@H]2c2ccc3sc(C4CCN(C)CC4)nc3c2)cnc1N` |
| M032 | C03 | `Cn1nc2c(=O)n(C3CC3)ncc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M033 | C22 | `Cn1nc(-c2ccnn2C)cc1CNC(=O)c1cc(-c2ccco2)ccc1Cl` |
| M034 | C23 | `CN(CCCOCCCc1cccc2c1n(C)c(=O)n2C1CCC(=O)NC1=O)C[C@H]1CC[C@H](n2cc(NC(=O)c3cnn4ccc(N5C[C@H]6C[C@@H]5CO6)nc34)c(C(F)F)n2)CC1` |
| M035 | C06 | `CNS(=O)(=O)c1ccc(Nc2ncc3ccc(C(=O)N4CC[C@@H]4C)nc3n2)c(F)c1` |
| M036 | C14 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCC(=O)N3C)n1` |
| M037 | C14 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCc2cncn2-3)n1` |
| M038 | C24 | `C/C=C(/F)C(=O)N[C@H](c1cn2ncc([C@@H](COC)N3C[C@@H](C(F)(F)F)NC3=O)cc2n1)C1CCC(F)(F)CC1` |
| M039 | C24 | `COC[C@H](c1cnn2cc([C@@H](NC(=O)/C(F)=C3\CCOC3)C3CCC(F)(F)CC3)nc2c1)N1C[C@@H](C(F)(F)F)NC1=O` |
| M040 | C04 | `Cc1cc(S(=O)(=O)NCCO[C@H]2CC[C@H](CN3CCC(c4ccc5c(c4)n(C)c(=O)n5C4CCC(=O)NC4=O)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c([C@H]2CC[C@@](C)(O)CC2)n1` |
| M041 | C04 | `Cc1cc(S(=O)(=O)N[C@H]2CC[C@H](N3CCN(CC4CCN(c5cccc6c5n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M042 | C25 | `Cc1nnc(Nc2cc(F)c(Oc3ccnc4[nH]cc(Cl)c34)c(F)c2)[nH]1` |
| M043 | C25 | `CC1(CO)CN=C(Nc2cc(F)c(Oc3ccnc4[nH]cc(C(F)(F)F)c34)c(F)c2)OC1` |
| M044 | C26 | `O=C1CCc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc2N1` |
| M045 | C26 | `O=C1COc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc2N1` |

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

## 2. Analogue comparisons

Compare the left and right absolute oral bioavailabilities. Choose A if F(left) - F(right) > 20 percentage points; B if the difference lies between -20 and +20 percentage points, inclusive; C if F(left) - F(right) < -20 percentage points. Percentage points describe the difference between two percentages, rather than a fold ratio.

Each pair belongs to one literature analogue family and one study context. B denotes only the specified numerical difference category; it does not establish statistical equivalence. No cross-species or cross-dose comparison is requested.

| Item | Left molecule | Right molecule | Points |
|---|---|---|---|
| Q036 | M036 | M037 | 6 |
| Q037 | M038 | M039 | 6 |
| Q038 | M040 | M041 | 6 |
| Q039 | M042 | M043 | 6 |
| Q040 | M044 | M045 | 6 |

## Response format and scoring

Return ONLY a strict JSON object mapping each listed Q identifier to L/M/H for interval items, A/B/C for comparisons, or an ordered array of the listed molecule IDs for ordering items.

Syntax example only; these values do not imply answers:

`{"Q001": "L", "Q036": "B"}`

Each molecule is assessed in one item. Missing or invalid items earn zero. An ordering array must contain every specified molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0–1 scale.
