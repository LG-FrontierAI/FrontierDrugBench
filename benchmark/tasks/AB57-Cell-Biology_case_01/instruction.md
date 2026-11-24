---
bench_id: AB57-Cell-Biology_case_01
category: "Cell-Biology"
title: "Auditing donor heterogeneity, units and replication"
format: open_rubric
task_type: "review"
input_mode: "single_case_csv"
pass_threshold: 0.8
---

# Prompt
The following study information applies to this case:

Example19 treats PBMCs from five donors with TAK-505 for seven days. The stated concentration series is1000,100,10,1,.1,.01pM, with triplicate wells on three plates. Table35 labels EC50 valuespM. The prose repeats summary numbers withuM, a source-unit inconsistency. Reported means Vδ1/Ki67/NKG2D/CD27 are1.73/.19/.38/14.25;SDs.80/.09/.22/30.61. The five donor identities are the biological units; technical wells and plates are not additional donors.

Use only the supplied CSV and study information. Do not browse, execute code or use tools. Answer in English. A proposed analysis states: (1) all four markers show homogeneous potency across donors; (2) theTable35 CD27 mean14.25pM is a typical donor response; (3) the text/Table unit conflict can be silently resolved by usinguM; (4) triplicate wells on three plates establish15 independent biological donors. Review and correct these claims using the supplied records. Specify which quantitative summaries can be preserved, which need qualification, and two immediate checks.

name,donor,Vdelta1_EC50_pM,Ki67_EC50_pM,NKG2D_EC50_pM,CD27_EC50_pM,table_unit,prose_unit_for_same_summary
ALK051,ALK051,0.55,0.13,0.22,0.2,pM,uM
ALK052,ALK052,2,0.19,0.27,0.1,pM,uM
ALK055,ALK055,2.39,0.33,0.57,1.84,pM,uM
ALK056,ALK056,2.43,0.2,0.67,68.99,pM,uM
ALK057,ALK057,1.3,0.1,0.17,0.12,pM,uM
