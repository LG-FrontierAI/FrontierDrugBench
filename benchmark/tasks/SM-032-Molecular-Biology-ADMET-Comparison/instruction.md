---
bench_id: "SM-032-Molecular-Biology-ADMET-Comparison"
category: "Molecular-Biology"
format: "structured_json"
---

# Prompt

Predict experimental human liver microsomal (HLM) metabolic stability from the supplied molecular structures. Total: 100 points.
Structures are listed in each question. The same molecule ID always denotes the same structure.
Use the supplied assay context; unreported conditions remain unspecified.
All required inputs are included in this Markdown; inputs/ contains no additional material.
Lower total HLM intrinsic clearance (CLint, μL/min/mg) means greater stability.

Relative comparisons are confined to each original candidate group. Do not compare molecules across groups with different assays.

- Top2: an array of exactly two distinct candidate IDs; each correct selection earns half the question points. Order does not matter.
- Pair: one candidate ID string; a correct choice earns the question points.
- Ranking: an array containing every candidate ID exactly once in the stated direction; the score is the fraction of correct scored pairwise relations.

Question allocations preserve their original relative weights; any fractional point allocations below are exact.

Return ONLY one strict JSON object keyed by the question IDs below. Do not include Markdown fences or explanations.
Unanswered questions or molecules may be omitted or set to null and earn zero. Arrays must contain distinct, valid options.
Unknown question IDs or duplicate JSON keys invalidate the entire response. Unknown molecule IDs in a binning/profile object
make that question score zero; other invalid answers lose only the affected question or molecule points.
The scoring interface returns total points divided by 100, a number from 0 to 1.

## HLM-TOP201 (25/2 points)

Select the TWO most stable molecules (lowest total HLM CLint).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M011 | `Cn1cc(-c2ccnc3[nH]c(-c4ccc(CN5CCOCC5)cc4)cc23)cn1` |
| M012 | `Cn1cc(-c2ccnc3[nH]c(-c4ccc(CN5CCCC5)cc4)cc23)cn1` |
| M013 | `Cn1cc(-c2ccnc3[nH]c(-c4ccc(CN5CCCCC5)cc4)cc23)cn1` |
| M014 | `CCNCc1ccc(-c2cc3c(-c4cnn(C)c4)ccnc3[nH]2)cc1` |
| M015 | `Cn1cc(-c2ccnc3[nH]c(-c4ccc(CNCC(F)F)cc4)cc23)cn1` |

Assay context (all candidates): Human liver microsomes; total CLint (μL/min/mg).

## HLM-TOP202 (25/2 points)

Select the TWO most stable molecules (lowest total HLM CLint).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M016 | `O=c1c(NCc2ncccn2)c(-c2ccc(N3CCOCC3)cc2)c1=O` |
| M017 | `O=c1c(NCc2nccs2)c(-c2ccc(N3CCOCC3)cc2)c1=O` |
| M018 | `Cc1cccc(CNc2c(-c3ccc(N4CCOCC4)cc3)c(=O)c2=O)n1` |
| M019 | `O=c1c(NCCN2CCCC2)c(-c2ccc(N3CCOCC3)cc2)c1=O` |
| M020 | `O=c1c(NCc2cccnc2)c(-c2ccc(N3CCOCC3)cc2)c1=O` |

Assay context (all candidates): Human liver microsomes; total CLint (μL/min/mg).

## HLM-TOP203 (25/2 points)

Select the TWO most stable molecules (lowest total HLM CLint).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M021 | `COc1cc(NC(=O)Cn2ccc3ccc(-c4nnc(C)o4)cc32)cc(OC)c1OC` |
| M022 | `COc1cc(NC(=O)Cn2cc(Cl)c3ccc(-c4cnn(C)c4)cc32)cc(OC)c1OC` |
| M023 | `COc1cc(NC(=O)Cn2ccc3cc(F)c(-c4cnn(C)c4)cc32)cc(OC)c1OC` |
| M024 | `COc1cc(NC(=O)Cn2ccc3ccc(-c4cnn(C)c4)cc32)cc(OC)c1OC` |
| M025 | `COc1cc(NC(=O)Cn2ccc3ccc(-c4cn(C)nc4C)cc32)cc(OC)c1OC` |

Assay context (all candidates): Human liver microsomes; total CLint (μL/min/mg).

## HLM-PAIR01 (5 points)

Select the more stable molecule (lower total HLM CLint).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M026 | `O=C(O)c1ccc2c(c1)nc(NCCOCCCCNCc1ccc(OC(F)(F)F)c(Cl)c1)c1ccncc12` |
| M027 | `NC(=O)c1ccc2c(c1)nc(NCCOCCCCNCc1ccc(OC(F)(F)F)c(Cl)c1)c1ccncc12` |

Assay context (all candidates): Human liver microsomes; total CLint (μL/min/mg).

