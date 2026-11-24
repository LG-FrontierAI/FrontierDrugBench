---
bench_id: "SM-088-Cell-Biology-Activity-Prediction"
category: "Cell-Biology"
format: "structured_json"
---
# Prompt

Predict concentration potency for suppression of LPA-stimulated cellular responses associated with human LPAR1 in the indicated assay. There are 50 distinct molecules. Total: 100 points.

Calcium mobilization, the Tango beta-arrestin reporter and MRTF-A nuclear translocation have distinct assay contexts; the author-reported endpoint is IC50 or EC50 as specified. Comparisons and ordering stay within one context.

Use each molecule's assay context. In the tables below, P denotes its stated IC50, EC50, DC50, qAC50 or CD, expressed in nM. Lower P means greater concentration potency.

## Reference protein sequences

A canonical full-length human LPAR1 FASTA is provided as `LPAR1_HUMAN_Q92633_full_length.fasta` and may be consulted if useful. Reporter tags and assay-specific cell-line constructs are not included in the reference sequence.

Target FASTA (`LPAR1_HUMAN_Q92633_full_length.fasta`):

>LPAR1_HUMAN|Q92633|full_length|UniProt_reference
MAAISTSIPVISQPQFTAMNEPQCFYNESIAFFYNRSGKHLATEWNTVSKLVMGLGITVCIFIMLANLLVMVAIYVNRRF
HFPIYYLMANLAAADFFAGLAYFYLMFNTGPNTRRLTVSTWLLRQGLIDTSLTASVANLLAIAIERHITVFRMQLHTRMS
NRRVVVVIVVIWTMAIVMGAIPSVGWNCICDIENCSNMAPLYSDSYLVFWAIFNLVTFVVMVVLYAHIFGYVRQRTMRMS
RHSSGPRRNRDTMMSLLKTVVIVLGAFIICWTPGLVLLLLDVCCPQCDVLAYEKFFLLLAEFNSAMNPIIYSYRDKEMSA
TFRQILCCQRSENPTGPTEGSDRSASSLNHTILAGVHSNDHSVV


## Assay contexts

