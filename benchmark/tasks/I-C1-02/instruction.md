---
bench_id: "I-C1-02"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Binary): Predict whether normalized percent body fat i"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

{"id":"I-C1-02","task_type":"Binary","biological_context":"DDAH1 regulates methylarginine metabolism, which can influence nitric-oxide-related vascular and metabolic signaling. Basal glucose handling and triglyceride phenotypes do not directly measure fat accumulation under dietary excess. The IMPC reference allele is distinct from the Lexicon gene-trap line in the target experiment.","evidence_blocks":[{"assay":"Frozen IMPC baseline metabolic phenotyping. Each number is a knockout-to-wild-type group-mean ratio, not a standardized effect or evidence of significance. Different centers and sexes are retained. Cohort age and strain details are not encoded in these summary cells; these are reference cohorts, not the later independent experimental animals.","rows":[{"gene":"Slc25a4","mgi_gene_id":"MGI:1353495","ensembl_gene_id":11739,"center":"WTSI","zygosity":"homozygote","phenotype":"IPGTT AUC 0-120 male","KO_to_WT_ratio":0.490479},{"gene":"Ucp1","mgi_gene_id":"MGI:98894","ensembl_gene_id":22227,"center":"HMGU","zygosity":"homozygote","phenotype":"Triglycerides male","KO_to_WT_ratio":0.779511},{"gene":"Slc25a4","mgi_gene_id":"MGI:1353495","ensembl_gene_id":11739,"center":"WTSI","zygosity":"homozygote","phenotype":"Triglycerides male","KO_to_WT_ratio":0.809446},{"gene":"Ncs1","mgi_gene_id":"MGI:109166","ensembl_gene_id":14299,"center":"ICS","zygosity":"homozygote","phenotype":"IPGTT AUC 0-120 male","KO_to_WT_ratio":0.897459},{"gene":"Ddah1","mgi_gene_id":"MGI:1916469","ensembl_gene_id":69219,"center":"WTSI","zygosity":"homozygote","phenotype":"IPGTT t0 male","KO_to_WT_ratio":1.016052},{"gene":"Slc25a4","mgi_gene_id":"MGI:1353495","ensembl_gene_id":11739,"center":"WTSI","zygosity":"homozygote","phenotype":"IPGTT t0 male","KO_to_WT_ratio":1.048666},{"gene":"Ddah1","mgi_gene_id":"MGI:1916469","ensembl_gene_id":69219,"center":"WTSI","zygosity":"homozygote","phenotype":"Triglycerides male","KO_to_WT_ratio":0.68289},{"gene":"Ucp1","mgi_gene_id":"MGI:98894","ensembl_gene_id":22227,"center":"HMGU","zygosity":"homozygote","phenotype":"IPGTT t0 male","KO_to_WT_ratio":1.000818},{"gene":"Ucp1","mgi_gene_id":"MGI:98894","ensembl_gene_id":22227,"center":"HMGU","zygosity":"homozygote","phenotype":"IPGTT AUC 0-120 male","KO_to_WT_ratio":1.065323},{"gene":"Ddah1","mgi_gene_id":"MGI:1916469","ensembl_gene_id":69219,"center":"WTSI","zygosity":"homozygote","phenotype":"IPGTT AUC 0-120 male","KO_to_WT_ratio":0.948133},{"gene":"Ncs1","mgi_gene_id":"MGI:109166","ensembl_gene_id":14299,"center":"ICS","zygosity":"homozygote","phenotype":"IPGTT t0 male","KO_to_WT_ratio":0.827498}]}],"target_experiment":{"model":"Lexicon Ddah1 gene-trap knockout line on mixed C57BL/6J x 129SvEv background","perturbation":"constitutive Ddah1 disruption by gene trap","comparator":"wild-type littermates; n=8 per genotype","condition":"D12451 high-fat diet, 45% energy from fat, from weaning","endpoint":"percent body fat measured by quantitative magnetic resonance, normalized to wild-type mean=100","time":"male mice at 11 weeks of age"},"question":"Predict whether normalized percent body fat is higher or lower in the knockout after high-fat feeding.","options":{"A":"Lower than the matched control.","B":"Higher than the matched control."},"language":"en","evaluation_mode":"empirical_phenotype_prediction","response_schema":{"type":"string","enum":["A","B"]},"output_instruction":"Output only A or B."}

## Options

A. Lower than the matched control.
B. Higher than the matched control.
