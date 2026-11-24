---
bench_id: "PROT-V4-MECH-012"
category: "Disease-Biology"
title: "IDH1 variant function prediction (position 132 R→H)"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "IDH1",
  "species": "Homo sapiens",
  "wild_type_sequence": "MSKKISGGSVVEMQGDEMTRIIWELIKEKLIFPYVELDLHSYDLGIENRDATNDQVTKDAAEAIKKHNVGVKCATITPDEKRVEEFKLKQMWKSPNGTIRNILGGTVFREAIICKNIPRLVSGWVKPIIIGRHAYGDQYRATDFVVPGPGKVEITYTPSDGTQKVTYLVHNFEEGGGVAMGMYNQDKSIEDFAHSSFQMALSKGWPLYLSTKNTILKKYDGRFKDIFQEIYDKQYKSQFEAQKIWYEHRLIDDMVAQAMKSEGGFIWACKNYDGDVQSDSVAQGYGSLGMMTSVLVCPDGKTVEAEAAHGTVTRHYRMYQKGQETSTNPIASIFAWTRGLAHRAKLDNNKELAFFANALEEVSIETIEAGFMTKDLAACIKGLPNVQRSDYLNTFEFMDKLGENLKIKLAQAKL",
  "variant": "position 132 R→H",
  "experiment": "Use purified human variant IDH1 with either isocitrate/NADP+ or α-ketoglutarate/NADPH. Detect products by LC-MS and chiral analysis, and monitor NADPH."
}
```

## Question

In addition to impaired normal activity, which new reaction is the best prediction to test first? Output only the letter(s) corresponding to your answer.

## Options

A. Uses α-ketoglutarate as substrate to predominantly produce S-2-hydroxyglutarate, using NADPH
B. Uses α-ketoglutarate as substrate to predominantly produce R-2-hydroxyglutarate, using NADH
C. Uses α-ketoglutarate as substrate to predominantly produce S-2-hydroxyglutarate, using NADH
D. Uses α-ketoglutarate as substrate to predominantly produce R-2-hydroxyglutarate, using NADPH
