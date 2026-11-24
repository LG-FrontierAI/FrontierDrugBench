---
bench_id: "sexual::PAIR-07"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Pairwise): Use only the stated context and permitted sup"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

Use only the stated context and permitted support. Answer each item in a fresh context without retrieving the original article, full datasets or another item's answers. Keep baseline sex differences, sex-stratified knockout effects and interaction evidence separate.

Panel context
The requested knockout effect is a sex-specific fitted KO-minus-matched-WT contrast, adjusted for body weight under the archived continuous-analysis model. It is not the raw difference between male and female mutant means. The target is e_s = beta_s / D, where D=(WT male mean + WT female mean)/2. This reproduces the Figure-8 normalization: e is a dimensionless ratio, not a percentage, not a standard-deviation unit and not divided by each sex's own WT mean. Positive e means the fitted knockout value is higher than its same-sex WT reference; negative e means lower. Body-weight adjustment defines a conditional association, not an identified total or direct causal effect. Both target-sex coefficients, mutant means, target-trait sex-specific P values, interaction results and outcome annotations are hidden unless explicitly displayed for an interpretation task.
Dataset=USP_HDL; gene=Usp47 (MGI:1922246); colony=Usp47 EPD0676_2_C08-1; allele=Usp47[tm1b(EUCOMM)Wtsi], MGI:5605792 (verified colony crosswalk); zygosity=homozygote; center=NING; background=C57BL/6N (MGI:2159965); pipeline=IMPC_001; parameter=HDL-cholesterol (IMPC_CBC_016_001); metadata group=4ea94b859911e20f2319b9a694f71086. Method=SD continuous pipeline, generalized least squares, equation withWeight; transformation flag=lambda=na, scaleshift=na, transformed=false, code=0. Source counts: male KO=9, female KO=7, male WT=193, female WT=189. WT male mean=83.012834934373; WT female mean=70.7498434864024. Raw units are not supplied here; use only the explicitly defined normalized ratio.

Question
Which sex has the higher signed normalized knockout effect e? The two effects remain hidden.

Options
A. Female
B. Male

Response format
Return a JSON object with a single string field "answer", containing one displayed option letter.

Required response schema:
{"type": "object", "additionalProperties": false, "required": ["answer"], "properties": {"answer": {"type": "string", "enum": ["A", "B"]}}}
