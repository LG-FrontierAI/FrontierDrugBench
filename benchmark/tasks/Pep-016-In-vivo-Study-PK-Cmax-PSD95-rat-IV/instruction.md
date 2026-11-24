---
bench_id: Pep-016-In-vivo-Study-PK-Cmax-PSD95-rat-IV
category: "In-vivo-Study"
format: mcq
---
# Prompt

Target: **PSD-95**
Property to predict: **Rat IV plasma Cmax (ng/mL)**
Experimental context: species_or_model: Male SD rat plasma, n=3/group; route: IV bolus; dose: 3 nmol/g; assay_condition: Single IV bolus over 10 min; plasma PK; both compounds dosed at 3 nmol/g.

Using peptide sequence, residue composition, modifications, topology, and the stated experimental context, which candidate is predicted to have the **highest value** of this property? Select one option. Measured values and source evidence are withheld from the model and used only by the evaluator. This numerical direction is not a claim of therapeutic superiority. Equality and unresolved-order options refer to the experimental measurements, not uncertainty in your own prediction.

Candidate sequence and modification information (no measured property values):
{
  "candidates": [
    {
      "sample_id": "Formula-I",
      "compound_id": "Formula (I), SEQ ID NO. 01",
      "target": "PSD-95",
      "peptide_sequence": "r-K-K-R-r-Q-R-R-r-G-Aib-Dab-T-Tle-Tle-T-D-V",
      "cyclization_or_linkage": "Linear; ordinary backbone amides; no ring closure. Uppercase residues are L, lowercase r is D-Arg; Gly and Aib are achiral.",
      "unit": "ng/mL",
      "species_or_model": "Male SD rat plasma, n=3/group",
      "route": "IV bolus",
      "dose": "3 nmol/g",
      "assay_condition": "Single IV bolus over 10 min; plasma PK; both compounds dosed at 3 nmol/g",
      "sequence_tokens": [
        "r",
        "K",
        "K",
        "R",
        "r",
        "Q",
        "R",
        "R",
        "r",
        "G",
        "Aib",
        "Dab",
        "T",
        "Tle",
        "Tle",
        "T",
        "D",
        "V"
      ],
      "sequence_source": "WO2026012336A1 body/claims, SEQ ID NO.01, MD lines 86, 271, 772. Lowercase r = D-Arg, not d-R or D-Asp. Abstract OCR has an extra Tle and is not used."
    },
    {
      "sample_id": "NA-1",
      "compound_id": "Nerinetide / NA-1",
      "target": "PSD-95",
      "peptide_sequence": "YGRKKRRQRRRKLSSIESDV",
      "cyclization_or_linkage": "Linear 20-residue peptide; standard backbone amides",
      "unit": "ng/mL",
      "species_or_model": "Male SD rat plasma, n=3/group",
      "route": "IV bolus",
      "dose": "3 nmol/g",
      "assay_condition": "Single IV bolus over 10 min; plasma PK; both compounds dosed at 3 nmol/g"
    }
  ],
  "noncanonical_residue_definitions": {
    "Aib": {
      "name": "2-aminoisobutyric acid",
      "smiles": "NC(C)(C)C(=O)O",
      "notes": "Achiral free amino acid."
    },
    "Dab": {
      "name": "L-2,4-diaminobutyric acid",
      "smiles": "N[C@@H](CCN)C(=O)O",
      "notes": "Free amino acid; uppercase L convention in WO2026012336A1."
    },
    "Tle": {
      "name": "L-tert-leucine",
      "smiles": "N[C@@H](C(C)(C)C)C(=O)O",
      "notes": "Free amino acid; uppercase L convention in WO2026012336A1."
    },
    "r": {
      "name": "D-arginine",
      "smiles": "N=C(N)NCCC[C@@H](N)C(=O)O",
      "notes": "Free D-arginine; lowercase r in WO2026012336A1 body/claims, SEQ ID NO.01."
    }
  }
}

Noncanonical residue and modification definitions:
token,residue_or_modification_name,smiles,formula,molecular_weight_g_mol,size_class,logP,hydrophilicity,charge_at_pH7,aromatic_rings,H_bond_donors,H_bond_acceptors,TPSA_A2,property_basis_and_notes
Aib,2-aminoisobutyric acid,NC(C)(C)C(=O)O,,,,,,,,,,,Achiral free amino acid.
Dab,"L-2,4-diaminobutyric acid",N[C@@H](CCN)C(=O)O,,,,,,,,,,,Free amino acid; uppercase L convention in WO2026012336A1.
Tle,L-tert-leucine,N[C@@H](C(C)(C)C)C(=O)O,,,,,,,,,,,Free amino acid; uppercase L convention in WO2026012336A1.
r,D-arginine,N=C(N)NCCC[C@@H](N)C(=O)O,,,,,,,,,,,"Free D-arginine; lowercase r in WO2026012336A1 body/claims, SEQ ID NO.01."

Options:
A. Both candidates have the same measured value.
B. NA-1 (Nerinetide / NA-1)
C. The experimental measurements do not resolve which candidate is higher or lower.
D. Formula-I (Formula (I), SEQ ID NO. 01)

Reply with a single letter (A/B/C/D) only.
