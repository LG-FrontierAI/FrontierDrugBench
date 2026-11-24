---
bench_id: "PROT-V4-MECH-016"
category: "Disease-Biology"
title: "RET variant function prediction (position 634 C→R)"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "RET",
  "species": "Homo sapiens",
  "sequence_region": "WT residues 590–635; positions use full-length numbering",
  "wild_type_sequence": "IVGGHEPGEPRGIKAGYGTCNCFPEEEKCFCEPEDIQDPLCDELCR",
  "variant": "position 634 C→R",
  "experiment": "Purify the human RET extracellular domain without adding ligand or coreceptor. Compare SEC-MALS with reducing and nonreducing SDS-PAGE. The supplied WT sequence spans the end of the extracellular domain and includes the substituted residue."
}
```

## Question

Which result best fits the assembly rearrangement that could follow this Cys substitution? Output only the letter(s) corresponding to your answer.

## Options

A. Forms dimers even without ligand, and reduction disrupts the disulfide linkage
B. Predominantly forms tetramers without ligand and retains covalent linkage after reduction
C. Forms dimers without ligand but retains an SDS-stable linkage after reduction
D. Is predominantly monomeric without ligand and forms stable dimers only after ligand addition
