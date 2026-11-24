---
bench_id: AB70-In-vivo-Study_case_01
category: "In-vivo-Study"
title: "Predicting cynomolgus clearance of a dual ActRII antibody"
format: regression
task_type: "numeric"
input_mode: "single_case_csv"
pass_threshold: 0.9
---

# Prompt
Predict ofaschlupfer total clearance (mL/h/kg) after a single 30 mg/kg IV dose in cynomolgus monkeys. Matched human receptor-binding results, a qualitative HIC comparison and the bimagrumab clearance reference are visible. Target AUC, Vss, half-life and other algebraic clearance proxies are withheld. Each group contained two animals; predict the reported finite-cohort mean. Use only the supplied CSV. Do not browse, execute code, call external tools or explain. Return only a JSON object mapping every target name to a positive numerical prediction.

name,role,format,human_ActRIIA_KD_pM,human_ActRIIB_KD_pM,HIC_vs_bimagrumab,cyno_IV30_clearance_mL_h_kg
ofaschlupfer,target,dual_ActRIIA_ActRIIB_antibody,20.0,3.0,lower_in_reported_comparison,
bimagrumab,reference,dual_ActRIIA_ActRIIB_antibody,197,2.0,reference,0.467
