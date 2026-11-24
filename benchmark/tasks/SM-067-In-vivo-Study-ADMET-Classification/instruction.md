---
bench_id: "SM-067-In-vivo-Study-ADMET-Classification"
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
| C01 | mouse; ICR; male. IV 3 mg/kg. Matrix: plasma. Vehicle/formulation: unspecified. Half-life phase: not specified. Sampling: 0,0.5,1,2,4,6,8,16,24h. |
| C02 | mouse; C57BL/6J. IV 10 mg/kg. Matrix: whole blood. Vehicle/formulation: DMA/PEG400/20%aqueousSBE-beta-CD10/60/30. Half-life phase: elimination. Sampling: 5min,15min,30min,1,3,8,24h. Cassette dosing. |
| C03 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 10%EtOH/40%PEG400/50%saline. Half-life phase: terminal. Sampling: 0.033,0.117,0.25,0.5,1,2,4,7,24h. |
| C04 | rat; Sprague-Dawley; male. PO 2.5 mg/kg. Matrix: plasma. Half-life phase: not specified. Sampling: 0.08h(IVonly),0.25,0.5,1,2,4,8,24h. |
| C05 | mouse; Balb/c; male. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 30% Captisol. Half-life phase: not specified. Sampling: 0.08,0.25,0.5,1,2,4,8,24h. |
| C06 | rat; Sprague-Dawley; male. PO 5 mg/kg. Matrix: plasma. Half-life phase: not specified. Sampling: 0.08h(IVonly),0.25,0.5,1,2,4,8,24h. |
| C07 | mouse; CD-1; male. IV 1 mg/kg. Matrix: plasma. Half-life phase: not specified. Sampling: 0.25,0.5,1,3,5h. Cassette dosing. |
| C08 | mouse; C57BLKS; female. IV 1 mg/kg. Matrix: plasma. Half-life phase: not specified. Cassette dosing. |
| C09 | mouse; CD-1; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: DMSO/Cremophor/PBS10/10/80. Half-life phase: terminal. Sampling: up to24h. |
| C10 | mouse. IV 1 mg/kg. Matrix: plasma. Half-life phase: not specified. |
| C11 | mouse; C57BL/6J; female. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: unspecified. Half-life phase: not specified. Sampling: up to24h. |
| C12 | mouse; CD-1; male. IV 1 mg/kg. Matrix: plasma. Half-life phase: elimination. |
| C13 | dog. IV 0.5 mg/kg. Matrix: systemic matrix unspecified. Half-life phase: not specified. |
| C14 | rat. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 10% DMSO/40% PEG400/50% water. Half-life phase: terminal. |
| C15 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 5–10% w/v Trappsol with 5–10% DMSO. Feeding: overnight fast; food restored4h. Half-life phase: not specified. Sampling: up to72h. |
| C16 | mouse. IV 3 mg/kg. Matrix: plasma. Vehicle/formulation: 10%NMP/5%Solutol/0.9%NaCl85%. Half-life phase: not specified. |
| C17 | mouse; C57BL/6; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 99.8%of0.5%methylcelluloseaqueous+0.2%Tween80. Half-life phase: not specified. Sampling: 0-24h. |
| C18 | mouse; C57BL/6; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 99.8% (v/v) of0.5% methylcellulose in water +0.2% (v/v) Tween80. Half-life phase: not specified. Sampling: 0–24h. |
| C19 | rat; Sprague-Dawley; male. IV 0.5 mg/kg. Matrix: plasma. Half-life phase: not specified. Sampling: 0.08h(IVonly),0.25,0.5,1,2,4,8,24h. |
| C20 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. Half-life phase: not specified. Sampling: 0.08h(IVonly),0.25,0.5,1,2,4,8,24h. |
| C21 | mouse; ICR; male. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: unspecified. Half-life phase: not specified. Sampling: 0,0.5,1,2,4,6,8,16,24h. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `Cn1cc(-c2oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c3c2-c2cccc(N)c2)cn1` |
| M002 | C02 | `O=C(Nc1cnn(-c2ccccn2)c1)Nc1cccc2ccccc12` |
| M003 | C03 | `Cc1ncc(S(=O)(=O)N2CCC(c3cn4ncnc4cc3Cl)CC2)s1` |
| M004 | C04 | `O=C1COc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc2N1` |
| M005 | C05 | `O=C(Cc1ccc(C2CC2)cc1F)N1CCN(c2ccc(Cl)nn2)CC1` |
| M006 | C06 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3)n1` |
| M007 | C07 | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)OC(C)(C)C)c1=O` |
| M008 | C08 | `Cc1cccc(CN(C)c2ncnc3[nH]c(-c4ccc(CO)cc4)cc23)c1` |
| M009 | C02 | `CNC(=O)c1cccc(-n2cc(NC(=O)Nc3cccc4ccccc34)cn2)c1` |
| M010 | C09 | `Nc1cc(-c2cnco2)ccc1NC1CCC1` |
| M011 | C10 | `CCNC(=O)c1c(OC)cc(-n2cnc3cc(-c4cnn(CC)c4)ccc32)cc1OC(F)F` |
| M012 | C11 | `Cc1nc(-c2onc(C)c2NC(=O)O[C@H](C)c2ccccc2)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M013 | C12 | `O=C1CCC(c2c(F)cc(N3CCC4(CCC(CN5CCC(c6ccc7c(c6)-n6c(nc(=O)c8c(Cl)cccc86)C76CCCCC6)CC5)CO4)CC3)cc2F)C(=O)N1` |
| M014 | C13 | `CC(C)(O)c1cc2nn(CCS(C)(=O)=O)cc2cc1NC(=O)c1cccc(C(F)(F)F)n1` |
| M015 | C14 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2ccccc21` |
| M016 | C15 | `CCn1cc(C)c2c([C@H](O)c3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M017 | C14 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc([C@H]3C[C@H](COC4CCN(C[C@H]5CC[C@H](n6cc(NC(=O)c7cnn8ccc(N9C[C@H]%10C[C@@H]9CO%10)nc78)c(C(F)F)n6)CC5)CC4)C3)c21` |
| M018 | C16 | `CCN(CC)CCNC(=O)[C@H]1CC[C@H](NC(=O)c2cnc3nc2Nc2ccc(C#N)c(c2)OC/C=C\CN3)CC1` |
| M019 | C05 | `O=C(Cc1ccc(C2CC2)c(F)c1)N1CCN(c2ccc(Cl)nn2)CC1` |
| M020 | C15 | `Cn1nc2c(=O)n(C3CC3)cnc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M021 | C17 | `Oc1nc2nonc2cc1Nc1cc(C(F)(F)F)c(F)cc1F` |
| M022 | C18 | `FC(F)(F)c1cccc(-c2ccnc3[nH]c(C(F)(F)F)nc23)c1` |
| M023 | C19 | `O=C1CCc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc2N1` |
| M024 | C17 | `Oc1c(Nc2ccc(-c3cccc(Cl)c3)cc2)cnc2nonc12` |
| M025 | C07 | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)Cc2ccccc2)c1=O` |
| M026 | C20 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3C)n1` |
| M027 | C07 | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)C2CCCCC2)c1=O` |
| M028 | C15 | `Cn1nc2c(=O)n(C3CC3)ncc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M029 | C15 | `Cn1nc2c(=O)n(C3CC3)ncc2c1[C@](N)(c1ccc(C(F)(F)F)c(Cl)c1)C1CC1` |
| M030 | C07 | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)Nc2ccccc2)c1=O` |
| M031 | C07 | `CC(C)(C)OC(=O)Nc1cccn([C@@H](CC2CC2)C(=O)N[C@@H](C[C@@H]2CCNC2=O)C(=O)C(=O)NC2CC2)c1=O` |
| M032 | C20 | `O=C1COc2cc(F)c(C(=O)Nc3cccc(-c4nncn4-c4ccccc4)n3)cc2N1` |
| M033 | C20 | `O=C1CCCc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc2N1` |
| M034 | C21 | `CC(=O)Nc1cccc(-c2c(-c3cnn(C)c3)oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c23)c1` |
| M035 | C21 | `Cn1cc(-c2oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c3c2-c2cccc(CN)c2)cn1` |

