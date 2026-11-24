---
bench_id: "BX-RET-FDA-ANKTIVA-PAP"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-FDA-ANKTIVA-PAP"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T1_outcome_probability"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-09
[Task background] This task forecasts the outcome of a regulatory decision. The key uncertainty is whether the FDA will grant approval substantially earlier than the publicly disclosed PDUFA target date by extrapolating from existing CIS evidence. Weigh regulatory precedents, signals from the public workshop, and the distribution of review durations.

[Question]
By 2026-10-16, will the U.S. FDA approve nogapendekin alfa inbakicept-pmln (Anktiva, ImmunityBio/Altor BioScience) in combination with BCG for adults with BCG-unresponsive, high-risk, papillary-only non-muscle-invasive bladder cancer (NMIBC)? Y=1 denotes initial approval for this expanded indication by that date; Y=0 denotes no approval.

[Information available before the cutoff]
- The sBLA (Anktiva+BCG for BCG-unresponsive NMIBC with papillary disease without CIS) was accepted by the FDA on 2026-05-20, with a PDUFA target date of 2027-01-06.
- On 2026-05-18, the FDA held a public workshop on efficacy assessment in the two NMIBC histologies, papillary disease and CIS, discussing the feasibility of extrapolating CIS evidence to papillary disease.
- In 2026-03, NCCN included treatment of BCG-unresponsive papillary disease as a Category 2A guideline recommendation.
- Supporting evidence consists of results from QUILT-3.032 Cohort A (the CIS population) plus a literature-based extrapolation rationale, rather than a prospective randomized trial in a papillary-only population.
- If approved, it would be the first approved bladder-sparing treatment for this population.

[Precollected source excerpts]
- ImmunityBio Announces FDA Acceptance of Supplemental BLA for ANKTIVA Plus BCG in BCG-Unresponsive NMIBC with Papillary Disease; PDUFA Date Set for January 6, 2027 (ImmunityBio, 2026-05-20)
  - The FDA has accepted for review a supplemental biologics license application (sBLA) seeking the approval of nogapendekin alfa inbakicept-pmln (Anktiva) in combination with BCG for the treatment of adult patients with BCG-unresponsive non-muscle-invasive bladder cancer (NMIBC) with papillary disease without carcinoma in situ (CIS).
  - The agency has set a goal date of January 6, 2027, for the sBLA under the Prescription Drug User Fee Act.

[Target and adjudication contract]
{
 "Y_definition": "Y=1 if and only if the FDA grants initial approval of Anktiva+BCG for high-risk, papillary-only, BCG-unresponsive NMIBC by 2026-10-16T23:59:59Z; a CRL, no action, or a delay is scored as Y=0.",
 "source_priority": [
  "FDA news release or approval announcement page",
  "Company press release announcing approval",
  "Approval letter"
 ],
 "notes": "Approval occurred approximately three months before the publicly disclosed PDUFA date; use the date of the FDA news release for adjudication."
}

[Temporal contract]
{
 "decision_window": "First FDA action within 2026-10-10 to 2026-10-16 (inclusive)",
 "Y": "1=initial approval for this expanded indication; 0=no approval",
 "adjudication_source": [
  "FDA news release",
  "Company press release"
 ]
}

[Output] Return only a single JSON number between 0 and 1 representing P(Y=1).
Do not include Markdown, explanations, units, or additional fields.
