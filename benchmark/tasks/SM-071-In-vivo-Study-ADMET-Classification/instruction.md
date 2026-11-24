---
bench_id: "SM-071-In-vivo-Study-ADMET-Classification"
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
| C01 | mouse; CD-1; male. PO 50 mg/kg. Matrix: plasma. Vehicle/formulation: DMSO/PEG400/20%HP-beta-CD1:4:5. AUC interval: 0 to last quantifiable sample. Sampling: 5,15,30min,1,2,4,8,24h. |
| C02 | mouse; BALB/c. PO 5 mg/kg. Matrix: whole blood. Vehicle/formulation: unspecified. AUC interval: 0-6h. Reported geometric mean. |
| C03 | rat; Sprague-Dawley; male. PO 5 mg/kg. Matrix: plasma. AUC interval: 0 to last quantifiable sample. Sampling: 0.25,0.5,1,2,4,8,24h. |
| C04 | mouse; BALB/c. PO 5 mg/kg. Matrix: whole blood. Vehicle/formulation: unspecified. AUC interval: 0-24h. Reported geometric mean. |
| C05 | mouse; CD-1. PO 50 mg/kg. Matrix: whole blood. Vehicle/formulation: 70% PEG,30% D5W. AUC interval: 0 to infinity. |
| C06 | mouse; CD-1; female. PO 50 mg/kg. Matrix: plasma. Vehicle/formulation: 2%hydroxypropyl cellulose/0.5%Tween80 in water. AUC interval: 0 to last quantifiable sample. Sampling: 0.5,1,2,4,7,24h. |
| C07 | rat; Sprague-Dawley. PO 5 mg/kg. Matrix: whole blood. Vehicle/formulation: unspecified. AUC interval: 0-24h. Reported geometric mean. |
| C08 | mouse; ICR; male. PO 10 mg/kg. Matrix: plasma. Dosed form: hydrochloride salt. Vehicle/formulation: unspecified. AUC interval: 0 to infinity. Sampling: 0,0.5,1,2,4,6,8,16,24h. |
| C09 | mouse; CD-1; male. PO 5 mg/kg. Matrix: plasma. Vehicle/formulation: Solutol HS15/0.5%methylcellulose 2/98 v/v. AUC interval: 0 to infinity. |
| C10 | mouse; BALB/cA; male. PO 50 mg/kg. Matrix: plasma. Vehicle/formulation: 0.5% w/v hydroxypropyl methylcellulose. AUC interval: 0-6h. Sampling: to6h. |
| C11 | mouse; ICR; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 0.5% CMC-Na,pH2.1. AUC interval: 0 to infinity. |
| C12 | mouse. PO 10 mg/kg. Matrix: plasma. AUC interval: 0 to infinity. |
| C13 | rat. PO 5 mg/kg. Matrix: plasma. Vehicle/formulation: 20%HP-beta-CD/80%water. AUC interval: 0 to last quantifiable sample. |
| C14 | mouse; C57BL/6J; female. PO 30 mg/kg. Matrix: plasma. AUC interval: 0 to last quantifiable sample. Sampling: 8 time points to24h. |
| C15 | mouse; CD-1; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: DMSO/Cremophor/PBS 10/10/80. AUC interval: 0 to infinity. Sampling: seven PO timepoints to24h. |
| C16 | rat; Sprague-Dawley; male. PO 2.5 mg/kg. Matrix: plasma. AUC interval: 0 to last quantifiable sample. Sampling: 0.25,0.5,1,2,4,8,24h. |
| C17 | mouse; CD-1. PO 50 mg/kg. Matrix: whole blood. Vehicle/formulation: 80% PEG,20% D5W. AUC interval: 0 to infinity. |
| C18 | rat; Sprague-Dawley; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: deionized water pH2.1 adjusted HCl. AUC interval: 0-24h. Sampling: to24h. |
| C19 | rat; Wistar-Han; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 2%Tween80 in0.5%methylcellulose water; amorphous. Feeding: fed. AUC interval: 0-24h. |
| C20 | mouse; BALB/c. PO 5 mg/kg. Matrix: whole blood. Vehicle/formulation: 10% DMSO,5% Tween20 in saline. Feeding: food and water ad libitum. AUC interval: 0-6h. Sampling: 7 or8 timepoints;parameters through6h. |
| C21 | rat. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 100% propylene glycol. AUC interval: 0 to last quantifiable sample. |
| C22 | rat; Sprague-Dawley; male. PO 0.1 mg/kg. Matrix: plasma. Vehicle/formulation: 10%DMSO/0.1M phosphate buffer,pH8.5. AUC interval: 0-8h. Sampling: 0.25,0.5,1,2,4,8h. Cassette dosing. |
| C23 | mouse; CD1; female. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 5% NMP,5% SolutolHS15,20% PEG400,70% normal saline. AUC interval: 0 to last quantifiable sample. Sampling: 0.25,0.5,1,2,4,6,8,12,24h. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `CCc1cnc2c(c1)[C@@H](N1CCOc3c(cc(Cn4ccnc4)cc3-c3cn(C)nc3C(F)(F)F)C1=O)CCC2` |
| M002 | C02 | `CCN1CCN(Cc2ccc3cc(C(=O)Nc4cc(NC(=O)c5ccc6c(c5)OCCO6)ccc4Cl)ccc3n2)CC1` |
| M003 | C03 | `Cc1cc(F)c(C(=O)Nc2cccc(-c3nncn3C(C)C)n2)cc1-n1cnc(C2CC2)c1` |
| M004 | C04 | `CCN1CCN(Cc2ccc3cc(C(=O)Nc4cc(NC(=O)c5ccc6c(c5)OCCO6)ccc4F)ccc3n2)CC1` |
| M005 | C05 | `CNS(=O)(=O)c1ccc(Nc2ncc3ccc(C(=O)N4C[C@@H](C#N)[C@@H]4C)nc3n2)c(F)c1` |
| M006 | C06 | `COc1cc(S(C)(=O)=O)ccc1NCC#Cc1cc2c(NC3CCN(C)CC3)cccc2n1CC(F)(F)F` |
| M007 | C07 | `Cc1ccc(NC(=O)c2ccc3c(c2)OCCO3)cc1NC(=O)c1ccc2nc(OCCN3CCCC3)ccc2c1` |
| M008 | C03 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)C(C)(C)CC(=O)N3)n1` |
| M009 | C08 | `CN1CCN(c2cccc(-c3c(-c4cnn(C)c4)oc4ncnc(Oc5ccc(NC(=O)c6cccn(-c7ccc(F)cc7)c6=O)cc5)c34)c2)CC1` |
| M010 | C03 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3)n1` |
| M011 | C09 | `Cc1cc(C#N)ncc1Oc1cc(Nc2ccc(N3CCOCC3)nn2)c2ncn(C)c2n1` |
| M012 | C10 | `COc1cc(C#Cc2nn(C3CN(C(=O)/C=C/CN(C)C)C3)c3ncnc(N)c23)cc(OC)c1` |
| M013 | C11 | `N#Cc1ccnc(N2C(=O)CC[C@H]2C(=O)N(c2cncc(F)c2)[C@H](C(=O)NC2CC(F)(F)C2)c2ccccc2Cl)c1` |
| M014 | C12 | `O=C(Cc1ccc(C2CC2)cc1F)N1CCN(c2ccc(Cl)nn2)CC1` |
| M015 | C13 | `CN(CCCOCCCc1cccc2c1n(C)c(=O)n2C1CCC(=O)NC1=O)C[C@H]1CC[C@H](n2cc(NC(=O)c3cnn4ccc(N5C[C@H](N)CC(F)(F)C5)nc34)c(C(F)F)n2)CC1` |
| M016 | C13 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc([C@H]3C[C@H](COC4CCN(C[C@H]5CC[C@H](n6cc(NC(=O)c7cnn8ccc(N9C[C@H]%10C[C@@H]9CO%10)nc78)c(C(F)F)n6)CC5)CC4)C3)c21` |
| M017 | C03 | `O=C1CCCc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc2N1` |
| M018 | C03 | `CC(CO)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3C)n1` |
| M019 | C14 | `Cc1nc(-c2onc(C)c2NC(=O)O[C@H](C)c2ccccc2Cl)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M020 | C03 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCc2cncn2-3)n1` |
| M021 | C15 | `Nc1cc(-c2cnco2)ccc1NC1CCC1` |
| M022 | C16 | `O=C1COc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc2N1` |
| M023 | C17 | `CNS(=O)(=O)c1ccc(Nc2ncc3ccc(C(=O)N4C[C@@H](OC)[C@@H]4C)nc3n2)c(F)c1` |
| M024 | C18 | `CS(=O)(=O)N1CCC(c2ccc(-c3cc4nccnc4c(NC[C@@H]4CNCCO4)n3)cc2)CC1` |
| M025 | C03 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3C)n1` |
| M026 | C19 | `COC(=O)N[C@H](C(=O)N1C[C@H](OC(F)(F)F)C[C@H]1C(=O)N[C@H](C#N)C[C@@H]1CCNC1=O)C(C)(C)C` |
| M027 | C10 | `C=CC(=O)N1CC[C@H](n2nc(C#Cc3cc(OC)cc(OC)c3)c3c(N)ncnc32)C1` |
| M028 | C20 | `Cn1c(=O)c2c(c3cc(Nc4ccnc(F)c4Cl)ccc31)N[C@@H](C1CC1)C(F)(F)CO2` |
| M029 | C20 | `Cn1c(=O)c2c(c3cc(Nc4nc(N5CC(F)(F)C5)ncc4Cl)ccc31)N[C@@H](C1CC1)C(F)(F)CO2` |
| M030 | C21 | `CCOc1ncccc1-c1ccc(N2CCN(C(=O)c3ccc(Cl)cc3C(F)(F)F)C[C@H]2CC)c(C(=O)N[C@@H]2CCN(C)C2)n1` |
| M031 | C21 | `CCOc1ncccc1-c1ccc(N2CCN(C(=O)c3ccc(Cl)cc3C(F)(F)F)C[C@H]2CC)c(C(=O)NCCN(C)C)n1` |
| M032 | C22 | `CCc1oc2c(Cl)ccc(Cl)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M033 | C22 | `CCc1oc2cccc(C)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M034 | C13 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(CCCOC3CCN(C[C@H]4CC[C@H](n5cc(NC(=O)c6cnn7ccc(N8C[C@H]9C[C@@H]8CO9)nc67)c(C(F)F)n5)CC4)CC3)c21` |
| M035 | C13 | `CN(CCCOCCCc1cccc2c1n(C)c(=O)n2C1CCC(=O)NC1=O)C[C@H]1CC[C@H](n2cc(NC(=O)c3cnn4ccc(N5C[C@H]6C[C@@H]5CO6)nc34)c(C(F)F)n2)CC1` |
| M036 | C23 | `O=C1CCC(N2Cc3cc(Nc4noc5ccccc45)ccc3C2=O)C(=O)N1` |
| M037 | C23 | `O=C1CCC(N2Cc3cc(NC(=O)c4cccc(F)c4)ccc3C2=O)C(=O)N1` |
| M038 | C06 | `COc1cc(C(N)=O)ccc1NCC#Cc1cc2c(N[C@@H]3CCN(C)C[C@@H]3F)cccc2n1CC(F)(F)F` |
| M039 | C06 | `COc1cc(S(N)(=O)=O)ccc1NCC#Cc1cc2c(N[C@@H]3CCN(C)C[C@@H]3F)cccc2n1CC(F)(F)F` |
| M040 | C06 | `COc1cc(C(=O)NC2CCOCC2)ccc1NCC#Cc1cc2c(N[C@@H]3CCN(C)C[C@@H]3F)cccc2n1CC(F)(F)F` |

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

