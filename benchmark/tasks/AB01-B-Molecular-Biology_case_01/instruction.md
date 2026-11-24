---
bench_id: AB01-B-Molecular-Biology_case_01
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
M_ca97d1695a1c715a,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGTTSSINAMSWYRQAPGGQRELVSAISDGGTHYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADDLRGWPEYWGQGTLVTVSS,0.4,
parent,one_armed_VHH_Fc,QVQLQASGGGLVQSGGSLRLSCAASGTTSSINAMSWYRQAPGGQRLLVAAISDGGTHYADSVKGRFTISRNNAKNTVYLQMNSLKPEDTAVYYCNADDLRGWPEYWGKGTQVTVSS,2.54,0.4
M_a38e89ab750aeb12,one_armed_VHH_Fc,QVQLLESGGGLVQPGGSLRLSCAASGTTSSINAMSWYRQAPGGQRLLVAAISDGGTHYADSVKGRFTISRDNSKNTVYLQMNSLRAEDTAVYYCNADDLRGWPEYWGQGTLVTVSS,1,
M_bb5d3ae00580bc83,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGTTSSINAMSWYRQAPGKQRLLVSAISDGGTHYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADDLRGWPEYWGQGTLVTVSS,0.66,
M_2a09ac305e2893e6,one_armed_VHH_Fc,QVQLLESGGGLVQPGGSLRLSCAASGTTSSINAMSWYRQAPGKQRELVSAISDGGTHYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADDLRGWPEYWGQGTLVTVSS,0.41,
M_c2ed39eb172f6363,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGTTSSINAMSWYRQAPGGQRLLVAAISDGGTHYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADDLRGWPEYWGQGTLVTVSS,0.72,
M_66ce7c0bea6b6c63,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGTTSSINAMSWYRQAPGKQRELVSAISDGGTHYADSVKGRFTISRDNSKNTVYLQMNSLRAEDTAVYYCNADDLRGWPEYWGQGTLVTVSS,0.35,
M_dc2199fdcbb19a57,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGTTSSINAMSWYRQAPGKQRELVAAISDGGTHYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADDLRGWPEYWGQGTLVTVSS,0.36,
M_70c316405f5d9d39,one_armed_VHH_Fc,EVQLLESGGGLVQPGGSLRLSCAASGTTSSINAMSWYRQAPGKQRELVSAISDGGTHYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCNADDLRGWPEYWGQGTLVTVSS,0.3,
