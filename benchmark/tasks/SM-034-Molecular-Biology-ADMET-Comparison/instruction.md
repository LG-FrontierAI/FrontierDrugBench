---
bench_id: "SM-034-Molecular-Biology-ADMET-Comparison"
category: "Molecular-Biology"
format: "structured_json"
---

# Prompt

Predict relative experimental CYP inhibition within each specified isoform/probe group from the supplied molecular structures. Total: 100 points.
Structures are listed in each question. The same molecule ID always denotes the same structure.
Use the supplied assay context; unreported conditions remain unspecified.
All required inputs are included in this Markdown; inputs/ contains no additional material.
Higher CYP IC50 means weaker inhibition. Enzyme preparations, probes and preincubation conditions can differ between the listed assay contexts; retain those distinctions.

Relative comparisons are confined to each original candidate group. Do not compare molecules across groups with different assays.

- Top2: an array of exactly two distinct candidate IDs; each correct selection earns half the question points. Order does not matter.
- Pair: one candidate ID string; a correct choice earns the question points.

Question allocations preserve their original relative weights; any fractional point allocations below are exact.

Return ONLY one strict JSON object keyed by the question IDs below. Do not include Markdown fences or explanations.
Unanswered questions or molecules may be omitted or set to null and earn zero. Arrays must contain distinct, valid options.
Unknown question IDs or duplicate JSON keys invalidate the entire response. Unknown molecule IDs in a binning/profile object
make that question score zero; other invalid answers lose only the affected question or molecule points.
The scoring interface returns total points divided by 100, a number from 0 to 1.

## CYP-TOP201 (25 points)

Select the TWO weakest CYP inhibitors (highest IC50) for the specified isoform/probe.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M061 | `CC(=O)Nc1cc2cc(C(=O)NCCc3c(C)[nH]c4ccccc34)n(C)c2cn1` |
| M062 | `COCCOc1cc2cc(C(=O)NCCc3c(C)[nH]c4ccccc34)n(C)c2cn1` |
| M063 | `Cc1[nH]c2ccccc2c1CCNC(=O)c1cc2cc(N)ncc2n1C` |
| M064 | `Cc1[nH]c2ccccc2c1CCNC(=O)c1cc2ccncc2n1C` |
| M065 | `Cc1[nH]c2ccccc2c1CCNC(=O)c1cc2ccnc(C)c2n1C` |

Assay context (all candidates): Human CYP3A4; probe: midazolam.

## CYP-TOP202 (25 points)

Select the TWO weakest CYP inhibitors (highest IC50) for the specified isoform/probe.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M066 | `Cc1cc(-c2cc(Nc3ccn(C)n3)ncn2)ccc1CNC(=O)c1nc(C(C)(C)C)no1` |
| M067 | `Cc1c(CNC(=O)c2nc(C(C)(C)C)no2)ccc(-c2cc(Nc3ccn(C)n3)ncn2)c1F` |
| M068 | `Cn1ccc(Nc2cc(-c3ccc(CNC(=O)c4nc(C(C)(C)C)no4)c(Cl)c3)ncn2)n1` |
| M069 | `Cn1ccc(Nc2cc(-c3ccc(CNC(=O)c4nc(C(C)(C)C)no4)c(C(F)(F)F)c3)ncn2)n1` |
| M070 | `Cn1ccc(Nc2cc(-c3ccc(CNC(=O)c4nc(C(C)(C)C)no4)c(C4CC4)c3)ncn2)n1` |

Assay context (all candidates): Human CYP2C9; probe: not reported.

## CYP-PAIR01 (10 points)

Select the weaker CYP inhibitor (higher IC50) for the specified isoform/probe.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M071 | `CN(C[C@H]1Cc2c(cccc2N2C[C@@H]3CO[C@H]2C3)CN1)[C@H]1CCCc2cccnc21` |
| M072 | `CN(C[C@H]1Cc2c(cccc2N2CCOCC2=O)CN1)[C@H]1CCCc2cccnc21` |

Assay context (all candidates): Human CYP3A4; probe: fluorogenic probe unspecified.

## CYP-PAIR02 (10 points)

Select the weaker CYP inhibitor (higher IC50) for the specified isoform/probe.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M073 | `Cn1ccc(Nc2cc(-c3ccc(CNC(=O)c4nc(C(C)(C)C)no4)c(Cl)c3F)ncn2)n1` |
| M074 | `Cc1cc(-c2cc(Nc3ccn(C)n3)ncn2)c(F)cc1CNC(=O)c1nc(C(C)(C)C)no1` |

Assay context (all candidates): Human CYP2C9; probe: not reported.

## CYP-PAIR03 (10 points)

Select the weaker CYP inhibitor (higher IC50) for the specified isoform/probe.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M075 | `Cc1[nH]c2ccccc2c1CCNC(=O)c1cc2ccncc2[nH]1` |
| M076 | `Cc1cc2cc(C(=O)NCCc3c(C)[nH]c4ccccc34)[nH]c2cn1` |

Assay context (all candidates): Human CYP3A4; probe: midazolam.

## CYP-PAIR04 (10 points)

Select the weaker CYP inhibitor (higher IC50) for the specified isoform/probe.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M077 | `CNC(=O)C1CC=C(c2cc(NC(=O)c3ccc(F)cc3Cl)cnc2OC)CC1` |
| M078 | `CNC(=O)C1CC=C(c2cc(NC(=O)c3ccc(F)cc3Cl)ccc2OC)CC1` |

Assay context (all candidates): Human CYP2C19; probe: not reported.

## CYP-PAIR05 (10 points)

Select the weaker CYP inhibitor (higher IC50) for the specified isoform/probe.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M079 | `Nc1cc2c(c(F)n1)C(=O)N(CC1(O)CCC(F)(F)CC1)C2` |
| M080 | `Nc1cc2c(c(C(F)(F)F)n1)C(=O)N(CC1(O)CCC(F)(F)CC1)C2` |

Assay context (all candidates): Human CYP2C9; probe: not reported.
