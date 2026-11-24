---
bench_id: AB73-In-vivo-Study_case_01
category: "In-vivo-Study"
title: "Predicting how TfR-affinity engineering changes brain pharmacodynamics"
format: regression
task_type: "numeric"
input_mode: "single_case_csv"
pass_threshold: 0.9
---

# Prompt
Predict day-7 brain BMP22:6, relative to the assay internal standard, for affinity_weak_1 and affinity_weak_2. The 10 nM TfR-binding parent is a visible PD anchor. Constructs have the same PGRN-fusion format and receive 5 mg/kg IV in Grn-knockout mice. This is affinity-engineering transfer at a fixed dose and endpoint. Weaker TfR affinity need not give a monotonic change in brain pharmacodynamics. BMP22:6 is not a percentage of healthy rescue. Use only the supplied CSV. Do not browse, execute code, call external tools or explain. Return only a JSON object mapping every target name to a positive numerical prediction.

name,TfR_KD_nM,format,dose_mg_kg,day7_BMP22_6
affinity_parent,10,10E10_PGRN_fusion,5,0.78
affinity_weak_1,300,10E10_PGRN_fusion,5,
affinity_weak_2,1000,10E10_PGRN_fusion,5,
