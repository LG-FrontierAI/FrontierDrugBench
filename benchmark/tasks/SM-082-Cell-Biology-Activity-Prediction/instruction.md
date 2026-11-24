---
bench_id: "SM-082-Cell-Biology-Activity-Prediction"
category: "Cell-Biology"
format: "structured_json"
---
# Prompt

Predict intact-cell NanoBRET target-engagement concentration potency for CSNK2A2, MST2, ENL YEATS and EPHA2. There are 50 distinct molecules. Total: 100 points.

Use the intact-cell assay with its stated tracer concentration. Original one-decimal pIC50 results are converted to concentration for a common response format.

Use each molecule's assay context. In the tables below, P denotes its stated IC50, EC50, DC50, qAC50 or CD, expressed in nM. Lower P means greater concentration potency.

## Reference protein sequences

Reference FASTA files for CSNK2A2, MST2, ENL and EPHA2 are provided as `CSNK2A2_HUMAN_P19784_full_length.fasta`, `MST2_STK3_HUMAN_Q13188_full_length.fasta`, `ENL_HUMAN_Q03111_YEATS_1-148.fasta`, `ENL_HUMAN_Q03111_full_length.fasta` and `EPHA2_HUMAN_P29317_full_length.fasta`. They may be consulted if useful. The ENL assay uses the YEATS fragment comprising residues 1–148; both the full-length ENL reference and a derived 1–148 FASTA are provided. NanoLuc and other reporter/tracer components are not included in the target FASTA files.

Target FASTA (`CSNK2A2_HUMAN_P19784_full_length.fasta`):

>CSNK2A2_HUMAN|P19784|full_length|UniProt_reference
MPGPAAGSRARVYAEVNSLRSREYWDYEAHVPSWGNQDDYQLVRKLGRGKYSEVFEAINITNNERVVVKILKPVKKKKIK
REVKILENLRGGTNIIKLIDTVKDPVSKTPALVFEYINNTDFKQLYQILTDFDIRFYMYELLKALDYCHSKGIMHRDVKP
HNVMIDHQQKKLRLIDWGLAEFYHPAQEYNVRVASRYFKGPELLVDYQMYDYSLDMWSLGCMLASMIFRREPFFHGQDNY
DQLVRIAKVLGTEELYGYLKKYHIDLDPHFNDILGQHSRKRWENFIHSENRHLVSPEALDLLDKLLRYDHQQRLTAKEAM
EHPYFYPVVKEQSQPCADNAVLSSGLTAAR

Target FASTA (`MST2_STK3_HUMAN_Q13188_full_length.fasta`):

>STK3_HUMAN|Q13188|full_length|UniProt_reference
MEQPPAPKSKLKKLSEDSLTKQPEEVFDVLEKLGEGSYGSVFKAIHKESGQVVAIKQVPVESDLQEIIKEISIMQQCDSP
YVVKYYGSYFKNTDLWIVMEYCGAGSVSDIIRLRNKTLIEDEIATILKSTLKGLEYLHFMRKIHRDIKAGNILLNTEGHA
KLADFGVAGQLTDTMAKRNTVIGTPFWMAPEVIQEIGYNCVADIWSLGITSIEMAEGKPPYADIHPMRAIFMIPTNPPPT
FRKPELWSDDFTDFVKKCLVKNPEQRATATQLLQHPFIKNAKPVSILRDLITEAMEIKAKRHEEQQRELEEEEENSDEDE
LDSHTMVKTSVESVGTMRATSTMSEGAQTMIEHNSTMLESDLGTMVINSEDEEEEDGTMKRNATSPQVQRPSFMDYFDKQ
DFKNKSHENCNQNMHEPFPMSKNVFPDNWKVPQDGDFDFLKNLSLEELQMRLKALDPMMEREIEELRQRYTAKRQPILDA
MDAKKRRQQNF

Target FASTA (`ENL_HUMAN_Q03111_YEATS_1-148.fasta`):

>ENL_HUMAN|Q03111|residues_1-148|assay_domain_reference
MDNQCTVQVRLELGHRAQLRKKPTTEGFTHDWMVFVRGPEQCDIQHFVEKVVFWLHDSFPKPRRVCKEPPYKVEESGYAG
FIMPIEVHFKNKEEPRKVCFTYDLFLNLEGNPPVNHLRCEKLTFNNPTTEFRYKLLRAGGVMVMPEGA

