---
bench_id: "SM-074-In-vivo-Study-ADMET-Classification"
category: "In-vivo-Study"
format: "structured_json"
---
# Prompt

Predict total systemic Cmax after oral administration under the stated study conditions. This task contains 40 distinct molecules and is worth 100 points.

Predict the maximum observed total systemic concentration after oral administration. These are raw total exposures, not unbound or dose-normalized exposures.

Predict the peak total systemic concentration at the stated oral dose and formulation. A higher Cmax is a concentration change; its desirability depends on efficacy and safety requirements.

Use the study context assigned to each molecule. PO means oral administration; IV means intravenous administration. Conditions not listed are unspecified.

## Study contexts

| Context | Conditions |
|---|---|
| C01 | rat; Sprague-Dawley; male. PO 5 mg/kg. Matrix: plasma. Sampling: 0.25,0.5,1,2,4,8,24h. |
| C02 | rat; Sprague-Dawley; male. PO 3 mg/kg. Matrix: plasma. Vehicle/formulation: 0.5%HPMC/0.5%benzyl alcohol/0.4%polysorbate80 in water. Feeding: overnight fast,food restored4h. Sampling: to72h. |
| C03 | rat; Sprague-Dawley; male. PO 2.5 mg/kg. Matrix: plasma. Sampling: 0.25,0.5,1,2,4,8,24h. |
| C04 | mouse; C57BL/6; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 99.8% of0.5% methylcellulose in water,0.2% Tween80. Sampling: to24h. |
| C05 | rat. PO 4 mg/kg. Matrix: systemic blood-derived;matrix subtype unspecified. Vehicle/formulation: 0.5% methylcellulose. |
| C06 | mouse; C57BL/6; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 99.8% of0.5% methylcellulose in water,0.2% Tween80. |
| C07 | mouse; db/db. PO 100 mg/kg. Matrix: blood-derived; plasma versus whole blood not explicit in PK methods. Vehicle/formulation: 1% hydroxyethyl cellulose. Feeding: fed. Sampling: 0.5,1,2,4,6,24h;2 samples/mouse. |
| C08 | mouse. PO 10 mg/kg. Matrix: plasma. |
| C09 | mouse; C57BL/6J; female. PO 30 mg/kg. Matrix: plasma. Sampling: 8 time points to24h. |
| C10 | mouse; CD-1; male. PO 5 mg/kg. Matrix: plasma. Vehicle/formulation: Solutol HS15/0.5%methylcellulose 2/98 v/v. |
| C11 | rat; Han Wistar; male. PO 0.5 mg/kg. Matrix: plasma. Vehicle/formulation: 0.5%HPMC/0.1%Tween in water. Feeding: free access to food and water. Sampling: 0.08,0.25,0.5,1,2,4,8,24h. Cassette dosing. |
| C12 | rat; Sprague-Dawley; male. PO 0.1 mg/kg. Matrix: plasma. Vehicle/formulation: 10%DMSO/0.1M phosphate buffer,pH8.5. Sampling: 0.25,0.5,1,2,4,8h. Cassette dosing. |
| C13 | mouse; ICR; male. PO 10 mg/kg. Matrix: plasma. Dosed form: hydrochloride salt. Vehicle/formulation: unspecified. Sampling: 0,0.5,1,2,4,6,8,16,24h. |
| C14 | mouse; C57BL/6J; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 99.8% of0.5% methylcellulose in water,0.2% Tween80. |
| C15 | mouse. PO 3 mg/kg. Matrix: whole blood. |
| C16 | mouse; CD-1; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: DMSO/Cremophor/PBS 10/10/80. Sampling: seven PO timepoints to24h. |
| C17 | mouse; CD-1; female. PO 50 mg/kg. Matrix: plasma. Vehicle/formulation: 2%hydroxypropyl cellulose/0.5%Tween80 in water. Sampling: 0.5,1,2,4,7,24h. |
| C18 | mouse; C57BL/6; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 99.8% of0.5%methylcellulose in water/0.2%Tween80. Sampling: to24h. |
| C19 | rat; Han Wistar; male. PO 1 mg/kg. Matrix: plasma. Vehicle/formulation: 0.5%HPMC/0.1%Tween in water. Feeding: free access to food and water. Sampling: 0.08,0.25,0.5,1,2,4,8,24h. Cassette dosing. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCCC(=O)N3C)c1` |
| M002 | C02 | `CCn1cc(Cl)c2c(Cc3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M003 | C03 | `O=C1CCc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc2N1` |
| M004 | C01 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)CCC(=O)N3)n1` |
| M005 | C01 | `CN1C(=O)CCCc2cc(F)c(C(=O)Nc3cccc(-c4nncn4C4CC4)n3)cc21` |
| M006 | C04 | `Oc1c(Nc2ccc(-c3ccc(F)cc3)cc2)cnc2nonc12` |
| M007 | C03 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OC(C)(C)C(=O)N3C)n1` |
| M008 | C02 | `Cn1nc2c(=O)n(C3CC3)ncc2c1[C@](N)(c1ccc(C(F)(F)F)c(Cl)c1)C1CC1` |
| M009 | C05 | `C[C@@]12COCCN1c1nc(-c3cccc4[nH]ccc34)ncc1N([C@H]1CC[C@H](O)CC1)C2=O` |
| M010 | C06 | `Oc1nc2nonc2cc1Nc1c(F)c(F)c(F)c(F)c1F` |
| M011 | C07 | `CCS(=O)(=O)c1nc(S(=O)(=O)c2ccccc2C#N)c(N2CCN(C)C(=O)C2)s1` |
| M012 | C08 | `C[C@@H]1CN(c2ccc(Cl)nn2)CCN1C(=O)Cc1ccc(C2CC2)c(F)c1` |
| M013 | C09 | `Cc1nc(-c2nnn(C)c2NC(=O)O[C@H](C)c2ccccc2Cl)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M014 | C10 | `Cc1cc(C#N)ncc1Oc1cc(Nc2ccc(C(=O)N3CCOCC3)cn2)c2ncn(C)c2n1` |
| M015 | C11 | `CN(C)C(=O)N1CCN(c2cc3c(cc2F)c(=O)c(C(=O)O)cn3C2CC2)CC1` |
| M016 | C12 | `CCc1oc2cccc(I)c2c1C(=O)c1cc(I)c(O)c(I)c1` |
| M017 | C05 | `Cc1ccc(-c2ncc3c(n2)N2CCOC[C@@]2(C)C(=O)N3[C@H]2CC[C@H](O)CC2)c2cc[nH]c12` |
| M018 | C13 | `Cn1cc(-c2oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c3c2-c2cccc(N3CCNCC3)c2)cn1` |
| M019 | C07 | `CCS(=O)(=O)c1nc(S(=O)(=O)c2ccccc2Cl)c(N2CCN(C)C(=O)[C@H]2C)s1` |
| M020 | C14 | `O=C(ONc1nc2nonc2nc1Nc1ccccc1F)c1ccc(OC(F)(F)F)cc1` |
| M021 | C02 | `Cn1nc2c(=O)n(C3CC3)ncc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M022 | C08 | `C[C@@H]1CN(c2ccc(Cl)nn2)CCN1C(=O)Cc1ccc(C2CC2)cc1` |
| M023 | C01 | `O=C(Nc1cccc(-c2nncn2CC2CC2)c1)c1cc2c(cc1F)OCc1cncn1-2` |
| M024 | C15 | `Cc1cc(F)ccc1-c1cc2c(cn1)ncn2-c1cnc2c(cnn2C)c1` |
| M025 | C16 | `O=S(=O)(NCCN1CCNCC1)c1ccc(NC2CCCCC2)c(NCc2ccccc2)c1` |
| M026 | C08 | `O=C(Cc1ccc(C2CC2)c(F)c1)N1CCN(c2ccc(Cl)nn2)CC1` |
| M027 | C07 | `CCP1(=O)CCN(c2sc(S(=O)(=O)CC)nc2S(=O)(=O)c2cccc(Cl)c2Cl)CC1` |
| M028 | C14 | `CC(C)COC(=O)NNc1nc2nonc2nc1Nc1ccccc1F` |
| M029 | C14 | `CC(C)(C)OC(=O)NNc1nc2nonc2nc1Nc1ccccc1Cl` |
| M030 | C17 | `COc1cc(C(=O)N2CC3(COC3)C2)ccc1NCC#Cc1cc2c(N[C@@H]3CCN(C)C[C@@H]3F)cccc2n1CC(F)(F)F` |
| M031 | C17 | `COc1cc(S(C)(=O)=O)ccc1NCC#Cc1cc2c(N[C@@H]3CCN(C)C[C@@H]3F)cccc2n1CC(F)(F)F` |
| M032 | C18 | `FC(F)(F)c1nc2c(-c3cccc(Cl)c3)ccnc2[nH]1` |
| M033 | C18 | `FC(F)(F)c1nc2c(-c3cc(Cl)cc(Cl)c3)ccnc2[nH]1` |
| M034 | C18 | `FC(F)(F)c1ccc(-c2ccnc3[nH]c(C(F)(F)F)nc23)cc1` |
| M035 | C18 | `Fc1cc(F)cc(-c2ccnc3[nH]c(C(F)(F)F)nc23)c1` |
| M036 | C19 | `CN(C(=O)N1CCN(c2cc3c(cc2F)c(=O)c(C(=O)O)cn3C2CC2)CC1)C(F)(F)F` |
| M037 | C19 | `O=C(O)c1cn(C2CC2)c2cc(N3CCN(C(=O)N(C4CC4)C(F)(F)F)CC3)c(F)cc2c1=O` |
| M038 | C02 | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M039 | C02 | `CC[C@@](N)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ncn(C3CC3)c(=O)c2nn1C` |
| M040 | C02 | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C1CC1` |

## 1. Interval prediction

Assign L, M, or H using the following ranges (ng/mL). These are numerical endpoint ranges under the listed animal-study conditions, rather than universal development criteria.

| Label | Interval | Interpretation |
|---|---|---|
| L | value < 100 | Lower peak total concentration range in this dosing context |
| M | 100 <= value < 1000 | Intermediate peak total concentration range in this dosing context |
| H | value >= 1000 | Higher peak total concentration range in this dosing context |

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

Compare total oral Cmax. Let R = value(left) / value(right). Choose A if R > 3; B if 1/3 <= R <= 3; C if R < 1/3.

Each pair belongs to one literature analogue family and one study context. B denotes only the specified numerical difference category; it does not establish statistical equivalence. No cross-species or cross-dose comparison is requested.

| Item | Left molecule | Right molecule | Points |
|---|---|---|---|
| Q028 | M028 | M029 | 8 |
| Q029 | M030 | M031 | 7 |
| Q030 | M032 | M033 | 7 |
| Q031 | M034 | M035 | 7 |
| Q032 | M036 | M037 | 7 |

## 3. Within-series ordering

Order each group from highest to lowest total oral Cmax at its stated common dose and formulation.

Each group shares one study context. Its score is the listed points multiplied by max(0, Spearman rho) between the submitted and reference orders.

| Item | Molecules to order | Points |
|---|---|---|
| Q033 | M038, M039, M040 | 10 |

## Response format and scoring

Return ONLY a strict JSON object mapping each listed Q identifier to L/M/H for interval items, A/B/C for comparisons, or an ordered array of the listed molecule IDs for ordering items.

Syntax example only; these values do not imply answers:

`{"Q001": "L", "Q028": "B", "Q033": ["M038", "M039", "M040"]}`

Each molecule is assessed in one item. Missing or invalid items earn zero. An ordering array must contain every specified molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0–1 scale.
