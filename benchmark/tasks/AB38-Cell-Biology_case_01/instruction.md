---
bench_id: AB38-Cell-Biology_case_01
category: "Cell-Biology"
title: "Predicting IL17F neutralization from paired cytokine binding and IL17A function"
format: ranking
task_type: "ranking"
input_mode: "single_case_csv"
pass_threshold: 0.6
---

# Prompt
The following study information applies to this case:

Ten measured affinity-matured/framework-modified antibody clones from a single anti-IL17A/F campaign. Columns describe the same named source clones across source Tables4,5,7,9. This is a transfer-from-measured-assays task, not inference from unprovided sequences. SPR: captured antibody, soluble human cytokine, 25C, source neutral pH7.4 normalized to benchmark pH7.5. NFkB: HEK293 IL17RA+/IL17RC+ luciferase reporter, cytokine/antibody preassociation1h, cells16h. NHDF: normal human dermal fibroblasts, 0.5ng/mL TNF, cytokine/antibody preassociation1h, cells16h, supernatantIL6 ELISA. Reported ties are retained; source precision and finite sample uncertainty limit interpretation of near ties. No target relative IC50 or direct derived target is supplied.

Use only the supplied CSV and study information. Do not browse, execute code or use tools. Predict the withheld experimental endpoint. Return only one comma-separated line containing every candidate ID exactly once, ordered from lowest IC50 (most potent) to highest IC50. Do not explain. Predict inhibition of NFkB-linked luciferase in HEK293 IL17RA+/IL17RC+ cells stimulated with1ug/mL humanIL17F. The target is absolute antibody IC50 (nM) after16h. IL17A reporter potency is visible, but IL17F reporter values are withheld.

name,format,human_IL17A_kon_M_1_s_1,human_IL17A_koff_s_1,human_IL17A_KD_M,human_IL17F_kon_M_1_s_1,human_IL17F_koff_s_1,human_IL17F_KD_M,NFkB_IL17A_IC50_nM,NFkB_IL17F_IC50_nM
candidate_01,IgG,1250000.0,3.67e-05,2.93e-11,263000.0,5.02e-05,1.91e-10,0.055,
candidate_02,IgG,759000.0,1.69e-05,2.22e-11,186000.0,0.000118,6.33e-10,0.058,
candidate_03,IgG,1680000.0,8.25e-06,4.91e-12,289000.0,6.05e-05,2.09e-10,0.061,
candidate_04,IgG,1780000.0,2.55e-06,1.44e-12,402000.0,0.000172,4.28e-10,0.049,
candidate_05,IgG,1750000.0,6.33e-06,3.61e-12,389000.0,5.97e-06,1.53e-11,0.056,
candidate_06,IgG,1680000.0,6.71e-06,4e-12,279000.0,0.000277,9.94e-10,0.047,
candidate_07,IgG,1500000.0,4.01e-05,2.68e-11,186000.0,0.00013,7e-10,0.06,
candidate_08,IgG,1190000.0,3.05e-06,2.56e-12,312000.0,4.55e-05,1.46e-10,0.055,
candidate_09,IgG,1670000.0,7.06e-06,4.23e-12,392000.0,2.09e-05,5.32e-11,0.055,
candidate_10,IgG,1320000.0,2.14e-05,1.62e-11,304000.0,0.000404,1.33e-09,0.069,
