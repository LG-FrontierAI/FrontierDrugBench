---
bench_id: Pep-074-Cell-Biology-cAMP-Emax-KOR
category: "Cell-Biology"
format: mcq
---
# Prompt

Predict which cyclic dynorphin analogue has the highest maximum response (Emax) in the specified cell assay. Use the complete backbone, terminal group and covalent linkage descriptions. No measured activity is supplied.

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
  "endpoint": "Emax",
  "candidates": [
    {
      "id": "candidate_03",
      "backbone": "YGGFLRRCRPKLK",
      "C_terminus": "COOH",
      "cyclization": "N-terminal Tyr alpha-NH acylated with 3-mercaptopropionyl; the N-terminal thiol and Cys8 sulfur are connected by -CH2-. All backbone chiral residues are L."
    },
    {
      "id": "candidate_02",
      "backbone": "YGGFLRRCRPKLK",
      "C_terminus": "COOH",
      "cyclization": "Intramolecular N(Tyr1)-C(=O)-CH2-S(Cys8) thioether linkage. All backbone chiral residues are L."
    },
    {
      "id": "candidate_04",
      "backbone": "YGGFLRRIRCKLK",
      "C_terminus": "COOH",
      "cyclization": "N-terminal Tyr alpha-NH acylated with 3-mercaptopropionyl; the N-terminal thiol and Cys10 sulfur are connected by -CH2-. All backbone chiral residues are L."
    },
    {
      "id": "candidate_01",
      "backbone": "YGGFLRRCRPKLK",
      "C_terminus": "COOH",
      "cyclization": "N-terminal Tyr alpha-NH acylated with 3-mercaptopropionyl; the N-terminal thiol and Cys8 sulfur are connected by -CH2-C(=O)-CH2-. All backbone chiral residues are L."
    }
  ]
}

A. candidate_03
B. candidate_02
C. candidate_04
D. candidate_01

Reply with a single option letter only.
