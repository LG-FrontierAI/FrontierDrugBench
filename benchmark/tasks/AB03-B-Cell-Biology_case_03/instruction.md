---
bench_id: AB03-B-Cell-Biology_case_03
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
M_00e8fe81f36e2af0,HCAb,QVQLVESGGGLVKPGGSLRLSCAASGSISSTTVMGWYRQAPGKQRDFVAGITRSGRINYGDFVKGRFTISRDNAKNSVYLQMNSLRPEDTAVYYCAAWNYGSSAPSSWGQGTLVTVSS,1268.7,
M_aed1d3cd799af790,HCAb,QVQLVESGGGLVKPGGSLRLSCAASGSISSTTVMGWYRQAPGKQREFVAGITRSGRINYGDFVKGRFTISRDNAKNSVYLQMNSLRAEDTAVYYCAAWNYGSSAPSSWGQGTLVTVSS,1287.2,1.459
M_4778dc8f58207381,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGSISSTTVMGWYRQAPGKQREFVAGITRSGRINYGDFVKGRFTISRDNAKNSVYLQMNSLRAEDTAVYYCAAWNYGSSAPSSWGQGTLVTVSS,1419.0,
M_b0fd3a286e9a2fc7,HCAb,QVQLVESGGGLVKPGGSLRLSCAASGSISSTTVMGWYRQAPGKQREFVSGITRSGRINYGDFVKGRFTISRDNAKNSVYLQMNSLRAEDTAVYYCAAWNYGSSAPSSWGQGTLVTVSS,1451.8,1.188
M_6a9cd95495e98abb,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGSISSTTVMGWYRQAPGKQREFVSGITRSGRINYGDFVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCAAWNYGSSAPSSWGQGTLVTVSS,1065.0,0.59
M_a5fa9c3af14ce6b2,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGSISSTTVMGWYRQAPGKQREFVSGITRSGRINYGDFVKGRFTISRDNSKNTVYLQMNSLRAEDTAVYYCAAWNYGSSAPSSWGQGTLVTVSS,1465.7,1.402
M_fecb77b79ee3000e,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGSISSTTVMGWYRQAPGKQRDFVAGITRSGRINYGDFVKGRFTISRDNAKNTVYLQMNSLRAEDTAVYYCAAWNYGSSAPSSWGQGTLVTVSS,1394.1,3.376
M_e9f36099dcd0196f,HCAb,QVHLVESGGGLVQAGGSLRLSCAASGSISSTTVMGWYRQAPGKQRDFVAGITRSGRINYGDFVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCAAWNYGSSAPSSWGQGTQVTVSS,1295,1.77
M_4e1a0bc8dda4e5b2,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGSISSTTVMGWYRQAPGKQREFVSGITRSGRINYGDFVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCAAWNYGSSAPSSWGQGTLVTVSS,1143.7,
M_369c3dfb6efc3558,HCAb,EVQLVESGGGLVQPGRSLRLSCAASGSISSTTVMGWYRQAPGKQRDFVAGITRSGRINYGDFVKGRFTISRDNAKNSLYLQMNSLKAEDTAVYYCAAWNYGSSAPSSWGQGTLVTVSS,911.1,
M_82a8ab5c02a8dc69,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGSISSTTVMGWYRQAPGKQREFVAGITRSGRINYGDFVKGRFTISRDNAKNSLYLQMNSLRAEDTAVYYCAAWNYGSSAPSSWGQGTLVTVSS,1059.9,
M_ebf51084bf5844fd,HCAb,QVQLVESGGGLVKPGGSLRLSCAASGSISSTTVMGWYRQAPGKQREFVSGITRSGRINYGDFVKGRFTISRDNAKNSLYLQMNSLRAEDTAVYYCAAWNYGSSAPSSWGQGTLVTVSS,1106.7,0.613
M_3b039b3502568d74,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGSISSTTVMGWYRQAPGKQREFVSGITRSGRINYGDFVKGRFTISRDNSKNTVYLQMNSLRAEDTAVYYCAAWNYGSSAPSSWGQGTLVTVSS,1492.3,1.628
