---
bench_id: "SM-077-Molecular-Biology-ADMET-Classification"
category: "Molecular-Biology"
format: "structured_json"
---
# Prompt

Predict ex-vivo stability of the dosed parent molecule under its indicated assay context. There are 50 distinct molecules. Total: 100 points.

T denotes parent-disappearance half-life in hours; R denotes percentage of intact parent remaining after 2 h. Apply each row's endpoint. All comparisons and ordering groups use T within one chemical series and assay context.

## Assay contexts

| Context | Conditions |
|---|---|
| C01 | Human plasma; 5 uM compound; 37 C; 120 min incubation; HPLC-MS/MS measurement of parent remaining. |
| C02 | Human plasma; reported parent-compound plasma stability assay. Other incubation settings are unspecified here. |
| C03 | Pooled human K2EDTA plasma (approximately 99% plasma); 1 uM compound; 37 C; LC-MS/MS; sampling from 0.2 to 240 min. The reported half-life reflects loss of the dosed parent, including rapid initial loss. |
| C04 | Mouse plasma; reported parent-compound plasma stability assay. Other incubation settings are unspecified here. |
| C05 | 50% pooled human plasma in Tris-buffered saline, pH 7.5; 100 uM compound; 37 C; intact parent quantified by LC-MS. |
| C06 | 50% human plasma in Tris-buffered saline; 100 uM compound; parent remaining measured by MS. |

## Molecules

