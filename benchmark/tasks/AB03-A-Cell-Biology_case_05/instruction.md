---
bench_id: AB03-A-Cell-Biology_case_05
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
M_6d6265947e50a34c,HCAb,EVQLLESGGGLVQPGGSLRLSCAASGRTLMTFAMGWFRQAPGKEREFVAGLRWGVGLQRIAESVKGRFTISRDNAKKTVYLQMNSLRAEDTAVYYCAADTDHSPSLIYTAVNAYEVWGQGTLVTVSS,
M_090b64c84134d7bc,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGRTLMTFAMGWFRQAPGKEREFVAGLRWGVGLQRIAESVKGRFTISRDNAKKSVYLQMNSLRAEDTAVYYCAADTDHSPSLIYTAVNAYEVWGQGTLVTVSS,145.0
M_d8b76708b59bcc39,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGRTLMTFAMGWFRQAPGKEREFVAGLRWGVGLQRIAESVKGRFTISRDNAKKSVYLQMNSLKPEDTAVYYCAADTDHSPSLIYTAVNAYEVWGQGTLVTVSS,169.4
M_36d2d735093e9037,HCAb,EVQLVESGGGLVQPGRSLRLSCAASGRTLMTFAMGWFRQAPGKEREFVAGLRWGVGLQRIAESVKGRFTISRDNAKKSVYLQMNSLRPEDTAVYYCAADTDHSPSLIYTAVNAYEVWGQGTLVTVSS,
M_b8154de690cb4257,HCAb,EVQLVESGGGLVQAGGSLRLSCEASGRTLMTFAMGWFRQAPGKEREFVAGLRWGVGLQRIAESVKGRFTITRDNAKKVVYLQMSSLKPEDTAAYYCAADTDHSPSLIYTAVNAYEVWGQGTQVTVSS,243
M_87663e0363fae9ff,HCAb,EVQLVESGGGLVQPGGSLRLSCAASGRTLMTFAMGWFRQAPGKEREFVAGLRWGVGLQRIAESVKGRFTISRDNAKKSVYLQMNSLRPEDTAVYYCAADTDHSPSLIYTAVNAYEVWGQGTLVTVSS,149.6
