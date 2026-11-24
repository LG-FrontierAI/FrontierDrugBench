---
bench_id: "SM-072-In-vivo-Study-ADMET-Classification"
category: "In-vivo-Study"
format: "structured_json"
---
# Prompt

Predict total systemic AUC after oral administration under the stated study conditions. This task contains 40 distinct molecules and is worth 100 points.

Predict AUC over the stated integration interval. These are raw total exposures, not unbound or dose-normalized exposures. The AUC integration interval and the observation window are distinct.

For a program seeking systemic exposure at a fixed oral dose and formulation, a higher AUC can be useful. Adequacy requires potency, unbound exposure and safety information beyond this task.

Use the study context assigned to each molecule. PO means oral administration; IV means intravenous administration. Conditions not listed are unspecified.

## Study contexts

| Context | Conditions |
|---|---|
| C01 | rat; Sprague-Dawley; male. PO 2.5 mg/kg. Matrix: plasma. AUC interval: 0 to last quantifiable sample. Sampling: 0.25,0.5,1,2,4,8,24h. |
| C02 | rat; Sprague-Dawley; male. PO 5 mg/kg. Matrix: plasma. AUC interval: 0 to last quantifiable sample. Sampling: 0.25,0.5,1,2,4,8,24h. |
| C03 | mouse. PO 3 mg/kg. Matrix: plasma. Vehicle/formulation: 10% NMP,5% Solutol,85% normal saline. AUC interval: 0 to last quantifiable sample. |
| C04 | rat. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 20%HP-beta-CD/80%water. AUC interval: 0 to last quantifiable sample. |
| C05 | mouse; C57BL/6J; female. PO 30 mg/kg. Matrix: plasma. AUC interval: 0 to last quantifiable sample. Sampling: 8 time points to24h. |
| C06 | mouse; BALB/c. PO 5 mg/kg. Matrix: whole blood. Vehicle/formulation: unspecified. AUC interval: 0-6h. Reported geometric mean. |
| C07 | mouse; CD-1. PO 50 mg/kg. Matrix: whole blood. Vehicle/formulation: 70% PEG,30% D5W. AUC interval: 0 to infinity. |
| C08 | mouse; ICR; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 0.5% CMC-Na,pH2.1. AUC interval: 0-24h. |
| C09 | rat; Wistar-Han; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 2%Tween80 in0.5%methylcellulose water; 50%ASD. Feeding: fed. AUC interval: 0 to infinity. |
| C10 | rat. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 100% propylene glycol. AUC interval: 0 to last quantifiable sample. |
| C11 | mouse; CD1; female. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 5% NMP,5% SolutolHS15,90% normal saline. AUC interval: 0 to last quantifiable sample. Sampling: 0.25,0.5,1,2,4,6,8,12,24h. |
| C12 | rat; Wistar-Han; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 2%Tween80 in0.5%methylcellulose water; amorphous. Feeding: fed. AUC interval: 0-24h. |
| C13 | mouse; CD-1; male. PO 50 mg/kg. Matrix: plasma. Vehicle/formulation: ethanol/TPGS/PEG400/water5:5:30:60. AUC interval: 0 to last quantifiable sample. Sampling: 5,15,30min,1,2,4,8,24h. |
| C14 | mouse; CD1; male. PO 3 mg/kg. Matrix: plasma. Vehicle/formulation: 10% NMP,5% Solutol,85% normal saline. AUC interval: 0 to last quantifiable sample. Sampling: 0.083,0.25,0.5,1,2,4,8,24h. |
| C15 | mouse; BALB/cA; male. PO 50 mg/kg. Matrix: plasma. Vehicle/formulation: 0.5% w/v hydroxypropyl methylcellulose. AUC interval: 0-6h. Sampling: to6h. |
| C16 | cynomolgus monkey; cynomolgus; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 2%Tween80 in0.5%methylcellulose water; crystalline. Feeding: fed. AUC interval: 0-24h. |
| C17 | mouse; CD-1; male. PO 5 mg/kg. Matrix: plasma. Vehicle/formulation: Solutol HS15/0.5%methylcellulose 2/98 v/v. AUC interval: 0 to infinity. |
| C18 | dog. PO 3 mg/kg. Matrix: plasma. Vehicle/formulation: 0.5%MC/0.1%Tween80 in saline; source form not specified. AUC interval: 0 to infinity. |
| C19 | mouse; ICR; male. PO 10 mg/kg. Matrix: plasma. AUC interval: 0-8h. Sampling: to24h. |
| C20 | nonhuman primate (species unspecified). PO 5 mg/kg. Matrix: plasma. Vehicle/formulation: 10%HP-beta-CD/90%water. AUC interval: 0 to last quantifiable sample. |
| C21 | rat; Sprague-Dawley; male. PO 0.1 mg/kg. Matrix: plasma. Vehicle/formulation: 10%DMSO/0.1M phosphate buffer,pH8.5. AUC interval: 0-8h. Sampling: 0.25,0.5,1,2,4,8h. Cassette dosing. |
| C22 | mouse; CD-1; female. PO 50 mg/kg. Matrix: plasma. Vehicle/formulation: 2%hydroxypropyl cellulose/0.5%Tween80 in water. AUC interval: 0 to last quantifiable sample. Sampling: 0.5,1,2,4,7,24h. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OC(C)(C)C(=O)N3)n1` |
| M002 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCC(=O)N3C)n1` |
| M003 | C03 | `COC1CCN(Cc2ccc(-c3cn([C@H]4CC[C@H](O)CC4)c4nc(Nc5cc(C(F)(F)F)cc(C(F)(F)F)c5)ncc34)cc2)CC1` |
| M004 | C04 | `Nc1cccc2c1C(=O)N(C1CCC(=O)NC1=O)C2=O` |
| M005 | C05 | `Cc1noc(-c2ccc(NC(=O)[C@H]3CCCC[C@@H]3C(=O)O)cn2)c1NC(=O)O[C@H](C)c1ccccc1Cl` |
| M006 | C06 | `Cc1ccc(NC(=O)c2ccc3c(c2)OCCO3)cc1NC(=O)c1ccc2nc(CN3CCN(C(C)C)CC3)ccc2c1` |
| M007 | C07 | `CNS(=O)(=O)c1ccc(Nc2ncc3ccc(C(=O)N4CC[C@@H]4C)nc3n2)c(F)c1` |
| M008 | C06 | `CC(C)N1CCN(Cc2ccc3cc(C(=O)Nc4cc(NC(=O)c5ccc6c(c5)OCCO6)ccc4Cl)ccc3n2)CC1` |
| M009 | C08 | `CC(C)(O)CNc1nc(Nc2ccnc(C(F)(F)F)c2)nc(-c2cccc(C(F)(F)F)n2)n1` |
| M010 | C09 | `CC(C)(C)[C@H](NC(=O)C(F)(F)F)C(=O)N1C[C@H](OC(F)F)C[C@H]1C(=O)N[C@H](C#N)C[C@@H]1CCNC1=O` |
| M011 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3)c1` |
| M012 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCC(=O)N3)c1` |
| M013 | C10 | `CCOc1ccccc1-c1ccc(N2CCN(C(=O)C3(C(F)(F)F)CCC3)C[C@H]2CC)c(C(=O)N[C@@H]2CN3CCC2CC3)n1` |
| M014 | C02 | `CC(CO)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCC(=O)N3)n1` |
| M015 | C11 | `O=C1CCC(N2Cc3cc(Nc4noc5cc(F)ccc45)ccc3C2=O)C(=O)N1` |
| M016 | C12 | `COC(=O)N[C@H](C(=O)N1C[C@H](C(F)(F)F)C[C@H]1C(=O)N[C@H](C#N)C[C@@H]1CCCNC1=O)C(C)(C)C` |
| M017 | C05 | `Cc1nc(-c2onc(C)c2Nc2cncc(OC(C)C)n2)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M018 | C08 | `C[C@@H](Nc1nc(N[C@H](C)C(F)(F)F)nc(C2=C(F)[C@H](O)C(F)(F)CC2)n1)C(F)(F)F` |
| M019 | C13 | `CCn1cc(-c2cc(Cn3ccnc3)cc3c2OCCN([C@H](c2cc(OC)ccn2)C2CC2)C3=O)c(C(F)(F)F)n1` |
| M020 | C05 | `Cc1nc(-c2cnn(C)c2NC(=O)O[C@H](C)c2ccccc2Cl)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M021 | C14 | `CN1CCN(Cc2ccc(-c3cn([C@H]4CC[C@@H](O)CC4)c4nc(Nc5cc(C(F)(F)F)cc(C(F)(F)F)c5)ncc34)cc2)CC1` |
| M022 | C15 | `C=CC(=O)N1CC(n2nc(C#Cc3cc(OC)cc(OC)c3)c3c(N)ncnc32)C1` |
| M023 | C05 | `Cc1nc(-c2onc(C)c2NC(=O)O[C@H](C)c2ccccc2)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M024 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)C(C)(C)CC(=O)N3C)n1` |
| M025 | C02 | `O=C1COc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CCCC4)n3)cc2N1` |
| M026 | C16 | `COC(=O)N[C@H](C(=O)N1C[C@H](C(F)(F)F)C[C@H]1C(=O)N[C@H](C#N)C[C@@H]1CCNC1=O)C(C)(C)C` |
| M027 | C17 | `Cc1cc(C#N)ncc1Oc1cc(Nc2ccc(C(=O)N3CCN(C)CC3)cn2)c2ncn(C)c2n1` |
| M028 | C18 | `Cc1ncc(S(=O)(=O)N2CCC(c3cn4ncnc4cc3Cl)CC2)s1` |
| M029 | C19 | `CS(=O)(=O)N1CCN(c2ccc(-c3cc4nccnc4c(NC[C@@H]4CNCCO4)n3)cc2)CC1` |
| M030 | C06 | `Cc1ccc(NC(=O)c2ccc3c(c2)OCCO3)cc1NC(=O)c1ccc2nc(OCCN3CCCCC3)ccc2c1` |
| M031 | C19 | `CC(=O)N1CCN(c2ccc(-c3cc4nccnc4c(NC[C@@H]4CNCCO4)n3)cc2)CC1` |
| M032 | C02 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCC(=O)N3)n1` |
| M033 | C20 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(C#CCOC3CCN(C[C@H]4CC[C@H](n5cc(NC(=O)c6cnn7ccc(N8C[C@H]9C[C@@H]8CO9)nc67)c(C(F)F)n5)CC4)CC3)c21` |
| M034 | C19 | `Fc1cc(-c2cc3nccnc3c(NC[C@@H]3CNCCO3)n2)ccc1N1CCOCC1` |
| M035 | C21 | `CCc1oc2cccc(Br)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M036 | C21 | `CCc1oc2cccc(Cl)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M037 | C22 | `COc1cc(C(=O)NCC(O)CO)ccc1NCC#Cc1cc2c(N[C@@H]3CCN(C)C[C@@H]3F)cccc2n1CC(F)(F)F` |
| M038 | C22 | `COc1cc(S(C)(=O)=O)ccc1NCC#Cc1cc2c(N[C@H]3CCN(C)C[C@H]3F)cccc2n1CC(F)(F)F` |
| M039 | C22 | `COc1cc(C(=O)O)ccc1NCC#Cc1cc2c(N[C@@H]3CCN(C)C[C@@H]3F)cccc2n1CC(F)(F)F` |
| M040 | C22 | `CNC(=O)c1ccc(NCC#Cc2cc3c(N[C@@H]4CCN(C)C[C@@H]4F)cccc3n2CC(F)(F)F)c(OC)c1` |

