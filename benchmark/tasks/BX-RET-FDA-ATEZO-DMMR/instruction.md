---
bench_id: "BX-RET-FDA-ATEZO-DMMR"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-FDA-ATEZO-DMMR"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T1_outcome_probability"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-05
[Task background] This task forecasts the outcome of a regulatory decision. Based on the publicly disclosed PDUFA target date, Priority Review status, and the strength of Phase III evidence, estimate the probability that the FDA will grant initial approval within the specified window.

[Question]
By 2026-10-16, will the U.S. FDA approve atezolizumab (Tecentriq/Tecentriq Hybreza, Genentech) in combination with chemotherapy as adjuvant treatment for patients with stage III dMMR/MSI-H colon cancer? Y=1 denotes initial approval for this indication by that date; Y=0 denotes no approval.

[Information available before the cutoff]
- The sBLA (atezolizumab + Tecentriq Hybreza in combination with chemotherapy as adjuvant treatment for stage III dMMR/MSI-H colon cancer) was accepted by the FDA and granted Priority Review in June 2026.
- The company has publicly announced a PDUFA target date of 2026-10-09.
- Supporting data are from Alliance ATOMIC (A021502, NCT02912559, 712 patients): adding atezolizumab reduced the risk of recurrence or death by 50%, with 36-month DFS of 86.3% versus 76.2%; the results have been published in NEJM.
- If approved, it would be the first adjuvant immunotherapy regimen for this molecularly defined population.

[Precollected source excerpts]
- FDA Grants Priority Review for Genentech's Tecentriq for a Certain Type of Stage III Colon Cancer (Genentech/Roche, 2026-06-10)
  - The FDA has granted Priority Review and is expected to make a decision on the approval by October 9, 2026.
  - ATOMIC demonstrated that adding Tecentriq to standard FOLFOX6 chemotherapy reduced the risk of disease recurrence or death by 50% ... The 36-month disease-free survival was 86% for Tecentriq combined with FOLFOX6 compared with 76% in the FOLFOX6 alone group.

[Target and adjudication contract]
{
 "Y_definition": "Y=1 if and only if the FDA grants initial approval of atezolizumab in combination with chemotherapy as adjuvant treatment for stage III dMMR/MSI-H colon cancer by 2026-10-16T23:59:59Z; a CRL, no action, or a delay is scored as Y=0.",
 "source_priority": [
  "FDA approval announcement page",
  "Company press release announcing approval",
  "Approval letter"
 ],
 "notes": "Approval (10-08) occurred one day before the PDUFA target date (10-09); use the date on the FDA page."
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
