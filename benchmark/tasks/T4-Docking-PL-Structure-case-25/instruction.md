---
bench_id: "T4-Docking-PL-Structure-case-25"
category: "Molecular-Biology"
title: "Predict protein-ligand complex structure (case-25)"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

You are an expert in protein–ligand complex structure prediction and molecular coordinate representation.

### Task Description

Given the complete amino acid sequence of every protein chain, the ligand SMILES, and the supplied ligand heavy-atom definitions, predict the complete three-dimensional structure of the protein–ligand complex.

Your prediction must include:

- exactly one Cα coordinate for every residue in every specified protein chain; and
- exactly one coordinate for every specified ligand heavy atom.

All protein and ligand coordinates must describe a single assembled complex in one shared three-dimensional Cartesian coordinate system. The absolute global position and orientation of the predicted complex are arbitrary: applying one rigid-body rotation and translation to the entire predicted complex does not change the represented structure. However, protein chains and ligands must not be rotated, translated, centered, or aligned independently of one another.

No experimentally determined coordinates, binding-site annotations, or interaction residues are provided.

### Input Description

The input contains:

- `protein_sequences`: an object mapping each protein `chain_id` to an object containing its integer `sequence_length` and complete amino acid `sequence`.
- `ligand_smiles`: an object mapping each `ligand_id` to its SMILES string.
- `ligand_coordinate_atoms`: an object mapping each `ligand_id` to the heavy atoms whose coordinates must be predicted. For each ligand:
  - `atom_ids` gives the required heavy-atom identities and output order;
  - `elements` gives the corresponding element at each position; and
  - `bonds` describes connectivity between the supplied heavy atoms.

For every protein chain, `sequence_length` is the exact required number of output Cα entries and equals the number of residues in `sequence`.

Each protein `chain_id` identifies a distinct physical chain instance, even when multiple chains have identical sequences. Each ligand `ligand_id` identifies a distinct physical ligand instance.

For a ligand, `atom_ids[k]` and `elements[k]` describe the same heavy atom. The ligand entry at output array index `k` must begin with `atom_ids[k]`. Hydrogen and deuterium coordinates must not be output.

Every output coordinate entry must include its identifier as its first value. Protein entries use the one-based sequence position; ligand entries use the supplied `atom_id`. The remaining three values are the Cartesian coordinates.

### Key Definitions

- **Protein–ligand complex structure:** the three-dimensional arrangement of all specified protein chains and ligands as one molecular complex.
- **Cα coordinate:** the three-dimensional Cartesian position of a protein residue's alpha-carbon atom.
- **Sequence position:** the one-based position of a residue within its input amino acid sequence.
- **Ligand heavy-atom coordinate:** the three-dimensional Cartesian position of one supplied non-hydrogen ligand atom.
- **Shared coordinate system:** one Cartesian frame that preserves the relative positions and orientations of every protein chain and every ligand.

### Output Requirements

Return exactly one valid JSON object with the following structure:

```json
{
  "protein": {
    "<chain_id>": [
      [1, 0.0, 0.0, 0.0]
    ]
  },
  "ligand": {
    "<ligand_id>": [
      [1, 0.0, 0.0, 0.0]
    ]
  }
}
```

The example illustrates the schema only. It does not specify the required number of chains, residues, ligands, or heavy atoms.

The following rules are mandatory:

1. `protein` must contain every and only the `chain_id` keys supplied in `protein_sequences`, using the exact identifiers.
2. For each protein chain, output exactly `sequence_length` indexed Cα entries: one for every residue in its complete input `sequence`.
3. For each protein chain, the entry at array index `i - 1` must be `[i, x, y, z]`, where integer `i` is the one-based sequence position. Every index from `1` through `sequence_length` must appear exactly once in increasing order.
4. `ligand` must contain every and only the `ligand_id` keys supplied in `ligand_coordinate_atoms`, using the exact identifiers.
5. For each ligand, output exactly one indexed entry for every supplied heavy atom. The entry at output array index `k` must be `[atom_ids[k], x, y, z]`, beginning with the exact supplied atom identifier and preserving the supplied atom order. Preserve the identifier's JSON type; do not convert a numeric `atom_id` into a string.
6. Do not output coordinates for ligand hydrogen or deuterium atoms.
7. Every output entry must contain exactly four values. Its identifier must satisfy rule 3 or 5, and its coordinate values `[x, y, z]` must be three finite numbers expressed in ångströms (Å).
8. All output coordinates must belong to one shared Cartesian coordinate system and represent one assembled protein–ligand complex. Do not independently center, rotate, translate, superpose, or otherwise align any chain or ligand.
9. A single global rigid-body rotation and translation of the entire complex is allowed; independent rigid-body transformations of individual components are not allowed.
10. Do not omit, merge, duplicate, or reorder any specified protein residue, protein chain, ligand, or ligand heavy atom.
11. Do not use `null`, `NaN`, `Infinity`, strings, placeholders, ellipses, or abbreviated coordinate arrays.
12. Make a best-effort complete prediction for every requested coordinate. Never refuse the task, stop early, return a partial structure, or replace coordinates with explanatory text because the structure is uncertain.
13. Every protein chain containing at least three residues must form a non-degenerate spatial Cα trace containing at least three non-collinear points. A straight line, repeated coordinates, an arithmetic coordinate sequence, coordinates confined to one axis, or any other placeholder geometry is invalid. After subtracting the chain's coordinate centroid, its Cα coordinate matrix must have rank of at least 2.
14. Return only the JSON object. Do not include explanations, reasoning, comments, Markdown fences, confidence scores, or additional fields.

