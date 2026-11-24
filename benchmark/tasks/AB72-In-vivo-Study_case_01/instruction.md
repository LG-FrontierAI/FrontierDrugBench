---
bench_id: AB72-In-vivo-Study_case_01
category: "In-vivo-Study"
title: "Extrapolating high-dose primate exposure of an anti-PRLR antibody"
format: regression
task_type: "numeric"
input_mode: "single_case_csv"
pass_threshold: 0.95
---

# Prompt
Predict total serum AUCinf (h·µg/mL) for ABS_201_300 after a single 300 mg/kg IV dose in cynomolgus monkeys. The matched 100 mg/kg cohort is visible. Target 300 mg/kg Cmax, clearance, half-life and all derived exposure parameters are withheld. Dose proportionality is a baseline assumption to test, not an observed answer. Each cohort contained two male and two female animals. Preserve the source label ABS-201 without assuming every AB001 alias identifies the same construct. Use only the supplied CSV. Do not browse, execute code, call external tools or explain. Return only a JSON object mapping every target name to a positive numerical prediction.

name,dose_mg_kg,route,male_female_counts,AUC0_336_h_ug_mL,AUCinf_h_ug_mL
ABS_201_100,100,IV,2/2,206000,426000
ABS_201_300,300,IV,2/2,,
