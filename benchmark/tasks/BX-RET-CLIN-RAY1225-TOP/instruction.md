---
bench_id: "BX-RET-CLIN-RAY1225-TOP"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-CLIN-RAY1225-TOP"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T1_outcome_probability"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-13
[Task background] This task forecasts the probability of clinical trial success. Based on Phase II weight-loss signals, effect sizes for a similar dual-target agonist (tirzepatide) in Chinese populations, the primary endpoint definition, and statistical power, estimate the probability of positive topline results.

[Question]
Will positive results (meeting the primary endpoint) be announced in the topline analysis of Guangdong Zhongsheng/Zhongcheng Ruichuang's Phase III REBUILDING-2 weight-loss trial of RAY1225 injection (a multicenter, randomized, double-blind, placebo-controlled trial in Chinese adults with overweight/obesity)? Y=1 denotes that positive results are announced; Y=0 denotes that positive results are not announced or that no results are disclosed.

[Information available before the cutoff]
- RAY1225 is an internally developed GLP-1/GIP dual-target agonist (a Class 1 new drug).
- REBUILDING-2 is a multicenter, randomized, double-blind, placebo-controlled Phase III trial enrolling Chinese adults with overweight or obesity.
- Publicly available Phase II data have shown significant weight loss and a favorable safety profile.
- A similar dual-target agonist (tirzepatide) has demonstrated approximately 15%–18% body-weight reductions in Phase III studies in Chinese populations with overweight/obesity, with a high likelihood of meeting the primary endpoint.

[Precollected source excerpts]
- BioX item-development team: summary of information publicly available before the knowledge-lock date (BioX curation, 2026-10-13)
  - RAY1225 is an internally developed GLP-1/GIP dual-target agonist (a Class 1 new drug).
  - REBUILDING-2 is a multicenter, randomized, double-blind, placebo-controlled Phase III trial enrolling Chinese adults with overweight or obesity.
  - Publicly available Phase II data have shown significant weight loss and a favorable safety profile.
  - A similar dual-target agonist (tirzepatide) has demonstrated approximately 15%–18% body-weight reductions in Phase III studies in Chinese populations with overweight/obesity, with a high likelihood of meeting the primary endpoint.

[Target and adjudication contract]
{
 "Y_definition": "Y=1 if and only if the company announces by T23:59:59Z on the result release date (after the knowledge-lock date) that REBUILDING-2 met the primary endpoint in its topline analysis (positive results); an announcement of negative results, a delay without an announcement, or no action is scored as Y=0.",
 "source_priority": [
  "Company announcement",
  "Reporting by authoritative financial media"
 ],
 "notes": "This item concerns only whether the topline results are positive; it does not ask for the specific magnitude of weight loss (the announcement did not disclose a value)."
}

[Temporal contract]
{
 "estimand": "Whether the REBUILDING-2 topline announcement reports that the primary endpoint was met (positive results)",
 "Y": "1=positive results announced; 0=negative/not announced",
 "adjudication_source": [
  "Company announcement",
  "Authoritative financial media"
 ]
}

[Output] Return only a single JSON number between 0 and 1 representing P(Y=1).
Do not include Markdown, explanations, units, or additional fields.
