---
bench_id: "SM-054-In-vivo-Study-ADMET-Distribution"
category: "In-vivo-Study"
format: "structured_json"
---
# Prompt

Predict intestinal and liver distribution of small molecules from their structures and the stated animal-study context. Total: 100 points.

All molecular structures and required study information are provided below. PO means oral administration; IV means intravenous administration. Unreported conditions remain unspecified.

## Part 1: Ratio classification (55 points)

For each molecule, predict the bin of its total parent-compound tissue/plasma ratio under its own stated conditions. Each correct answer earns 5 points.

- L: ratio < 10.
- M: 10 <= ratio < 100.
- H: ratio >= 100.

Apply these cutoffs to the numerical ratio on the stated basis. A concentration ratio divides tissue concentration by plasma concentration at the specified time; an AUC ratio divides tissue AUC by plasma AUC over the stated window. Mass-based ratios use tissue ng/g and plasma ng/mL (ratio unit: mL/g); micromolar-based ratios divide the two reported micromolar concentrations. These are total exposure measurements, not unbound ratios or equilibrium partition coefficients. Where concentrations are given as group means, the target is their quotient.

### Q01 — M001 (5 points)

SMILES: `O=S(=O)(NC1CCCOc2c1nn(-c1ccccc1Cl)c2-c1ccc(Cl)cc1)c1ccc(Cl)cc1`

Context: Lean male C57BL/6J mouse; overnight fast; single PO 1 mg/kg dose; liver/plasma concentration ratio at 1 h, in mL/g. Structure has source-unspecified stereochemistry.

### Q02 — M002 (5 points)

SMILES: `Cc1ccc(C#Cc2cc(-c3nn(-c4nc(C(=O)O)cs4)c(CC4CC4)c3Cc3ccc(S(N)(=O)=O)c(F)c3)ccc2F)s1`

Context: Mouse; PO 20 mg/kg as a solution in NaOH/phosphate buffer; liver/plasma concentration ratio at 4 h; both concentrations on the reported micromolar basis.

### Q03 — M003 (5 points)

SMILES: `NS(=O)(=O)c1ccc(Cc2c(-c3cccc(-c4ccccc4)c3)nn(-c3nc(C(=O)O)cs3)c2CC2CC2)cc1`

Context: Mouse; PO 20 mg/kg as a solution in NaOH/phosphate buffer; liver/plasma concentration ratio at 1 h; both concentrations on the reported micromolar basis.

### Q04 — M004 (5 points)

SMILES: `NS(=O)(=O)c1ccc(Cc2c(-c3ccc(F)cc3)nn(-c3nc(C(=O)O)cs3)c2CC2CC2)cc1F`

Context: Mouse; PO 20 mg/kg in 0.5% methylcellulose/0.1% Tween80; liver/plasma concentration ratio at 4 h; both concentrations on the reported micromolar basis.

### Q05 — M005 (5 points)

SMILES: `Nc1ccc2ccc(NC[C@H]3C[C@@H](n4ccc5cncnc54)[C@H](O)[C@@H]3O)cc2n1`

Context: Mouse; PO 50 mg/kg; no elacridar; distal colon about 4 h and systemic plasma 4 h; concentration ratio in mL/g.

### Q06 — M006 (5 points)

SMILES: `CC(C)(C)OC(=O)N1CCN(c2ccc3c(O)c(C(=O)NCc4ccc(C#N)nc4)ncc3n2)CC1`

Context: Healthy C57BL/6J mouse; PO 10 mg/kg; overnight fast; colon/systemic-plasma AUC ratio through 8 h, in mL/g.

### Q07 — M007 (5 points)

SMILES: `NC(=O)Cc1cccc(OCCCN(Cc2cccc(C(F)(F)F)c2Cl)CC(c2ccccc2)c2ccccc2)c1`

Context: Healthy male C57BL/6 mouse; PO 30 mg/kg; ileum/systemic-plasma concentration ratio at 3 h; both concentrations on the reported micromolar basis.

### Q08 — M008 (5 points)

SMILES: `Cc1c(C(=O)NN2CCCCC2)nn(-c2ccc(Cl)cc2Cl)c1-c1ccc(Cl)cc1`

Context: Lean male C57BL/6J mouse; overnight fast; single PO 1 mg/kg dose; liver/plasma concentration ratio at 1 h, in mL/g.

### Q09 — M009 (5 points)

SMILES: `C[C@H](CCC(=O)OCOC(=O)CC[C@H](CP(=O)(O)O)C(=O)O)[C@H]1CC[C@H]2[C@@H]3CC[C@@H]4C[C@H](O)CC[C@]4(C)[C@H]3C[C@H](O)[C@]12C`

Context: Healthy male C57BL/6NHsd mouse; PO dose equimolar to 100 mg/kg 2-(phosphonomethyl)pentanedioic acid; colon/systemic-plasma AUC ratio through 6 h, in mL/g. Predict distribution of the administered parent.

