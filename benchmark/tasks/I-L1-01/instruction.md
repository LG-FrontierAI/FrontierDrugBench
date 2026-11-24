---
bench_id: "I-L1-01"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Binary): Predict whether adrenergically stimulated who"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

{"id":"I-L1-01","task_type":"Binary","biological_context":"Slc8b1 encodes NCLX, the mitochondrial sodium/calcium exchanger. Adrenergic activation raises calcium and activates UCP1-mediated proton leak; sustained mitochondrial calcium overload can limit respiration. IMPC basal measurements do not represent a cold challenge. The literature uses C57BL/6NJ Slc8b1-em1(IMPC)J/J null mice; this is a separate cohort from the baseline panels.","evidence_blocks":[{"assay":"Frozen IMPC baseline metabolic phenotyping. Each number is a knockout-to-wild-type group-mean ratio, not a standardized effect or evidence of significance. Different centers and sexes are retained. Cohort age and strain details are not encoded in these summary cells; these are reference cohorts, not the later independent experimental animals.","rows":[{"gene":"Ucp1","mgi_gene_id":"MGI:98894","ensembl_gene_id":22227,"center":"HMGU","zygosity":"homozygote","phenotype":"Metabolic rate male","KO_to_WT_ratio":0.969196},{"gene":"Slc25a4","mgi_gene_id":"MGI:1353495","ensembl_gene_id":11739,"center":"WTSI","zygosity":"homozygote","phenotype":"Body mass female","KO_to_WT_ratio":0.861832},{"gene":"Slc8b1","mgi_gene_id":"MGI:2180781","ensembl_gene_id":170756,"center":"JAX","zygosity":"homozygote","phenotype":"Body mass female","KO_to_WT_ratio":0.933832},{"gene":"Slc8b1","mgi_gene_id":"MGI:2180781","ensembl_gene_id":170756,"center":"JAX","zygosity":"homozygote","phenotype":"Body mass male","KO_to_WT_ratio":0.906628},{"gene":"Slc25a4","mgi_gene_id":"MGI:1353495","ensembl_gene_id":11739,"center":"WTSI","zygosity":"homozygote","phenotype":"Body mass male","KO_to_WT_ratio":0.929891},{"gene":"Slc25a4","mgi_gene_id":"MGI:1353495","ensembl_gene_id":11739,"center":"WTSI","zygosity":"homozygote","phenotype":"Oxygen consumption male","KO_to_WT_ratio":1.08996},{"gene":"Ucp1","mgi_gene_id":"MGI:98894","ensembl_gene_id":22227,"center":"HMGU","zygosity":"homozygote","phenotype":"Oxygen consumption male","KO_to_WT_ratio":0.965723},{"gene":"Slc25a4","mgi_gene_id":"MGI:1353495","ensembl_gene_id":11739,"center":"WTSI","zygosity":"homozygote","phenotype":"Metabolic rate male","KO_to_WT_ratio":1.08579}]},{"assay":"Independent isolated brown-adipocyte bioenergetics","rows":[{"observation":"In isolated brown adipocytes, NCLX deletion reduces the norepinephrine-evoked respiratory response by 45%; FCCP-stimulated maximal respiration after norepinephrine is 426.2 +/- 36.86% of basal in WT versus 173.8 +/- 19.37% in knockout. Mitochondrial calcium efflux is impaired despite retained calcium entry."}]}],"target_experiment":{"model":"C57BL/6NJ Slc8b1/NCLX whole-body knockout mice","perturbation":"constitutive homozygous Slc8b1 deletion","comparator":"age- and sex-matched wild-type mice","condition":"30 degrees C thermoneutrality; pentobarbital anesthesia 120 mg/kg; subcutaneous CL-316,243 1 mg/kg after 45–60 minutes baseline","endpoint":"whole-body oxygen consumption response to beta-3 adrenergic stimulation","time":"acute stimulation trace after CL-316,243 injection; WT n=5, KO n=6"},"question":"Predict whether adrenergically stimulated whole-body oxygen consumption is lower or higher in knockout mice.","options":{"A":"Lower than the matched control.","B":"Higher than the matched control."},"language":"en","evaluation_mode":"empirical_phenotype_prediction","response_schema":{"type":"string","enum":["A","B"]},"output_instruction":"Output only A or B."}

## Options

A. Lower than the matched control.
B. Higher than the matched control.
