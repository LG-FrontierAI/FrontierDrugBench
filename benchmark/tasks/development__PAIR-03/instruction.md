---
bench_id: "development::PAIR-03"
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
These are the paper-specific mouse knockout observations on a C57BL/6N background. Sex and embryo identity are not supplied for individual illustrated cohorts unless explicitly stated; do not invent them. Primary preweaning classes and stage-specific embryo calls are different endpoints. In the primary screen, lethal denotes no homozygous pups recovered after at least 28 pups were assessed; subviable denotes a nonzero recovery fraction below 12.5%. Supplementary Table 5 describes viable as above 12.5%; the exact 12.5% boundary is not resolved here and no boundary-case animal counts are invented. A stage lethal call can reflect absent homozygous embryos or embryos without a heartbeat in the Results definition; this call alone does not distinguish the two. The table legend uses the narrower wording no homozygous animals/embryos, so source labels are retained without reconstructing an unreported mechanism.
Gfpt1 (MGI:95698), allele Gfpt1tm1b(EUCOMM)Wtsi, centre H; gene description: glutamine fructose-6-phosphate transaminase 1. The queried outcome is hidden.
Tmem100 (MGI:1915138), allele Tmem100tm1e.1(KOMP)Wtsi, centre TCP; gene description: transmembrane protein 100. The queried outcome is hidden.

Explicitly allowed support observations:
- Gfpt1 at E9.5: Homozygous - Viable.
- Tmem100 at E9.5: Homozygous - Viable.

Question
Which line has the less severe E12.5 recovery call under viable > subviable > lethal?

Options
A. Gfpt1
B. Tmem100

Response format
Return only {"answer": "<option letter>"}.

Required response schema:
{"type": "object", "additionalProperties": false, "required": ["answer"], "properties": {"answer": {"type": "string", "enum": ["A", "B"]}}}