Target FASTA (`ENL_HUMAN_Q03111_full_length.fasta`):

>ENL_HUMAN|Q03111|full_length|UniProt_reference
MDNQCTVQVRLELGHRAQLRKKPTTEGFTHDWMVFVRGPEQCDIQHFVEKVVFWLHDSFPKPRRVCKEPPYKVEESGYAG
FIMPIEVHFKNKEEPRKVCFTYDLFLNLEGNPPVNHLRCEKLTFNNPTTEFRYKLLRAGGVMVMPEGADTVSRPSPDYPM
LPTIPLSAFSDPKKTKPSHGSKDANKESSKTSKPHKVTKEHRERPRKDSESKSSSKELEREQAKSSKDTSRKLGEGRLPK
EEKAPPPKAAFKEPKMALKETKLESTSPKGGPPPPPPPPPRASSKRPATADSPKPSAKKQKKSSSKGSRSAPGTSPRTSS
SSSFSDKKPAKDKSSTRGEKVKAESEPREAKKALEVEESNSEDEASFKSESAQSSPSNSSSSSDSSSDSDFEPSQNHSQG
PLRSMVEDLQSEESDEDDSSSGEEAAGKTNPGRDSRLSFSDSESDNSADSSLPSREPPPPQKPPPPNSKVSGRRSPESCS
KPEKILKKGTYDKAYTDELVELHRRLMALRERNVLQQIVNLIEETGHFNVTNTTFDFDLFSLDETTVRKLQSCLEAVAT

Target FASTA (`EPHA2_HUMAN_P29317_full_length.fasta`):

>EPHA2_HUMAN|P29317|full_length|UniProt_reference
MELQAARACFALLWGCALAAAAAAQGKEVVLLDFAAAGGELGWLTHPYGKGWDLMQNIMNDMPIYMYSVCNVMSGDQDNW
LRTNWVYRGEAERIFIELKFTVRDCNSFPGGASSCKETFNLYYAESDLDYGTNFQKRLFTKIDTIAPDEITVSSDFEARH
VKLNVEERSVGPLTRKGFYLAFQDIGACVALLSVRVYYKKCPELLQGLAHFPETIAGSDAPSLATVAGTCVDHAVVPPGG
EEPRMHCAVDGEWLVPIGQCLCQAGYEKVEDACQACSPGFFKFEASESPCLECPEHTLPSPEGATSCECEEGFFRAPQDP
ASMPCTRPPSAPHYLTAVGMGAKVELRWTPPQDSGGREDIVYSVTCEQCWPESGECGPCEASVRYSEPPHGLTRTSVTVS
DLEPHMNYTFTVEARNGVSGLVTSRSFRTASVSINQTEPPKVRLEGRSTTSLSVSWSIPPPQQSRVWKYEVTYRKKGDSN
SYNVRRTEGFSVTLDDLAPDTTYLVQVQALTQEGQGAGSKVHEFQTLSPEGSGNLAVIGGVAVGVVLLLVLAGVGFFIHR
RRKNQRARQSPEDVYFSKSEQLKPLKTYVDPHTYEDPNQAVLKFTTEIHPSCVTRQKVIGAGEFGEVYKGMLKTSSGKKE
VPVAIKTLKAGYTEKQRVDFLGEAGIMGQFSHHNIIRLEGVISKYKPMMIITEYMENGALDKFLREKDGEFSVLQLVGML
RGIAAGMKYLANMNYVHRDLAARNILVNSNLVCKVSDFGLSRVLEDDPEATYTTSGGKIPIRWTAPEAISYRKFTSASDV
WSFGIVMWEVMTYGERPYWELSNHEVMKAINDGFRLPTPMDCPSAIYQLMMQCWQQERARRPKFADIVSILDKLIRAPDS
LKTLADFDPRVSIRLPSTSGSEGVPFRTVSEWLESIKMQQYTEHFMAAGYTAIEKVVQMTNDDIKRIGVRLPGHQKRIAY
SLLGLKDQVNTVGIPI


## Assay contexts

