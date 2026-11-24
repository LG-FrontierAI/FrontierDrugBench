---
bench_id: AB05-Molecular-Biology_case_07
category: "Molecular-Biology"
format: design
title: "Paired VH/VL CDR design with AlphaFold 3 evaluation"
pass_threshold: 0.6
---

# Prompt

Design exactly ten distinct paired VH/VL candidates for the human extracellular target in the single supplied CSV. Optimize the AlphaFold 3 ranking score of the antigen-antibody complex while retaining the supplied framework.

The single CSV row supplies the target sequence, framework template(s), and allowed design positions. X marks a position to design; all other residues are fixed. Positions are one-based sequence indices separated by semicolons, not IMGT residue labels. Use only the 20 standard amino acids. Preserve every chain length, fixed residue and the supplied pairing, and replace all X positions. Sequence1 is VH and sequence2 is VL. The evaluated complex contains one copy each of the supplied antigen, VH and VL as three separate chains. This is an Fv complex; do not add CH1, CL, Fc, linkers or other constant regions. No experimentally verified epitope is prescribed.

Return only a CSV with header `name,sequence1,sequence2` and exactly ten rows using unique names, for example design_01 through design_10. All ten complete candidate sequences must be different. Do not include markdown fences or explanations. Row order does not affect the score.

After submission, the organizer predicts each complex with a frozen AlphaFold 3 protocol: seed 20261023 and five structure samples per candidate. A candidate's score is its highest raw ranking_score among all five samples, clipped to [0,1]. The case score is the arithmetic mean of all ten candidate scores. There are no additional binding, developability, novelty or diversity score gates. Sequence constraints remain mandatory. This computational score does not establish experimental binding or success probability.

Use only the supplied CSV. Do not browse, execute code or call external tools. Each case runs independently without any previous case answers or scores.

name,format,sequence1,sequence2,target_name,target_sequence,designable_positions1,designable_positions2
design_request,Fv,QSLVESGGGVVQPGRSLRLSCAASXXXXXXXXXICWVRQAPGKGLEWVGCXXXXXXXXNYASWARGRFTISKDNSKNTLYLQMNSLRAEDTAVYYCXXXXXXXXXXXXXWGQGTLVTVSS,ELVLTQSPSTLSASVGDRVTITCRASXXXXXXLAWYQQKPGKAPKLLIYXXXKLESGVPSRFSGSGSGTEFTLTISSLQPDDFATYYCXCXXXXXXXXXXFGGGTKVEIK,human TfR1 extracellular domain,CKGVEPKTECERLAGTESPVREEPGEDFPAARRLYWDDLKRKLSEKLDSTDFTGTIKLLNENSYVPREAGSQKDENLALYVENQFREFKLSKVWRDQHFVKIQVKDSAQNSVIIVDKNGRLVYLVENPGGYVAYSKAATVTGKLVHANFGTKKDFEDLYTPVNGSIVIVRAGKITFAEKVANAESLNAIGVLIYMDQTKFPIVNAELSFFGHAHLGTGDPYTPGFPSFNHTQFPPSRSSGLPNIPVQTISRAAAEKLFGNMEGDCPSDWKTDSTCRMVTSESKNVKLTVSNVLKEIKILNIFGVIKGFVEPDHYVVVGAQRDAWGPGAAKSGVGTALLLKLAQMFSDMVLKDGFQPSRSIIFASWSAGDFGSVGATEWLEGYLSSLHLKAFTYINLDKAVLGTSNFKVSASPLLYTLIEKTMQNVKHPVTGQFLYQDSNWASKVEKLTLDNAAFPFLAYSGIPAVSFCFCEDTDYPYLGTTMDTYKELIERIPELNKVARAAAEVAGQFVIKLTHDVELNLDYERYNSQLLSFVRDLNQYRADIKEMGLSLQWLYSARGDFFRATSRLTTDFGNAEKTDRFVMKKLNDRVMRVEYHFLSPYVSPKESPFRHVFWGSGSHTLPALLENLKLRKQNNGAFNETLFRNQLALATWTIQGAANALSGDVWDIDNEF,25;26;27;28;29;30;31;32;33;51;52;53;54;55;56;57;58;97;98;99;100;101;102;103;104;105;106;107;108;109,27;28;29;30;31;32;50;51;52;89;91;92;93;94;95;96;97;98;99;100
