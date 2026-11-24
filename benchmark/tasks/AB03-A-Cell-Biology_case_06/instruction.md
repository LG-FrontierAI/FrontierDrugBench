---
bench_id: AB03-A-Cell-Biology_case_06
category: "Cell-Biology"
title: "Predicting Jurkat CD3-positive cell binding from HCAb sequence"
format: ranking
input_mode: single_case_csv
pass_threshold: 0.6
---

# Prompt

The CSV contains yeast-produced anti-CD3 HCAbs from one lineage and their complete variable-domain sequences. Rows with populated `Jurkat_CD3_positive_MFI` are measured binding references. Rank every row with blank `Jurkat_CD3_positive_MFI` from highest to lowest predicted Jurkat CD3-positive cell-binding MFI. Exclude measured references. MFI is an assay fluorescence readout, not KD or a CD3-positive/CD3-negative ratio. No activation outcomes are supplied.

The following study information applies to this case:

Humanized anti-CD3 HCAbs from one lineage were produced in yeast. The endpoint is the Table 17 flow-cytometry Jurkat CD3-positive fluorescence intensity (MFI). This readout is not an equilibrium KD or a normalized CD3-positive/CD3-negative ratio. No CD3-negative measurement is supplied. Measured-reference MFI values are provided; target MFI and all activation outcomes are withheld. Predict binding under the source-described matched assay, without assuming unreported assay conditions.

Use only the supplied CSV and study information. Do not browse, execute code, or call external tools. Return one comma-separated line containing every target exactly once, without explanations. Each case and each task runs in an independent context; no sibling-task results or previous answers are supplied.

name,format,sequence1,Jurkat_CD3_positive_MFI
M_739f93106f81cde6,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVAAISSRGRDTYYADSVKGRFTISRDNSKNTVYLQMNSLRAEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,1147.5
M_f28081c3691e2610,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVSAISSRGRDTYYADSVKGRFTISRDNAKNSLYLQMNSLRAEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,1067
M_3e185afa93552724,HCAb,EVQLVESKGGLVQFGGSLNLSCAASGRTFSSLPMGWFRQAPGKEREFVAAISSRGRDTYYADSVKGRFIISRDNAKNTVYLQMSSLKPEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTQVTVSS,1059
M_58b812f78ab6632b,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVSAISSRGRDTYYADSVKGRFTISRDNSKNTLYLQMNSLKAEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,
M_5b31ec7a47f112a2,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVSAISSRGRDTYYADSVKGRFTISRDNSKNTVYLQMNSLRAEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,
M_5c072cde7729513b,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVAAISSRGRDTYYADSVKGRFTISRDNAKNSVYLQMNSLRPEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,1039.8
M_957ad08c06607453,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVAAISSRGRDTYYADSVKGRFTISRDNAKNSLYLQMNSLRAEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,1074.9
M_98ce2a84a5f23115,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVSAISSRGRDTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,1164.0
M_68c2774148772743,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVAAISSRGRDTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,
M_828dcef4e97fec6a,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVSAISSRGRDTYYADSVKGRFTISRDNAKNTLYLQMNSLRAEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,
