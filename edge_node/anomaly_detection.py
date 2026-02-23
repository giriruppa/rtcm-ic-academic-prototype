"""Simple anomaly scoring for telemetry events."""

from __future__ import annotations

from dataclasses import dataclass

from edge_node.data_collector import TelemetryEvent


SEVERITY_WEIGHT = {
    "low": 1,
    "medium": 2,
    "high": 3,
    "critical": 4,
}

EVENT_WEIGHT = {
    "failed_login": 1,
    "phishing": 2,
    "ddos": 4,
    "data_exfiltration": 4,
    "malware": 3,
    "intrusion": 4,
    "ransomware": 4,
    "credential_stuffing": 3,
    "botnet": 2,
    "firmware_tamper": 3,
    "sql_injection": 2,
    "privilege_escalation": 3,
    "scada_probe": 4,
}


@dataclass
class ThreatAssessment:
    event: TelemetryEvent
    risk_score: int
    threat_dna: str
    confidence: str


def assess_event(event: TelemetryEvent) -> ThreatAssessment:
    base = SEVERITY_WEIGHT.get(event.severity, 1)
    modifier = EVENT_WEIGHT.get(event.event_type, 1)
    risk_score = base * modifier

    if risk_score >= 12:
        confidence = "high"
    elif risk_score >= 6:
        confidence = "medium"
    else:
        confidence = "low"

    threat_dna = f"{event.event_type}:{event.source}:{event.region}:{risk_score}"

    return ThreatAssessment(
        event=event,
        risk_score=risk_score,
        threat_dna=threat_dna,
        confidence=confidence,
    )


def assess_events(events: list[TelemetryEvent]) -> list[ThreatAssessment]:
    return [assess_event(event) for event in events]
