---
bench_id: "SM-042-In-vivo-Study-ADMET-Ranking"
category: "In-vivo-Study"
format: "structured_json"
---

# Prompt

Predict experimental unbound brain/plasma partitioning (Kp,uu) from the supplied molecular structures. Total: 100 points.
Structures are listed in each question. The same molecule ID always denotes the same structure.
Use the supplied assay context; unreported conditions remain unspecified.
All required inputs are included in this Markdown; inputs/ contains no additional material.
Kp,uu is the unbound tissue/plasma ratio for the specified brain region and time basis. Use the stated species, route and sampling context. Brain and cerebellum, single-time-point and AUC measurements, and different species or dosing regimens must retain their stated distinctions.

Relative comparisons are confined to each listed candidate group. For each question return every candidate ID exactly once in an array ordered from highest to lowest Kp,uu. Each question is worth 50 points. Ranking points use equally weighted experimental pairwise relations separated by at least 1.5-fold; the order of closer values does not affect the score.

Return ONLY one strict JSON object keyed by the question IDs below. Do not include Markdown fences or explanations.
Unanswered questions or molecules may be omitted or set to null and earn zero. Arrays must contain distinct, valid options.
Unknown question IDs or duplicate JSON keys invalidate the entire response. Unknown molecule IDs in a binning object
make that question score zero; other invalid answers lose only the affected question or molecule points.
The scoring interface returns total points divided by 100, a number from 0 to 1.

## RANK-01 (50 points)

Rank all molecules from highest to lowest Kp,uu.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M071 | `Cc1cc2nc(C3CCOCC3)cn2cc1NC(=O)c1cccc(C(F)F)n1` |
| M072 | `COc1cc(NC(=O)c2cccc(C(F)(F)F)n2)cn2cc(C3CCOCC3)nc12` |
| M073 | `CCOc1cc2nc(C3CCOCC3)cn2cc1NC(=O)c1cccc(C(F)F)n1` |
| M074 | `Cc1cc(NC(=O)c2cccc(C(F)F)n2)cn2cc(C3CCOCC3)nc12` |
| M075 | `CCOc1cc2nc(C34COC(C)(C3)C4)cn2cc1NC(=O)c1cccc(C(F)F)n1` |

Assay context (all candidates): rat; constant IV infusion; sampling: 4–24 h infusion; exact duration per analogue not reported; end of infusion; unbound brain/plasma ratio.

## RANK-02 (50 points)

Rank all molecules from highest to lowest Kp,uu.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M076 | `Cc1cc(-c2ncnc(Nc3ccn(C)n3)n2)ccc1CNC(=O)c1noc(C(C)(C)C)n1` |
| M077 | `Cc1cc(-c2ccnc(Nc3ccn(C)n3)n2)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1` |
| M078 | `Cn1ccc(Nc2cc(-c3ccc(CNC(=O)c4nc(C(C)(C)C)no4)c(C4CC4)c3)ncn2)n1` |
| M079 | `Cc1c(CNC(=O)c2nc(C(C)(C)C)no2)ccc(-c2cc(Nc3ccn(C)n3)ncn2)c1F` |
| M080 | `Cc1cc(-c2cc(Nc3ccn(C)n3)ncn2)ccc1CNC(=O)c1nc(C(C)(C)C)no1` |

Assay context (all candidates): rat; constant IV infusion; sampling: 24 h; end of infusion; unbound brain/plasma ratio.

The CXSMILES |a:…| extension specifies enhanced stereochemistry. Preserve it and use a CXSMILES-compatible reader.
