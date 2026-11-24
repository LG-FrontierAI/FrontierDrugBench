---
bench_id: "PROT-V4-CLIN-002"
category: "Disease-Biology"
title: "PAH variant function prediction (position 157 R→N)"
format: "mcq"
input_mode: "inline_prompt"
---

# Prompt

## Context

```json
{
  "protein": "PAH",
  "reference_protein": "P00439",
  "wild_type_sequence": "MSTAVLENPGLGRKLSDFGQETSYIEDNCNQNGAISLIFSLKEEVGALAKVLRLFEENDVNLTHIESRPSRLKKDEYEFFTHLDKRSLPALTNIIKILRHDIGATVHELSRDKKKDTVPWFPRTIQELDRFANQILSYGAELDADHPGFKDPVYRARRKQFADIAYNYRHGQPIPRVEYMEEEKKTWGTVFKTLKSLYKTHACYEYNHIFPLLEKYCGFHEDNIPQLEDVSQFLQTCTGFRLRPVAGLLSSRDFLGGLAFRVFHCTQYIRHGSKPMYTPEPDICHELLGHVPLFSDRSFAQFSQEIGLASLGAPDEYIEKLATIYWFTVEFGLCKQGDSIKAYGAGLLSSFGELQYCLSEKPKLLPLELEKTAIQNYTVTEFQPLYYVAESFNDAKEKVRNFAATIPRPFSVRYDPYTQRIEVLDNTQQLKILADSINSEIGILCSALQKIK",
  "variant": "position 157 R→N",
  "experiment": "Express the PAH variant in A293 cells, defining WT enzyme activity in the same experiment as 100%."
}
```

## Question

Which interval is most likely to contain this variant's residual enzyme activity? Output only the letter(s) corresponding to your answer.

## Options

A. At least 80%
B. At least 10% but below 50%
C. At least 50% but below 80%
D. Below 10%
