---
bench_id: "SM-056-In-vivo-Study-ADMET-Classification"
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
| C01 | mouse; CD-1; male. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: IVPEG200/water60/40; POSolutolHS15/0.5%MC2/98. |
| C02 | dog. PO 1 mg/kg; IV reference 0.5 mg/kg. Matrix: blood. |
| C03 | mouse; Balb/c; male. PO 10 mg/kg; IV reference 2 mg/kg. Matrix: plasma. Vehicle/formulation: IV30%Captisol; PO formulation not separately assigned. |
| C04 | dog; beagle. PO dose unspecified; IV reference dose unspecified. Matrix: plasma. |
| C05 | mouse; BALB/c. PO 5 mg/kg; IV reference 5 mg/kg. Matrix: blood. |
| C06 | rat; Sprague-Dawley; male. PO 3 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: PO: 0.5% w/v HPMC,0.5% v/v benzyl alcohol,0.4% v/v polysorbate80 in water; IV:5-10% w/v Trappsol with5-10% DMSO. Feeding: overnight fast; food restored4 h. |
| C07 | mouse; BALB/c. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: blood. |
| C08 | rat; Wistar-Han; male. PO 10 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: IV10%PEG400/90%(23%HPBCDwater); PO2%Tween80 in0.5%MC water; amorphous solution. Feeding: fed. |
| C09 | mouse; CD-1. PO 50 mg/kg; IV reference 1 mg/kg. Matrix: whole blood. Vehicle/formulation: IV10%DMSO/35%PEG400(remainder unspecified);PO80%PEG/20%D5W. |
| C10 | rat; Han Wistar; male. PO 1 mg/kg; IV reference 0.5 mg/kg. Matrix: plasma. Vehicle/formulation: IV5%DMSO/95%SBE-beta-CD(30%w/v); PO0.5%HPMC/0.1%Tween in water. Cassette dosing. |
| C11 | mouse; CD-1; male. PO 40 mg/kg; IV reference 10 mg/kg. Matrix: plasma. Vehicle/formulation: PO20%DMSO/80%(20%w/vHP-beta-CD in water); IV10%DMSO/90%(20%w/vHP-beta-CD). Feeding: non-fasted; no water restriction. |
| C12 | rat; Sprague-Dawley. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: 20%HP-beta-CD solution. Feeding: fed. |
| C13 | mouse; CD1. PO 5 mg/kg; IV reference dose unspecified. Matrix: plasma. |
| C14 | rat. PO 3 mg/kg; IV reference dose unspecified. Matrix: unspecified. |
| C15 | mouse; C57BL/6J; female. PO 30 mg/kg; IV reference 2 mg/kg. Matrix: plasma. |
| C16 | mouse; CD-1. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: IV DMSO; PO1%Tween80/2%HPMC/97%water. |
| C17 | cynomolgus monkey; cynomolgus; male. PO 10 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: IV5%PEG400/95%(23%HPBCDwater); PO2%Tween80 in0.5%MC water; crystalline solution. Feeding: fed. |
| C18 | rat; Sprague-Dawley; male. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: plasma. |
| C19 | rat; Sprague-Dawley; male. PO 2 mg/kg; IV reference 1 mg/kg. Matrix: plasma. |
| C20 | rat; Sprague-Dawley; male. PO 3 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: PO1%MC400aqueous,10mL/kg; IVvehicle not specified in inspected SI. |
| C21 | mouse; CD-1; male. PO 3 mg/kg; IV reference 1 mg/kg. Matrix: plasma. |
| C22 | rat; Wistar Han; male. PO dose unspecified; IV reference dose unspecified. Matrix: blood. |
| C23 | rat. PO 10 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: IV10%EtOH/40%PEG400/50%saline; PO10%Tween80water; HCl salt. |
| C24 | rat; Sprague-Dawley; male. PO 2.5 mg/kg; IV reference 0.5 mg/kg. Matrix: plasma. |
| C25 | rat; Wistar; male. PO 0.6 mg/kg; IV reference 0.3 mg/kg. Matrix: reported blood basis. |
| C26 | rat; Sprague-Dawley; male. PO 2 mg/kg; IV reference .5 mg/kg. Matrix: plasma. Vehicle/formulation: IV10/50/40DMSO/PEG400/water;POMCT. Feeding: PO fast16h;IVfed. |
| C27 | mouse; CD-1; male. PO 15 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: IVPEG200/water60/40; POSolutol/0.5%MC2/98. Feeding: fasted. |
| C28 | mouse; ICR; male. PO 10 mg/kg; IV reference 2.5 mg/kg. Matrix: plasma. |
| C29 | rat. PO 2 mg/kg; IV reference 0.5 mg/kg. Matrix: blood. |
| C30 | mouse. PO 30 mg/kg; IV reference 2 mg/kg. Matrix: plasma. Vehicle/formulation: PEG400/SolutolHS15/Phosal53MCT30:20:50v/v/v. |
| C31 | rat; Sprague-Dawley; male. PO .1 mg/kg; IV reference .1 mg/kg. Matrix: plasma. Vehicle/formulation: 10%DMSO/0.1M phosphate buffer pH8.5. F based on AUC0-8 h. Cassette dosing. |
| C32 | rat. PO 10 mg/kg; IV reference 2 mg/kg. Matrix: plasma. |
| C33 | rat. PO 1 mg/kg; IV reference .3 mg/kg. Matrix: unspecified. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `Cc1cc(C#N)ncc1Oc1cc(Nc2ccc(C(=O)N3CCN(C)CC3)cn2)c2ncn(C)c2n1` |
| M002 | C02 | `CC(C)(O)CCn1cc2cc(NC(=O)c3cccc(C(F)(F)F)n3)c(C(C)(C)O)cc2n1` |
| M003 | C03 | `O=C(Cc1ccc(C2CC2)c(F)c1)N1CCN(c2ccc(Cl)nn2)CC1` |
| M004 | C04 | `C[C@H]1CC[C@H](c2ccc3scnc3c2)N(C(=O)C(=O)Nc2cnc(N)c3cn[nH]c23)C1` |
| M005 | C05 | `CCN1CCN(Cc2ccc3cc(C(=O)Nc4cc(NC(=O)c5ccc6c(c5)OCCO6)ccc4F)ccc3n2)CC1` |
| M006 | C06 | `CC[C@@](O)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2cnn(C3CC3)c(=O)c2nn1C` |
| M007 | C07 | `CC(C)N1CCN(Cc2ccc3cc(C(=O)Nc4cc(NC(=O)c5ccc6c(c5)OCCO6)ccc4Cl)ccc3n2)CC1` |
| M008 | C08 | `COC(=O)N[C@H](C(=O)N1C[C@H](C(F)(F)F)C[C@H]1C(=O)N[C@H](C#N)C[C@@H]1CCCNC1=O)C(C)(C)C` |
| M009 | C09 | `CNS(=O)(=O)c1ccc(Nc2ncc3ccc(C(=O)N4C[C@@H](OC)[C@@H]4C)nc3n2)c(F)c1` |
| M010 | C10 | `CN(C(=O)N1CCN(c2cc3c(cc2F)c(=O)c(C(=O)O)cn3C2CC2)CC1)C(F)(F)F` |
| M011 | C11 | `NCCNC(=O)c1cc2c(ncn2Cc2ccccc2)c(-c2cc(Cl)c(Cl)c(Cl)c2)n1` |
| M012 | C06 | `Cn1nc2c(=O)n(C3CC3)cnc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M013 | C12 | `[2H]C([2H])([2H])C1(C([2H])([2H])[2H])Cn2nc(-c3ccc(F)cn3)c(-c3ccnc4[nH]ncc34)c2CO1` |
| M014 | C13 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@]6(CCO6)C5)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3F)c12` |
| M015 | C14 | `CC(F)(F)c1nnc(N[C@H](c2cn3ncc([C@@H](C4CC4)N4C[C@@H](C(F)(F)F)NC4=O)cc3n2)C2CCC(F)(F)CC2)o1` |
| M016 | C15 | `Cc1nc(-c2onc(C)c2Nc2cncc(OC(C)C)n2)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M017 | C16 | `C=CC(=O)N1CCN([C@@H]2CN(c3cc(N4CCC(c5c(C)cnn5C)CC4)nc(C(F)(F)F)n3)[C@@H]2C)CC1` |
| M018 | C17 | `COC(=O)N[C@H](C(=O)N1C[C@H](C(F)(F)F)C[C@H]1C(=O)N[C@H](C#N)C[C@@H]1CCNC1=O)C(C)(C)C` |
| M019 | C14 | `COC[C@H](c1cnn2cc([C@@H](NC(=O)/C(F)=C\C3(F)CC3)C3CCC(F)(F)CC3)nc2c1)N1C[C@@H](C(F)(F)F)NC1=O` |
| M020 | C18 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3)c1` |
| M021 | C06 | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M022 | C19 | `Cc1c(-c2cc3cc(NC(=O)O[C@H]4COC[C@@H]4C)ncc3c(N)c2F)cnc2c1NCCO2` |
| M023 | C20 | `CNC(=O)c1ncn2c1CC[C@H](c1c(F)ccc(NS(=O)(=O)c3cc(F)cnc3OC)c1F)C2` |
| M024 | C21 | `O=C1CCC(c2c(F)cc(N3CCC4(CCC(CN5CCC(c6ccc7c(c6)-n6c(nc(=O)c8c(Cl)cccc86)C76CCCCC6)CC5)CO4)CC3)cc2F)C(=O)N1` |
| M025 | C13 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@](O)(CF)C5)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3F)c12` |
| M026 | C22 | `Cc1cc(C)n(-c2cccc(C(CC(=O)O)CN3CC(C(F)(F)CCc4ccc5c(n4)NCCC5)C3)c2)n1` |
| M027 | C18 | `O=C(Nc1cccc(-c2nncn2CC2CC2)n1)c1cc2c(cc1F)OCc1cncn1-2` |
| M028 | C23 | `Cc1ncc(S(=O)(=O)N2CCC(c3cn4ncnc4cc3Cl)CC2)s1` |
| M029 | C24 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OC(C)(C)C(=O)N3C)n1` |
| M030 | C25 | `O=C(NCc1ccncc1)Nc1cc(F)c(Oc2ccnc3[nH]cc(C(F)(F)F)c23)c(F)c1` |
| M031 | C26 | `Cc1c(N)cncc1-c1cc2cc(NC(=O)OC3CCOCC3)ncc2c(N)c1F` |
| M032 | C27 | `CCNC(=O)c1c(OC)cc(-n2cnc3cc(-c4cnn(CC)c4)ccc32)cc1OC(F)F` |
| M033 | C28 | `CC(C)(O)CNc1nc(Nc2ccnc(C(F)(F)F)c2)nc(-c2cccc(C(F)(F)F)n2)n1` |
| M034 | C29 | `CC(C)(O)c1cc2nn(CCS(C)(=O)=O)cc2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M035 | C30 | `CC(C)C[C@@H]1NC(=O)[C@@H](N(C)C(=O)[C@@H](NC(=O)[C@@H]2C[C@@H](F)CN2C(=O)C2(C(F)(F)F)CC(F)(F)C2)C2CC2)CCCCCCCN(C)C(=O)[C@H](Cc2cc(Cl)cnc2OC2CC2)N(C)C1=O` |
| M036 | C31 | `CCc1oc2cccc(Br)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M037 | C31 | `CCc1oc2cccc(Cl)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M038 | C18 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCC(=O)N3)n1` |
| M039 | C18 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCC(=O)N3)n1` |
| M040 | C06 | `CC[C@@](N)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ncn(C3CC3)c(=O)c2nn1C` |
| M041 | C06 | `CC[C@@](O)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ccn(C3CC3)c(=O)c2nn1C` |
| M042 | C32 | `Cc1cc(S(=O)(=O)N[C@H]2CC[C@H](CN3CCN(c4cccc(NC5CCC(=O)NC5=O)c4)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M043 | C32 | `C[C@]1(O)CCCN(c2nc(Nc3ccc(S(=O)(=O)N[C@H]4CC[C@H](CN5CCN(c6ccc(C7CCC(=O)NC7=O)cc6F)CC5)CC4)cc3F)ncc2C(F)(F)F)C1` |
| M044 | C33 | `CCC[C@@H](C(=O)Nc1ccc(C(N)=O)c(F)c1)n1cc(OC)c(-c2cc(Cl)ccc2-n2cc(C(F)(F)F)nn2)cc1=O` |
| M045 | C33 | `CC[C@@H](C(=O)Nc1ccc2nccnc2c1)n1cc(OC)c(-c2cc(Cl)ccc2-n2cc(C(F)F)nn2)cc1=O` |

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
