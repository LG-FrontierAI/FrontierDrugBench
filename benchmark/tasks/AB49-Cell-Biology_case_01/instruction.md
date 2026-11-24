---
bench_id: AB49-Cell-Biology_case_01
category: "Cell-Biology"
title: "Transferring VEGFR2 reporter inhibition to primary endothelial proliferation"
format: ranking
task_type: "ranking"
input_mode: "single_case_csv"
pass_threshold: 0.6
---

# Prompt
Use only the supplied CSV and study information. Do not browse, execute code, use tools or provide explanations. Predict the antibody concentration inhibiting VEGF-driven proliferation of primary human umbilical-vein endothelial cells. HUVECs undergo5h serum starvation, then0.125nM humanVEGF-A165 stimulation,48h incubation and CCK-8 readout after3h. Visible reporter results come from VEGFR2-NFAT-RE-luc2 HEK293 cells exposed to0.125nM VEGF for6h; the Emaxcolumn is normalized to the reference in that reporter experiment. These readouts are not interchangeable. AK112 retains its observed HUVECIC50; new construct values are withheld. Reported ties reflect source precision and are preserved. The target IDs are candidate_01, candidate_02, candidate_03, candidate_04, candidate_05, candidate_06, candidate_08, candidate_09, candidate_10, candidate_11, candidate_12, candidate_13, candidate_14, candidate_15. Return only one comma-separated line containing every target ID once, from lowest to highest HUVEC IC50.

name,format,VEGFR2_reporter_IC50_nM,VEGFR2_reporter_Emax_fold_reference,HUVEC_proliferation_IC50_nM
candidate_01,VEGF_PD1_bispecific_IgG_scFv,0.59,0.96,
candidate_02,VEGF_PD1_bispecific_IgG_scFv,0.69,0.99,
candidate_03,VEGF_PD1_bispecific_IgG_scFv,0.74,0.97,
candidate_04,VEGF_PD1_bispecific_IgG_scFv,0.63,0.99,
candidate_05,VEGF_PD1_bispecific_IgG_scFv,0.6,0.98,
candidate_06,VEGF_PD1_bispecific_IgG_scFv,0.23,0.98,
candidate_07,VEGF_PD1_bispecific_IgG_scFv,0.9,0.98,0.14
candidate_08,VEGF_PD1_bispecific_IgG_scFv,0.3,0.98,
candidate_09,VEGF_PD1_bispecific_IgG_scFv,0.16,0.97,
candidate_10,VEGF_PD1_bispecific_IgG_scFv,0.37,0.94,
candidate_11,VEGF_PD1_bispecific_IgG_scFv,0.13,1.03,
candidate_12,VEGF_PD1_bispecific_IgG_scFv,0.64,0.95,
candidate_13,VEGF_PD1_bispecific_IgG_scFv,0.18,0.96,
candidate_14,VEGF_PD1_bispecific_IgG_scFv,0.81,0.96,
candidate_15,VEGF_PD1_bispecific_IgG_scFv,0.33,0.94,
