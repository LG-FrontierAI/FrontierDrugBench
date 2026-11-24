---
bench_id: "SM-075-Molecular-Biology-ADMET-Classification"
category: "Molecular-Biology"
format: "structured_json"
---
# Prompt

Predict human CES1-mediated activation of ester prodrugs, measured as formation of released indomethacin. There are 44 distinct molecules. Total: 100 points.

V denotes indomethacin formation rate in nmol/min/mg of the stated enzyme-preparation or lysate protein. Protein normalization refers to the preparation, not purified CES mass. Evaluate the reported central rate under each molecule's context. Low, intermediate and high release are assay categories; the desired activation rate depends on the intended delivery strategy.

## Prediction approach

Use your internal medicinal-chemistry and chemical-biology knowledge together with the information explicitly provided in this prompt and the optional FASTA reference `CES1_HUMAN_P23141_full_length.fasta`. Do not search or retrieve the original papers or other source literature. Infer CES1/CES2 hydrolysis trends from the molecular structures, prodrug design, the reference sequence if useful, and the stated assay context.

## Reference protein sequences

Reference FASTA files are provided as `CES1_HUMAN_P23141_full_length.fasta`. They contain the canonical human CES1 UniProt sequence and may be consulted if useful. The sequence is auxiliary reference information; use the molecule structures and stated assay context as the prediction inputs. The commercial hCES1b preparation may not be identical to a particular splice isoform.

Target FASTA (`CES1_HUMAN_P23141_full_length.fasta`):

>CES1_HUMAN|P23141|full_length|UniProt_reference
MWLRAFILATLSASAAWGHPSSPPVVDTVHGKVLGKFVSLEGFAQPVAIFLGIPFAKPPLGPLRFTPPQPAEPWSFVKNA
TSYPPMCTQDPKAGQLLSELFTNRKENIPLKLSEDCLYLNIYTPADLTKKNRLPVMVWIHGGGLMVGAASTYDGLALAAH
ENVVVVTIQYRLGIWGFFSTGDEHSRGNWGHLDQVAALRWVQDNIASFGGNPGSVTIFGESAGGESVSVLVLSPLAKNLF
HRAISESGVALTSVLVKKGDVKPLAEQIAITAGCKTTTSAVMVHCLRQKTEEELLETTLKMKFLSLDLQGDPRESQPLLG
TVIDGMLLLKTPEELQAERNFHTVPYMVGINKQEFGWLIPMQLMSYPLSEGQLDQKTAMSLLWKSYPLVCIAKELIPEAT
EKYLGGTDDTVKKKDLFLDLIADVMFGVPSVIVARNHRDAGAPTYMYEFQYRPSFSSDMKPKTVIGDHGDELFSVFGAPF
LKEGASEEEIRLSKMVMKFWANFARNGNPNGEGLPHWPEYNQKEGYLQIGANTQAAQKLKDKEVAFWTNLFAKKAVEKPP
QTEHIEL


## Assay contexts

| Context | Conditions |
|---|---|
| C01 | Commercial human hCES1b preparations. Substrate 100 uM; preparation protein 0.25 mg/mL; 100 mM HEPES pH 7.4; 1% DMSO; 37 C; 30 min. HPLC quantification of released indomethacin. |
| C02 | Human CES1A1 expressed in HEK293 cells; ex-vivo cell lysates. Substrate 50 uM; lysate protein 0.05 mg/mL; 100 mM HEPES; 1% DMSO; 37 C; reported incubation range 30-120 min, compound-specific durations unspecified. HPLC quantification of released indomethacin. Reaction-buffer pH unspecified. |
| C03 | Human CES1A1 expressed in HEK293 cells; ex-vivo cell lysates. Substrate 250 uM; lysate protein 0.25 mg/mL; 100 mM HEPES; 1% DMSO; 37 C; 60 min. HPLC quantification of released indomethacin. Reaction-buffer pH unspecified. |

## Molecules

