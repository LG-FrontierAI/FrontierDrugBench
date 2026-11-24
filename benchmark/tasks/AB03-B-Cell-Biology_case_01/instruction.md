---
bench_id: AB03-B-Cell-Biology_case_01
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
M_f0f050da0ce602ba,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGITFRSYAMGWYRQAPGKQRELVSGISSSGNAHYGDSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCYAQRWVPGGVDYWGQGTLVTVSS,272.8,
M_37380872a587f5f7,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGITFRSYAMGWYRQAPGKQRELVAGISSSGNAHYGDSVKGRFTISRDNAKNSLYLQMNSLRAEDTAVYYCYAQRWVPGGVDYWGQGTLVTVSS,269.0,0.241
M_94ec6406476bbfee,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGITFRSYAMGWYRQAPGKQRELVAGISSSGNAHYGDSVKGRFTISRDNAQNSVYLQMNSLRAEDTAVYFCYAQRWVPGGVDYWGQGTLVTVSS,246.7,
M_fa011ba72aea01e1,HCAb,EVQLVESGGGLVQPGRSLRLSCAASGITFRSYAMGWYRQAPGKQRELVSGISSSGNAHYGDSVKGRFTISRDNAKNSLYLQMNSLRAEDTAVYFCYAQRWVPGGVDYWGQGTLVTVSS,292.5,0.0
M_a616046447e47a1b,HCAb,EVQLVESGGGLVQPGRSLRLSCAASGITFRSYAMGWYRQAPGKQRELVAGISSSGNAHYGDSVKGRFTISRDNAKNSVYLQMNSLRAEDTAVYYCYAQRWVPGGVDYWGQGTLVTVSS,336.4,0.0
M_ab0c7d8ad4d26c2f,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGITFRSYAMGWYRQAPGKQRELVAGISSSGNAHYGDSVKGRFTISRDNSKNTVYLQMNSLRAEDTAVYYCYAQRWVPGGVDYWGQGTLVTVSS,328.4,0.173
M_bf8ba2b3d2e8b605,HCAb,QVQLVESGGGLVQAGGSLRLSCAASGITFRSYAMGWYRRVPGKQRELVAGISSSGNAHYGDSVKGRFAISRDNVQNQVYLQMNSLKPEDTAVYFCYAQRWVPGGVDYWGQGTQVTVSS,334,0.051
M_e8c84f784dea4cff,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGITFRSYAMGWYRQAPGKQRELVSGISSSGNAHYGDSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCYAQRWVPGGVDYWGQGTLVTVSS,292.8,0.207
M_43556f14506acbdc,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGITFRSYAMGWYRQAPGKQRELVAGISSSGNAHYGDSVKGRFTISRDNSQNTVYLQMNSLRAEDTAVYFCYAQRWVPGGVDYWGQGTLVTVSS,252.8,
M_e48eccc6c71762e6,HCAb,EVQLVESGGGLVQPGRSLRLSCAASGITFRSYAMGWYRQAPGKQRELVAGISSSGNAHYGDSVKGRFTISRDNAKNSLYLQMNSLRAEDTAVYYCYAQRWVPGGVDYWGQGTLVTVSS,344.9,
M_3cbdd000ee06fe89,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGITFRSYAMGWYRQAPGKQRELVAGISSSGNAHYGDSVKGRFTISRDNVQNSVYLQMNSLRAEDTAVYFCYAQRWVPGGVDYWGQGTLVTVSS,212.3,0.196
M_22fc23e01809c0ab,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGITFRSYAMGWYRQAPGKQRELVAGISSSGNAHYGDSVKGRFTISRDNSKNTVYLQMNSLRAEDTAVYYCYAQRWVPGGVDYWGQGTLVTVSS,284.4,
M_9ebbaed28aebf057,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGITFRSYAMGWYRQAPGKQRELVSGISSSGNAHYGDSVKGRFTISRDNSKNTVYLQMNSLRAEDTAVYYCYAQRWVPGGVDYWGQGTLVTVSS,257.9,0.173
