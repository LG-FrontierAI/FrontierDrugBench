---
bench_id: "SM-078-Molecular-Biology-ADMET-Classification"
category: "Molecular-Biology"
format: "structured_json"
---
# Prompt

Predict human plasma protein binding under each indicated assay context. There are 50 distinct molecules. Total: 100 points.

PPB denotes protein-bound percentage on a 0–100% scale. For analogue comparisons use unbound fraction fu = 1 - PPB/100. Binding strength here describes equilibrium partition into bound and unbound pools; desirability depends on the drug's exposure and pharmacology.

## Assay contexts

| Context | Conditions |
|---|---|
| C01 | Human plasma; reported plasma protein binding assay. Incubation settings are unspecified here. |
| C02 | Human plasma; equilibrium dialysis at 37 C for 18 h; pH 7.4 phosphate buffer; LC-MS/MS readout. Final compound concentration in plasma is unspecified. |
| C03 | Pooled human plasma; rapid equilibrium dialysis; 2 uM compound; 37 C; 6 h; pH 7.4. |
| C04 | Human plasma; equilibrium dialysis with LC-MS/MS readout. Other incubation details are unspecified here. |
| C05 | Human plasma; rapid equilibrium dialysis; 1 uM compound; 37 C; 5 h. |

## Molecules

| Molecule ID | Context | Endpoint | SMILES |
|---|---|---|---|
| M001 | C01 | PPB | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)CCc2cccs2)c1=O` |
| M002 | C02 | PPB | `CCCc1c(CC)n[nH]c1Nc1ccnc2[nH]ccc12` |
| M003 | C01 | PPB | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)C2CCCCC2)c1=O` |
| M004 | C02 | PPB | `CCc1cc(Nc2ccnc3[nH]ccc23)[nH]n1` |
| M005 | C03 | PPB | `Cc1nn(C2CC2)c(=O)c2nn(C)c(Cc3ccc(C(F)(F)F)c(C#N)c3)c12` |
| M006 | C04 | PPB | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(S(N)(=O)=O)C2)c(OC(F)F)n1` |
| M007 | C05 | PPB | `Cc1ccc(NC(=O)c2ccc(S(=N)C3CC3)cc2)cc1Nc1nccc(-c2cccnc2)n1` |
| M008 | C05 | PPB | `CN=S(C)(=O)c1ccc(C(=O)Nc2ccc(C)c(Nc3nccc(-c4cccnc4)n3)c2)cc1` |
| M009 | C04 | PPB | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(CCNS(N)(=O)=O)C2)c(OC(F)F)n1` |
| M010 | C04 | PPB | `COc1cc(C)ccc1NC(=O)C1(c2ccccc2C(C)C)CN(C(=O)CCC(=O)O)C1` |
| M011 | C05 | PPB | `Cc1ccc(NC(=O)c2ccc(C(=O)O)cc2)cc1Nc1nccc(-c2cccnc2)n1` |
| M012 | C04 | PPB | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(C(=O)CC3(C(=O)O)CC3)C2)c(OC(F)F)n1` |
| M013 | C02 | PPB | `c1cc(Nc2cc(C3CC3)n[nH]2)c2cc[nH]c2n1` |
| M014 | C05 | PPB | `Cc1c(-c2ccnn2C)cc(C(=O)NCc2ccc(S(C)(=N)=N)cc2)c(=O)n1-c1cccc(C(F)(F)F)c1` |
| M015 | C04 | PPB | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(C(=O)CC(C)(C)C(=O)O)C2)c(OC(F)F)n1` |
| M016 | C04 | PPB | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(C(=O)CC3(C(=O)O)CCC3)C2)c(OC(F)F)n1` |
| M017 | C04 | PPB | `Cc1ccc(NC(=O)C2(c3ncccc3C(C)C)CNC2)c(OC(F)F)n1` |
| M018 | C05 | PPB | `Cc1c(-c2ccnn2C)cc(C(=O)NCc2ccc(S(=N)C3CC3)cc2)c(=O)n1-c1cccc(C(F)(F)F)c1` |
| M019 | C01 | PPB | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)CCc2ccccc2)c1=O` |
| M020 | C05 | PPB | `Cc1ccc(NC(=O)c2ccc(S(=N)(=O)C3CC3)cc2)cc1Nc1nccc(-c2cccnc2)n1` |
| M021 | C02 | PPB | `Fc1ccccc1Nc1ccnc2[nH]ccc12` |
| M022 | C02 | PPB | `CC(C)(C)c1cc(Nc2ccnc3[nH]ccc23)[nH]n1` |
| M023 | C04 | PPB | `COc1cc(C)ccc1NC(=O)C1(c2ccccc2C(C)C)CCN(C(=O)CCC(=O)O)CC1` |
| M024 | C02 | PPB | `Cc1cc(Nc2ccnc3[nH]ccc23)[nH]n1` |
| M025 | C05 | PPB | `Cc1ccc(NC(=O)c2ccc(P(C)(C)=O)cc2)cc1Nc1nccc(-c2cccnc2)n1` |
| M026 | C05 | PPB | `Cc1ccc(NC(=O)c2ccc(S(C)=O)cc2)cc1Nc1nccc(-c2cccnc2)n1` |
| M027 | C04 | PPB | `COc1cc(Cl)ncc1NC(=O)C1(c2ccccc2C(C)C)CN(S(N)(=O)=O)C1` |
| M028 | C04 | PPB | `COc1cc(C)ncc1NC(=O)C1(c2ccccc2C(C)C)CNC1` |
| M029 | C01 | PPB | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)Cc2ccccc2)c1=O` |
| M030 | C01 | PPB | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cc(F)cc(NC(=O)OC(C)(C)C)c1=O` |
| M031 | C02 | PPB | `CCCc1n[nH]c(Nc2ccnc3[nH]ccc23)c1CC` |
| M032 | C02 | PPB | `CCCc1n[nH]c(Nc2ccnc3[nH]ccc23)c1CCC` |
| M033 | C03 | PPB | `Cn1nc2c(=O)n(C3CC3)cnc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M034 | C03 | PPB | `CC[C@@](N)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ncn(C3CC3)c(=O)c2nn1C` |
| M035 | C03 | PPB | `CC[C@@](O)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ccn(C3CC3)c(=O)c2nn1C` |
| M036 | C03 | PPB | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1ccc(C(F)(F)F)nc1)C1CC1` |
| M037 | C02 | PPB | `CCc1n[nH]c(Nc2ccnc3[nH]ccc23)c1C` |
| M038 | C02 | PPB | `CCCc1n[nH]c(Nc2ccnc3[nH]ccc23)c1C(C)C` |
| M039 | C05 | PPB | `Cc1c(-c2ccnn2C)cc(C(=O)NCc2ccc(/S(C)=N/C#N)cc2)c(=O)n1-c1cccc(C(F)(F)F)c1` |
| M040 | C05 | PPB | `Cc1c(-c2ccnn2C)cc(C(=O)NCc2ccc(S(C)=O)cc2)c(=O)n1-c1cccc(C(F)(F)F)c1` |
| M041 | C03 | PPB | `CCn1cc(C)c2c([C@H](N)c3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M042 | C03 | PPB | `CCn1cc(C)c2c([C@H](O)c3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M043 | C03 | PPB | `CCn1ccc2c([C@@](O)(CC)c3ccc(C(F)(F)F)nc3)n(C)nc2c1=O` |
| M044 | C03 | PPB | `Cn1nc2c(=O)n(C3CC3)ccc2c1[C@](O)(c1cnc(C(F)(F)F)c(Cl)c1)C(F)(F)F` |
| M045 | C03 | PPB | `CC[C@@](N)(c1cnc(C(F)(F)F)c(Cl)c1)c1c2ccn(C3CC3)c(=O)c2nn1C` |
| M046 | C01 | PPB | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)OC(C)(C)C)c1=O` |
| M047 | C01 | PPB | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)NCc2ccccc2)c1=O` |
| M048 | C01 | PPB | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)C(C)C)c1=O` |
| M049 | C01 | PPB | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)Nc2ccccc2)c1=O` |
| M050 | C01 | PPB | `CC(C)(C)OC(=O)Nc1cccn([C@@H](CC2CC2)C(=O)N[C@@H](C[C@@H]2CCNC2=O)C(=O)C(N)=O)c1=O` |

