---
bench_id: AB64-In-vivo-Study_case_01
category: "In-vivo-Study"
title: "Predicting primate persistence of PD-1–VEGF bispecific antibodies"
format: ranking
task_type: "ranking"
input_mode: "single_case_csv"
pass_threshold: 0.8
---

# Prompt
Rank the six target PD-1–VEGF bispecific antibodies from highest to lowest terminal serum half-life in the male cynomolgus IV study. AK112 is a visible same-study reference. Use matched binding, reporter and DSC measurements; missing measurements remain blank. Constructs ending .1L are distinct from .1La YTE constructs. The study used five males per group, body weights 2.5–3.9 kg, and serum follow-up through day 28. An IV dose is not specified in the accessible methods; do not infer one. Use only the supplied CSV. Do not browse, execute code, call external tools or explain. Return only one comma-separated line containing every target name, highest first.

name,role,format,human_PD1_KD_nM,cyno_PD1_KD_nM,PD1_reporter_without_VEGF_IC50_nM,PD1_reporter_with_VEGF_IC50_nM,VEGF_reporter_relative_IC50_nM,DSC_onset_C,DSC_Tm1_C,cyno_IV_half_life_days
AK112,reference,VEGF_PD1_bispecific_IgG_scFv,39.6,12.5,1,0.033,1,59.06,66.46,1.5
PAL054_0157_1L,target,VEGF_PD1_bispecific_IgG_scFv,45.7,7.15,0.71,0.23,1.1,57.54,62.88,
PAL054_0167_1L,target,VEGF_PD1_bispecific_IgG_scFv,49.1,,1.5,0.26,1.0,52.9,62.7,
PAL054_0168_1L,target,VEGF_PD1_bispecific_IgG_scFv,46.1,7.61,1.1,0.23,1.2,55.5,63.3,
PAL054_0169_1L,target,VEGF_PD1_bispecific_IgG_scFv,47.4,,0.92,0.24,1.1,54.5,62.8,
PAL054_0170_1L,target,VEGF_PD1_bispecific_IgG_scFv,31.5,4.33,0.55,0.2,1.0,58.8,65.8,
PAL054_0171_1L,target,VEGF_PD1_bispecific_IgG_scFv,,7.06,1.3,0.23,1.1,51.6,61.8,
