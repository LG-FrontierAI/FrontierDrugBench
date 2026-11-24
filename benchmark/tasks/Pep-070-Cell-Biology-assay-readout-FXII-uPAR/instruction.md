---
bench_id: Pep-070-Cell-Biology-assay-readout-FXII-uPAR
category: "Cell-Biology"
format: mcq
---
# Prompt

Predict the direction of the supplied peptide's effect on the specified cellular endpoint. Use its sequence and covalent structure. No measured migration result is supplied.

{
  "target": "FXII-uPAR axis",
  "context": {
    "cells": "human neutrophils",
    "challenge": "FXII",
    "endpoint": "Boyden-chamber chemotaxis relative to matched vehicle",
    "peptide_concentration_uM": 10
  },
  "candidates": [
    {
      "id": "candidate_01",
      "sequence": "yTWQPEWYLKYYSSTTC",
      "residue_definitions": {
        "y": "D-tyrosine; uppercase residues are L"
      },
      "N_terminus_and_ring": "N-alpha-chloroacetyl-derived thioether linking the N terminus to terminal Cys side-chain sulfur",
      "C_terminus": "CONH2"
    }
  ]
}

A. Greater chemotaxis than vehicle
B. Lower chemotaxis than vehicle
C. No detectable change from vehicle

Reply with a single option letter only.
