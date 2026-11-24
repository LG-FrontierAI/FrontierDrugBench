---
bench_id: "D-L1-09"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Binary): Predict whether the PTPN14-knockout tumors ha"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

{"id":"D-L1-09","task_type":"Binary","biological_context":"PTPN14 is a nonreceptor protein tyrosine phosphatase. Loss of matrix attachment can trigger anoikis; PI3K/AKT and ERK signaling influence survival in detached cells. PTK2/FAK and BCAR3 connect adhesion signaling to cell behavior. Cultured fitness and phosphosignaling do not directly measure in-vivo tumor expansion.","evidence_blocks":[{"assay":"Frozen Sanger/Behan 2019 cancer dependency map, separate single-gene knockout experiments in standard monoculture. More negative CRISPRcleaned depletion log-fold change indicates greater loss of cell fitness. Values are not CERES or fractions of dead cells. These reference measurements precede the independent target study.","rows":[{"gene":"PTPN14","model":"MDA-MB-231","CRISPRcleaned_depletion_logFC":-0.0485},{"gene":"BCAR3","model":"MDA-MB-231","CRISPRcleaned_depletion_logFC":0.2041},{"gene":"AKT1","model":"MDA-MB-231","CRISPRcleaned_depletion_logFC":0.3131},{"gene":"PTK2","model":"MDA-MB-231","CRISPRcleaned_depletion_logFC":-0.7665}]},{"assay":"Detached-cell phosphosignaling","rows":[{"observation":"After 12 hours under ultra-low-attachment conditions, PTPN14-knockout MDA-MB-231 cells have higher AKT Ser473 and ERK1/2 phosphorylation than control cells."}]}],"target_experiment":{"model":"MDA-MB-231 cells implanted in female BALB/c nude mice, approximately 4–5 weeks old","perturbation":"stable CRISPR PTPN14 knockout before implantation","comparator":"sgControl MDA-MB-231 cells","condition":"8 x 10^5 cells injected into the right fourth mammary fat pad; four mice per group","endpoint":"excised orthotopic tumor weight","time":"approximately 6 weeks after implantation"},"question":"Predict whether the PTPN14-knockout tumors have higher or lower excised weight.","options":{"A":"Lower tumor weight.","B":"Higher tumor weight."},"language":"en","evaluation_mode":"empirical_phenotype_prediction","response_schema":{"type":"string","enum":["A","B"]},"output_instruction":"Output only A or B."}

## Options

A. Lower tumor weight.
B. Higher tumor weight.
