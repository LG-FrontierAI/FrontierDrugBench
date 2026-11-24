---
bench_id: AB65-In-vivo-Study_case_01
category: "In-vivo-Study"
title: "Predicting long-term lysosomal biomarker durability"
format: ranking
task_type: "ranking"
input_mode: "single_case_csv"
pass_threshold: 0.85
---

# Prompt
Rank all six construct–dose regimens from highest to lowest observed day-63 brain BMP22:6. Early values through day 14 are visible; days 21, 35 and 63 are withheld. Regimens comprise two PGRN-fusion architectures at three IV doses in Grn-knockout mice. The endpoint is relative to the internal standard, not percent healthy rescue. Only organizer-frozen pairs with nonoverlapping mean ± reported-SD intervals are scored. Use only the CSV; do not call tools or explain. Return one comma-separated line containing all six names.

The following study information applies to this case:

WO2024263567A2 Example3 Table5; singleIV1.5/5/15mg/kg; GrnKO; day1/4/7/14 earlydata; hidden day63 experimental groupmeans. Table1 mapsKappaEx5 HC34/LC35 andEx6 HC34/LC36.

name,format,PGRN_payload,TfR_shuttle,albumin_binding_domain,dose_mg_kg,route,BMP22_6_day1,BMP22_6_day4,BMP22_6_day7,BMP22_6_day14,BMP22_6_day63
kappa5_1p5,10E10_Fab_albumin_binding_PGRN_fusion,full_length,10E10,C80.43,1.5,IV,0.7,1.0,0.89,0.87,
kappa5_5,10E10_Fab_albumin_binding_PGRN_fusion,full_length,10E10,C80.43,5,IV,1.01,1.1,1.06,0.98,
kappa5_15,10E10_Fab_albumin_binding_PGRN_fusion,full_length,10E10,C80.43,15,IV,0.95,1.15,1.15,1.26,
kappa6_1p5,10E10_Fab_albumin_binding_PGRN_fusion,delta_pGF,10E10,C80.43,1.5,IV,0.9,1.01,1.02,0.95,
kappa6_5,10E10_Fab_albumin_binding_PGRN_fusion,delta_pGF,10E10,C80.43,5,IV,0.87,1.22,1.1,1.13,
kappa6_15,10E10_Fab_albumin_binding_PGRN_fusion,delta_pGF,10E10,C80.43,15,IV,0.93,1.19,1.14,1.16,
