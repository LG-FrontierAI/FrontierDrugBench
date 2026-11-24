---
bench_id: "T3-Pocket-AbAg-Structure-case-03"
category: "Molecular-Biology"
title: "Predict epitope residues from antibody-antigen sequence (case-03)"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

You have expertise in protein sequence–structure relationships, antibody molecular recognition, antigen–antibody interface formation, and the physicochemical principles governing antibody–antigen binding.

### Task Description

Your task is to predict the binding sites (epitopes) of a specified antibody on a specified antigen, using only their amino acid sequences.

Infer the antigen residues most likely to form the binding interface with the given antibody, considering sequence-derived structural characteristics and the molecular recognition properties of both binding partners.

An epitope is defined as the complete set of antigen residues expected to contain at least one heavy atom within 5.0 Å of any heavy atom of the bound antibody in the antibody–antigen complex.

Residues belonging to the same epitope may be distant in the primary sequence or may belong to different antigen entities, but are spatially adjacent in the bound complex.

You must predict **only the binding residues on the antigen**. Do not predict or output antibody binding residues (paratopes).

Do not assume that a given antibody–antigen pair has only one possible binding interface.

### Input Description

The input is one JSON object containing two arrays:

- `antigen_entities`: One or more antigen sequence entities.
- `antibody_entities`: One or more antibody sequence entities. Together, these entities represent the specified antibody and its component chains.

Every entity object contains exactly these fields:

- `entity_id`: The entity identifier, represented as a JSON string.
- `sequence_length`: The number of residues in the entity sequence.
- `copy_count`: The number of equivalent structural chain copies represented by the entity.
- `sequence`: The complete amino acid sequence in standard one-letter notation.

Treat each `entity_id` as an opaque string. Do not convert it to a number, renumber it, or infer biological meaning from its appearance. Distinct entity IDs must remain distinct even if their sequences are identical.

The antigen and antibody may each contain multiple sequence entities. One entity may represent multiple equivalent structural chain copies. Predictions must refer to sequence entities, not individual structural chain copies.

No experimentally determined three-dimensional structures, atomic coordinates, or binding-site annotations are provided.

You must infer potential antigen epitopes from the supplied antigen and antibody sequences alone.

### Prediction Requirements

**Complete Residue Enumeration**

For each predicted epitope, enumerate the complete set of antigen residues expected to form the binding interface with the specified antibody.

Each candidate must represent the sequence-level union of contacts in one hypothesized bound biological assembly. For an antigen entity with multiple equivalent structural copies, include a sequence position if that position is expected to contact any supplied antibody component in at least one copy. Do not output separate candidates merely for equivalent structural copies.

Completeness is essential:

- Include every antigen residue predicted to belong to the epitope.
- Do not omit residues that belong to the predicted epitope.
- Do not include additional antigen residues outside the predicted epitope.
- Do not substitute a short list of representative, conserved, or key interaction residues for the complete epitope residue set.
- Do not include antibody residues in the output.

Both missing residues and extra residues are considered prediction errors.

**Multiple Candidate Epitopes**

You may predict up to **20 distinct candidate epitopes** for the specified antibody–antigen pair.

Requirements:

- Each candidate must represent one complete and independently plausible antibody-binding interface on the antigen.
- A single candidate epitope may contain residues from multiple antigen sequences.
- Do not divide one epitope into multiple partial candidates.
- Do not merge unrelated alternative binding hypotheses into a single candidate. Within one candidate, however, include the complete union of contacts expected from all supplied antibody components and equivalent structural copies in that hypothesized assembly.
- Do not generate redundant or nearly identical candidates.
- Different candidates may share some `(entity_id, position)` pairs only when the independently plausible binding hypotheses genuinely overlap.
- Rank all candidates in descending order of their predicted likelihood of binding the specified antibody.
- The most likely epitope must appear first.
- You may output fewer than 20 candidates when fewer plausible epitopes can be identified.
- Do not invent additional epitopes merely to reach the maximum number of candidates.

**Prediction Consistency**

All predicted residues must belong to the supplied antigen sequences.

Each candidate must contain at least one predicted antigen residue across all of its entity arrays.

Use the same residue-numbering convention for all candidates.

Do not include any `entity_id` that is not defined in the antigen input.

### Residue Representation

Represent each antigen residue using its **entity identifier and 1-based position**.

