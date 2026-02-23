"""Edge data collection and normalization utilities."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class TelemetryEvent:
    timestamp: str
    source: str
    ip_address: str
    event_type: str
    severity: str
    description: str
    region: str


VALID_SEVERITIES = {"low", "medium", "high", "critical"}


def _normalize_row(row: dict[str, str]) -> TelemetryEvent:
    severity = row.get("severity", "low").strip().lower()
    if severity not in VALID_SEVERITIES:
        severity = "low"

    return TelemetryEvent(
        timestamp=row.get("timestamp", "").strip(),
        source=row.get("source", "unknown").strip().lower(),
        ip_address=row.get("ip_address", "0.0.0.0").strip(),
        event_type=row.get("event_type", "unknown").strip().lower(),
        severity=severity,
        description=row.get("description", "").strip(),
        region=row.get("region", "unknown").strip().title(),
    )


def collect_from_csv(csv_path: str | Path) -> list[TelemetryEvent]:
    """Load telemetry logs from CSV and normalize into telemetry events."""
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Telemetry CSV not found: {path}")

    events: list[TelemetryEvent] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            events.append(_normalize_row(row))
    return events


def to_dicts(events: Iterable[TelemetryEvent]) -> list[dict[str, str]]:
    """Convert event objects into serializable dictionaries."""
    return [event.__dict__.copy() for event in events]
