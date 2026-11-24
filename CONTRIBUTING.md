# Contributing

This repository distributes benchmark **data**: task prompts, input payloads,
reference answers and the graders they were scored with. Two kinds of change are
welcome; one is not.

## Welcome

**A correction to a reference answer.** Include the `bench_id`, the value you
believe is right, and the source that establishes it — a measurement, a resolved
structure, a trial registration, or the scorer's own stated rule.

**A correction to a prompt that does not change the question.** Typographical
fixes and clarity edits are fine as long as the scientific ask and the required
output format are unchanged. For the 117 `open_rubric` tasks the conversation in
the prompt is part of the judge's input, so a rewording there can move the grade:
say so explicitly if your edit touches one.

## Not accepted

**Reformatting anything under `benchmark/tasks/*/inputs/`.** Their SHA-256 may be
part of the score for the antibody and patent families. A re-encoded CSV, a
converted line ending or a stripped trailing newline breaks grading even though
the content looks identical.

**Removing or rewriting `tests/score.py` to make an item easier.** The grader is
the definition of the task. If a scorer is wrong, the fix has to keep the
reference answer earning full marks.

## Checklist for a change

1. `benchmark/metadata/tasks.csv` still matches the tree — every directory listed,
   every row present, and `category` / `format` agreeing with the task header.
2. No file under an `inputs/` directory changed unless the change is the point of
   the pull request; if it did change, so must every SHA-256 pinned against it.
3. The task's reference answer still earns the scorer's maximum attainable score
   (some ranking tasks legitimately top out below 1.0 when the reference has
   ties).
4. Counts in `README.md` are updated if the inventory changed.

## Reporting a scoring problem

Include the `bench_id`, the submission verbatim (or a minimal reproducer), the
score you expected, the score you got, and the output of the task's own scorer.
Without a reproducer a scorer bug is hard to tell from a parse failure.
