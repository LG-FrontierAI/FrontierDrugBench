---
bench_id: "BX-FLU-ED-20261024"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-FLU-ED-20261024"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T2_quantitative_effect"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-15
[Task background] This task forecasts a population health or infectious disease surveillance indicator. Adhere to the reference week, region, denominator, metric definition, release version, and revision-freezing rules; do not mix different weeks, age groups, or surveillance definitions.

[Question]
Predict the proportion of all emergency department visits that are influenza-related in the U.S. FluSight ground-truth file for 2026-10-18 to 2026-10-24 (CDC epidemiological week, Sunday through Saturday), location='US'. Use the fixed file version as of 2026-10-29T18:00:00Z, not the final value after subsequent revisions.

[Information available before the cutoff]
- These data are released weekly.
- Preliminary counts are released on Wednesdays.
- Official counts can be revised in subsequent data updates.
- A set of comma-separated plain text files are automatically updated every week with the latest observed values for incident hospitalizations and emergency department visits.
- After this date, the as_of variable indicates the date of data release, typically the Wednesday following the reference_date.
- The historical series can be used as training data; future targets are not present in the downloaded file.
- Target unit: proportion in [0,1]

[Historical input summary]
{
  "status": "numeric_history_embedded",
  "as_of": "2026-10-15",
  "purpose": "Provide the raw LLM with reproducible historical context available before the cutoff; no ground-truth results for the target period or future results are included.",
  "known_public_facts": [
    "The historical series can be used as training data; future targets are not present in the downloaded file."
  ],
  "source_metadata": [
    {
      "title": "FluSight target-data README",
      "url": "https://github.com/cdcepi/FluSight-forecast-hub/blob/main/target-data/README.md",
      "accessed_at": "2026-10-15"
    },
    {
      "title": "flu_ed public target data",
      "url": "https://raw.githubusercontent.com/cdcepi/FluSight-forecast-hub/main/target-data/target-ed-visits-prop.csv",
      "download_sha256": "d75d15450e52f022d1265a2a8a8287e016658a94a4915c51f7f8a31fce983ec8",
      "row_count": 10972,
      "latest_observation_date": "2026-10-10",
      "columns": [
        "date",
        "location_name",
        "value",
        "location"
      ],
      "accessed_at": "2026-10-15T10:06:26.391096+00:00"
    }
  ],
  "numeric_values_included": true,
  "numeric_summary": {
    "n": 14,
    "min": 0.0008,
    "max": 0.0075,
    "mean": 0.0024214285714285713,
    "last_observation": {
      "timestamp": "2026-10-10",
      "value": 0.0075,
      "unit": "proportion in [0,1]",
      "missing_flag": false,
      "source_version": "target-ed-visits-prop.csv"
    },
    "reference_only": false,
    "freshness_note": "Use only observations from before the cutoff; ground truth for the target period is obtained from an independent adjudication snapshot."
  },
  "recent_observations": [
    {
      "timestamp": "2026-07-11",
      "value": 0.0008,
      "unit": "proportion in [0,1]",
      "missing_flag": false,
      "source_version": "target-ed-visits-prop.csv"
    },
    {
      "timestamp": "2026-07-18",
      "value": 0.0008,
      "unit": "proportion in [0,1]",
      "missing_flag": false,
      "source_version": "target-ed-visits-prop.csv"
    },
    {
      "timestamp": "2026-07-25",
      "value": 0.0008,
      "unit": "proportion in [0,1]",
      "missing_flag": false,
      "source_version": "target-ed-visits-prop.csv"
    },
    {
      "timestamp": "2026-08-01",
      "value": 0.0008,
      "unit": "proportion in [0,1]",
      "missing_flag": false,
      "source_version": "target-ed-visits-prop.csv"
    },
    {
      "timestamp": "2026-08-08",
      "value": 0.0009,
      "unit": "proportion in [0,1]",
      "missing_flag": false,
      "source_version": "target-ed-visits-prop.csv"
    },
    {
      "timestamp": "2026-08-15",
      "value": 0.001,
      "unit": "proportion in [0,1]",
      "missing_flag": false,
      "source_version": "target-ed-visits-prop.csv"
    },
    {
      "timestamp": "2026-08-22",
      "value": 0.0012,
      "unit": "proportion in [0,1]",
      "missing_flag": false,
      "source_version": "target-ed-visits-prop.csv"
    },
    {
      "timestamp": "2026-08-29",
      "value": 0.0016,
      "unit": "proportion in [0,1]",
      "missing_flag": false,
      "source_version": "target-ed-visits-prop.csv"
    },
    {
      "timestamp": "2026-09-05",
      "value": 0.002,
      "unit": "proportion in [0,1]",
      "missing_flag": false,
      "source_version": "target-ed-visits-prop.csv"
    },
    {
      "timestamp": "2026-09-12",
      "value": 0.0026,
      "unit": "proportion in [0,1]",
      "missing_flag": false,
      "source_version": "target-ed-visits-prop.csv"
    },
    {
      "timestamp": "2026-09-19",
      "value": 0.0033,
      "unit": "proportion in [0,1]",
      "missing_flag": false,
      "source_version": "target-ed-visits-prop.csv"
    },
    {
      "timestamp": "2026-09-26",
      "value": 0.0046,
      "unit": "proportion in [0,1]",
      "missing_flag": false,
      "source_version": "target-ed-visits-prop.csv"
    },
    {
      "timestamp": "2026-10-03",
      "value": 0.006,
      "unit": "proportion in [0,1]",
      "missing_flag": false,
      "source_version": "target-ed-visits-prop.csv"
    },
    {
      "timestamp": "2026-10-10",
      "value": 0.0075,
      "unit": "proportion in [0,1]",
      "missing_flag": false,
      "source_version": "target-ed-visits-prop.csv"
    }
  ],
  "snapshot_source": {
    "dataset_kind": "flusight_ed",
    "source_url": "https://raw.githubusercontent.com/cdcepi/FluSight-forecast-hub/main/target-data/target-ed-visits-prop.csv",
    "local_source_basename": "target-ed-visits-prop.csv",
    "sha256": "d75d15450e52f022d1265a2a8a8287e016658a94a4915c51f7f8a31fce983ec8",
    "selection": "Filter for the fixed site/region/variable and retain the 14 most recent finite values from before the cutoff; no ground truth for the target period is included."
  },
  "limitation": "The most recent finite observations from before the cutoff are embedded as historical reference data; ground-truth results for the target period are still obtained from an independent adjudication snapshot."
}

