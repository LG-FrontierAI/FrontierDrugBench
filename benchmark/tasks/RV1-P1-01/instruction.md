---
bench_id: "RV1-P1-01"
category: "Disease-Biology"
title: "Biochemical/cellular phenotype and candidate activity prediction (Binary): Will MTF1 knockout increase SF295 sensitivity"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content, definitions, evidence and numerical data supplied in this question. Do not browse, search, retrieve, call tools, use external files, consult previous questions or conversations, or use remembered publications, experimental outcomes, drug facts, or outside factual knowledge as evidence. Reason only from the supplied information. No tools are available. Return only the final option code, ordered candidate-ID JSON array, or candidate-ID set JSON array specified in the question. Do not include explanation, reasoning, confidence, citations, Markdown or any additional fields.

## Task

{"biological_context":"MTF1 regulates metal-binding metallothioneins. SF295 has a chromosome 16q amplification; MT1E/MT1X/MT2A can buffer metals. Disulfiram has ALDH-inhibitory pharmacology, but its anticancer activity can also depend on copper.","evaluation_mode":"empirical_phenotype_prediction","evidence_blocks":[{"assay":"Untreated CCLE RNA-seq, DepMap 19Q4; log2(TPM+1). Values rounded to four decimals. Expression is not a measurement of protein activity.","columns":["model","depmap_id","tissue","MTF1","MT1E","MT2A","ALDH2"],"rows":[{"ALDH2":4.2555,"MT1E":7.479,"MT2A":10.9874,"MTF1":2.6346,"depmap_id":"ACH-000376","model":"SF295","tissue":"central_nervous_system"},{"ALDH2":4.9787,"MT1E":0.3785,"MT2A":7.537,"MTF1":2.5777,"depmap_id":"ACH-000389","model":"H4","tissue":"central_nervous_system"},{"ALDH2":5.4063,"MT1E":0.2265,"MT2A":4.942,"MTF1":2.3896,"depmap_id":"ACH-000756","model":"GI1","tissue":"central_nervous_system"},{"ALDH2":5.0518,"MT1E":9.4845,"MT2A":11.9023,"MTF1":2.8718,"depmap_id":"ACH-000075","model":"U87MG","tissue":"central_nervous_system"},{"ALDH2":0.516,"MT1E":0.5059,"MT2A":9.5776,"MTF1":2.5801,"depmap_id":"ACH-000027","model":"GOS3","tissue":"central_nervous_system"}]},{"assay":"PRISM primary screen 19Q4: 2.5 micromolar drug for 5 days; replicate-collapsed log2 barcode signal relative to DMSO. Lower is a stronger relative viability/growth signal reduction; not an IC50 or an apoptosis measurement.","columns":["model","depmap_id","drug","log2_barcode_change"],"rows":[{"depmap_id":"ACH-000376","drug":"disulfiram","log2_barcode_change":-0.8007,"model":"SF295"},{"depmap_id":"ACH-000389","drug":"disulfiram","log2_barcode_change":-2.3073,"model":"H4"},{"depmap_id":"ACH-000756","drug":"disulfiram","log2_barcode_change":-2.1504,"model":"GI1"},{"depmap_id":"ACH-000075","drug":"disulfiram","log2_barcode_change":0.1325,"model":"U87MG"},{"depmap_id":"ACH-000027","drug":"disulfiram","log2_barcode_change":-0.1952,"model":"GOS3"}]},{"assay":"Independent, drug-free RNA-seq in SF295 after MTF1 knockout versus parental cells; three independent wells. Source-reported qualitative directions, not invented fold changes.","columns":["gene","change_after_MTF1_KO"],"rows":[{"change_after_MTF1_KO":"decreased","gene":"MT1E"},{"change_after_MTF1_KO":"decreased","gene":"MT1X"},{"change_after_MTF1_KO":"decreased","gene":"MT2A"}]}],"id":"RV1-P1-01","language":"en","options":{"A":"No, sensitivity does not increase.","B":"Yes, sensitivity increases."},"output_instruction":"Return only one option code.","question":"Will MTF1 knockout increase SF295 sensitivity to disulfiram?","target_experiment":{"comparator":"SF295 sgGFP control under the same disulfiram dose-response conditions","condition":"RPMI with 10% heat-inactivated FBS and 1% penicillin-streptomycin; no copper chelator. CellTiter-Glo normalized to vehicle in each group; three independently treated wells per condition.","endpoint":"Direction of disulfiram sensitivity shift","model":"SF295 glioma cells","perturbation":"CRISPR/Cas9 MTF1 knockout followed by disulfiram","time":"Follow-up incubation time and exact dose grid are not specified in the retrieved text; predict the overall dose-response shift, not a numerical fixed-dose effect."},"task_type":"Binary"}

## Options

A. No, sensitivity does not increase.
B. Yes, sensitivity increases.
