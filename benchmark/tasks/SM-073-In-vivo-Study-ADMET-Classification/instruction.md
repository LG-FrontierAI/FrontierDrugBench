---
bench_id: "SM-073-In-vivo-Study-ADMET-Classification"
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
| C01 | mouse; C57BL/6J; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 99.8% of0.5% methylcellulose in water,0.2% Tween80. |
| C02 | mouse; ICR; male. PO 10 mg/kg. Matrix: plasma. Dosed form: hydrochloride salt. Vehicle/formulation: unspecified. Sampling: 0,0.5,1,2,4,6,8,16,24h. |
| C03 | mouse. PO 3 mg/kg. Matrix: whole blood. |
| C04 | rat; Sprague-Dawley; male. PO 3 mg/kg. Matrix: plasma. Vehicle/formulation: 0.5%HPMC/0.5%benzyl alcohol/0.4%polysorbate80 in water. Feeding: overnight fast,food restored4h. Sampling: to72h. |
| C05 | mouse; C57BL/6; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 99.8% of0.5% methylcellulose in water,0.2% Tween80. |
| C06 | rat; Sprague-Dawley; male. PO 5 mg/kg. Matrix: plasma. Sampling: 0.25,0.5,1,2,4,8,24h. |
| C07 | mouse; ICR; male. PO 3 mg/kg. Matrix: plasma. Dosed form: hydrochloride salt. Vehicle/formulation: unspecified. Sampling: 0,0.5,1,2,4,6,8,16,24h. |
| C08 | mouse; CD-1; male. PO 40 mg/kg. Matrix: plasma. Feeding: nonfasted. |
| C09 | mouse; db/db. PO 100 mg/kg. Matrix: blood-derived; plasma versus whole blood not explicit in PK methods. Vehicle/formulation: 1% hydroxyethyl cellulose. Feeding: fed. Sampling: 0.5,1,2,4,6,24h;2 samples/mouse. |
| C10 | mouse. PO 20 mg/kg. Matrix: systemic blood-derived;matrix subtype unspecified. Vehicle/formulation: PEG300/D5W3:1 solution;2.9mg/mL. |
| C11 | rat. PO 4 mg/kg. Matrix: systemic blood-derived;matrix subtype unspecified. Vehicle/formulation: 0.5% methylcellulose. |
| C12 | rat. PO 11 mg/kg. Matrix: plasma. Vehicle/formulation: 0.5%MC/0.1%Tween80 in saline; source form not specified. |
| C13 | rat. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 10%Tween80 in water; source form not specified. |
| C14 | mouse. PO 10 mg/kg. Matrix: plasma. |
| C15 | rat; Han Wistar; male. PO 0.5 mg/kg. Matrix: plasma. Vehicle/formulation: 0.5%HPMC/0.1%Tween in water. Feeding: free access to food and water. Sampling: 0.08,0.25,0.5,1,2,4,8,24h. Cassette dosing. |
| C16 | mouse; CD-1; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: DMSO/Cremophor/PBS 10/10/80. Sampling: seven PO timepoints to24h. |
| C17 | mouse; C57BL/6; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 99.8% of0.5% methylcellulose in water,0.2% Tween80. Sampling: to24h. |
| C18 | mouse; C57BL/6; male. PO 10 mg/kg. Matrix: plasma. Vehicle/formulation: 99.8% of0.5%methylcellulose in water/0.2%Tween80. Sampling: to24h. |
| C19 | rat; Han Wistar; male. PO 1 mg/kg. Matrix: plasma. Vehicle/formulation: 0.5%HPMC/0.1%Tween in water. Feeding: free access to food and water. Sampling: 0.08,0.25,0.5,1,2,4,8,24h. Cassette dosing. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `CC(C)(C)OC(=O)NNc1nc2nonc2nc1Nc1ccccc1F` |
| M002 | C02 | `CN(C)Cc1ccc(-c2c(-c3cnn(C)c3)oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c23)cc1` |
| M003 | C03 | `Cc1cc(C#N)ccc1-c1cc2c(cn1)ncn2-c1ccc2c(C)n[nH]c2c1` |
| M004 | C04 | `Cc1nn(C2CC2)c(=O)c2nn(C)c(Cc3ccc(C(F)(F)F)c(C#N)c3)c12` |
| M005 | C04 | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1ccc(C(F)(F)F)nc1)C1CC1` |
| M006 | C05 | `Oc1nc2nonc2cc1Nc1cc(C(F)(F)F)ccc1C(F)(F)F` |
| M007 | C06 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCc2cncn2-3)c1` |
| M008 | C04 | `Cn1nc2c(=O)n(C3CC3)cnc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M009 | C07 | `Cn1cc(-c2oc3ncnc(Oc4ccc(NC(=O)c5cccn(-c6ccc(F)cc6)c5=O)cc4)c3c2-c2cccc(N)c2)cn1` |
| M010 | C08 | `NCCNC(=O)c1cc2c(ncn2Cc2ccccc2)c(-c2cc(Cl)c(Cl)c(Cl)c2)n1` |
| M011 | C03 | `Cc1cc(F)ncc1-c1cc2c(cn1)ncn2-c1ccc2c(cnn2C)c1` |
| M012 | C09 | `CCS(=O)(=O)c1nc(S(=O)(=O)c2ccccc2C#N)c(N2CCN(C)C(=O)[C@H]2C)s1` |
| M013 | C10 | `Cc1cc(N2CCc3c(c(C)nn3CC34CCC(N)(CC3)CC4)C2)c2cnn(C)c2n1` |
| M014 | C11 | `C[C@@]12COCCN1c1nc(-c3cccc4[nH]ccc34)ncc1N([C@H]1CC[C@@H](O)CC1)C2=O` |
| M015 | C12 | `[2H]C1([2H])CC(c2cn3ncnc3cc2Cl)CC([2H])([2H])N1S(=O)(=O)c1cnc(C)o1` |
| M016 | C13 | `Cc1ncc(S(=O)(=O)N2CCC(c3cn4ncnc4cc3Cl)CC2)o1` |
| M017 | C09 | `CN1CCN(c2sc(S(=O)(=O)C3CC3)nc2S(=O)(=O)c2ccccc2Cl)CC1=O` |
| M018 | C06 | `CC(C)n1cnnc1-c1cccc(NC(=O)c2cc3c(cc2F)OCC(=O)N3C)n1` |
| M019 | C14 | `N#Cc1ccc(N2CCN(C(=O)Cc3ccc(C4CC4)c(F)c3)CC2)nn1` |
| M020 | C04 | `CC[C@@](O)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2cnn(C3CC3)c(=O)c2nn1C` |
| M021 | C15 | `CC(C)N(C)C(=O)N1CCN(c2cc3c(cc2F)c(=O)c(C(=O)O)cn3C2CC2)CC1` |
| M022 | C04 | `CCn1cc(C2CC2)c2c(Cc3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M023 | C06 | `O=C1COc2cc(F)c(C(=O)Nc3cccc(-c4nncn4-c4ccccc4)n3)cc2N1` |
| M024 | C16 | `Nc1cc(-c2cnco2)ccc1NC1CCCCC1` |
| M025 | C06 | `O=C(Nc1cccc(-c2nncn2CC2CC2)n1)c1cc2c(cc1F)OCc1cncn1-2` |
| M026 | C17 | `Oc1c(Nc2ccc(-c3cccc(F)c3)cc2)cnc2nonc12` |
| M027 | C14 | `O=C(Cc1ccc(C2CC2)cc1)N1CCN(c2ccc(Cl)nn2)CC1` |
| M028 | C05 | `Oc1nc2nonc2cc1Nc1cc(C(F)(F)F)c(F)cc1F` |
| M029 | C05 | `Oc1nc2nonc2cc1Nc1c(F)c(F)c(C(F)(F)F)c(F)c1F` |
| M030 | C18 | `FC(F)(F)Oc1cccc(-c2ccnc3[nH]c(C(F)(F)F)nc23)c1` |
| M031 | C18 | `FC(F)(F)c1cccc(-c2ccnc3[nH]c(C(F)(F)F)nc23)c1` |
| M032 | C17 | `Oc1c(Nc2ccc(-c3cccc(Cl)c3)cc2)cnc2nonc12` |
| M033 | C17 | `Oc1c(Nc2ccc(-c3ccc(Cl)cc3)cc2)cnc2nonc12` |
| M034 | C19 | `CC(C)N(C(=O)N1CCN(c2cc3c(cc2F)c(=O)c(C(=O)O)cn3C2CC2)CC1)C1CC1` |
| M035 | C19 | `CN(C(=O)N1CCN(c2cc3c(cc2F)c(=O)c(C(=O)O)cn3C2CC2)CC1)C1CC1` |
| M036 | C05 | `Oc1nc2nonc2cc1Nc1cc(C(F)(F)F)ccc1F` |
| M037 | C05 | `Oc1nc2nonc2cc1Nc1ccc(OC(F)(F)F)cc1C(F)(F)F` |
| M038 | C04 | `CCn1ccc2c([C@](O)(c3cnc(C(F)(F)F)c(Cl)c3)C3CC3)n(C)nc2c1=O` |
| M039 | C04 | `CC[C@@](N)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ccn(C3CC3)c(=O)c2nn1C` |
| M040 | C04 | `CC[C@@](O)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ccn(C3CC3)c(=O)c2nn1C` |

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
