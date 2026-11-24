---
bench_id: "BX-UKHSA-RSV-U5-2026W43"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-UKHSA-RSV-U5-2026W43"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T2_quantitative_effect"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-15
[Task background] This task forecasts a population health or infectious disease surveillance indicator. Adhere to the reference week, region, denominator, metric definition, release version, and revision-freezing rules; do not mix different weeks, age groups, or surveillance definitions.

[Question]
Predict the rate of new RSV hospital admissions excluding ICU/HDU admissions among children under 5 years of age in England for data week 2026 week 43 (19–25 October), per 100,000 population in the catchment areas of NHS trusts reporting that week, as reported in the UKHSA week 44 report scheduled for publication on 2026-10-29. Use the SARI Watch value in the first public release of that report, not subsequent revisions.

[Information available before the cutoff]
- 29 October 2026 2:00pm (provisional)
- These statistics will be released on 29 October 2026 2:00pm
- The flu, COVID-19 and RSV surveillance report and the national norovirus and rotavirus surveillance reports: 2026 to 2027 season are published weekly.
- SARI Watch data is provisional and subject to retrospective updates.
- Rates are presented per 100,000 trust catchment population.
- RSV hospitalisations, excluding ICU or HDU admissions, in week 40 2026 were based on 14 sentinel NHS trusts in England:
- The denominator is the population covered by the institutions reporting that week and may change as institutional reporting varies.

[Historical input summary]
{
  "status": "evidence_summary",
  "as_of": "2026-10-15",
  "purpose": "Provide the raw LLM with reproducible historical context available before the cutoff; no ground-truth results for the target period or future results are included.",
  "known_public_facts": [
    "The denominator is the population covered by the institutions reporting that week and may change as institutional reporting varies."
  ],
  "source_metadata": [
    {
      "title": "National flu and COVID-19 surveillance report, week 44: official statistics announcement",
      "url": "https://www.gov.uk/government/statistics/announcements/national-flu-and-covid-19-surveillance-report-week-44-report-data-to-week-43-data-up-to-25-october-2026",
      "accessed_at": "2026-10-15"
    },
    {
      "title": "Latest UKHSA weekly winter virus surveillance data",
      "url": "https://www.gov.uk/government/news/latest-ukhsa-weekly-winter-virus-surveillance-data",
      "accessed_at": "2026-10-15"
    },
    {
      "title": "National flu and COVID-19 surveillance report: 8 October 2026 (week 41)",
      "url": "https://www.gov.uk/government/statistics/national-flu-and-covid-19-surveillance-reports-2026-to-2027-season/national-flu-and-covid-19-surveillance-report-8-october-2026-week-41",
      "accessed_at": "2026-10-15"
    }
  ],
  "numeric_values_included": false,
  "numeric_summary": null,
  "recent_observations": [

  ],
  "snapshot_source": null,
  "limitation": "This is a fixed task based on clinical/registry evidence, with no definable uniform historical observation series; publicly available evidence from before the cutoff has been summarized."
}

[Numeric snapshot as of the knowledge-lock time]
{
  "status": "not_embedded_or_not_applicable",
  "required_before_submission": false,
  "available_in_prompt": false,
  "source_url": "https://www.gov.uk/government/statistics/announcements/national-flu-and-covid-19-surveillance-report-week-44-report-data-to-week-43-data-up-to-25-october-2026",
  "target_filter": null,
  "value_column": "value",
  "unit": null,
  "snapshot_cutoff_field": "knowledge_cutoff",
  "freeze_rule": "Fixed items use only evidence from before the cutoff in historical_context_summary; if numeric historical data are added later, the prompt must be regenerated and its version recorded.",
  "required_fields": [

  ],
  "quality_checks": [

  ],
  "payload": null,
  "missing_snapshot_policy": "The absence of numeric historical data does not automatically invalidate the item; score it according to the existing evidence and target contract."
}

[Precollected source excerpts]
- National flu and COVID-19 surveillance report, week 44: official statistics announcement
  - 29 October 2026 2:00pm (provisional)
  - These statistics will be released on 29 October 2026 2:00pm
- Latest UKHSA weekly winter virus surveillance data
  - The flu, COVID-19 and RSV surveillance report and the national norovirus and rotavirus surveillance reports: 2026 to 2027 season are published weekly.
- National flu and COVID-19 surveillance report: 8 October 2026 (week 41)
  - SARI Watch data is provisional and subject to retrospective updates.
  - Rates are presented per 100,000 trust catchment population.
  - RSV hospitalisations, excluding ICU or HDU admissions, in week 40 2026 were based on 14 sentinel NHS trusts in England:

[Target and adjudication contract]
{
  "extraction_rule": {
    "locate": "Find the week 44 report with data to week 43 (up to 25 October 2026) in the collection/announcement; do not invent a future URL by extrapolating from the date.",
    "section": "RSV hospital admissions",
    "metric": {
      "virus": "RSV",
      "age_group": "under_5_years",
      "care_levels": "excluding_ICU_HDU"
    },
    "selection": "Use the hospitalization rate for the specified week and age group in the main HTML text of the first release of the report; if it is provided only in that report's supplementary data, read the corresponding table row. Do not substitute ICU/HDU rates, positivity, or the previous week's rate.",
    "unit_conversion": "None; use the rate per 100,000 in the main text/table."
  },
  "version_policy": "Freeze the first publicly released HTML/accompanying table for this report and archive the files and SHA256; later silent corrections or retrospective updates do not replace the first snapshot. If the initial version cannot be verified, do not use the current webpage to retrospectively establish the initial value.",
  "missing_or_delay_policy": "If publication on the 29th is delayed, score only if the first official report for the same specified data week is located before adjudication on 5 November; record the actual public release date and mark actual delivery within two weeks as false. Do not score if the target metric is missing.",
  "public_result_link_required": true
}

[Timing and version contract]
{
  "prediction_deadline_utc": "2026-10-16T23:59:00Z",
  "planned_publication_window_utc": {
    "start": "2026-10-29T14:00:00Z",
    "end": "2026-10-29T23:59:59Z",
    "timezone": "UTC",
    "basis": "verified_weekly_cadence_and_official_dated_notice",
    "certainty": "dated_notice_provisional",
    "note": "The official release date and time of 14:00 UK time on the 29th are marked provisional; the weekly release cadence is separately confirmed by an official source. London is on GMT on 29 October, so the time is 14:00 UTC; publication on schedule is not guaranteed."
  },
  "adjudication_deadline_utc": "2026-11-05T23:59:59Z",
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
    "upper_bound": null,
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
    "upper_bound": null,
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
