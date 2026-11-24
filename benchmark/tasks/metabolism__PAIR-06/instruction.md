---
bench_id: "metabolism::PAIR-06"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Pairwise): Panel context Species: Mus musculus. Study ba"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

Panel context
Species: Mus musculus. Study background: C57BL/6N. A targeted gene knockout line is compared with wild-type (WT) controls. The source zygosity is stated for each model; a heterozygote is not a complete biallelic knockout. Every displayed numerical measurement is a dimensionless group-level mutant/WT ratio computed within the stated center and sex. A ratio above 1 means a higher mean than the corresponding WT reference; it is not a significance test. MR and VO2 were adjusted using center- and sex-specific linear-model residuals plus a constant, not by simply dividing by body mass. The study-wide phenotyping window was 4-16 weeks; assay-specific age, allele identifier, sample size, variance, diet, housing temperature, and WT absolute means are not supplied in this ratio table. Do not invent them. NA means an unavailable source measurement, not a normal value. Measurements across procedures need not be from the same individual mouse.

Models
Gene: Dtnbp1; center: TCP; zygosity: homozygote; sex: female.
Gene: Dtnbp1; center: TCP; zygosity: homozygote; sex: male.
Gene: Epha5; center: TCP; zygosity: homozygote; sex: female.
Gene: Epha5; center: TCP; zygosity: homozygote; sex: male.

Metric definitions
AUC: baseline-relative blood-glucose AUC over 0-120 min in the intraperitoneal glucose tolerance test.
T0: basal blood glucose after overnight food deprivation.
TG: non-fasted plasma triglycerides.
BM: body mass (not fat mass or body-fat percentage).

Allowed observations
Epha5 | TCP | homozygote | female | AUC | ratio = 1.401473 | WT reference = 1 (normalized only).
Epha5 | TCP | homozygote | female | T0 | ratio = 1.080182 | WT reference = 1 (normalized only).
Epha5 | TCP | homozygote | female | BM | ratio = 0.951798 | WT reference = 1 (normalized only).
Epha5 | TCP | homozygote | male | TG | ratio = 1.280323 | WT reference = 1 (normalized only).
Dtnbp1 | TCP | homozygote | female | AUC | ratio = 1.377646 | WT reference = 1 (normalized only).
Dtnbp1 | TCP | homozygote | female | T0 | ratio = 1.222283 | WT reference = 1 (normalized only).
Dtnbp1 | TCP | homozygote | female | BM | ratio = 0.922478 | WT reference = 1 (normalized only).
Dtnbp1 | TCP | homozygote | male | TG | ratio = 1.146006 | WT reference = 1 (normalized only).

Masked target records
Epha5 | TCP | homozygote | female | TG = [MASKED].
Dtnbp1 | TCP | homozygote | female | TG = [MASKED].
Predict the held-out recorded outcome using only the allowed observations and general biological knowledge. These covariates do not algebraically determine the target; do not copy a value from another sex or assume it transfers exactly. No external article or database retrieval is allowed.

Question
Which model has the larger recorded TG mutant/WT ratio? Model A is Epha5, female (TCP, homozygote); Model B is Dtnbp1, female (TCP, homozygote). Compare relative responses, not absolute measurements or p-values. Different centers, sexes or zygosities are not a matched causal comparison; there is no tie in the source values.
All numerical decision cutoffs in this question are benchmark-defined descriptive rules, not the paper's percentile cutoffs, clinical diagnostic criteria, or statistical significance thresholds. Do not infer insulin resistance, obesity, or therapeutic benefit from a flag alone.

Options
A. Model B: Dtnbp1, female (TCP, homozygote)
B. Model A: Epha5, female (TCP, homozygote)

Response format
Return only {"answer":"<option letter>"}.

Required response schema:
{"type": "object", "properties": {"answer": {"type": "string", "enum": ["A", "B"]}}, "required": ["answer"], "additionalProperties": false}
