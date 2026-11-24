---
bench_id: Pep-076-Cell-Biology-cAMP-KOR
category: "Cell-Biology"
format: mcq
---
# Prompt

Predict which cyclic dynorphin analogue has the lowest EC50 in the specified cell assay. Use the complete backbone, terminal group and covalent linkage descriptions. No measured activity is supplied.

{
  "target": "mouse KOR",
  "cell_system": "HEK293 cells expressing mouse KOR",
  "assay": "adenylyl-cyclase dependent cAMP inhibition",
  "assay_context": {
    "platform": "Cisbio cAMP HTRF",
    "incubation": "30 minutes at 37 C",
    "signal": "665/620 nm fluorescence ratio",
    "replicates": "three technical replicates"
  },
  "endpoint": "EC50",
  "candidates": [
    {
      "id": "candidate_02",
      "backbone": "YGGFLRRCRPKLK",
      "C_terminus": "COOH",
      "cyclization": "Intramolecular N(Tyr1)-C(=O)-CH2-S(Cys8) thioether linkage. All backbone chiral residues are L."
    },
    {
      "id": "candidate_04",
      "backbone": "YGGFLRRCRPKLK",
      "C_terminus": "CONH2",
      "cyclization": "Intramolecular N(Tyr1)-C(=O)-CH2-S(Cys8) thioether linkage. All backbone chiral residues are L."
    },
    {
      "id": "candidate_01",
      "backbone": "YGGFLRRCRPKLK",
      "C_terminus": "COOH",
      "cyclization": "N-terminal Tyr alpha-NH acylated with 3-mercaptopropionyl; the N-terminal thiol and Cys8 sulfur are connected by -CH2-C(=O)-CH2-. All backbone chiral residues are L."
    },
    {
      "id": "candidate_03",
      "backbone": "YGGFLRRCRPKLK",
      "C_terminus": "CONH2",
      "cyclization": "N-terminal Tyr alpha-NH acylated with 3-mercaptopropionyl; the N-terminal thiol and Cys8 sulfur are connected by -CH2-C(=O)-CH2-. All backbone chiral residues are L."
    }
  ]
}

A. candidate_02
B. candidate_04
C. candidate_01
D. candidate_03

Reply with a single option letter only.
