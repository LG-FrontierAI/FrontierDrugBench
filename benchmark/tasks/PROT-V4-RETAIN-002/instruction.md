---
bench_id: "PROT-V4-RETAIN-002"
category: "Disease-Biology"
title: "GCK variant function prediction (position 288 L→P)"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "GCK",
  "wild_type_sequence": "MLDDRARMEAAKKEKVEQILAEFQLQEEDLKKVMRRMQKEMDRGLRLETHEEASVKMLPTYVRSTPEGSEVGDFLSLDLGGTNFRVMLVKVGEGEEGQWSVKTKHQMYSIPEDAMTGTAEMLFDYISECISDFLDKHQMKHKKLPLGFTFSFPVRHEDIDKGILLNWTKGFKASGAEGNNVVGLLRDAIKRRGDFEMDVVAMVNDTVATMISCYYEDHQCEVGMIVGTGCNACYMEEMQNVELVEGDEGRMCVNTEWGAFGDSGELDEFLLEYDRLVDESSANPGQQLYEKLIGGKYMGELVRLVLLRLVDENLLFHGEASEQLRTRGAFETRFVSQVESDTGDRKQIYNILSTLGLRPSTTDCDIVRRACESVSTRAAHMCSAGLAGVINRMRESRSEDVMRITVGVDGSVYKLHPSFKERFHASVRRLTPSCEITFIESEEGSGRGAALVSAVACKKACMLGQ",
  "experimental_setting": "Measure glucokinase activity by yeast growth complementation, using the original experimental functional score in which higher values indicate greater activity. Scores are centered on 1 for synonymous variants and 0 for nonsense variants.",
  "variant": "position 288 L→P"
}
```

## Question

Predict the glucokinase activity score of this substitution in the same expression background. Use the stated experimental scale and Return one JSON object {"value": <number>} holding that single finite number.
