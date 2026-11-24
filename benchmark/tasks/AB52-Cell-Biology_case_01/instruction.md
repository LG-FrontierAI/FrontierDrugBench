---
bench_id: AB52-Cell-Biology_case_01
category: "Cell-Biology"
title: "Auditing units and censored endpoints before cell-potency modeling"
format: open_rubric
task_type: "review"
input_mode: "single_case_csv"
pass_threshold: 0.8
---

# Prompt
A proposed analysis converts every blank or no-binding mouse value tozero, changes the03O05 functional EC50 from0.5g/ml to0.5ug/ml without qualification, pools human binding and NFAT EC50 in one response column, and reports that03O05 has a verified3.6-fold functional potency gain relative to its human binding. Identify and correct every data-use error. State what can be retained quantitatively and what remains unresolved. Do not invent a corrected unit or censoring limit.

Use only the supplied CSV. Do not browse, execute code or use tools. Answer in English. Give a structured scientific review with source-row references.

The following study information applies to this case:

The rows are final reported results or explicitly stated assay methods; absent quantitative outcomes are not fabricated. Source units and missing statuses are preserved.

name,assay,source_location,molecule_or_panel,endpoint,reported_value,reported_unit,status_or_condition
record_01,binding_human,humanHEK293T FACS Table2,03O05,humanEC50,1.8,ug/mL,measured
record_02,binding_mouse,mouseHEK293T FACS Table2,03O05,mouseEC50,6.6,ug/mL,measured
record_03,binding_mouse,mouseHEK293T FACS Table2,02M10,mouseEC50,,ug/mL,no_binding
record_04,binding_mouse,mouseHEK293T FACS Table2,22A17,mouseEC50,,ug/mL,not_tested
record_05,binding_mouse,mouseHEK293T FACS Table2,23E21-2,mouseEC50,,ug/mL,not_tested
record_06,NFAT_reporter,Example3,03O05,functionalEC50,0.5,g/ml,reported_unit_conflict
record_07,NFAT_reporter,Example3,02M10,functionalEC50,0.5,ug/ml,measured
