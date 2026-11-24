---
bench_id: "I-L2-01"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Binary): Predict the direction of the ejection-fractio"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

{"id":"I-L2-01","task_type":"Binary","biological_context":"Ric8b acts as a chaperone/regulator of stimulatory G proteins. Beta-adrenergic signaling recruits calcium entry and contractility. Baseline organ size alone does not specify contractile performance. The IMPC Ric8b reference is a systemic heterozygous tm1b allele; the target is adult cardiac-specific biallelic deletion from an exon-4-floxed tm1c allele.","evidence_blocks":[{"assay":"IMPC release 05.0 reference genotypes. Percentage change is the database-reported change versus its matched wild-type controls. Categorical annotations are not quantitative effect sizes. Records below are not from the independent target experiment.","rows":[{"marker_symbol":"Ric8b","marker_accession_id":"MGI:2682307","allele_symbol":"Ric8b<tm1b(EUCOMM)Hmgu>","allele_accession_id":"MGI:5548860","strain_name":"C57BL/6NTac","phenotyping_center":"MRC Harwell","sex":"male","zygosity":"heterozygote","parameter_name":"Lean mass","percentage_change":"-15.21%","mp_term_name":"decreased lean body mass"},{"marker_symbol":"Ric8b","marker_accession_id":"MGI:2682307","allele_symbol":"Ric8b<tm1b(EUCOMM)Hmgu>","allele_accession_id":"MGI:5548860","strain_name":"C57BL/6NTac","phenotyping_center":"MRC Harwell","sex":"male","zygosity":"heterozygote","parameter_name":"Heart weight","percentage_change":"-17.52%","mp_term_name":"decreased heart weight"},{"marker_symbol":"Pink1","marker_accession_id":"MGI:1916193","allele_symbol":"Pink1<tm1b(EUCOMM)Wtsi>","allele_accession_id":"MGI:5637036","strain_name":"C57BL/6NTac","phenotyping_center":"MRC Harwell","sex":"male","zygosity":"homozygote","parameter_name":"Heart weight","percentage_change":"18.98%","mp_term_name":"increased heart weight"},{"marker_symbol":"Slc25a4","marker_accession_id":"MGI:1353495","allele_symbol":"Slc25a4<tm1a(EUCOMM)Wtsi>","allele_accession_id":"MGI:4432177","strain_name":"C57BL/6N","phenotyping_center":"WTSI","sex":"male","zygosity":"homozygote","parameter_name":"Heart weight","percentage_change":"35.83%","mp_term_name":"increased heart weight"}]},{"assay":"Independent isolated ventricular-myocyte patch clamp","rows":[{"observation":"Isolated ventricular-myocyte L-type calcium current density: control basal -3.12 +/- 0.43 pA/pF (n=12 cells), Ric8b-deleted basal -3.92 +/- 0.32 (n=11); after 10 micromolar isoprenaline, control -8.70 +/- 0.75, deleted -4.65 +/- 0.56. The article text and caption differ on the voltage; no voltage-specific quantitative transfer is requested."}]}],"target_experiment":{"model":"10–12-week-old Ric8b flox/flox; alpha-MHC-MerCreMer mice","perturbation":"Tamoxifen-induced cardiomyocyte Ric8b deletion, 3-day induction","comparator":"tamoxifen-treated control littermates, with pre-induction measurements","condition":"standard chow, normal housing","endpoint":"left-ventricular ejection fraction by echocardiography","time":"48 hours after last tamoxifen injection"},"question":"Predict the direction of the ejection-fraction response after cardiac Ric8b deletion.","options":{"A":"Lower than the matched control.","B":"Higher than the matched control."},"language":"en","evaluation_mode":"empirical_phenotype_prediction","response_schema":{"type":"string","enum":["A","B"]},"output_instruction":"Output only A or B."}

## Options

A. Lower than the matched control.
B. Higher than the matched control.
