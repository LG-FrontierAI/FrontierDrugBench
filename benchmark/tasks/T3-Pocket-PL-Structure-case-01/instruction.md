---
bench_id: "T3-Pocket-PL-Structure-case-01"
category: "Molecular-Biology"
title: "Predict binding-site residues from protein sequence and ligand SMILES (case-01)"
format: "structured_json"
input_mode: "inline_prompt"
---

# Prompt

You are an expert in structural biology, protein–ligand interactions, and computational binding-site prediction, specializing in identifying ligand-binding sites from protein amino acid sequences and ligand chemical structures.

You have expertise in protein sequence–structure relationships, protein folding, molecular recognition, and the physicochemical principles governing protein–ligand binding.

### Task Description

Your task is to predict the binding sites of a specified small-molecule ligand on a protein, using only the protein's amino acid sequence and the ligand's SMILES representation.

Infer the protein residues that are most likely to form a binding site for the given ligand, considering sequence-derived structural characteristics and the ligand's molecular properties.

A binding site (pocket) is defined as the complete set of protein residues that form the ligand-contacting region. Residues belonging to the same binding site may be distant in the primary sequence but spatially adjacent in the folded protein.

You must not assume that the protein has only one possible binding site for the specified ligand.

### Input Description

Each question provides the following information:

- **Protein sequence:** The complete amino acid sequence of the target protein, represented using standard one-letter amino acid codes.
- **Ligand SMILES:** The SMILES representation of the target small-molecule ligand, describing its chemical connectivity, functional groups, and any explicitly encoded stereochemistry and formal charges.

No experimentally determined protein structure, ligand coordinates, or binding-site annotations are provided.

You must infer potential ligand-binding sites from the supplied sequence and SMILES alone.

### Prediction Requirements

**Complete Residue Enumeration**

For each predicted binding site, enumerate the complete set of protein residues expected to participate in the binding region.

Completeness is essential:

- Include every residue predicted to belong to the binding site.
- Do not omit residues that belong to the predicted binding site.
- Do not include additional residues outside the predicted binding site.
- Do not substitute a short list of representative, conserved, catalytic, or key interaction residues for the complete binding-site residue set.

Both missing residues and extra residues are considered prediction errors.

**Multiple Candidate Binding Sites**

You may predict up to **20 distinct candidate binding sites** for the specified protein–ligand pair.

Requirements:

- Each candidate must represent one complete and independently plausible binding site.
- Candidate binding sites must be mutually exclusive at the residue level: no protein residue may appear in more than one candidate.
- Do not divide one binding site into multiple partial candidates.
- Do not combine spatially distinct binding sites into a single candidate.
- Do not generate redundant or nearly identical candidates.
- Rank all candidates in descending order of their predicted likelihood of binding the specified ligand.
- The most likely binding site must appear first.
- You may output fewer than 20 candidates when fewer plausible binding sites can be identified.
- Do not invent additional binding sites merely to reach the maximum number of candidates.

**Prediction Consistency**

All predicted residues must belong to the supplied protein sequence.

Each candidate must contain a nonempty set of unique residue positions.

Use the same residue-numbering convention for all candidates.

### Residue Representation

Represent each protein residue using its **1-based sequence position**.

- The first amino acid in the provided sequence has position 1.
- Residue positions must be positive integers not exceeding the length of the protein sequence.
- Residue positions must correspond directly to the supplied sequence, without applying any external numbering scheme.
- Do not use PDB residue numbering, chain identifiers, insertion codes, or atom identifiers.
- Within each binding site, list residue positions in strictly ascending numerical order.
- Do not repeat any residue position within or across binding sites.

For example, `[15, 18, 42, 46, 103]` represents five residues at the corresponding positions in the input sequence.

### Output Format

Return exactly one valid JSON object for each question.

The JSON object must contain a single key, `"pockets"`, whose value is an array of predicted binding sites.

Each binding site must be represented as an object containing:

- `"rank"`: An integer indicating the candidate's rank, starting from 1.
- `"residues"`: An array of integers containing the complete predicted binding-site residue set.

The `"pockets"` array must be ordered from the most likely to the least likely binding site.

Ranks must be consecutive integers starting from 1.

Return at most 20 candidates. If no plausible binding site can be identified, return an empty array.

**Required JSON structure:**

```json
{
  "pockets": [
    {
      "rank": 1,
      "residues": [15, 18, 42, 46, 103]
    },
    {
      "rank": 2,
      "residues": [67, 71, 109, 152]
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
- Do not include confidence scores, probabilities, pocket descriptions, or other metadata.
- Ensure that the JSON is syntactically valid and can be parsed directly by a standard JSON parser.

Input:

```text
sequence_length: 358
sequence: PSLRTQPSLYSGPFPFYRRPSELGCFSLDAQRQYHGDARALRYYSPPPINGPGPDFDLRDGYPDRYQPRDEEVQERLDHLLRWVLEHRNQLEGGPGWLAGATVTWRGHLTKLLTTPYERQEGWQLAASRFQGTLYLSEVETPAARAQRLARPPLLRELMYMGYKFEQYMCADKPGGSPDPSGEVNTNVAYCSVLRSRLGNHPLLFSGEVDCLNPQAPCTQPPSCYVELKTSKEMHSPGQWRSFYRHKLLKWWAQSFLPGVPHVVAGFRNPEGFVCSLKTFPTMEMFENVRNDREGWNPSVCMNFCAAFLSFAQSTVVQDDPRLVHLFSWEPGGPVTVSVHRDAPYAFLPSWYVETMTQ
ligand_smiles: CC(=O)N[C@@H]1[C@H]([C@@H]([C@H](O[C@@H]1O[P@@](=O)(O)O[P@@](=O)(O)OC[C@@H]2[C@H]([C@H]([C@@H](O2)N3C=CC(=O)NC3=O)O)O)CO)O)O
```
