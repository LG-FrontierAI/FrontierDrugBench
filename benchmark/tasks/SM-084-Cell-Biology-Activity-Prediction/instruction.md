---
bench_id: "SM-084-Cell-Biology-Activity-Prediction"
category: "Cell-Biology"
format: "structured_json"
---
# Prompt

Predict cellular protein-degradation DC50 for IRAK4, KRAS G12D, CCDC6-RET and ERalpha. There are 50 distinct molecules. Total: 100 points.

This task assesses degradation concentration potency. No Dmax is inferred from DC50. KRAS records with only a 24-48 h method range are used for interval prediction; comparisons and ordering use only their matched, source-specific assay context.

Use each molecule's assay context. In the tables below, P denotes its stated IC50, EC50, DC50, qAC50 or CD, expressed in nM. Lower P means greater concentration potency.

## Reference protein sequences

Reference FASTA files are provided as `KRAS_HUMAN_P01116_G12D_derived.fasta`, `KRAS_HUMAN_P01116_WT_full_length.fasta`, `CCDC6_HUMAN_Q16204_native_component.fasta`, `RET_HUMAN_P07949_native_component.fasta`, `ESR1_HUMAN_P03372_full_length.fasta` and `IRAK4_HUMAN_Q9NWZ3_full_length.fasta`. The KRAS files include canonical WT KRAS and a derived G12D reference; the assay context is KRAS G12D. For CCDC6–RET, the files are native CCDC6 and RET component references; the exact fusion junction and tagged assay construct are not provided. Use these sequences only as auxiliary references together with the stated cellular assay context.

Target FASTA (`KRAS_HUMAN_P01116_G12D_derived.fasta`):

>KRAS_HUMAN|P01116|G12D|derived_from_WT_reference
MTEYKLVVVGADGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAGQEEYSAMRDQYMRTGEGFLC
VFAINNTKSFEDIHHYREQIKRVKDSEDVPMVLVGNKCDLPSRTVDTKQAQDLARSYGIPFIETSAKTRQRVEDAFYTLV
REIRQYRLKKISKEEKTPGCVKIKKCIIM

Target FASTA (`KRAS_HUMAN_P01116_WT_full_length.fasta`):

>KRAS_HUMAN|P01116|WT_full_length|UniProt_reference
MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAGQEEYSAMRDQYMRTGEGFLC
VFAINNTKSFEDIHHYREQIKRVKDSEDVPMVLVGNKCDLPSRTVDTKQAQDLARSYGIPFIETSAKTRQRVEDAFYTLV
REIRQYRLKKISKEEKTPGCVKIKKCIIM

Target FASTA (`CCDC6_HUMAN_Q16204_native_component.fasta`):

>CCDC6_HUMAN|Q16204|native_full_length_component|CCDC6-RET_reference
MADSASESDTDGAGGNSSSSAAMQSSCSSTSGGGGGGGGGGGGGKSGGIVISPFRLEELTNRLASLQQENKVLKIELETY
KLKCKALQEENRDLRKASVTIQARAEQEEEFISNTLFKKIQALQKEKETLAVNYEKEEEFLTNELSRKLMQLQHEKAELE
QHLEQEQEFQVNKLMKKIKKLENDTISKQLTLEQLRREKIDLENTLEQEQEALVNRLWKRMDKLEAEKRILQEKLDQPVS
APPSPRDISMEIDSPENMMRHIRFLKNEVERLKKQLRAAQLQHSEKMAQYLEEERHMREENLRLQRKLQREMERREALCR
QLSESESSLEMDDERYFNEMSAQGLRPRTVSSPIPYTPSPSSSRPISPGLSYASHTVGFTPPTSLTRAGMSYYNSPGLHV
QHMGTSHGITRPSPRRSNSPDKFKRPTPPPSPNTQTPVQPPPPPPPPPMQPTVPSAATSQPTPSQHSAHPSSQP

Target FASTA (`RET_HUMAN_P07949_native_component.fasta`):

