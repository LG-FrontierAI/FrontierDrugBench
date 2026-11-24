---
bench_id: Pep-014-In-vivo-Study-PK-AUC-NPRC
category: "In-vivo-Study"
format: mcq
---
# Prompt

Target: **NPR-C**
Property to predict: **IV AUC from zero to last quantifiable sample (ng*h/mL)**
Experimental context: species_or_model: Mouse (strain and sex not specified); route: IV, tail vein; dose: 1 mg/kg; assay_condition: Single administration in histidine/sucrose/Tween-80 vehicle; LC/MS with internal standard; nominal sampling 0.083, 0.5, 1, 2, 4 and 12 h.

Using peptide sequence, residue composition, modifications, topology, and the stated experimental context, which candidate is predicted to have the **highest value** of this property? Select one option. Measured values and source evidence are withheld from the model and used only by the evaluator. This numerical direction is not a claim of therapeutic superiority. Equality and unresolved-order options refer to the experimental measurements, not uncertainty in your own prediction.

Candidate sequence and modification information (no measured property values):
{
  "candidates": [
    {
      "sample_id": "POL-1-10-2",
      "compound_id": "POL-1-10-2",
      "target": "NPR-C",
      "peptide_sequence": "bALA-SAR-SAR-SAR-SAR-his-his-his-his-his-his-GLY-GLY-his-his-his-his-bALA-bALA-phe-SER-J92-A99-ser-GLY-A64-ILE-ASP-E80-ILE",
      "cyclization_or_linkage": "Linear peptide construct; standard backbone amide connections, including the named noncanonical residues. No siRNA payload is attached to this measured construct.",
      "n_terminal_modification": "6-azidohexanoyl attached through an amide to the N-terminal amino group",
      "c_terminal_modification": "Methylamide (-CONHCH3)",
      "unit": "ng*h/mL",
      "species_or_model": "Mouse (strain and sex not specified)",
      "route": "IV, tail vein",
      "dose": "1 mg/kg",
      "assay_condition": "Single administration in histidine/sucrose/Tween-80 vehicle; LC/MS with internal standard; nominal sampling 0.083, 0.5, 1, 2, 4 and 12 h"
    },
    {
      "sample_id": "POL-1-9-2",
      "compound_id": "POL-1-9-2",
      "target": "NPR-C",
      "peptide_sequence": "bALA-SAR-SAR-SAR-SAR-phe-SER-J92-A99-ser-GLY-A64-ILE-ASP-E80-ILE",
      "cyclization_or_linkage": "Linear peptide construct; standard backbone amide connections, including the named noncanonical residues. No siRNA payload is attached to this measured construct.",
      "n_terminal_modification": "6-azidohexanoyl attached through an amide to the N-terminal amino group",
      "c_terminal_modification": "Methylamide (-CONHCH3)",
      "unit": "ng*h/mL",
      "species_or_model": "Mouse (strain and sex not specified)",
      "route": "IV, tail vein",
      "dose": "1 mg/kg",
      "assay_condition": "Single administration in histidine/sucrose/Tween-80 vehicle; LC/MS with internal standard; nominal sampling 0.083, 0.5, 1, 2, 4 and 12 h"
    }
  ],
  "noncanonical_residue_definitions": {
    "bALA": {
      "name": "beta-Alanine",
      "smiles": "NCCC(=O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary."
    },
    "SAR": {
      "name": "N-methyl-Glycine (sarcosine)",
      "smiles": "N(C)CC(=O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary."
    },
    "E80": {
      "name": "N(omega)-methyl-L-arginine; Arg(Me) in SEQ 94/96",
      "smiles": "CN=C(N)NCCC[C@@H](C(=O)O)N",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary."
    },
    "J92": {
      "name": "trans-4-Hydroxy-D-proline; lowercase hyp in SEQ 94/96",
      "smiles": "C1[C@@H](CN[C@H]1C(=O)O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary."
    },
    "A99": {
      "name": "3-Cyclohexyl-L-alanine; CHA in SEQ 94/96",
      "smiles": "N[C@@H](CC1CCCCC1)C(=O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary."
    },
    "A64": {
      "name": "trans-4-Hydroxy-L-proline; uppercase HYP in SEQ 94/96",
      "smiles": "O=C(O)[C@@H]1C[C@@H](O)CN1",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary."
    },
    "C71": {
      "name": "3-Cyclohexyl-D-alanine",
      "smiles": "N[C@H](CC1CCCCC1)C(=O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary."
    },
    "G77": {
      "name": "5-aminovaleric acid",
      "smiles": "C(CCN)CC(=O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary."
    },
    "G78": {
      "name": "6-aminohexanoic acid",
      "smiles": "C(CCC(=O)O)CCN",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary."
    },
    "E76": {
      "name": "N-Methyl-L-serine",
      "smiles": "N(C)[C@@H](CO)C(=O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary."
    },
    "NLE": {
      "name": "L-Norleucine",
      "smiles": "N[C@@H](CCCC)C(=O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary."
    },
    "H16": {
      "name": "N-Methyl-L-isoleucine",
      "smiles": "N(C)[C@@H]([C@H](CC)C)C(=O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary."
    },
    "E82": {
      "name": "L-Beta-leucine; retain the source designation",
      "smiles": "N[C@@H](C(C)C)CC(=O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary."
    },
    "I14": {
      "name": "alpha-methyl-L-aspartic acid",
      "smiles": "C[C@](CC(=O)O)(C(=O)O)N",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary."
    },
    "K02": {
      "name": "L-Aminopimelic acid",
      "smiles": "C(CCC(=O)O)C[C@@H](C(=O)O)N",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary."
    },
    "phe": {
      "name": "D-phenylalanine",
      "smiles": "N[C@H](Cc1ccccc1)C(=O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES."
    },
    "ser": {
      "name": "D-serine",
      "smiles": "N[C@H](CO)C(=O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES."
    },
    "his": {
      "name": "D-histidine",
      "smiles": "N[C@H](Cc1c[nH]cn1)C(=O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES."
    },
    "ile": {
      "name": "D-isoleucine",
      "smiles": "CC[C@@H](C)[C@@H](N)C(=O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES."
    },
    "asp": {
      "name": "D-aspartic acid",
      "smiles": "N[C@H](CC(=O)O)C(=O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES."
    },
    "leu": {
      "name": "D-leucine",
      "smiles": "CC(C)C[C@@H](N)C(=O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES."
    },
    "6-azidohexanoyl": {
      "name": "N-terminal acyl group derived from 6-azidohexanoic acid",
      "smiles": "[N-]=[N+]=NCCCCCC(=O)O",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES."
    },
    "NHCH3": {
      "name": "C-terminal methylamide",
      "smiles": "CN",
      "notes": "Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES."
    }
  }
}

