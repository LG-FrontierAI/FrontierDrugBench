---
bench_id: "wrn::PAIR-04"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Pairwise): Predict the hidden intervention outcome from"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

Predict the hidden intervention outcome from the stated baseline and any explicitly allowed support observations. Do not retrieve the original article or answer key. Each item is answered in an independent context. Do not convert dependency scores into viability percentages or tumour-volume ratios.

Panel context
The MSI colorectal cancer model KM12 is represented by five cDNA backgrounds: GFP control, WRN-WT, WRN-E84A (exonuclease-inactivating mutation), WRN-K577M (ATP-binding/helicase-function defect), and WRN-E84A-K577M (double mutant). Expression controls were assessed separately; cDNA identity is given here as an existing experimental background. sgWRN-EIJ targets endogenous WRN but not the exogenous cDNA. In contrast, sgWRN2 targets both endogenous and exogenous WRN. The endpoint is competitive relative cell viability on day 9. Each of six biological replicate Firefly/Renilla ratios is divided by the same-background mean sgCh2-2 negative-control ratio; the six normalized values are then averaged. The negative-control mean is 1. This is cell viability, not helicase enzyme activity. Target-condition results are hidden.

Question
Under sgWRN-EIJ, which cDNA background has higher mean relative viability?

Options
A. WRN-E84A
B. WRN-K577M

Response format
Return only {"answer": "<option letter>"}.

Required response schema:
{"type": "object", "additionalProperties": false, "required": ["answer"], "properties": {"answer": {"type": "string", "enum": ["A", "B"]}}}
