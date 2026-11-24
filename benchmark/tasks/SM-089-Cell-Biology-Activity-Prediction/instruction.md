---
bench_id: "SM-089-Cell-Biology-Activity-Prediction"
category: "Cell-Biology"
format: "structured_json"
---
# Prompt

Predict GPR119 cAMP agonist EC50, 5-HT1A p-ERK agonist EC50, or concentration potency for suppression of LPA-stimulated responses, as specified for each molecule. There are 50 distinct molecules. Total: 100 points.

For GPR119, potency refers to cAMP activation and does not specify full versus partial agonism. For 5-HT1A, potency refers to ERK activation without specifying intrinsic efficacy. For LPAR1-associated assays, potency refers to inhibition of the stated stimulated response. Comparisons and ordering never mix agonist and antagonist contexts.

Use each molecule's assay context. In the tables below, P denotes its stated IC50, EC50, DC50, qAC50 or CD, expressed in nM. Lower P means greater concentration potency.

## Reference protein sequences

Canonical full-length human LPAR1, GPR119 and 5-HT1A FASTA files are provided as `LPAR1_HUMAN_Q92633_full_length.fasta`, `GPR119_HUMAN_Q8TDV5_full_length.fasta` and `HTR1A_HUMAN_P08908_full_length.fasta` and may be consulted if useful. Reporter tags and assay-specific constructs are not included in the reference sequences.

Target FASTA (`LPAR1_HUMAN_Q92633_full_length.fasta`):

>LPAR1_HUMAN|Q92633|full_length|UniProt_reference
MAAISTSIPVISQPQFTAMNEPQCFYNESIAFFYNRSGKHLATEWNTVSKLVMGLGITVCIFIMLANLLVMVAIYVNRRF
HFPIYYLMANLAAADFFAGLAYFYLMFNTGPNTRRLTVSTWLLRQGLIDTSLTASVANLLAIAIERHITVFRMQLHTRMS
NRRVVVVIVVIWTMAIVMGAIPSVGWNCICDIENCSNMAPLYSDSYLVFWAIFNLVTFVVMVVLYAHIFGYVRQRTMRMS
RHSSGPRRNRDTMMSLLKTVVIVLGAFIICWTPGLVLLLLDVCCPQCDVLAYEKFFLLLAEFNSAMNPIIYSYRDKEMSA
TFRQILCCQRSENPTGPTEGSDRSASSLNHTILAGVHSNDHSVV

Target FASTA (`GPR119_HUMAN_Q8TDV5_full_length.fasta`):

>GPR119_HUMAN|Q8TDV5|full_length|UniProt_reference
MESSFSFGVILAVLASLIIATNTLVAVAVLLLIHKNDGVSLCFTLNLAVADTLIGVAISGLLTDQLSSPSRPTQKTLCSL
RMAFVTSSAAASVLTVMLITFDRYLAIKQPFRYLKIMSGFVAGACIAGLWLVSYLIGFLPLGIPMFQQTAYKGQCSFFAV
FHPHFVLTLSCVGFFPAMLLFVFFYCDMLKIASMHSQQIRKMEHAGAMAGGYRSPRTPSDFKALRTVSVLIGSFALSWTP
FLITGIVQVACQECHLYLVLERYLWLLGVGNSLLNPLIYAYWQKEVRLQLYHMALGVKKVLTSFLLFLSARNCGPERPRE
SSCHIVTISSSEFDG

Target FASTA (`HTR1A_HUMAN_P08908_full_length.fasta`):

>HTR1A_HUMAN|P08908|full_length|UniProt_reference
MDVLSPGQGNNTTSPPAPFETGGNTTGISDVTVSYQVITSLLLGTLIFCAVLGNACVVAAIALERSLQNVANYLIGSLAV
TDLMVSVLVLPMAALYQVLNKWTLGQVTCDLFIALDVLCCTSSILHLCAIALDRYWAITDPIDYVNKRTPRRAAALISLT
WLIGFLISIPPMLGWRTPEDRSDPDACTISKDHGYTIYSTFGAFYIPLLLMLVLYGRIFRAARFRIRKTVKKVEKTGADT
RHGASPAPQPKKSVNGESGSRNWRLGVESKAGGALCANGAVRQGDDGAALEVIEVHRVGNSKEHLPLPSEAGPTPCAPAS
FERKNERNAEAKRKMALARERKTVKTLGIIMGTFILCWLPFFIVALVLPFCESSCHMPTLLGAIINWLGYSNSLLNPVIY
AYFNKDFQNAFKKIIKCKFCRQ


## Assay contexts

