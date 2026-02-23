"""Predictive cyber twin simulation utilities."""

from __future__ import annotations

from collections import Counter

from edge_node.anomaly_detection import ThreatAssessment


def simulate_next_24h(assessments: list[ThreatAssessment]) -> dict[str, int]:
    """Very lightweight projection of likely next-24h threat distribution."""
    event_counts = Counter(item.event.event_type for item in assessments)
    projected: dict[str, int] = {}

    for event_type, count in event_counts.items():
        # Growth factor uses confidence/risk trend proxy from observed scores.
        avg_event_risk = sum(
            item.risk_score for item in assessments if item.event.event_type == event_type
        ) / count
        growth = 1.35 if avg_event_risk >= 12 else 1.15 if avg_event_risk >= 6 else 1.05
        projected[event_type] = int(round(count * growth))

    return dict(sorted(projected.items(), key=lambda item: item[1], reverse=True))
