---
bench_id: "D-C1-01"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Binary): Predict whether SLIT2 knockout increases or d"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

{"id":"D-C1-01","task_type":"Binary","biological_context":"SLIT2 is a secreted guidance ligand. Rotenone inhibits mitochondrial respiratory complex I. NDUFS1 contributes to complex I, SDHA to complex II, and UQCRC1 to complex III. Increased respiratory-component RNA can indicate altered metabolic demand but does not itself measure respiratory flux or drug sensitivity. DU-145 and LNCaP are reference prostate models; neither is PC-3M.","evidence_blocks":[{"assay":"Frozen Sanger/Behan 2019 cancer dependency map, separate single-gene knockout experiments in standard monoculture. More negative CRISPRcleaned depletion log-fold change indicates greater loss of cell fitness. Values are not CERES or fractions of dead cells. These reference measurements precede the independent target study.","rows":[{"gene":"UQCRC1","model":"LNCaP-Clone-FGC","CRISPRcleaned_depletion_logFC":0.1336},{"gene":"UQCRC1","model":"DU-145","CRISPRcleaned_depletion_logFC":-0.4992},{"gene":"NDUFS1","model":"DU-145","CRISPRcleaned_depletion_logFC":-0.3513},{"gene":"NDUFS1","model":"LNCaP-Clone-FGC","CRISPRcleaned_depletion_logFC":0.2707},{"gene":"SDHA","model":"LNCaP-Clone-FGC","CRISPRcleaned_depletion_logFC":0.2654},{"gene":"SDHA","model":"DU-145","CRISPRcleaned_depletion_logFC":-0.0972},{"gene":"SLIT2","model":"DU-145","CRISPRcleaned_depletion_logFC":0.1832},{"gene":"SLIT2","model":"LNCaP-Clone-FGC","CRISPRcleaned_depletion_logFC":0.1433}]},{"assay":"Drug-free target-line transcriptomic observation","rows":[{"observation":"Drug-free SLIT2-knockout PC-3M cells show increased RNA expression of ATP6 and the mitochondrial complex-I subunits MT-ND1, MT-ND2 and MT-ND5 relative to non-targeting controls."}]}],"target_experiment":{"model":"human PC-3M prostate cancer cells","perturbation":"CRISPR SLIT2 knockout","comparator":"non-targeting CRISPR control PC-3M cells","condition":"2 x 10^4 cells per well in 96-well plates; next day, twofold rotenone dose series from 0 to 10 micromolar; triplicate wells","endpoint":"relative drug sensitivity in the Cell Counting Kit-8 viability dose-response assay","time":"48 hours after rotenone addition"},"question":"Predict whether SLIT2 knockout increases or decreases rotenone sensitivity.","options":{"A":"Decreased sensitivity.","B":"Increased sensitivity."},"language":"en","evaluation_mode":"empirical_phenotype_prediction","response_schema":{"type":"string","enum":["A","B"]},"output_instruction":"Output only A or B."}

## Options

A. Decreased sensitivity.
B. Increased sensitivity.
