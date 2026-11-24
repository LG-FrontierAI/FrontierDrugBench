---
bench_id: "RV1-K3-02"
category: "Disease-Biology"
title: "Biochemical/cellular phenotype and candidate activity prediction (Binary): Will adding IL-3 lower the ponatinib cellular"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content, definitions, evidence and numerical data supplied in this question. Do not browse, search, retrieve, call tools, use external files, consult previous questions or conversations, or use remembered publications, experimental outcomes, drug facts, or outside factual knowledge as evidence. Reason only from the supplied information. No tools are available. Return only the final option code, ordered candidate-ID JSON array, or candidate-ID set JSON array specified in the question. Do not include explanation, reasoning, confidence, citations, Markdown or any additional fields.

## Task

{"biological_context":"Ba/F3 is an IL-3-dependent murine pro-B model. Expression of active BCR-ABL can sustain growth without IL-3. T315 is a gatekeeper residue; E255 lies in the phosphate-binding loop; H396 lies in the activation loop. Ponatinib contains an ethynyl linker designed to accommodate the bulky T315I side chain. Mutations can still change potency, and exogenous IL-3 provides a growth signal outside BCR-ABL.","evaluation_mode":"empirical_phenotype_prediction","evidence_blocks":[{"assay":"Recombinant kinase catalytic inhibition by ponatinib/AP24534; IC50 in nM. Values beginning > are censored lower bounds. This concentration-response assay is separate from the 0.5 micromolar single-dose panel. Exact ATP concentrations are not supplied in this main-text table.","columns":["kinase","IC50_nM"],"rows":[{"IC50_nM":"0.37","kinase":"ABL"},{"IC50_nM":"2.0","kinase":"ABLT315I"},{"IC50_nM":"0.44","kinase":"ABLQ252H"},{"IC50_nM":"0.30","kinase":"ABLY253 F"},{"IC50_nM":"0.30","kinase":"ABLM351T"},{"IC50_nM":"0.34","kinase":"ABLH396P"},{"IC50_nM":"5.4","kinase":"c-SRC"},{"IC50_nM":"0.24","kinase":"LYN"},{"IC50_nM":"12.5","kinase":"c-KIT"},{"IC50_nM":"1.5","kinase":"VEGFR2"},{"IC50_nM":"2.2","kinase":"FGFR1"},{"IC50_nM":"1.1","kinase":"PDGFRα"},{"IC50_nM":">1000","kinase":"IR"},{"IC50_nM":">1000","kinase":"IGF-1R"},{"IC50_nM":">1000","kinase":"Aurora A"},{"IC50_nM":">1000","kinase":"CDK2/Cyclin E"}]}],"id":"RV1-K3-02","language":"en","options":{"A":"No.","B":"Yes."},"output_instruction":"Return only one option code.","question":"Will adding IL-3 lower the ponatinib cellular IC50 in BCR-ABL T315I-expressing Ba/F3 cells relative to the same genotype without IL-3?","target_experiment":{"comparator":"Vehicle-treated cells of each genotype and cytokine condition","condition":"RPMI 1640 with 10% FCS, 37 C, 5% CO2; 4,000 cells/well. MTS-based viability normalized to no drug. Three independent experiments in quadruplicate; genotype confirmed by RT-PCR and sequencing.","endpoint":"Cellular viability IC50 in nM","model":"Engineered Ba/F3: T315I + IL-3, T315I","perturbation":"Expression of the specified BCR-ABL variant, followed by graded ponatinib exposure; add IL-3 only where specified","time":"72 hours of ponatinib exposure"},"task_type":"Binary"}

## Options

A. No.
B. Yes.
