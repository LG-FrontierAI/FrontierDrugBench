---
bench_id: Pep-095-Molecular-Biology-enzyme-IC50-FXIa
category: "Molecular-Biology"
format: ranking
---
# Prompt

Target: **FXIa**  
Assay: **continuous chromogenic enzyme inhibition assay**  
Property to rank: **FXIa enzyme IC50**

Rank the listed candidates from lower to higher measured FXIa enzyme IC50. Predict the ranking using the supplied candidate sequences, sequence-notation definitions, molecular annotations, and assay context. The measured values are withheld from the model and used only by the evaluator.

{
  "target": "FXIa",
  "assay": "continuous chromogenic enzyme inhibition assay",
  "endpoint": "FXIa enzyme IC50",
  "direction_to_rank": "lower to higher",
  "context": {
    "target": "FXIa",
    "system": "purified enzyme",
    "unit": "nM",
    "assay_conditions": "Table 3, same continuous enzyme assay"
  },
  "candidates": [
    {
      "id": "1",
      "value_unit": "nM",
      "sequence": "YPHGLNRHTFC"
    },
    {
      "id": "2",
      "value_unit": "nM",
      "sequence": "YHWKTTRSNYLC"
    },
    {
      "id": "3",
      "value_unit": "nM",
      "sequence": "YHFLNIRSNYDC"
    },
    {
      "id": "4",
      "value_unit": "nM",
      "sequence": "YHDRYIRSNYLC"
    },
    {
      "id": "5",
      "value_unit": "nM",
      "sequence": "YIPASFVNTRLHC"
    },
    {
      "id": "6",
      "value_unit": "nM",
      "sequence": "yAYRIVWPDRTQYEC"
    },
    {
      "id": "7",
      "value_unit": "nM",
      "sequence": "yLLGPYVRIVC"
    },
    {
      "id": "8",
      "value_unit": "nM",
      "sequence": "yRTRIEDIFC"
    },
    {
      "id": "9",
      "value_unit": "nM",
      "sequence": "yHWRNIRSNYSC"
    }
  ],
  "sequence_notation": {
    "source": "WO2026006882, paragraph 0049",
    "verbatim_definition": "[0049] D-isomers of the proteinogenic naturally occurring amino acids may be denoted herein using the corresponding lower case letter of the single letter code included in Table 1 above. For example, in amino acid sequences included herein ‘a’ denotes D-alanine, and ‘y’ denotes D-tyrosine, and so on.",
    "topology_note": "The candidate peptides are cyclic constructs with a thioether linkage between the N-terminal chloroacetyl-derived group and the cysteine side chain. Sequence strings are residue order, not a claim that the measured molecules are unmodified linear peptides.",
    "topology_source": "WO2026006882, paragraph 0086 and compound-specific descriptions for peptides 1–9."
  }
}

Return one JSON array of candidate IDs in the requested order. Do not include explanations. For equal values, sort IDs ascending.
