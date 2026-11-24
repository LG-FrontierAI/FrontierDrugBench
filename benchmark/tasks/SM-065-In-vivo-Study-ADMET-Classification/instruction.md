---
bench_id: "SM-065-In-vivo-Study-ADMET-Classification"
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
| C01 | cynomolgus monkey. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 10% HP-beta-CD/90% water. |
| C02 | rat. IV 2 mg/kg. Matrix: plasma. |
| C03 | rat. IV dose unspecified. Matrix: plasma. |
| C04 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. |
| C05 | rat. IV 1 mg/kg. Matrix: plasma. |
| C06 | mouse; C57BL/6; female. IV 1 mg/kg. Matrix: blood. |
| C07 | mouse; ICR; male. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: unspecified. |
| C08 | rat; Sprague-Dawley. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 20%DMSO+40%PEG400 in water. |
| C09 | mouse; CD-1; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: PEG200/water60/40. |
| C10 | rat; Sprague-Dawley; male. IV 0.1 mg/kg. Matrix: plasma. Vehicle/formulation: 10%DMSO/0.1Mphosphate buffer,pH8.5. Cassette dosing. |
| C11 | rat. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 10% DMSO/40% PEG400/50% water. |
| C12 | rat; Sprague-Dawley; male. IV 0.5 mg/kg. Matrix: plasma. |
| C13 | mouse; CD-1. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: DMSO. |
| C14 | rat; Wistar-Han; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 10% PEG400/90% 23% HPBCD in water. |
| C15 | rat; Han Wistar. IV dose unspecified. Matrix: blood. |
| C16 | mouse; C57BL/6J; female. IV 2 mg/kg. Matrix: plasma. |
| C17 | rat; Wistar-Han; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 10% DMSO/50% PEG400/40% water. |
| C18 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 10% EtOH/40% PEG400/50% saline. |
| C19 | mouse. IV 0.5 mg/kg. Matrix: blood. |
| C20 | mouse; Balb/c; male. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 30% Captisol. |
| C21 | rat; Sprague-Dawley; male. IV 1.1 mg/kg. Matrix: plasma. Vehicle/formulation: 10% EtOH/70% PEG400/20% saline. |
| C22 | rat; Sprague-Dawley. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 20%HP-beta-CD solution. Feeding: fed. |
| C23 | mouse; CD-1. IV 1 mg/kg. Matrix: whole blood. Vehicle/formulation: 10%DMSO,35%PEG400;remaining fraction not reported. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(C#CCOC3CCN(C[C@H]4CC[C@H](n5cc(NC(=O)c6cnn7ccc(N8C[C@H]9C[C@@H]8CO9)nc67)c(C(F)F)n5)CC4)CC3)c21` |
| M002 | C02 | `Cc1cc(S(=O)(=O)N[C@H]2C[C@H](N3CC[C@@H](OC4CN(c5cccc6c5n(C)c(=O)n6C5CCC(=O)NC5=O)C4)[C@H](F)C3)C2)ccc1Nc1ncc(C(F)(F)F)c(N2CCC[C@](C)(O)C2)n1` |
| M003 | C03 | `CC(C)(O)c1cc2nn([C@H]3CC[C@H](CN4CCC(O[C@H]5C[C@H](Nc6cccc7c6C(=O)N(C6CCC(=O)NC6=O)C7=O)C5)CC4)CC3)cc2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M004 | C04 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3)n1` |
| M005 | C05 | `CC[C@@](O)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2cnn(C3CC3)c(=O)c2nn1C` |
| M006 | C04 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)C(C)(C)CC(=O)N3)n1` |
| M007 | C05 | `CCn1cc(C)c2c([C@H](O)c3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M008 | C06 | `Cc1c(-c2cc3cc(NC(=O)O[C@H]4COC[C@@H]4C)ncc3c(N)c2F)cnc2c1NCCO2` |
| M009 | C07 | `Cn1cc(-c2oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c3c2-c2cccc(N3CCNCC3)c2)cn1` |
| M010 | C08 | `COCC[C@H]1CNC(=O)c2c1[nH]c(-c1ccncc1F)c2Nc1cccc(Cl)c1OC` |
| M011 | C09 | `Cc1cc(C#N)ncc1Oc1cc(Nc2ccc(C(=O)N3CCN(C)CC3)cn2)c2ncn(C)c2n1` |
| M012 | C03 | `COc1cc2nn([C@H]3CC[C@H](CN4CCC5(CC4)CC(CNc4cccc6c4C(=O)N(C4CCC(=O)NC4=O)C6=O)C5)CC3)cc2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M013 | C04 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3)c1` |
| M014 | C04 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)C(C)(C)CC(=O)N3C)n1` |
| M015 | C10 | `CCc1oc2c(Cl)ccc(Cl)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M016 | C03 | `O=C1CCC(N2C(=O)c3cccc(NCC4CC5(CCN(C[C@H]6CC[C@H](n7cc8cc(NC(=O)c9cccc(C(F)(F)F)n9)c(C(F)F)cc8n7)CC6)CC5)C4)c3C2=O)C(=O)N1` |
| M017 | C04 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCC(=O)N3C)n1` |
| M018 | C11 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc([C@H]3C[C@H](COC4CCN(C[C@H]5CC[C@H](n6cc(NC(=O)c7cnn8ccc(N9C[C@H]%10C[C@@H]9CO%10)nc78)c(C(F)F)n6)CC5)CC4)C3)c21` |
| M019 | C12 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OC(C)(C)C(=O)N3C)n1` |
| M020 | C05 | `Cn1nc2c(=O)n(C3CC3)ncc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M021 | C13 | `C=CC(=O)N1CCN(C2CN(c3cc(N4CCC(c5c(C)cnn5C)CC4)nc(C(F)(F)F)n3)C2)CC1` |
| M022 | C05 | `CCn1ccc2c([C@](O)(c3cnc(C(F)(F)F)c(Cl)c3)C3CC3)n(C)nc2c1=O` |
| M023 | C07 | `CN(C)Cc1ccc(-c2c(-c3cnn(C)c3)oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c23)cc1` |
| M024 | C14 | `COC(=O)N[C@H](C(=O)N1C[C@H](C(F)(F)F)C[C@H]1C(=O)N[C@H](C#N)C[C@@H]1CCCNC1=O)C(C)(C)C` |
| M025 | C04 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3C)n1` |
| M026 | C15 | `CC[C@@H]1CN(Cc2cc([C@@H](CC(=O)O)c3ccc4c(nnn4C)c3C)ccc2C)S(=O)(=O)c2ccccc2O1` |
| M027 | C02 | `C[C@H]1CN(CC2CCN(c3ccc(C4CCC(=O)NC4=O)cc3F)CC2)CC[C@H]1NS(=O)(=O)c1ccc(Nc2ncc(C(F)(F)F)c(N3CCC[C@](C)(O)C3)n2)c(F)c1` |
| M028 | C16 | `Cc1nc(-c2onc(C)c2NC(=O)O[C@H](C)c2ccccc2Cl)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M029 | C17 | `CC(C)(C)[C@H](NC(=O)C(F)(F)F)C(=O)N1C[C@H](OC(F)F)C[C@H]1C(=O)N[C@H](C#N)C[C@@H]1CCNC1=O` |
| M030 | C05 | `CCn1cc(Cl)c2c(Cc3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M031 | C18 | `Cc1ncc(S(=O)(=O)N2CCC(c3cn4ncnc4cc3Cl)CC2)o1` |
| M032 | C19 | `CC(C)(O)CCn1cc2cc(NC(=O)c3cccc(C(F)(F)F)n3)c(C(C)(C)O)cc2n1` |
| M033 | C20 | `N#Cc1ccc(N2CCN(C(=O)Cc3ccc(C4CC4)c(F)c3)CC2)nn1` |
| M034 | C09 | `Cc1cc(C#N)ncc1Oc1cc(Nc2ccc(C(=O)N3CCOCC3)cn2)c2ncn(C)c2n1` |
| M035 | C21 | `[2H]C1([2H])CC(c2cn3ncnc3cc2Cl)CC([2H])([2H])N1S(=O)(=O)c1cnc(C)o1` |
| M036 | C22 | `Cn1cc(-c2ccnc3[nH]ncc23)c(-c2ccc(F)cc2)n1` |
| M037 | C22 | `Cn1cc(-c2ccnc3[nH]ccc23)c(-c2ccc(F)cn2)n1` |
| M038 | C11 | `CN(CCCOCCCc1cccc2c1n(C)c(=O)n2C1CCC(=O)NC1=O)C[C@H]1CC[C@H](n2cc(NC(=O)c3cnn4ccc(N5C[C@H]6C[C@@H]5CO6)nc34)c(C(F)F)n2)CC1` |
| M039 | C11 | `CN(CCCOCCCc1cccc2c1n(C)c(=O)n2C1CCC(=O)NC1=O)C[C@H]1CC[C@H](n2cc(NC(=O)c3cnn4ccc(N5C[C@H](N)CC(F)(F)C5)nc34)c(C(F)F)n2)CC1` |
| M040 | C10 | `CCc1oc2cccc(C)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M041 | C10 | `CCc1oc2cccc(Br)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M042 | C08 | `COc1c(Cl)cccc1Nc1c(-c2ccncc2F)[nH]c2c1C(=O)NC[C@@H]2C[C@H]1COCCO1` |
| M043 | C08 | `COc1c(Cl)cccc1Nc1c(-c2ccncn2)[nH]c2c1C(=O)NC[C@@H]2C[C@@H]1COCCO1` |
| M044 | C23 | `CNS(=O)(=O)c1ccc(Nc2ncc3ccc(C(=O)N4CC[C@@H]4C)nc3n2)c(F)c1` |
| M045 | C23 | `CNS(=O)(=O)c1ccc(Nc2ncc3ccc(C(=O)N4C[C@@H](C#N)[C@@H]4C)nc3n2)c(F)c1` |

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
| Q035 | M035 |

## 2. Analogue comparisons

Compare IV Vss. Let R = value(left) / value(right). Choose A if R > 2; B if 1/2 <= R <= 2; C if R < 1/2.

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