| Molecule ID | Context | Endpoint | SMILES |
|---|---|---|---|
| M001 | C01 | V | `COc1ccc2c(c1)c(CC(=O)Oc1ccc(F)cc1)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M002 | C01 | V | `COc1ccc2c(c1)c(CC(=O)OCCCC(C)C)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M003 | C02 | V | `C=CCOC(=O)OC(C)OC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |
| M004 | C01 | V | `COc1ccc2c(c1)c(CC(=O)Oc1cccc(Br)c1)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M005 | C02 | V | `COc1ccc2c(c1)c(CC(=O)OC(C)OC(=O)N(C)C)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M006 | C01 | V | `COc1ccc(OC(=O)Cc2c(C)n(C(=O)c3ccc(Cl)cc3)c3ccc(OC)cc23)cc1` |
| M007 | C01 | V | `COc1ccc2c(c1)c(CC(=O)OC(C)OC(=O)OC(C)C)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M008 | C01 | V | `COc1ccc2c(c1)c(CC(=O)Oc1ccccc1C(C)=O)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M009 | C01 | V | `COc1ccc2c(c1)c(CC(=O)Oc1cccc(C(C)=O)c1)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M010 | C02 | V | `CCC(=O)OCOC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |
| M011 | C01 | V | `COc1cccc(OC(=O)Cc2c(C)n(C(=O)c3ccc(Cl)cc3)c3ccc(OC)cc23)c1` |
| M012 | C01 | V | `COc1ccc2c(c1)c(CC(=O)OC1OC(=O)c3ccccc31)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M013 | C01 | V | `COc1ccc2c(c1)c(CC(=O)Oc1ccccc1F)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M014 | C01 | V | `COc1ccc2c(c1)c(CC(=O)OC(C)OC(=O)OC1CCCCC1)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M015 | C02 | V | `COc1ccc2c(c1)c(CC(=O)OCOC(=O)C(C)C)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M016 | C03 | V | `COc1ccc2c(c1)c(CC(=O)OCOC(=O)CCC(C)C)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M017 | C02 | V | `COC(=O)OCOC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |
| M018 | C01 | V | `COc1ccc2c(c1)c(CC(=O)OCOC(=O)C(C)(C)C)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M019 | C01 | V | `COc1ccc2c(c1)c(CC(=O)OCc1oc(=O)oc1C)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M020 | C03 | V | `CCCCCC(=O)OCOC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |
| M021 | C01 | V | `CCOC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |
| M022 | C01 | V | `COc1ccc2c(c1)c(CC(=O)Oc1ccccc1Br)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M023 | C02 | V | `CCN(CC)C(=O)OC(C)OC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |
| M024 | C01 | V | `COc1ccc2c(c1)c(CC(=O)Oc1ccccc1)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M025 | C03 | V | `CCCC(C)C(=O)OCOC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |
| M026 | C03 | V | `CCC(C)CC(=O)OCOC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |
| M027 | C02 | V | `C=CCN(CC=C)C(=O)OC(C)OC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |
| M028 | C02 | V | `COc1ccc2c(c1)c(CC(=O)OCOC(=O)N1CCCC1)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M029 | C02 | V | `COc1ccc2c(c1)c(CC(=O)OC(C)OC(=O)OCC(C)C)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M030 | C02 | V | `COCCOC(=O)OC(C)OC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |
| M031 | C02 | V | `COC(=O)OC(C)OC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |
| M032 | C02 | V | `COc1ccc2c(c1)c(CC(=O)OC(C)OC(=O)OC(C)(C)C)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M033 | C02 | V | `CCN(CC)C(=O)OCOC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |
| M034 | C02 | V | `COc1ccc2c(c1)c(CC(=O)OCOC(=O)N(C)C)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M035 | C01 | V | `CCCCCOC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |
| M036 | C01 | V | `CCC(C)CCOC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |
| M037 | C01 | V | `COc1ccc2c(c1)c(CC(=O)Oc1ccccc1OC)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M038 | C01 | V | `COc1ccc2c(c1)c(CC(=O)Oc1cccc(F)c1)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M039 | C01 | V | `COc1ccc2c(c1)c(CC(=O)Oc1ccc(Br)cc1)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M040 | C01 | V | `COc1ccc2c(c1)c(CC(=O)Oc1ccc(C(C)=O)cc1)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M041 | C03 | V | `CCCCCCCCCC(=O)OCOC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |
| M042 | C03 | V | `CCCC(=O)OCOC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |
| M043 | C03 | V | `COc1ccc2c(c1)c(CC(=O)OCOC(C)=O)c(C)n2C(=O)c1ccc(Cl)cc1` |
| M044 | C03 | V | `CCCCCCCC(=O)OCOC(=O)Cc1c(C)n(C(=O)c2ccc(Cl)cc2)c2ccc(OC)cc12` |

## 1. Interval prediction

| Label | Parent-drug formation rate V (nmol/min/mg preparation protein) |
|---|---|
| L | < 1 |
| M | 1 to < 3 |
| H | >= 3 |

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

A: left/right formation-rate ratio > 3 (left releases parent drug faster); B: 1/3 <= left/right <= 3; C: left/right < 1/3 (left releases parent drug slower).

Each correct item earns 6 points. Each pair shares one assay context. "Similar" denotes the stated numerical category for the reported central results.

| Item | Left molecule | Right molecule |
|---|---|---|
| Q025 | M025 | M026 |
| Q026 | M027 | M028 |
| Q027 | M029 | M030 |
| Q028 | M031 | M032 |
| Q029 | M033 | M034 |
| Q030 | M035 | M036 |

## 3. Within-series ordering

Order each group from highest to lowest indomethacin formation rate. Each group is one chemical series measured in one assay context. Use each molecule exactly once.

Each group is worth 8 points, multiplied by max(0, Spearman rho) between the submitted and reference order.

| Item | Molecules to order |
|---|---|
| Q031 | M037, M038, M039, M040 |
| Q032 | M041, M042, M043, M044 |

## Response format and scoring

Return ONLY one strict JSON object mapping each listed Q identifier to its response: L/M/H for interval items, A/B/C for comparisons, and an ordered array of molecule IDs for ordering items.

Syntax example only; the values do not imply answers:

`{"Q001": "L", "Q025": "B", "Q031": ["M037", "M038", "M039", "M040"]}`

Missing or invalid items earn zero. An ordering array must contain every listed molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0–1 scale.
