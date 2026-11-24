---
bench_id: "BX-RET-CLIN-AFFIRM-EM"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-CLIN-AFFIRM-EM"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T2_quantitative_effect"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-09
[Task background] This task forecasts a quantitative clinical trial result. Based on the publicly available Week 12 co-primary endpoint results, the distribution of endoscopic remission rates for similar drugs, and population characteristics, provide calibrated quantile forecasts for the endoscopic remission rate.

[Question]
Predict the proportion of patients achieving endoscopic remission after treatment with subcutaneous SKYRIZI (%, 0–100) in the new data from AbbVie's Phase 3 AFFIRM trial (a subcutaneous SKYRIZI/risankizumab induction regimen for moderately to severely active Crohn's disease) to be presented at the ACG 2026 annual meeting. Provide the seven quantiles q05–q95.

[Information available before the cutoff]
- AFFIRM is a Phase III trial evaluating subcutaneous SKYRIZI (risankizumab) as an induction regimen for moderately to severely active Crohn's disease.
- Superiority on the Week 12 co-primary endpoints (clinical remission and endoscopic response) has previously been publicly reported.
- The new data to be presented at ACG 2026 concern endoscopic remission and ulcer-free endoscopic outcomes.
- SKYRIZI is an IL-23 inhibitor already approved for intravenous induction and subcutaneous maintenance treatment of Crohn's disease.
- Similar biologics (IL-23/IL-12, anti-integrin, anti-TNF) typically achieve endoscopic remission rates of 20%–45% in Crohn's disease.

[Precollected source excerpts]
- BioX item-development team: summary of information publicly available before the knowledge-lock date (BioX curation, 2026-10-09)
  - AFFIRM is a Phase III trial evaluating subcutaneous SKYRIZI (risankizumab) as an induction regimen for moderately to severely active Crohn's disease.
  - Superiority on the Week 12 co-primary endpoints (clinical remission and endoscopic response) has previously been publicly reported.
  - The new data to be presented at ACG 2026 concern endoscopic remission and ulcer-free endoscopic outcomes.
  - SKYRIZI is an IL-23 inhibitor already approved for intravenous induction and subcutaneous maintenance treatment of Crohn's disease.
  - Similar biologics (IL-23/IL-12, anti-integrin, anti-TNF) typically achieve endoscopic remission rates of 20%–45% in Crohn's disease.

[Target and adjudication contract]
{
 "target_locator": "Endoscopic remission rate after treatment with subcutaneous SKYRIZI in the AFFIRM trial, as reported at ACG 2026 (full analysis population).",
 "source_priority": [
  "Company press release",
  "ACG 2026 abstract/presentation"
 ],
 "notes": "Use the value for the overall population, not a subgroup value."
}

[Temporal contract]
{
 "estimand": "Endoscopic remission rate after treatment with subcutaneous SKYRIZI (full analysis population)",
 "unit": "percent",
 "value_range": [
  0,
  100
 ],
 "adjudication_source": [
  "Company press release",
  "ACG 2026 presentation"
 ]
}

[Output] Return only a JSON array of length 7, ordered as q05, q10, q25, q50, q75, q90, q95. Each value must be between 0 and 100, and the values must be nondecreasing.
Do not include Markdown, explanations, units, or additional fields.
