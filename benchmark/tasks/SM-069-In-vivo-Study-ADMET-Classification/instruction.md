---
bench_id: "SM-069-In-vivo-Study-ADMET-Classification"
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
| C01 | dog. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 10% HP-beta-CD/90% water. Half-life phase: terminal. |
| C02 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 5–10% w/v Trappsol with 5–10% DMSO. Feeding: overnight fast; food restored4h. Half-life phase: not specified. Sampling: up to72h. |
| C03 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 0.5%DMSO/5%Solutol/5%ethanol/89.5%saline. Half-life phase: not specified. Sampling: 0-144h. |
| C04 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. Half-life phase: not specified. Sampling: 0.08h(IVonly),0.25,0.5,1,2,4,8,24h. |
| C05 | mouse; C57BL/6; male. PO 10 mg/kg. Matrix: plasma. Half-life phase: not specified. |
| C06 | mouse; CD-1; male. IV 1 mg/kg. Matrix: plasma. Half-life phase: not specified. Sampling: 0.25,0.5,1,3,5h. Cassette dosing. |
| C07 | rat; Sprague-Dawley; male. PO 5 mg/kg. Matrix: plasma. Half-life phase: not specified. Sampling: 0.08h(IVonly),0.25,0.5,1,2,4,8,24h. |
| C08 | rat; Sprague-Dawley. PO 5 mg/kg. Matrix: plasma. Vehicle/formulation: 20%HP-beta-CD solution. Feeding: fed. Half-life phase: not specified. Sampling: .033IV,.083IV,.25,.5,1,2,4,6,8,24h. |
| C09 | mouse; ICR. IV 2.0 mg/kg. Matrix: plasma. Vehicle/formulation: 5%DMSO+10%solutol+85%saline. Half-life phase: elimination. Sampling: 5min,15min,30min,1,2,4,6,8,24h. |
| C10 | mouse; CD-1; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 20%PEG200 in pH5 acetate buffer. Half-life phase: not specified. Sampling: .017,.083,.25,.5,1,2,4,8h. |
| C11 | rat; Sprague-Dawley; male. IV 0.5 mg/kg. Matrix: plasma. Half-life phase: not specified. Sampling: 0.08h(IVonly),0.25,0.5,1,2,4,8,24h. |
| C12 | mouse; ICR; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 0.5%CMC-Na,pH2.1. Half-life phase: not specified. Sampling: 0-24h. |
| C13 | mouse. IV 1 mg/kg. Matrix: plasma. Half-life phase: not specified. |
| C14 | rat; Sprague-Dawley. IV 0.5 mg/kg. Matrix: plasma. Vehicle/formulation: 20%DMSO+40%PEG400 in water (IV). Half-life phase: not specified. Cassette dosing. |
| C15 | mouse; ICR; male. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: unspecified. Half-life phase: not specified. Sampling: 0,0.5,1,2,4,6,8,16,24h. |
| C16 | mouse; C57BL/6J. IV 10 mg/kg. Matrix: whole blood. Vehicle/formulation: DMA/PEG400/20%aqueousSBE-beta-CD10/60/30. Half-life phase: elimination. Sampling: 5min,15min,30min,1,3,8,24h. Cassette dosing. |
| C17 | mouse; C57BL/6; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 99.8%of0.5%methylcelluloseaqueous+0.2%Tween80. Half-life phase: not specified. Sampling: 0-24h. |
| C18 | mouse; BALB/c; female. IV 5 mg/kg. Matrix: whole blood. Vehicle/formulation: unspecified. Half-life phase: terminal. Sampling: SI general methods: 8 time points over 24 h; exact individual IV fit interval not given. |
| C19 | mouse; C57BL/6J; female. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: unspecified. Half-life phase: not specified. Sampling: up to24h. |
| C20 | mouse; Balb/c; male. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 30% Captisol. Half-life phase: not specified. Sampling: 0.08,0.25,0.5,1,2,4,8,24h. |
| C21 | mouse; C57BLKS; female. IV 1 mg/kg. Matrix: plasma. Half-life phase: not specified. Cassette dosing. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(C#CCOC3CCN(C[C@H]4CC[C@H](n5cc(NC(=O)c6cnn7ccc(N8C[C@H]9C[C@@H]8CO9)nc67)c(C(F)F)n5)CC4)CC3)c21` |
| M002 | C02 | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M003 | C03 | `C[C@@H](Nc1nc(N[C@H](C)C(F)(F)F)nc(C2=C(F)[C@H](O)C(F)(F)CC2)n1)C(F)(F)F` |
| M004 | C04 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCC(=O)N3C)n1` |
| M005 | C04 | `O=C1COc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CCCC4)n3)cc2N1` |
| M006 | C05 | `Cc1cc(N)nc(COc2cc(CCN(C)C)cc(F)c2F)c1` |
| M007 | C06 | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)NC2CCCCC2)c1=O` |
| M008 | C07 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCC(=O)N3)n1` |
| M009 | C08 | `Cn1cc(-c2ccnc3[nH]ccc23)c(-c2ccc(F)cn2)n1` |
| M010 | C09 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@@](C)(O)C5)nc(OCC5(CN6CCC(F)(CN7CCN(c8ccc9c(c8)n(C)c(=O)n9C8CCC(=O)NC8=O)CC7)CC6)CC5)nc4c3F)c12` |
| M011 | C04 | `O=C(Nc1cccc(-c2nncn2CC2CC2)c1)c1cc2c(cc1F)OCc1cncn1-2` |
| M012 | C10 | `CC(C)C1(CN2CCC3(CC2)CN(c2ncnnc2Oc2ccc(F)cc2CN2C(=O)COC[C@H]2C)C3)CC1` |
| M013 | C06 | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)CCc2ccccc2)c1=O` |
| M014 | C02 | `CC[C@@](N)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ccn(C3CC3)c(=O)c2nn1C` |
| M015 | C11 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OC(C)(C)C(=O)N3)n1` |
| M016 | C02 | `CCn1cc(C)c2c([C@H](N)c3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M017 | C12 | `N#Cc1ccnc(N2C(=O)CC[C@H]2C(=O)N(c2cncc(F)c2)[C@H](C(=O)NC2CC(F)(F)C2)c2ccccc2Cl)c1` |
| M018 | C13 | `COc1cc(-n2cnc3cc(-c4cnn(C)c4)ccc32)cc(OC(F)F)c1C(=O)NC1CC1` |
| M019 | C14 | `COCC[C@@]1(C)CNC(=O)c2c1[nH]c(-c1ccncc1F)c2Nc1cccc(Cl)c1OC` |
| M020 | C15 | `Cn1cc(-c2oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c3c2-c2cccc(N3CCNCC3)c2)cn1` |
| M021 | C16 | `CC(=O)Nc1cccc(-n2cc(NC(=O)Nc3cccc4ccccc34)cn2)c1` |
| M022 | C10 | `C[C@@H]1CCC(=O)N1Cc1cc(F)ccc1Oc1nncnc1N1CC2(CCN(CC3(C)CC3)CC2)C1` |
| M023 | C17 | `Oc1nc2nonc2cc1Nc1ccc(OC(F)(F)F)cc1C(F)(F)F` |
| M024 | C18 | `Cc1ccc(NC(=O)c2ccc3c(c2)OCCO3)cc1NC(=O)c1ccc2nc(CN3CCN(C(C)C)CC3)ccc2c1` |
| M025 | C10 | `CCN(C(=O)c1cc(F)ccc1Oc1nncnc1N1CC2(CCN(CC3(C)CC3)CC2)C1)C(C)C` |
| M026 | C10 | `CON(C(=O)c1cc(F)ccc1Oc1nncnc1N1CC2(CCN(CC3(C)CC3)CC2)C1)C(C)C` |
| M027 | C19 | `Cc1noc(-c2ccc(NC(=O)[C@H]3CCCC[C@@H]3C(=O)O)cn2)c1NC(=O)O[C@H](C)c1ccccc1Cl` |
| M028 | C19 | `Cc1nc(-c2cnn(C)c2NC(=O)O[C@H](C)c2ccccc2Cl)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M029 | C20 | `C[C@@H]1CN(c2ccc(Cl)nn2)CCN1C(=O)Cc1ccc(C2CC2)cc1` |
| M030 | C20 | `C[C@@H]1CN(c2ccc(Cl)nn2)CCN1C(=O)Cc1ccc(C2CC2)c(F)c1` |
| M031 | C21 | `Cc1cccc(CN(C)c2ncnc3[nH]c(-c4ccc(C(=O)O)cc4)cc23)c1` |
| M032 | C21 | `CN(Cc1ccccc1)c1ncnc2[nH]c(-c3ccc(O)cc3)cc12` |
| M033 | C15 | `CN1CCN(c2cccc(-c3c(-c4cnn(C)c4)oc4ncnc(Oc5ccc(NC(=O)c6cccn(-c7ccc(F)cc7)c6=O)cc5)c34)c2)CC1` |
| M034 | C15 | `CN(C)Cc1ccc(-c2c(-c3cnn(C)c3)oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c23)cc1` |
| M035 | C15 | `CN(C)Cc1cccc(-c2c(-c3cnn(C)c3)oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c23)c1` |

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

## 2. Analogue comparisons

Compare reported half-life. Let R = value(left) / value(right). Choose A if R > 3; B if 1/3 <= R <= 3; C if R < 1/3. A means the left half-life is longer; C means it is shorter.

Each pair belongs to one literature analogue family and one study context. B denotes only the specified numerical difference category; it does not establish statistical equivalence. No cross-species or cross-dose comparison is requested.

| Item | Left molecule | Right molecule | Points |
|---|---|---|---|
| Q025 | M025 | M026 | 8 |
| Q026 | M027 | M028 | 8 |
| Q027 | M029 | M030 | 8 |
| Q028 | M031 | M032 | 8 |

## 3. Within-series ordering

Order each group from longest to shortest reported half-life.

Each group shares one study context. Its score is the listed points multiplied by max(0, Spearman rho) between the submitted and reference orders.

| Item | Molecules to order | Points |
|---|---|---|
| Q029 | M033, M034, M035 | 8 |

## Response format and scoring

Return ONLY a strict JSON object mapping each listed Q identifier to L/M/H for interval items, A/B/C for comparisons, or an ordered array of the listed molecule IDs for ordering items.

Syntax example only; these values do not imply answers:

`{"Q001": "L", "Q025": "B", "Q029": ["M033", "M034", "M035"]}`

Each molecule is assessed in one item. Missing or invalid items earn zero. An ordering array must contain every specified molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0–1 scale.
