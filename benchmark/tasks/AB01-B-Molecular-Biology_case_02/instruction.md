---
bench_id: AB01-B-Molecular-Biology_case_02
category: "Molecular-Biology"
title: "Predicting cross-species affinity retention after humanization"
format: ranking
input_mode: single_case_csv
pass_threshold: 0.6
---

# Prompt

The CSV contains anti-IL-2Rbeta VHHs in the same one-armed VHH-Fc format. Human KD measurements and the parental human/cynomolgus reference measurements are supplied. Rank every molecule with blank `cyno_KD_nM` from lowest to highest predicted cynomolgus-to-human KD ratio. Exclude the measured parent. Use the ratio, rather than raw cynomolgus KD, as the ranking endpoint.

The following study information applies to this case:

Each molecule is an anti-IL-2Rbeta VHH in the same one-armed VHH-Fc format. The VHH-Fc molecules were captured on an anti-PGLALA CM3 surface. Recombinant human or cynomolgus IL-2Rbeta-gamma extracellular-domain constructs were injected as analytes in a Biacore T200 assay at 25 C, using PBS-P+ buffer, a top receptor concentration of 150 nM and threefold serial dilutions. Association and dissociation were monitored for 240 s and 600 s, respectively; KD values were reported from a 1:1 Langmuir fit and are in nM. Predict ratios of the reported matched SPR KD values. The source does not provide replicate-level uncertainty for these table entries.

Use only the supplied CSV and study information. Do not browse, execute code, or call external tools. Return one comma-separated line containing every target exactly once, without explanations. Each case and each task runs in an independent context; no sibling-task results or previous answers are supplied.

name,format,sequence1,human_KD_nM,cyno_KD_nM
M_82d8f894ad4b3c89,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKQRELVSAIDRGGGTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,0.57,
M_191daa4df8a04c06,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKQRGLVSAIDRGGGTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,0.38,
M_7f09371131964f78,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKQRELVAAIDRGGGTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,0.7,
M_cbc5f893c6210ebd,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKGLELVSAIDRGGGTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,0.26,
M_a614f8e92019bec6,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKQRGLVAAIDRGGGTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,0.39,
parent,one_armed_VHH_Fc,QVQLQESGGGLVQAGGSLRLSCAASGSTFSINGMGWYRQAPGKQRGLVAAIDRGGGTYYADSVKGRFTISRDNAKNTVYLQMNSLKPEDTAIYYCNADSWDGDDYWGQGTLVTVSS,0.29,5
M_80c85ab4dc74e054,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKQRELVSAIDRGGGTYYADSVKGRFTISRDNSKNTVYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,0.27,
M_64dd8c75973a81a0,one_armed_VHH_Fc,QVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKQRELVSAIDRGGGTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,0.59,
M_1b0f19b51c7506ad,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKGRELVSAIDRGGGTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,0.5,
M_f741fc76e6431936,one_armed_VHH_Fc,QVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKQRGLVAAIDRGGGTYYADSVKGRFTISRDNSKNTVYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,0.25,
