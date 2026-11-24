---
bench_id: Pep-092-Molecular-Biology-SPR-Kd-FXIa-variant
category: "Molecular-Biology"
format: ranking
---
# Prompt

Target: **human FXIa**  
Assay: **surface plasmon resonance (SPR)**  
Property to rank: **human FXIa binding Kd**

Rank the listed candidates from lower to higher measured human FXIa binding Kd. Every candidate is the same 14-residue cyclic scaffold carrying exactly one alanine substitution; the input gives the scaffold, each candidate's full sequence, its substitution label, and whether Tyr12 is sulfated. The measured Kd values are withheld from the model and used only by the evaluator.

{
  "target": "human FXIa",
  "assay": "surface plasmon resonance (SPR)",
  "endpoint": "human FXIa binding Kd",
  "unit": "nM",
  "direction_to_rank": "lower to higher",
  "measured_values": "withheld from the model; used only by the evaluator",
  "scaffold": {
    "reference_sequence": "YRIVWGPDRIEYDC",
    "length_residues": 14,
    "residue_numbering": "1-based from the N-terminus (Y1 ... C14)",
    "stereochemistry": "all L-amino acids",
    "termini": "free N-terminus, C-terminal amide",
    "cyclization": "head-to-side-chain thioether formed between an N-terminal chloroacetyl group and the Cys14 thiol",
    "modifications_in_scope": "Tyr12 may carry a sulfate ester (sulfotyrosine, Tyr(SO3))",
    "substitution_label_format": "`<parent residue><n>-A` is the alanine scan label: the parent residue letter, then n when that residue occurs more than once in the scaffold (D1 = the first Asp, D2 = the second), then `-A` for the replacement. It names the same position that differs between the candidate sequence and `reference_sequence`.",
    "note": "Every candidate is this scaffold carrying exactly one alanine substitution at the position named in its `substitution` label, with or without the Tyr12 sulfate. The scaffold itself is the patent's reference sequence."
  },
  "candidates": [
    {
      "id": "Compound 13",
      "substitution": "V-A",
      "sequence": "YRIAWGPDRIEYDC",
      "modifications": [],
      "value_unit": "nM"
    },
    {
      "id": "Compound 15",
      "substitution": "G-A",
      "sequence": "YRIVWAPDRIEYDC",
      "modifications": [],
      "value_unit": "nM"
    },
    {
      "id": "Compound 16",
      "substitution": "P-A",
      "sequence": "YRIVWGADRIEYDC",
      "modifications": [],
      "value_unit": "nM"
    },
    {
      "id": "Compound 17",
      "substitution": "D1-A",
      "sequence": "YRIVWGPARIEYDC",
      "modifications": [],
      "value_unit": "nM"
    },
    {
      "id": "Compound 18",
      "substitution": "R2-A",
      "sequence": "YRIVWGPDAIEYDC",
      "modifications": [],
      "value_unit": "nM"
    },
    {
      "id": "Compound 19",
      "substitution": "I2-A",
      "sequence": "YRIVWGPDRAEYDC",
      "modifications": [],
      "value_unit": "nM"
    },
    {
      "id": "Compound 20",
      "substitution": "E-A",
      "sequence": "YRIVWGPDRIAYDC",
      "modifications": [],
      "value_unit": "nM"
    },
    {
      "id": "Compound 22",
      "substitution": "D2-A",
      "sequence": "YRIVWGPDRIEYAC",
      "modifications": [],
      "value_unit": "nM"
    },
    {
      "id": "Compound 26",
      "substitution": "V-A",
      "sequence": "YRIAWGPDRIEYDC",
      "modifications": [
        "Tyr12 sulfotyrosine: the Tyr12 side chain carries a sulfate ester (Tyr(SO3))"
      ],
      "value_unit": "nM"
    },
    {
      "id": "Compound 28",
      "substitution": "G-A",
      "sequence": "YRIVWAPDRIEYDC",
      "modifications": [
        "Tyr12 sulfotyrosine: the Tyr12 side chain carries a sulfate ester (Tyr(SO3))"
      ],
      "value_unit": "nM"
    },
    {
      "id": "Compound 29",
      "substitution": "P-A",
      "sequence": "YRIVWGADRIEYDC",
      "modifications": [
        "Tyr12 sulfotyrosine: the Tyr12 side chain carries a sulfate ester (Tyr(SO3))"
      ],
      "value_unit": "nM"
    },
    {
      "id": "Compound 30",
      "substitution": "D1-A",
      "sequence": "YRIVWGPARIEYDC",
      "modifications": [
        "Tyr12 sulfotyrosine: the Tyr12 side chain carries a sulfate ester (Tyr(SO3))"
      ],
      "value_unit": "nM"
    },
    {
      "id": "Compound 31",
      "substitution": "R2-A",
      "sequence": "YRIVWGPDAIEYDC",
      "modifications": [
        "Tyr12 sulfotyrosine: the Tyr12 side chain carries a sulfate ester (Tyr(SO3))"
      ],
      "value_unit": "nM"
    },
    {
      "id": "Compound 32",
      "substitution": "I2-A",
      "sequence": "YRIVWGPDRAEYDC",
      "modifications": [
        "Tyr12 sulfotyrosine: the Tyr12 side chain carries a sulfate ester (Tyr(SO3))"
      ],
      "value_unit": "nM"
    },
    {
      "id": "Compound 33",
      "substitution": "E-A",
      "sequence": "YRIVWGPDRIAYDC",
      "modifications": [
        "Tyr12 sulfotyrosine: the Tyr12 side chain carries a sulfate ester (Tyr(SO3))"
      ],
      "value_unit": "nM"
    },
    {
      "id": "Compound 34",
      "substitution": "Y2-A",
      "sequence": "YRIVWGPDRIEADC",
      "modifications": [],
      "value_unit": "nM"
    },
    {
      "id": "Compound 35",
      "substitution": "D2-A",
      "sequence": "YRIVWGPDRIEYAC",
      "modifications": [
        "Tyr12 sulfotyrosine: the Tyr12 side chain carries a sulfate ester (Tyr(SO3))"
      ],
      "value_unit": "nM"
    }
  ]
}

Return one JSON array of candidate IDs in the requested order. Do not include explanations. For equal values, sort IDs ascending.
