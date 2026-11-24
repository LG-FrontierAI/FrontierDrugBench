---
bench_id: "impc::PAIR-08"
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
This is a frozen genotype-to-Mammalian-Phenotype (MP) annotation panel from the supplied IMPC archive. The target is the recorded effect direction or the set of recorded MP terms for the specified allele, colony, zygosity and sex. Some identical statistical estimates are exported for both sexes; duplicated rows are not independent evidence and are not treated as proof of a sex-specific effect. The source percentage_change field, where compared, is the exported statistical-result field and is not a raw mutant/control mean ratio. Unlisted or unobserved annotations do not prove biological normality; no absence-of-effect label is created from missing rows.
Gene=Fam53b; allele=Fam53b[tm1b(EUCOMM)Hmgu]; colony=Monterotondo-HEPD0667_7_D08-1-1; center=HMGU; sex=female; zygosity=homozygote; strain=C57BL/6NTac. Measured parameter=Red blood cell count (IMPC_HEM_002_001); procedure=Hematology. Except for annotations explicitly revealed as support, outcome terms are withheld; source numeric effects, percentage_change and P values are not shown.
Gene=Rxfp2; allele=Rxfp2[tm1b(EUCOMM)Wtsi]; colony=GSF-EPD0243_5_D11-1-1; center=HMGU; sex=female; zygosity=homozygote; strain=C57BL/6NTac. Measured parameter=Red blood cell count (IMPC_HEM_002_001); procedure=Hematology. Except for annotations explicitly revealed as support, outcome terms are withheld; source numeric effects, percentage_change and P values are not shown.

Question
Which model has the lower signed percentage_change value in this frozen annotation export? Compare the same source field and parameter, not raw KO/WT ratios or cross-parameter physical effects.

Options
A. Rxfp2
B. Fam53b

Response format
Return a JSON object with the single string field "answer", set to one of the displayed option letters.

Required response schema:
{"type": "object", "additionalProperties": false, "required": ["answer"], "properties": {"answer": {"type": "string", "enum": ["A", "B"]}}}
