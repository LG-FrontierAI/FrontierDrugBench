---
bench_id: AB03-B-Cell-Biology_case_05
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
M_b8154de690cb4257,HCAb,EVQLVESGGGLVQAGGSLRLSCEASGRTLMTFAMGWFRQAPGKEREFVAGLRWGVGLQRIAESVKGRFTITRDNAKKVVYLQMSSLKPEDTAAYYCAADTDHSPSLIYTAVNAYEVWGQGTQVTVSS,243,0.451
M_36d2d735093e9037,HCAb,EVQLVESGGGLVQPGRSLRLSCAASGRTLMTFAMGWFRQAPGKEREFVAGLRWGVGLQRIAESVKGRFTISRDNAKKSVYLQMNSLRPEDTAVYYCAADTDHSPSLIYTAVNAYEVWGQGTLVTVSS,77.4,
M_87663e0363fae9ff,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGRTLMTFAMGWFRQAPGKEREFVAGLRWGVGLQRIAESVKGRFTISRDNAKKSVYLQMNSLRPEDTAVYYCAADTDHSPSLIYTAVNAYEVWGQGTLVTVSS,149.6,0.0
M_d8b76708b59bcc39,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGRTLMTFAMGWFRQAPGKEREFVAGLRWGVGLQRIAESVKGRFTISRDNAKKSVYLQMNSLKPEDTAVYYCAADTDHSPSLIYTAVNAYEVWGQGTLVTVSS,169.4,0.192
M_090b64c84134d7bc,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGRTLMTFAMGWFRQAPGKEREFVAGLRWGVGLQRIAESVKGRFTISRDNAKKSVYLQMNSLRAEDTAVYYCAADTDHSPSLIYTAVNAYEVWGQGTLVTVSS,145.0,0.0
M_6d6265947e50a34c,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGRTLMTFAMGWFRQAPGKEREFVAGLRWGVGLQRIAESVKGRFTISRDNAKKTVYLQMNSLRAEDTAVYYCAADTDHSPSLIYTAVNAYEVWGQGTLVTVSS,126.2,
