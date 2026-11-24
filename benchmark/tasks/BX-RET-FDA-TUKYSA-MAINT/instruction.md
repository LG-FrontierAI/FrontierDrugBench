---
bench_id: "BX-RET-FDA-TUKYSA-MAINT"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-FDA-TUKYSA-MAINT"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T1_outcome_probability"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-05
[Task background] This task forecasts the outcome of a regulatory decision. Key efficacy data were publicly available before the knowledge-lock date. Based on the strength of the data, the submission date, and precedents for review duration, estimate the probability that the FDA will grant initial approval within the specified window.

[Question]
By 2026-10-16, will the U.S. FDA approve tucatinib (Tukysa, Seagen/Pfizer) in combination with trastuzumab and pertuzumab as maintenance treatment after induction therapy for adults with HER2-positive unresectable locally advanced or metastatic breast cancer? Y=1 denotes initial approval for this indication by that date; Y=0 denotes no approval.

[Information available before the cutoff]
- The sNDA was submitted on 2025-12-17 for maintenance treatment after induction therapy for HER2+ unresectable locally advanced or metastatic breast cancer.
- Supporting data from HER2CLIMB-05 (NCT05132582, 654 patients) were presented at SABCS on 2025-12-10 and published in JCO: PFS 24.9 versus 16.3 months, HR 0.641 (p<0.0001).
- tucatinib is already approved for second-line and later treatment of HER2+ MBC (including patients with brain metastases).
- If approved, it would be the first chemotherapy-free first-line maintenance regimen for this population.

[Precollected source excerpts]
- TUKYSA Added to First-Line Maintenance Therapy Extends Median Progression-Free Survival by Over 8 Months (Pfizer, 2025-12-10)
  - The primary endpoint analysis showed a 35.9% reduction in the risk of disease progression or death among patients treated with TUKYSA, trastuzumab, and pertuzumab compared to those treated with placebo ... (hazard ratio [HR] of 0.641, 95% confidence interval (CI): 0.514-0.799; 2-sided p<0.0001).
  - the median progression-free survival (PFS) was 24.9 months ... in the TUKYSA arm and 16.3 months ... in the placebo arm
- Tukysa approval letter (sNDA dated December 17, 2025) (FDA, result release date (after the knowledge-lock date))
  - Please refer to your supplemental new drug application (sNDA) dated December 17, 2025, received December 17, 2025

[Target and adjudication contract]
{
 "Y_definition": "Y=1 if and only if the FDA grants initial approval of tucatinib in combination with trastuzumab and pertuzumab for maintenance treatment after induction therapy for HER2+ metastatic breast cancer by 2026-10-16T23:59:59Z; a CRL, no action, or a delay is scored as Y=0.",
 "source_priority": [
  "FDA approval announcement page",
  "Company press release announcing approval",
  "Approval letter"
 ],
 "notes": "The trial efficacy values were publicly available before the knowledge-lock date and are not the prediction target; this item concerns only the approval event."
}

[Temporal contract]
{
 "decision_window": "First FDA action within 2026-10-06 to 2026-10-16 (inclusive)",
 "Y": "1=initial approval for this indication; 0=no approval",
 "adjudication_source": [
  "FDA approval announcement page",
  "Company press release"
 ]
}

[Output] Return only a single JSON number between 0 and 1 representing P(Y=1).
Do not include Markdown, explanations, units, or additional fields.
