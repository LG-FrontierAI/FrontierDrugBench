---
bench_id: "BX-RET-CLIN-EXCALIBER-PFS"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-CLIN-EXCALIBER-PFS"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T1_outcome_probability"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-05
[Task background] This task forecasts the probability of clinical trial success. Based on the MRD evidence supporting accelerated approval, signals from CELMoD-class agents, the comparator regimen, and general success rates for confirmatory trials, estimate the probability of meeting the primary PFS endpoint.

[Question]
Will Bristol Myers Squibb's Phase III EXCALIBER-RRMM trial (iberdomide in combination with daratumumab and dexamethasone versus daratumumab and dexamethasone for relapsed/refractory multiple myeloma) meet the primary PFS endpoint with statistical significance? Y=1 denotes that the endpoint is met; Y=0 denotes that it is not met or that achievement is not announced.

[Information available before the cutoff]
- EXCALIBER-RRMM is a Phase III confirmatory trial comparing the oral CELMoD agent iberdomide (ZENBEXUS) in combination with daratumumab and dexamethasone versus daratumumab and dexamethasone for relapsed/refractory multiple myeloma.
- iberdomide received U.S. accelerated approval in 2026-08 based on an MRD-negativity endpoint; this trial is intended to verify clinical benefit.
- The primary endpoint is PFS.
- A previous me-too combination (daratumumab + pomalidomide + dex, APOLLO) demonstrated a PFS benefit in a similar population.

[Precollected source excerpts]
- BioX item-development team: summary of information publicly available before the knowledge-lock date (BioX curation, 2026-10-05)
  - EXCALIBER-RRMM is a Phase III confirmatory trial comparing the oral CELMoD agent iberdomide (ZENBEXUS) in combination with daratumumab and dexamethasone versus daratumumab and dexamethasone for relapsed/refractory multiple myeloma.
  - iberdomide received U.S. accelerated approval in 2026-08 based on an MRD-negativity endpoint; this trial is intended to verify clinical benefit.
  - The primary endpoint is PFS.
  - A previous me-too combination (daratumumab + pomalidomide + dex, APOLLO) demonstrated a PFS benefit in a similar population.

[Target and adjudication contract]
{
 "Y_definition": "Y=1 if and only if the company announces by 2026-10-16T23:59:59Z that EXCALIBER-RRMM met the primary PFS endpoint with statistical significance; an announcement that the endpoint was not met, a delay without an announcement, or no action is scored as Y=0.",
 "source_priority": [
  "Company topline results press release",
  "Authoritative secondary reporting (with the date specified)"
 ],
 "notes": "This item concerns only whether the primary endpoint was met; it does not ask for the HR value (the specific value was not disclosed in the topline results)."
}

[Temporal contract]
{
 "estimand": "Whether the Phase III trial meets the primary PFS endpoint",
 "Y": "1=achievement announced; 0=not achieved/not announced",
 "adjudication_source": [
  "Company topline results press release",
  "Authoritative secondary reporting"
 ]
}

[Output] Return only a single JSON number between 0 and 1 representing P(Y=1).
Do not include Markdown, explanations, units, or additional fields.
