---
bench_id: "PROT-V4-CLIN-003"
category: "Disease-Biology"
title: "HNF1A variant function prediction (position 619 E→K)"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "HNF1A",
  "reference_protein": "P20823",
  "wild_type_sequence": "MVSKLSQLQTELLAALLESGLSKEALIQALGEPGPYLLAGEGPLDKGESCGGGRGELAELPNGLGETRGSEDETDDDGEDFTPPILKELENLSPEEAAHQKAVVETLLQEDPWRVAKMVKSYLQQHNIPQREVVDTTGLNQSHLSQHLNKGTPMKTQKRAALYTWYVRKQREVAQQFTHAGQGGLIEEPTGDELPTKKGRRNRFKWGPASQQILFQAYERQKNPSKEERETLVEECNRAECIQRGVSPSQAQGLGSNLVTEVRVYNWFANRRKEEAFRHKLAMDTYSGPPPGPGPGPALPAHSSPGLPPPALSPSKVHGVRYGQPATSETAEVPSSSGGPLVTVSTPLHQVSPTGLEPSHSLLSTEAKLVSAAGGPLPPVSTLTALHSLEQTSPGLNQQPQNLIMASLPGVMTIGPGEPASLGPTFTNTGASTLVIGLASTQAQSVPVINSMGSSLTTLQPVQFSQPLHPSYQQPLMPPVQSHVTQSPFMATMAQLQSPHALYSHKPEVAQYTHTGLLPQTMLITDTTNLSALASLTPTKQVFTSDTEASSESGLHTPASQATTLHVPSQDPASIQHLQPAHRLSASPTVSSSSLVLYQSSDSSNGQSHLLPSNHSVIETFISTQMASSSQ",
  "variant": "position 619 E→K",
  "experiment": "Measure DNA binding, transcriptional activation, and nuclear localization of the HNF1A variant separately, normalizing each readout to its corresponding WT control."
}
```

## Question

Which combination of the three readouts is the best prediction to test first? Output only the letter(s) corresponding to your answer.

## Options

A. Nuclear localization, DNA binding, and transcriptional activation all increase
B. DNA binding and transcriptional activation remain near WT, while nuclear localization decreases
C. DNA binding decreases markedly, while nuclear localization is largely preserved
D. DNA binding, transcriptional activation, and nuclear localization are all completely lost
