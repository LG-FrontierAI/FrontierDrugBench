"""Summarize six related prediction tasks without counting them as six studies."""
from __future__ import annotations
import math

CASE_FAMILIES = {
    "NT_period1": ("AB15",),
    "dula_LG260818": ("AB16", "AB17", "AB18"),
    "NT_period2": ("AB19", "AB20"),
}


def summarize(scores):
    """Require every released prediction score; never drop failed items."""
    required = {item for group in CASE_FAMILIES.values() for item in group}
    if not isinstance(scores, dict) or set(scores) != required:
        raise ValueError("Exactly AB15–AB20 scores are required for a case-family summary")
    for value in scores.values():
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or not 0 <= value <= 1:
            raise ValueError("Each item score must be a finite number in [0, 1]")
    family_scores = {name: sum(scores[item] for item in items)/len(items)
        for name, items in CASE_FAMILIES.items()}
    return {"item_scores": dict(scores), "family_scores": family_scores,
        "family_balanced_mean": sum(family_scores.values())/len(family_scores),
        "AB20_minus_AB19": scores["AB20"]-scores["AB19"],
        "interpretation": "Descriptive averages over three shared experimental case families; not six independent studies, a confidence interval, or a calibrated biological success rate."}
