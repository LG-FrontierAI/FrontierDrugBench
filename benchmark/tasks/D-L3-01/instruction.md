---
bench_id: "D-L3-01"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Binary): Predict the direction of liver metastatic les"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

{"id":"D-L3-01","task_type":"Binary","biological_context":"PCMT1 repairs damaged isoaspartyl residues and can participate in extracellular protein interactions. The study investigates its interaction with LAMB3 and integrin–FAK–Src signaling, which connects adhesion to motility. The quantitative dependency-map lines below are ovarian reference models; SKOV3 is not present in this frozen matrix. The separate SKOV3 molecular experiment provides the target-line bridge.","evidence_blocks":[{"assay":"Frozen Sanger/Behan 2019 cancer dependency map, separate single-gene knockout experiments in standard monoculture. More negative CRISPRcleaned depletion log-fold change indicates greater loss of cell fitness. Values are not CERES or fractions of dead cells. These reference measurements precede the independent target study.","rows":[{"gene":"LAMB3","model":"OVCAR-5","CRISPRcleaned_depletion_logFC":0.1599},{"gene":"SRC","model":"OVCAR-8","CRISPRcleaned_depletion_logFC":-0.0673},{"gene":"PTK2","model":"OVCAR-5","CRISPRcleaned_depletion_logFC":-1.3443},{"gene":"PTK2","model":"OVCAR-3","CRISPRcleaned_depletion_logFC":-0.3144},{"gene":"LAMB3","model":"OVCAR-3","CRISPRcleaned_depletion_logFC":0.2152},{"gene":"PCMT1","model":"OVCAR-8","CRISPRcleaned_depletion_logFC":0.057},{"gene":"SRC","model":"OVCAR-5","CRISPRcleaned_depletion_logFC":-0.2034},{"gene":"PCMT1","model":"OVCAR-3","CRISPRcleaned_depletion_logFC":-0.2463},{"gene":"PTK2","model":"OVCAR-8","CRISPRcleaned_depletion_logFC":-0.333},{"gene":"LAMB3","model":"OVCAR-8","CRISPRcleaned_depletion_logFC":-0.001},{"gene":"SRC","model":"OVCAR-3","CRISPRcleaned_depletion_logFC":0.3151},{"gene":"PCMT1","model":"OVCAR-5","CRISPRcleaned_depletion_logFC":-0.0288}]},{"assay":"SKOV3 signaling and genetic rescue","rows":[{"observation":"In SKOV3 cells, PCMT1 knockout reduces FAK and Src phosphorylation without changing total protein abundance; re-expression of PCMT1 restores phosphorylation."}]}],"target_experiment":{"model":"SKOV3 ovarian cancer cells in female BALB/c nude mice aged 4–5 weeks","perturbation":"stable PCMT1 CRISPR knockout before inoculation","comparator":"sgControl SKOV3 cells","condition":"intraperitoneal injection of 3 x 10^6 cells","endpoint":"number of metastatic lesions in the liver","time":"10 weeks after inoculation; Figure 7K: control n=10, knockout n=9"},"question":"Predict the direction of liver metastatic lesion number after PCMT1 knockout.","options":{"A":"Fewer liver metastatic lesions.","B":"More liver metastatic lesions."},"language":"en","evaluation_mode":"empirical_phenotype_prediction","response_schema":{"type":"string","enum":["A","B"]},"output_instruction":"Output only A or B."}

## Options

A. Fewer liver metastatic lesions.
B. More liver metastatic lesions.
