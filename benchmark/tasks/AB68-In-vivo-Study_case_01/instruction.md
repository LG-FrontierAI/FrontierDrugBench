---
bench_id: AB68-In-vivo-Study_case_01
category: "In-vivo-Study"
title: "Predicting detergent-extracted brain exposure from soluble-fraction data"
format: regression
task_type: "numeric"
input_mode: "single_case_csv"
pass_threshold: 0.6
---

# Prompt
Predict 48-hour RIPA-extracted brain PGRN concentration (pg/mg wet tissue) for sandwich1_h48, sandwich2_h48 and kappa3_h48. Measurements through 24 hours, corresponding 48-hour PBS-soluble values and the older PTV11 profile are visible. Target RIPA and CSF results are withheld. PBS and RIPA are distinct extraction fractions; infer detergent-associated retention without treating the fractions as interchangeable free-drug measurements. Use only the supplied CSV. Do not browse, execute code, call external tools or explain. Return only a JSON object mapping every target name to a positive numerical prediction.

name,construct,architecture,payload,time_h,brain_PBS_pg_mg,brain_RIPA_pg_mg,CSF_pg_mL
sandwich1_h1,sandwich1,H09-PGRN-C90.43,full_length,1,11.91,149.82,12420.2
sandwich1_h6,sandwich1,H09-PGRN-C90.43,full_length,6,7.78,89.22,3152.94
sandwich1_h10,sandwich1,H09-PGRN-C90.43,full_length,10,4.03,30.32,1290.79
sandwich1_h24,sandwich1,H09-PGRN-C90.43,full_length,24,0.59,3.09,134.69
sandwich1_h48,sandwich1,H09-PGRN-C90.43,full_length,48,0.35,,
sandwich2_h1,sandwich2,H09-dPGF-C90.43,delta_pGF,1,10.52,129.56,10847.96
sandwich2_h4,sandwich2,H09-dPGF-C90.43,delta_pGF,4,16.58,121.39,12739.72
sandwich2_h9,sandwich2,H09-dPGF-C90.43,delta_pGF,9,17.16,83.38,11763.27
sandwich2_h24,sandwich2,H09-dPGF-C90.43,delta_pGF,24,4.14,12.04,1346.26
sandwich2_h48,sandwich2,H09-dPGF-C90.43,delta_pGF,48,0.63,,
kappa3_h1,kappa3,H09-C90.43_H09-PGRN,full_length,1,6.22,121.71,7002.73
kappa3_h6,kappa3,H09-C90.43_H09-PGRN,full_length,6,3.56,53.9,1579.28
kappa3_h10,kappa3,H09-C90.43_H09-PGRN,full_length,10,1.47,21.18,880.79
kappa3_h24,kappa3,H09-C90.43_H09-PGRN,full_length,24,0.57,2.23,76.3
kappa3_h48,kappa3,H09-C90.43_H09-PGRN,full_length,48,0.11,,
PTV11_h1,PTV11,literature_Fc_PGRN,full_length,1,3.63,34.4,1257.05
PTV11_h6,PTV11,literature_Fc_PGRN,full_length,6,2.21,11.59,793.28
PTV11_h10,PTV11,literature_Fc_PGRN,full_length,10,1.82,2.5,480.76
PTV11_h24,PTV11,literature_Fc_PGRN,full_length,24,1.57,1.99,205.95
PTV11_h48,PTV11,literature_Fc_PGRN,full_length,48,0.31,1.62,124.33
