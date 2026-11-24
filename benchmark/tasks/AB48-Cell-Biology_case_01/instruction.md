---
bench_id: AB48-Cell-Biology_case_01
category: "Cell-Biology"
title: "Predicting VEGF-dependent enhancement of cellular PD1 blockade"
format: ranking
task_type: "ranking"
input_mode: "single_case_csv"
pass_threshold: 0.8
---

# Prompt
Use only the supplied CSV and study information. Do not browse, execute code, use tools or provide explanations. Predict the fold enhancement of PD1 reporter blockade produced by1.25nM humanVEGF-A165 in the source coculture bioassay. Define enhancement as IC50 withoutVEGF divided by IC50 withVEGF; larger values mean stronger conditional potency gain. Both conditions use antiCD3/PD-L1 aAPC CHO-K1 cells cocultured with PD1-effector cells for6h. Human/cynomolgus PD1SPR and cellularIC50 withoutVEGF are visible; the withVEGF values and all ratios for new constructs are withheld. AK112 is a visible reference. MissingSPR remainsblank. This is a context-effect prediction, not inference of clinical efficacy. The target IDs are candidate_02, candidate_03, candidate_04, candidate_05, candidate_06, candidate_07. Return only one comma-separated line containing every target ID once, from highest to lowest conditional enhancement.

name,format,human_PD1_KD_nM,cyno_PD1_KD_nM,PD1_reporter_without_VEGF_IC50_nM,conditional_enhancement_fold
candidate_01,VEGF_PD1_bispecific_IgG_scFv,39.6,12.5,1,30.3030303030303
candidate_02,VEGF_PD1_bispecific_IgG_scFv,49.1,,1.5,
candidate_03,VEGF_PD1_bispecific_IgG_scFv,45.7,7.15,0.71,
candidate_04,VEGF_PD1_bispecific_IgG_scFv,47.4,,0.92,
candidate_05,VEGF_PD1_bispecific_IgG_scFv,,7.06,1.3,
candidate_06,VEGF_PD1_bispecific_IgG_scFv,31.5,4.33,0.55,
candidate_07,VEGF_PD1_bispecific_IgG_scFv,46.1,7.61,1.1,
