---
bench_id: "SM-068-In-vivo-Study-ADMET-Classification"
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
| C01 | mouse. IV 3 mg/kg. Matrix: plasma. Vehicle/formulation: 10%NMP/5%Solutol/0.9%NaCl85%. Half-life phase: not specified. |
| C02 | rat; Sprague-Dawley; male. IV .5 mg/kg. Matrix: plasma. Vehicle/formulation: 10%DMSO/50%PEG400/40%water. Feeding: not fasted. Half-life phase: not specified. Sampling: .033,.083,.25,.5,1,2,4,6,8h. |
| C03 | mouse; ICR; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 0.5%CMC-Na,pH2.1. Half-life phase: not specified. Sampling: 0-24h. |
| C04 | mouse. PO 100 mg/kg. Matrix: plasma. Vehicle/formulation: PO:PEG400/SolutolHS15/Phosal53MCT30:20:50v/v/v. Half-life phase: not specified. |
| C05 | mouse; BALB/c; female. IV 1 mg/kg. Matrix: whole blood. Vehicle/formulation: unspecified. Half-life phase: terminal. Sampling: SI general methods: 8 time points over 24 h; exact individual IV fit interval not given. |
| C06 | rat; Sprague-Dawley. PO 5 mg/kg. Matrix: plasma. Vehicle/formulation: 20%HP-beta-CD solution. Feeding: fed. Half-life phase: not specified. Sampling: .033IV,.083IV,.25,.5,1,2,4,6,8,24h. |
| C07 | mouse; BALB/c; female. IV 5 mg/kg. Matrix: whole blood. Vehicle/formulation: unspecified. Half-life phase: terminal. Sampling: SI general methods: 8 time points over 24 h; exact individual IV fit interval not given. |
| C08 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. Half-life phase: not specified. Sampling: 0.08h(IVonly),0.25,0.5,1,2,4,8,24h. |
| C09 | mouse; ICR. IV 2.0 mg/kg. Matrix: plasma. Vehicle/formulation: 5%DMSO+10%solutol+85%saline. Half-life phase: elimination. Sampling: 5min,15min,30min,1,2,4,6,8,24h. |
| C10 | mouse; C57BL/6J. IV 10 mg/kg. Matrix: whole blood. Vehicle/formulation: DMA/PEG400/20%aqueousSBE-beta-CD10/60/30. Half-life phase: elimination. Sampling: 5min,15min,30min,1,3,8,24h. Cassette dosing. |
| C11 | rat. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 10% DMSO/40% PEG400/50% water. Half-life phase: terminal. |
| C12 | mouse; C57BL/6; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 99.8%of0.5%methylcelluloseaqueous+0.2%Tween80. Half-life phase: not specified. Sampling: 0-24h. |
| C13 | mouse; Balb/c; male. IV 2 mg/kg. Matrix: plasma. Vehicle/formulation: 30% Captisol. Half-life phase: not specified. Sampling: 0.08,0.25,0.5,1,2,4,8,24h. |
| C14 | mouse. IV 1 mg/kg. Matrix: plasma. Half-life phase: not specified. |
| C15 | rat; Sprague-Dawley; male. IV 0.5 mg/kg. Matrix: plasma. Half-life phase: not specified. Sampling: 0.08h(IVonly),0.25,0.5,1,2,4,8,24h. |
| C16 | mouse; C57BL/6; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 99.8% (v/v) of0.5% methylcellulose in water +0.2% (v/v) Tween80. Half-life phase: not specified. Sampling: 0–24h. |
| C17 | mouse; CD-1; male. IV 1 mg/kg. Matrix: plasma. Half-life phase: not specified. Sampling: 0.25,0.5,1,3,5h. Cassette dosing. |
| C18 | dog. IV 0.1 mg/kg. Matrix: plasma. Half-life phase: not specified. |
| C19 | rat; Sprague-Dawley; male. PO 5 mg/kg. Matrix: plasma. Half-life phase: not specified. Sampling: 0.08h(IVonly),0.25,0.5,1,2,4,8,24h. |
| C20 | mouse; CD-1; male. IV 10 mg/kg. Matrix: plasma. Vehicle/formulation: DMSO/Cremophor/PBS10/10/80. Half-life phase: terminal. Sampling: up to24h. |
| C21 | dog. IV 0.3 mg/kg. Matrix: plasma. Vehicle/formulation: water50%/PEG40040%/EtOH10%. Half-life phase: terminal. |
| C22 | rat; Sprague-Dawley. IV 0.5 mg/kg. Matrix: plasma. Vehicle/formulation: 20%DMSO+40%PEG400 in water (IV). Half-life phase: not specified. Cassette dosing. |
| C23 | rat; Sprague-Dawley; male. IV 1 mg/kg. Matrix: plasma. Vehicle/formulation: 5–10% w/v Trappsol with 5–10% DMSO. Feeding: overnight fast; food restored4h. Half-life phase: not specified. Sampling: up to72h. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `CN1CCC(NC(=O)[C@H]2CC[C@H](NC(=O)c3cnc4nc3Nc3ccc(C#N)c(c3)OC/C=C\CN4)CC2)CC1` |
| M002 | C02 | `Cc1c(N)cncc1-c1cc2cc(NC(=O)OC3CCOCC3)ncc2c(N)c1F` |
| M003 | C03 | `CC(C)(O)CNc1nc(Nc2ccnc(C(F)(F)F)c2)nc(-c2cccc(C(F)(F)F)n2)n1` |
| M004 | C04 | `CC(C)C[C@@H]1NC(=O)[C@@H](N(C)C(=O)[C@@H](NC(=O)[C@@H]2C[C@@H](F)CN2C(=O)C2(C(F)(F)F)CC(F)(F)C2)C2CC2)CCCCCCCN(C)C(=O)[C@H](Cc2cc(Cl)cnc2OC2CC2)N(C)C1=O` |
| M005 | C05 | `CC(C)N1CCN(Cc2ccc3cc(C(=O)Nc4cc(NC(=O)c5ccc6c(c5)OCCO6)ccc4Cl)ccc3n2)CC1` |
| M006 | C06 | `Cn1cc(-c2ccnc3[nH]ncc23)c(-c2ccc(F)cc2)n1` |
| M007 | C07 | `CCN1CCN(Cc2ccc3cc(C(=O)Nc4cc(NC(=O)c5ccc6c(c5)OCCO6)ccc4Cl)ccc3n2)CC1` |
| M008 | C08 | `CC(CO)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCC(=O)N3)n1` |
| M009 | C09 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@]6(CCO6)C5)nc(OCC5(CN6CCC(F)(CN7CCC8(CC7)COc7cc9c(cc78)n(C)c(=O)n9C7CCC(=O)NC7=O)CC6)CC5)nc4c3F)c12` |
| M010 | C10 | `C=CCNC(=O)c1cccc(-n2cc(NC(=O)Nc3cccc4ccccc34)cn2)c1` |
| M011 | C11 | `Nc1cccc2c1C(=O)N(C1CCC(=O)NC1=O)C2=O` |
| M012 | C12 | `Oc1nc2nonc2cc1Nc1c(F)c(F)c(F)c(F)c1F` |
| M013 | C13 | `O=C(Cc1ccc(C2CC2)cc1)N1CCN(c2ccc(Cl)nn2)CC1` |
| M014 | C14 | `CCNC(=O)c1c(OC)cc(-n2cnc3cc(-c4cnn(C)c4)ccc32)cc1OC(F)F` |
| M015 | C08 | `Cc1cc(F)c(C(=O)Nc2cccc(-c3nncn3C(C)C)n2)cc1-n1cnc(C2CC2)c1` |
| M016 | C15 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OC(C)(C)C(=O)N3C)n1` |
| M017 | C16 | `FC(F)(F)c1nc2c(-c3cc(Cl)cc(Cl)c3)ccnc2[nH]1` |
| M018 | C17 | `CC(C)(C)OC(=O)Nc1cccn([C@@H](CC2CC2)C(=O)N[C@@H](C[C@@H]2CCNC2=O)C(=O)C(N)=O)c1=O` |
| M019 | C18 | `C[C@]1(O)CCCN(c2nc(Nc3ccc(S(=O)(=O)N[C@@H]4CCN(CC5CCN(c6ccc(C7CCC(=O)NC7=O)cc6F)CC5)C[C@@H]4F)cc3F)ncc2C(F)(F)F)C1` |
| M020 | C12 | `Oc1nc2nonc2cc1Nc1cc(C(F)(F)F)ccc1C(F)(F)F` |
| M021 | C19 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)C(C)(C)CC(=O)N3)n1` |
| M022 | C20 | `Nc1cc(-c2cnco2)ccc1NC1CCCCC1` |
| M023 | C11 | `CN(CCCOCCCc1cccc2c1n(C)c(=O)n2C1CCC(=O)NC1=O)C[C@H]1CC[C@H](n2cc(NC(=O)c3cnn4ccc(N5C[C@H]6C[C@@H]5CO6)nc34)c(C(F)F)n2)CC1` |
| M024 | C11 | `O=C1CCC(n2c(=O)[nH]c3ccccc32)C(=O)N1` |
| M025 | C17 | `CC(C)(C)OC(=O)Nc1cc(F)cn([C@@H](CC2CC2)C(=O)N[C@@H](C[C@@H]2CCNC2=O)C(=O)C(N)=O)c1=O` |
| M026 | C21 | `Cn1nccc1[C@]1(CNC(=O)c2ccc(F)c(F)c2-c2ccc(C(F)(F)F)cc2)NC(=O)NC1=O` |
| M027 | C22 | `COc1c(Cl)cccc1Nc1c(-c2ccncc2F)[nH]c2c1C(=O)NC[C@@H]2C[C@@H]1CCO1` |
| M028 | C23 | `CC[C@@](O)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ccn(C3CC3)c(=O)c2nn1C` |
| M029 | C23 | `CCn1ccc2c([C@](O)(c3ccc(C(F)(F)F)nc3)C3CC3)n(C)nc2c1=O` |
| M030 | C08 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCc2cncn2-3)c1` |
| M031 | C08 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3C)c1` |
| M032 | C12 | `Oc1c(Nc2ccc(-c3cccc(F)c3)cc2)cnc2nonc12` |
| M033 | C12 | `Oc1c(Nc2ccc(-c3ccc(F)cc3)cc2)cnc2nonc12` |
| M034 | C16 | `FC(F)(F)c1ccc(-c2ccnc3[nH]c(C(F)(F)F)nc23)cc1` |
| M035 | C16 | `FC(F)(F)c1nc2c(-c3cccc(Cl)c3)ccnc2[nH]1` |

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
