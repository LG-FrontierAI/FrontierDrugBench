---
bench_id: "wrn::PAIR-06"
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
The model is an HCT116-WRN clone-a subcutaneous xenograft. Cells express Cas9 and carry an inducible sgWRN4 construct. Doxycycline induces genetic WRN knockout; doxycycline is not a WRN small-molecule inhibitor. The vehicle group contains 9 mice and the induction group contains 10 mice. Day 0 is treatment initiation, not implantation. The endpoint is the arithmetic mean of individual-mouse tumour-volume ratios V(day21)/V(day0). Raw volumes are in mm^3; ratios are dimensionless. All day-21 observations are hidden. There are no missing or carried-forward observations in this clone-a panel.
Vehicle day-0 volumes: 551.343, 217.976, 275.885, 459.340, 122.677, 454.382, 476.671, 912.052, 603.074 mm^3.
Induction day-0 volumes: 486.208, 226.374, 440.199, 613.578, 301.981, 284.868, 585.342, 797.225, 1072.802, 459.136 mm^3.

Question
Which arm has the lower mean of individual V(day21)/V(day0) ratios?

Options
A. Induced-knockout arm
B. Vehicle arm

Response format
Return only {"answer": "<option letter>"}.

Required response schema:
{"type": "object", "additionalProperties": false, "required": ["answer"], "properties": {"answer": {"type": "string", "enum": ["A", "B"]}}}
