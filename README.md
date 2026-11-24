# FrontierDrugBench

A benchmark of **971 expert-authored, zero-shot tasks** for evaluating language
models on real drug-discovery and development questions. Experimental scientists
and pharmaceutical experts in biology, medicinal chemistry and clinical research
wrote the questions, endpoints and scoring criteria, and every task is graded
against a reference grounded in measured functional data, resolved structures,
curated clinical annotations or an explicitly identified computational proxy.

Companion paper: *FrontierDrugBench: Can One Large Language Model Rival Specialists
across Drug Discovery and Development?* (LGLab Frontier AI Group).

- Homepage: <https://oribench.lglab.ac.cn/fdb>
- Version 1.0 (2026-11-24), English, CC BY 4.0

The full benchmark contains **1,196 tasks**: 1,154 across five biological domains
plus a separately reported 42-task Live Benchmark. This release publishes the
**971 external tasks** (81.2% of the inventory); the remaining 225 are internally
sourced and are not distributed, so scores computed here are not directly
comparable with the paper's 1,154-task results.

This repository ships **data only**: the task tree, the shared scorer library it
imports, and the per-task reference answers. No evaluation harness is included —
each task is self-contained, so it can be driven by any runner that sends one
prompt and reads one reply.

## What is in this repository

| Path | Contents |
| --- | --- |
| `benchmark/tasks/` | 971 task directories plus the shared scorer library `_packages/` |
| `benchmark/metadata/tasks.csv` | one row per task: `bench_id`, `category`, `format` |
| `benchmark/README.md` | task layout, `instruction.md` header, `answer.json` schema, rules that keep the tree scoreable |
| `CONTRIBUTING.md` | what counts as a valid correction, and what breaks grading |

Each task is one directory holding its prompt, the evidence it cites and the
grader it was evaluated with:

```
benchmark/tasks/<bench_id>/
├── instruction.md          prompt + classification front matter
├── inputs/                 data files (137 tasks)
└── tests/
    ├── score.py            the grader this task was scored with
    ├── answer.json         reference answer + scoring rule
    ├── rubric.txt          rendered rubric (open_rubric tasks only)
    └── reference/          per-case payloads (structure and design families)
```

Prompts are shipped already expanded: any data a task cites is inlined, so copying
the prompt body to a model sends the data rather than a path. `inputs/` holds the
same payload as separate files and is **not** a spare copy — for the antibody and
patent families the scorer verifies each file's SHA-256, so editing or deleting one
breaks grading. See [`benchmark/README.md`](benchmark/README.md) for the full
layout rules.

## Composition

By research domain (`category` in each task header):

| Domain | This release | Full benchmark |
| --- | ---: | ---: |
| Molecular Biology | 400 | 466 |
| Clinical Research | 200 | 250 |
| Disease Biology | 187 | 200 |
| Cell Biology | 71 | 118 |
| In-vivo Study | 71 | 120 |
| Live Benchmark | 42 | 42 |
| **Total** | **971** | **1,196** |

The Live Benchmark keeps its own label and is reported separately: it is a rolling
forecasting set, not a sixth biological domain, and it never enters the
five-domain aggregate.

By task family:

| Family | Prefix | Tasks |
| --- | --- | ---: |
| Clinical trial patient matching | `H1` | 100 |
| Clinical inquiry and information verification | `H3` | 100 |
| Protein Cα backbone from sequence | `T1` | 83 |
| Antibody–antigen epitope prediction and ranking | `T2` | 95 |
| Epitope residue prediction | `T3` | 86 |
| Antibody–antigen complex structure | `T4` | 80 |
| Antibody affinity, developability and design | `AB` | 98 |
| Variant function and protein property prediction | `PROT` | 50 |
| 5′UTR ribosome-loading prediction | `DNA` | 50 |
| Small-molecule ADMET and activity prediction | `SM` | 64 |
| Peptide pharmacokinetics | `Pep` | 31 |
| Phenotype and candidate activity prediction | `RV1` | 37 |
| Perturbation fitness/dependency phenotype | `D-` | 25 |
| Ionizable lipid design | `LNP` | 5 |
| Prospective forecasting (Live Benchmark) | `BX` | 42 |
| Perturbation phenotype | `development`/`wrn`/`metabolism`/`impc`/`sexual` | 19 |
| Other disease-biology items | `I` | 6 |

By expected response (`format`):

| Format | Tasks | Response |
| --- | ---: | --- |
| `structured_json` | 545 | a JSON object matching the schema in the prompt |
| `ranking` | 128 | one comma-separated ordering of the listed candidates |
| `open_rubric` | 117 | free-text clinical answer, graded against a rubric |
| `mcq` | 106 | one option letter |
| `forecast` | 42 | a point forecast (and interval where asked) |
| `design` | 20 | a set of designed sequences or molecules |
| `regression` | 13 | a single numeric prediction |

## Grading

