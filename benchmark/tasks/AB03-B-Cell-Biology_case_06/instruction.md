---
bench_id: AB03-B-Cell-Biology_case_06
category: "Cell-Biology"
title: "Predicting immobilized-HCAb IL-2 response from sequence and binding"
format: ranking
input_mode: single_case_csv
pass_threshold: 0.6
---

# Prompt

The CSV contains yeast-produced anti-CD3 HCAbs from one lineage, complete variable-domain sequences and Jurkat CD3-positive binding MFI. Rows with populated `IL2_response` are measured functional references. Rank every row with blank `IL2_response` from highest to lowest predicted IL-2 secretion in pg/mL under the source-described plate-immobilized HCAb Jurkat assay. Exclude measured references. The exact antibody coating concentration is unreported. Binding and secretion are different assays; this endpoint is not soluble-antibody autonomous activation or clinical cytokine-release risk.

The following study information applies to this case:

The source study describes humanized anti-CD3 HCAbs tested in plate-immobilized-antibody Jurkat activation and flow-cytometry binding assays. The variable-domain sequence is supplied for each candidate. Binding is reported as Jurkat CD3-positive fluorescence intensity (MFI); no CD3-negative measurement is supplied. The activation endpoint is IL-2 concentration in pg/mL. The humanized HCAbs were yeast-produced. The exact antibody coating concentration is not reported in the source. Predict the withheld IL-2 response under this source-described assay; this endpoint does not represent soluble-antibody autonomous activation or a clinical cytokine-release estimate.

Use only the supplied CSV and study information. Do not browse, execute code, or call external tools. Return one comma-separated line containing every target exactly once, without explanations. Each case and each task runs in an independent context; no sibling-task results or previous answers are supplied.

name,format,sequence1,Jurkat_CD3_positive_MFI,IL2_response
M_5c072cde7729513b,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVAAISSRGRDTYYADSVKGRFTISRDNAKNSVYLQMNSLRPEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,1039.8,1.146
M_5b31ec7a47f112a2,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVSAISSRGRDTYYADSVKGRFTISRDNSKNTVYLQMNSLRAEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,1212.7,
M_828dcef4e97fec6a,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVSAISSRGRDTYYADSVKGRFTISRDNAKNTLYLQMNSLRAEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,1070.1,
M_957ad08c06607453,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVAAISSRGRDTYYADSVKGRFTISRDNAKNSLYLQMNSLRAEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,1074.9,1.44
M_58b812f78ab6632b,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVSAISSRGRDTYYADSVKGRFTISRDNSKNTLYLQMNSLKAEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,1158.2,
M_3e185afa93552724,HCAb,EVQLVESKGGLVQFGGSLNLSCAASGRTFSSLPMGWFRQAPGKEREFVAAISSRGRDTYYADSVKGRFIISRDNAKNTVYLQMSSLKPEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTQVTVSS,1059,0.0
M_f28081c3691e2610,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVSAISSRGRDTYYADSVKGRFTISRDNAKNSLYLQMNSLRAEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,1067,1.582
M_739f93106f81cde6,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVAAISSRGRDTYYADSVKGRFTISRDNSKNTVYLQMNSLRAEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,1147.5,0.726
M_98ce2a84a5f23115,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVSAISSRGRDTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,1164.0,0.863
M_68c2774148772743,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGRTFSSLPMGWFRQAPGKEREFVAAISSRGRDTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCAVRAWGSISTTSLTPYGNWGQGTLVTVSS,1101.6,