>RET_HUMAN|P07949|native_full_length_component|CCDC6-RET_reference
MAKATSGAAGLRLLLLLLLPLLGKVALGLYFSRDAYWEKLYVDQAAGTPLLYVHALRDAPEEVPSFRLGQHLYGTYRTRL
HENNWICIQEDTGLLYLNRSLDHSSWEKLSVRNRGFPLLTVYLKVFLSPTSLREGECQWPGCARVYFSFFNTSFPACSSL
KPRELCFPETRPSFRIRENRPPGTFHQFRLLPVQFLCPNISVAYRLLEGEGLPFRCAPDSLEVSTRWALDREQREKYELV
AVCTVHAGAREEVVMVPFPVTVYDEDDSAPTFPAGVDTASAVVEFKRKEDTVVATLRVFDADVVPASGELVRRYTSTLLP
GDTWAQQTFRVEHWPNETSVQANGSFVRATVHDYRLVLNRNLSISENRTMQLAVLVNDSDFQGPGAGVLLLHFNVSVLPV
SLHLPSTYSLSVSRRARRFAQIGKVCVENCQAFSGINVQYKLHSSGANCSTLGVVTSAEDTSGILFVNDTKALRRPKCAE
LHYMVVATDQQTSRQAQAQLLVTVEGSYVAEEAGCPLSCAVSKRRLECEECGGLGSPTGRCEWRQGDGKGITRNFSTCSP
STKTCPDGHCDVVETQDINICPQDCLRGSIVGGHEPGEPRGIKAGYGTCNCFPEEEKCFCEPEDIQDPLCDELCRTVIAA
AVLFSFIVSVLLSAFCIHCYHKFAHKPPISSAEMTFRRPAQAFPVSYSSSGARRPSLDSMENQVSVDAFKILEDPKWEFP
RKNLVLGKTLGEGEFGKVVKATAFHLKGRAGYTTVAVKMLKENASPSELRDLLSEFNVLKQVNHPHVIKLYGACSQDGPL
LLIVEYAKYGSLRGFLRESRKVGPGYLGSGGSRNSSSLDHPDERALTMGDLISFAWQISQGMQYLAEMKLVHRDLAARNI
LVAEGRKMKISDFGLSRDVYEEDSYVKRSQGRIPVKWMAIESLFDHIYTTQSDVWSFGVLLWEIVTLGGNPYPGIPPERL
FNLLKTGHRMERPDNCSEEMYRLMLQCWKQEPDKRPVFADISKDLEKMMVKRRDYLDLAASTPSDSLIYDDGLSEEETPL
VDCNNAPLPRALPSTWIENKLYGMSDPNWPGESPVPLTRADGTNTGFPRYPNDSVYANWMLSPSAAKLMDTFDS

Target FASTA (`ESR1_HUMAN_P03372_full_length.fasta`):

>ESR1_HUMAN|P03372|full_length|UniProt_reference
MTMTLHTKASGMALLHQIQGNELEPLNRPQLKIPLERPLGEVYLDSSKPAVYNYPEGAAYEFNAAAAANAQVYGQTGLPY
GPGSEAAAFGSNGLGGFPPLNSVSPSPLMLLHPPPQLSPFLQPHGQQVPYYLENEPSGYTVREAGPPAFYRPNSDNRRQG
GRERLASTNDKGSMAMESAKETRYCAVCNDYASGYHYGVWSCEGCKAFFKRSIQGHNDYMCPATNQCTIDKNRRKSCQAC
RLRKCYEVGMMKGGIRKDRRGGRMLKHKRQRDDGEGRGEVGSAGDMRAANLWPSPLMIKRSKKNSLALSLTADQMVSALL
DAEPPILYSEYDPTRPFSEASMMGLLTNLADRELVHMINWAKRVPGFVDLTLHDQVHLLECAWLEILMIGLVWRSMEHPG
KLLFAPNLLLDRNQGKCVEGMVEIFDMLLATSSRFRMMNLQGEEFVCLKSIILLNSGVYTFLSSTLKSLEEKDHIHRVLD
KITDTLIHLMAKAGLTLQQQHQRLAQLLLILSHIRHMSNKGMEHLYSMKCKNVVPLYDLLLEMLDAHRLHAPTSRGGASV
EETDQSHLATAGSTSSHSLQKYYITGEAEGFPATV

Target FASTA (`IRAK4_HUMAN_Q9NWZ3_full_length.fasta`):

