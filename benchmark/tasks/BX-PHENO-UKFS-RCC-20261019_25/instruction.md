---
bench_id: "BX-PHENO-UKFS-RCC-20261019_25"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-PHENO-UKFS-RCC-20261019_25"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T2_quantitative_trajectory"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-15
[Task background] This task involves short-term forecasting of ecosystems or plant phenology. Adhere to the fixed site, variable, time window, units, observational data product, and quality-control rules; the target ground truth is obtained from the prespecified official target file.

[Question]
Predict the arithmetic mean of the valid daily observation values of the red chromatic coordinate in the EFI/NEON phenology ground-truth file for site_id='UKFS', duration='P1D', and variable='rcc_90' over 2026-10-19 to 2026-10-25 (at least 5 of the 7 days must be valid). Use the fixed snapshot at 2026-10-29T18:00:00Z; the unit is a dimensionless 0–1 ratio.

[Information available before the cutoff]
- Phenology targets
- Timing: The phenology targets are at 2 pm UTC. Latency: New data each day is from 1-day prior
- The targets are updated as new NEON data is made available.
- Green chromatic coordinate is the ratio of the green digital number to the sum of the red, green, blue digital numbers from a digital camera.
- Red chromatic coordinate is the ratio of the Red digital number to the sum of the red, green, blue digital numbers from a digital camera.
- Valid historical observations are available; recent_values in the audit contain only past observations, not future ground truth.

