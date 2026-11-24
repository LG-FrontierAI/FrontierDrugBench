---
bench_id: AB56-Cell-Biology_case_01
category: "Cell-Biology"
title: "Separating antigen density from target-cell context"
format: open_rubric
task_type: "review"
input_mode: "single_case_csv"
pass_threshold: 0.8
---

# Prompt
The following study information applies to this case:

Example10 uses primary skin-derived Vδ1 γδT cells from two donors at1:1 E:T with A431 PD-L1-high, A549 PD-L1-low and A549 PD-L1-knockout cells. Table34 reports CD107a degranulationEC50 in pM. Source methods contain inconsistent244h versus24h wording; this benchmark preserves that discrepancy as unresolved. >1000pM is a right-censored result, not a measured finiteEC50.

Use only the supplied CSV and study information. Do not browse, execute code or use tools. Answer in English. Review these claims: (1) PD-L1-high cells must show lower degranulationEC50 than PD-L1-low cells; (2) activity on PD-L1-low A549 proves target-independent activation; (3) the knockout comparison supports a role for PD-L1; (4) “>1000pM” means an EC50 of exactly1000pM. Assess each claim, preserve donor-specific evidence and censoring, then propose two checks that distinguish density dependence from cell-line context. Flag the inconsistent incubation-time wording rather than silently choosing a corrected value.

name,donor,target_cell,PDL1_context,ADT5_1_CD107a_EC50_pM,CD3_PDL1_control_EC50_pM,anti_RSV_EC50_pM
ATS036_A431,ATS036,A431,high,20,7.6,>1000
ATS036_A549,ATS036,A549,low,11.7,7.2,>1000
ATS036_A549_KO,ATS036,A549_KO,knockout,>1000,>1000,>1000
ATS037_A431,ATS037,A431,high,18.4,7.5,>1000
ATS037_A549,ATS037,A549,low,7.1,4.1,>1000
ATS037_A549_KO,ATS037,A549_KO,knockout,>1000,>1000,>1000
