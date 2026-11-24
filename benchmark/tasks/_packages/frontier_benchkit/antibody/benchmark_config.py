"""Frozen task registry for the 30-task release (threshold version v1)."""
from __future__ import annotations

CATEGORY_LABELS = {
    "Molecular Biology": "Molecular Biology",
    "Cell Biology": "Cell Biology",
    "In Vivo Studies": "In Vivo Studies",
}

TASKS = {
    "AB01-A": ("AB01", "Molecular Biology", .60),
    "AB01-B": ("AB01", "Molecular Biology", .60),
    "AB02-A": ("AB02", "Molecular Biology", .60),
    "AB02-B": ("AB02", "Cell Biology", 1.00),
    "AB03-A": ("AB03", "Cell Biology", .60),
    "AB03-B": ("AB03", "Cell Biology", .60),
    "AB04": ("AB04", "Molecular Biology", .70),
    "AB05": ("AB05", "Molecular Biology", .60),
    "AB06": ("AB06", "Molecular Biology", .60),
    "AB07-A": ("AB07", "Molecular Biology", .60),
    "AB07-B": ("AB07", "Molecular Biology", .60),
    "AB08": ("AB08", "Molecular Biology", .60),
    "AB09": ("AB09", "Molecular Biology", .60),
    "AB10-A": ("AB10", "Molecular Biology", .60),
    "AB10-B": ("AB10", "Molecular Biology", .60),
    "AB11": ("AB11", "Molecular Biology", .60),
    "AB12-A": ("AB12", "Molecular Biology", .60),
    "AB12-B": ("AB12", "Molecular Biology", .60),
    "AB13": ("AB13", "Molecular Biology", .60),
    "AB14-A": ("AB14", "Cell Biology", .80),
    "AB14-B": ("AB14", "Cell Biology", .80),
    "AB15": ("AB15", "In Vivo Studies", .60),
    "AB16-A": ("AB16", "In Vivo Studies", .80),
    "AB16-B": ("AB16", "In Vivo Studies", .80),
    "AB17": ("AB17", "In Vivo Studies", .80),
    "AB18": ("AB18", "In Vivo Studies", .70),
    "AB19-A": ("AB19", "In Vivo Studies", .70),
    "AB19-B": ("AB19", "In Vivo Studies", .70),
    "AB20-A": ("AB20", "In Vivo Studies", .70),
    "AB20-B": ("AB20", "In Vivo Studies", .70),
}
THRESHOLD_VERSION = "v1-20261023"
FOLLOW_UPS = {"AB20-A": "AB19-A", "AB20-B": "AB19-B"}


def task_metadata(item):
    family, category, threshold = TASKS[item]
    return {"item_id": item, "parent_item_id": family, "category": category,
            "category_label": CATEGORY_LABELS[category], "pass_threshold": threshold,
            "threshold_version": THRESHOLD_VERSION,
            "pass_rule": "unrounded_item_score >= pass_threshold"}