| Molecule ID | Context | Endpoint | SMILES |
|---|---|---|---|
| M001 | C01 | R | `CC(C)[C@@H]1CCN1Cc1cc2cnc(NC(=O)c3ccc4nncn4c3)cc2[nH]1` |
| M002 | C01 | R | `C[C@H]1CCCN1Cc1cc2cnc(NC(=O)c3ccc4nncn4c3)cc2[nH]1` |
| M003 | C02 | T | `CC(C)(C)OC(=O)Nc1cc(F)cn([C@@H](CC2CC2)C(=O)N[C@@H](C[C@@H]2CCNC2=O)C(=O)C(N)=O)c1=O` |
| M004 | C03 | T | `CC(=O)Oc1cccc2[nH]cc(CCN(C)C)c12` |
| M005 | C02 | T | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cc(F)cc(NC(=O)OC(C)(C)C)c1=O` |
| M006 | C02 | T | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)OC(C)(C)C)c1=O` |
| M007 | C02 | T | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)Nc2ccccc2)c1=O` |
| M008 | C03 | T | `CN(C)CCc1c[nH]c2cccc(OC(=O)C3CC3)c12` |
| M009 | C01 | R | `CC(C)(C)C1CCN1Cc1ccc(CNC(=O)c2ccc3nncn3c2)cc1` |
| M010 | C02 | T | `CC(C)(C)OC(=O)Nc1cccn([C@@H](CC2CC2)C(=O)N[C@@H](C[C@@H]2CCNC2=O)C(=O)C(N)=O)c1=O` |
| M011 | C04 | T | `CC(C)CC(C(=O)Nc1ccc(-c2ccc(Cl)cc2)cc1)P(=O)(O)O` |
| M012 | C04 | T | `CC(C)CC(C(=O)Nc1ccc(NC(=O)c2ccncc2)cc1)P(=O)(O)O` |
| M013 | C03 | T | `CN(C)CCc1c[nH]c2cccc(OCc3ccccc3)c12` |
| M014 | C01 | R | `O=C(Nc1cc2[nH]c(CN3CCC3C3CC3)cc2cn1)c1ccc2nncn2c1` |
| M015 | C02 | T | `CC(C)(C)OC(=O)Nc1cccn([C@@H](CC2CC2)C(=O)N[C@@H](C[C@@H]2CCNC2=O)C(=O)C(=O)NC2CC2)c1=O` |
| M016 | C04 | T | `CC(C)CC(C(=O)Nc1ccc(NC(=O)c2nc3ccccc3s2)cc1)P(=O)(O)O` |
| M017 | C05 | T | `C/C(=C\CCP(=O)(OCOC(=O)c1cccc(C(F)(F)F)c1)Oc1ccc(C(C)C)cc1)CO` |
| M018 | C04 | T | `CC(C)CC(C(=O)Nc1ccc(N2CCN(C)CC2)cc1)P(=O)(O)O` |
| M019 | C04 | T | `CC(C)CC(C(=O)Nc1ccc(-c2ccc(Cl)cc2)nc1)P(=O)(O)O` |
| M020 | C01 | R | `O=C(NCc1ccc(CNc2ncc(F)cn2)cc1)c1ccc2nncn2c1` |
| M021 | C04 | T | `CC(C)CC(C(=O)Nc1cnc(-c2ccc(OC(C)C)cc2)nc1)P(=O)(O)O` |
| M022 | C03 | T | `CCOC(=O)Oc1cccc2[nH]cc(CCN(C)C)c12` |
| M023 | C01 | R | `CC(C)C1CCN1Cc1ccc(CNC(=O)c2ccc3nncn3c2)cc1` |
| M024 | C02 | T | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)NC2CCCCC2)c1=O` |
| M025 | C01 | R | `CC1CCN1Cc1ccc(CNC(=O)c2ccc3nncn3c2)cc1` |
| M026 | C01 | R | `O=C(NCc1cccc(CN2CCC2)c1)c1ccc2nncn2c1` |
| M027 | C04 | T | `CC(C)CC(C(=O)Nc1ccc(N2CCNCC2)cc1)P(=O)(O)O` |
| M028 | C02 | T | `CNC(=O)C(=O)[C@H](C[C@@H]1CCNC1=O)NC(=O)[C@H](CC1CC1)n1cccc(NC(=O)C(C)C)c1=O` |
| M029 | C04 | T | `CC(C)CC(C(=O)Nc1ccc(NS(=O)(=O)c2ccc(Cl)c(Cl)c2)cc1)P(=O)(O)O` |
| M030 | C01 | R | `CSc1ccc(CNC(=O)c2ccc3nncn3c2)cc1` |
| M031 | C06 | T | `CC(=O)OC/C(C)=C/CCP(=O)(OCOC(=O)CC1CCOCC1)Oc1ccc(C(C)C)cc1` |
| M032 | C06 | T | `CC(=O)OC/C(C)=C/CCP(=O)(OCOC(=O)c1ccccc1)Oc1ccc(C(C)C)cc1` |
| M033 | C06 | T | `COc1ccc(C(=O)OCOP(=O)(CC/C=C(\C)CO)Oc2ccc(C(C)C)cc2)cc1` |
| M034 | C06 | T | `C/C(=C\CCP(=O)(OCOC(=O)CC1CCCCC1)Oc1ccc(C(C)C)cc1)CO` |
| M035 | C05 | T | `CC(=O)OC/C(C)=C/CCP(=O)(OCOC(=O)c1ccccc1F)Oc1ccc(C(C)C)cc1` |
| M036 | C05 | T | `CC(=O)OC/C(C)=C/CCP(=O)(OCOC(=O)c1ccc(C(C)=O)cc1)Oc1ccc(C(C)C)cc1` |
| M037 | C05 | T | `C/C(=C\CCP(=O)(OCOC(=O)c1ccc(C#N)cc1)Oc1ccc(C(C)C)cc1)CO` |
| M038 | C05 | T | `CC(=O)OC/C(C)=C/CCP(=O)(OCOC(=O)c1cccc(C(F)(F)F)c1)Oc1ccc(C(C)C)cc1` |
| M039 | C05 | T | `CC(=O)OC/C(C)=C/CCP(=O)(OCOC(=O)c1ccc(C#N)cc1F)Oc1ccc(C(C)C)cc1` |
| M040 | C05 | T | `C/C(=C\CCP(=O)(OCOC(=O)c1ccc(C#N)cc1F)Oc1ccc(C(C)C)cc1)CO` |
| M041 | C05 | T | `CC(=O)OC/C(C)=C/CCP(=O)(OCOC(=O)c1ccc(C(F)(F)F)cc1)Oc1ccc(C(C)C)cc1` |
| M042 | C05 | T | `CC(=O)OC/C(C)=C/CCP(=O)(OCOC(=O)c1ccc(C(F)(F)F)c(F)c1)Oc1ccc(C(C)C)cc1` |
| M043 | C06 | T | `CC(=O)OC/C(C)=C/CCP(=O)(OCOC(=O)CC1CCCCC1)Oc1ccc(C(C)C)cc1` |
| M044 | C06 | T | `C/C(=C\CCP(=O)(OCOC(=O)c1ccccc1)Oc1ccc(C(C)C)cc1)CO` |
| M045 | C06 | T | `COc1ccc(C(=O)OCOP(=O)(CC/C=C(\C)COC(C)=O)Oc2ccc(C(C)C)cc2)cc1` |
| M046 | C06 | T | `C/C(=C\CCP(=O)(OCOC(=O)C1CCOCC1)Oc1ccc(C(C)C)cc1)CO` |
| M047 | C05 | T | `C/C(=C\CCP(=O)(OCOC(=O)c1ccccc1F)Oc1ccc(C(C)C)cc1)CO` |
| M048 | C05 | T | `C/C(=C\CCP(=O)(OCOC(=O)c1ccc(C(F)(F)F)cc1)Oc1ccc(C(C)C)cc1)CO` |
| M049 | C05 | T | `C/C(=C\CCP(=O)(OCOC(=O)c1ccc([N+](=O)[O-])cc1)Oc1ccc(C(C)C)cc1)CO` |
| M050 | C05 | T | `C/C(=C\CCP(=O)(OCOC(=O)c1cc(C(F)(F)F)cc(C(F)(F)F)c1)Oc1ccc(C(C)C)cc1)CO` |

