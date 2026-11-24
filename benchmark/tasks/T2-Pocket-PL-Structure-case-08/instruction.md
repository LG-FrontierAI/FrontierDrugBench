---
bench_id: "T2-Pocket-PL-Structure-case-08"
category: "Molecular-Biology"
title: "Predict and rank small-molecule binding pockets from protein sequence (case-08)"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

You are an expert in protein structure, molecular recognition, and protein–ligand interactions.

# Task

Given only the amino acid sequence of a protein, identify its potential small-molecule ligand-binding pockets.

You are not provided with the identity, molecular structure, SMILES, or any other information about the ligand. Infer potential binding pockets solely from the supplied protein sequence and your knowledge of protein structure and molecular recognition.

Each question describes exactly one target protein. Treat the supplied sequence as one complete protein and make predictions only for that protein. No PDB entity identifiers, chain identifiers, complex composition, or sequences of other proteins are provided.

A protein may contain multiple distinct ligand-binding pockets. Predict all distinct pockets that you judge plausible and rank them from most to least likely. There is no fixed maximum number of pockets.

# Definition of a Binding Pocket

A binding pocket is a spatially coherent region of a protein that can accommodate and interact with a small-molecule ligand.

Each predicted pocket must be represented by the **complete set of protein residues expected to participate directly in ligand binding**.

Include all residues predicted to form the binding site, rather than only a few representative or highly conserved residues. Do not include unrelated residues merely to increase the size of a candidate.

Residues belonging to the same pocket do not need to be consecutive in the amino acid sequence, because spatially adjacent residues may be distant in sequence.

Each output object must represent one independent binding pocket. Multiple predicted pockets are distinct sites that may coexist on the same protein; they are not alternative answers for one site. Do not split a single pocket into multiple partial predictions or output duplicate or near-duplicate pockets.

# Input

The following information describes one target protein:

```text
sequence_length: 175
sequence: GMEEDIACVKDLVSKYLADNERLSRQKLAFLVQTEPRMLLMEGLKLLSLCIEIDSCNANGCEHNSEDKSVERILHDHGILTPSLCFVVPDGYKLTGNVLILLECFVRSSPANFEQKYIEDFKKLEQLKEDLKTVNISLIPLIDGRTSFYNEQIPDWVNDKLRDTLFSLLRYAQES
```

The sequence contains `175` amino acid residues.

# Output Requirements

1. Output all distinct binding pockets that you predict, ranked by predicted likelihood in descending order.
2. Represent each pocket as a complete set of amino acid sequence positions.
3. Use **1-based sequence indexing**: the first amino acid is position 1.
4. Every residue index must be an integer between 1 and `175`, inclusive.
5. Sort residue indices within each pocket in ascending order, without duplicates.
6. Every `residues` array must be nonempty.
7. Each pocket must represent a distinct, spatially coherent potential binding site that may coexist with the other predicted pockets.
8. The `pockets` array must be ordered from most to least likely.
9. The `rank` values must be consecutive JSON integers starting at 1 and must agree with the array order.
10. Return exactly one valid JSON object and nothing else.

# Required Output Format

```json
{
  "pockets": [
    {
      "rank": 1,
      "residues": [12, 15, 18, 45, 48, 92]
    },
    {
      "rank": 2,
      "residues": [120, 123, 126, 168, 172]
    }
  ]
}
```

The residue indices above are illustrative only. Predict the actual binding pockets based on the provided protein sequence.

# Strict Output Contract

- The top-level JSON object must contain exactly one key: `pockets`.
- `pockets` must be a JSON array.
- Every array element must be a JSON object containing exactly two keys: `rank` and `residues`.
- `rank` must be a JSON integer. Do not encode it as a string.
- `residues` must be a nonempty JSON array of unique JSON integers. Do not encode residue positions as strings.
- Do not include confidence scores, probabilities, names, descriptions, explanations, or any other fields.
- Do not wrap the JSON object in Markdown or a code fence.
- Do not output reasoning, comments, introductory text, or trailing text.
- Ensure that the response can be parsed directly by a standard JSON parser.
