---
bench_id: "PROT-V4-MECH-006"
category: "Disease-Biology"
title: "VWF variant function prediction (M1,M2)"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "VWF",
  "species": "Homo sapiens",
  "sequence_region": "WT residues 1473–1670; positions use full-length numbering",
  "wild_type_sequence": "MAQVTVGPGLLGVSTLGPKRNSMVLDVAFVLEGSDKIGEADFNRSKEFMEEVIQRMDVGQDSIHVTVLQYSYMVTVEYPFSEAQSKGDILQRVREIRYQGGNRTNTGLALRYLSDHSFLVSQGDREQAPNLVYMVTGNPASDEIKRLPGDIQVVPIGVGPNANVQELERIGWPNAPILIQDFETLPREAPDLVLQRCC",
  "variants": {
    "M1": "position 1505 G→E",
    "M2": "position 1505 G→R"
  },
  "experiment": "Express each full-length VWF construct in HEK293 cells, measure VWF antigen in culture supernatants and cell lysates, and compare the supernatant/lysate ratio. The supplied sequence covers the A2 region; the experimental construct is full-length."
}
```

## Question

The same glycine is replaced by either an acidic or a basic side chain. Which secretion prediction is more reasonable? Output only the letter(s) corresponding to your answer.

## Options

A. The secretion ratio remains near WT for M1 but decreases markedly for M2
B. Secretion decreases markedly for M1 but remains near WT for M2
C. Both M1 and M2 retain secretion ratios near WT
D. Secretion ratios decrease markedly for both M1 and M2
