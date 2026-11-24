---
bench_id: AB69-In-vivo-Study_case_01
category: "In-vivo-Study"
title: "Predicting HER2 nanobody persistence after multimerization and charge engineering"
format: regression
task_type: "numeric"
input_mode: "single_case_csv"
pass_threshold: 0.7
---

# Prompt
Predict the terminal beta-elimination half-life (hours) of HER2_trimer and HER2_negative_trimer. The HER2 monomer reference is visible. The constructs are one copy or three copies joined by 5-amino-acid flexible linkers; none contains an Fc. Negative charge engineering retained HER2 binding with an approximately 1.8-fold KD change versus the unmodified trimer. The experiment used six-week-old female BALB/c mice, 100 µg IP and terminal sampling through 24 hours, with selected trimer observations to 48 hours. Predict observed beta-phase persistence, not IV clearance. Use only the supplied CSV. Do not browse, execute code, call external tools or explain. Return only a JSON object mapping every target name to a positive numerical prediction.

name,target,oligomer_count,charge_engineering,terminal_half_life_h
HER2_monomer,HER2,1,unmodified,1.0
HER2_trimer,HER2,3,unmodified,
HER2_negative_trimer,HER2,3,negatively_charged_surface,