## HLM-PAIR02 (5 points)

Select the more stable molecule (lower total HLM CLint).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M028 | `Cn1cc(-c2ccc3c(Cl)cn(CC(=O)Nc4ccccc4Cl)c3c2)cn1` |
| M029 | `Cn1cc(-c2ccc3ccn(CC(=O)Nc4ccccc4Cl)c3c2)cn1` |

Assay context (all candidates): Human liver microsomes; total CLint (μL/min/mg).

## HLM-PAIR03 (5 points)

Select the more stable molecule (lower total HLM CLint).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M030 | `O=c1c(NCc2cccc(F)n2)c(-c2ccc(N3CCC(F)(F)CC3)cc2)c1=O` |
| M031 | `O=c1c(NCc2cccc(F)n2)c(-c2ccc(N3CCC(F)CC3)cc2)c1=O` |

Assay context (all candidates): Human liver microsomes; total CLint (μL/min/mg).

## HLM-PAIR04 (5 points)

Select the more stable molecule (lower total HLM CLint).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M032 | `CN(C)Cc1ccc(-c2cc3c(-c4cn[nH]c4)ccnc3[nH]2)cc1` |
| M033 | `CN(C)Cc1ccc(-c2cc3c(-c4ccccc4)ccnc3[nH]2)cc1` |

Assay context (all candidates): Human liver microsomes; total CLint (μL/min/mg).

## HLM-PAIR05 (5 points)

Select the more stable molecule (lower total HLM CLint).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M034 | `COc1ncc(-c2ccn3c(-c4cc(OC)c(C(=O)NCC(F)(F)F)c(OC)c4)cnc3c2)c(OC)n1` |
| M035 | `COc1ncc(-c2ccn3c(-c4cc(OC)c(C(=O)N5CC(F)(F)C5)c(OC)c4)cnc3c2)c(OC)n1` |

Assay context (all candidates): Human liver microsomes; total CLint (μL/min/mg).

## HLM-RANK01 (25/2 points)

Rank all molecules from most to least stable (total HLM CLint from lowest to highest).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M036 | `CC(C)NCc1ccc(-c2cc3c(-c4cnn(C5CCOCC5)c4)ccnc3[nH]2)cc1` |
| M037 | `CC(c1ccc(-c2cc3c(-c4cnn(C)c4)ccnc3[nH]2)cc1)N1CCCC1` |
| M038 | `CC(=O)Nc1ccc(-c2cc3c(-c4cnn(C)c4)ccnc3[nH]2)cc1` |
| M039 | `Cc1cc(-c2ccnc3[nH]c(-c4ccc(CNC(C)C)cc4)cc23)ccn1` |
| M040 | `Cn1cc(-c2ccnc3[nH]c(-c4ccc(O)cc4)cc23)cn1` |

Assay context (all candidates): Human liver microsomes; total CLint (μL/min/mg).

## HLM-RANK02 (25/2 points)

Rank all molecules from most to least stable (total HLM CLint from lowest to highest).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M041 | `C[C@H]1COCCN1c1ccc(-c2c(NCc3ccccn3)c(=O)c2=O)cc1` |
| M042 | `C[C@@H]1COCCN1c1ccc(-c2c(NCc3ccccn3)c(=O)c2=O)cc1` |
| M043 | `COC1CCN(c2ccc(-c3c(NCc4ccccn4)c(=O)c3=O)cc2)CC1` |
| M044 | `O=c1c(NCc2ccccn2)c(-c2ccc(N3CCC(F)CC3)cc2)c1=O` |
| M045 | `Cc1cc(-c2c(NCc3ccccn3)c(=O)c2=O)ccc1N1CCOCC1` |

Assay context (all candidates): Human liver microsomes; total CLint (μL/min/mg).

## HLM-RANK03 (25/2 points)

Rank all molecules from most to least stable (total HLM CLint from lowest to highest).

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M046 | `COc1cc(-c2cnc3cc(-c4cccc(NC(C)=O)c4)ccn23)cc(OC)c1C(=O)N1CC(F)(F)C1` |
| M047 | `COc1cc(-c2cnc3cc(-c4ccc(N5CCN(C)CC5)cc4)ccn23)cc(OC)c1C(=O)N1CC(F)(F)C1` |
| M048 | `COc1cc(-c2ccn3c(-c4cc(OC)c(C(=O)N5CC(F)(F)C5)c(OC)c4)cnc3c2)cc(OC)c1OC` |
| M049 | `COc1ccc(-c2ccn3c(-c4cc(OC)c(C(=O)N5CC(F)(F)C5)c(OC)c4)cnc3c2)c(OC)c1OC` |
| M050 | `COc1cc(-c2cnc3cc(-c4cnn(C)c4C)ccn23)cc(OC)c1C(=O)N1CC(F)(F)C1` |

Assay context (all candidates): Human liver microsomes; total CLint (μL/min/mg).
