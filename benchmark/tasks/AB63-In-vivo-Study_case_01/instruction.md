---
bench_id: AB63-In-vivo-Study_case_01
category: "In-vivo-Study"
title: "Predicting subcutaneous persistence from matched primate IV data"
format: ranking
task_type: "ranking"
input_mode: "single_case_csv"
pass_threshold: 0.6
---

# Prompt
Rank all ten IL-17A/F IgG1-YTE antibodies from highest to lowest terminal half-life after SC dosing in cynomolgus monkeys. Matched IV half-lives, human binding and functional results are visible. The experiment used a single 50 mg/kg dose, four animals per group and sampling through day 49. The reference antibody had IV/SC half-lives of 9.2/9.8 days. Predict the observed route-dependent outcome; target SC values are withheld and true experimental ties are retained in organizer scoring. Use only the supplied CSV. Do not browse, execute code, call external tools or explain. Return only one comma-separated line containing every target name, highest first.

name,format,Fc_mutations_EU,IV_half_life_days,SC_half_life_days,human_IL17A_kon_M_1_s_1,human_IL17A_koff_s_1,human_IL17A_KD_M,human_IL17F_kon_M_1_s_1,human_IL17F_koff_s_1,human_IL17F_KD_M,NFkB_IL17A_IC50_nM,NFkB_IL17F_IC50_nM,NHDF_IL6_IL17A_IC50_nM,NHDF_IL6_IL17F_IC50_nM
molecule_01,IgG1_YTE,M252Y/S254T/T256E,24.5,,759000.0,1.69e-05,2.22e-11,186000.0,0.000118,6.33e-10,0.058,15,0.015,0.678
molecule_02,IgG1_YTE,M252Y/S254T/T256E,24.0,,1750000.0,6.33e-06,3.61e-12,389000.0,5.97e-06,1.53e-11,0.056,12.5,0.014,0.719
molecule_03,IgG1_YTE,M252Y/S254T/T256E,19.4,,1320000.0,2.14e-05,1.62e-11,304000.0,0.000404,1.33e-09,0.069,12.3,0.017,0.808
molecule_04,IgG1_YTE,M252Y/S254T/T256E,29.7,,1250000.0,3.67e-05,2.93e-11,263000.0,5.02e-05,1.91e-10,0.055,11.6,0.015,0.675
molecule_05,IgG1_YTE,M252Y/S254T/T256E,22.7,,1680000.0,6.71e-06,4e-12,279000.0,0.000277,9.94e-10,0.047,14.6,0.015,0.729
molecule_06,IgG1_YTE,M252Y/S254T/T256E,17.0,,1670000.0,7.06e-06,4.23e-12,392000.0,2.09e-05,5.32e-11,0.055,14.9,0.015,0.63
molecule_07,IgG1_YTE,M252Y/S254T/T256E,21.5,,1500000.0,4.01e-05,2.68e-11,186000.0,0.00013,7e-10,0.06,15.6,0.013,0.545
molecule_08,IgG1_YTE,M252Y/S254T/T256E,20.4,,1680000.0,8.25e-06,4.91e-12,289000.0,6.05e-05,2.09e-10,0.061,15,0.013,0.7
molecule_09,IgG1_YTE,M252Y/S254T/T256E,31.2,,1190000.0,3.05e-06,2.56e-12,312000.0,4.55e-05,1.46e-10,0.055,13.6,0.015,0.772
molecule_10,IgG1_YTE,M252Y/S254T/T256E,24.9,,1780000.0,2.55e-06,1.44e-12,402000.0,0.000172,4.28e-10,0.049,14.3,0.014,0.74