>IRAK4_HUMAN|Q9NWZ3|full_length|UniProt_reference
MNKPITPSTYVRCLNVGLIRKLSDFIDPQEGWKKLAVAIKKPSGDDRYNQFHIRRFEALLQTGKSPTSELLFDWGTTNCT
VGDLVDLLIQNEFFAPASLLLPDAVPKTANTLPSKEAITVQQKQMPFCDKDRTLMTPVQNLEQSYMPPDSSSPENKSLEV
SDTRFHSFSFYELKNVTNNFDERPISVGGNKMGEGGFGVVYKGYVNNTTVAVKKLAAMVDITTEELKQQFDQEIKVMAKC
QHENLVELLGFSSDGDDLCLVYVYMPNGSLLDRLSCLDGTPPLSWHMRCKIAQGAANGINFLHENHHIHRDIKSANILLD
EAFTAKISDFGLARASEKFAQTVMTSRIVGTTAYMAPEALRGEITPKSDIYSFGVVLLEIITGLPAVDEHREPQLLLDIK
EEIEDEEKTIEDYIDKKMNDADSTSVEAMYSVASQCLHEKKNKRPDIKKVQQLLQEMTAS


## Assay contexts

| Context | Conditions and endpoint |
|---|---|
| C01 | KRAS G12D-HiBiT knock-in HEK293 cells; Nano-Glo HiBiT lytic detection; DC50. WT and derived G12D KRAS reference sequences are provided; the HiBiT tag is not included. The series method reports 24-48 h treatment without assigning a duration to each compound. |
| C02 | Human MCF-7 cells; 24 h treatment; ERalpha protein degradation quantified by In-Cell Western; DC50. |
| C03 | Human THP-1 cells; 24 h treatment; IRAK4 degradation quantified with HiBiT lytic detection; DC50. |
| C04 | Human TPC-1 cells carrying wild-type CCDC6-RET fusion; 24 h compound treatment; total RET protein measured by AlphaLISA; native CCDC6 and RET component references are provided, but the exact fusion junction is not provided. |

## Molecules