Noncanonical residue and modification definitions:
token,residue_or_modification_name,smiles,formula,molecular_weight_g_mol,size_class,logP,hydrophilicity,charge_at_pH7,aromatic_rings,H_bond_donors,H_bond_acceptors,TPSA_A2,property_basis_and_notes
bALA,beta-Alanine,NCCC(=O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary.
SAR,N-methyl-Glycine (sarcosine),N(C)CC(=O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary.
E80,N(omega)-methyl-L-arginine; Arg(Me) in SEQ 94/96,CN=C(N)NCCC[C@@H](C(=O)O)N,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary.
J92,trans-4-Hydroxy-D-proline; lowercase hyp in SEQ 94/96,C1[C@@H](CN[C@H]1C(=O)O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary.
A99,3-Cyclohexyl-L-alanine; CHA in SEQ 94/96,N[C@@H](CC1CCCCC1)C(=O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary.
A64,trans-4-Hydroxy-L-proline; uppercase HYP in SEQ 94/96,O=C(O)[C@@H]1C[C@@H](O)CN1,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary.
C71,3-Cyclohexyl-D-alanine,N[C@H](CC1CCCCC1)C(=O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary.
G77,5-aminovaleric acid,C(CCN)CC(=O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary.
G78,6-aminohexanoic acid,C(CCC(=O)O)CCN,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary.
E76,N-Methyl-L-serine,N(C)[C@@H](CO)C(=O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary.
NLE,L-Norleucine,N[C@@H](CCCC)C(=O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary.
H16,N-Methyl-L-isoleucine,N(C)[C@@H]([C@H](CC)C)C(=O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary.
E82,L-Beta-leucine; retain the source designation,N[C@@H](C(C)C)CC(=O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary.
I14,alpha-methyl-L-aspartic acid,C[C@](CC(=O)O)(C(=O)O)N,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary.
K02,L-Aminopimelic acid,C(CCC(=O)O)C[C@@H](C(=O)O)N,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Exact free-monomer SMILES transcribed from WO2025222300A1 Table 3 glossary.
phe,D-phenylalanine,N[C@H](Cc1ccccc1)C(=O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES.
ser,D-serine,N[C@H](CO)C(=O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES.
his,D-histidine,N[C@H](Cc1c[nH]cn1)C(=O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES.
ile,D-isoleucine,CC[C@@H](C)[C@@H](N)C(=O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES.
asp,D-aspartic acid,N[C@H](CC(=O)O)C(=O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES.
leu,D-leucine,CC(C)C[C@@H](N)C(=O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES.
6-azidohexanoyl,N-terminal acyl group derived from 6-azidohexanoic acid,[N-]=[N+]=NCCCCCC(=O)O,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES.
NHCH3,C-terminal methylamide,CN,,,,,,,,,,,Table 2/3 glossary and Table 4 terminal modifications. Uppercase standard residues are L; lowercase are D. Gly is achiral. No calculated descriptors supplied. Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES.

Options:
A. Both candidates have the same measured value.
B. The experimental measurements do not resolve which candidate is higher or lower.
C. POL-1-9-2
D. POL-1-10-2

Reply with a single letter (A/B/C/D) only.
