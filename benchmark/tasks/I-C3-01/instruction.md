---
bench_id: "I-C3-01"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Binary): Predict whether lung bacterial burden is high"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

{"id":"I-C3-01","task_type":"Binary","biological_context":"STAT1 transduces type I, II and III interferon responses; IRF8 contributes to myeloid differentiation and CYBB supports phagocyte oxidant production. Enlarged lymph nodes or altered circulating cell indices alone do not establish pathogen control. The IMPC Stat1 tm2b reference and the independent Stat1 tm1Dlv/J infection model are separate null alleles.","evidence_blocks":[{"assay":"IMPC release 05.0 reference genotypes. Percentage change is the database-reported change versus its matched wild-type controls. Categorical annotations are not quantitative effect sizes. Records below are not from the independent target experiment.","rows":[{"marker_symbol":"Cybb","marker_accession_id":"MGI:88574","allele_symbol":"Cybb<tm2b(KOMP)Wtsi>","allele_accession_id":"MGI:5548926","strain_name":"C57BL/6NTac","phenotyping_center":"MRC Harwell","sex":"female","zygosity":"homozygote","parameter_name":"Spleen weight","percentage_change":"28.18%","mp_term_name":"increased spleen weight"},{"marker_symbol":"Stat1","marker_accession_id":"MGI:103063","allele_symbol":"Stat1<tm2b(EUCOMM)Wtsi>","allele_accession_id":"MGI:5766744","strain_name":"C57BL/6N","phenotyping_center":"ICS","sex":"male","zygosity":"homozygote","parameter_name":"Lymph node","percentage_change":"","mp_term_name":"enlarged lymph nodes"},{"marker_symbol":"Irf8","marker_accession_id":"MGI:96395","allele_symbol":"Irf8<tm1b(KOMP)Wtsi>","allele_accession_id":"MGI:5446132","strain_name":"C57BL/6NJ","phenotyping_center":"JAX","sex":"male","zygosity":"homozygote","parameter_name":"Platelet count","percentage_change":"-40.91%","mp_term_name":"thrombocytopenia"},{"marker_symbol":"Stat1","marker_accession_id":"MGI:103063","allele_symbol":"Stat1<tm2b(EUCOMM)Wtsi>","allele_accession_id":"MGI:5766744","strain_name":"C57BL/6N","phenotyping_center":"ICS","sex":"male","zygosity":"homozygote","parameter_name":"Mean corpuscular hemoglobin","percentage_change":"-15.01%","mp_term_name":"decreased mean corpuscular hemoglobin"}]}],"target_experiment":{"model":"8–16-week-old B6.129S(Cg)-Stat1 tm1Dlv/J knockout mice, backcrossed to C57BL/6J; age- and sex-matched controls","perturbation":"global Stat1 knockout","comparator":"wild-type littermates/C57BL/6J controls housed in the same room for at least 4 weeks","condition":"intratracheal inoculation of 1,000 CFU K. pneumoniae W42, a hypervirulent K1 clinical respiratory isolate, in 100 microliters","endpoint":"viable bacterial burden in left-lung homogenate, CFU/ml","time":"48 hours after inoculation"},"question":"Predict whether lung bacterial burden is higher or lower in knockout mice.","options":{"A":"Higher than the matched control.","B":"Lower than the matched control."},"language":"en","evaluation_mode":"empirical_phenotype_prediction","response_schema":{"type":"string","enum":["A","B"]},"output_instruction":"Output only A or B."}

## Options

A. Higher than the matched control.
B. Lower than the matched control.
