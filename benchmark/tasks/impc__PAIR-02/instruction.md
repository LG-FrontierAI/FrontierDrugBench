---
bench_id: "impc::PAIR-02"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Pairwise): Predict the hidden result from the stated bac"
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
Pink1; MGI=MGI:1916193; allele=Pink1[tm1b(EUCOMM)Wtsi]; colony=H-PINK1-G02-TM1B; center=MRC Harwell; sex=male; zygosity=homozygote (HOM). Readout scope: bone-mineral-density report value. The same source-row WT mean is 0.05491535812672176 in the report's unspecified native scale. Reported counts: WT=1452, HOM=9. Record date range: Mon Oct 20 01:00:00 BST 2014 to Tue Oct 28 00:00:00 GMT 2014. The summary does not establish that this range also defines the control-selection window.
Rcc2; MGI=MGI:1919784; allele=Rcc2[tm1b(EUCOMM)Wtsi]; colony=H-RCC2-B10-TM1B; center=MRC Harwell; sex=male; zygosity=homozygote (HOM). Readout scope: bone-mineral-density report value. The same source-row WT mean is 0.05491535812672176 in the report's unspecified native scale. Reported counts: WT=1452, HOM=8. Record date range: Mon Jun 29 01:00:00 BST 2015 to Wed Sep 02 01:00:00 BST 2015. The summary does not establish that this range also defines the control-selection window.

Question
Which model has the larger absolute descriptive contrast |R|?

Options
A. Pink1
B. Rcc2

Response format
Return a JSON object with the single string field "answer", set to one of the displayed option letters.

Required response schema:
{"type": "object", "additionalProperties": false, "required": ["answer"], "properties": {"answer": {"type": "string", "enum": ["A", "B"]}}}
