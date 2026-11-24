---
bench_id: AB47-Cell-Biology_case_01
category: "Cell-Biology"
title: "Quantitative prediction of membrane-ligand neutralization"
format: regression
task_type: "numeric"
input_mode: "single_case_csv"
pass_threshold: 0.6
---

# Prompt
Use only the supplied CSV and study information. Do not browse, execute code, use tools or provide explanations. Predict the reported half-maximal concentration (nM; Table18 labels thisEC50) inhibiting membrane-bound humanTL1A-driven NF-kB-luciferase in TF1 cells cocultured with CHO-K1-TL1A for6h. It is a functional inhibition endpoint, notSPR KD. Antibody dilution covers100nM maximum with5-fold dilutions. Table11 monomer/trimerSPR and Table13 cell-binding values are visible; no-binding monomer control remains blank, notzero. Both analogue references retain their measured Table18 values. Two new antibodies are targets. Target candidates are candidate_01, candidate_03. Return only one JSON object mapping each target candidate ID to its positive numerical reported EC50 in nM.

name,format,human_monomer_SPR_KD_nM,human_trimer_SPR_KD_nM,TL1A_cell_binding_EC50_nM,TL1A_cell_binding_top_MFI,membrane_TL1A_NFkB_EC50_nM
candidate_01,IgG,14.7,0.657,1.81,55419,
candidate_02,IgG,,0.221,1.02,49017,0.393
candidate_03,IgG,0.602,0.199,0.41,56310,
candidate_04,IgG,0.0547,0.216,24.95,40329,2.45
