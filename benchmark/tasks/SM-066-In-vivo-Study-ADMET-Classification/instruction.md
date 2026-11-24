---
bench_id: "SM-066-In-vivo-Study-ADMET-Classification"
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
| C01 | mouse; BALB/c. IV 5 mg/kg. Matrix: blood. |
| C02 | rat. IV 2 mg/kg. Matrix: plasma. |
| C03 | dog; beagle. IV 0.5 mg/kg. Matrix: plasma. Vehicle/formulation: 20%DMSO+60%PEG400 in water. |
| C04 | rat. IV 0.3 mg/kg. Matrix: plasma. |
| C05 | rat; Sprague-Dawley. IV 0.5 mg/kg. Matrix: plasma. Vehicle/formulation: 20%DMSO+40%PEG400 in water. Cassette dosing. |
| C06 | dog. IV 0.3 mg/kg. Matrix: plasma. |
| C07 | dog. IV dose unspecified. Matrix: plasma. |
| C08 | mouse; Balb/c; male. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 30% Captisol. |
| C09 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 0.5%DMSO/5%Solutol/5%ethanol/89.5%saline. |
| C10 | mouse; CD-1. IV 1 mg/kg. Matrix: whole blood. Vehicle/formulation: 10%DMSO,35%PEG400;remaining fraction not reported. |
| C11 | rat; Sprague-Dawley; male. IV 0.5 mg/kg. Matrix: plasma. |
| C12 | cynomolgus monkey; cynomolgus. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 1%DMSO/99%20%HP-beta-CD saline. |
| C13 | mouse; CD-1. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: DMSO. |
| C14 | rat. IV 1 mg/kg. Matrix: plasma. |
| C15 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. |
| C16 | rat; Han Wistar. IV dose unspecified. Matrix: blood. |
| C17 | mouse; CD-1; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: PEG200/water 60/40. |
| C18 | rat; Sprague-Dawley; male. IV 0.1 mg/kg. Matrix: plasma. Vehicle/formulation: 10%DMSO/0.1Mphosphate buffer,pH8.5. Cassette dosing. |
| C19 | mouse; ICR; male. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: unspecified. |
| C20 | rat; Sprague-Dawley; male. IV dose unspecified. Matrix: plasma. |
| C21 | mouse; CD-1; male. IV 1 mg/kg. Matrix: plasma. |
| C22 | rat. IV dose unspecified. Matrix: plasma. |
| C23 | rat. IV dose unspecified. Matrix: blood. |
| C24 | rat; Sprague-Dawley; male. IV .5 mg/kg. Matrix: plasma. |
| C25 | rat. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 10% DMSO/40% PEG400/50% water. |
| C26 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 10% EtOH/40% PEG400/50% saline. |
| C27 | mouse; C57BL/6J; female. IV 2 mg/kg. Matrix: plasma. |
| C28 | mouse; C57BLKS; female. IV 1 mg/kg. Matrix: plasma. Cassette dosing. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `CCN1CCN(Cc2ccc3cc(C(=O)Nc4cc(NC(=O)c5ccc6c(c5)OCCO6)ccc4Cl)ccc3n2)CC1` |
| M002 | C02 | `Cc1cc(S(=O)(=O)NCCO[C@H]2CC[C@H](CN3CCC(c4ccc5c(c4F)n(C)c(=O)n5C4CCC(=O)NC4=O)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c([C@H]2CC[C@@](C)(O)CC2)n1` |
| M003 | C03 | `COc1c(Cl)cccc1Nc1c(-c2ccnc(C)n2)[nH]c2c1C(=O)NC[C@H]2C[C@@H]1COCCO1` |
| M004 | C04 | `COc1cn([C@@H](C[C@@H]2CCCCO2)C(=O)Nc2ccc(C(=O)O)cc2)c(=O)cc1-c1cc(Cl)ccc1C#N` |
| M005 | C05 | `COCC[C@@]1(C)CNC(=O)c2c1[nH]c(-c1ccncc1F)c2Nc1cccc(Cl)c1OC` |
| M006 | C06 | `CC[C@@H](C(=O)Nc1ccc(C(=O)O)cc1)n1cc(OC)c(-c2cc(Cl)ccc2C#N)cc1=O` |
| M007 | C07 | `CC(C)(O)c1cc2nc([C@H]3CC[C@H](CN4CC5(CC(CCNc6cccc7c6C(=O)N(C6CCC(=O)NC6=O)C7=O)C5)C4)CC3)sc2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M008 | C08 | `C[C@@H]1CN(c2ccc(Cl)nn2)CCN1C(=O)Cc1ccc(C2CC2)cc1` |
| M009 | C09 | `C[C@@H](Nc1nc(N[C@H](C)C(F)(F)F)nc(C2=C(F)[C@H](O)C(F)(F)CC2)n1)C(F)(F)F` |
| M010 | C10 | `CNS(=O)(=O)c1ccc(Nc2ncc3ccc(C(=O)N4C[C@@H](OC)[C@@H]4C)nc3n2)c(F)c1` |
| M011 | C11 | `O=C1COc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc2N1` |
| M012 | C12 | `CCc1cc(NC(=O)C(=O)N2C[C@@H](C)CC[C@@H]2c2ccc3sc(C4CCN(C)CC4)nc3c2)cnc1N` |
| M013 | C13 | `C=CC(=O)N1CCN([C@@H]2CN(c3cc(N4CCC(c5c(C)cnn5C)CC4)nc(C(F)(F)F)n3)[C@@H]2C)CC1` |
| M014 | C14 | `CCn1ccc2c([C@@](O)(CC)c3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M015 | C15 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCc2cncn2-3)c1` |
| M016 | C16 | `CC[C@@H]1CN(Cc2cc([C@H](CC(=O)O)c3ccc4c(nnn4CC)c3C)ccc2C)S(=O)(=O)c2cccnc2O1` |
| M017 | C17 | `CCNC(=O)c1c(OC)cc(-n2cnc3cc(-c4cnn(C)c4)ccc32)cc1OC(F)F` |
| M018 | C18 | `CCc1oc2cccc(Cl)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M019 | C14 | `Cc1nn(C2CC2)c(=O)c2nn(C)c(Cc3ccc(C(F)(F)F)c(C#N)c3)c12` |
| M020 | C19 | `CN1CCN(c2cccc(-c3c(-c4cnn(C)c4)oc4ncnc(Oc5ccc(NC(=O)c6cccn(-c7ccc(F)cc7)c6=O)cc5)c34)c2)CC1` |
| M021 | C15 | `CC(CO)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCC(=O)N3)n1` |
| M022 | C20 | `C=CC(=O)N1CC[C@H]2[C@H]1C[C@]2(C)Oc1nc(-c2cnn(C)c2)cn2nccc12` |
| M023 | C14 | `CC[C@@](O)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ccn(C3CC3)c(=O)c2nn1C` |
| M024 | C21 | `O=C1CCC(c2c(F)cc(N3CCC4(CCC(CN5CCC(c6ccc7c(c6)-n6c(nc(=O)c8c(Cl)cccc86)C76CCCCC6)CC5)CO4)CC3)cc2F)C(=O)N1` |
| M025 | C22 | `COc1cc2nn([C@H]3CC[C@H](CN4CC5(CC(CCNc6cccc7c6C(=O)N(C6CCC(=O)NC6=O)C7=O)C5)C4)CC3)cc2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M026 | C23 | `COc1c(Cl)cccc1Nc1c(-c2ccncc2C#C[C@@]2(C)CCCN2C(=O)/C=C/CN(C)C)[nH]c2c1C(=O)NCC2` |
| M027 | C15 | `O=C(Nc1cccc(-c2nncn2CC2CC2)n1)c1cc2c(cc1F)OCc1cncn1-2` |
| M028 | C02 | `C[C@H]1CN(c2ccc(C3CCC(=O)NC3=O)cc2F)CCN1CC12CCC(NS(=O)(=O)c3ccc(Nc4ncc(C(F)(F)F)c(N5CCC[C@](C)(O)C5)n4)c(F)c3)(CC1)CO2` |
| M029 | C24 | `Cc1c(N)cncc1-c1cc2cc(NC(=O)OC3CCOCC3)ncc2c(N)c1F` |
| M030 | C04 | `CCC[C@@H](C(=O)Nc1ccc(C(N)=O)c(F)c1)n1cc(OC)c(-c2cc(Cl)ccc2-n2cc(C(F)(F)F)nn2)cc1=O` |
| M031 | C25 | `O=C1CCC(n2c(=O)[nH]c3ccccc32)C(=O)N1` |
| M032 | C21 | `CON(C(=O)c1cc(F)ccc1Oc1nncnc1N1CC2(CCN(CC3(C)CC3)CC2)C1)C(C)C` |
| M033 | C26 | `Cc1ncc(S(=O)(=O)N2CCC(c3cn4ncnc4cc3Cl)CC2)s1` |
| M034 | C27 | `Cc1nc(-c2cnn(C)c2NC(=O)O[C@H](C)c2ccccc2Cl)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M035 | C27 | `Cc1noc(-c2ccc(NC(=O)[C@H]3CCCC[C@@H]3C(=O)O)cn2)c1NC(=O)O[C@H](C)c1ccccc1Cl` |
| M036 | C15 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3C)c1` |
| M037 | C15 | `CN1C(=O)CCCc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc21` |
| M038 | C08 | `O=C(Cc1ccc(C2CC2)cc1)N1CCN(c2ccc(Cl)nn2)CC1` |
| M039 | C08 | `O=C(Cc1ccc(C2CC2)cc1F)N1CCN(c2ccc(Cl)nn2)CC1` |
| M040 | C28 | `Cc1cccc(CN(C)c2ncnc3[nH]c(-c4ccc(C(=O)O)cc4)cc23)c1` |
| M041 | C28 | `Cc1cccc(CN(C)c2ncnc3[nH]c(-c4ccc(CCC(=O)O)cc4)cc23)c1` |
| M042 | C02 | `Cc1cc(S(=O)(=O)N[C@]2(C)C[C@H](N3CCN(CC4CCN(c5ccc6c(c5F)n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)CC3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M043 | C02 | `Cc1cc(S(=O)(=O)N[C@H]2C[C@H](N3CCN(CC4CCN(c5ccc6c(c5F)n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)CC3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCCC(C)(O)C2)n1` |
| M044 | C02 | `Cc1cc(S(=O)(=O)N[C@H]2C[C@H](N3CCN(CC4CCN(c5ccc(NC6CCC(=O)NC6=O)cc5C)CC4)CC3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M045 | C02 | `[2H]C(C)(CO[C@H]1CC[C@H](CN2CCN(c3ccc4c(c3F)n(C)c(=O)n4C3CCC(=O)NC3=O)CC2)CC1)NS(=O)(=O)c1ccc(Nc2ncc(C(F)(F)F)c([C@H]3CC[C@@](C)(O)CC3)n2)c(C)c1` |

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

## 2. Analogue comparisons

Compare IV Vss. Let R = value(left) / value(right). Choose A if R > 2; B if 1/2 <= R <= 2; C if R < 1/2.

Each pair belongs to one literature analogue family and one study context. B denotes only the specified numerical difference category; it does not establish statistical equivalence. No cross-species or cross-dose comparison is requested.

| Item | Left molecule | Right molecule | Points |
|---|---|---|---|
| Q034 | M034 | M035 | 6 |
| Q035 | M036 | M037 | 6 |
| Q036 | M038 | M039 | 6 |
| Q037 | M040 | M041 | 6 |

## 3. Within-series ordering

Order each group from largest to smallest IV Vss.

Each group shares one study context. Its score is the listed points multiplied by max(0, Spearman rho) between the submitted and reference orders.

| Item | Molecules to order | Points |
|---|---|---|
| Q038 | M042, M043, M044, M045 | 10 |

## Response format and scoring

Return ONLY a strict JSON object mapping each listed Q identifier to L/M/H for interval items, A/B/C for comparisons, or an ordered array of the listed molecule IDs for ordering items.

Syntax example only; these values do not imply answers:

`{"Q001": "L", "Q034": "B", "Q038": ["M042", "M043", "M044", "M045"]}`

Each molecule is assessed in one item. Missing or invalid items earn zero. An ordering array must contain every specified molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0–1 scale.
