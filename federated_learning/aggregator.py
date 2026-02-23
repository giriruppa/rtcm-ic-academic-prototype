"""Federated model aggregation functions."""

from __future__ import annotations


def aggregate_updates(updates: list[dict[str, dict[str, float]]]) -> dict[str, float]:
    """Aggregate local updates into a national overview without raw event sharing."""
    if not updates:
        return {"participants": 0.0, "total_events": 0.0, "national_avg_risk": 0.0, "max_risk": 0.0}

    participants = 0
    total_events = 0.0
    weighted_risk = 0.0
    max_risk = 0.0

    for node in updates:
        for _, summary in node.items():
            participants += 1
            count = summary.get("count", 0.0)
            avg_risk = summary.get("avg_risk", 0.0)
            total_events += count
            weighted_risk += avg_risk * count
            max_risk = max(max_risk, summary.get("max_risk", 0.0))

    national_avg_risk = round(weighted_risk / total_events, 2) if total_events else 0.0

    return {
        "participants": float(participants),
        "total_events": float(total_events),
        "national_avg_risk": national_avg_risk,
        "max_risk": max_risk,
    }