## 1. Interval prediction

| Label | Protein-bound percentage | Corresponding unbound fraction fu |
|---|---|---|
| L | < 90% | > 10% |
| M | 90% to < 99% | > 1% to 10% |
| H | >= 99% | <= 1% |

L/M/H label the bound-percentage intervals; the unbound-fraction column indicates the corresponding exposure-relevant range. A rounded 100% result belongs to H without implying an exact zero unbound fraction.

Each correct item earns 2 points.

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

A: left binds more strongly, fu(left) < fu(right)/3; B: unbound fractions differ by at most 3-fold, 1/3 <= fu(left)/fu(right) <= 3; C: left binds less strongly, fu(left) > 3*fu(right). Compare unbound fractions; applying a fold threshold directly to bound percentages would compress differences near high binding.

Each correct item earns 4 points. Each pair shares one assay context. "Similar" denotes the stated numerical category for the reported central results.

| Item | Left molecule | Right molecule |
|---|---|---|
| Q025 | M025 | M026 |
| Q026 | M027 | M028 |
| Q027 | M029 | M030 |
| Q028 | M031 | M032 |
| Q029 | M033 | M034 |
| Q030 | M035 | M036 |
| Q031 | M037 | M038 |
| Q032 | M039 | M040 |

## 3. Within-series ordering

Order each group from highest to lowest protein-bound percentage. This is equivalently lowest to highest unbound fraction. All molecules within a group share one assay context. Use each molecule exactly once.

Each group is worth 10 points, multiplied by max(0, Spearman rho) between the submitted and reference order.

| Item | Molecules to order |
|---|---|
| Q033 | M041, M042, M043, M044, M045 |
| Q034 | M046, M047, M048, M049, M050 |

## Response format and scoring

Return ONLY one strict JSON object mapping each listed Q identifier to its response: L/M/H for interval items, A/B/C for comparisons, and an ordered array of molecule IDs for ordering items.

Syntax example only; the values do not imply answers:

`{"Q001": "L", "Q025": "B", "Q033": ["M041", "M042", "M043", "M044", "M045"]}`

Missing or invalid items earn zero. An ordering array must contain every listed molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0–1 scale.
