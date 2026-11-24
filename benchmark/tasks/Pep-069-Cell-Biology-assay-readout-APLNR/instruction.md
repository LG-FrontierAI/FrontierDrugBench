---
bench_id: Pep-069-Cell-Biology-assay-readout-APLNR
category: "Cell-Biology"
format: mcq
---
# Prompt

Predict the cellular signaling profile for the supplied peptide in the two assays. The measured signaling responses and bias classification are hidden. Choose one profile.

{
  "target": "APLNR",
  "context": {
    "cells": "HEK293",
    "readouts": [
      "NanoBiT G-protein dissociation",
      "BRET beta-arrestin recruitment"
    ],
    "comparison": "detectable response within the source study assay range; ND is not a numerical zero"
  },
  "candidates": [
    {
      "id": "candidate_01",
      "sequence_modified": "C15-alkyl-CO-γGlu-Cys-Arg-Pro-Arg-Leu-Cys-His-Lys-Gly-Pro-DMet-Gly-Pro-Phe (Disulfide bridge:1-6)",
      "definitions": {
        "DMet": "D-methionine",
        "γGlu": "gamma-glutamyl linker",
        "C15-alkyl-CO": "hexadecanoyl group",
        "disulfide 1-6": "between first and sixth residues of the Cys-initiated peptide core"
      },
      "terminal_cap": "not separately specified in source Table 4"
    }
  ]
}

A. G-protein response detectable; beta-arrestin response not detected
B. Both G-protein and beta-arrestin responses detectable
C. G-protein response not detected; beta-arrestin response detectable
D. Neither response detected

Reply with a single option letter only.