| Context | Conditions and endpoint |
|---|---|
| C01 | Rat-derived B103 cells stably expressing human LPAR1; LPA-induced calcium mobilization measured with Fluo-4; 24 h compound preincubation; functional antagonism IC50. |
| C02 | Human TWNT-4 hepatic stellate cells; compound preincubation 1 h, then 1 uM LPA for 30 min; inhibition of MRTF-A nuclear translocation. The author reports an EC50 for this LPAR1-associated downstream functional response. |
| C03 | CHO cells expressing human LPAR1; 30 min compound incubation; FLIPR calcium-mobilization assay; functional antagonist IC50. |
| C04 | Human Tango EDG2-bla U2OS cells expressing human LPAR1; compound preincubation 30 min followed by LPA stimulation for 16 h; beta-arrestin/TEV beta-lactamase reporter FRET; functional antagonism IC50. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `COc1nc(C#N)ccc1NC(=O)N(c1ccccc1C(C)C)C1CCN(C(C)=O)CC1` |
| M002 | C02 | `C[C](OC(=O)Nc1c(-c2ccc(NS(=O)(=O)CC#N)cc2)nnn1C)c1ccccc1Cl` |
| M003 | C03 | `Cc1nc(-c2snc(C)c2NC(=O)O[C@H](C)c2ccccc2Cl)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M004 | C02 | `C[C](OC(=O)Nc1c(-c2ccc(NS(C)(=O)=O)cn2)nnn1C)c1ccccc1` |
| M005 | C04 | `COc1nc(C)ccc1NC(=O)C1(c2ccccc2C(C)C)CNC1` |
| M006 | C04 | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(C(=O)CC(C)(C)C(=O)O)C2)c(OC(F)F)n1` |
| M007 | C04 | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(C(=O)[C@@H](N)CC(=O)O)C2)c(OC(F)F)n1.N` |
| M008 | C04 | `Cc1ccc(NC(=O)C2(c3ncccc3C(C)C)CNC2)c(OC(F)F)n1` |
| M009 | C03 | `Cc1noc(-c2ccc(NC(=O)[C@H]3CCCC[C@@H]3C(=O)O)c(F)n2)c1NC(=O)O[C@H](C)c1ccccc1Cl` |
| M010 | C02 | `C[C](OC(=O)Nc1c(-c2ccc(NS(C)(=O)=O)cn2)nnn1C)c1cccnc1Cl` |
| M011 | C02 | `C[C](OC(=O)Nc1c(-c2ccc(NC(C)=O)cn2)nnn1C)c1cc(F)cnc1F` |
| M012 | C02 | `C[C](OC(=O)Nc1c(-c2ccc(NC(=O)C3CC(F)(F)C3)cn2)nnn1C)c1cc(F)cnc1F` |
| M013 | C01 | `COc1ncccc1NC(=O)N(c1ccccc1C(C)C)C1CCN(C(C)=O)CC1` |
| M014 | C03 | `Cc1nc(-c2onc(C)c2Nc2cncc(OC3CC3)n2)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M015 | C03 | `CCOc1cncc(Nc2c(C)noc2-c2ccc(NC(=O)[C@H]3CCCC[C@@H]3C(=O)O)c(C)n2)n1` |
| M016 | C02 | `C[C](OC(=O)Nc1c(-c2ccc(NS(C)(=O)=O)c(C)n2)nnn1C)c1cc(F)cnc1Cl` |
| M017 | C01 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)[C@@H]2CC[C@]3(C(=O)O)C[C@@H]3C2)c(OC(F)F)n1` |
| M018 | C03 | `Cc1noc(-c2ccc(NC(=O)[C@H]3CCCC[C@@H]3C(=O)O)cn2)c1NC(=O)O[C@H](C)c1ccccc1Cl` |
| M019 | C02 | `C[C](OC(=O)Nc1c(-c2ccc(NS(C)(=O)=O)cn2)nnn1C)c1cccnc1F` |
| M020 | C02 | `C[C](OC(=O)Nc1c(-c2ccc(NC(=O)C(F)(F)F)cc2)nnn1C)c1ccccc1Cl` |
| M021 | C03 | `Cc1nc(-c2onc(C)c2NC(=O)O[C@H](C)c2ccccn2)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M022 | C03 | `Cc1nc(-c2nnn(C)c2NC(=O)O[C@H](C)c2ccccc2Cl)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M023 | C02 | `C[C](OC(=O)Nc1c(-c2ccc(NS(C)(=O)=O)c(C)n2)nnn1C)c1cccnc1F` |
| M024 | C03 | `Cc1nc(-c2cnn(C)c2NC(=O)O[C@H](C)c2ccccc2Cl)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M025 | C03 | `Cc1nc(-c2onc(C)c2CNC(=O)O[C@H](C)c2ccccc2Cl)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M026 | C04 | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(CCNS(N)(=O)=O)C2)c(OC(F)F)n1` |
| M027 | C03 | `Cc1nc(-c2onc(C)c2Nc2cncc(OC(C)C)n2)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M028 | C04 | `Cc1ccc(NC(=O)C2(c3ccncc3C(C)C)CNC2)c(OC(F)F)n1` |
| M029 | C02 | `C[C](OC(=O)Nc1c(-c2ccc(NC(=O)c3ccnc(C(F)(F)F)c3)cn2)nnn1C)c1cc(F)cnc1F` |
| M030 | C04 | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CNC2)c(OC(F)F)n1` |
| M031 | C01 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)[C@H]2CC[C@H](CC(=O)O)CC2)c(OC(F)F)n1` |
| M032 | C01 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)[C@H]2CC[C@@H](CC(=O)O)CC2)c(OC(F)F)n1` |
| M033 | C04 | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(S(N)(=O)=O)C2)c(OC(F)F)n1` |
| M034 | C04 | `CNS(=O)(=O)N1CC(C(=O)Nc2ccc(C)nc2OC(F)F)(c2ccccc2C(C)C)C1` |
| M035 | C02 | `C[C](OC(=O)Nc1c(-c2ccccc2)nnn1C)c1ccccc1Cl` |
| M036 | C02 | `C[C](OC(=O)Nc1c(-c2ccc(O)cc2)nnn1C)c1ccccc1Cl` |
| M037 | C03 | `Cc1nc(-c2onc(C)c2NC(=O)O[C@H](C)c2ccccc2)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M038 | C03 | `Cc1nc(-c2onc(C)c2NC(=O)O[C@H](C)c2ccccc2Cl)ccc1NC(=O)[C@H]1CCCC[C@@H]1C(=O)O` |
| M039 | C01 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)[C@@H]2C[C@H]3CC[C@@H](C2)N3C(C)=O)c(OC(F)F)n1` |
| M040 | C01 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)[C@H]2C[C@H]3CC[C@@H](C2)N3C(C)=O)c(OC(F)F)n1` |
| M041 | C01 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)[C@@H]2CCN(C(C)=O)C[C@@H]2F)c(OC(F)F)n1` |
| M042 | C01 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)[C@H]2CCN(C(C)=O)C[C@H]2F)c(OC(F)F)n1` |
| M043 | C01 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)[C@H]2CCN(C(C)=O)C[C@@H]2F)c(OC(F)F)n1` |
| M044 | C01 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)C2C3CC2CN(C(C)=O)C3)c(OC(F)F)n1` |
| M045 | C01 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)C2CCN(C(C)=O)CC2)c(OC(F)F)n1` |
| M046 | C01 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)[C@H]2[C@@H]3CC[C@H]2CN(C(C)=O)C3)c(OC(F)F)n1` |
| M047 | C04 | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(C(=O)CC3(C(=O)O)CC3)C2)c(OC(F)F)n1` |
| M048 | C04 | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(C(=O)CNS(C)(=O)=O)C2)c(OC(F)F)n1` |
| M049 | C04 | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(C(=O)CC(=O)NS(C)(=O)=O)C2)c(OC(F)F)n1` |
| M050 | C04 | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(C(=O)CNCC(=O)O)C2)c(OC(F)F)n1` |

