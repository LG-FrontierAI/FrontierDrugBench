---
bench_id: Pep-089-In-vivo-Study-fat-mass-GLP1R-GIPR
category: "In-vivo-Study"
format: ranking
---
# Prompt

Target: **GLP-1R/GIPR dual agonist peptides**  
Assay: **C57BL/6J male DIO mouse; repeated SC dosing**  
Property to rank: **change in fat mass from baseline**

Rank the listed candidates from lower to higher measured change in fat mass from baseline. Predict the ranking using the supplied candidate sequences, sequence-notation definitions, molecular annotations, and assay context. The measured values are withheld from the model and used only by the evaluator.

{
  "target": "GLP-1R/GIPR dual agonist peptides",
  "assay": "C57BL/6J male DIO mouse; repeated SC dosing",
  "endpoint": "change in fat mass from baseline",
  "direction_to_rank": "lower to higher",
  "context": {
    "target": "GLP-1R/GIPR dual agonist peptides",
    "species": "C57BL/6J male DIO mouse",
    "route": "SC",
    "dose": "10 nmol/kg every three days for 15 days",
    "unit": "%"
  },
  "candidates": [
    {
      "id": "SEQ ID NO:1",
      "value_unit": "%",
      "sequence": "Y-Z-EGTFTSDYSI-Z-LDKI-Z-Q-B₁⁸-Z-F-VQWLI-Z-GGPSSGSPPPS-NH₂"
    },
    {
      "id": "SEQ ID NO:2",
      "value_unit": "%",
      "sequence": "Y-Z-EGTFTSDYSI-Z-LDKI-A-Q-B₁⁸-Z-F-VQWLI-A-GGPSSG-Z-PPPS-NH₂"
    },
    {
      "id": "SEQ ID NO:3",
      "value_unit": "%",
      "sequence": "Y-Z-EGTFTSDYSI-Z-LDKI-A-Q-B₁⁸-A-F-VQWLI-A-GGPSSG-Z-PPPS-NH₂"
    },
    {
      "id": "SEQ ID NO:4",
      "value_unit": "%",
      "sequence": "Y-Z-EGTFTSDYSI-Z-LDKI-A-Q-B₁⁸-Z₄-F-VQWLI-A-GGPSSG-Z-PPPS-NH₂"
    },
    {
      "id": "SEQ ID NO:5",
      "value_unit": "%",
      "sequence": "Y-Z-EGTFTSDYSI-Z-LDKI-A-Q-B₁⁸-Z₅-F-VQWLI-A-GGPSSG-Z-PPPS-NH₂"
    },
    {
      "id": "SEQ ID NO:6",
      "value_unit": "%",
      "sequence": "Y-Z-EGTFTSDYSI-Z-LDKI-A-Q-B₁⁸-Z-Z⁸-VQWLI-A-GGPSSGAPPPS-NH₂"
    },
    {
      "id": "SEQ ID NO:7",
      "value_unit": "%",
      "sequence": "Y-Z-EGTFTSDYSI-Z-LDKI-A-Q-B₁⁸-Z₄-Z⁸-VQWLI-A-GGPSSGAPPPS-NH₂"
    },
    {
      "id": "SEQ ID NO:8",
      "value_unit": "%",
      "sequence": "Y-Z-EGTFTSDYSI-Z-LDKI-A-Q-B₁⁸-Z-Z⁸-VQWLI-Z₁₄-GGPSSGAPPPS-NH₂"
    },
    {
      "id": "SEQ ID NO:9",
      "value_unit": "%",
      "sequence": "Y-Z-EGTFTSDYSI-Z-LDKI-A-Q-B₁⁸-Z₄-Z⁸-VQWLI-Z₁₄-GGPSSGAPPPS-NH₂"
    },
    {
      "id": "SEQ ID NO:10",
      "value_unit": "%",
      "sequence": "Y-Z-EGTFTSDYSI-Z-LDKI-A-Q-B₁⁸-A-Z⁸-VQWLI-Z₁₄-GGPSSGAPPPS-NH₂"
    },
    {
      "id": "SEQ ID NO:11",
      "value_unit": "%",
      "sequence": "Y-Z-EGTFTSDYSI-Z-LDKI-A-Q-B₁⁸-Z-F-VQWLI-Z₁₄-GGPSSGAPPPS-NH₂"
    },
    {
      "id": "SEQ ID NO:12",
      "value_unit": "%",
      "sequence": "Y-Z-EGTFTSDYSI-Z-LDKI-A-Q-B₁⁸-Z₄-F-VQWLI-Z₁₄-GGPSSGAPPPS-NH₂"
    }
  ],
  "sequence_notation": {
    "source": "WO2026011797, paragraph 0195",
    "verbatim_definition": "[0195] In the above peptide sequences: Z is an α-aminoisobutyric acid residue; Z₁ is a 2-amino-3,3,3-trifluoro-2-methylpropanoic acid residue; Z₂ is a 1-aminocyclobutane carboxylic acid residue; Z₃ is an isovaline residue; Z₄ is a 2-aminobutyric acid residue; Z₅ is a norvaline residue; Z₆ is a 3-(1-naphthyl)-alanine residue; Z₇ is a 3-chlorophenylalanine residue; Z⁸ is a 3-trifluoromethylphenylalanine residue; Z₉ is a 3-fluorophenylalanine residue; Z₁₀ is a 2-fluorophenylalanine residue; Z₁₁ is a 2-chlorophenylalanine residue; Z₁₂ is a 2-trifluoromethylphenylalanine residue; Z₁₃ is a 3-(2-naphthyl)-alanine residue; Z₁₄ is a D-serine residue; B₁₆ is a lysine residue whose side-chain ε-amino group is modified with ([2-(2-amino-ethoxy)-ethoxy]-acetyl)₂ -(γGlu)₁ -CO-(CH₂)₁₆ -CO₂ H; B₁₇ is a lysine residue whose side-chain ε-amino group is modified with ([2-(2-amino-ethoxy)-ethoxy]-acetyl)₂ -(γGlu)₁ -CO-(CH₂)₁₇ -CO₂ H; B₁⁸ is a lysine residue whose side-chain ε-amino group is modified with ([2-(2-amino-ethoxy)-ethoxy]-acetyl)₂ -(γGlu)₁ -CO-(CH₂)₁⁸ -CO₂ H; B₁₉ is a lysine residue whose side-chain ε-amino group is modified with ([2-(2-amino-ethoxy)-ethoxy]-acetyl)₂ -(γGlu)₁ -CO-(CH₂)₁₉ -CO₂ H; B₂₀ is a lysine residue whose side-chain ε-amino group is modified with ([2-(2-amino-ethoxy)-ethoxy]-acetyl)₂ -(γGlu)₁ -CO-(CH₂)₂₀ -CO₂ H; B₂₁ is a lysine residue whose side-chain ε-amino group is modified with ([2-(2-amino-ethoxy)-ethoxy]-acetyl)₂ -(γGlu)₁ -CO-(CH₂)₂₁ -CO₂ H; B₂₂ is a lysine residue whose side-chain ε-amino group is modified with ([2-(2-amino-ethoxy)-ethoxy]-acetyl)₂ -(γGlu)₁ -CO-(CH₂)₂₂ -CO₂ H."
  }
}

Return one JSON array of candidate IDs in the requested order. Do not include explanations. For equal values, sort IDs ascending.
