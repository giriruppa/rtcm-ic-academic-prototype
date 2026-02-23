"""Local federated node summary generation."""

from __future__ import annotations

from collections import defaultdict

from edge_node.anomaly_detection import ThreatAssessment


def build_local_update(assessments: list[ThreatAssessment]) -> dict[str, dict[str, float]]:
    """Create per-source summary updates to share with aggregator."""
    grouped: dict[str, list[int]] = defaultdict(list)
    for item in assessments:
        grouped[item.event.source].append(item.risk_score)

    update: dict[str, dict[str, float]] = {}
    for source, scores in grouped.items():
        update[source] = {
            "count": float(len(scores)),
            "avg_risk": round(sum(scores) / len(scores), 2),
            "max_risk": float(max(scores)),
        }
    return update
