---
bench_id: "wrn::BIN-03"
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
This screening panel measures the growth/survival effect of genetic WRN perturbation, not drug response. CRISPR scores use CERES; RNAi scores use DEMETER2. More-negative scores indicate greater dependency. Zero is the negative-control gene median and -1 is the pan-essential gene median, not a percentage of cell death. The composite field uses the source-provided average when both platforms are available and the source-provided available score when only one is present; no missing platform is imputed.
SNU1: gastric cancer; CCLE MSI annotation=MSI; MMR-loss flag present; MLH1 flagged for a damaging mutation; TP53 annotation=TP53_proficient; fraction of deletion events in microsatellite regions=0.788050; available WRN screening platforms: CRISPR and RNAi. All WRN outcome scores and the dependency label are hidden unless explicitly given below.

Question
Use the source composite WRN dependency definition: score < -0.5 means dependent; score >= -0.5 means not classified as dependent. Is SNU1 classified as WRN-dependent?

Options
A. Yes
B. No

Response format
Return only {"answer": "<option letter>"}.

Required response schema:
{"type": "object", "additionalProperties": false, "required": ["answer"], "properties": {"answer": {"type": "string", "enum": ["A", "B"]}}}
