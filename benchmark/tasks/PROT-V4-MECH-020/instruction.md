---
bench_id: "PROT-V4-MECH-020"
category: "Disease-Biology"
title: "CASR variant function prediction (position 129 C→S)"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "CASR",
  "species": "Homo sapiens",
  "sequence_region": "WT residues 20–180; positions use full-length numbering",
  "wild_type_sequence": "YGPDQRAQKKGDIILGGLFPIHFGVAAKDQDLKSRPESVECIRYNFRGFRWLQAMIFAIEEINSSPALLPNLTLGYRIFDTCNTVSKALEATLSFVAQNKIDSLNLDEFCNCSEHIPSTIAVVGATGSGVSTAVANLLGLFYIPQVSYASSSRLLSNKNQF",
  "variant": "position 129 C→S",
  "experiment": "Express CaSR in HEK293 cells with matched cell-surface expression. Assess receptor signaling without added agonist and construct CaCl2 concentration–response curves."
}
```

## Question

Which combination is most likely when this extracellular Cys is replaced by Ser? Output only the letter(s) corresponding to your answer.

## Options

A. Basal activity decreases, and CaCl2 potency decreases
B. Basal activity increases, and CaCl2 potency increases
C. Basal activity decreases, and CaCl2 potency increases
D. Basal activity increases, and CaCl2 potency decreases
