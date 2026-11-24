---
bench_id: "BX-RET-CLIN-GALAXI-W144-CR"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-CLIN-GALAXI-W144-CR"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T2_quantitative_effect"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-09
[Task background] This task forecasts a quantitative clinical trial result. Based on publicly available Week 12 data, survivor bias in long-term extension studies, and general patterns of remission rates during maintenance treatment, provide calibrated quantile forecasts for the Week 144 clinical remission rate.

[Question]
Predict the proportion of patients achieving clinical remission (%, 0–100) in the TREMFYA (guselkumab) 100 mg q8w maintenance group in the Week 144 data from Janssen/J&J's Phase 3 GALAXI 2/3 long-term extension study (to be presented at ACG 2026). Provide the seven quantiles q05–q95.

[Information available before the cutoff]
- GALAXI is a randomized, double-blind, placebo-controlled and active-controlled (ustekinumab) Phase 2/3 program (NCT03466411).
- The ACG 2026 presentation covers Week 144 long-term extension data for two maintenance regimens: 100 mg q8w and 200 mg q4w.
- The main reported endpoints include clinical remission, corticosteroid-free clinical remission, and endoscopic remission.
- Survivor bias in long-term extension studies generally increases observed remission rates; TREMFYA is already approved for Crohn's disease.

[Precollected source excerpts]
- BioX item-development team: summary of information publicly available before the knowledge-lock date (BioX curation, 2026-10-09)
  - GALAXI is a randomized, double-blind, placebo-controlled and active-controlled (ustekinumab) Phase 2/3 program (NCT03466411).
  - The ACG 2026 presentation covers Week 144 long-term extension data for two maintenance regimens: 100 mg q8w and 200 mg q4w.
  - The main reported endpoints include clinical remission, corticosteroid-free clinical remission, and endoscopic remission.
  - Survivor bias in long-term extension studies generally increases observed remission rates; TREMFYA is already approved for Crohn's disease.

[Target and adjudication contract]
{
 "target_locator": "Clinical remission rate at Week 144 in the TREMFYA 100 mg q8w maintenance group in the GALAXI 2/3 LTE.",
 "source_priority": [
  "Company press release",
  "ACG 2026 abstract"
 ],
 "notes": "Use the value for the 100 mg q8w group; do not use the value for the 200 mg q4w group or the corticosteroid-free remission rate."
}

[Temporal contract]
{
 "estimand": "Clinical remission rate at Week 144 in the TREMFYA 100 mg q8w maintenance group",
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
