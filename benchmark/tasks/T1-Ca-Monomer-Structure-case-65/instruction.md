---
bench_id: "T1-Ca-Monomer-Structure-case-65"
category: "Molecular-Biology"
title: "Predict monomeric protein Cα backbone coordinates from sequence (case-65)"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

You are an expert in protein three-dimensional structure prediction and protein backbone geometry.

## Task

Given a protein amino-acid sequence, predict the three-dimensional Cartesian coordinates of the Cα atom for every residue in the sequence.

The input sequence contains exactly `L` amino-acid residues. You must output exactly `L` Cα coordinates, one for each residue, in the same order as the input sequence.

Residue index `i` in the output must correspond exactly to residue `i` in the input sequence.

Do not omit any residue. Do not add any residue. Do not reorder residues.

## Input

The input contains:

* `sequence`: the complete deposited experimental construct sequence used for this target. It may represent a truncated or engineered portion of a naturally occurring protein.
* `sequence_length`: the number of residues in the sequence.

The sequence uses the standard one-letter amino-acid representation.

You must infer the protein's three-dimensional Cα trace from the sequence alone.

## Prediction policy

This is a best-effort structure-prediction benchmark. The coordinates are predictions and are not expected to reproduce an experimentally determined structure exactly.

Do not decline the task because specialized structure-prediction software is unavailable. Do not recommend external tools or discuss limitations. Use your learned structural priors to produce the best complete estimate you can from the sequence alone.

Uncertainty about the structure does not change the output requirements. Always return one coordinate for every residue. A complete approximate prediction is preferable to a refusal or an incomplete response.

## Coordinate definition

For each residue, predict the Cartesian coordinate of its Cα atom:

`[x, y, z]`

Coordinates must:

* be expressed in ångströms (Å);
* be finite real numbers;
* represent one coherent three-dimensional protein structure;
* contain exactly one coordinate triplet for every input residue.

The absolute origin and global orientation of the predicted structure are arbitrary. Only the relative three-dimensional geometry of the protein structure is important.

## Output requirements

Return JSON only.

The output must contain exactly one top-level key:

`"result"`

The value of `"result"` must be an array of exactly `sequence_length` objects.

Each object must have exactly the following fields:

* `"residue_index"`: 1-based position in the input sequence;
* `"residue_name"`: the one-letter amino-acid at that position;
* `"ca"`: an array containing exactly three finite floating-point numbers `[x, y, z]`.

The `result` array must be ordered strictly by increasing `residue_index`, starting from 1 and ending at `sequence_length`.

Example schema:

```json
{
  "result": [
    {
      "residue_index": 1,
      "residue_name": "M",
      "ca": [1.234, 2.345, 3.456]
    },
    {
      "residue_index": 2,
      "residue_name": "A",
      "ca": [2.111, 3.222, 4.333]
    }
  ]
}
```

The two-residue example only demonstrates the schema.
For the actual task, continue until all sequence_length residues have been included.

## Mandatory consistency rules

Before producing the final answer, internally verify all of the following:

1. The number of output objects equals `sequence_length`.
2. Every residue index from `1` to `sequence_length` appears exactly once.
3. No residue index is duplicated or missing.
4. `residue_name` exactly matches the amino acid at the corresponding position in the input sequence.
5. Every `"ca"` field contains exactly three numeric values.
6. No coordinate contains `null`, `NaN`, `Infinity`, strings, or missing values.
7. No explanatory text, comments, Markdown, or additional keys appear outside the required JSON object.

Input:

```text
sequence_length: 195
sequence: GPAGSMGYRNGNYAAFYVSEPFSESSLGANATKDFVSYNMLRAWKGKDNNYPFNDSHDKTYNVRDGSDWEKTLKPRLRKRLDQSKNIIFFLSKHTENSKALREEIDYGINVKGLPVIVVYPELSEKSDIIDCTTKVFRSEVVNLWSRVPVFKDSMLKVPTIHIPYKKDQIKKALENKDFMINSKISAGSVYFYPC
```