### Q10 — M010 (5 points)

SMILES: `O=C1N[C@](c2ccc(N3CCOCC3)cc2)(c2ccsc2)CC(O)=C1Sc1ccccc1Cl`

Context: Mouse; PO 400 mg/kg in 0.5% methylcellulose/0.1% Tween80; liver/plasma concentration ratio at 1 h; both concentrations on the reported micromolar basis.

### Q11 — M011 (5 points)

SMILES: `C[C@@H](O)Cc1cc2ccc(N)nc2cc1CC[C@H]1C[C@@H](n2ccc3cncnc32)[C@H](O)[C@@H]1O`

Context: Mouse; PO 20 mg/kg with elacridar pretreatment (25 mg/kg); distal colon about 4 h and systemic plasma 4 h; concentration ratio in mL/g.

## Part 2: Analogue comparison (30 points)

For each pair, compare the total parent-compound tissue/plasma ratios under the shared study context. Each correct answer earns 10 points.

Let R_left and R_right denote the ratios for the left and right molecules, respectively. Select one option:

- A: left higher; R_left / R_right > 3.
- B: similar; 1/3 <= R_left / R_right <= 3.
- C: right higher; R_left / R_right < 1/3.

Compare tissue/plasma ratios, not tissue concentrations alone. Similar means within the stated numerical interval; it does not imply statistically demonstrated equivalence.

### Q12 (10 points)

Shared context: Male CD-1 mouse; IV 10 mg/kg in DMSO/Cremophor/PBS (10:10:80); liver/plasma concentration ratio at 4 h, in mL/g.

| Side | Molecule ID | SMILES |
|---|---|---|
| Left | M012 | `Nc1cc(-c2cnco2)ccc1NC1CCCCC1` |
| Right | M013 | `Nc1cc(-c2cnco2)ccc1NC1CCC1` |

### Q13 (10 points)

Shared context: Fasted male C57BL/6 mouse; PO 5 mg/kg in 60% PEG400/water; liver/plasma AUC0-24h ratio in mL/g.

| Side | Molecule ID | SMILES |
|---|---|---|
| Left | M014 | `CC(C)c1cc(Oc2c(Cl)cc(-n3nc(N)c(=O)[nH]c3=O)cc2Cl)n[nH]c1=O` |
| Right | M015 | `CC(C)c1cc(Oc2c(Cl)cc(-n3nc(C#N)c(=O)[nH]c3=O)cc2Cl)n[nH]c1=O` |

### Q14 (10 points)

Shared context: Mouse; PO 20 mg/kg with elacridar pretreatment (25 mg/kg); distal colon about 4 h and systemic plasma 4 h; concentration ratio in mL/g.

| Side | Molecule ID | SMILES |
|---|---|---|
| Left | M016 | `Nc1ccc2cc(CCO)c(CC[C@H]3C[C@@H](n4ccc5cncnc54)[C@H](O)[C@@H]3O)cc2n1` |
| Right | M017 | `Nc1ccc2cc(-c3cn[nH]c3)c(CC[C@H]3C[C@@H](n4ccc5cncnc54)[C@H](O)[C@@H]3O)cc2n1` |

## Part 3: Select the highest liver/plasma exposure ratio (15 points)

### Q15 (15 points)

Select the one molecule with the highest liver/plasma AUC0-24h ratio. Compare the intact administered parent compounds.

All three molecules were evaluated in healthy male C57BL/6 mice after a single oral 10 mg/kg dose in 90:10 olive oil/ethanol, with three animals per sampling time. Plasma was sampled through 24 h; liver samples were collected at 1, 4 and 24 h. The same liver sample preparation and concentration-reporting convention were used for all three molecules. Predict only the within-group ordering of the ratios.

| Molecule ID | SMILES |
|---|---|
| M018 | `C[C@H](Cn1cnc2c(N)ncnc21)OCP(=O)(O)OCCCSCCCCCCCCCCCCc1ccc(F)cc1` |
| M019 | `CCCCCCCCCCCCCCCCSCCCOP(=O)(O)CO[C@H](C)Cn1cnc2c(N)ncnc21` |
| M020 | `C[C@H](Cn1cnc2c(N)ncnc21)OCP(=O)(O)OCCCSCCCCCCCCCCCCC1CCCCC1` |

## Response format

Return ONLY a strict JSON object keyed by Q01 through Q15. A single-item response has the form `{"Q01":"M"}`; this illustrates the syntax only.

Use L, M or H for Q01–Q11; A, B or C for Q12–Q14; and one molecule ID for Q15. No explanations or Markdown fences. Missing or null answers earn zero. An invalid option earns zero for that item. Unknown question IDs, duplicate JSON keys or invalid JSON invalidate the response. The scoring function returns total points divided by 100, on a 0–1 scale.