[Historical input summary]
{
  "status": "numeric_history_embedded",
  "as_of": "2026-10-15",
  "purpose": "Provide the raw LLM with reproducible historical context available before the cutoff; no ground-truth results for the target period or future results are included.",
  "known_public_facts": [
    "Valid historical observations are available; recent_values in the audit contain only past observations, not future ground truth."
  ],
  "source_metadata": [
    {
      "title": "Timing of Data Availability",
      "url": "https://projects.ecoforecast.org/neon4cast-docs/CronTiming.html",
      "accessed_at": "2026-10-15"
    },
    {
      "title": "What to forecast",
      "url": "https://projects.ecoforecast.org/neon4cast-ci/targets.html",
      "accessed_at": "2026-10-15"
    },
    {
      "title": "phenology public target data",
      "url": "https://sdsc.osn.xsede.org/bio230014-bucket01/challenges/targets/project_id=neon4cast/duration=P1D/phenology-targets.csv.gz",
      "download_sha256": "192b508625f6558420593b793a7f65763ba8c1d47af93eaef57273d658bce8d5",
      "row_count": 367540,
      "latest_observation_date": "2026-10-12T00:00:00Z",
      "columns": [
        "project_id",
        "site_id",
        "datetime",
        "duration",
        "variable",
        "observation"
      ],
      "accessed_at": "2026-10-15T10:06:27.982453+00:00"
    }
  ],
  "numeric_values_included": true,
  "numeric_summary": {
    "n": 14,
    "min": 0.38472,
    "max": 0.41582,
    "mean": 0.3999078571428572,
    "last_observation": {
      "timestamp": "2026-10-12T00:00:00Z",
      "value": 0.41254,
      "unit": "dimensionless [0,1]",
      "missing_flag": false,
      "source_version": "neon_phenology_targets.csv.gz"
    },
    "reference_only": false,
    "freshness_note": "Use only observations from before the cutoff; ground truth for the target period is obtained from an independent adjudication snapshot."
  },
  "recent_observations": [
    {
      "timestamp": "2026-09-29T00:00:00Z",
      "value": 0.40724,
      "unit": "dimensionless [0,1]",
      "missing_flag": false,
      "source_version": "neon_phenology_targets.csv.gz"
    },
    {
      "timestamp": "2026-09-30T00:00:00Z",
      "value": 0.39789,
      "unit": "dimensionless [0,1]",
      "missing_flag": false,
      "source_version": "neon_phenology_targets.csv.gz"
    },
    {
      "timestamp": "2026-10-01T00:00:00Z",
      "value": 0.39346,
      "unit": "dimensionless [0,1]",
      "missing_flag": false,
      "source_version": "neon_phenology_targets.csv.gz"
    },
    {
      "timestamp": "2026-10-02T00:00:00Z",
      "value": 0.38472,
      "unit": "dimensionless [0,1]",
      "missing_flag": false,
      "source_version": "neon_phenology_targets.csv.gz"
    },
    {
      "timestamp": "2026-10-03T00:00:00Z",
      "value": 0.38978,
      "unit": "dimensionless [0,1]",
      "missing_flag": false,
      "source_version": "neon_phenology_targets.csv.gz"
    },
    {
      "timestamp": "2026-10-04T00:00:00Z",
      "value": 0.39096,
      "unit": "dimensionless [0,1]",
      "missing_flag": false,
      "source_version": "neon_phenology_targets.csv.gz"
    },
    {
      "timestamp": "2026-10-05T00:00:00Z",
      "value": 0.393,
      "unit": "dimensionless [0,1]",
      "missing_flag": false,
      "source_version": "neon_phenology_targets.csv.gz"
    },
    {
      "timestamp": "2026-10-06T00:00:00Z",
      "value": 0.397,
      "unit": "dimensionless [0,1]",
      "missing_flag": false,
      "source_version": "neon_phenology_targets.csv.gz"
    },
    {
      "timestamp": "2026-10-07T00:00:00Z",
      "value": 0.40077,
      "unit": "dimensionless [0,1]",
      "missing_flag": false,
      "source_version": "neon_phenology_targets.csv.gz"
    },
    {
      "timestamp": "2026-10-08T00:00:00Z",
      "value": 0.40411,
      "unit": "dimensionless [0,1]",
      "missing_flag": false,
      "source_version": "neon_phenology_targets.csv.gz"
    },
    {
      "timestamp": "2026-10-09T00:00:00Z",
      "value": 0.40476,
      "unit": "dimensionless [0,1]",
      "missing_flag": false,
      "source_version": "neon_phenology_targets.csv.gz"
    },
    {
      "timestamp": "2026-10-10T00:00:00Z",
      "value": 0.40666,
      "unit": "dimensionless [0,1]",
      "missing_flag": false,
      "source_version": "neon_phenology_targets.csv.gz"
    },
    {
      "timestamp": "2026-10-11T00:00:00Z",
      "value": 0.41582,
      "unit": "dimensionless [0,1]",
      "missing_flag": false,
      "source_version": "neon_phenology_targets.csv.gz"
    },
    {
      "timestamp": "2026-10-12T00:00:00Z",
      "value": 0.41254,
      "unit": "dimensionless [0,1]",
      "missing_flag": false,
      "source_version": "neon_phenology_targets.csv.gz"
    }
  ],
  "snapshot_source": {
    "dataset_kind": "neon_phenology",
    "source_url": "https://sdsc.osn.xsede.org/bio230014-bucket01/challenges/targets/project_id=neon4cast/duration=P1D/phenology-targets.csv.gz",
    "local_source_basename": "neon_phenology_targets.csv.gz",
    "sha256": "192b508625f6558420593b793a7f65763ba8c1d47af93eaef57273d658bce8d5",
    "selection": "Filter for the fixed site/region/variable and retain the 14 most recent finite values from before the cutoff; no ground truth for the target period is included."
  },
  "limitation": "The most recent finite observations from before the cutoff are embedded as historical reference data; ground-truth results for the target period are still obtained from an independent adjudication snapshot."
}

[Numeric snapshot as of the knowledge-lock time]
{
  "status": "historical_reference_embedded",
  "required_before_submission": false,
  "available_in_prompt": true,
  "source_url": "https://sdsc.osn.xsede.org/bio230014-bucket01/challenges/targets/project_id=neon4cast/duration=P1D/phenology-targets.csv.gz",
  "target_filter": {
    "project_id": "neon4cast",
    "site_id": "UKFS",
    "duration": "P1D",
    "variable": "rcc_90"
  },
  "value_column": "observation",
  "unit": "dimensionless [0,1]",
  "snapshot_cutoff_field": "knowledge_cutoff",
  "freeze_rule": "Fixed items use only evidence from before the cutoff in historical_context_summary; if numeric historical data are added later, the prompt must be regenerated and its version recorded.",
  "required_fields": [

  ],
  "quality_checks": [

  ],
  "payload": null,
  "missing_snapshot_policy": "The absence of numeric historical data does not automatically invalidate the item; score it according to the existing evidence and target contract.",
  "historical_rows_source": "context.historical_context_summary.recent_observations"
}

