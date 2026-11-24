---
bench_id: "SM-064-In-vivo-Study-ADMET-Classification"
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
| C01 | mouse; CD-1; male. IV 10 mg/kg. Matrix: plasma. Vehicle/formulation: DMSO/Cremophor/PBS10/10/80. |
| C02 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. |
| C03 | rat; Wistar-Han; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 10% DMSO/50% PEG400/40% water. |
| C04 | mouse; Balb/c; male. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 30% Captisol. |
| C05 | rat. IV dose unspecified. Matrix: plasma. |
| C06 | rat. IV 1 mg/kg. Matrix: plasma. |
| C07 | mouse; C57BL/6; female. IV 1 mg/kg. Matrix: blood. |
| C08 | mouse; CD-1; male. IV 1 mg/kg. Matrix: plasma. |
| C09 | rat. IV 2 mg/kg. Matrix: plasma. |
| C10 | rat. IV 0.3 mg/kg. Matrix: plasma. |
| C11 | rat. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 5%DMSO/10%Solutol/85%saline. Feeding: fasted. |
| C12 | rat; Han Wistar. IV dose unspecified. Matrix: blood. |
| C13 | mouse; CD-1; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: PEG200/water 60/40. |
| C14 | rat. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 10% DMSO/40% PEG400/50% water. |
| C15 | dog; beagle; male. IV 0.5 mg/kg. Matrix: plasma. Vehicle/formulation: 30% HP-beta-CD/70% water. |
| C16 | rat. IV dose unspecified. Matrix: blood. |
| C17 | rat; Sprague-Dawley; male. IV dose unspecified. Matrix: plasma. |
| C18 | cynomolgus monkey; cynomolgus. IV dose unspecified. Matrix: plasma. Vehicle/formulation: 1%DMSO/99%20%HP-beta-CD saline. |
| C19 | mouse; ICR; male. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: unspecified. |
| C20 | rat; Sprague-Dawley. IV 0.5 mg/kg. Matrix: plasma. Vehicle/formulation: 20%DMSO+40%PEG400 in water. Cassette dosing. |
| C21 | dog. IV 0.5 mg/kg. Matrix: blood. |
| C22 | mouse; C57BLKS; female. IV 1 mg/kg. Matrix: plasma. Cassette dosing. |
| C23 | mouse; C57BL/6J; female. IV 2 mg/kg. Matrix: plasma. |
| C24 | mouse; CD-1. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: DMSO. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `Nc1cc(-c2cnco2)ccc1NC1CCCCC1` |
| M002 | C02 | `O=C1CCCc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc2N1` |
| M003 | C03 | `COC(=O)N[C@H](C(=O)N1C[C@H](OC(F)(F)F)C[C@H]1C(=O)N[C@H](C#N)C[C@@H]1CCNC1=O)C(C)(C)C` |
| M004 | C02 | `O=C(Nc1cccc(-c2nncn2CC2CC2)c1)c1cc2c(cc1F)OCc1cncn1-2` |
| M005 | C04 | `C[C@@H]1CN(c2ccc(Cl)nn2)CCN1C(=O)Cc1ccc(C2CC2)c(F)c1` |
| M006 | C05 | `C=CC(=O)N1CCC[C@@H]1C#Cc1cnccc1-c1[nH]c2c(c1Nc1cccc(Cl)c1OC)C(=O)NCC2` |
| M007 | C06 | `CCn1cc(C2CC2)c2c(Cc3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M008 | C07 | `Cc1c(N)cncc1-c1cc2cc(Nc3cc4n(n3)CC(=O)N(C)CC4)ncc2c(N)c1F` |
| M009 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCc2cncn2-3)n1` |
| M010 | C08 | `C[C@@H]1CCC(=O)N1Cc1cc(F)ccc1Oc1nncnc1N1CC2(CCN(CC3(C)CC3)CC2)C1` |
| M011 | C01 | `Nc1cc(-c2cnco2)ccc1NC1CCC1` |
| M012 | C06 | `CCn1ccc2c([C@](O)(c3ccc(C(F)(F)F)nc3)C3CC3)n(C)nc2c1=O` |
| M013 | C09 | `Cc1cc(S(=O)(=O)N[C@]2(C)C[C@@H](N3CCN(CC4CCN(c5ccc6c(c5F)n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)CC3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M014 | C06 | `Cn1nc2c(=O)n(C3CC3)cnc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M015 | C10 | `CC[C@@H](C(=O)Nc1ccc(C(N)=O)c(F)c1)n1cc(OC)c(-c2cc(Cl)ccc2-n2cc(Cl)nn2)cc1=O` |
| M016 | C09 | `CNS(=O)(=O)c1ccc(Nc2ncc(C(F)(F)F)c(N3CCC[C@](C)(O)C3)n2)c(C)c1` |
| M017 | C11 | `O=C1CC[C@H](N2Cc3c(ccc4c3OCC43CCN(C[C@@H]4CCC5(CCN(c6ccc([C@@H]7c8ccc(O)cc8CC[C@@H]7c7ccccc7)cc6)CC5)OC4)CC3)C2=O)C(=O)N1` |
| M018 | C09 | `Cc1cc(S(=O)(=O)N[C@H]2CC[C@H](CN3CCN(c4ccc(C5CCC(=O)NC5=O)c(Cl)c4)CC3)CC2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M019 | C12 | `CC[C@@H]1CN(Cc2cc([C@H](CC(=O)O)c3ccc4c(nnn4C)c3C)ccc2C)S(=O)(=O)c2ccccc2O1` |
| M020 | C13 | `CCNC(=O)c1c(OC)cc(-n2cnc3cc(-c4cnn(CC)c4)ccc32)cc1OC(F)F` |
| M021 | C14 | `Nc1cccc2c1C(=O)N(C1CCC(=O)NC1=O)C2=O` |
| M022 | C02 | `O=C1COc2cc(F)c(C(=O)Nc3cccc(-c4nncn4-c4ccccc4)n3)cc2N1` |
| M023 | C15 | `CS(=O)(=O)c1cncc(C(=O)N2[C@@H](C(=O)N[C@@H](c3cc(F)c(C(F)(F)F)cc3F)C3CC3)C[C@H]3C[C@H]32)c1` |
| M024 | C09 | `C[C@]1(O)CCCN(c2nc(Nc3ccc(S(=O)(=O)N[C@H]4CC[C@H](CN5CCN(c6ccc(C7CCC(=O)NC7=O)cc6F)CC5)CC4)cc3F)ncc2C(F)(F)F)C1` |
| M025 | C02 | `CC(CO)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3C)n1` |
| M026 | C16 | `COCCCn1cc2cc(NC(=O)c3cccc(C(F)(F)F)n3)c(C(C)(C)O)cc2n1` |
| M027 | C06 | `CC[C@@](N)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ccn(C3CC3)c(=O)c2nn1C` |
| M028 | C17 | `C=CC(=O)N1CCC[C@@H](Oc2nc(-c3cnn(C)c3)cn3nccc23)CC1` |
| M029 | C18 | `C[C@H]1CC[C@H](c2ccc3scnc3c2)N(C(=O)C(=O)Nc2cnc(N)c3cn[nH]c23)C1` |
| M030 | C05 | `COc1cc2nc([C@H]3CC[C@H](CN4CC5(CC(CCNc6cccc7c6C(=O)N(C6CCC(=O)NC6=O)C7=O)C5)C4)CC3)cn2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M031 | C19 | `CNc1cccc(-c2c(-c3cnn(C)c3)oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c23)c1` |
| M032 | C20 | `COc1c(Cl)cccc1Nc1c(-c2ccncc2F)[nH]c2c1C(=O)NC[C@@H]2C[C@@H]1CCO1` |
| M033 | C21 | `CC(C)(O)c1cc2nn(CCS(C)(=O)=O)cc2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M034 | C22 | `CN(Cc1ccccc1)c1ncnc2[nH]c(-c3ccc(O)cc3)cc12` |
| M035 | C09 | `Cc1cc(S(=O)(=O)N[C@H]2C[C@H](N3CCN(CC4CCN(c5cccc6c5n(C)c(=O)n6C5CCC(=O)NC5=O)CC4)CC3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M036 | C09 | `C[C@]1(O)CCCN(c2nc(Nc3ccc(S(=O)(=O)N[C@H]4CC[C@H](CN5CCN(c6ccc(C7CCC(=O)NC7=O)c(F)c6)CC5)CC4)cc3F)ncc2C(F)(F)F)C1` |
| M037 | C23 | `Cc1nc(-c2onc(C)c2Nc2cncc(OC(C)C)n2)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M038 | C23 | `Cc1nc(-c2onc(C)c2NC(=O)O[C@H](C)c2ccccc2)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M039 | C08 | `CC(C)C1(CN2CCC3(CC2)CN(c2ncnnc2Oc2ccc(F)cc2CN2C(=O)COC[C@H]2C)C3)CC1` |
| M040 | C08 | `CCN(C(=O)c1cc(F)ccc1Oc1nncnc1N1CC2(CCN(CC3(C)CC3)CC2)C1)C(C)C` |
| M041 | C24 | `C=CC(=O)N1CCN(C2CN(c3cc(N4CCC(c5scnc5C)CC4)nc(C(F)(F)F)n3)C2)CC1` |
| M042 | C24 | `C=CC(=O)N1CCN(C2CN(c3cc(N4CCC(c5nccs5)CC4)nc(C(F)(F)F)n3)C2)CC1` |
| M043 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCC(=O)N3)n1` |
| M044 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCC(=O)N3)c1` |
| M045 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCC(=O)N3C)n1` |

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
