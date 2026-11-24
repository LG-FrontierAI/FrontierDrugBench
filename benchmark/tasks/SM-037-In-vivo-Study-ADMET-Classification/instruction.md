---
bench_id: "SM-037-In-vivo-Study-ADMET-Classification"
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

## BIN-02 (100 points)

Predict the Kp,uu bin for each molecule: B1, B2 or B3.

| Molecule ID | SMILES / CXSMILES |
|---|---|
| M011 | `Cc1cn(-c2ccc3n(c2=O)CCN([C@@H](C)[C@@H]2CC[C@H](c4ccc(C(F)(F)F)c(F)c4F)O2)C3=O)cn1` |
| M012 | `C=CC(=O)N1CCN(C2CN(c3cc(N4CCC(c5nccs5)CC4)nc(C(F)(F)F)n3)C2)CC1` |
| M013 | `CCn1nc(-c2cnc(N)c(OC(F)F)c2)c2ccc([C@H]3CCC(=O)N3C)cc21 \|a:20\|` |
| M014 | `CN1CCCC[C@H]1c1ccc2c(-c3cnc(N)c(C(F)(F)F)c3)ncn2c1 \|a:6\|` |
| M015 | `Cc1cn(-c2ccc3n(c2=O)CCN([C@@H](C)[C@@H]2CC[C@H](c4cc(F)c(Cl)cc4C(F)(F)F)O2)C3=O)cn1` |
| M016 | `CC(C)c1nc(-c2cnc(N)c(OC(F)F)c2)c2ccc([C@H]3COCCN3C)cn12 \|a:21\|` |
| M017 | `C=CC(=O)N1CCN(C2CN(c3cc(N4CCC(c5scnc5C)CC4)nc(C(F)(F)F)n3)C2)CC1` |
| M018 | `CCc1nc(-c2cnc(N)c(C(F)(F)F)c2)c2ccc(C3CCN(C)CC3)cn12` |
| M019 | `COc1ccc(NC(=O)N(c2ccccc2C(C)C)[C@@H]2CC[C@]3(C(=O)O)C[C@@H]3C2)c(OC(F)F)n1` |
| M020 | `Cc1cc(-c2ccnc(Nc3cnn(C)c3)n2)ccc1CNC(=O)c1noc(C(C)(C)C)n1` |

Assay context:

- M011, M015: male Sprague-Dawley rat; oral; 10 mg/kg; sampling: samples 1,4,8,11,16,20 h; AUC summary; AUC; unbound cerebellum/plasma AUC ratio.
- M012, M017: mouse CD1; PO; single time point; unbound brain/plasma ratio.
- M013, M014, M016, M018: rodent; specific species not reported; IV or oral; route for individual compounds not specified; time basis for individual compounds not reported; reported unbound brain/plasma ratio.
- M019: rat; PO; 10 mg/kg; sampling: 2 h; single time point, 2 h postdose; unbound brain/plasma ratio.
- M020: rat; constant IV infusion; sampling: 24 h; end of infusion; unbound brain/plasma ratio.

The CXSMILES |a:…| extension specifies enhanced stereochemistry. Preserve it and use a CXSMILES-compatible reader.
