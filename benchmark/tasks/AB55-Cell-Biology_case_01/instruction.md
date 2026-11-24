---
bench_id: AB55-Cell-Biology_case_01
category: "Cell-Biology"
title: "Testing the limits of an affinity-to-function conclusion"
format: open_rubric
task_type: "review"
input_mode: "single_case_csv"
pass_threshold: 0.8
---

# Prompt
The following study information applies to this case:

Table6 reports four dual-binding ADT1-4-x/ADT5-1n constructs; the n suffix is retained and is not silently equated with the nonsuffixed TAK-505/ADT1-4-2/ADT5-1 used in the PBMC experiment. Example11 compares4h CD107a degranulation by skin-derived Vδ1 γδT cells with tumor targets at1:1 E:T,37C. Example12 measures24h live-GFP A375 target-cell lysis at1:1 E:T with a top antibody concentration of100nM. The source states similar degranulation across <1–60nM Vδ1 affinities and no significant lysis differences in the tested panel; individual figure-derived potency values are not supplied.

Use only the supplied CSV and study information. Do not browse, execute code or use tools. Answer in English. A project summary claims: (1) the60nM Vδ1-binding construct must have the weakest degranulation; (2) the report proves affinity never matters for Vδ1 engager function; (3) “no significant difference” proves biological equivalence; (4) CD107a and tumor-cell lysis are the same endpoint. Assess each claim as supported, contradicted or not established. Cite the supplied assay evidence, write a corrected conclusion, and propose two discriminating checks.

name,source_record,Vdelta1_KD_nM,PDL1_KD_nM,degranulation_comparison,TDCC_comparison
ADT1-4-2/ADT5-1n,Table6 reported affinity row 1,0.75,2.7,Example11: similar degranulation across <1 to60nM Vdelta1 affinity range,Example12: no significant difference in A375 live-GFP lysis under tested conditions
ADT1-4-1/ADT5-1n,Table6 reported affinity row 2,0.97,2,Example11: similar degranulation across <1 to60nM Vdelta1 affinity range,Example12: no significant difference in A375 live-GFP lysis under tested conditions
ADT1-4-6/ADT5-1n,Table6 reported affinity row 3,7.4,2.7,Example11: similar degranulation across <1 to60nM Vdelta1 affinity range,Example12: no significant difference in A375 live-GFP lysis under tested conditions
ADT1-4-138/ADT5-1n,Table6 reported affinity row 4,60,1.8,Example11: similar degranulation across <1 to60nM Vdelta1 affinity range,Example12: no significant difference in A375 live-GFP lysis under tested conditions
