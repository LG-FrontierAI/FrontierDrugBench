---
bench_id: "BX-RET-FDA-PRITELIVIR"
category: "Live Benchmark"
title: "BioX prospective forecast: BX-RET-FDA-PRITELIVIR"
format: "forecast"
input_mode: "inline_prompt"
task_type: "T1_outcome_probability"
---

# Prompt

You are BioX's raw LLM for prospective biological forecasting. Internet access, web searches, code execution, and all tool calls are prohibited; use only the precollected context in this message. The prediction target and time window for this item are fixed, so you may answer directly.

[Knowledge cutoff] 2026-10-05
[Task background] This task forecasts the outcome of a regulatory decision. Based on the review pathway (Priority Review, Breakthrough Therapy designation), precedents for similar therapies, and the strength of pivotal trial evidence, estimate the probability that the FDA will grant initial approval within the specified window, rather than predicting the trial results themselves.

[Question]
By 2026-10-16, will the U.S. FDA approve pritelivir (AiCuris/Asahi Kasei, NDA 221154) for the treatment of mucocutaneous herpes simplex virus (HSV) lesions in immunocompromised adults who have not responded to acyclovir, valacyclovir, or famciclovir, with or without evidence of resistance? Y=1 denotes initial approval for this indication by that date; Y=0 denotes no approval (a Complete Response Letter, no action, or a delay).

[Information available before the cutoff]
- pritelivir is a first-in-class oral helicase-primase inhibitor that has received Priority Review, Breakthrough Therapy, and Fast Track designations.
- Pivotal Phase III data from PRIOH-1 Part C (NCT03073967) have been publicly released: the rate of complete lesion crusting and healing at Day 28 was 62.7% versus 34% with investigator's choice of treatment (adjusted difference 28.4%, p=0.0047).
- Third-party PDUFA calendars and pharmaceutical company overviews list an anticipated decision in Q4 2026; the exact date has not been disclosed.
- The indicated population is small (immunocompromised patients with resistant/refractory disease), with no previously approved drug in the same class.

[Precollected source excerpts]
- FDA Decisions Expected: October 2026 (Prime Therapeutics, 2026-09-11)
  - Q4 2026: pritelivir ... is under FDA Priority Review for the treatment of refractory herpes simplex virus (HSV) infections ... has received both Breakthrough Therapy and Fast Track designations.
  - At Day 28, complete lesion healing was achieved in 62.7% of pritelivir-treated patients compared with 34% of patients who received the standard-of-care therapy

[Target and adjudication contract]
{
 "Y_definition": "Y=1 if and only if the FDA grants initial approval of pritelivir for refractory mucocutaneous HSV disease in immunocompromised adults by 2026-10-16T23:59:59Z; a CRL, no action, or a delay is scored as Y=0.",
 "source_priority": [
  "FDA approval announcement page or approval letter",
  "Company press release announcing approval",
  "Drugs@FDA record"
 ],
 "notes": "Approval dates have day-level precision; if the FDA action date differs from the public disclosure date, use the first verifiable public record."
}

[Temporal contract]
{
 "decision_window": "First FDA action within 2026-10-06 to 2026-10-16 (inclusive)",
 "Y": "1=initial approval for this indication; 0=no approval",
 "adjudication_source": [
  "FDA approval announcement page",
  "Company press release announcing approval"
 ]
}

[Output] Return only a single JSON number between 0 and 1 representing P(Y=1).
Do not include Markdown, explanations, units, or additional fields.
