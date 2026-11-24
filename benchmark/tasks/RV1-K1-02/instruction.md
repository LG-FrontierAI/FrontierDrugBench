---
bench_id: "RV1-K1-02"
category: "Disease-Biology"
title: "Biochemical/cellular phenotype and candidate activity prediction (Binary): Does SB203580 raise the HSPB1 S15 phosphosite"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content, definitions, evidence and numerical data supplied in this question. Do not browse, search, retrieve, call tools, use external files, consult previous questions or conversations, or use remembered publications, experimental outcomes, drug facts, or outside factual knowledge as evidence. Reason only from the supplied information. No tools are available. Return only the final option code, ordered candidate-ID JSON array, or candidate-ID set JSON array specified in the question. Do not include explanation, reasoning, confidence, citations, Markdown or any additional fields.

## Task

{"biological_context":"The p38-MAPKAPK2 pathway can phosphorylate HSPB1/HSP27 at S15. A direct inhibitor of an upstream kinase can affect a substrate without directly inhibiting the substrate protein.","evaluation_mode":"empirical_phenotype_prediction","evidence_blocks":[{"assay":"Recombinant functional kinase panel: 0.5 micromolar inhibitor, 10 micromolar ATP, 120 minutes. Values are percent remaining catalytic activity relative to the assay control, not binding affinity; lower means greater inhibition. Null denotes a missing source value, not inactivity. The displayed panel does not include PI3K lipid-kinase activity.","columns":["compound","EGFR","ERBB2/HER2","AKT1","AKT2","AKT3","GSK3a","GSK3b","P38a/MAPK14","MAPKAPK2","ERK1","PKCa","PKCb1","PKCd"],"rows":[{"AKT1":102.377,"AKT2":96.781,"AKT3":101.553,"EGFR":86.515,"ERBB2/HER2":94.561,"ERK1":100.568,"GSK3a":94.133,"GSK3b":80.237,"MAPKAPK2":98.28,"P38a/MAPK14":22.822,"PKCa":92.334,"PKCb1":73.983,"PKCd":106.858,"compound":"SB203580"}]}],"id":"RV1-K1-02","language":"en","options":{"A":"No.","B":"Yes."},"output_instruction":"Return only one option code.","question":"Does SB203580 raise the HSPB1 S15 phosphosite signal by more than 1 unit on the published centered log-intensity scale relative to EGF alone?","target_experiment":{"comparator":"EGF-stimulated cells without inhibitor; matched across compounds","condition":"DMEM with 10% FBS, 37 C, 5% CO2 culture; EGF-stimulated kinase-inhibitor phosphoproteomics panel. Three biological replicates per treatment. The target is the published average, centered log-transformed phosphosite-intensity summary, not phosphorylation stoichiometry.","endpoint":"HSPB1_S15_M1 phosphosite abundance summary from DIA LC-MS/MS","model":"hTERT-RPE1 human retinal pigment epithelial cells","perturbation":"Pretreatment with each specified inhibitor at 1 micromolar, followed by EGF stimulation","time":"Acute inhibitor pretreatment and EGF stimulation; the exact durations for the 30-inhibitor panel are not explicitly specified in the retrieved main methods and are not inferred from a separate experiment."},"task_type":"Binary"}

## Options

A. No.
B. Yes.