## 1. Interval prediction

Assign L, M, or H using the following ranges (h). These are numerical endpoint ranges under the listed animal-study conditions, rather than universal development criteria.

| Label | Interval | Interpretation |
|---|---|---|
| L | value < 1 | Reported half-life below one hour |
| M | 1 <= value < 4 | Reported half-life from one to four hours |
| H | value >= 4 | Reported half-life at least four hours |

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

## 2. Analogue comparisons

Compare reported half-life. Let R = value(left) / value(right). Choose A if R > 3; B if 1/3 <= R <= 3; C if R < 1/3. A means the left half-life is longer; C means it is shorter.

Each pair belongs to one literature analogue family and one study context. B denotes only the specified numerical difference category; it does not establish statistical equivalence. No cross-species or cross-dose comparison is requested.

| Item | Left molecule | Right molecule | Points |
|---|---|---|---|
| Q028 | M028 | M029 | 12 |
| Q029 | M030 | M031 | 12 |
| Q030 | M032 | M033 | 11 |
| Q031 | M034 | M035 | 11 |

## Response format and scoring

Return ONLY a strict JSON object mapping each listed Q identifier to L/M/H for interval items, A/B/C for comparisons, or an ordered array of the listed molecule IDs for ordering items.

Syntax example only; these values do not imply answers:

`{"Q001": "L", "Q028": "B"}`

Each molecule is assessed in one item. Missing or invalid items earn zero. An ordering array must contain every specified molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0–1 scale.
