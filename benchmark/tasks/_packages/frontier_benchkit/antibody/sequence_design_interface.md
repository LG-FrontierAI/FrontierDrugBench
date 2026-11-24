# Organizer-only sequence design evaluation interface

AB04 requires CSV `name,sequence1` (VHH). AB05 requires CSV
`name,sequence1,sequence2` (VH and VL only, Fv rather than full Fab). Each case
requires exactly ten distinct complete designs with standard amino acids, the
supplied lengths and every non-X residue unchanged. Invalid submissions receive
a protocol score of zero; sequence validity is not a binding measurement.

## Approved AlphaFold 3 protocol

The active evaluator type is `alphafold3_ranking`. Chain A is one copy of the
exact supplied antigen ECD; B is the VHH (AB04) or VH (AB05); C is VL (AB05).
Do not add constant regions, Fc, linkers, a second antigen copy or other chains.
Each candidate uses seed 20261023 and five samples with indices 0 through 4.
Select the maximum raw AF3 `ranking_score`, then clip that candidate score to
[0,1]. Average every one of the ten candidate scores, then average all ten cases
with equal weight. Keep raw sample values and the raw selected-score mean in the
organizer report. No metric gates contribute to the active score. This is a
computational confidence proxy, not affinity or experimental success probability.

The selected protocol is recorded even when `external_config.frozen` is false.
The current template deliberately contains no invented tool versions, model
hashes or database hashes. Freeze immutable `tool_versions` (including
`alphafold3`), `model_parameters_sha256`, `database_snapshot_sha256`, a
`sha256:...` container digest, MSA/template policies and `max_template_date`
before scoring model submissions. `calibration_basis` and `metric_gates` belong
only to the legacy evaluator; they are not required by the AF3 branch. Pass
thresholds are set in the central item policy, separately from candidate scores.

## Binding results to inputs

The frozen configuration is embedded in each case answer. Its
`target_sequence_sha256` must match the exact `target_sequence` in the case gold
and input. All hash values use SHA256; `canonical_hash` hashes canonical UTF-8
JSON, whereas target hashes use the raw ASCII amino-acid sequence.

`evaluate_case(prediction, gold_path, external_results=...)` and the existing
per-question `evaluate` entrypoint retain their signatures. A completed external
result must contain `status`, `config_sha256`, `submission_sha256`,
`target_sequence_sha256`, matching `tool_versions` and `candidates`. The candidate
mapping must contain exactly all ten submitted IDs. Each value has:

```json
{
  "status": "completed",
  "complex_sha256": "hash returned by af3_complex_sha256(row, gold)",
  "samples": [
    {"seed": 20261023, "sample_index": 0, "status": "completed", "ranking_score": 0.75}
  ]
}
```

The illustrative array above must contain all five distinct sample indices in
real results. `af3_complex_sha256(row, gold)` binds chain IDs, roles, order and
exact sequences. `submission_sha256=canonical_hash(rows)` also binds the ordered
ten candidate rows and names. Optional `resource_usage` is reported separately.
Missing samples, nonfinite values, inconsistent hashes, wrong versions or missing
candidate results are organizer errors, never contestant zeroes. Top-level,
candidate or sample infrastructure/inference failures make the entire case
unavailable; no failed candidate or sample is discarded before averaging.
Unfrozen evaluators and missing results return `score: null`; an item containing
any pending case remains pending. Do not selectively rerun poor-scoring designs.

## Legacy compatibility

Historical configurations with no evaluator_type, or `evaluator_type: metric_gates`,
retain the old all-gates-pass fraction and its four required metric categories.
They must not be applied to active AF3 questions or silently mixed with the new
score. Historical answers are kept in the pre-split archive.
