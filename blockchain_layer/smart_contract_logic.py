"""Smart-contract-style incident response policy logic."""

from __future__ import annotations

from edge_node.anomaly_detection import ThreatAssessment


def containment_action(assessment: ThreatAssessment) -> str:
    """Decide automated response based on risk and event type."""
    if assessment.risk_score >= 16:
        return "isolate_network_segment"
    if assessment.risk_score >= 12:
        return "block_source_and_raise_priority_alert"
    if assessment.risk_score >= 6:
        return "raise_alert_and_monitor"
    return "log_only"
