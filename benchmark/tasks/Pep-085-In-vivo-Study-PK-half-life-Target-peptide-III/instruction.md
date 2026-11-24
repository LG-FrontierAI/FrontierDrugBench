---
bench_id: Pep-085-In-vivo-Study-PK-half-life-Target-peptide-III
category: "In-vivo-Study"
format: ranking
---
# Prompt

Predict the ordering of the two administration conditions by mean terminal plasma half-life, from higher to lower. Both conditions use exactly the same molecule and dose. This is a route-conditioned PK comparison, not a ranking of different compounds. Target means are hidden.

{
  "molecule": {
    "id": "peptide_01",
    "sequence_modified": "2-[4-[(2-methylphenylaminocarbonyl)-amino]-phenyl]-acetyl-Cit-Glu-Ser-Val-AEEA-Lys(γGlu-eicosanedioic acid)-NH2",
    "modifications": "N-terminal arylacetyl; AEEA linker between backbone Val-Lys; γGlu-eicosanedioic acid on the Lys ε-amino group; C-terminal amidation",
    "definitions": {
      "Cit": "L-citrulline",
      "AEEA": "8-amino-3,6-dioxaoctanoic acid linker",
      "γGlu": "gamma-glutamyl linkage; Lys ε-amino side-chain attachment"
    }
  },
  "context": {
    "species": "male SD rat",
    "dose_mg_per_kg": 0.22,
    "formulation": "5% DMSO + 10% PEG400 + 85% saline",
    "assay": "LC-MS/MS",
    "endpoint": "mean terminal plasma half-life"
  },
  "candidates": [
    {
      "id": "condition_02",
      "molecule": "peptide_01",
      "route": "IV"
    },
    {
      "id": "condition_01",
      "molecule": "peptide_01",
      "route": "SC"
    }
  ]
}

Return a JSON array containing each candidate ID exactly once, in the requested order. Do not include explanations. Candidates with indistinguishable predicted values may be placed in either order.
