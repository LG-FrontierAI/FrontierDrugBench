---
bench_id: LNP-022-Molecular-Biology-design-lipid-pka-il
category: "Molecular-Biology"
title: "Non-urea degradable dual-hydrophobic-arm lipid design (computational proxy scoring)"
format: structured_json
---

# Prompt

Following the modular lipid design direction of a first-publication patent from 2026, propose 10 distinct candidate molecules rather than predicting the experimental performance of a given formulation. Every candidate must be a single connected molecule containing a protonatable amine or pyridine-type N, at least one carboxylate ester and at least two saturated alkyl paths of C8 or longer as defined by the scorer, and must not contain a urea N-C(=O)-N; they must not contain a permanent quaternary ammonium. The ten molecules must cover at least 5 distinct amine-local head-group signatures; changing only the distal tail length does not count as head-group diversity. The target is a QupKake-predicted highest basic micro-pKa of the free molecule within 6.5–7.5, not a TNS-LNP apparent pKa. Output JSON: reason and a designs array, each entry with id (D01–D10), smiles and reason. Submitting fewer than 10 loses points for each missing entry; submit at most 10. Scoring uses a pre-registered computational proxy and does not represent in vivo delivery, toxicity, clinical efficacy or patent novelty. This task is a source-compliant migration of a baseline design task; do not claim the new constraints as patent-measured optimization results.

## Input

The structured model input is below (JSON).

```json
{
  "design_count": 10,
  "required_urea": false,
  "forbidden_urea": true,
  "constraints": [
    "One connected molecular graph",
    "Protonatable amine or pyridine N",
    "At least one carboxylate ester",
    "At least two terminal-to-branch/heteroatom paths of >=8 saturated carbons",
    "No permanent quaternary ammonium",
    "At least 5 distinct amine-local-two-bond-plus-touching-ring signatures"
  ],
  "reference_endpoint": "QupKake highest basic micro-pKa of the free molecule",
  "target_window": [
    6.5,
    7.5
  ],
  "score_weights_per_molecule": {
    "pka": 8,
    "il_classifier": 2
  },
  "experimental_efficacy_claim": false
}
```

## Output

Output only the JSON fields specified in the prompt; reason is required.

A missing or empty `reason` scores zero for the whole task.

Scoring rule (pre-registered computational proxy): at most 10 molecules, each scoring 8 × max(0, 1 - d/0.5) + 2 × IL classification probability, where d = max(6.5 - pKa, pKa - 7.5, 0); the total is then multiplied by min(1, amine-local head-group signature count/5).