## 1. Concentration intervals

| Label | P (nM) |
|---|---|
| L | < 10 |
| M | 10 to < 100 |
| H | >= 100 |

These are assay-specific concentration intervals, not universal clinical or development criteria.

Each correct item earns 2 points (30 items; 60 points).

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

Compare concentration potency within each pair. Define R = P(right)/P(left).

| Answer | Criterion | Interpretation |
|---|---|---|
| A | R > 3 | Left has greater concentration potency |
| B | 1/3 <= R <= 3 | Concentration potencies are within threefold |
| C | R < 1/3 | Right has greater concentration potency |

B is a numerical comparison category, not a claim of statistical equivalence. Each pair uses one assay context.

Each correct item earns 4 points (6 items; 24 points).

| Item | Left molecule | Right molecule |
|---|---|---|
| Q031 | M031 | M032 |
| Q032 | M033 | M034 |
| Q033 | M035 | M036 |
| Q034 | M037 | M038 |
| Q035 | M039 | M040 |
| Q036 | M041 | M042 |

## 3. Within-series ordering

Order each group from lowest to highest P (strongest to weakest concentration potency). All four molecules share one assay context. Use every listed molecule exactly once.

Each group earns 8 * max(0, Spearman rho) points for the submitted versus reference order (2 groups; 16 points).

| Item | Molecules to order |
|---|---|
| Q037 | M043, M044, M045, M046 |
| Q038 | M047, M048, M049, M050 |

## Response format and scoring

Return ONLY one strict JSON object mapping Q001-Q038 to responses: L/M/H for classification, A/B/C for comparisons, and an ordered array of molecule IDs for ordering.

Syntax example only; the values do not imply answers:

`{"Q001": "L", "Q031": "B", "Q037": ["M043", "M044", "M045", "M046"]}`

Missing or invalid items earn zero. An ordering array must contain every listed molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0-1 scale.
