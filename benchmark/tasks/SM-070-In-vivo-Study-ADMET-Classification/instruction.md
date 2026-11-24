---
bench_id: "SM-070-In-vivo-Study-ADMET-Classification"
category: "In-vivo-Study"
format: "structured_json"
---
# Prompt

Predict reported in-vivo half-life under the stated study conditions. This task contains 35 distinct molecules and is worth 100 points.

Use each molecule's specified administration route. Oral half-life may reflect absorption and formulation as well as elimination. A terminal phase is specified only when explicitly reported.

A longer reported half-life may support longer exposure, but dosing frequency also depends on exposure, potency and safety. Compare half-lives only within the stated route and study conditions.

Use the study context assigned to each molecule. PO means oral administration; IV means intravenous administration. Conditions not listed are unspecified.

## Study contexts

| Context | Conditions |
|---|---|
| C01 | mouse; C57BL/6; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 99.8%of0.5%methylcelluloseaqueous+0.2%Tween80. Half-life phase: not specified. Sampling: 0-24h. |
| C02 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. Half-life phase: not specified. Sampling: 0.08h(IVonly),0.25,0.5,1,2,4,8,24h. |
| C03 | rat; Sprague-Dawley. PO 5 mg/kg. Matrix: plasma. Vehicle/formulation: 20%HP-beta-CD solution. Feeding: fed. Half-life phase: not specified. Sampling: .033IV,.083IV,.25,.5,1,2,4,6,8,24h. |
| C04 | mouse; ICR; male. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: unspecified. Half-life phase: not specified. Sampling: 0,0.5,1,2,4,6,8,16,24h. |
| C05 | mouse. IV 5 mg/kg. Matrix: plasma. Vehicle/formulation: 10%NMP/5%Solutol/0.9%NaCl85%. Half-life phase: not specified. |
| C06 | mouse; C57BL/6; female. IV 1 mg/kg. Matrix: whole blood. Vehicle/formulation: 35%PEG400/65%water. Feeding: not fasted. Half-life phase: not specified. Sampling: .033,.25,.5,1,2,4,6,8,24h. |
| C07 | mouse; Balb/c; male. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 30% Captisol. Half-life phase: not specified. Sampling: 0.08,0.25,0.5,1,2,4,8,24h. |
| C08 | mouse; C57BLKS; female. IV 1 mg/kg. Matrix: plasma. Half-life phase: not specified. Cassette dosing. |
| C09 | mouse; C57BL/6; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 99.8% (v/v) of0.5% methylcellulose in water +0.2% (v/v) Tween80. Half-life phase: not specified. Sampling: 0–24h. |
| C10 | rat; Sprague-Dawley. IV 0.5 mg/kg. Matrix: plasma. Vehicle/formulation: 20%DMSO+40%PEG400 in water. Half-life phase: not specified. Cassette dosing. |
| C11 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 5–10% w/v Trappsol with 5–10% DMSO. Feeding: overnight fast; food restored4h. Half-life phase: not specified. Sampling: up to72h. |
| C12 | mouse; ICR. IV 2.0 mg/kg. Matrix: plasma. Vehicle/formulation: 5%DMSO+10%solutol+85%saline. Half-life phase: elimination. Sampling: 5min,15min,30min,1,2,4,6,8,24h. |
| C13 | mouse; C57BL/6J. IV 10 mg/kg. Matrix: whole blood. Vehicle/formulation: DMA/PEG400/20%aqueousSBE-beta-CD10/60/30. Half-life phase: elimination. Sampling: 5min,15min,30min,1,3,8,24h. |
| C14 | rat; Sprague-Dawley; male. PO 5 mg/kg. Matrix: plasma. Half-life phase: not specified. Sampling: 0.08h(IVonly),0.25,0.5,1,2,4,8,24h. |
| C15 | rat; Sprague-Dawley; male. IV .5 mg/kg. Matrix: plasma. Vehicle/formulation: 10%DMSO/50%PEG400/40%water. Feeding: not fasted. Half-life phase: not specified. Sampling: .033,.083,.25,.5,1,2,4,6,8h. |
| C16 | rat; Sprague-Dawley; male. IV 1.1 mg/kg. Matrix: plasma. Vehicle/formulation: 10%EtOH/70%PEG400/20%saline. Half-life phase: terminal. Sampling: 0.033,0.117,0.25,0.5,1,2,4,7,24h. |
| C17 | mouse; BALB/c; female. IV 5 mg/kg. Matrix: whole blood. Vehicle/formulation: unspecified. Half-life phase: terminal. Sampling: SI general methods: 8 time points over 24 h; exact individual IV fit interval not given. |
| C18 | rat; Sprague-Dawley (CD); female. IV 1 mg/kg. Matrix: whole blood. Vehicle/formulation: unspecified. Half-life phase: terminal. Sampling: SI general methods: 8 time points over 24 h; exact individual IV fit interval not given. |
| C19 | rat. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 10% DMSO/40% PEG400/50% water. Half-life phase: terminal. |
| C20 | mouse; C57BL/6J; female. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: unspecified. Half-life phase: not specified. Sampling: up to24h. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `Oc1nc2nonc2cc1Nc1c(F)c(F)c(C(F)(F)F)c(F)c1F` |
| M002 | C02 | `O=C(Nc1cccc(-c2nncn2CC2CC2)n1)c1cc2c(cc1F)OCc1cncn1-2` |
| M003 | C02 | `CC(CO)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3C)n1` |
| M004 | C03 | `[2H]C([2H])([2H])C1(C([2H])([2H])[2H])Cn2nc(-c3ccc(F)cn3)c(-c3ccnc4[nH]ncc34)c2CO1` |
| M005 | C04 | `CNc1cccc(-c2c(-c3cnn(C)c3)oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c23)c1` |
| M006 | C05 | `CCN(CC)CCNC(=O)[C@H]1CC[C@H](NC(=O)c2cnc3nc2Nc2ccc(C)c(c2)OC/C=C\CN3)CC1` |
| M007 | C06 | `Cc1c(N)cncc1-c1cc2cc(Nc3cc4n(n3)CC(=O)N(C)CC4)ncc2c(N)c1F` |
| M008 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCC(=O)N3)n1` |
| M009 | C07 | `CN(C)c1ccc(CC(=O)N2CCN(c3ccc(Cl)nn3)CC2)cc1` |
| M010 | C08 | `CN(Cc1ccccc1)c1ncnc2[nH]c(-c3ccc(CO)c(F)c3)cc12` |
| M011 | C09 | `FC(F)(F)Oc1cccc(-c2ccnc3[nH]c(C(F)(F)F)nc23)c1` |
| M012 | C10 | `C=CC(=O)N1CCC[C@@H]1C#Cc1cnccc1-c1[nH]c2c(c1Nc1cccc(Cl)c1OC)C(=O)NCC2` |
| M013 | C11 | `CCn1ccc2c([C@@](O)(CC)c3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M014 | C12 | `CCc1c(F)ccc2cc(O)cc(-c3nc4c5c(nc(OCC6(CN7CCC(F)(CN8CCC9(CC8)COc8cc%10c(cc89)n(C)c(=O)n%10C8CCC(=O)NC8=O)CC7)CC6)nc5c3F)N3CCCOC[C@H]3CO4)c12` |
| M015 | C09 | `Fc1cc(F)cc(-c2ccnc3[nH]c(C(F)(F)F)nc23)c1` |
| M016 | C13 | `O=C(Nc1cnn(-c2cccc(C(=O)NC3CC3)c2)c1)Nc1cccc2ccccc12` |
| M017 | C14 | `CN1C(=O)CCCc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc21` |
| M018 | C11 | `CC[C@@](O)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2cnn(C3CC3)c(=O)c2nn1C` |
| M019 | C15 | `Cc1c(-c2cc3cc(NC(=O)OC4CCOCC4)ncc3c(N)c2F)cnc2c1NCCO2` |
| M020 | C11 | `Cc1nn(C2CC2)c(=O)c2nn(C)c(Cc3ccc(C(F)(F)F)c(C#N)c3)c12` |
| M021 | C16 | `[2H]C1([2H])CC(c2cn3ncnc3cc2Cl)CC([2H])([2H])N1S(=O)(=O)c1cnc(C)o1` |
| M022 | C01 | `Oc1c(Nc2ccc(-c3ccc(Cl)cc3)cc2)cnc2nonc12` |
| M023 | C17 | `Cc1ccc(NC(=O)c2ccc3c(c2)OCCO3)cc1NC(=O)c1ccc2nc(OCCN3CCCCC3)ccc2c1` |
| M024 | C18 | `CCN1CCN(Cc2ccc3cc(C(=O)Nc4cc(NC(=O)c5ccc6c(c5)OCCO6)ccc4F)ccc3n2)CC1` |
| M025 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCC(=O)N3)c1` |
| M026 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCc2cncn2-3)n1` |
| M027 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3)c1` |
| M028 | C11 | `CC[C@@](N)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ncn(C3CC3)c(=O)c2nn1C` |
| M029 | C19 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(CCCOC3CCN(C[C@H]4CC[C@H](n5cc(NC(=O)c6cnn7ccc(N8C[C@H]9C[C@@H]8CO9)nc67)c(C(F)F)n5)CC4)CC3)c21` |
| M030 | C19 | `CN(CCCOCCCc1cccc2c1n(C)c(=O)n2C1CCC(=O)NC1=O)C[C@H]1CC[C@H](n2cc(NC(=O)c3cnn4ccc(N5C[C@H](N)CC(F)(F)C5)nc34)c(C(F)F)n2)CC1` |
| M031 | C20 | `Cc1nc(-c2onc(C)c2NC(=O)O[C@H](C)c2ccccc2Cl)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M032 | C20 | `Cc1nc(-c2onc(C)c2Nc2cncc(OC(C)C)n2)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M033 | C11 | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1ccc(C(F)(F)F)nc1)C1CC1` |
| M034 | C11 | `CCn1ccc2c([C@](O)(c3cnc(C(F)(F)F)c(Cl)c3)C3CC3)n(C)nc2c1=O` |
| M035 | C11 | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C1CC1` |

