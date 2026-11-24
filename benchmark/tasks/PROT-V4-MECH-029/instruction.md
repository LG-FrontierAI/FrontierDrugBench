---
bench_id: "PROT-V4-MECH-029"
category: "Disease-Biology"
title: "EGFR variant function prediction (position 790 T→M)"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "EGFR",
  "species": "Homo sapiens",
  "sequence_region": "WT residues 696–1022; positions use full-length numbering",
  "wild_type_sequence": "GEAPNQALLRILKETEFKKIKVLGSGAFGTVYKGLWIPEGEKVKIPVAIKELREATSPKANKEILDEAYVMASVDNPHVCRLLGICLTSTVQLITQLMPFGCLLDYVREHKDNIGSQYLLNWCVQIAKGMNYLEDRRLVHRDLAARNVLVKTPQHVKITDFGLAKLLGAEEKEYHAEGGKVPIKWMALESILHRIYTHQSDVWSYGVTVWELMTFGSKPYDGIPASEISSILEKGERLPQPPICTIDVYMIMVKCWMIDADSRPKFRELIIEFSKMARDPQRYLVIQGDERMHLPSPTDSNFYRALMDEEDMDDVVDADEYLIPQQG",
  "variant": "position 790 T→M",
  "experiment": "Purify WT EGFR kinase domain and the kinase domain carrying only T790M. Use the Tyr1173-site peptide ENAEYLRVA as substrate and fit apparent ATP Km and kcat."
}
```

## Question

Without L858R in the background, which combination is more likely for T790M? Output only the letter(s) corresponding to your answer.

## Options

A. kcat decreases, while ATP Km remains near WT
B. kcat is unchanged, while ATP Km decreases by more than tenfold
C. kcat increases, while ATP Km remains near WT
D. Both kcat and ATP Km decrease by more than tenfold
