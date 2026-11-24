---
bench_id: "D-C4-01"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Binary): Predict the direction of the tumor-cell apopt"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

{"id":"D-C4-01","task_type":"Binary","biological_context":"PRMT1 is a protein arginine methyltransferase involved in protein and transcriptional regulation. RIPK1 participates in death-receptor signaling and can scaffold prosurvival signaling; loss of a scaffold is not equivalent to inhibiting its kinase activity. CASP8 links death receptors to apoptosis, while BCL2L1 restrains mitochondrial apoptosis. Monoculture dependency and immune-mediated killing need not have the same direction.","evidence_blocks":[{"assay":"Frozen Sanger/Behan 2019 cancer dependency map, separate single-gene knockout experiments in standard monoculture. More negative CRISPRcleaned depletion log-fold change indicates greater loss of cell fitness. Values are not CERES or fractions of dead cells. These reference measurements precede the independent target study.","rows":[{"gene":"CASP8","model":"NCI-H1299","CRISPRcleaned_depletion_logFC":-0.0378},{"gene":"BCL2L1","model":"NCI-H2023","CRISPRcleaned_depletion_logFC":-0.3236},{"gene":"CASP8","model":"NCI-H2023","CRISPRcleaned_depletion_logFC":0.2587},{"gene":"PRMT1","model":"NCI-H1299","CRISPRcleaned_depletion_logFC":-1.5076},{"gene":"PRMT1","model":"NCI-H2023","CRISPRcleaned_depletion_logFC":-2.8683},{"gene":"RIPK1","model":"A549","CRISPRcleaned_depletion_logFC":0.0012},{"gene":"BCL2L1","model":"NCI-H1299","CRISPRcleaned_depletion_logFC":-0.1235},{"gene":"RIPK1","model":"NCI-H1299","CRISPRcleaned_depletion_logFC":0.2924},{"gene":"CASP8","model":"A549","CRISPRcleaned_depletion_logFC":0.0754},{"gene":"BCL2L1","model":"A549","CRISPRcleaned_depletion_logFC":-1.3402},{"gene":"PRMT1","model":"A549","CRISPRcleaned_depletion_logFC":-1.6225},{"gene":"RIPK1","model":"NCI-H2023","CRISPRcleaned_depletion_logFC":0.1742}]},{"assay":"Tumor antigen and restriction background","rows":[{"observation":"H2023 lung cancer cells express MAGE-B2 and HLA-A0201; the T cells carry a human HLA-A2-restricted, MAGE-B2-specific TCR."}]}],"target_experiment":{"model":"H2023 (NCI-H2023) human lung cancer cells expressing Cas9","perturbation":"PRMT1 knockout with two independently validated sgRNAs","comparator":"non-targeting sgRNA tumor cells exposed to the same T cells","condition":"HLA-A2-restricted MAGE-B2-specific TCR T cells; effector:target ratio 3:1; 37 degrees C","endpoint":"fraction of tumor cells positive for cleaved caspase-3 by flow cytometry","time":"4 hours of co-incubation, as specified for the human validation in Figure 3C–D"},"question":"Predict the direction of the tumor-cell apoptosis fraction after PRMT1 knockout in this co-culture.","options":{"A":"Higher cleaved-caspase-3-positive tumor-cell fraction.","B":"Lower cleaved-caspase-3-positive tumor-cell fraction."},"language":"en","evaluation_mode":"empirical_phenotype_prediction","response_schema":{"type":"string","enum":["A","B"]},"output_instruction":"Output only A or B."}

## Options

A. Higher cleaved-caspase-3-positive tumor-cell fraction.
B. Lower cleaved-caspase-3-positive tumor-cell fraction.