Every task ships the grader it was evaluated with. `tests/score.py` returns a score
in `[0, 1]` for a submission; that number is the score, with no post-processing.
Most scorers are thin wrappers over the shared library in
`benchmark/tasks/_packages/frontier_benchkit/`, which each file loads by path, so a
task directory can be copied elsewhere and still score identically.

`tests/answer.json` holds the reference and, for 809 of the 971 tasks, names the
comparison under `scoring.type`. The other 162 implement the comparison directly in
their own `score.py`.

| `scoring.type` | Tasks | Comparison |
| --- | ---: | --- |
| `structure_case` | 344 | predicted coordinates or sequences vs. a frozen structural reference |
| *(absent: task-local `score.py`)* | 162 | whatever the task's own scorer implements |
| `label_exact` | 100 | exact match of a normalised label |
| `healthbench_rubric_judge` | 100 | an LLM judge weighs the answer against a criteria list |
| `option_letter` | 88 | one option letter |
| `ranking_concordant` | 63 | concordant-pair ratio against the reference ordering |
| `mixed` | 36 | a weighted combination declared in the key |
| `relative_wis` | 32 | weighted interval score relative to a reference forecast |
| `numeric_gaussian` | 20 | Gaussian log-score around the reference value |
| `binary_accuracy` | 10 | correct/incorrect call |
| `top_k_overlap` | 8 | overlap between the predicted and reference top-k sets |
| `option_set` | 8 | set equality of selected options |

Ranking tasks are scored by the **concordant-pair ratio**: the fraction of
candidate pairs ordered as the reference orders them, so a random ordering scores
0.50 by construction.

Two families need more than a text comparison:

- **117 `open_rubric` tasks** are graded by an LLM judge against a frozen rubric.
  The judge is an OpenAI-compatible endpoint configured through `LLM_BASE_URL`,
  `LLM_API_KEY` and `LLM_MODEL` (plus optional `LLM_MAX_TOKENS`, `LLM_TIMEOUT`,
  `LLM_TEMPERATURE`, `LLM_THINKING`, `LLM_REASONING_EFFORT`, retry knobs). These
  are the interface names the reference harness exports; renaming them breaks
  scoring.
- **20 `design` tasks** are graded by predicting each submitted sequence or
  molecule with a frozen protocol, which needs AlphaFold3 and a GPU.

Aggregation is the **five-domain macro-average**: each domain's mean over the tasks
scored in it, then the mean of the five, so a domain with 400 tasks does not
outweigh one with 71. Live Benchmark numbers are reported on their own line and
never pooled in. Recorded execution failures, refusals, parsing failures and
timeouts count as zero.

## Intended use

Measuring the zero-shot scientific judgement of general-purpose models on
drug-discovery and development questions, and tracking progress against specialist
systems on matched subsets. Specialist comparisons cover matched subsets only: the
reference is the best evaluated pipeline on that subset, not an exhaustive
comparison with the state of the art.

**Not** intended as a clinical decision tool. The tasks are research instruments
and several are deliberately narrow: one assay, one endpoint, one structure.

## Answer key and contamination

This repository ships `tests/answer.json`, `tests/reference/` payloads and
per-case reference answers, because the graders need them. **Treat it as
contaminated for training purposes.** If you publish derived data or a model
trained on this tree, check it against `CANARY.txt` first.

An evaluation-only mirror without the answer key is distributed as a gated
Hugging Face dataset; use that one when you only need to run the benchmark.

## Limitations

- Several tasks share one source study, structure, trial or assay, so they are
  not independent biological replicates and cannot be treated as a random sample
  of endpoints.
- The 0–100 display spans heterogeneous metrics. The five-domain mean is a
  descriptive composite of capability breadth, not calibrated accuracy on a common
  error scale.
- Twenty `design` tasks cannot be re-scored without AlphaFold3 inference, so the
  rest of the tree runs on CPU but those do not.
- 137 tasks ship `inputs/` whose SHA-256 may be part of the score, so those files
  must not be reformatted.
- The Live Benchmark is a rolling set; its composition changes over time, so its
  mean is not comparable across release dates.

## Contributing

Corrections to a reference answer need the source that establishes the right
value, and any change to `inputs/` is treated as a breaking change. See
[`CONTRIBUTING.md`](CONTRIBUTING.md).

`benchmark/metadata/tasks.csv` is the single index of the release: adding or
removing a task means updating the tree, the index and the counts above together.

## Citation

```bibtex
@misc{frontierdrugbench2026,
  title  = {FrontierDrugBench: Can One Large Language Model Rival Specialists
            across Drug Discovery and Development?},
  author = {{LGLab Frontier AI Group}},
  year   = {2026},
  url    = {https://oribench.lglab.ac.cn/fdb}
}
```

`CITATION.cff` carries the same metadata in machine-readable form.

## License

Task instructions, input data, verification scripts and rubrics are released under
[CC BY 4.0](LICENSE). Source documents referenced by individual tasks (patent
publications, journal articles) remain subject to their own terms.
