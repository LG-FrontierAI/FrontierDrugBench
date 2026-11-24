---
bench_id: "BX-RET-FDA-REMBRUTINIB-SD"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-FDA-REMBRUTINIB-SD"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T1_outcome_probability"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-05
[Task background] This task forecasts the outcome of a regulatory decision. Based on the drug's existing approved indications, the strength of Phase III evidence for the new indication, precedents for similar therapies, and review status, estimate the probability that the FDA will approve the indication expansion within the specified window.

[Question]
By 2026-10-16, will the U.S. FDA approve remibrutinib (Rhapsido, Novartis) for adults with symptomatic dermographism (SD) inadequately controlled by H1 antihistamines? Y=1 denotes initial approval for this indication by that date; Y=0 denotes no approval.

[Information available before the cutoff]
- remibrutinib is a highly selective oral BTK inhibitor that received FDA approval for chronic spontaneous urticaria (CSU) in September 2025.
- The SD indication is supported by Phase III randomized controlled data in adults with SD inadequately controlled by H1 antihistamines; these data have been publicly reported.
- If approved, it would be the first treatment specifically approved for SD; no drug has previously received FDA approval for this indication.
- A third-party PDUFA calendar records an FDA action date of 2026-10-06, but no official target date had been publicly disclosed before the knowledge-lock date.

[Precollected source excerpts]
- BioX item-development team: summary of information publicly available before the knowledge-lock date (BioX curation, 2026-10-05)
  - remibrutinib is a highly selective oral BTK inhibitor that received FDA approval for chronic spontaneous urticaria (CSU) in September 2025.
  - The SD indication is supported by Phase III randomized controlled data in adults with SD inadequately controlled by H1 antihistamines; these data have been publicly reported.
  - If approved, it would be the first treatment specifically approved for SD; no drug has previously received FDA approval for this indication.
  - A third-party PDUFA calendar records an FDA action date of 2026-10-06, but no official target date had been publicly disclosed before the knowledge-lock date.

[Target and adjudication contract]
{
 "Y_definition": "Y=1 if and only if the FDA grants initial approval of remibrutinib for SD by 2026-10-16T23:59:59Z; a CRL, no action, or a delay is scored as Y=0.",
 "source_priority": [
  "Company press release announcing approval",
  "FDA approval announcement or approval letter",
  "Drugs@FDA record"
 ],
 "notes": "The FDA action date (10-06) and public disclosure date (10-07) differ by one day; use the first verifiable public record."
}

[Temporal contract]
{
 "decision_window": "First FDA action within 2026-10-06 to 2026-10-16 (inclusive)",
 "Y": "1=initial approval for the SD indication; 0=no approval",
 "adjudication_source": [
  "Company press release announcing approval",
  "FDA record"
 ]
}

[Output] Return only a single JSON number between 0 and 1 representing P(Y=1).
Do not include Markdown, explanations, units, or additional fields.