## 1. Interval prediction

Assign L, M, or H using the following ranges (h). These are numerical endpoint ranges under the listed animal-study conditions, rather than universal development criteria.

| Label | Interval | Interpretation |
|---|---|---|
| L | value < 1 | Reported half-life below one hour |
| M | 1 <= value < 4 | Reported half-life from one to four hours |
| H | value >= 4 | Reported half-life at least four hours |

Each correct interval item earns 2.5 points.

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

## 2. Analogue comparisons

Compare reported half-life. Let R = value(left) / value(right). Choose A if R > 3; B if 1/3 <= R <= 3; C if R < 1/3. A means the left half-life is longer; C means it is shorter.

Each pair belongs to one literature analogue family and one study context. B denotes only the specified numerical difference category; it does not establish statistical equivalence. No cross-species or cross-dose comparison is requested.

| Item | Left molecule | Right molecule | Points |
|---|---|---|---|
| Q029 | M029 | M030 | 10 |
| Q030 | M031 | M032 | 10 |

## 3. Within-series ordering

Order each group from longest to shortest reported half-life.

Each group shares one study context. Its score is the listed points multiplied by max(0, Spearman rho) between the submitted and reference orders.

| Item | Molecules to order | Points |
|---|---|---|
| Q031 | M033, M034, M035 | 10 |

## Response format and scoring

Return ONLY a strict JSON object mapping each listed Q identifier to L/M/H for interval items, A/B/C for comparisons, or an ordered array of the listed molecule IDs for ordering items.

Syntax example only; these values do not imply answers:

`{"Q001": "L", "Q029": "B", "Q031": ["M033", "M034", "M035"]}`

Each molecule is assessed in one item. Missing or invalid items earn zero. An ordering array must contain every specified molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0–1 scale.
