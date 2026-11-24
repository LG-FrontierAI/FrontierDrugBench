---
bench_id: "T2-Pocket-AbAg-Structure-case-15"
category: "Molecular-Biology"
title: "Predict and rank antibody binding epitopes from antigen sequence (case-15)"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

# Role

You are an expert in protein structure, antigen–antibody recognition, and structural immunology.

# Task

Given the amino acid sequences of all proteins that constitute one antigen, identify the antigen's potential antibody-binding epitopes.

You are not provided with an antibody sequence, antibody structure, antibody identity, PDB entity identifiers, chain identifiers, or any information about the actual antigen–antibody complex. Infer potential antibody-binding regions solely from the supplied antigen protein sequences and your knowledge of protein structure and molecular recognition.

Each question describes one complete antigen from one benchmark complex. The antigen may contain one or multiple proteins. The neutral labels `protein_1`, `protein_2`, and so on identify the supplied proteins only within this question.

An antigen may contain multiple distinct epitopes recognized by different antibodies. Predict all distinct epitopes that you judge plausible across all supplied antigen proteins and rank them from most to least likely. There is no fixed maximum number of epitopes.

Your task is to predict **epitopes on the antigen**, not paratopes on an antibody.

# Definition of an Epitope

An epitope is a spatially coherent region of an antigen protein that can be directly recognized and contacted by an antibody.

Each predicted epitope must be represented by the **complete set of residues on one supplied antigen protein expected to participate directly in the antibody–antigen binding interface**.

Include all residues predicted to constitute the binding interface, rather than only a few representative residues or functional hotspots. Do not include unrelated residues merely to increase the size of a candidate.

An epitope may be conformational (discontinuous): its constituent residues can be separated in the primary amino acid sequence but spatially adjacent in the folded antigen.

Different supplied antigen proteins may each contain independent epitopes. Report those epitopes as separate array elements. Do not combine residue numbering from different proteins into one element, split a single epitope into partial predictions, or output duplicate or near-duplicate epitopes.

# Input

The following JSON array describes all proteins in one target antigen:

```json
[
  {
    "protein_id": "protein_1",
    "sequence_length": 85,
    "sequence": "HMGPPGPPGPPGPPGPPGASGDRGPPGPVGPPGLTGPAGEPGPPGPPGPPGPPGPPGSGYIPEAPRDGQAYVRKDGEWVLLSTFL"
  }
]
```

# Output Requirements

1. Output all distinct epitopes that you predict across all supplied antigen proteins, ranked by predicted likelihood in descending order.
2. Each epitope must specify exactly one input `protein_id` and the complete set of sequence positions on that protein.
3. Copy `protein_id` exactly from the input. Do not invent another identifier.
4. Use **1-based sequence indexing** independently for each protein.
5. Every residue index must be an integer between 1 and that protein's `sequence_length`, inclusive.
6. Sort residue indices within each epitope in ascending order, without duplicates.
7. Every `residues` array must be nonempty.
8. The `epitopes` array must be ordered from most to least likely.
9. The `rank` values must be consecutive JSON integers starting at 1 and must agree with the array order.
10. Return exactly one valid JSON object and nothing else.

# Required Output Format

```json
{
  "epitopes": [
    {
      "rank": 1,
      "protein_id": "protein_1",
      "residues": [25, 27, 30, 85, 88, 91]
    },
    {
      "rank": 2,
      "protein_id": "protein_2",
      "residues": [14, 17, 19, 42, 46]
    }
  ]
}
```

The identifiers and residue indices above are illustrative only. Predict the actual epitopes from the supplied antigen protein sequences.

# Strict Output Contract

- The top-level JSON object must contain exactly one key: `epitopes`.
- `epitopes` must be a JSON array.
- Every array element must contain exactly three keys: `rank`, `protein_id`, and `residues`.
- `rank` must be a JSON integer. Do not encode it as a string.
- `protein_id` must exactly equal one `protein_id` supplied in the input.
- `residues` must be a nonempty JSON array of unique JSON integers. Do not encode residue positions as strings.
- Do not include confidence scores, probabilities, names, descriptions, explanations, or any other fields.
- Do not wrap the JSON object in Markdown or a code fence.
- Do not output reasoning, comments, introductory text, or trailing text.
- Ensure that the response can be parsed directly by a standard JSON parser.
