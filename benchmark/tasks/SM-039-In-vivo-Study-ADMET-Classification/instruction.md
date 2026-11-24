---
bench_id: "SM-039-In-vivo-Study-ADMET-Classification"
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

## BIN-04 (100 points)

Predict the Kp,uu bin for each molecule: B1, B2 or B3.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M031 | `C=CC(=O)N1CCC[C@@H](Oc2nc(-c3cnn(C)c3)cn3nccc23)CC1` |
| M032 | `Cc1cn(-c2ccc3n(c2=O)CCN([C@@H](C)[C@@H]2CC[C@H](c4cc(F)c(C(F)(F)F)c(F)c4)O2)C3=O)cn1` |
| M033 | `CC(C)[C@H](O)c1nc(-c2cnc(N)c(C(F)(F)F)c2)cn1C12CC(F)(C1)C2 \|a:3\|` |
| M034 | `C=CC(=O)N1CCN([C@@H]2CN(c3cc(N4CCC(c5c(C)cnn5C)CC4)nc(C(F)(F)F)n3)[C@@H]2C)CC1` |
| M035 | `CCn1nc(-c2cnc(N)c(OC(F)F)c2)c2ccc([C@H]3COCCN3C)cc21 \|a:20\|` |
| M036 | `CCn1nc(-c2cnc(N)c(OC(F)(F)F)c2)c2ccc([C@@]34CO[C@@H](CN3C)C4)cc21 \|a:21,24\|` |
| M037 | `Cc1cnc2c(NC(=O)c3cn4cc(C56COC(C)(C5)C6)nc4nc3OC(C)C)cnn2c1` |
| M038 | `Nc1ncc(-c2cn(C34CC(C3)C4)c([C@@H](O)C(F)(F)F)n2)cc1OC(F)(F)F \|a:14\|` |
| M039 | `CCn1nc(-c2cnc(N)c(OC(F)(F)F)c2)c2ccn(C3COC3)c(=O)c21` |
| M040 | `CO[C@H]1COCC[C@H]1n1ccc2c(-c3cnc(N)c(OC(F)F)c3)nn(C3CC3)c2c1=O \|a:2,7\|` |

Assay context:

- M031: rat; constant IV infusion; sampling: 24 h infusion study; end of infusion; unbound brain/plasma ratio.
- M032: male fed Wistar-Han rat; oral; 10 mg/kg; sampling: AUC 0–7 h; AUC; unbound cerebellum/plasma AUC ratio.
- M033, M035, M036, M038, M039, M040: rodent; specific species not reported; IV or oral; route for individual compounds not specified; time basis for individual compounds not reported; reported unbound brain/plasma ratio.
- M034: mouse CD1; PO; single time point; unbound brain/plasma ratio.
- M037: rat; constant IV infusion; sampling: 4–24 h infusion; exact duration per analogue not reported; end of infusion; unbound brain/plasma ratio.

The CXSMILES |a:…| extension specifies enhanced stereochemistry. Preserve it and use a CXSMILES-compatible reader.
