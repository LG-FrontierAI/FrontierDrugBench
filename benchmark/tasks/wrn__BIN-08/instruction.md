---
bench_id: "wrn::BIN-08"
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
Baseline MSS reference ranges (bp): NR-21=94-101; BAT-26=103-115; BAT-25=114-124; NR-24=130-133; MONO-27=142-154. These are molecular input features, not intervention-response labels.
MFE-280, endometrial carcinoma: microsatellite main-peak lengths in bp are NR-21=99.6; BAT-26=113.4; BAT-25=122.6; NR-24=131.1; MONO-27=148.9. Source identity QC reports 'Near full' STR concordance, not an unqualified full match.
The validation endpoint is CellTiter-Glo relative cell viability seven days after siRNA transfection, normalized to each model's non-targeting siRNA control (NTC=100%). WRN siRNA #1 is one specific WRN-targeting reagent; PLK1 siRNA is a separate mitotic-kinase perturbation, not another WRN reagent. The plotted summaries are means +/- SD from three independent experiments. Only unambiguous threshold sides and rankings are requested, not exact bar heights.

Question
Predict whether WRN siRNA #1 reduces the mean relative viability below 50% of NTC. This is the item's operational definition of a strong response.

Options
A. No
B. Yes

Response format
Return only {"answer": "<option letter>"}.

Required response schema:
{"type": "object", "additionalProperties": false, "required": ["answer"], "properties": {"answer": {"type": "string", "enum": ["A", "B"]}}}
