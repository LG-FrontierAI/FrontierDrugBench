# Scoring contract

The current release has 30 tasks. Use `benchmark_eval.py` as the common entry point and `benchmark_config.py` as the authoritative task, category and threshold registry. See the [slim-package instructions](../README.md). Retired parent IDs are not scored as additional tasks; their archives remain in the organizer’s full project.

Sequence tasks use `sequence_case_eval.py` through the common entry point. Ranking uses max(0, Spearman rho); AB02-B uses only its frozen resolvable comparison pairs, and AB11 uses max(0, MCC). The exact target set is required; invalid submissions receive zero for the whole case. Every required case remains in the equal-weight item denominator, including missing submissions. Synthetic and experimental data are reported separately. Case evaluation is bound to the input hash.

AB04/AB05 require ten complete unique sequence candidates per case and use the `alphafold3_ranking` evaluator. AB04 predicts antigen plus VHH; AB05 predicts antigen plus VH plus VL (Fv). Select the highest raw ranking_score among five samples with seed 20261023, clip each selected candidate score to [0,1], average ten candidates, then average all ten cases. Formal score and pass status remain null until the runtime is frozen and complete results are available. Preserve protocol-zero diagnostics for invalid submissions. See the [AF3 interface](sequence_design_interface.md). The score is a structure-prediction proxy.

AB14-A/B use separate report-specific rubrics normalized to [0,1]. In-vivo ranking tasks use positive-truncated Spearman; AB18 uses exp(-mean(abs(log(prediction)-log(gold)))). The two independent locked follow-ups are AB19-A to AB20-A (0.5–2 h) and AB19-B to AB20-B (2–6 h).

All tasks retain continuous scores and add `pass_threshold`, `passed` and `threshold_version`. Compare the unrounded whole-item score against its threshold after complete-case aggregation. Pending evaluation has score and passed both null. Summaries report all 30 tasks, categories and equal-weight original-20-family results.

## Patent expansion AB21–AB80 (90-task release, 2026-10-26)

> **Correction to the two paragraphs above.** "The current release has 30 tasks"
> and "Summaries report all 30 tasks" describe `benchmark_eval.py` /
> `benchmark_config.py`, which still cover exactly the frozen thirty and were
> not edited. The directory tree in this package now holds **230 task
> directories**, and the harness scores each one independently; use the harness'
> reports, not the organizer's 30-task summary, for the expansion.

The first 170 directories are the frozen thirty items expanded per case
(`AB01-A` … `AB20-B`) and are unchanged; the last 60 are `AB21` … `AB80`, one
directory each (`<item>-<Category>_case_01`). A suite run that keeps
`run.case_groups` as shipped executes 120 of them (see the batch configs): the
110 `AB06`–`AB13` non-experimental cases stay out of that run.

`patent_case_eval.py` scores the expansion through `tests/score.py`; it needs
only `sequence_case_eval.py`, which is byte-identical to the 30-task release, so
`benchmark_eval.py` / `benchmark_config.py` still describe exactly the frozen
thirty and were not edited.

Task types and the harness formats (one case per item, `input_mode:
single_case_csv`):

| snapshot `task_type` | count | the harness `format` | score |
|---|---|---|---|
| `ranking` | 26 | `ranking` | `max(0, Spearman rho)`, or `max(0, (correct − wrong) / frozen pairs)` when `ranking_metric` is `resolvable_pair_concordance` (AB32/AB33/AB65) |
| `binary` | 6 | `structured_json` | `max(0, MCC)` over integer labels 0/1 |
| `numeric` | 13 | `regression` | `exp(−mean(abs(log(prediction/truth))))`, predictions must be finite and > 0 |
| `review` | 15 | `open_rubric` | points/100 from a bound evidence judgment (see below) |

Every case is gated by `patent_case_eval.evaluate_question`, which re-verifies
`input_sha256`, `answer_sha256` and `study_information_sha256` against
`tests/evaluation_spec.json`, requires `data_status: patent_experimental` and
`admission_status: admitted`, and rejects any submission that does not name
exactly the frozen target set (invalid ⇒ `0.0` with a diagnostic, never a crash).

### Ranking cases with tied gold

Six ranking cases (AB22, AB37, AB38, AB39, AB49, AB63) have duplicate measured
values in the frozen truth. Spearman is computed against the average ranks of
those values, so no submission can reach 1.0; the ceiling is 0.9309–0.9970 and
`tests/answer.json` records it under `reference.selfcheck.skip`, which is why
`harness validate --score-check` reports those six as *skipped* rather than
*mismatch*. Their pass thresholds (0.6) are unaffected. The other 20 ranking
cases, all 6 binary and all 13 numeric cases score exactly 1.0 on the gold.

### Review cases

`review` cases are judged, not compared: `tests/score.py` asks the configured
judge (`LLM_BASE_URL` / `LLM_API_KEY` / `LLM_MODEL`, exported from the `judge:`
block) for a judgment bound to `response_sha256` and `rubric_sha256`, with one
decision per rubric criterion and an exact quotation for every awarded point.
`patent_case_eval.review` validates that binding and rejects fabricated quotes,
a wrong rubric hash, missing or extra criteria, and non-boolean `met` values.
Awarded points sum to 100. A case without a judgment returns
`status: pending_adjudication` (score `None`, reported as 0.0 by the harness) rather
than a number, so an unjudged review is never silently averaged in as a zero
without a trace.

Organizer-side assets kept beside each review case: `tests/rubric.txt` (rendered
for the harness' `Criterion N: / Points:` parser), `tests/review_examples.json`
(the snapshot's `review_validation_examples` / `rubric_contrast_checks`
calibration material), `tests/cases/case_01.answer.json` (frozen gold) and
`tests/cases/case_01.reference.txt` (the organizer's frozen reference answer,
also inlined as `answer.json`'s `answer`).

### Provenance assets in every expansion directory

`tests/random_baseline.json` (exact/permutation random-score calibration and the
threshold grid from the snapshot), `tests/organizer_note.md` (the snapshot's
`usage_notes.md`: category, case count, pass threshold, shared-study disclosure) and
`tests/cases/case_01.reference.txt` (the frozen reference submission in the shape
the case expects). None of them is read at scoring time.