- Each antigen entity has a unique `entity_id`, as specified in the input.
- The first amino acid in each antigen sequence has position 1.
- Residue positions must be integers between 1 and the length of their corresponding antigen sequence, inclusive.
- Residue positions must correspond directly to the supplied sequence, without applying any external numbering scheme.
- Use the exact antigen `entity_id` values provided in the input.
- JSON object keys representing entity IDs must be quoted strings.
- Include every supplied antigen `entity_id` exactly once in every candidate's `entities` object.
- Use an empty array for an antigen entity that has no predicted binding residues in that candidate.
- Never include an antibody `entity_id` in the output.
- Do not use PDB residue numbering, structural chain identifiers, insertion codes, or atom identifiers.
- If multiple structural chains share the same antigen sequence and are represented by one `entity_id`, equivalent residue positions are represented by the same `(entity_id, position)` pair.
- Within each antigen sequence, list residue positions in strictly ascending numerical order.
- Do not repeat any `(entity_id, position)` pair within a candidate epitope.
- If an epitope spans multiple antigen sequences, group its residues by `entity_id`.

For example, if an antigen contains entity_id `1` and `3`, an epitope may include residues `[15, 18, 42]` from `1` and `[21, 25]` from `3`.

### Output Format

Return exactly one valid JSON object for each question.

The JSON object must contain a single key, `"epitopes"`, whose value is an array of predicted antigen-binding sites.

Each epitope must be represented as an object containing:

- `"rank"`: An integer indicating the candidate's rank, starting from 1.
- `"entities"`: An object containing every supplied antigen `entity_id` as a key and an array of integer residue positions as its value. Use `[]` when that entity has no predicted residues in the candidate.

The `"epitopes"` array must be ordered from the most likely to the least likely binding site.

Ranks must be consecutive integers starting from 1.

Return at most 20 candidates. If no plausible epitope can be identified, return an empty array.

**Required JSON structure:**

```json
{
  "epitopes": [
    {
      "rank": 1,
      "entities": {
        "1": [15, 18, 42],
        "3": [21, 25]
      }
    },
    {
      "rank": 2,
      "entities": {
        "1": [67, 71, 109],
        "3": []
      }
    }
  ]
}
```

The example above illustrates the required format only; its residue positions are not a prediction.

**Strict Output Constraints:**

- Output valid JSON only.
- Do not include Markdown formatting or code fences.
- Do not include explanations, reasoning, comments, or additional text.
- Do not include any keys other than those explicitly specified.
- Do not include confidence scores, probabilities, epitope descriptions, or other metadata.
- Ensure that the JSON is syntactically valid and can be parsed directly by a standard JSON parser.

Before returning the answer, internally verify that every candidate contains exactly the supplied antigen entity IDs, contains no antibody entity IDs, uses only in-range integer positions, and contains at least one predicted residue in total.

Input:

```json
{
  "antigen_entities": [{"entity_id":"1","sequence_length":394,"copy_count":1,"sequence":"SSGNKIHFINVQEGGSDAIILESNGHFAMVDTGEDYDFPDGSDSRYPWREGIETSYKHVLTDRVFRRLKELGVQKLDFILVTHTHSDHIGNVDELLSTYPVDRVYLKKYSDNRITNSERLWDNLYGYDKVLQTASEKGVSVIQNITQGDAHFQFGDMDIQLYNYENETDSSGELKKIWDDNSNSLISVVKVNGKKIYLGGDLDNVHGAEDKYGPLIGKVDLMKFNHHHDTNKSNTKDFIKNLSPSLIVQTSDSLPWKNGVDSEYVNWLKERGIERINAASKDYDATVFDIRQDGLVNISTSYKPIPSFQAGWHKSSYGNWWYQAPDSTGEYAVGWNEIKGEWYYFNQTGILLQNQWKKWNNRWFYLTDSGVAAKNWKKIAGIWYYFNKENQMEI"}],
  "antibody_entities": [{"entity_id":"2","sequence_length":125,"copy_count":1,"sequence":"QVQLQESGPRLVKVSETLSLTCSLSGHSISSGHHWAWIRQSPGRGLEWIATVDHNGRTYYNPSLRGRVILSKDTTKNSFSVQLTSVTAADTAVYYCARREAPSPGTGWYPPFGQWGQGALVTVST"},{"entity_id":"3","sequence_length":111,"copy_count":1,"sequence":"QSVLTQPPSLSGAPGQTVTISCTGSSSNIGAGYDVHWYRQLPGTAPTLLISVFDNRPLGVPGRISGSKSGTSASLAITGLQAEDEADYYCQSHDNMLSGSVFGGGTKLTVL"}]
}
```
