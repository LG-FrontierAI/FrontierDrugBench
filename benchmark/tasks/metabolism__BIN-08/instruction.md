---
bench_id: "metabolism::BIN-08"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Binary): Panel context Species: Mus musculus. Study ba"
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
Gene: Rnf144b; center: ICS; zygosity: homozygote; sex: female.
Gene: Rnf144b; center: ICS; zygosity: homozygote; sex: male.

Metric definitions
AUC: baseline-relative blood-glucose AUC over 0-120 min in the intraperitoneal glucose tolerance test.
T0: basal blood glucose after overnight food deprivation.
RER: respiratory exchange ratio (VCO2/VO2); the displayed number is the mutant/WT ratio of RER, not absolute RER.
MR: body-mass-adjusted metabolic rate (residual-plus-constant method).
TG: non-fasted plasma triglycerides.
BM: body mass (not fat mass or body-fat percentage).

Allowed observations
Rnf144b | ICS | homozygote | female | MR | ratio = 0.825807 | WT reference = 1 (normalized only).
Rnf144b | ICS | homozygote | female | BM | ratio = 0.960688 | WT reference = 1 (normalized only).
Rnf144b | ICS | homozygote | female | RER | ratio = 1.052311 | WT reference = 1 (normalized only).
Rnf144b | ICS | homozygote | male | AUC | ratio = 0.967692 | WT reference = 1 (normalized only).
Rnf144b | ICS | homozygote | male | T0 | ratio = 1.004316 | WT reference = 1 (normalized only).
Rnf144b | ICS | homozygote | male | RER | ratio = 1.084158 | WT reference = 1 (normalized only).
Rnf144b | ICS | homozygote | male | TG | ratio = 0.820704 | WT reference = 1 (normalized only).
Rnf144b | ICS | homozygote | male | BM | ratio = 0.881745 | WT reference = 1 (normalized only).

Masked target records
Rnf144b | ICS | homozygote | male | MR = [MASKED].
Predict the held-out recorded outcome using only the allowed observations and general biological knowledge. These covariates do not algebraically determine the target; do not copy a value from another sex or assume it transfers exactly. No external article or database retrieval is allowed.

Question
Will the masked male Rnf144b metabolic-rate ratio meet MR < 0.90?
All numerical decision cutoffs in this question are benchmark-defined descriptive rules, not the paper's percentile cutoffs, clinical diagnostic criteria, or statistical significance thresholds. Do not infer insulin resistance, obesity, or therapeutic benefit from a flag alone.

Options
A. No
B. Yes

Response format
Return only {"answer":"<option letter>"}.

Required response schema:
{"type": "object", "properties": {"answer": {"type": "string", "enum": ["A", "B"]}}, "required": ["answer"], "additionalProperties": false}