## 1. Interval prediction

Assign L, M, or H using the following ranges (ng.h/mL). These are numerical endpoint ranges under the listed animal-study conditions, rather than universal development criteria.

| Label | Interval | Interpretation |
|---|---|---|
| L | value < 1000 | Lower total exposure range in this dosing context |
| M | 1000 <= value < 10000 | Intermediate total exposure range in this dosing context |
| H | value >= 10000 | Higher total exposure range in this dosing context |

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

Compare total oral AUC. Let R = value(left) / value(right). Choose A if R > 3; B if 1/3 <= R <= 3; C if R < 1/3.

Each pair belongs to one literature analogue family and one study context. B denotes only the specified numerical difference category; it does not establish statistical equivalence. No cross-species or cross-dose comparison is requested.

| Item | Left molecule | Right molecule | Points |
|---|---|---|---|
| Q035 | M035 | M036 | 12 |

## 3. Within-series ordering

Order each group from highest to lowest total oral AUC at its stated common dose, formulation and integration interval.

Each group shares one study context. Its score is the listed points multiplied by max(0, Spearman rho) between the submitted and reference orders.

| Item | Molecules to order | Points |
|---|---|---|
| Q036 | M037, M038, M039, M040 | 20 |

## Response format and scoring

Return ONLY a strict JSON object mapping each listed Q identifier to L/M/H for interval items, A/B/C for comparisons, or an ordered array of the listed molecule IDs for ordering items.

Syntax example only; these values do not imply answers:

`{"Q001": "L", "Q035": "B", "Q036": ["M037", "M038", "M039", "M040"]}`

Each molecule is assessed in one item. Missing or invalid items earn zero. An ordering array must contain every specified molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0–1 scale.
