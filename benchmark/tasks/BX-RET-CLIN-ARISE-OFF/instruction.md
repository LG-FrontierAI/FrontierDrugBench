---
bench_id: "BX-RET-CLIN-ARISE-OFF"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-CLIN-ARISE-OFF"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T2_quantitative_effect"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-05
[Task background] This task forecasts a quantitative clinical trial result. Based on the drug's mechanism of action, Phase II signals, the distribution of effect sizes for similar drugs, and statistical power, provide calibrated quantile forecasts for the effect size rather than merely predicting its direction.

[Question]
Predict the placebo-adjusted reduction in mean daily OFF time at Week 12 in the solengepras 150 mg group in the topline results of Cerevance's Phase III ARISE trial (solengepras 150 mg orally once daily as adjunctive treatment for patients with Parkinson's disease and motor fluctuations). The unit is hours, the target is the placebo-adjusted difference, and the range is 0–6 hours. Provide the seven quantiles q05–q95.

[Information available before the cutoff]
- ARISE is a randomized, double-blind, placebo-controlled Phase III trial evaluating oral solengepras 150 mg once daily as adjunctive treatment for patients with Parkinson's disease and motor fluctuations.
- solengepras targets the GPR6 receptor in the striatal indirect pathway and is a potential first-in-class therapy, with no direct action on dopamine receptors.
- The primary endpoint is the change from baseline in mean daily OFF time at Week 12 (placebo-adjusted).
- Similar adjunctive treatments for Parkinson's disease (istradefylline, safinamide, opicapone) typically produce placebo-adjusted reductions in OFF time of 0.3–1.1 hours.
- Publicly available Phase II data have shown a directional signal of reduced OFF time.

[Precollected source excerpts]
- BioX item-development team: summary of information publicly available before the knowledge-lock date (BioX curation, 2026-10-05)
  - ARISE is a randomized, double-blind, placebo-controlled Phase III trial evaluating oral solengepras 150 mg once daily as adjunctive treatment for patients with Parkinson's disease and motor fluctuations.
  - solengepras targets the GPR6 receptor in the striatal indirect pathway and is a potential first-in-class therapy, with no direct action on dopamine receptors.
  - The primary endpoint is the change from baseline in mean daily OFF time at Week 12 (placebo-adjusted).
  - Similar adjunctive treatments for Parkinson's disease (istradefylline, safinamide, opicapone) typically produce placebo-adjusted reductions in OFF time of 0.3–1.1 hours.
  - Publicly available Phase II data have shown a directional signal of reduced OFF time.

[Target and adjudication contract]
{
 "target_locator": "Reduction in mean daily OFF time at Week 12 for the solengepras 150 mg group relative to placebo (placebo-adjusted difference) in the Phase III ARISE topline results press release.",
 "source_priority": [
  "Company topline results press release",
  "Subsequent full results presented at conferences/published in journals (if they conflict with the press release, the press release takes precedence)"
 ],
 "notes": "Use only the comparison between the 150 mg dose group and placebo; do not use the within-group change from baseline."
}

[Temporal contract]
{
 "estimand": "Placebo-adjusted difference in mean daily OFF time at Week 12 (solengepras 150 mg − placebo)",
 "unit": "hours",
 "value_range": [
  0,
  6
 ],
 "adjudication_source": [
  "Company topline results press release"
 ]
}

[Output] Return only a JSON array of length 7, ordered as q05, q10, q25, q50, q75, q90, q95. Each value must be between 0 and 6, and the values must be nondecreasing.
Do not include Markdown, explanations, units, or additional fields.
