---
bench_id: "D-C2-05"
category: "Disease-Biology"
title: "Perturbation fitness/dependency phenotype prediction (Rank): Rank the candidate knockouts from strongest t"
format: "ranking"
input_mode: "inline_prompt"
---

# Prompt

## Instructions

Answer this biological benchmark using only the content and data supplied in the question. Do not browse, search, use tools, or use remembered publications or their results as evidence. Reason from the supplied information. Return only the final answer in the exact minimal format specified by the question. Do not provide explanations, citations, confidence, or reasoning text.

## Task

{"id":"D-C2-05","task_type":"Rank","biological_context":"Oxidative phosphorylation, mitochondrial protein synthesis, redox control and carbon metabolism contribute differently to cancer-cell fitness. The table combines a frozen DepMap pan-cancer annotation with independently measured baseline growth-screen data. A pan-cancer common-essential label is not a U2OS-specific numerical CERES score. Glucose supports substantial glycolytic ATP production. Replacing glucose with galactose can increase reliance on mitochondrial respiration; amino acids, pyruvate and serum remain available, so this is not total nutrient starvation.","evidence_blocks":[{"assay":"Baseline normoxia-glucose U2OS screen: median sgRNA log2 fold change relative to plasmid library, library-depth normalized, shown separately for three independent repeats. More negative values mean greater depletion. These are not CERES scores. All selected genes remain visible.","rows":[{"gene":"PDE12","entrez_gene_id":201626,"functional_annotation":["Antiviral Response"],"DepMap_19Q3_common_essential":false,"baseline_glucose_screen_log2_fold_change_by_repeat":[-0.6964,-1.1817,-1.0306]},{"gene":"BDH1","entrez_gene_id":622,"functional_annotation":["Ketone Bodies Metabolism","Oxidative Phosphorylation"],"DepMap_19Q3_common_essential":false,"baseline_glucose_screen_log2_fold_change_by_repeat":[0.0064,-1.4319,0.1048]},{"gene":"TUFM","entrez_gene_id":7284,"functional_annotation":["Translation"],"DepMap_19Q3_common_essential":false,"baseline_glucose_screen_log2_fold_change_by_repeat":[-1.4597,-2.4808,-1.8764]}]}],"target_experiment":{"model":"human U2OS-HRE-luc osteosarcoma cells stably expressing Cas9","perturbation":"Separate CRISPR knockouts using the published library with at least five sgRNAs per gene","comparator":"parallel normoxia-glucose culture with the same genetic perturbation","condition":"Normoxia; glucose-free DMEM supplemented with 4.5 g/L galactose, 4 mM glutamine, 1 mM sodium pyruvate and 10% FCS after galactose preconditioning","endpoint":"condition-dependent competitive cell fitness, measured by depth-normalized sgRNA representation relative to the parallel glucose-normoxia culture","time":"5-day condition exposure after 14–15 days of selection/expansion; three independently transduced screen repeats"},"candidate_ids":["PDE12","TUFM","BDH1"],"question":"Rank the candidate knockouts from strongest to weakest fitness loss in galactose relative to normoxia-glucose.","language":"en","evaluation_mode":"empirical_phenotype_prediction","response_schema":{"type":"array","items":{"type":"string","enum":["PDE12","TUFM","BDH1"]},"minItems":3,"maxItems":3,"uniqueItems":true},"output_instruction":"Output only a JSON array of candidate IDs."}