| Molecule ID | Context | SMILES |
|---|---|---|
| M001 | C01 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@@](C)(O)C5)nc(OCC5(CN6CCC(F)(CN7CCN(c8ccc9c(c8)n(C)c(=O)n9C8CCC(=O)NC8=O)CC7)CC6)CC5)nc4c3F)c12` |
| M002 | C02 | `Oc1ccc2c(c1)CCC[C@H](c1ccc(F)cc1F)[C@@H]2c1ccc(OCCN2CC(CF)C2)cc1` |
| M003 | C01 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cc3c(cc21)C1(CCN(CC2(F)CCN(CC4(COc5nc6c7c(nc(-c8c(C9CC9)c(Cl)cc9[nH]ncc89)c(F)c7n5)OC[C@@H]5COCCCN65)CC4)CC2)CC1)CO3` |
| M004 | C01 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@]6(CCO6)C5)nc(OCC5(CN6CCC(CN7CCC8(CC7)COc7cc9c(cc78)n(C)c(=O)n9C7CCC(=O)NC7=O)CC6)CC5)nc4c3F)c12` |
| M005 | C01 | `CC1CCCc2cc3[nH]ncc3c(-c3nc4c5c(nc(OCC6(CN7CCC(F)(CN8CCC9(CC8)COc8cc%10c(cc89)n(C)c(=O)n%10C8CCC(=O)NC8=O)CC7)CC6)nc5c3F)N3CCCOC[C@H]3CO4)c21` |
| M006 | C02 | `CC(=O)N1CCC([C@H]2COc3cc(O)ccc3[C@H]2c2ccc(OCCN3CC(CF)C3)cc2)CC1` |
| M007 | C01 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@]6(CCO6)C5)nc(OCC5(CN6CCC(F)(CN7CCC8(CC7)COc7cc9c(cc78)n(C)c(=O)n9C7CCC(=O)NC7=O)CC6)CCC5)nc4c3F)c12` |
| M008 | C03 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(C#CCO[C@H]3CC[C@](F)(CN4CCC5(CC4)Cc4cc(NC(=O)c6cnn7cccnc67)c(N6CCC(CO)CC6)cc4O5)CC3)c21` |
| M009 | C04 | `CCOc1cc(-c2ccc(N3CCC(CN(C)C(=O)CCCCN4CCN(c5ccc6c(c5)C(=O)N(C5CCC(=O)NC5=O)C6)CC4)(NC(=O)c4cc(F)ccc4F)CC3)nc2)c2c(C#N)cnn2c1` |
| M010 | C04 | `CCOc1cc(-c2ccc(N3CCC(CN4CCN(C(=O)CCN5CCC(c6ccc7c(c6)CN(C6CCC(=O)NC6=O)C7=O)CC5)CC4)(NC(=O)c4cc(F)ccc4F)CC3)nc2)c2c(C#N)cnn2c1` |
| M011 | C04 | `COC1(C(=O)N[C@@H](C)c2ccc(-n3cc(F)cn3)nc2)CCN(c2nc(CCCCC(=O)NCCCCCCCCNc3ccc(C4CCC(=O)NC4=O)cc3)cc(Nc3cc(C)[nH]n3)n2)CC1` |
| M012 | C01 | `CCc1c(F)ccc2cc(O)cc(-c3nc4c5c(nc(OCC6(CN7CCC(F)(CN8CCC9(CC8)COc8cc%10c(cc89)n(C)c(=O)n%10C8CCC(=O)NC8=O)CC7)CC6)nc5c3F)N3CCCOC[C@H]3CO4)c12` |
| M013 | C04 | `CCOc1cc(-c2ccc(N3CCC(CN4CCN(CC)CC4)(NC(=O)c4cc(F)ccc4F)CC3)nc2)c2c(C#N)cnn2c1` |
| M014 | C02 | `Cc1cc(F)ccc1[C@H]1CSc2cc(O)ccc2[C@H]1c1ccc(OCCN2CC(CF)C2)cc1` |
| M015 | C01 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CC6CCC(C5)N6)nc(OCC5(CN6CCC(F)(CN7CCC8(CC7)COc7cc9c(cc78)n(C)c(=O)n9C7CCC(=O)NC7=O)CC6)CC5)nc4c3F)c12` |
| M016 | C03 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(C#CCO[C@H]3CC[C@H](CN4CCC5(CC4)Oc4cc(NC(=O)c6cnn7cccnc67)c(N6CCC(CO)CC6)cc4O5)CC3)c21` |
| M017 | C02 | `COc1ccc([C@H]2CSc3cc(O)ccc3[C@H]2c2ccc(OCCN3CC(CF)C3)cc2)c(F)c1` |
| M018 | C04 | `CCOc1cc(-c2ccc(N3CCC(CN4CCN(C(=O)CCCCCCN5CCN(c6ccc7c(c6)CN(C6CCC(=O)NC6=O)C7=O)CC5)CC4)(NC(=O)c4cc(F)ccc4F)CC3)nc2)c2c(C#N)cnn2c1` |
| M019 | C02 | `COc1cc(F)ccc1[C@@H]1CSc2cc(O)ccc2[C@@H]1c1ccc(OCCN2CC(CF)C2)cc1` |
| M020 | C04 | `CCOc1cc(-c2ccc(N3CCC(CN4CCN(C(=O)CCN5CCC(c6ccc7c(c6)C(=O)N(C6CCC(=O)NC6=O)C7)CC5)CC4)(NC(=O)c4ncccc4F)CC3)nc2)c2c(C#N)cnn2c1` |
| M021 | C02 | `Oc1ccc2c(c1)OC[C@H](c1ccc(OC(F)(F)F)cc1F)[C@@H]2c1ccc(OCCN2CC(CF)C2)cc1` |
| M022 | C01 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@@](C)(O)C5)nc(OCC5(CN6CCC7(CC6)CC(N6CCC8(CC6)COc6cc9c(cc68)n(C)c(=O)n9C6CCC(=O)NC6=O)C7)CC5)nc4c3F)c12` |
| M023 | C01 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@@](C)(O)C5)nc(OCC5(CN6CCC(CN7CCC8(CC7)COc7cc9c(cc78)n(C)c(=O)n9C7CCC(=O)NC7=O)CC6)CC5)nc4c3F)c12` |
| M024 | C03 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(C#CCO[C@H]3CC[C@H](CN4CCC5(CC4)Oc4cc(N6CCC(CO)CC6)c(NC(=O)c6cnn7cccnc67)cc4C5=O)CC3)c21` |
| M025 | C04 | `CCOc1cc(-c2ccc(N3CCC(CN4CCC(CN5CC(N6CCC(c7ccc8c(c7)C(=O)N(C7CCC(=O)NC7=O)C8)CC6)C5)CC4)(NC(=O)c4cc(F)ccc4F)CC3)nc2)c2c(C#N)cnn2c1` |
| M026 | C04 | `CCOc1cc(-c2ccc(N3CCC(CC)(CN4CCN(C(=O)CCN5CCC(c6ccc7c(c6)C(=O)N(C6CCC(=O)NC6=O)C7)CC5)CC4)CC3)nc2)c2c(C#N)cnn2c1` |
| M027 | C01 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cc3c(cc21)C1(CCN(CC2(F)CCN(CC4(COc5nc(N6CCC[C@]7(CCO7)C6)c6cnc(-c7c(C8CC8)c(Cl)cc8[nH]ncc78)c(F)c6n5)CC4)CC2)CC1)CO3` |
| M028 | C04 | `COC1(C(=O)N[C@@H](CCCN)c2ccc(-n3cc(F)cn3)nc2)CCN(c2nc(C)cc(Nc3cc(C)[nH]n3)n2)CC1` |
| M029 | C01 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@]6(CCO6)C5)nc(OCC5(CN6CCC(F)(CN7CCC8(CC7)COc7cc9c(cc78)n(C)c(=O)n9C7CCC(=O)NC7=O)CC6)CC5(F)F)nc4c3F)c12` |
| M030 | C01 | `CCc1c(F)ccc2cc(O)cc(-c3ncc4c(N5CCC[C@]6(CCO6)C5)nc(OCC5(CN6CCC7(CC6)CC(N6CCC8(CC6)COc6cc9c(cc68)n(C)c(=O)n9C6CCC(=O)NC6=O)C7)CC5)nc4c3F)c12` |
| M031 | C03 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(C#CCOC3CCN(C(=O)CN4CCC5(CC4)Cc4cc(NC(=O)c6cnn7cccnc67)c(N6CCC(CO)CC6)cc4O5)CC3)c21` |
| M032 | C03 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(C#CCOC3CCN(CC(=O)N4CCC5(CC4)Cc4cc(NC(=O)c6cnn7cccnc67)c(N6CCC(CO)CC6)cc4O5)CC3)c21` |
| M033 | C04 | `CCOc1cc(-c2ccc(N3CCC(CN4CCN(C(=O)CCN5CCN(c6cccc(C7CCC(=O)NC7=O)c6)CC5)CC4)(NC(=O)c4cc(F)ccc4F)CC3)nc2)c2c(C#N)cnn2c1` |
| M034 | C04 | `CCOc1cc(-c2ccc(N3CCC(CN4CCN(C(=O)CCN5CCN(c6ccc(C7CCC(=O)NC7=O)cc6)CC5)CC4)(NC(=O)c4cc(F)ccc4F)CC3)nc2)c2c(C#N)cnn2c1` |
| M035 | C02 | `Oc1ccc2c(c1)SC[C@H](c1ccc(F)cc1F)[C@@H]2c1ccc(OCCN2CC(CF)C2)cc1` |
| M036 | C02 | `Oc1ccc2c(c1)SC[C@@H](c1cc(F)c(F)cc1F)[C@H]2c1ccc(OCCN2CC(CF)C2)cc1` |
| M037 | C04 | `CCOc1cc(-c2ccc(N3CCC(CN4CCC(CN5CCN(c6ccc7c(c6)C(=O)N(C6CCC(=O)NC6=O)C7)CC5)CC4)(NC(=O)c4cc(F)ccc4F)CC3)nc2)c2c(C#N)cnn2c1` |
| M038 | C04 | `CCOc1cc(-c2ccc(N3CCC(CN4CCC(N5CCN(c6ccc7c(c6)C(=O)N(C6CCC(=O)NC6=O)C7)CC5)CC4)(NC(=O)c4cc(F)ccc4F)CC3)nc2)c2c(C#N)cnn2c1` |
| M039 | C03 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(C#CCO[C@H]3CC[C@H](CN4CCC5(CC4)Cc4cc(NC(=O)c6cnn7cccnc67)c(N6CCC(CO)CC6)cc4O5)CC3)c21` |
| M040 | C03 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(C#CCO[C@H]3CC[C@H](CN4CCC5(CC4)Cc4cc(NC(=O)c6cnn7cccnc67)c(N6CCC(C(=O)O)CC6)cc4O5)CC3)c21` |
| M041 | C03 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(CN3CCC4(CC3)CN(CCN3CCC5(CC3)Cc3cc(NC(=O)c6cnn7cccnc67)c(N6CCC(CO)CC6)cc3O5)C4)c21` |
| M042 | C03 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(CN3CC4(CCN(CCN5CCC6(CC5)Cc5cc(NC(=O)c7cnn8cccnc78)c(N7CCC(CO)CC7)cc5O6)CC4)C3)c21` |
| M043 | C02 | `COc1cc(F)ccc1[C@H]1COc2cc(O)ccc2[C@H]1c1ccc(OCCN2CC(CF)C2)cc1` |
| M044 | C02 | `Cn1cc([C@H]2COc3cc(O)ccc3[C@H]2c2ccc(OCCN3CC(CF)C3)cc2)cn1` |
| M045 | C02 | `COc1ccc([C@H]2COc3cc(O)ccc3[C@H]2c2ccc(OCCN3CC(CF)C3)cc2)cn1` |
| M046 | C02 | `Oc1ccc2c(c1)OC[C@H](c1cccc(F)c1F)[C@@H]2c1ccc(OCCN2CC(CF)C2)cc1` |
| M047 | C03 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(C#CCO[C@H]3CC[C@@](F)(CN4CCC5(CC4)Cc4cc(NC(=O)c6cnn7cccnc67)c(N6CCC(CO)CC6)cc4O5)CC3)c21` |
| M048 | C03 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(C#CCO[C@H]3CC[C@H](CN4CCC5(CC4)Cc4cc(NC(=O)c6cnn7cccnc67)c(N6CCC(O)CC6)cc4O5)CC3)c21` |
| M049 | C03 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(C#CCO[C@H]3CC[C@H](CN4CCC5(CC4)Cc4cc(NC(=O)c6cnn7cccnc67)c(N6CCC(F)CC6)cc4O5)CC3)c21` |
| M050 | C03 | `Cn1c(=O)n(C2CCC(=O)NC2=O)c2cccc(C#CCO[C@H]3CC[C@H](CN4CCC5(CC4)Cc4cc(NC(=O)c6cnn7cccnc67)c(N6CCC(CO)CC6)cc4C5)CC3)c21` |

## 1. Concentration intervals

| Label | P (nM) |
|---|---|
| L | < 10 |
| M | 10 to < 100 |
| H | >= 100 |

These are assay-specific concentration intervals, not universal clinical or development criteria.

Each correct item earns 2 points (30 items; 60 points).

| Item | Molecule |
|---|---|
| Q001 | M001 |
| Q002 | M002 |
| Q003 | M003 |
| Q004 | M004 |
| Q005 | M005 |
| Q006 | M006 |
| Q007 | M007 |
| Q008 | M008 |
| Q009 | M009 |
| Q010 | M010 |
| Q011 | M011 |
| Q012 | M012 |
| Q013 | M013 |
| Q014 | M014 |
| Q015 | M015 |
| Q016 | M016 |
| Q017 | M017 |
| Q018 | M018 |
| Q019 | M019 |
| Q020 | M020 |
| Q021 | M021 |
| Q022 | M022 |
| Q023 | M023 |
| Q024 | M024 |
| Q025 | M025 |
| Q026 | M026 |
| Q027 | M027 |
| Q028 | M028 |
| Q029 | M029 |
| Q030 | M030 |

## 2. Analogue comparisons

Compare concentration potency within each pair. Define R = P(right)/P(left).

| Answer | Criterion | Interpretation |
|---|---|---|
| A | R > 3 | Left has greater concentration potency |
| B | 1/3 <= R <= 3 | Concentration potencies are within threefold |
| C | R < 1/3 | Right has greater concentration potency |

B is a numerical comparison category, not a claim of statistical equivalence. Each pair uses one assay context.

Each correct item earns 4 points (6 items; 24 points).

| Item | Left molecule | Right molecule |
|---|---|---|
| Q031 | M031 | M032 |
| Q032 | M033 | M034 |
| Q033 | M035 | M036 |
| Q034 | M037 | M038 |
| Q035 | M039 | M040 |
| Q036 | M041 | M042 |

## 3. Within-series ordering

Order each group from lowest to highest P (strongest to weakest concentration potency). All four molecules share one assay context. Use every listed molecule exactly once.

Each group earns 8 * max(0, Spearman rho) points for the submitted versus reference order (2 groups; 16 points).

| Item | Molecules to order |
|---|---|
| Q037 | M043, M044, M045, M046 |
| Q038 | M047, M048, M049, M050 |

## Response format and scoring

Return ONLY one strict JSON object mapping Q001-Q038 to responses: L/M/H for classification, A/B/C for comparisons, and an ordered array of molecule IDs for ordering.

Syntax example only; the values do not imply answers:

`{"Q001": "L", "Q031": "B", "Q037": ["M043", "M044", "M045", "M046"]}`

Missing or invalid items earn zero. An ordering array must contain every listed molecule exactly once. Invalid JSON, duplicate JSON keys, or unknown Q identifiers invalidate the response. The scoring function returns total points divided by 100 on a 0-1 scale.
