---
bench_id: "SM-038-In-vivo-Study-ADMET-Classification"
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

## BIN-03 (100 points)

Predict the Kp,uu bin for each molecule: B1, B2 or B3.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M021 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)[C@H]2CC[C@H](CC(=O)O)CC2)c(OC(F)F)n1` |
| M022 | `CCn1nc(-c2cnc(N)c(OC(F)(F)F)c2)c2ccc([C@@H]3CCC(=O)N3C)cc21 \|a:21\|` |
| M023 | `C=CC(=O)N1CCN([C@@H]2CN(c3cc(N4CCC(c5c(C)ccnc5CCOC)CC4)nc(C(F)(F)F)n3)[C@@H]2C)CC1` |
| M024 | `CC(C)Oc1cc2nc(C3CCOCC3)cn2cc1NC(=O)c1cccc(C(F)F)n1` |
| M025 | `C=CC(=O)N1CCN(C2CN(c3cc(N4CCC(c5c(C)cnn5C)CC4)nc(C(F)(F)F)n3)C2)CC1` |
| M026 | `CCc1nc(-c2cnc(N)c(C(F)(F)F)c2)c2ccc([C@@H]3CC(=O)N(C)C3)cn12 \|a:20\|` |
| M027 | `Cn1ccc(Nc2nccc(-c3ccc4c(c3)CCCC[C@H]4NC(=O)c3noc(C(C)(C)C)n3)n2)n1` |
| M028 | `Nc1ncc(-c2cn(C34CC(N5CCC(F)(F)CC5)(C3)C4)c([C@@H](O)C(F)(F)F)n2)cc1OC(F)(F)F \|a:22\|` |
| M029 | `CCn1nc(-c2cnc(N)c(OC(F)(F)F)c2)c2ccc([C@H]3COCCN3C)nc21 \|a:21\|` |
| M030 | `CCn1nc(-c2cnc(N)c(OC(F)(F)F)c2)c2ccc([C@H]3CCC(=O)N3C)nc21 \|a:21\|` |

Assay context:

- M021: rat; PO; 10 mg/kg; sampling: 2 h; single time point, 2 h postdose; unbound brain/plasma ratio.
- M022, M026, M028, M029, M030: rodent; specific species not reported; IV or oral; route for individual compounds not specified; time basis for individual compounds not reported; reported unbound brain/plasma ratio.
- M023, M025: mouse CD1; PO; single time point; unbound brain/plasma ratio.
- M024: rat; constant IV infusion; sampling: 4–24 h infusion; exact duration per analogue not reported; end of infusion; unbound brain/plasma ratio.
- M027: rat; constant IV infusion; sampling: 24 h; end of infusion; unbound brain/plasma ratio.

The CXSMILES |a:…| extension specifies enhanced stereochemistry. Preserve it and use a CXSMILES-compatible reader.
