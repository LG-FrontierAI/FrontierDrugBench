---
bench_id: "BX-RET-FLU-US-HOSP-TX-W42"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-FLU-US-HOSP-TX-W42"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T2_quantitative_effect"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-07
[Task background] This task forecasts an epidemiological surveillance time series. Based on historical data available before the knowledge-lock date, patterns of seasonal increases, reporting delays, and data revisions, provide calibrated quantile forecasts.

[Question]
Predict the number of hospital admissions with confirmed influenza in Texas, United States (FIPS 48), for the week with target_end_date=2026-10-10 (eW 2026-10-10) in the FluSight 2026-27 season (0–5000). Provide the seven quantiles q05–q95.

[Information available before the cutoff]
- The FluSight 2026-27 season launched on 2026-10-07 and requires probabilistic forecasts of weekly hospital admissions with confirmed influenza (NHSN Weekly Hospital Respiratory Dataset) and the proportion of emergency department visits due to influenza.
- The NHSN national hospital admissions series available before the knowledge-lock date (as_of 2026-10-07 snapshot) shows eW 2026-09-26 = 2621 and eW 2026-10-03 = 3246, with a sustained increase since late summer.
- Earlier data (as_of 2026-10-07 snapshot) show national weekly hospital admissions on the order of 2000 for eW 2026-09-19, during the early seasonal increase.
- NHSN data are subject to subsequent revisions: the value for eW 2026-09-26 was progressively revised from 2515 to 2660 across release snapshots.
- At the same point in the 2025-26 season (early October), national weekly hospital admissions were in a rising phase, ranging from several hundred to around two thousand.
- Historical state-level values available before the knowledge-lock date: in early October, weekly hospital admissions in most states were on the order of tens to hundreds, with higher values in more populous states.

[Precollected source excerpts]
- FluSight 2026-2027 forecast hub (CDC / cdcepi, 2026-10-07)
  - This project collects forecasts for weekly new hospital admissions and proportion of emergency department visits due to confirmed influenza.
  - currently planned to begin October 7, 2026

[Target and adjudication contract]
{
 "target_locator": "The observation in the FluSight target-data time series with target=wk inc flu hosp, location=48 (Texas), and target_end_date=2026-10-10.",
 "source_priority": [
  "cdcepi/FluSight-forecast-hub target-data/time-series.csv",
  "NHSN Weekly Hospital Respiratory Dataset"
 ]
}

[Temporal contract]
{
 "estimand": "Number of hospital admissions with confirmed influenza in Texas, United States (FIPS 48), for eW 2026-10-10",
 "unit": "count",
 "value_range": [
  0,
  5000
 ]
}

[Output] Return only a JSON array of length 7, ordered as q05, q10, q25, q50, q75, q90, q95. Each value must be between 0 and 5000, and the values must be nondecreasing.
Do not include Markdown, explanations, units, or additional fields.
