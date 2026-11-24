---
bench_id: AB45-Cell-Biology_case_01
category: "Cell-Biology"
title: "Predicting receptor-cell ligand blockade from cross-species ligand binding"
format: ranking
task_type: "ranking"
input_mode: "single_case_csv"
pass_threshold: 0.65
---

# Prompt
Use only the supplied CSV and study information. Do not browse, execute code, use tools or provide explanations. Predict inhibition of biotinylated human TL1A binding to Expi293 cells displaying human DR3, measured by FACS after30min at4C at ligandEC80. Visible ELISA EC50 values measure binding to coated soluble human/cynomolgus TL1A proteins; they are not intrinsicKD. The two analogue reference antibodies retain observed blockingIC50. Table12 is the source of ELISA columns; Table14 is the withheld receptor-cell endpoint. Target candidates are candidate_01, candidate_02, candidate_05, candidate_06, candidate_07, candidate_08, candidate_09, candidate_10. Return only one comma-separated line containing every target candidate ID exactly once, from lowest IC50 (most potent) to highest IC50.

name,format,human_TL1A_ELISA_EC50_nM,cyno_TL1A_ELISA_EC50_nM,DR3_cell_blocking_IC50_nM
candidate_01,IgG,0.05,0.06,
candidate_02,IgG,0.04,0.05,
candidate_03,IgG,0.06,0.065,85.05
candidate_04,IgG,0.04,0.05,16.68
candidate_05,IgG,0.04,0.05,
candidate_06,IgG,0.04,0.05,
candidate_07,IgG,0.03,0.05,
candidate_08,IgG,0.04,0.05,
candidate_09,IgG,0.04,0.05,
candidate_10,IgG,0.03,0.04,
