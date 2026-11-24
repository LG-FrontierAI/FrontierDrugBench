---
bench_id: "PROT-V4-MECH-024"
category: "Disease-Biology"
title: "SCN4A variant function prediction (M1,M2)"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "SCN4A",
  "species": "Rattus norvegicus",
  "sequence_region": "WT residues 620–690; positions use full-length numbering",
  "wild_type_sequence": "VLKLIAMDPYEYFQQGWNIFDSFIVTLSLVELGLANVQGLSVLRSFRLLRVFKLAKSWPTLNMLIKIIGNS",
  "variants": {
    "M1": "position 666 R→G",
    "M2": "position 666 R→H"
  },
  "experiment": "Express rat Nav1.4 variants corresponding to a human hypokalemic periodic paralysis site in Xenopus oocytes. Measure steady-state gating-pore currents during hyperpolarization with the central pore blocked by 1 μM TTX. Compare physiological Na+/K+ conditions with conditions in which the major cations on both sides are replaced by NMDG.",
  "human_homolog_mapping": "Rat R666 ↔ human SCN4A R672; predict the rat construct's results."
}
```

## Question

Which combination best fits the gating-pore permeability produced by these side chains? Output only the letter(s) corresponding to your answer.

## Options

A. M1 predominantly conducts H+, whereas M2 conducts only K+
B. Both currents are predominantly carried by Cl−
C. M1 conducts Na+/K+, whereas the steady-state current of M2 is more consistent with H+ selectivity
D. Both are strictly Na+-selective, and both remain fully intact after replacement with NMDG
