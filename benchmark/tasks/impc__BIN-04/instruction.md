---
bench_id: "impc::BIN-04"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Binary): Predict the hidden result from the stated bac"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

Predict the hidden result from the stated background and explicitly permitted support. Use a fresh context for each item, with no access to the source files or answer key. Do not interpret a statistical, descriptive or matching endpoint as a different kind of biological evidence.

Panel context
This panel predicts a descriptive archive-report target, not the fitted PhenStat effect used for formal phenotype calling. Define R = 100 * (the same-row, same-sex reported HOM mean / reported WT mean - 1). Positive R means a higher exported mutant mean; negative R means a lower mean. The measurement unit, protocol version, per-row QC status and adjustment model are not supplied in these summaries. Do not invent them. A ratio is used only within a source row and does not establish cross-center experimental equivalence. The reported N fields are source counts, not independently verified unique animal counts; no new P value, standard error or confidence interval is implied. The target HOM mean, median, SD, opposite-sex result and target-derived phenotype annotations are hidden. This is prediction, not arithmetic from a revealed HOM mean.
Nudt14; MGI=MGI:1913424; allele=Nudt14[tm1.1(KOMP)Vlcg]; colony=BL2301; center=UC Davis; sex=female; zygosity=homozygote (HOM). Readout scope: glucose-concentration report value. The same source-row WT mean is 117.97894736842106 in the report's unspecified native scale. Reported counts: WT=665, HOM=8. Record date range: Thu Mar 14 00:00:00 GMT 2013 to Tue Mar 26 00:00:00 GMT 2013. The summary does not establish that this range also defines the control-selection window.

Explicitly allowed support observations:
- Slc41a1 (female, HOM, UC Davis): observed descriptive R=-22.125937%.
- Mtnr1b (female, HOM, UC Davis): observed descriptive R=25.203936%.

Question
Predict whether R is negative: is the source-row HOM mean lower than the same-sex WT mean? This does not ask whether a significant abnormality was called.

Options
A. No, R >= 0
B. Yes, R < 0

Response format
Return a JSON object with the single string field "answer", set to one of the displayed option letters.

Required response schema:
{"type": "object", "additionalProperties": false, "required": ["answer"], "properties": {"answer": {"type": "string", "enum": ["A", "B"]}}}
