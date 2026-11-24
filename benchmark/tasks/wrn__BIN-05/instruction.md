---
bench_id: "wrn::BIN-05"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Binary): Predict the hidden intervention outcome from"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

Predict the hidden intervention outcome from the stated baseline and any explicitly allowed support observations. Do not retrieve the original article or answer key. Each item is answered in an independent context. Do not convert dependency scores into viability percentages or tumour-volume ratios.

Panel context
The panel contains HCT116 parental cells, a chromosome-2 transfer control (Ch2), and a chromosome-3-plus-5 transfer background (Ch3+5). Ch3+5 restores MLH1/MSH3-associated MMR activity; whole-chromosome transfer changes additional genes and is not a clean single-gene add-back. For each shRNA condition, day-7 CellTiter-Glo viability is summarized as the mean of six biological replicates divided by the same-background shRFP-control mean. A value of 1 is the matched control. WRN knockdown, control perturbations, and genetic backgrounds must not be conflated. Target-condition outcomes are hidden.
Explicitly allowed previously observed support information:
- HCT116 parental:shWRN1: observed mean = 0.153427 (dimensionless_relative_viability).
- HCT116 Ch2:shWRN1: observed mean = 0.066049 (dimensionless_relative_viability).

Question
For Ch3+5 treated with shWRN1, predict whether mean relative viability is at least 0.70. The 0.70 cutoff is a benchmark convention, not proof of complete rescue.

Options
A. No
B. Yes

Response format
Return only {"answer": "<option letter>"}.

Required response schema:
{"type": "object", "additionalProperties": false, "required": ["answer"], "properties": {"answer": {"type": "string", "enum": ["A", "B"]}}}
