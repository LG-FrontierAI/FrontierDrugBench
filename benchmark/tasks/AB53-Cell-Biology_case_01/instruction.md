---
bench_id: AB53-Cell-Biology_case_01
category: "Cell-Biology"
title: "Interpreting cell binding, avidity and engineered signaling evidence"
format: open_rubric
task_type: "review"
input_mode: "single_case_csv"
pass_threshold: 0.8
---

# Prompt
Review these claims: (1)the lowest FACS EC50 proves the strongest intrinsic monovalent KD;(2)strong cell binding is sufficient to predict TREM2 agonism;(3)the BLI1:1 fit proves avidity is absent;(4)the engineered NFAT assay alone establishes physiological microglial efficacy. Give a corrected conclusion and two immediate discriminating checks, with the question each check resolves.

Use only the supplied CSV. Do not browse, execute code or use tools. Answer in English. Give a structured scientific review with source-row references.

The following study information applies to this case:

The rows are final reported results or explicitly stated assay methods; absent quantitative outcomes are not fabricated. Source units and missing statuses are preserved.

name,assay,source_location,molecule_or_panel,endpoint,reported_value,reported_unit,status_or_condition
record_01,cellbinding,Table2,22A17,FACS_EC50,0.1,ug/mL,humanHEK293T
record_02,signaling,Example3,22A17,NFAT_EC50,0.04,ug/mL,humanTREM2_reporter
record_03,cellbinding,Table2,08B23,FACS_EC50,0.6,ug/mL,humanHEK293T
record_04,signaling,Example3,08B23,functional_class,,,inverse_agonist
record_05,BLI,Example4,panel,assay_method,,,AHC_capture60s;humanTREM2_Fc100to6.25nM;association200s;dissociation200s;global1to1
