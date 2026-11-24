---
bench_id: "BX-RET-UKHSA-FLUPOS-W42"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-UKHSA-FLUPOS-W42"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T2_quantitative_effect"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-09
[Task background] This task forecasts an infectious disease surveillance indicator. Based on the positivity level and trend reported in the previous week, within-week revisions, and seasonal dynamics, provide calibrated quantile forecasts for the following week's rolling 7-day positivity rate.

[Question]
Predict the rolling 7-day influenza PCR positivity rate in England through 2026-10-11 (Sunday) (%, 0–100), as will be reported in the UKHSA week 42 report (to be published on the result release date (after the knowledge-lock date)). Provide the seven quantiles q05–q95.

[Information available before the cutoff]
- UKHSA week 41 report (published on 2026-10-08, with data through week 40, i.e., 2026-09-28 to 10-04): influenza activity was increasing and at baseline levels; the rolling 7-day influenza positivity rate through 10-04 was 6.5% (5.0% on the previous Sunday).
- Week 41 report: rolling 7-day positivity was 5.8% for influenza A and 0.4% for influenza B (through 10-04); Respiratory DataMart influenza positivity for week 40 was 5.6% (5.3% in the previous week).
- Week 41 report: the GP ILI consultation rate was 5.6 per 100,000 (week 40).
- Week 41 report: the influenza hospitalization rate was 1.97 per 100,000 (week 40; surveillance formally began in week 40).
- At the same point in the 2025-26 season, influenza positivity was in a similar early-winter rising phase.

[Precollected source excerpts]
- National flu and COVID-19 surveillance report: 8 October 2026 (week 41) (UKHSA, 2026-10-08)
  - Influenza positivity increased in week 40, with a rolling 7-day positivity rate of 6.5% up to Sunday 4 October 2026. This is compared with 5.0% on the previous Sunday.
  - By type, influenza A positivity increased in week 40, with a rolling 7 day positivity rate of 5.8% up to Sunday 4 October 2026.

[Target and adjudication contract]
{
 "target_locator": "UKHSA week 42 report: rolling 7-day influenza positivity rate in England through 2026-10-11 (Sunday).",
 "source_priority": [
  "UKHSA week 42 report (result release date (after the knowledge-lock date))",
  "UKHSA weekly winter virus surveillance report"
 ],
 "note": "The value for the previous Sunday (10-04) was revised to 6.2% in the week 42 report."
}

[Temporal contract]
{
 "estimand": "Rolling 7-day influenza PCR positivity rate in England (through 2026-10-11)",
 "unit": "percent",
 "value_range": [
  0,
  100
 ],
 "adjudication_source": [
  "UKHSA week 42 report (result release date (after the knowledge-lock date))"
 ]
}

[Output] Return only a JSON array of length 7, ordered as q05, q10, q25, q50, q75, q90, q95. Each value must be between 0 and 100, and the values must be nondecreasing.
Do not include Markdown, explanations, units, or additional fields.
