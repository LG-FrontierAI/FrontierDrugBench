---
bench_id: AB58-Cell-Biology_case_01
category: "Cell-Biology"
title: "Attributing cytotoxicity in mixed and primed effector populations"
format: open_rubric
task_type: "review"
input_mode: "single_case_csv"
pass_threshold: 0.8
---

# Prompt
The following study information applies to this case:

Examples11/12 use skin-derived Vδ1 γδT cells at1:1 E:T for degranulation/lysis. Example13 first primes PBMCs for seven days, then uses40:1 totalPBMC:tumor. The reported PBMC composition is approximately83% αβT cells and8.6% Vδ1 cells. Source observations are not normalized to matched Vδ1-cell numbers, priming histories or accessory-cell composition.

Use only the supplied CSV and study information. Do not browse, execute code or use tools. Answer in English. A project compares the primed PBMC and skin-derived Vδ1 experiments and concludes: (1) the PBMC preparation is intrinsically more potent perVδ1 cell; (2) all PBMC-mediated tumor lysis is attributable toVδ1 cells; (3) seven-day priming and a40:1 E:T ratio are interchangeable with the skin-cell1:1 assay. Evaluate these conclusions. Explain the denominator and composition problems and propose two discriminating experiments. Do not invent a normalized potency or a lysis percentage.

name,cell_source,culture,effector_target_ratio,alpha_beta_fraction_percent,Vdelta1_fraction_percent,readout,interpretation
skin_Vdelta1,skin-derived Vdelta1 cells,skin-derived,1:1,,,CD107a4h or A375liveGFP24h,enriched effector preparation
PBMC_primed,PBMC after7dayTAK505 priming,7dayTAK505,40:1,83,8.6,tumorlysis after priming,mixed effector preparation
