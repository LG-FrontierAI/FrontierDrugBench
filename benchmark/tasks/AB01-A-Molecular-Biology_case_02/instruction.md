---
bench_id: AB01-A-Molecular-Biology_case_02
category: "Molecular-Biology"
title: "Predicting human IL-2Rbeta affinity from humanized VHH sequences"
format: ranking
input_mode: single_case_csv
pass_threshold: 0.6
---

# Prompt

The CSV contains anti-IL-2Rbeta VHHs in the same one-armed VHH-Fc format. Predict human receptor binding from the supplied complete variable-domain sequences. All `human_KD_nM` values are withheld. The row named `parent` is a sequence reference; exclude it from your answer. Rank every other molecule from lowest to highest predicted human KD in nM (strongest to weakest affinity).

The following study information applies to this case:

Each molecule is an anti-IL-2Rbeta VHH in the same one-armed VHH-Fc format. The VHH-Fc molecules were captured on an anti-PGLALA CM3 surface. Recombinant human or cynomolgus IL-2Rbeta-gamma extracellular-domain constructs were injected as analytes in a Biacore T200 assay at 25 C, using PBS-P+ buffer, a top receptor concentration of 150 nM and threefold serial dilutions. Association and dissociation were monitored for 240 s and 600 s, respectively; KD values were reported from a 1:1 Langmuir fit and are in nM. Predict the reported human SPR KD values of the target variants. All human affinity measurements, including the parent reference, are withheld. The parent is a sequence reference only and is not a ranking target. The source does not provide replicate-level uncertainty for these table entries.

Use only the supplied CSV and study information. Do not browse, execute code, or call external tools. Return one comma-separated line containing every target exactly once, without explanations. Each case and each task runs in an independent context; no sibling-task results or previous answers are supplied.

name,format,sequence1,human_KD_nM
M_191daa4df8a04c06,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKQRGLVSAIDRGGGTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,
M_f741fc76e6431936,one_armed_VHH_Fc,QVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKQRGLVAAIDRGGGTYYADSVKGRFTISRDNSKNTVYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,
M_1b0f19b51c7506ad,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKGRELVSAIDRGGGTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,
M_80c85ab4dc74e054,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKQRELVSAIDRGGGTYYADSVKGRFTISRDNSKNTVYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,
M_cbc5f893c6210ebd,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKGLELVSAIDRGGGTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,
M_64dd8c75973a81a0,one_armed_VHH_Fc,QVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKQRELVSAIDRGGGTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,
parent,one_armed_VHH_Fc,QVQLQESGGGLVQAGGSLRLSCAASGSTFSINGMGWYRQAPGKQRGLVAAIDRGGGTYYADSVKGRFTISRDNAKNTVYLQMNSLKPEDTAIYYCNADSWDGDDYWGQGTLVTVSS,
M_a614f8e92019bec6,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKQRGLVAAIDRGGGTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,
M_7f09371131964f78,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKQRELVAAIDRGGGTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,
M_82d8f894ad4b3c89,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGSTFSINGMGWYRQAPGKQRELVSAIDRGGGTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADSWDGDDYWGQGTLVTVSS,
