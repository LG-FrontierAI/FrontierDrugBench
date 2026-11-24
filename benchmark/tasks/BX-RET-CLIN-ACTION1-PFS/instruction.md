---
bench_id: "BX-RET-CLIN-ACTION1-PFS"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-CLIN-ACTION1-PFS"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T1_outcome_probability"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-09
[Task background] This task forecasts the probability of clinical trial success. Based on Phase I signals, precedents for similar radioligand therapies (NETTER-1, Lutathera; Pluvicto), the choice of comparator, and the interim analysis design, estimate the probability of meeting the primary endpoint.

[Question]
Will the planned interim analysis of Bristol Myers Squibb/RayzeBio's Phase III ACTION-1 trial (RYZ101, 225Ac-DOTATATE, versus investigator's choice of standard therapy in patients with SSTR+ GEP-NETs that have progressed after Lu177 treatment) meet the primary endpoint of BICR-assessed PFS with statistical significance? Y=1 denotes that the endpoint is met; Y=0 denotes that it is not met or that achievement is not announced.

[Information available before the cutoff]
- ACTION-1 (NCT05477576) is a randomized Phase III trial comparing RYZ101 (225Ac-DOTATATE) with investigator's choice of standard therapy (high-dose/increased-frequency long-acting somatostatin analogues, everolimus, or sunitinib).
- The population consists of patients with SSTR+ gastroenteropancreatic neuroendocrine tumors (GEP-NETs) that have progressed after Lu177-based therapy.
- The primary endpoint is BICR-assessed PFS; this is a planned interim analysis.
- Publicly available Phase I data for RYZ101 have shown signals of antitumor activity; the FDA granted Orphan Drug designation in 2026-08.
- 177Lu-DOTATATE (Lutathera) demonstrated a PFS benefit in a similar population in NETTER-1; 225Ac has a higher linear energy transfer.

[Precollected source excerpts]
- BioX item-development team: summary of information publicly available before the knowledge-lock date (BioX curation, 2026-10-09)
  - ACTION-1 (NCT05477576) is a randomized Phase III trial comparing RYZ101 (225Ac-DOTATATE) with investigator's choice of standard therapy (high-dose/increased-frequency long-acting somatostatin analogues, everolimus, or sunitinib).
  - The population consists of patients with SSTR+ gastroenteropancreatic neuroendocrine tumors (GEP-NETs) that have progressed after Lu177-based therapy.
  - The primary endpoint is BICR-assessed PFS; this is a planned interim analysis.
  - Publicly available Phase I data for RYZ101 have shown signals of antitumor activity; the FDA granted Orphan Drug designation in 2026-08.
  - 177Lu-DOTATATE (Lutathera) demonstrated a PFS benefit in a similar population in NETTER-1; 225Ac has a higher linear energy transfer.

[Target and adjudication contract]
{
 "Y_definition": "Y=1 if and only if the company announces by 2026-10-16T23:59:59Z that the planned interim analysis of ACTION-1 met the primary endpoint of BICR-assessed PFS with statistical significance; an announcement that the endpoint was not met, a delay without an announcement, or no action is scored as Y=0.",
 "source_priority": [
  "Company topline results press release",
  "Subsequent regulatory disclosures or conference presentations"
 ],
 "notes": "This item concerns only whether the interim analysis met the primary endpoint; it does not ask for the HR value (not disclosed in the topline results)."
}

[Temporal contract]
{
 "estimand": "Whether the planned interim analysis meets the primary endpoint of BICR-assessed PFS",
 "Y": "1=achievement announced; 0=not achieved/not announced",
 "adjudication_source": [
  "Company topline results press release"
 ]
}

[Output] Return only a single JSON number between 0 and 1 representing P(Y=1).
Do not include Markdown, explanations, units, or additional fields.
