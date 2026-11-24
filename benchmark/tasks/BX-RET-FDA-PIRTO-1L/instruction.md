---
bench_id: "BX-RET-FDA-PIRTO-1L"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-FDA-PIRTO-1L"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T1_outcome_probability"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-09-28
[Task background] This task forecasts the outcome of a regulatory decision. Based on the strength of publicly available Phase III data, review status, and precedents for similar therapies, estimate the probability that the FDA will grant initial approval within the specified window despite the absence of a publicly disclosed target date.

[Question]
By 2026-10-16, will the U.S. FDA approve pirtobrutinib (Jaypirca, Eli Lilly) for adults with previously untreated chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL) without a known 17p deletion? Y=1 denotes initial approval for this indication by that date; Y=0 denotes no approval.

[Information available before the cutoff]
- pirtobrutinib is the first approved noncovalent BTK inhibitor, with existing indications for R/R CLL/SLL and MCL.
- The primary analysis of BRUIN CLL-313 (NCT05023980, 282 patients, pirtobrutinib versus bendamustine+rituximab) was presented at ASH in December 2025 and published in JCO: IRC-assessed PFS HR 0.20 (95% CI 0.11–0.37).
- The sNDA for this first-line indication has been submitted and is under review, but no PDUFA target date has been publicly disclosed.
- Current standard first-line CLL treatments are regimens based on BTK inhibitors or BCL-2 inhibitors.

[Precollected source excerpts]
- BioX item-development team: summary of information publicly available before the knowledge-lock date (BioX curation, 2026-09-28)
  - pirtobrutinib is the first approved noncovalent BTK inhibitor, with existing indications for R/R CLL/SLL and MCL.
  - The primary analysis of BRUIN CLL-313 (NCT05023980, 282 patients, pirtobrutinib versus bendamustine+rituximab) was presented at ASH in December 2025 and published in JCO: IRC-assessed PFS HR 0.20 (95% CI 0.11–0.37).
  - The sNDA for this first-line indication has been submitted and is under review, but no PDUFA target date has been publicly disclosed.
  - Current standard first-line CLL treatments are regimens based on BTK inhibitors or BCL-2 inhibitors.

[Target and adjudication contract]
{
 "Y_definition": "Y=1 if and only if the FDA grants initial approval of pirtobrutinib for previously untreated CLL/SLL (without a known 17p deletion) by 2026-10-16T23:59:59Z; a CRL, no action, or a delay is scored as Y=0.",
 "source_priority": [
  "FDA approval announcement page",
  "Company press release announcing approval",
  "Approval letter"
 ],
 "notes": "No PDUFA date has been publicly disclosed, so uncertainty about the timing of the decision is high; use the date on the FDA page for adjudication."
}

[Temporal contract]
{
 "decision_window": "First FDA action within 2026-09-29 to 2026-10-16 (inclusive)",
 "Y": "1=initial approval for this indication; 0=no approval",
 "adjudication_source": [
  "FDA approval announcement page",
  "Company press release"
 ]
}

[Output] Return only a single JSON number between 0 and 1 representing P(Y=1).
Do not include Markdown, explanations, units, or additional fields.
