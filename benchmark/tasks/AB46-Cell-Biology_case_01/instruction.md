---
bench_id: AB46-Cell-Biology_case_01
category: "Cell-Biology"
title: "Predicting downstream apoptosis rescue after antibody humanization"
format: ranking
task_type: "ranking"
input_mode: "single_case_csv"
pass_threshold: 0.65
---

# Prompt
Use only the supplied CSV and study information. Do not browse, execute code, use tools or provide explanations. Predict inhibition of TL1A-induced caspase3/7 activity in TF-1 cells (endogenousDR3) after6h with cycloheximide sensitization. The source uses Caspase-Glo3/7, not a direct proliferation endpoint. Table15 receptor-cell blockadeIC50 and fitted Bottom are visible. Table20 downstream caspaseIC50 values for eight humanized descendants are withheld; the parental antibody is a visible control. Do not treat receptor blockade potency or fitted Bottom as the target itself. Target candidates are candidate_01, candidate_02, candidate_03, candidate_04, candidate_05, candidate_06, candidate_07, candidate_08. Return only one comma-separated line containing every target candidate ID exactly once, from lowest IC50 (most potent) to highest IC50.

name,format,DR3_cell_blocking_IC50_nM,DR3_cell_blocking_bottom_MFI,TF1_caspase_inhibition_IC50_nM
candidate_01,IgG,10.76,519,
candidate_02,IgG,11.01,642,
candidate_03,IgG,11.92,916,
candidate_04,IgG,10.33,363,
candidate_05,IgG,11.89,1059,
candidate_06,IgG,11.29,605,
candidate_07,IgG,11.83,300,
candidate_08,IgG,12.03,327,
candidate_09,IgG,10.52,263,1.16