[Numeric snapshot as of the knowledge-lock time]
{
  "status": "historical_reference_embedded",
  "required_before_submission": false,
  "available_in_prompt": true,
  "source_url": "https://raw.githubusercontent.com/cdcepi/FluSight-forecast-hub/main/target-data/target-ed-visits-prop.csv",
  "target_filter": null,
  "value_column": "value",
  "unit": "proportion in [0,1]",
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
- FluSight target-data README
  - These data are released weekly.
  - Preliminary counts are released on Wednesdays.
  - Official counts can be revised in subsequent data updates.
  - A set of comma-separated plain text files are automatically updated every week with the latest observed values for incident hospitalizations and emergency department visits.
  - After this date, the as_of variable indicates the date of data release, typically the Wednesday following the reference_date.
- flu_ed public target data

[Target and adjudication contract]
{
  "extraction_rule": {
    "dataset": "flu_ed",
    "row_filter": {
      "target_end_date": "2026-10-24",
      "location": "US"
    },
    "value_column": "value",
    "expected_rows": 1,
    "transform": "identity; value is a decimal proportion in [0,1]; do not multiply or divide by 100.",
    "field_contract": {
      "required_columns": [
        "target_end_date",
        "location",
        "value"
      ],
      "target_date_column": "target_end_date",
      "release_version_column": "as_of",
      "value_column": "value"
    }
  },
  "version_policy": "Freeze the latest qualifying file version at or before 2026-10-29T18:00:00Z; save commit SHA, file SHA256, and as_of. If the target_end_date/location row is absent, duplicated, or the required fields are unavailable, mark unscorable.",
  "missing_or_delay_policy": "If the target_end_date=2026-10-24, location=US row is absent at the frozen cutoff, or the row has invalid fields, mark unscorable; do not backfill from a later revision.",
  "public_result_link_required": true,
  "truth_version": {
    "dataset_url": "https://raw.githubusercontent.com/cdcepi/FluSight-forecast-hub/main/target-data/target-ed-visits-prop.csv",
    "snapshot_cutoff_utc": "2026-10-29T18:00:00Z",
    "selection": "Select the latest Git commit at or before snapshot_cutoff_utc; freeze commit SHA, file SHA256, and the as_of value in the adjudication record.",
    "later_revisions": "Do not replace the first frozen release with later revisions; report revision sensitivity separately."
  },
  "unit": "proportion in [0,1]",
  "field_contract": {
    "required_columns": [
      "target_end_date",
      "location",
      "value"
    ],
    "target_date_column": "target_end_date",
    "release_version_column": "as_of",
    "value_column": "value"
  }
}

[Timing and version contract]
{
  "prediction_deadline_utc": "2026-10-16T23:59:00Z",
  "planned_publication_window_utc": {
    "start": "2026-10-28T00:00:00Z",
    "end": "2026-10-28T23:59:59Z",
    "timezone": "UTC",
    "basis": "verified_weekly_cadence",
    "certainty": "planned_not_guaranteed",
    "note": "The planned schedule follows the Wednesday preliminary-data/Hub update cadence; official Friday hospitalization counts and subsequent revisions do not replace the fixed version specified for this item."
  },
  "adjudication_deadline_utc": "2026-10-29T18:00:00Z",
  "result_public_time_rule": "At the pre-registered snapshot cutoff, freeze the latest public target-data commit and record its as_of release date. The locator URL is not itself the truth release."
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
