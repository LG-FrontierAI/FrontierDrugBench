---
bench_id: "PROT-V4-RETAIN-001"
category: "Disease-Biology"
title: "PTEN variant function prediction (position 252 D→R)"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "PTEN",
  "wild_type_sequence": "MTAIIKEIVSRNKRRYQEDGFDLDLTYIYPNIIAMGFPAERLEGVYRNNIDDVVRFLDSKHKNHYKIYNLCAERHYDTAKFNCRVAQYPFEDHNPPQLELIKPFCEDLDQWLSEDDNHVAAIHCKAGKGRTGVMICAYLLHRGKFLKAQEALDFYGEVRTRDKKGVTIPSQRRYVYYYSYLLKNHLDYRPVALLFHKMMFETIPMFSGGTCNPQFVVCQLKVKIYSSNSGPTRREDKFMYFEFPQPLPVCGDIKVEFFHKQNKMLKKDKMFHFWVNTFFIPGPEETSEKVENGSLCDQEIDSICSIERADNDKEYLVLTLTKNDLDKANKDKANRYFSPNFKVKLYFTKTVEEPSNPEASSSTSVTPDVSDNEPDHYRYSDTTDSDPENEPFDEDQHTQITKV",
  "experimental_setting": "Measure PTEN lipid phosphatase function by yeast complementation, using a direction-adjusted DMS score in which higher values indicate greater function. The score is fitness on a natural-log scale relative to WT; WT is 0, and negative values indicate reduced function.",
  "variant": "position 252 D→R"
}
```

## Question

Predict the direction-adjusted functional score of this substitution in the specified yeast complementation system. Return one JSON object {"value": <number>} holding that single finite number.
