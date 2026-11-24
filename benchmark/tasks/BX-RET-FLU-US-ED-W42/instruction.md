---
bench_id: "BX-RET-FLU-US-ED-W42"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-FLU-US-ED-W42"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T2_quantitative_effect"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-07
[Task background] This task forecasts an epidemiological surveillance time series. The target is a proportion (the proportion of emergency department visits due to influenza), which is related to the hospital admissions series but differs in data source and units of measurement.

[Question]
Predict the proportion of emergency department visits due to confirmed influenza nationwide in the United States for the week with target_end_date=2026-10-10 (eW 2026-10-10) in the FluSight 2026-27 season (proportion, 0–0.1). Provide the seven quantiles q05–q95.

[Information available before the cutoff]
- The FluSight 2026-27 season launched on 2026-10-07 and includes a forecast target for the weekly proportion of emergency department visits due to influenza.
- The national ED proportion series available before the knowledge-lock date (as_of 2026-10-07 snapshot) shows eW 2026-09-26 = 0.0046 and eW 2026-10-03 = 0.0060, with a sustained increase.
- NHSN ED data are subject to reporting delays and revisions similar to those in the hospital admissions data.

[Precollected source excerpts]
- FluSight 2026-2027 forecast hub (CDC / cdcepi, 2026-10-07)
  - weekly proportion of emergency department visits due to influenza (for locations with sufficient data)

[Target and adjudication contract]
{
 "target_locator": "The observation in the FluSight target-data time series with target=wk inc flu prop ed visits, location=US (US (nationwide)), and target_end_date=2026-10-10.",
 "source_priority": [
  "cdcepi/FluSight-forecast-hub target-data/time-series.csv",
  "NHSN Weekly Hospital Respiratory Dataset"
 ]
}

[Temporal contract]
{
 "estimand": "Proportion of emergency department visits due to confirmed influenza nationwide in the United States for eW 2026-10-10",
 "unit": "proportion",
 "value_range": [
  0,
  0.1
 ]
}

[Output] Return only a JSON array of length 7, ordered as q05, q10, q25, q50, q75, q90, q95. Each value must be between 0 and 0.1, and the values must be nondecreasing.
Do not include Markdown, explanations, units, or additional fields.
