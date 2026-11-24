---
bench_id: "PROT-V4-CLIN-019"
category: "Disease-Biology"
title: "F9 variant function prediction (position 384 R→Q)"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "F9",
  "reference_protein": "P00740",
  "wild_type_sequence": "MQRVNMIMAESPGLITICLLGYLLSAECTVFLDHENANKILNRPKRYNSGKLEEFVQGNLERECMEEKCSFEEAREVFENTERTTEFWKQYVDGDQCESNPCLNGGSCKDDINSYECWCPFGFEGKNCELDVTCNIKNGRCEQFCKNSADNKVVCSCTEGYRLAENQKSCEPAVPFPCGRVSVSQTSKLTRAETVFPDVDYVNSTEAETILDNITQSTQSFNDFTRVVGGEDAKPGQFPWQVVLNGKVDAFCGGSIVNEKWIVTAAHCVETGVKITVVAGEHNIEETEHTEQKRNVIRIIPHHNYNAAINKYNHDIALLELDEPLVLNSYVTPICIADKEYTNIFLKFGSGYVSGWGRVFHKGRSALVLQYLRVPLVDRATCLRSTKFTIYNNMFCAGFHEGGRDSCQGDSGGPHVTEVEGTSFLTGIISWGEECAMKGKYGIYTKVSRYVNWIKEKTKLT",
  "variant": "position 384 R→Q",
  "experiment": "Express the F9 variant in HEK293T cells, measure coagulation activity by APTT and FIX antigen by ELISA, and compare the activity/antigen ratio; the clinical target is hemophilia B.",
  "disease": "hemophilia B"
}
```

## Question

Which combination of coagulation activity per unit FIX antigen and disease association is most likely? Output only the letter(s) corresponding to your answer.

## Options

A. Coagulation activity is completely lost, but the variant does not support pathogenicity for hemophilia B
B. Coagulation activity increases, but this does not support pathogenicity for hemophilia B
C. Coagulation activity decreases, supporting pathogenicity for hemophilia B
D. Coagulation activity remains at WT levels, and the variant supports pathogenicity for hemophilia B
