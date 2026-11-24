---
bench_id: "SM-063-In-vivo-Study-ADMET-Classification"
category: "In-vivo-Study"
format: "structured_json"
---
# Prompt

Predict steady-state volume of distribution after intravenous administration (Vss) under the stated study conditions. This task contains 45 distinct molecules and is worth 100 points.

Predict the reported IV Vss. This is not terminal volume (Vz) or apparent oral volume (V/F).

Vss describes an apparent distribution volume relative to the sampled systemic matrix. A larger Vss does not by itself demonstrate more unbound drug in a particular target tissue.

Use the study context assigned to each molecule. PO means oral administration; IV means intravenous administration. Conditions not listed are unspecified.

## Study contexts

| Context | Conditions |
|---|---|
| C01 | dog; beagle; male. IV 0.5 mg/kg. Matrix: plasma. Vehicle/formulation: 30% HP-beta-CD/70% water. |
| C02 | rat. IV 2 mg/kg. Matrix: plasma. |
| C03 | dog; Beagle; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: PEG200/water 60/40. Feeding: fasted. |
| C04 | dog; beagle. IV 0.5 mg/kg. Matrix: plasma. Vehicle/formulation: 20%DMSO+60%PEG400 in water. |
| C05 | rat; Sprague-Dawley. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 20%HP-beta-CD solution. Feeding: fed. |
| C06 | rat. IV dose unspecified. Matrix: plasma. |
| C07 | rat; Sprague-Dawley; male. IV .5 mg/kg. Matrix: plasma. |
| C08 | rat. IV dose unspecified. Matrix: blood. |
| C09 | dog; Beagle. IV 0.5 mg/kg. Matrix: plasma. Vehicle/formulation: 30% Captisol/70% water. |
| C10 | rat; Wistar-Han; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 10% DMSO/30% PEG400/60% water. |
| C11 | rat; Han Wistar. IV dose unspecified. Matrix: blood. |
| C12 | mouse; BALB/c. IV 5 mg/kg. Matrix: blood. |
| C13 | mouse. IV 3 mg/kg. Matrix: plasma. Vehicle/formulation: 10%NMP/5%Solutol/85%normal saline. |
| C14 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. |
| C15 | rat. IV 1 mg/kg. Matrix: plasma. |
| C16 | rat. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: EtOH/PEG300/water 1:4:5v/v. |
| C17 | rat. IV 0.3 mg/kg. Matrix: plasma. |
| C18 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: PEG200/water60/40. |
| C19 | rat; Sprague-Dawley; male. IV 0.5 mg/kg. Matrix: plasma. |
| C20 | mouse; ICR; male. IV 3 mg/kg. Matrix: plasma. Vehicle/formulation: unspecified. |
| C21 | rat; Sprague-Dawley; male. IV 0.1 mg/kg. Matrix: plasma. Vehicle/formulation: 10%DMSO/0.1Mphosphate buffer,pH8.5. Cassette dosing. |
| C22 | mouse; C57BLKS; female. IV 1 mg/kg. Matrix: plasma. Cassette dosing. |
| C23 | rat. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 10%EtOH/40%PEG/50%saline. |
| C24 | mouse; C57BL/6J; female. IV 2 mg/kg. Matrix: plasma. |
| C25 | mouse; CD1; male. IV 3 mg/kg. Matrix: plasma. Vehicle/formulation: 10%NMP/5%Solutol/85%normal saline. |
| C26 | rat; SD. IV 5 mg/kg. Matrix: blood. |
| C27 | mouse; Balb/c; male. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 30% Captisol. |
| C28 | mouse; ICR; male. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: unspecified. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `CS(=O)(=O)c1cncc(C(=O)N2[C@@H](C(=O)N[C@@H](c3cc(F)c(Cl)cc3F)C3CC3)C[C@H]3C[C@H]32)c1` |
| M002 | C02 | `Cc1cc(S(=O)(=O)NCCO[C@H]2CC[C@H](CN3CCC(c4ccc5c(c4)n(C)c(=O)n5C4CCC(=O)NC4=O)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c([C@H]2CC[C@@](C)(O)CC2)n1` |
| M003 | C03 | `COc1cc(-n2cnc3cc(-c4cnn(C)c4)ccc32)cc(OC(F)F)c1C(=O)NC1CC1` |
| M004 | C04 | `COc1c(Cl)cccc1Nc1c(-c2ccncc2F)[nH]c2c1C(=O)NC[C@@H]2C[C@@H]1COCCO1` |
| M005 | C05 | `CC1(C)Cn2nc(-c3ccc(F)cn3)c(-c3ccnc4[nH]ncc34)c2CO1` |
| M006 | C06 | `COc1cc2nc([C@H]3CC[C@H](CN4CC5(CC(CCNc6cccc7c6C(=O)N(C6CCC(=O)NC6=O)C7=O)C5)C4)CC3)sc2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M007 | C07 | `Cc1c(-c2cc3cc(NC(=O)OC4CCOCC4)ncc3c(N)c2F)cnc2c1NCCO2` |
| M008 | C08 | `COc1cc2nn(CCC(C)(C)O)cc2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M009 | C09 | `C=CC(=O)N1CCN([C@@H]2CN(c3cc(N4CCC(c5c(C)ccnc5C5(OC)COC5)CC4)nc(C(F)(F)F)n3)[C@@H]2C)CC1` |
| M010 | C10 | `COC(=O)N[C@H](C(=O)N1C[C@H](C(F)(F)F)C[C@H]1C(=O)N[C@H](C#N)C[C@@H]1CCNC1=O)C(C)(C)C` |
| M011 | C06 | `CN(CCCO[C@H]1C[C@H](Nc2cccc3c2C(=O)N(C2CCC(=O)NC2=O)C3=O)C1)C[C@H]1CC[C@H](n2cc3cc(NC(=O)c4cccc(C(F)(F)F)n4)c(C(C)(C)O)cc3n2)CC1` |
| M012 | C06 | `COc1cc2nc([C@H]3CC[C@H](CN4CC5(CC(CCNc6cccc7c6C(=O)N(C6CCC(=O)NC6=O)C7=O)C5)C4)CC3)n(C)c2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M013 | C11 | `CC[C@@H]1CN(Cc2cc([C@@H](CC(=O)O)c3ccc4c(nnn4CC)c3C)ccc2C)S(=O)(=O)c2cccnc2O1` |
| M014 | C12 | `Cc1ccc(NC(=O)c2ccc3c(c2)OCCO3)cc1NC(=O)c1ccc2nc(CN3CCN(C(C)C)CC3)ccc2c1` |
| M015 | C13 | `COC1CCN(Cc2ccc(-c3cn([C@H]4CC[C@H](O)CC4)c4nc(Nc5cc(C(F)(F)F)cc(C(F)(F)F)c5)ncc34)cc2)CC1` |
| M016 | C14 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCC(=O)N3)n1` |
| M017 | C15 | `CC[C@@](N)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ncn(C3CC3)c(=O)c2nn1C` |
| M018 | C06 | `CC(C)(O)c1cc2nn([C@H]3CC[C@H](CN4CCC5(CC4)CC(CNc4cccc6c4C(=O)N(C4CCC(=O)NC4=O)C6=O)C5)CC3)cc2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M019 | C16 | `CC(C)C[C@@H](O)C(=O)N1CC2(CC2)C[C@H]1C(=O)N[C@@H](C[C@@H]1CCNC1=O)C(=O)COC(F)(F)F` |
| M020 | C17 | `CCC[C@@H](C(=O)Nc1ccc(C(N)=O)c(F)c1)n1cc(OC)c(-c2cc(Cl)ccc2-n2cc(C(F)F)nn2)cc1=O` |
| M021 | C02 | `Cc1cc(S(=O)(=O)N[C@H]2CC[C@H](CN3CCN(c4cccc(NC5CCC(=O)NC5=O)c4)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M022 | C18 | `Cc1cc(C#N)ncc1Oc1cc(Nc2ccc(N3CCOCC3)nn2)c2ncn(C)c2n1` |
| M023 | C19 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OC(C)(C)C(=O)N3)n1` |
| M024 | C20 | `Cn1cc(-c2oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c3c2-c2cccc(N)c2)cn1` |
| M025 | C06 | `COc1cc2nc([C@H]3CC[C@H](CN4CC5(CC(CCNc6cccc7c6C(=O)N(C6CCC(=O)NC6=O)C7=O)C5)C4)CC3)oc2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M026 | C21 | `CCc1oc2cccc(I)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M027 | C22 | `Cc1cccc(CN(C)c2ncnc3[nH]c(-c4ccc(CO)cc4)cc23)c1` |
| M028 | C12 | `CCN1CCN(Cc2ccc3cc(C(=O)Nc4cc(NC(=O)c5ccc6c(c5)OCCO6)ccc4F)ccc3n2)CC1` |
| M029 | C06 | `CC(C)(O)c1cc2nn([C@H]3CC[C@H](CN4CCC5(CC4)CC(Nc4cccc6c4C(=O)N(C4CCC(=O)NC4=O)C6=O)C5)CC3)cc2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M030 | C02 | `CNS(=O)(=O)c1ccc(Nc2ncc(C(F)(F)F)c(N3CCC(C)(O)CC3)n2)c(C)c1` |
| M031 | C23 | `Cn1nc(-c2ccnn2C)cc1CNC(=O)c1cc(-c2ccco2)ccc1Cl` |
| M032 | C24 | `Cc1nc(-c2nnn(C)c2NC(=O)O[C@H](C)c2ccccc2Cl)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M033 | C25 | `CN1CCN(Cc2ccc(-c3cn([C@H]4CC[C@@H](O)CC4)c4nc(Nc5cc(C(F)(F)F)cc(C(F)(F)F)c5)ncc34)cc2)CC1` |
| M034 | C26 | `Cc1ccc(NC(=O)c2ccc3c(c2)OCCO3)cc1NC(=O)c1ccc2nc(OCCN3CCCC3)ccc2c1` |
| M035 | C15 | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M036 | C15 | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1ccc(C(F)(F)F)nc1)C1CC1` |
| M037 | C15 | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C1CC1` |
| M038 | C15 | `Cn1nc2c(=O)n(C3CC3)ncc2c1[C@](N)(c1ccc(C(F)(F)F)c(Cl)c1)C1CC1` |
| M039 | C27 | `O=C(Cc1ccc(C2CC2)c(F)c1)N1CCN(c2ccc(Cl)nn2)CC1` |
| M040 | C27 | `CN(C)c1ccc(CC(=O)N2CCN(c3ccc(Cl)nn3)CC2)cc1` |
| M041 | C28 | `Cn1cc(-c2oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c3c2-c2cccc(CN)c2)cn1` |
| M042 | C28 | `CC(=O)Nc1cccc(-c2c(-c3cnn(C)c3)oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c23)c1` |
| M043 | C02 | `Cc1cc(S(=O)(=O)N[C@H]2C[C@H](N3CCN(CC4CCN(c5cccc6c5n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)C4(CC4)C3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M044 | C02 | `Cc1cc(S(=O)(=O)N[C@@H](C)CO[C@H]2CC[C@H](CN3CCN(c4ccc5c(c4F)n(C)c(=O)n5C4CCC(=O)NC4=O)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c([C@H]2CC[C@@](C)(O)CC2)n1` |
| M045 | C02 | `Cc1cc(S(=O)(=O)N[C@H]2CC[C@H](N3CCN(CC4CCN(c5cccc6c5n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |

## 1. Interval prediction

Assign L, M, or H using the following ranges (L/kg). These are numerical endpoint ranges under the listed animal-study conditions, rather than universal development criteria.

| Label | Interval | Interpretation |
|---|---|---|
| L | value < 1 | Smaller apparent steady-state distribution volume |
| M | 1 <= value < 5 | Intermediate apparent steady-state distribution volume |
| H | value >= 5 | Larger apparent steady-state distribution volume |

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

Compare IV Vss. Let R = value(left) / value(right). Choose A if R > 2; B if 1/2 <= R <= 2; C if R < 1/2.

Each pair belongs to one literature analogue family and one study context. B denotes only the specified numerical difference category; it does not establish statistical equivalence. No cross-species or cross-dose comparison is requested.

| Item | Left molecule | Right molecule | Points |
|---|---|---|---|
| Q035 | M035 | M036 | 6 |
| Q036 | M037 | M038 | 6 |
| Q037 | M039 | M040 | 6 |
| Q038 | M041 | M042 | 6 |

## 3. Within-series ordering

Order each group from largest to smallest IV Vss.

Each group shares one study context. Its score is the listed points multiplied by max(0, Spearman rho) between the submitted and reference orders.

| Item | Molecules to order | Points |
|---|---|---|
| Q039 | M043, M044, M045 | 8 |

## Response format and scoring

Return ONLY a strict JSON object mapping each listed Q identifier to L/M/H for interval items, A/B/C for comparisons, or an ordered array of the listed molecule IDs for ordering items.

Syntax example only; these values do not imply answers:

`{"Q001": "L", "Q035": "B", "Q039": ["M043", "M044", "M045"]}`

Each molecule is assessed in one item. Missing or invalid items earn zero. An ordering array must contain every specified molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0–1 scale.