| Context | Conditions and endpoint |
|---|---|
| C01 | HEK293 cells expressing ENL YEATS residues 1-148; 2 h compound incubation with fluorescent tracer; intact-cell NanoBRET IC50. The inputs include the full-length ENL reference and a derived residues 1–148 reference. |
| C02 | HEK293T cells expressing MST2-NanoLuc; intact-cell NanoBRET EC50. The published database assay description reports 20 h incubation; it does not clearly separate expression time from compound-equilibration time. |
| C03 | Intact HEK293 cells expressing human CSNK2A2-NanoLuc; 2 h compound/tracer equilibration at 37 C; NanoBRET tracer K10, 0.25 uM; cellular IC50. |
| C04 | HEK293T cells expressing full-length EPHA2-NanoLuc; 2 h compound/tracer incubation; tracer K4; intact-cell NanoBRET EC50. Receptor species is not resolved in the source database description. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `O=C(Nc1cc2[nH]c(CN3CCC3C3CC3)cc2cn1)c1ccc2nncn2c1` |
| M002 | C01 | `O=C(NCc1ccc(CN2CCC2)cc1)c1ccc2nncn2c1` |
| M003 | C02 | `Cc1cccc(-c2ccc(-c3cc4cnc(NC(CO)CO)nc4n(CCCCN)c3=O)c(Cl)c2)n1` |
| M004 | C01 | `CC(C)C1CCN1Cc1ccc(CNC(=O)c2ccc3nncn3c2)cc1` |
| M005 | C01 | `C[C@H]1CCCN1Cc1cc2cnc(NC(=O)c3ccc4nncn4c3)cc2[nH]1` |
| M006 | C03 | `N#Cc1cnn2c(NC3CC3)cc(Nc3cc(-n4cnnc4)c(N4CC[C@H](N)C4)cc3F)nc12` |
| M007 | C04 | `COc1c(F)ccc(-c2cnc3nc2NCCCNS(=O)(=O)c2cccc(c2)N3)c1F` |
| M008 | C02 | `Cc1cccc(-c2ccc(-c3cc4cnc(Nc5ccc(F)c(CO)c5)nc4n(CCCCN)c3=O)c(Cl)c2)n1` |
| M009 | C01 | `CC(C)C1CCN1Cc1cc2cnc(NC(=O)c3ccc4nncn4c3)cc2[nH]1` |
| M010 | C04 | `O=S1(=O)NCCCNc2nc(ncc2-c2ccc(Cl)c(Cl)c2)Nc2cccc1c2` |
| M011 | C04 | `COc1cc(-c2cnc3nc2NCCCNS(=O)(=O)c2cccc(c2)N3)ccc1Br` |
| M012 | C01 | `CC(C)(C)C1CCN1Cc1ccc(CNC(=O)c2ccc3nncn3c2)cc1` |
| M013 | C04 | `COc1cc(-c2cnc3nc2NCCCNS(=O)(=O)c2cccc(c2)N3)ccc1F` |
| M014 | C01 | `CN(C)Cc1ccc(CNC(=O)c2ccc3nncn3c2)cc1` |
| M015 | C03 | `Cn1cnc(Nc2cc(Nc3cccc(-n4cnnc4)c3)nc3c(C#N)cnn23)c1` |
| M016 | C04 | `O=S1(=O)NCCCNc2nc(ncc2Br)Nc2cccc1c2` |
| M017 | C04 | `COCCOc1ccc2cc1S(=O)(=O)NCCCNc1nc(ncc1-c1ccc(F)c(OC)c1)N2` |
| M018 | C01 | `O=C(NCc1ccc(CNc2ncc(F)cn2)cc1)c1ccc2nncn2c1` |
| M019 | C04 | `COc1cc(-c2cnc3nc2NCCCNS(=O)(=O)c2cccc(c2)N3)c(F)cc1F` |
| M020 | C02 | `CNc1ncc2cc(-c3ccc(-c4cccc(C)n4)cc3Cl)c(=O)n(CCCCO)c2n1` |
| M021 | C01 | `O=C(NCc1ccc(CN2CCCCC2)cc1)c1ccc2nncn2c1` |
| M022 | C04 | `COc1cc(-c2cnc3nc2NCCCNS(=O)(=O)c2cc(ccc2O)N3)ccc1F` |
| M023 | C03 | `N#Cc1cnn2c(NC3CC3)cc(Nc3cccc(C(=O)O)c3)nc12` |
| M024 | C02 | `Cc1cccc(-c2ccc(-c3cc4cnc(Nc5ccc(O)cc5)nc4n(CCCCN)c3=O)c(Cl)c2)n1` |
| M025 | C04 | `COc1cc(-c2cnc3nc2NCCCNS(=O)(=O)c2cccc(c2)N3)c(F)cc1Cl` |
| M026 | C04 | `COc1cc(-c2cnc3nc2NCCCNS(=O)(=O)c2cc(ccc2OC)N3)ccc1F` |
| M027 | C01 | `O=C(NCc1ccc(CN2CCOCC2)cc1)c1ccc2nncn2c1` |
| M028 | C04 | `O=C(Nc1ccccc1Cl)c1cnc2ccc(C3CCNCC3)cn12` |
| M029 | C01 | `O=C(NCc1cccc(CN2CCC2)c1)c1ccc2nncn2c1` |
| M030 | C02 | `Cc1cccc(-c2ccc(-c3cc4cnc(NCCCN5CCNCC5)nc4n(CCCCN)c3=O)c(Cl)c2)n1` |
| M031 | C03 | `Cl.N#Cc1cnn2c(Nc3cn(CCN4CCOCC4)cn3)cc(Nc3cccc(-n4cnnc4)c3)nc12` |
| M032 | C03 | `N#Cc1cnn2c(Nc3cn(CCN4CCCC4)cn3)cc(Nc3cccc(-n4cnnc4)c3)nc12` |
| M033 | C02 | `CNc1ncc2cc(-c3ccc(-c4cccc(C)n4)cc3Cl)c(=O)n(CCCCN)c2n1` |
| M034 | C02 | `CNc1ncc2cc(-c3ccc(-c4cccc(C)n4)cc3Cl)c(=O)n(CCCCCN)c2n1` |
| M035 | C01 | `CC(C)[C@@H]1CCN1Cc1cc2cnc(NC(=O)c3ccc4nncn4c3)cc2[nH]1` |
| M036 | C01 | `CC(C)[C@H]1CCN1Cc1cc2cnc(NC(=O)c3ccc4nncn4c3)cc2[nH]1` |
| M037 | C03 | `C[C@@H](N)CN(C)c1ccc(Nc2cc(NC3CC3)n3ncc(C#N)c3n2)cc1-n1cnnc1` |
| M038 | C03 | `C[C@H](N)CN(C)c1ccc(Nc2cc(NC3CC3)n3ncc(C#N)c3n2)cc1-n1cnnc1` |
| M039 | C03 | `CN[C@H]1CCCN(c2ccc(Nc3cc(NC4CC4)n4ncc(C#N)c4n3)cc2-n2cnnc2)C1` |
| M040 | C03 | `CN[C@@H]1CCCN(c2ccc(Nc3cc(NC4CC4)n4ncc(C#N)c4n3)cc2-n2cnnc2)C1` |
| M041 | C02 | `CNc1ncc2cc(-c3ccc(-c4cccc(C)n4)cc3Cl)c(=O)n(CCCCOC)c2n1` |
| M042 | C02 | `CNc1ncc2cc(-c3ccc(-c4cccc(C)n4)cc3Cl)c(=O)n(CCOC)c2n1` |
| M043 | C03 | `N#Cc1cnn2c(NC3CC3)cc(Nc3cccc(Cn4cnnc4)c3)nc12` |
| M044 | C03 | `CC(C)(O)Cc1cccc(Nc2cc(NC3CC3)n3ncc(C#N)c3n2)c1` |
| M045 | C03 | `CC(=O)Nc1cccc(Nc2cc(NC3CC3)n3ncc(C#N)c3n2)c1` |
| M046 | C03 | `CS(=O)(=O)Cc1cccc(Nc2cc(NC3CC3)n3ncc(C#N)c3n2)c1` |
| M047 | C02 | `CNc1ncc2cc(-c3ccc(-c4cccc(C)n4)cc3Cl)c(=O)n(CCCCCO)c2n1` |
| M048 | C02 | `Cc1cccc(-c2ccc(-c3cc4cnc(Nc5ccc(CCCO)cc5)nc4n(CCCCN)c3=O)c(Cl)c2)n1` |
| M049 | C02 | `CNc1ncc2cc(-c3ccc(-c4cccc(C)n4)cc3Cl)c(=O)n(CCCO)c2n1` |
| M050 | C02 | `CNc1ncc2cc(-c3ccc(-c4cccc(C)n4)cc3Cl)c(=O)n(CCCN)c2n1` |

## 1. Concentration intervals

| Label | P (nM) |
|---|---|
| L | < 100 |
| M | 100 to < 1000 |
| H | >= 1000 |

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