## 1. Interval prediction

| Label | Interpretation | T: half-life (h) | R: parent remaining at 2 h (%) |
|---|---|---|---|
| L | Faster parent loss | < 1 | < 50 |
| M | Intermediate parent persistence | 1 to < 4 | 50 to < 90 |
| H | Slower parent loss | >= 4 | >= 90 |

Apply the thresholds separately to T and R. These are task-specific persistence intervals under each stated condition; they are not universal development go/no-go criteria.

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
| Q025 | M025 |
| Q026 | M026 |
| Q027 | M027 |
| Q028 | M028 |
| Q029 | M029 |
| Q030 | M030 |

## 2. Analogue comparisons

Compare plasma parent-disappearance half-lives. A: left/right > 3 (left is more stable); B: 1/3 <= left/right <= 3; C: left/right < 1/3 (left is less stable).

Each correct item earns 5 points. Each pair shares one assay context. "Similar" denotes the stated numerical category for the reported central results.

| Item | Left molecule | Right molecule |
|---|---|---|
| Q031 | M031 | M032 |
| Q032 | M033 | M034 |
| Q033 | M035 | M036 |
| Q034 | M037 | M038 |
| Q035 | M039 | M040 |
| Q036 | M041 | M042 |

## 3. Within-series ordering

Order each group from longest to shortest parent-disappearance half-life. All molecules within a group share one assay context. Use each molecule exactly once.

Each group is worth 5 points, multiplied by max(0, Spearman rho) between the submitted and reference order.

| Item | Molecules to order |
|---|---|
| Q037 | M043, M044, M045, M046 |
| Q038 | M047, M048, M049, M050 |

## Response format and scoring

Return ONLY one strict JSON object mapping each listed Q identifier to its response: L/M/H for interval items, A/B/C for comparisons, and an ordered array of molecule IDs for ordering items.

Syntax example only; the values do not imply answers:

`{"Q001": "L", "Q031": "B", "Q037": ["M043", "M044", "M045", "M046"]}`

Missing or invalid items earn zero. An ordering array must contain every listed molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0–1 scale.
