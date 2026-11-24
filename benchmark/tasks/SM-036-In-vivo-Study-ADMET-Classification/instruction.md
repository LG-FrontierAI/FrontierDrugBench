---
bench_id: "SM-036-In-vivo-Study-ADMET-Classification"
category: "In-vivo-Study"
format: "structured_json"
---

# Prompt

Predict experimental unbound brain/plasma partitioning (Kp,uu) from the supplied molecular structures. Total: 100 points.
Structures are listed in each question. The same molecule ID always denotes the same structure.
Use the supplied assay context; unreported conditions remain unspecified.
All required inputs are included in this Markdown; inputs/ contains no additional material.
Kp,uu is the unbound tissue/plasma ratio for the specified brain region and time basis. Use the stated species, route and sampling context. Brain and cerebellum, single-time-point and AUC measurements, and different species or dosing regimens must retain their stated distinctions.
Bins: B1 <0.1; B2 0.1–<0.3; B3 ≥0.3.

Return a binning object {"molecule_id": "bin"} under the question ID. Each of the 10 molecules earns 10 points for its correct bin.

Return ONLY one strict JSON object keyed by the question IDs below. Do not include Markdown fences or explanations.
Unanswered questions or molecules may be omitted or set to null and earn zero. Arrays must contain distinct, valid options.
Unknown question IDs or duplicate JSON keys invalidate the entire response. Unknown molecule IDs in a binning object
make that question score zero; other invalid answers lose only the affected question or molecule points.
The scoring interface returns total points divided by 100, a number from 0 to 1.

## BIN-01 (100 points)

Predict the Kp,uu bin for each molecule: B1, B2 or B3.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M001 | `CC(C)c1nc(-c2cnc(N)c(OC(F)(F)F)c2)cn1C12CC(N3CCOCC3)(C1)C2` |
| M002 | `Cn1ccc(Nc2cc(-c3ccc(CNC(=O)c4nc(C(C)(C)C)no4)c(C(F)F)c3F)ncn2)n1` |
| M003 | `CCn1nc(-c2cnc(N)c(OC(F)F)c2)c2ccc(N3CC4(COC4)C3)nc21` |
| M004 | `CC(=O)N1CC(N(C(=O)Nc2ccc(C)nc2OC(F)F)c2ccccc2C(C)C)C1` |
| M005 | `CC(=O)N1CC(C(=O)Nc2ccc(C)nc2OC(F)F)(c2ccccc2C(C)C)C1` |
| M006 | `CCn1nc(-c2cnc(N)c(OC(F)(F)F)c2)c2ccc(N3C[C@@H]4C[C@H]3CN4C3COC3)nc21 \|a:23,25\|` |
| M007 | `CCn1nc(-c2cnc(N)c(OC(F)F)c2)c2ccn([C@H](C)[C@@H]3CCOC3)c(=O)c21 \|a:20,22\|` |
| M008 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)[C@H]2CC[C@@H](CC(=O)O)CC2)c(OC(F)F)n1` |
| M009 | `C=CC(=O)N1CCN([C@@H]2CN(c3cc(N4CCC(c5c(C)cnn5C)CC4)nc(C(F)(F)F)n3)C2(C)C)CC1` |
| M010 | `CCn1nc(-c2cnc(N)c(OC(F)(F)F)c2)c2ccn(C3CCN(C4COC4)CC3)c(=O)c21` |

Assay context:

- M001, M003, M006, M007, M010: rodent; specific species not reported; IV or oral; route for individual compounds not specified; time basis for individual compounds not reported; reported unbound brain/plasma ratio.
- M002: rat; constant IV infusion; sampling: 24 h; end of infusion; unbound brain/plasma ratio.
- M004, M005, M008: rat; PO; 10 mg/kg; sampling: 2 h; single time point, 2 h postdose; unbound brain/plasma ratio.
- M009: mouse CD1; PO; single time point; unbound brain/plasma ratio.

The CXSMILES |a:…| extension specifies enhanced stereochemistry. Preserve it and use a CXSMILES-compatible reader.
