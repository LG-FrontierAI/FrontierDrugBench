---
bench_id: "T4-Docking-AbAg-Structure-case-23"
category: "Molecular-Biology"
title: "Predict antibody-antigen complex Cα structure (case-23)"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

You are an expert in antibody–antigen complex structure prediction and molecular coordinate representation.

### Task Description

Given the complete amino acid sequence of every antigen and antibody chain and the supplied antibody heavy–light pairing information, predict the complete Cα-trace structure of the antibody–antigen complex.

Your prediction must include exactly one Cα coordinate for every residue in every specified antigen and antibody chain.

All coordinates must describe a single assembled complex in one shared three-dimensional Cartesian coordinate system. The absolute global position and orientation of the predicted complex are arbitrary: applying one rigid-body rotation and translation to the entire predicted complex does not change the represented structure. However, antigen chains, antibody chains, and antibody binding units must not be rotated, translated, centered, superposed, or aligned independently of one another.

No experimentally determined coordinates, interface annotations, epitope residues, or paratope residues are provided.

### Input Description

The input contains:

- `antigen_sequences`: an object mapping each antigen `chain_id` to an object containing its integer `sequence_length` and complete amino acid `sequence`.
- `antibody_sequences`: an object mapping each antibody `chain_id` to an object containing its integer `sequence_length` and complete amino acid `sequence`. IDs beginning with `H` identify heavy or single-domain chains, and IDs beginning with `L` identify light chains.
- `antibody_pairs`: an object mapping each antibody `pair_id` to its member chains. Its `heavy` and `light` arrays contain the exact `chain_id` values belonging to that antibody binding unit. A binding unit may have no light chain when it represents a single-domain antibody or another heavy-only construct.

For every antigen and antibody chain, `sequence_length` is the exact required number of output Cα entries and equals the number of residues in `sequence`.

Each `chain_id` identifies a distinct physical chain instance, even when multiple chains have identical sequences. Each antibody chain listed in `antibody_pairs` refers to the sequence record with the same ID in `antibody_sequences`.

Every output coordinate entry must include the residue's one-based sequence position as its first value. The remaining three values are the Cartesian coordinates.

### Key Definitions

- **Antibody–antigen complex Cα trace:** the three-dimensional arrangement of the Cα atoms of all specified antigen and antibody chains as one assembled molecular complex.
- **Antigen chain:** a protein chain listed in `antigen_sequences`.
- **Antibody chain:** a heavy, light, or single-domain protein chain listed in `antibody_sequences`.
- **Antibody binding unit:** the heavy and light chains grouped under one `pair_id` in `antibody_pairs`.
- **Cα coordinate:** the three-dimensional Cartesian position of a protein residue's alpha-carbon atom.
- **Sequence position:** the one-based position of a residue within its complete input amino acid sequence.
- **Shared coordinate system:** one Cartesian frame that preserves the relative positions and orientations of every antigen chain, antibody chain, and antibody binding unit.

### Output Requirements

Return exactly one valid JSON object with the following structure:

```json
{
  "antigen": {
    "<chain_id>": [
      [1, 0.0, 0.0, 0.0]
    ]
  },
  "antibody": {
    "<chain_id>": [
      [1, 0.0, 0.0, 0.0]
    ]
  }
}
```

The example illustrates the schema only. It does not specify the required number of chains or residues.

The following rules are mandatory:

1. `antigen` must contain every and only the `chain_id` keys supplied in `antigen_sequences`, using the exact identifiers.
2. `antibody` must contain every and only the `chain_id` keys supplied in `antibody_sequences`, using the exact identifiers.
3. Do not move an antigen chain into `antibody` or an antibody chain into `antigen`.
4. For each chain, output exactly its supplied `sequence_length` indexed Cα entries: one for every residue in its complete input `sequence`.
5. For each chain, the entry at array index `i - 1` must be `[i, x, y, z]`, where integer `i` is the one-based sequence position. Every index from `1` through `sequence_length` must appear exactly once in increasing order.
6. Every output entry must contain exactly four values: its integer residue index followed by exactly three finite numerical coordinate values `[x, y, z]`, expressed in ångströms (Å).
7. All output coordinates must belong to one shared Cartesian coordinate system and represent one assembled antibody–antigen complex. Do not independently center, rotate, translate, superpose, or otherwise align any antigen chain, antibody chain, or antibody binding unit.
8. A single global rigid-body rotation and translation of the entire complex is allowed; independent rigid-body transformations of individual components are not allowed.
9. Preserve every antibody binding unit specified by `antibody_pairs` when arranging its heavy and light chains in the shared complex.
10. Do not omit, merge, duplicate, or reorder any specified residue or chain, including distinct physical chains with identical amino acid sequences.
11. Do not output side-chain atoms, backbone atoms other than Cα, `null`, `NaN`, `Infinity`, strings, placeholders, ellipses, or abbreviated coordinate arrays.
12. Make a best-effort complete prediction for every requested coordinate. Never refuse the task, stop early, return a partial structure, omit a long chain, or replace coordinates with explanatory text because the structure is uncertain.
13. Every antigen or antibody chain containing at least three residues must form a non-degenerate spatial Cα trace containing at least three non-collinear points. A straight line, repeated coordinates, an arithmetic coordinate sequence, coordinates confined to one axis, or any other placeholder geometry is invalid. After subtracting the chain's coordinate centroid, its Cα coordinate matrix must have rank of at least 2.
14. Return only the JSON object. Do not include explanations, reasoning, comments, Markdown fences, confidence scores, or additional fields.

