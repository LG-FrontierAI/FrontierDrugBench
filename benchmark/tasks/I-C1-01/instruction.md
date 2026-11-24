---
bench_id: "I-C1-01"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Binary): Predict whether knockout mice accumulate more"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

{"id":"I-C1-01","task_type":"Binary","biological_context":"NCS-1 participates in calcium-dependent trafficking and membrane protein regulation. Insulin-responsive tissues contribute to glucose and lipid storage. The reference IMPC alleles and follow-up constitutive Ncs1-null line are independent; the latter was generated from a floxed Ncs1-EGFP construct using CMV-Cre and backcrossed to C57BL/6J.","evidence_blocks":[{"assay":"Frozen IMPC baseline metabolic phenotyping. Each number is a knockout-to-wild-type group-mean ratio, not a standardized effect or evidence of significance. Different centers and sexes are retained. Cohort age and strain details are not encoded in these summary cells; these are reference cohorts, not the later independent experimental animals.","rows":[{"gene":"Ddah1","mgi_gene_id":"MGI:1916469","ensembl_gene_id":69219,"center":"WTSI","zygosity":"homozygote","phenotype":"IPGTT AUC 0-120 male","KO_to_WT_ratio":0.948133},{"gene":"Ncs1","mgi_gene_id":"MGI:109166","ensembl_gene_id":14299,"center":"ICS","zygosity":"homozygote","phenotype":"IPGTT t0 male","KO_to_WT_ratio":0.827498},{"gene":"Ucp1","mgi_gene_id":"MGI:98894","ensembl_gene_id":22227,"center":"HMGU","zygosity":"homozygote","phenotype":"IPGTT AUC 0-120 male","KO_to_WT_ratio":1.065323},{"gene":"Ncs1","mgi_gene_id":"MGI:109166","ensembl_gene_id":14299,"center":"ICS","zygosity":"homozygote","phenotype":"IPGTT AUC 0-120 male","KO_to_WT_ratio":0.897459},{"gene":"Slc25a4","mgi_gene_id":"MGI:1353495","ensembl_gene_id":11739,"center":"WTSI","zygosity":"homozygote","phenotype":"IPGTT t0 male","KO_to_WT_ratio":1.048666},{"gene":"Slc25a4","mgi_gene_id":"MGI:1353495","ensembl_gene_id":11739,"center":"WTSI","zygosity":"homozygote","phenotype":"Body mass male","KO_to_WT_ratio":0.929891},{"gene":"Slc25a4","mgi_gene_id":"MGI:1353495","ensembl_gene_id":11739,"center":"WTSI","zygosity":"homozygote","phenotype":"IPGTT AUC 0-120 male","KO_to_WT_ratio":0.490479},{"gene":"Ucp1","mgi_gene_id":"MGI:98894","ensembl_gene_id":22227,"center":"HMGU","zygosity":"homozygote","phenotype":"IPGTT t0 male","KO_to_WT_ratio":1.000818},{"gene":"Ncs1","mgi_gene_id":"MGI:109166","ensembl_gene_id":14299,"center":"ICS","zygosity":"homozygote","phenotype":"Body mass male","KO_to_WT_ratio":1.064425},{"gene":"Ddah1","mgi_gene_id":"MGI:1916469","ensembl_gene_id":69219,"center":"WTSI","zygosity":"homozygote","phenotype":"IPGTT t0 male","KO_to_WT_ratio":1.016052}]},{"assay":"Adipocyte-membrane protein on ordinary chow","rows":[{"observation":"On normal chow, adipocyte-membrane insulin-receptor signal normalized to beta-actin is WT 0.61 +/- 0.04 (n=4) versus Ncs1-null 0.30 +/- 0.06 (n=4). NCS-1 is a calcium sensor associated with membrane protein regulation and forms a complex with the insulin receptor."}]}],"target_experiment":{"model":"male C57BL/6J Ncs1-null mice","perturbation":"whole-body Ncs1 knockout","comparator":"wild-type littermates on the same diet","condition":"ssniff EF R/M D12492 high-fat diet from 6 weeks of age","endpoint":"isolated fat-body mass in grams","time":"30 weeks of age"},"question":"Predict whether knockout mice accumulate more or less fat-body mass than wild-type controls.","options":{"A":"Higher than the matched control.","B":"Lower than the matched control."},"language":"en","evaluation_mode":"empirical_phenotype_prediction","response_schema":{"type":"string","enum":["A","B"]},"output_instruction":"Output only A or B."}

## Options

A. Higher than the matched control.
B. Lower than the matched control.
