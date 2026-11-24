# benchmark/

```text
benchmark/
├── metadata/
│   └── tasks.csv           one row per task: bench_id, category, format
└── tasks/
    ├── _packages/          shared scorer library (frontier_benchkit)
    ├── <bench_id>/         one directory per task
    │   ├── instruction.md  prompt + classification front matter
    │   ├── inputs/         data files (137 tasks); may be hash-pinned
    │   └── tests/
    │       ├── score.py    authoritative grader
    │       ├── answer.json reference answer + scoring rule
    │       ├── rubric.txt  rendered rubric (117 open_rubric tasks)
    │       ├── reference/  per-case payloads (structure and design families)
    │       └── cases/      per-case answers (multi-case families)
    └── ...
```

Domain and format counts are in [`../README.md#composition`](../README.md#composition).

## Rules that keep the tree scoreable

1. **`_packages/` stays where it is.** Every `tests/score.py` resolves the shared
   library as `Path(__file__).parents[1] / "_packages"`. Moving it, or adding a
   level of nesting, disables all scoring.

2. **`tests/` is the contract.** A model never sees it. `score.py` is the
   authoritative grader; `answer.json` holds the reference and, for 809 tasks, the
   name of the comparison under `scoring.type`.

3. **`inputs/` is byte-exact.** For the antibody and patent families the scorer
   verifies each input file's SHA-256 against `tests/evaluation_spec.json`.
   Reformatting a CSV — even a trailing newline — breaks scoring.

4. **The prompt is the body after `# Prompt`.** The YAML header is classification
   metadata and is not part of the question.

5. **Directory name = `bench_id`, with `::` written as `__`.** Nineteen tasks carry
   a namespaced id (`wrn::BIN-05` → `wrn__BIN-05`); `:` is not portable in a path,
   so the directory uses `__`. The `bench_id` inside the file is authoritative.

6. **The index matches the tree.** `tasks.csv` lists every task with its
   `bench_id`, `category` and `format`; a mismatch between the two is a broken
   release.

## `instruction.md`

```yaml
---
bench_id: "H3-ClinicalInquiry-031"
category: "Clinical-Research"
title: "Clinical information verification and uncertainty expression (hedging)"
format: "open_rubric"
---

# Prompt

...
```

`category` is the research domain and the key the harness groups by; `format` is
the expected response shape. Some headers carry extra fields (`input_mode`,
`pass_threshold`, `sequence_length`, trial-eligibility keys); they are informative
or scorer-specific and never change the prompt.

## `tests/answer.json`

```json
{
  "bench_id": "wrn::BIN-05",
  "answer": "B",
  "scoring": { "type": "label_exact", "options": ["A", "B", "C", "D"] },
  "grading": { "method": "task_scorer", "scoring": "single_case" }
}
```

| Field | Meaning |
| --- | --- |
| `answer` | the reference. Its shape follows the task's own contract: a string, a number, an ordered list, or a dict |
| `scoring.type` | how the scorer compares a submission to the reference (**absent in 162 tasks**, which implement the comparison directly in `score.py`) |
| `grading.method` | `task_scorer` when the task's own `score.py` owns the rule |
| `reference` | optional: gold payload location, and `example_model_answer`, an authored submission that states the output contract |

`answer.json` is a reference, not a submission template. For tasks that ship
`reference.example_model_answer`, that example is the safer shape to imitate.

## Which files a scorer reads

A scorer reads only `tests/` (and `inputs/` when the prompt cites files). It never
needs `instruction.md` — except the rubric tasks, which prepend the conversation
body to the answer before asking the judge. That is why editing a prompt changes
grading for `open_rubric` tasks and only changes the question for the rest.

## Multi-case tasks

Some families split one study into several cases (`AB01-A-..._case_01`,
`T1-Ca-Monomer-Structure-case-02`). Each case is a separate task directory with its
own `bench_id`, prompt and reference, so it is scored and aggregated independently.
Nothing is shared between sibling cases at run time.