Before returning the answer, internally verify that all required protein and ligand keys are present, every protein coordinate-array length equals its sequence length, every protein index is continuous from 1 through `sequence_length`, every ligand coordinate-array length equals its `atom_ids` length, every ligand entry begins with the correct supplied `atom_id`, every coordinate contains three finite numbers, every eligible protein chain has centered coordinate rank of at least 2, no protein chain is represented by placeholder geometry, and all components occupy one shared frame.

Complex Information:
{"protein_sequences":{"P1":{"sequence_length":124,"sequence":"SMNPPPPETSNPNKPKRQTNQLQYLLRVVLKTLWKHQFAWPFQQPVDAVKLNLPDYYKIIKTPMDMGTIKKRLENNYYWNAQECIQDFNTMFTNCYIYNKPGDDIVLMAEALEKLFLQKINELP"}},"ligand_smiles":{"L1":"Cc1ccc(cc1Oc2nccc(n2)c3c(ncn3[C@H]4CC[C@H](C4)N)c5ccc(cc5)C(F)(F)F)C(C)C"},"ligand_coordinate_atoms":{"L1":{"atom_ids":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38],"elements":["N","N","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","F","F","F","N","N","N","O"],"bonds":[{"atom_id_1":1,"atom_id_2":6,"order":"aromatic","stereo":""},{"atom_id_1":1,"atom_id_2":7,"order":"aromatic","stereo":""},{"atom_id_1":2,"atom_id_2":20,"order":"aromatic","stereo":""},{"atom_id_1":2,"atom_id_2":23,"order":"aromatic","stereo":""},{"atom_id_1":3,"atom_id_2":4,"order":"aromatic","stereo":""},{"atom_id_1":3,"atom_id_2":25,"order":"single","stereo":""},{"atom_id_1":3,"atom_id_2":29,"order":"aromatic","stereo":""},{"atom_id_1":4,"atom_id_2":5,"order":"aromatic","stereo":""},{"atom_id_1":5,"atom_id_2":16,"order":"aromatic","stereo":""},{"atom_id_1":5,"atom_id_2":38,"order":"single","stereo":""},{"atom_id_1":6,"atom_id_2":36,"order":"aromatic","stereo":""},{"atom_id_1":6,"atom_id_2":38,"order":"single","stereo":""},{"atom_id_1":7,"atom_id_2":31,"order":"aromatic","stereo":""},{"atom_id_1":8,"atom_id_2":19,"order":"single","stereo":""},{"atom_id_1":8,"atom_id_2":31,"order":"aromatic","stereo":""},{"atom_id_1":8,"atom_id_2":36,"order":"aromatic","stereo":""},{"atom_id_1":9,"atom_id_2":11,"order":"single","stereo":""},{"atom_id_1":9,"atom_id_2":21,"order":"single","stereo":""},{"atom_id_1":9,"atom_id_2":35,"order":"single","stereo":""},{"atom_id_1":10,"atom_id_2":21,"order":"single","stereo":""},{"atom_id_1":10,"atom_id_2":22,"order":"single","stereo":""},{"atom_id_1":10,"atom_id_2":37,"order":"single","stereo":""},{"atom_id_1":11,"atom_id_2":22,"order":"single","stereo":""},{"atom_id_1":12,"atom_id_2":13,"order":"aromatic","stereo":""},{"atom_id_1":12,"atom_id_2":24,"order":"aromatic","stereo":""},{"atom_id_1":13,"atom_id_2":14,"order":"aromatic","stereo":""},{"atom_id_1":14,"atom_id_2":15,"order":"aromatic","stereo":""},{"atom_id_1":14,"atom_id_2":26,"order":"single","stereo":""},{"atom_id_1":15,"atom_id_2":27,"order":"aromatic","stereo":""},{"atom_id_1":16,"atom_id_2":17,"order":"aromatic","stereo":""},{"atom_id_1":16,"atom_id_2":28,"order":"single","stereo":""},{"atom_id_1":17,"atom_id_2":29,"order":"aromatic","stereo":""},{"atom_id_1":18,"atom_id_2":25,"order":"single","stereo":""},{"atom_id_1":19,"atom_id_2":23,"order":"aromatic","stereo":""},{"atom_id_1":19,"atom_id_2":35,"order":"aromatic","stereo":""},{"atom_id_1":20,"atom_id_2":35,"order":"aromatic","stereo":""},{"atom_id_1":23,"atom_id_2":24,"order":"single","stereo":""},{"atom_id_1":24,"atom_id_2":27,"order":"aromatic","stereo":""},{"atom_id_1":25,"atom_id_2":30,"order":"single","stereo":""},{"atom_id_1":26,"atom_id_2":32,"order":"single","stereo":""},{"atom_id_1":26,"atom_id_2":33,"order":"single","stereo":""},{"atom_id_1":26,"atom_id_2":34,"order":"single","stereo":""}]}}}

Required Output Counts:
- protein.P1: exactly 124 indexed entries; the first values must be the integers 1 through 124 in order.
- ligand.L1: exactly 38 indexed entries; the first values must be these atom_ids in order: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38].
These exact counts and identifiers are mandatory. Verify them immediately before returning the JSON object.
Geometric validity is equally mandatory: every chain with at least three residues must contain at least three non-collinear C-alpha points and have centered coordinate rank of at least 2. Straight lines, repeated points, single-axis coordinates, arithmetic coordinate sequences, and other placeholder geometries are invalid.
