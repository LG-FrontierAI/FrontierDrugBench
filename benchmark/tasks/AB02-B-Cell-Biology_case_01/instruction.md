---
bench_id: AB02-B-Cell-Biology_case_01
category: "Cell-Biology"
title: "Predicting cell-binding retention after developability repair"
format: ranking
input_mode: single_case_csv
pass_threshold: 1.0
---

# Prompt

The CSV contains matched parent and developability-repair anti-IL-2Rgamma VHHs. Predict cell-binding retention for every row with blank `cell_binding_retention`. The endpoint is the ratio of DP47-background-corrected MFI AUCs along log10 concentration to the matched-parent AUC, using the shared observed concentration window and the same figure panel. Rank targets from highest to lowest retention, excluding the measured parents. The published curves have digitization uncertainty; only the organizer-frozen resolvable pairs are scored, without forcing uncertain pairs into a true total order.

The following study information applies to this case:

All molecules are anti-IL-2Rgamma VHHs in the same monovalent VHH-Fc format. Human KD values are the printed Table 23 values against recombinant human IL-2Rbeta-gamma extracellular-domain reagent P1AE2657. These were measured on a Biacore 8K at 25 C, capturing VHH-Fc on an anti-PGLALA CM3 surface, using receptor as analyte and a 1:1 Langmuir fit. The benchmark neutral-pH label is 7.5. No numerical cynomolgus results are printed in this table; those fields remain unavailable. Cell binding was measured on human IL-2Rbeta-gamma Bioassay cells with antibody incubation for 60 min at 4 C and anti-human-Fc PE median-fluorescence detection. The hidden retention endpoint uses all 11 positive observed concentration columns from the published figure, excluding the separately plotted zero-dose control. Concentrations are digitized approximate chart coordinates rather than an asserted exact serial-dilution recipe. Parent, variant and DP47 curves are always matched within the same panel. Ranking is scored only on differences robust to conservative curve-reading and log-dose-coordinate uncertainty; unresolved pairs are not forced into an experimental total order.

Use only the supplied CSV and study information. Do not browse, execute code, or call external tools. Return one comma-separated line containing every target exactly once, without explanations. Each case and each task runs in an independent context; no sibling-task results or previous answers are supplied.

name,parent,format,sequence1,human_KD_nM,cyno_KD_nM,cell_binding_retention
M_1924494cab7ed3ff,M_45edc9838001954a,monovalent_VHH_Fc,EVQLVESGGGLVQAGGSLRLSCAASISISKIDLMGWYRQAPGKQRELVARVTSGGDSYYSTSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCYGVPESLAAFHWGQGTLVTVSS,2.27,,
M_d1626a0bdd500b6f,M_5b812563aead9b90,monovalent_VHH_Fc,EVQLVESGGGLVQAGGSLRLSCAASGSISKIDLMGWYRQAPGKQRELVSRVTHGGDSYYSTSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCYGVPESLAAFHWGQGTLVTVSS,11.7,,
M_6a5907eb3a180330,M_45edc9838001954a,monovalent_VHH_Fc,EVQLVESGGGLVQAGGSLRLSCAASISISKIDLMGWYRQAPGKQRELVARVTHGGDSYYSTSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCYGVPESLAAFHWGQGTLVTVSS,2.25,,
M_5b812563aead9b90,M_5b812563aead9b90,monovalent_VHH_Fc,EVQLVESGGGLVQAGGSLRLSCAASGSISKIDLMGWYRQAPGKQRELVSRVTNGGDSYYSTSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCYGVPESLAAFHWGQGTLVTVSS,8.69,,1.0
M_1a2795e21cb21218,M_5b812563aead9b90,monovalent_VHH_Fc,EVQLVESGGGLVQAGGSLRLSCAASGSISKIDLMGWYRQAPGKQRELVSRVTNMGDSYYSTSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCYGVPESLAAFHWGQGTLVTVSS,6.35,,
M_f88420a49ee89b39,M_45edc9838001954a,monovalent_VHH_Fc,EVQLVESGGGLVQAGGSLRLSCAASISISKIDLMGWYRQAPGKQRELVARVTNYGDSYYSTSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCYGVPESLAAFHWGQGTLVTVSS,1.82,,
M_f1b0f79445e47ac1,M_35bc2fb1c7968965,monovalent_VHH_Fc,EVQLVESGGGLVQPGGSLRLSCAASGFTSKIDLMGWYRQAPGKQRELVARVTDAGDSYYSTSVKGRFTISRDNSKNTLYLQMNSLKPEDTAVYYCYGVPESLAAFHWGQGTLVTVSS,18.8,,
M_35bc2fb1c7968965,M_35bc2fb1c7968965,monovalent_VHH_Fc,EVQLVESGGGLVQPGGSLRLSCAASGFTSKIDLMGWYRQAPGKQRELVARVTNGGDSYYSTSVKGRFTISRDNAKNTLYLQMNSLKPEDTAVYYCYGVPESLAAFHWGQGTLVTVSS,25.3,,1.0
M_9a59852efe898a4f,M_5b812563aead9b90,monovalent_VHH_Fc,EVQLVESGGGLVQAGGSLRLSCAASGSISKIDLMGWYRQAPGKQRELVSRVTSGGDSYYSTSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCYGVPESLAAFHWGQGTLVTVSS,7.96,,
M_0d7fbca4b855bbcc,M_45edc9838001954a,monovalent_VHH_Fc,EVQLVESGGGLVQAGGSLRLSCAASISISKIDLMGWYRQAPGKQRELVARVTNRGDSYYSTSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCYGVPESLAAFHWGQGTLVTVSS,4.71,,
M_392d77d4e91913ca,M_5b812563aead9b90,monovalent_VHH_Fc,EVQLVESGGGLVQAGGSLRLSCAASGSISKIDLMGWYRQAPGKQRELVSRVTDAGDSYYSTSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCYGVPESLAAFHWGQGTLVTVSS,17.0,,
M_45c5db3b0832c3a8,M_35bc2fb1c7968965,monovalent_VHH_Fc,EVQLVESGGGLVQPGGSLRLSCAASGFTSKIDLMGWYRQAPGKQRELVARVTSGGDSYYSTSVKGRFTISRDNSKNTLYLQMNSLKPEDTAVYYCYGVPESLAAFHWGQGTLVTVSS,7.05,,
M_0a5e41e28146b777,M_45edc9838001954a,monovalent_VHH_Fc,EVQLVESGGGLVQAGGSLRLSCAASISISKIDLMGWYRQAPGKQRELVARVTNMGDSYYSTSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCYGVPESLAAFHWGQGTLVTVSS,0.78,,
M_1760cc48565fdaed,M_45edc9838001954a,monovalent_VHH_Fc,EVQLVESGGGLVQAGGSLRLSCAASISISKIDLMGWYRQAPGKQRELVARVTDAGDSYYSTSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCYGVPESLAAFHWGQGTLVTVSS,2.94,,
M_45edc9838001954a,M_45edc9838001954a,monovalent_VHH_Fc,EVQLVESGGGLVQAGGSLRLSCAASISISKIDLMGWYRQAPGKQRELVARVTNGGDSYYSTSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCYGVPESLAAFHWGQGTLVTVSS,2.22,,1.0
