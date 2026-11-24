---
bench_id: "SM-057-In-vivo-Study-ADMET-Classification"
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
| C01 | mouse; CD-1; male. PO 10 mg/kg; IV reference 10 mg/kg. Matrix: plasma. Vehicle/formulation: DMSO/Cremophor/PBS10/10/80. |
| C02 | rat; Sprague-Dawley; male. PO 3 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: PO1%MC400aqueous,10mL/kg; IVvehicle not specified in inspected SI. |
| C03 | mouse; Balb/c; male. PO 10 mg/kg; IV reference 2 mg/kg. Matrix: plasma. Vehicle/formulation: IV30%Captisol; PO formulation not separately assigned. |
| C04 | rat. PO 10 mg/kg; IV reference 2 mg/kg. Matrix: plasma. |
| C05 | rat; Han Wistar; male. PO 0.5 mg/kg; IV reference 0.5 mg/kg. Matrix: plasma. Vehicle/formulation: IV5%DMSO/95%SBE-beta-CD(30%w/v); PO0.5%HPMC/0.1%Tween in water. Cassette dosing. |
| C06 | rat; Sprague-Dawley; male. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: plasma. |
| C07 | rat. PO 1 mg/kg; IV reference .3 mg/kg. Matrix: unspecified. |
| C08 | rat; SD. PO 5 mg/kg; IV reference 5 mg/kg. Matrix: blood. |
| C09 | rat; Wistar; male. PO 1 mg/kg; IV reference 0.5 mg/kg. Matrix: reported blood basis. |
| C10 | rat; Sprague-Dawley; male. PO 3 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: PO: 0.5% w/v HPMC,0.5% v/v benzyl alcohol,0.4% v/v polysorbate80 in water; IV:5-10% w/v Trappsol with5-10% DMSO. Feeding: overnight fast; food restored4 h. |
| C11 | mouse; ICR; male. PO 10 mg/kg; IV reference 2.5 mg/kg. Matrix: plasma. |
| C12 | rat. PO 3 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: 5%DMSO/10%Solutol/85%saline. Feeding: fasted. |
| C13 | rat; Sprague-Dawley; male. PO 2.5 mg/kg; IV reference 0.5 mg/kg. Matrix: plasma. |
| C14 | mouse; CD-1; male. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: IVPEG200/water60/40; POSolutolHS15/0.5%MC2/98. |
| C15 | mouse; BALB/c. PO 5 mg/kg; IV reference 5 mg/kg. Matrix: blood. |
| C16 | mouse; C57BL/6J; female. PO 30 mg/kg; IV reference 2 mg/kg. Matrix: plasma. |
| C17 | rat; Wistar; male. PO 0.6 mg/kg; IV reference 0.3 mg/kg. Matrix: reported blood basis. |
| C18 | rat. PO 5 mg/kg; IV reference 2 mg/kg. Matrix: unspecified. Vehicle/formulation: PO20%HP-beta-CD/80%water; IV10%DMSO/40%PEG400/50%water. |
| C19 | mouse; CD1. PO 5 mg/kg; IV reference dose unspecified. Matrix: plasma. |
| C20 | rat. PO 3 mg/kg; IV reference dose unspecified. Matrix: unspecified. |
| C21 | rat. PO 11 mg/kg; IV reference 1.1 mg/kg. Matrix: plasma. Vehicle/formulation: IV10%EtOH/70%PEG400/20%saline; PO0.5%MC/0.1%Tween80saline; not assigned. |
| C22 | rat. PO 10 mg/kg; IV reference 2 mg/kg. Matrix: unspecified. Vehicle/formulation: PO20%HP-beta-CD/80%water; IV10%DMSO/40%PEG400/50%water. |
| C23 | mouse; CD1. PO 100 mg/kg; IV reference dose unspecified. Matrix: plasma. |
| C24 | mouse; CD-1; male. PO 5 mg/kg; IV reference 1 mg/kg. Matrix: plasma. Vehicle/formulation: IVPEG200/water60/40; POSolutol/0.5%MC2/98. Feeding: fasted. |
| C25 | rat; Han Wistar; male. PO 1 mg/kg; IV reference 0.5 mg/kg. Matrix: plasma. Vehicle/formulation: IV5%DMSO/95%SBE-beta-CD(30%w/v); PO0.5%HPMC/0.1%Tween in water. Cassette dosing. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `O=S(=O)(NCCN1CCNCC1)c1ccc(NC2CCCCC2)c(NCc2ccccc2)c1` |
| M002 | C02 | `COc1ncc(Cl)cc1S(=O)(=O)Nc1ccc(F)c(-c2ccc3c(-c4ncc[nH]4)n[nH]c3c2F)c1F` |
| M003 | C03 | `O=C(Cc1ccc(C2CC2)cc1F)N1CCN(c2ccc(Cl)nn2)CC1` |
| M004 | C04 | `Cc1cc(S(=O)(=O)N[C@H]2C[C@H](N3CCN(CC4CCN(c5ccc6c(c5F)n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)CC3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCCC(C)(O)C2)n1` |
| M005 | C05 | `CN(C)C(=O)N1CCN(c2cc3c(cc2F)c(=O)c(C(=O)O)cn3C2CC2)CC1` |
| M006 | C06 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)C(C)(C)CC(=O)N3)n1` |
| M007 | C07 | `CC[C@@H](C(=O)Nc1ccc(C(=O)O)cc1)n1cc(OC)c(-c2cc(Cl)ccc2C#N)cc1=O` |
| M008 | C08 | `Cc1ccc(NC(=O)c2ccc3c(c2)OCCO3)cc1NC(=O)c1ccc2nc(OCCN3CCCC3)ccc2c1` |
| M009 | C04 | `Cc1cc(S(=O)(=O)N[C@H]2C[C@H](N3CCN(CC4CCN(c5cccc6c5n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)C4(CC4)C3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M010 | C09 | `OC[C@@]1(F)CN=C(Nc2cc(F)c(Oc3ccnc4[nH]cc(C(F)(F)F)c34)c(F)c2)OC1` |
| M011 | C10 | `CCn1cc(C2CC2)c2c(Cc3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M012 | C11 | `C[C@@H](Nc1nc(N[C@H](C)C(F)(F)F)nc(C2=C(F)[C@H](O)C(F)(F)CC2)n1)C(F)(F)F` |
| M013 | C04 | `CNS(=O)(=O)c1ccc(Nc2ncc(C(F)(F)F)c(N3CCC(C)(O)CC3)n2)c(C)c1` |
| M014 | C12 | `O=C1CC[C@H](N2Cc3c(ccc4c3OCC43CCN(C[C@@H]4CCC5(CCN(c6ccc([C@@H]7c8ccc(O)cc8CC[C@@H]7c7ccccc7)cc6)CC5)OC4)CC3)C2=O)C(=O)N1` |
| M015 | C13 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OC(C)(C)C(=O)N3)n1` |
| M016 | C07 | `CCC[C@@H](C(=O)Nc1ccc(C(N)=O)c(F)c1)n1cc(OC)c(-c2cc(Cl)ccc2-n2cc(C(F)F)nn2)cc1=O` |
| M017 | C14 | `Cc1cc(C#N)ncc1Oc1cc(Nc2ccc(C(=O)N3CCOCC3)cn2)c2ncn(C)c2n1` |
| M018 | C03 | `C[C@@H]1CN(c2ccc(Cl)nn2)CCN1C(=O)Cc1ccc(C2CC2)cc1` |
| M019 | C15 | `Cc1ccc(NC(=O)c2ccc3c(c2)OCCO3)cc1NC(=O)c1ccc2nc(CN3CCN(C(C)C)CC3)ccc2c1` |
| M020 | C16 | `Cc1nc(-c2onc(C)c2NC(=O)O[C@H](C)c2ccccc2)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M021 | C17 | `Fc1cc(NC2=NC[C@]3(CCOC3)CO2)cc(F)c1Oc1ccnc2[nH]cc(C3(C(F)(F)F)CC3)c12` |
| M022 | C15 | `Cc1ccc(NC(=O)c2ccc3c(c2)OCCO3)cc1NC(=O)c1ccc2nc(OCCN3CCCCC3)ccc2c1` |
| M023 | C04 | `Cc1cc(S(=O)(=O)N[C@]2(C)C[C@H](N3CCN(CC4CCN(c5ccc6c(c5F)n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)CC3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M024 | C18 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(CCCOC3CCN(C[C@H]4CC[C@H](n5cc(NC(=O)c6cnn7ccc(N8C[C@H]9C[C@@H]8CO9)nc67)c(C(F)F)n5)CC4)CC3)c21` |
| M025 | C19 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5C[C@H]6CC[C@@H](C5)N6)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3F)c12` |
| M026 | C04 | `Cc1cc(S(=O)(=O)N[C@H](C)CO[C@H]2CC[C@H](CN3CCN(c4ccc5c(c4F)n(C)c(=O)n5C4CCC(=O)NC4=O)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c([C@H]2CC[C@@](C)(O)CC2)n1` |
| M027 | C04 | `C[C@]1(O)CCCN(c2nc(Nc3ccc(S(=O)(=O)N[C@H]4CC[C@H](CN5CCN(c6ccc(C7CCC(=O)NC7=O)c(F)c6)CC5)CC4)cc3F)ncc2C(F)(F)F)C1` |
| M028 | C18 | `CN(CCCOCCCc1cccc2c1n(C)c(=O)n2C1CCC(=O)NC1=O)C[C@H]1CC[C@H](n2cc(NC(=O)c3cnn4ccc(N5C[C@H](N)CC(F)(F)C5)nc34)c(C(F)F)n2)CC1` |
| M029 | C20 | `COC[C@H](c1cnn2cc([C@@H](Nc3nnc(C(C)(F)F)o3)C3CCC(F)(F)CC3)nc2c1)N1C[C@@H](C(F)(F)F)NC1=O` |
| M030 | C21 | `[2H]C1([2H])CC(c2cn3ncnc3cc2Cl)CC([2H])([2H])N1S(=O)(=O)c1cnc(C)o1` |
| M031 | C17 | `COCCNC(=O)Nc1cc(F)c(Oc2ccnc3[nH]cc(C(F)(F)F)c23)c(F)c1` |
| M032 | C06 | `CC(CO)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCC(=O)N3)n1` |
| M033 | C22 | `Nc1cccc2c1C(=O)N(C1CCC(=O)NC1=O)C2=O` |
| M034 | C19 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCOC[C@@](C)(O)C5)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3F)c12` |
| M035 | C23 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@@](C)(O)C5)nc(OC[C@@]56CCCN5C[C@H](F)C6)nc4c3F)c12` |
| M036 | C10 | `Cn1nc2c(=O)n(C3CC3)ncc2c1[C@](N)(c1ccc(C(F)(F)F)c(Cl)c1)C1CC1` |
| M037 | C10 | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C1CC1` |
| M038 | C24 | `COc1cc(-n2cnc3cc(-c4cnn(C)c4)ccc32)cc(OC(F)F)c1C(=O)NC1CC1` |
| M039 | C24 | `CCNC(=O)c1c(OC)cc(-n2cnc3cc(-c4cnn(C)c4)ccc32)cc1OC(F)F` |
| M040 | C06 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCC(=O)N3)c1` |
| M041 | C06 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCc2cncn2-3)c1` |
| M042 | C25 | `CN(C(=O)N1CCN(c2cc3c(cc2F)c(=O)c(C(=O)O)cn3C2CC2)CC1)C1CC1` |
| M043 | C25 | `CC(C)N(C(=O)N1CCN(c2cc3c(cc2F)c(=O)c(C(=O)O)cn3C2CC2)CC1)C1CC1` |
| M044 | C04 | `C[C@H]1CN(CC2CCN(c3ccc(C4CCC(=O)NC4=O)cc3F)CC2)CC[C@H]1NS(=O)(=O)c1ccc(Nc2ncc(C(F)(F)F)c(N3CCC[C@](C)(O)C3)n2)c(F)c1` |
| M045 | C04 | `C[C@H]1CN(c2ccc(C3CCC(=O)NC3=O)cc2F)CCN1CC12CCC(NS(=O)(=O)c3ccc(Nc4ncc(C(F)(F)F)c(N5CCC[C@](C)(O)C5)n4)c(F)c3)(CC1)CO2` |

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