Before returning the answer, internally verify that all required antigen and antibody keys are present, no extra keys are present, every coordinate-array length equals its corresponding sequence length, every residue index is continuous from 1 through `sequence_length`, every coordinate contains three finite numbers, every eligible chain has centered coordinate rank of at least 2, no chain is represented by placeholder geometry, all antibody pair memberships are respected, and all chains occupy one shared frame.

Complex Information:
{"antigen_sequences":{"AG1":{"sequence_length":275,"sequence":"SHSMRYFSAAVSRPGRGEPRFIAMGYVDDTQFVRFDSDSASPRMEPRAPWVEQEGPEYWEEETRNTKAHAQTDRMNLQTLRGYYNQSEASSHTLQWMIGCDLGSDGRLLRGYEQYAYDGKDYLALNEDLRSWTAADTAAQISKRKCEAANVAEQRRAYLEGTCVEWLHRYLENGKEMLQRADPPKTHVTHHPVFDYEATLRCWALGFYPAEIILTWQRDGEDQTQDVELVETRPAGDGTFQKWAAVVVPSGEEQRYTCHVQHEGLPEPLMLRWKQ"},"AG2":{"sequence_length":99,"sequence":"IQRTPKIQVYSRHPAENGKSNFLNCYVSGFHPSDIEVDLLKNGERIEKVEHSDLSFSKDWSFYLLYYTEFTPTEKDEYACRVNHVTLSQPKIVKWDRDM"},"AG3":{"sequence_length":8,"sequence":"IIPRHLQL"}},"antibody_sequences":{"H1":{"sequence_length":212,"sequence":"QSVEESGGRLVTPGTPLTLTCTVSGIDLSSNAMSWVRQAPGEGLEWIGTISSGGRTYYASWAKGRFTISKTSTTVDLKIPSPTTEDTATYFCGRGDGATGFNIWGPGTLVTVSSGQPKAPSVFPLAPCCGDTPSSTVTLGCLVKGYLPEPVTVTWNSGTLTNGVRTFPSVRQSSGLYSLSSVVSVTSSSQPVTCNVAHPATNTKVDKTVAPS"},"L1":{"sequence_length":213,"sequence":"ALVMTQTPASVSEPVGGTVTIKCQASQSIYSYLSWYQQKPGQPPKLLIYKASTLASGVSSRFKGSGSGTQFTLTISDLECGDAATYYCQNHWNVGGNGWPFGGGTEVVVKRTPVAPTVLIFPPAADQVATGTVTIVCVANKYYPDVTVTWEVDGTTQTTGIENSKTPQNSADCTYNLSSTLTLTSTQYNSHKEYTCKVTQGTTSVVQSFNRGD"}},"antibody_pairs":{"PAIR1":{"heavy":["H1"],"light":["L1"]}}}

Required Output Counts:
- antigen.AG1: exactly 275 indexed entries; the first values must be the integers 1 through 275 in order.
- antigen.AG2: exactly 99 indexed entries; the first values must be the integers 1 through 99 in order.
- antigen.AG3: exactly 8 indexed entries; the first values must be the integers 1 through 8 in order.
- antibody.H1: exactly 212 indexed entries; the first values must be the integers 1 through 212 in order.
- antibody.L1: exactly 213 indexed entries; the first values must be the integers 1 through 213 in order.
These exact counts and identifiers are mandatory. Verify them immediately before returning the JSON object.
Geometric validity is equally mandatory: every chain with at least three residues must contain at least three non-collinear C-alpha points and have centered coordinate rank of at least 2. Straight lines, repeated points, single-axis coordinates, arithmetic coordinate sequences, and other placeholder geometries are invalid.
