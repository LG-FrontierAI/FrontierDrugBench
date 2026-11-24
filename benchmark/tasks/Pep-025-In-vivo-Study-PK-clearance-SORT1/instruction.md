---
bench_id: Pep-025-In-vivo-Study-PK-clearance-SORT1
category: "In-vivo-Study"
format: mcq
---
# Prompt

Target: **SORT1**
Property to predict: **IV systemic clearance (mL/min/kg)**
Experimental context: species_or_model: Male ICR mouse, 7-9 weeks; route: IV; dose: 2 mg/kg; assay_condition: Single-dose; n=3; 5% DMSO/45% PEG400/50% water; LC-MS/MS; 0.083-24 h sampling.

Using peptide sequence, residue composition, modifications, topology, and the stated experimental context, which candidate is predicted to have the **lowest value** of this property? Select one option. Measured values and source evidence are withheld from the model and used only by the evaluator. This numerical direction is not a claim of therapeutic superiority. Equality and unresolved-order options refer to the experimental measurements, not uncertainty in your own prediction.

Candidate sequence and modification information (no measured property values):
{
  "candidates": [
    {
      "sample_id": "SEQ ID NO.223",
      "compound_id": "SEQ ID NO.223",
      "target": "SORT1",
      "peptide_sequence": "Ac-CTKSKRYICIL-COOH",
      "cyclization_or_linkage": "Disulfide macrocycle between Cys1 and Cys9; N-terminus acetylated; C-terminus is a free acid.",
      "unit": "mL/min/kg",
      "species_or_model": "Male ICR mouse, 7-9 weeks",
      "route": "IV",
      "dose": "2 mg/kg",
      "assay_condition": "Single-dose; n=3; 5% DMSO/45% PEG400/50% water; LC-MS/MS; 0.083-24 h sampling"
    },
    {
      "sample_id": "SEQ ID NO.231",
      "compound_id": "SEQ ID NO.231",
      "target": "SORT1",
      "peptide_sequence": "Ac-CTRKPKPRYICIL-COOH",
      "cyclization_or_linkage": "Disulfide macrocycle between Cys1 and Cys11; N-terminus acetylated; C-terminus is a free acid.",
      "unit": "mL/min/kg",
      "species_or_model": "Male ICR mouse, 7-9 weeks",
      "route": "IV",
      "dose": "2 mg/kg",
      "assay_condition": "Single-dose; n=3; 5% DMSO/45% PEG400/50% water; LC-MS/MS; 0.083-24 h sampling"
    }
  ],
  "noncanonical_residue_definitions": {
    "Ac": {
      "name": "N-terminal acetyl",
      "smiles": "CC(=O)O",
      "notes": "Table 1 Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES."
    }
  }
}

Noncanonical residue and modification definitions:
token,residue_or_modification_name,smiles,formula,molecular_weight_g_mol,size_class,logP,hydrophilicity,charge_at_pH7,aromatic_rings,H_bond_donors,H_bond_acceptors,TPSA_A2,property_basis_and_notes
Ac,N-terminal acetyl,CC(=O)O,,,,,,,,,,,Table 1 Free precursor SMILES reconstructed from the explicit chemical name/stereochemistry; not a complete peptide SMILES.

Options:
A. Both candidates have the same measured value.
B. SEQ ID NO.231
C. The experimental measurements do not resolve which candidate is higher or lower.
D. SEQ ID NO.223

Reply with a single letter (A/B/C/D) only.