## 2. Analogue comparisons

Compare total oral AUC. Let R = value(left) / value(right). Choose A if R > 3; B if 1/3 <= R <= 3; C if R < 1/3.

Each pair belongs to one literature analogue family and one study context. B denotes only the specified numerical difference category; it does not establish statistical equivalence. No cross-species or cross-dose comparison is requested.

| Item | Left molecule | Right molecule | Points |
|---|---|---|---|
| Q028 | M028 | M029 | 8 |
| Q029 | M030 | M031 | 7 |
| Q030 | M032 | M033 | 7 |
| Q031 | M034 | M035 | 7 |
| Q032 | M036 | M037 | 7 |

## 3. Within-series ordering

Order each group from highest to lowest total oral AUC at its stated common dose, formulation and integration interval.

Each group shares one study context. Its score is the listed points multiplied by max(0, Spearman rho) between the submitted and reference orders.

| Item | Molecules to order | Points |
|---|---|---|
| Q033 | M038, M039, M040 | 10 |

## Response format and scoring

Return ONLY a strict JSON object mapping each listed Q identifier to L/M/H for interval items, A/B/C for comparisons, or an ordered array of the listed molecule IDs for ordering items.

Syntax example only; these values do not imply answers:

`{"Q001": "L", "Q028": "B", "Q033": ["M038", "M039", "M040"]}`

Each molecule is assessed in one item. Missing or invalid items earn zero. An ordering array must contain every specified molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0–1 scale.
