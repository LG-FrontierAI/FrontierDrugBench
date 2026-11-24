---
bench_id: Pep-088-In-vivo-Study-body-weight-GLP1R-GIPR
category: "In-vivo-Study"
format: mcq
---
# Prompt

Predict which supplied peptide yields the greatest mean reduction in body weight under the stated conditions. Choose the option for that candidate. Target values are hidden. The task predicts the ordering of group means; it does not ask whether active groups differ significantly.

{
  "context": {
    "species": "male C57BL/6J DIO mouse",
    "route": "SC",
    "dose_nmol_per_kg": 10,
    "schedule": "every three days for 15 days",
    "endpoint": "mean percent body-weight change from baseline"
  },
  "residue_definitions": {
    "Z": "alpha-aminoisobutyric acid (Aib)",
    "Z₄": "2-aminobutyric acid (Abu)",
    "B₁⁸": "Lys epsilon-N modified with ([2-(2-amino-ethoxy)-ethoxy]-acetyl)2-(gamma-Glu)1-CO-(CH2)18-CO2H",
    "NH₂": "C-terminal primary amide; other standard amino acids retain the source L configuration"
  },
  "candidates": [
    {
      "id": "candidate_04",
      "sequence_modified": "Y-Z-EGTFTSDYSI-Z-LDKI-A-Q-B₁⁸-Z₄-F-VQWLI-A-GGPSSG-Z-PPPS-NH₂"
    },
    {
      "id": "candidate_03",
      "sequence_modified": "Y-Z-EGTFTSDYSI-Z-LDKI-A-Q-B₁⁸-A-F-VQWLI-A-GGPSSG-Z-PPPS-NH₂"
    },
    {
      "id": "candidate_02",
      "sequence_modified": "Y-Z-EGTFTSDYSI-Z-LDKI-A-Q-B₁⁸-Z-F-VQWLI-A-GGPSSG-Z-PPPS-NH₂"
    },
    {
      "id": "candidate_01",
      "sequence_modified": "Y-Z-EGTFTSDYSI-Z-LDKI-Z-Q-B₁⁸-Z-F-VQWLI-Z-GGPSSGSPPPS-NH₂"
    }
  ]
}

A. candidate_04
B. candidate_03
C. candidate_02
D. candidate_01

Reply with a single option letter only.
