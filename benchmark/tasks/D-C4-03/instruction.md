---
bench_id: "D-C4-03"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Binary): Predict whether CD58 knockout shifts the MSLN"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

{"id":"D-C4-03","task_type":"Binary","biological_context":"OVCAR8 expresses mesothelin (MSLN). An MSLN-directed bispecific T-cell engager connects tumor antigen to T-cell CD3. CD58 on tumor cells binds T-cell CD2 and supplies costimulation. BID is a proapoptotic BH3 protein linking extrinsic to mitochondrial apoptosis; BCL2L1 encodes the antiapoptotic Bcl-xL protein; CFLAR regulates caspase-8 activation. OVCAR-3/5 are reference ovarian cancer lines, not aliases of OVCAR8.","evidence_blocks":[{"assay":"Frozen Sanger/Behan 2019 cancer dependency map, separate single-gene knockout experiments in standard monoculture. More negative CRISPRcleaned depletion log-fold change indicates greater loss of cell fitness. Values are not CERES or fractions of dead cells. These reference measurements precede the independent target study.","rows":[{"gene":"CASP8","model":"OVCAR-5","CRISPRcleaned_depletion_logFC":0.2622},{"gene":"CD58","model":"OVCAR-8","CRISPRcleaned_depletion_logFC":-0.0839},{"gene":"BCL2L1","model":"OVCAR-3","CRISPRcleaned_depletion_logFC":-0.4291},{"gene":"BCL2L1","model":"OVCAR-8","CRISPRcleaned_depletion_logFC":-0.5373},{"gene":"CASP8","model":"OVCAR-8","CRISPRcleaned_depletion_logFC":0.251},{"gene":"CFLAR","model":"OVCAR-3","CRISPRcleaned_depletion_logFC":-1.1482},{"gene":"BID","model":"OVCAR-5","CRISPRcleaned_depletion_logFC":0.332},{"gene":"CASP8","model":"OVCAR-3","CRISPRcleaned_depletion_logFC":0.0389},{"gene":"CD58","model":"OVCAR-5","CRISPRcleaned_depletion_logFC":-0.1448},{"gene":"CFLAR","model":"OVCAR-8","CRISPRcleaned_depletion_logFC":-0.9613},{"gene":"CD58","model":"OVCAR-3","CRISPRcleaned_depletion_logFC":0.2042},{"gene":"BID","model":"OVCAR-8","CRISPRcleaned_depletion_logFC":0.1064},{"gene":"CFLAR","model":"OVCAR-5","CRISPRcleaned_depletion_logFC":-1.8401},{"gene":"BCL2L1","model":"OVCAR-5","CRISPRcleaned_depletion_logFC":-1.3311},{"gene":"BID","model":"OVCAR-3","CRISPRcleaned_depletion_logFC":0.1746}]},{"assay":"Target-antigen control","rows":[{"observation":"The study confirmed that these genetic manipulations did not change MSLN surface expression in the engineered OVCAR8 cells."}]}],"target_experiment":{"model":"human OVCAR8 (OVCAR-8) ovarian cancer cells","perturbation":"CRISPR knockout of CD58","comparator":"parental wild-type OVCAR8 with the same T-cell donor and engager series","condition":"freshly thawed human CD3-positive T cells, E:T 2:1; increasing MSLN TCE concentrations; RPMI1640 with Glutamax and 10% heat-inactivated FBS; 37 degrees C, 5% CO2","endpoint":"MSLN TCE concentration producing half-maximal redirected lysis (EC50); adherent-target CellTiter-Glo viability assay","time":"72 hours; donor-repeat validation"},"question":"Predict whether CD58 knockout shifts the MSLN TCE EC50 upward or downward.","options":{"A":"Higher EC50.","B":"Lower EC50."},"language":"en","evaluation_mode":"empirical_phenotype_prediction","response_schema":{"type":"string","enum":["A","B"]},"output_instruction":"Output only A or B."}

## Options

A. Higher EC50.
B. Lower EC50.