| Context | Conditions and endpoint |
|---|---|
| C01 | Human TWNT-4 hepatic stellate cells; compound preincubation 1 h, then 1 uM LPA for 30 min; inhibition of MRTF-A nuclear translocation. The author reports an EC50 for this LPAR1-associated downstream functional response. |
| C02 | CHO cells expressing human GPR119; cAMP accumulation measured by HTRF after 90 min; agonist EC50. |
| C03 | CHO cells expressing 5-HT1A receptor; 15 min compound incubation; agonist-induced ERK1/2 phosphorylation by AlphaLISA; functional EC50. |
| C04 | Human Tango EDG2-bla U2OS cells expressing human LPAR1; compound preincubation 30 min followed by LPA stimulation for 16 h; beta-arrestin/TEV beta-lactamase reporter FRET; functional antagonism IC50. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `C[C](OC(=O)Nc1c(-c2ccc(N(C)S(C)(=O)=O)cc2)nnn1C)c1ccccc1Cl` |
| M002 | C02 | `CC(C)(C)OC(=O)N1CCC(COc2ccc(C3=CCC(C(=O)NCC(F)F)CC3)cc2)CC1` |
| M003 | C03 | `O=C(c1ccc(F)c(Cl)c1)N1CCC(F)(CNCCOc2cccc(F)n2)CC1` |
| M004 | C01 | `C[C](OC(=O)Nc1c(-c2ccc(NC(=O)[C]3CC3(F)F)cn2)nnn1C)c1cc(F)cnc1F` |
| M005 | C03 | `O=C(c1ccc(F)c(Cl)c1)N1CCC(F)(CNCCOc2cccc(N3CCCC3)n2)CC1` |
| M006 | C02 | `CCc1cnc(N2CCC(COc3ccc(C4=CCC(C(=O)N5CCC(F)(F)C5)CC4)cc3)CC2)nc1` |
| M007 | C01 | `C[C](OC(=O)Nc1c(-c2ccc(NS(C)(=O)=O)c(C)n2)nnn1C)c1ccccc1Cl` |
| M008 | C02 | `CCc1cnc(N2CCC(COc3ccc(C4=CCC(C(=O)N5CCOCC5)CC4)cc3)CC2)nc1` |
| M009 | C01 | `C[C](OC(=O)Nc1c(-c2ccc(NS(C)(=O)=O)cn2)nnn1C)c1cc(F)cnc1F` |
| M010 | C01 | `CNS(=O)(=O)c1ccc(-c2nnn(C)c2NC(=O)O[C](C)c2ccccc2Cl)cc1` |
| M011 | C04 | `Cc1ccc(NC(=O)C2(c3ccncc3C(C)C)CN(S(N)(=O)=O)C2)c(OC(F)F)n1` |
| M012 | C03 | `O=C(c1ccc(F)c(Cl)c1)N1CCC(F)(CNCCOc2cccc(-n3cccn3)n2)CC1` |
| M013 | C01 | `C[C](OC(=O)Nc1c(-c2ccc(NS(C)(=O)=O)c(C)n2)nnn1C)c1ccccc1` |
| M014 | C02 | `CN(CCO)C(=O)C1CC=C(c2ccc(OCC3CCN(C(=O)OC(C)(C)C)CC3)cc2)CC1` |
| M015 | C03 | `O=C(c1ccc(F)c(Cl)c1)N1CCC(F)(CNCCOc2ccccn2)CC1` |
| M016 | C04 | `COc1cc(C)ccc1NC(=O)C1(c2ccccc2C(C)C)CCN(C(=O)CCC(=O)O)CC1` |
| M017 | C02 | `CC(C)(C)OC(=O)N1CCC(COc2ccc(C3=CCC(C(=O)NCCO)CC3)cc2)CC1` |
| M018 | C01 | `C[C](OC(=O)Nc1c(-c2ccc(NC(=O)C34CC(C#N)(C3)C4)cn2)nnn1C)c1cc(F)cnc1F` |
| M019 | C04 | `Cc1ccc(NC(=O)C2(c3cccnc3C(C)C)CCNCC2)c(OC(F)F)n1` |
| M020 | C02 | `CCc1cnc(N2CCC(COc3ccc(C4=CCC(C(=O)N5CCC5)CC4)cc3)CC2)nc1` |
| M021 | C04 | `Cc1ccc(NC(=O)C2(c3ncccc3C(C)C)CN(S(N)(=O)=O)C2)c(OC(F)F)n1` |
| M022 | C01 | `C[C](OC(=O)Nc1c(-c2ccc(NS(C)(=O)=O)cn2)nnn1C)c1ccccc1Cl` |
| M023 | C03 | `O=C(c1ccc(F)c(Cl)c1)N1CCC(F)(CNCCOc2cccc(Cl)n2)CC1` |
| M024 | C01 | `C[C](OC(=O)Nc1c(-c2ccc(NS(C)(=O)=O)c(C)n2)nnn1C)c1cccnc1Cl` |
| M025 | C04 | `COc1cc(C)ncc1NC(=O)C1(c2ccccc2C(C)C)CNC1` |
| M026 | C03 | `CC(=O)Nc1cccc(OCCNCC2(F)CCN(C(=O)c3ccc(F)c(Cl)c3)CC2)n1` |
| M027 | C04 | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(CCCC(=O)O)C2)c(OC(F)F)n1.N` |
| M028 | C03 | `O=C(c1ccc(F)c(Cl)c1)N1CCC(F)(CNCCOc2cc(C(F)(F)F)ccn2)CC1` |
| M029 | C01 | `C[C](OC(=O)Nc1c(-c2ccc(NC(=O)C34CC(F)(C3)C4)cn2)nnn1C)c1cc(F)cnc1F` |
| M030 | C02 | `CC(C)(C)OC(=O)N1CCC(COc2ccc(C3=CCC(C(=O)N4CCOCC4)CC3)cc2)CC1` |
| M031 | C04 | `COc1cc(Cl)ncc1NC(=O)C1(c2ncccc2C(C)C)CN(S(N)(=O)=O)C1` |
| M032 | C04 | `COc1cc(Cl)ncc1NC(=O)C1(c2ccccc2C(C)C)CN(S(N)(=O)=O)C1` |
| M033 | C02 | `CCc1cnc(N2CCC(COc3ccc(C4=CCC(C(=O)N5CCC[C@@H]5CO)CC4)cc3)CC2)nc1` |
| M034 | C02 | `CCc1cnc(N2CCC(COc3ccc(C4=CCC(C(=O)N5CCC[C@H]5CO)CC4)cc3)CC2)nc1` |
| M035 | C02 | `CCc1cnc(N2CCC(COc3ccc(C4=CCC(C(=O)N5CC[C@H](CO)C5)CC4)cc3)CC2)nc1` |
| M036 | C02 | `CCc1cnc(N2CCC(COc3ccc(C4=CCC(C(=O)N5CC[C@@H](CO)C5)CC4)cc3)CC2)nc1` |
| M037 | C01 | `C[C](OC(=O)Nc1c(-c2ccc(NC(=O)c3ccc(C(F)(F)F)nc3)cn2)nnn1C)c1cc(F)cnc1F` |
| M038 | C01 | `C[C](OC(=O)Nc1c(-c2ccc(NC(=O)c3ccc(C)nc3)cn2)nnn1C)c1cc(F)cnc1F` |
| M039 | C02 | `CCc1cnc(N2CCC(COc3ccc(C4=CCC(C(=O)N5CC[C@H](O)C5)CC4)cc3)CC2)nc1` |
| M040 | C02 | `CCc1cnc(N2CCC(COc3ccc(C4=CCC(C(=O)N5CC[C@@H](O)C5)CC4)cc3)CC2)nc1` |
| M041 | C03 | `O=C(c1ccc(F)c(Cl)c1)N1CCC(F)(CNCCOc2ccc(Cl)cn2)CC1` |
| M042 | C03 | `O=C(c1ccc(F)c(Cl)c1)N1CCC(F)(CNCCOc2ccc(F)cn2)CC1` |
| M043 | C03 | `O=C(c1ccc(F)c(Cl)c1)N1CCC(F)(CNCCOc2cccc(C(F)(F)F)n2)CC1` |
| M044 | C03 | `COc1cccc(OCCNCC2(F)CCN(C(=O)c3ccc(F)c(Cl)c3)CC2)n1` |
| M045 | C03 | `Cc1cccc(OCCNCC2(F)CCN(C(=O)c3ccc(F)c(Cl)c3)CC2)n1` |
| M046 | C03 | `CNc1cccc(OCCNCC2(F)CCN(C(=O)c3ccc(F)c(Cl)c3)CC2)n1` |
| M047 | C04 | `CC(=O)NS(=O)(=O)CCC(=O)N1CC(C(=O)Nc2ccc(C)nc2OC(F)F)(c2ccccc2C(C)C)C1` |
| M048 | C04 | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(C(=O)CN3C(=O)CNC3=O)C2)c(OC(F)F)n1` |
| M049 | C04 | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(C(=O)CC3(C(=O)O)CCC3)C2)c(OC(F)F)n1` |
| M050 | C04 | `Cc1ccc(NC(=O)C2(c3ccccc3C(C)C)CN(C(=O)Cc3c[nH]nc3O)C2)c(OC(F)F)n1` |

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
