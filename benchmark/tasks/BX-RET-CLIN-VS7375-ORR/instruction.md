---
bench_id: "BX-RET-CLIN-VS7375-ORR"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-CLIN-VS7375-ORR"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T2_quantitative_effect"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-12
[Task background] This task forecasts an early-phase clinical response rate. Based on previous interim signals, activity levels of similar KRAS G12D inhibitors, sample size, and the time lag required for response confirmation, provide calibrated quantile forecasts for the confirmed response rate.

[Question]
Predict the confirmed response rate (%, 0–100) among evaluable patients with pancreatic cancer in the VS-7375 (oral KRAS G12D inhibitor) 900 mg dose group in Verastem's updated TARGET-D 101 data (to be reported in October 2026). Provide the seven quantiles q05–q95.

[Information available before the cutoff]
- VS-7375 is an oral, highly selective KRAS G12D inhibitor; TARGET-D 101 is an ongoing Phase I/II study (pancreatic cancer, colorectal cancer, NSCLC).
- Previously disclosed interim data have shown signals of activity in pancreatic cancer; this update reports confirmed responses among 20 evaluable patients in the 900 mg dose group.
- Response confirmation requires two assessments separated by an interval; unconfirmed responses are not counted.
- The literature reports confirmed response rates of approximately 20%–60% for similar KRAS G12D inhibitors in pancreatic cancer.
- The company also announced that the FDA had agreed to the design of the Phase III TARGET-D 301 study in first-line pancreatic cancer.

[Precollected source excerpts]
- BioX item-development team: summary of information publicly available before the knowledge-lock date (BioX curation, 2026-10-12)
  - VS-7375 is an oral, highly selective KRAS G12D inhibitor; TARGET-D 101 is an ongoing Phase I/II study (pancreatic cancer, colorectal cancer, NSCLC).
  - Previously disclosed interim data have shown signals of activity in pancreatic cancer; this update reports confirmed responses among 20 evaluable patients in the 900 mg dose group.
  - Response confirmation requires two assessments separated by an interval; unconfirmed responses are not counted.
  - The literature reports confirmed response rates of approximately 20%–60% for similar KRAS G12D inhibitors in pancreatic cancer.
  - The company also announced that the FDA had agreed to the design of the Phase III TARGET-D 301 study in first-line pancreatic cancer.

[Target and adjudication contract]
{
 "target_locator": "Confirmed response rate (8/20) among evaluable patients with pancreatic cancer receiving VS-7375 900 mg in the updated TARGET-D 101 data.",
 "source_priority": [
  "Company data report/press release",
  "Conference presentation"
 ],
 "notes": "Use the confirmed response rate (number of confirmed responses divided by the number of evaluable patients); do not use other cohorts or unconfirmed responses."
}

[Temporal contract]
{
 "estimand": "Confirmed response rate among evaluable patients with pancreatic cancer in the 900 mg dose group",
 "unit": "percent",
 "value_range": [
  0,
  100
 ],
 "adjudication_source": [
  "Company data report",
  "Conference presentation"
 ]
}

[Output] Return only a JSON array of length 7, ordered as q05, q10, q25, q50, q75, q90, q95. Each value must be between 0 and 100, and the values must be nondecreasing.
Do not include Markdown, explanations, units, or additional fields.
