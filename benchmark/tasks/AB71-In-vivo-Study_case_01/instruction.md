---
bench_id: AB71-In-vivo-Study_case_01
category: "In-vivo-Study"
title: "Predicting minipig subcutaneous bioavailability from a cross-route reference"
format: regression
task_type: "numeric"
input_mode: "single_case_csv"
pass_threshold: 0.9
---

# Prompt
Predict ofaschlupfer SC bioavailability as a fraction in Göttingen minipigs at 12 mg/kg SC relative to 12 mg/kg IV. Matched minipig IV exposure, monkey IV clearance and the bimagrumab reference are visible. Target SC AUC, Cmax and absorption parameters are withheld. Neither receptor affinity nor IV clearance uniquely determines absorption; interpret F using dose-normalized AUC. Use only the supplied CSV. Do not browse, execute code, call external tools or explain. Return only a JSON object mapping every target name to a positive numerical prediction.

name,role,format,human_ActRIIA_KD_pM,human_ActRIIB_KD_pM,HIC_vs_bimagrumab,cyno_IV30_clearance_mL_h_kg,cyno_IV30_Vss_mL_kg,minipig_IV12_AUC_ng_h_mL,minipig_SC12_bioavailability_fraction
ofaschlupfer,target,dual_ActRIIA_ActRIIB_antibody,20.0,3.0,lower_in_reported_comparison,0.16,113,25900000,
bimagrumab,reference,dual_ActRIIA_ActRIIB_antibody,197,2.0,reference,0.467,207,24200000,0.45
