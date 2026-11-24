---
bench_id: AB54-Cell-Biology_case_01
category: "Cell-Biology"
title: "Separating uptake observations from TREM2-specific phagocytosis mechanism"
format: open_rubric
task_type: "review"
input_mode: "single_case_csv"
pass_threshold: 0.8
---

# Prompt
An analysis says all antibody-associated increases in the three BMDM pHrodo assays prove a common TREM2-dependent mechanism, each fluorescent readout directly measures the mass of internalized intact cargo, and all observed effects transfer to human microglia. Evaluate these claims using the assay and species evidence. Give two focused controls or follow-ups and explain the causal uncertainty each resolves. Do not invent numerical uptake results.

Use only the supplied CSV. Do not browse, execute code or use tools. Answer in English. Give a structured scientific review with source-row references.

The following study information applies to this case:

The rows are final reported results or explicitly stated assay methods; absent quantitative outcomes are not fabricated. Source units and missing statuses are preserved.

name,assay,source_location,molecule_or_panel,endpoint,reported_value,reported_unit,status_or_condition
record_01,sTREM2,Example6,antibodypanel,method,,,hiPSCTREM2HeterozygousorHomozygous;20ug/mL;72h;CD11bflow;secretedsTREM2ELISA;IncuCyte
record_02,A_beta,Example7A,antibodypanel,method,,,BMDM5e4/well;preincubate20ug/mL30min;pHrodoA_beta1_42_1ug/mL;1to3h;acidfluorescence
record_03,lipid,Example7B,antibodypanel,method,,,BMDM;20ug/mL;pHrodoPGPC/POPCfluorescentlipid1ug/mL;1to3h
record_04,apoptotic_cells,Example7C,antibodypanel,method,,,BMDM;20ug/mL;pHrodoSHSY5Yapoptoticcellsratio5to1;1to3h
record_05,mousebinding,Table2,02M10,status,,,no_binding
record_06,mousebinding,Table2,22A17,status,,,not_tested
