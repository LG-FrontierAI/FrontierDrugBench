---
bench_id: "D-ENV-022"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Rank): Rank the candidate knockouts from strongest t"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

{"id":"D-ENV-022","task_type":"Rank","biological_context":"Mitochondrial protein synthesis, respiratory-chain assembly, substrate oxidation and redox control can affect cell fitness differently across environments. The table supplies actual baseline U2OS knockout measurements and a frozen pan-cancer DepMap annotation for every selected gene. Common-essential is a categorical annotation, not a U2OS-specific CERES score.Glucose permits glycolytic ATP production. Galactose substitution increases reliance on oxidative metabolism, while glutamine, pyruvate and serum remain available; this is not complete nutrient starvation.","evidence_blocks":[{"assay":"Baseline glucose-normoxia: median guide log2 fold change relative to plasmid library after sequencing-depth normalization. Three repeat values are shown separately; more negative means greater depletion. Scores are not CERES. All target-gene baseline data remain visible.","rows":[{"gene":"ABHD11","entrez_gene_id":83451,"functional_annotation":["Unknown"],"guides_per_repeat":[5,5,5],"DepMap_19Q3_common_essential":true,"baseline_glucose_log2_depletion_by_repeat":[0.1481,-0.212,-0.0165]},{"gene":"MRPS35","entrez_gene_id":60488,"functional_annotation":["Ribosome"],"guides_per_repeat":[5,5,5],"DepMap_19Q3_common_essential":true,"baseline_glucose_log2_depletion_by_repeat":[-0.2741,-0.6773,-0.9657]},{"gene":"ACO1","entrez_gene_id":48,"functional_annotation":["Citric Acid Cycle","DNA Damage Repair"],"guides_per_repeat":[5,5,5],"DepMap_19Q3_common_essential":false,"baseline_glucose_log2_depletion_by_repeat":[-0.4467,-1.0866,-0.239]}]}],"target_experiment":{"model":"human U2OS-HRE-luc osteosarcoma cells stably expressing Cas9","perturbation":"separate single-gene CRISPR knockout; multiple library guides per gene, with actual guide counts given in the input table","comparator":"parallel standard normoxia-glucose culture carrying the same genetic perturbation","condition":"normoxia; glucose-free DMEM with 4.5 g/L galactose, 4 mM glutamine, 1 mM sodium pyruvate and 10% FCS; galactose preconditioning","endpoint":"condition-dependent competitive fitness, measured by depth-normalized sgRNA representation relative to normoxia-glucose","time":"5-day challenge after 14–15 days of selection/expansion; three independently transduced repeat screens"},"candidate_ids":["MRPS35","ABHD11","ACO1"],"question":"Rank the candidate knockouts from strongest to weakest fitness loss in galactose relative to normoxia-glucose.","language":"en","evaluation_mode":"empirical_phenotype_prediction","response_schema":{"type":"array","items":{"type":"string","enum":["MRPS35","ABHD11","ACO1"]},"minItems":3,"maxItems":3,"uniqueItems":true},"output_instruction":"Output only a JSON array of candidate IDs."}
