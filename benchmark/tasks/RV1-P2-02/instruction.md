---
bench_id: "RV1-P2-02"
category: "Disease-Biology"
title: "Biochemical/cellular phenotype and candidate activity prediction (Binary): Will adding tariquidar enhance, rather than a"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content, definitions, evidence and numerical data supplied in this question. Do not browse, search, retrieve, call tools, use external files, consult previous questions or conversations, or use remembered publications, experimental outcomes, drug facts, or outside factual knowledge as evidence. Reason only from the supplied information. No tools are available. Return only the final option code, ordered candidate-ID JSON array, or candidate-ID set JSON array specified in the question. Do not include explanation, reasoning, confidence, citations, Markdown or any additional fields.

## Task

{"biological_context":"ABCB1 can limit intracellular exposure of substrates. tariquidar inhibits ABCB1 transport. Paclitaxel stabilizes microtubules and is an ABCB1 substrate; tepoxalin has a different pharmacologic mechanism. A viability signal and transporter abundance alone do not establish whether inhibiting ABCB1 will help a particular drug.","evaluation_mode":"empirical_phenotype_prediction","evidence_blocks":[{"assay":"Untreated CCLE RNA-seq, DepMap 19Q4; log2(TPM+1). Values rounded to four decimals. Expression is not a measurement of protein activity.","columns":["model","depmap_id","tissue","ABCB1","ABCC1","ABCG2"],"rows":[{"ABCB1":7.6695,"ABCC1":4.5577,"ABCG2":1.5211,"depmap_id":"ACH-000252","model":"LS1034","tissue":"colorectal"},{"ABCB1":6.9749,"ABCC1":4.9392,"ABCG2":1.2327,"depmap_id":"ACH-000997","model":"HCT15","tissue":"colorectal"},{"ABCB1":0.111,"ABCC1":4.5656,"ABCG2":2.101,"depmap_id":"ACH-000859","model":"HCC1954","tissue":"breast"}]},{"assay":"PRISM primary screen 19Q4: 2.5 micromolar drug for 5 days; replicate-collapsed log2 barcode signal relative to DMSO. Lower is a stronger relative viability/growth signal reduction; not an IC50 or an apoptosis measurement.","columns":["model","depmap_id","drug","log2_barcode_change"],"rows":[{"depmap_id":"ACH-000252","drug":"paclitaxel","log2_barcode_change":-2.5295,"model":"LS1034"},{"depmap_id":"ACH-000997","drug":"paclitaxel","log2_barcode_change":-4.0563,"model":"HCT15"},{"depmap_id":"ACH-000859","drug":"paclitaxel","log2_barcode_change":-5.1467,"model":"HCC1954"}]}],"id":"RV1-P2-02","language":"en","options":{"A":"Enhancement/synergy.","B":"Antagonism."},"output_instruction":"Return only one option code.","question":"Will adding tariquidar enhance, rather than antagonize, paclitaxel killing in the reported LS1034 dose-combination experiment?","target_experiment":{"comparator":"paclitaxel alone and tariquidar alone in the same combination matrix","condition":"Cell viability combination assay, assessed relative to the Bliss expectation of the two single-agent effects. For tepoxalin the question concerns the higher-exposure region above approximately 5 micromolar; individual untested combinations are excluded.","endpoint":"Qualitative enhancement versus antagonism of drug killing in the reported combination experiment","model":"LS1034 colorectal cancer cells","perturbation":"paclitaxel combined with the ABCB1 inhibitor tariquidar","time":"5-day combination viability assay; exact co-drug dose grid is not stated in the retrieved caption"},"task_type":"Binary"}

## Options

A. Enhancement/synergy.
B. Antagonism.