[Precollected source excerpts]
- Timing of Data Availability
  - Phenology targets
  - Timing: The phenology targets are at 2 pm UTC. Latency: New data each day is from 1-day prior
- What to forecast
  - The targets are updated as new NEON data is made available.
  - Green chromatic coordinate is the ratio of the green digital number to the sum of the red, green, blue digital numbers from a digital camera.
  - Red chromatic coordinate is the ratio of the Red digital number to the sum of the red, green, blue digital numbers from a digital camera.
- phenology public target data

[Target and adjudication contract]
{
  "extraction_rule": {
    "filter": {
      "project_id": "neon4cast",
      "site_id": "UKFS",
      "duration": "P1D",
      "variable": "rcc_90"
    },
    "inclusive_dates": [
      "2026-10-19",
      "2026-10-25"
    ],
    "value_column": "observation",
    "aggregation": "available_daily_mean",
    "minimum_valid_days": 5,
    "invalid_rows": "The item is unscorable if there are duplicate rows for the same date or finite values outside [0,1]; treat null/NaN as missing and do not impute."
  },
  "version_policy": "The benchmark maintainer must retrieve the complete raw file within the specified cutoff window [18:00,18:05) UTC and record the actual response time, HTTP Last-Modified, SHA256, and immutable archive URL. This capture must be performed for future tasks; no future monitoring was run for this deliverable. If the capture is missed and no corresponding historical version can be verified, the item is unscorable. Later revisions do not replace this snapshot.",
  "missing_or_delay_policy": "If minimum_valid_days is not met at the specified cutoff, or no verifiable snapshot is available, mark the item unscorable; do not wait for missing data to be filled in and then select another snapshot.",
  "public_result_link_required": true
}

[Timing and version contract]
{
  "prediction_deadline_utc": "2026-10-16T23:59:00Z",
  "planned_publication_window_utc": {
    "start": "2026-10-26T14:00:00Z",
    "end": "2026-10-29T18:00:00Z",
    "timezone": "UTC",
    "basis": "verified_daily_cadence",
    "certainty": "approximate_latency",
    "note": "The two official pages specify approximate latencies of 1 day and 2 days; in the observed data, the most recent valid date lagged the access date by approximately 3–4 days. This window includes a 4-day buffer and is a cadence-based plan, not an official daily guarantee."
  },
  "adjudication_deadline_utc": "2026-10-29T18:00:00Z",
  "result_public_time_rule": "Monitor the official result entry points within planned_publication_window; record the exact time when the result first becomes accessible. If publication is delayed, apply missing_or_delay_policy; do not treat a delay as a negative outcome."
}

[Output format] Return only a prediction object conforming to the following JSON schema. Do not include Markdown, explanations, or additional fields:
{
  "json_type": "array",
  "length": 7,
  "quantile_levels_in_order": [
    0.05,
    0.1,
    0.25,
    0.5,
    0.75,
    0.9,
    0.95
  ],
  "value_constraints": {
    "finite": true,
    "nondecreasing": true,
    "lower_bound": 0,
    "upper_bound": 1,
    "lower_exclusive": false
  },
  "example_prediction": null
}

[Scoring contract]
{
  "function_id": "numeric_wis",
  "primary_metric": "wis",
  "direction": "minimize",
  "parameters": {
    "lower_bound": 0,
    "upper_bound": 1,
    "lower_exclusive": false
  },
  "auxiliary_metrics": [
    "median_absolute_error",
    "interval_coverage",
    "interval_width"
  ],
  "coverage_rule": "Score only when a genuine, verifiable scalar ground-truth value is available; a single-item coverage indicator is not an assessment of calibration."
}

Do not independently treat 'not publicly available', 'not disclosed', or 'indeterminate' as a negative outcome; the evaluator obtains the ground-truth result separately under the preregistered public-disclosure rules. Do not use information from after the knowledge cutoff.
