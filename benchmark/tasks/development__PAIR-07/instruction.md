---
bench_id: "development::PAIR-07"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Pairwise): Predict the hidden developmental outcome usin"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

Predict the hidden developmental outcome using the specified knockout line, genotype, stage and explicitly allowed prior observations. Use only the supplied context; do not retrieve the article or answer key. No homozygotes recovered, recovered dead homozygotes, surviving abnormal embryos, and an unassayed stage are different observations. A missing annotation is not a measured normal result. Each question is answered in a fresh context.

Panel context
Morphology is supplied or requested as text, not as images. A figure can illustrate a phenotype without showing its prevalence in every mutant. Sample size alone is not the numerator of a penetrance fraction. An explicit normal observation applies only to the named organ, stage and observation method. A candidate not included in a selected figure-derived finding set is not declared biologically normal in all possible assays.
Compare the examined E9.5 Tmem100 homozygous cardiac cohort and the examined E14.5 Chtop homozygous spinal-ganglion cohort. The specific feature-positive counts are hidden.

Question
Which cohort has the higher reported within-cohort fraction showing its named defect? Do not interpret the cross-organ comparison as a general severity ranking.

Options
A. Chtop E14.5 ganglion-defect cohort
B. Tmem100 E9.5 cardiac-defect cohort

Response format
Return only {"answer": "<option letter>"}.

Required response schema:
{"type": "object", "additionalProperties": false, "required": ["answer"], "properties": {"answer": {"type": "string", "enum": ["A", "B"]}}}
