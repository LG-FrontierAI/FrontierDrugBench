---
bench_id: "BX-RET-UKHSA-GPILI-W42"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-UKHSA-GPILI-W42"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T2_quantitative_effect"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-09
[Task background] This task forecasts an infectious disease surveillance indicator. The target is the ILI consultation rate driven by GP care-seeking behavior; it is related to viral positivity but is influenced by care-seeking behavior and the reporting system.

[Question]
Predict the influenza-like illness (ILI) consultation rate reported by general practitioner (GP) practices participating in surveillance in England during week 41 (2026-10-05 to 10-11), per 100,000 registered population (0–50), as will be reported in the UKHSA week 42 report (to be published on the result release date (after the knowledge-lock date)). Provide the seven quantiles q05–q95.

[Information available before the cutoff]
- UKHSA week 41 report (published on 2026-10-08, with data through week 40, i.e., 2026-09-28 to 10-04): influenza activity was increasing and at baseline levels; the rolling 7-day influenza positivity rate through 10-04 was 6.5% (5.0% on the previous Sunday).
- Week 41 report: rolling 7-day positivity was 5.8% for influenza A and 0.4% for influenza B (through 10-04); Respiratory DataMart influenza positivity for week 40 was 5.6% (5.3% in the previous week).
- Week 41 report: the GP ILI consultation rate was 5.6 per 100,000 (week 40).
- Week 41 report: the influenza hospitalization rate was 1.97 per 100,000 (week 40; surveillance formally began in week 40).
- At the same point in the 2025-26 season, influenza positivity was in a similar early-winter rising phase.

[Precollected source excerpts]
- National flu and COVID-19 surveillance report: 8 October 2026 (week 41) (UKHSA, 2026-10-08)
  - ILI general practice (GP) consultations ... 5.6 per 100,000 in the previous week

[Target and adjudication contract]
{
 "target_locator": "UKHSA week 42 report: week 41 ILI consultation rate at participating GP practices.",
 "source_priority": [
  "UKHSA week 42 report (result release date (after the knowledge-lock date))",
  "UKHSA weekly winter virus surveillance report"
 ],
 "note": "The value for the previous week (week 40) was 5.6 per 100,000."
}

[Temporal contract]
{
 "estimand": "GP ILI consultation rate in England during week 41",
 "unit": "per 100,000",
 "value_range": [
  0,
  50
 ],
 "adjudication_source": [
  "UKHSA week 42 report (result release date (after the knowledge-lock date))"
 ]
}

[Output] Return only a JSON array of length 7, ordered as q05, q10, q25, q50, q75, q90, q95. Each value must be between 0 and 50, and the values must be nondecreasing.
Do not include Markdown, explanations, units, or additional fields.
