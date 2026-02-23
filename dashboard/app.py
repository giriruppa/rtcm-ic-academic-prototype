"""RTCMAS-IC dashboard server (stdlib only): backend, frontend, and database."""

from __future__ import annotations

import html
import json
import sqlite3
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from blockchain_layer.blockchain_simulator import IncidentLedger
from blockchain_layer.smart_contract_logic import containment_action
from cyber_twin.threat_simulator import simulate_next_24h
from edge_node.anomaly_detection import assess_events
from edge_node.data_collector import collect_from_csv
from federated_learning.aggregator import aggregate_updates
from federated_learning.local_model import build_local_update

DB_PATH = BASE_DIR / "dataset" / "rtcmas.db"
CSV_PATH = BASE_DIR / "dataset" / "sample_logs.csv"


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS incidents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                source TEXT NOT NULL,
                region TEXT NOT NULL,
                event_type TEXT NOT NULL,
                severity TEXT NOT NULL,
                risk_score INTEGER NOT NULL,
                confidence TEXT NOT NULL,
                threat_dna TEXT NOT NULL,
                action TEXT NOT NULL
            )
            """
        )
        conn.commit()


def seed_data(force_refresh: bool = True) -> dict[str, Any]:
    init_db()

    events = collect_from_csv(CSV_PATH)
    assessments = assess_events(events)
    ledger = IncidentLedger()

    with get_connection() as conn:
        if force_refresh:
            conn.execute("DELETE FROM incidents")

        for item in assessments:
            action = containment_action(item)
            payload = {
                "timestamp": item.event.timestamp,
                "source": item.event.source,
                "event_type": item.event.event_type,
                "risk_score": item.risk_score,
                "threat_dna": item.threat_dna,
                "action": action,
            }
            ledger.add_incident(payload)

            conn.execute(
                """
                INSERT INTO incidents
                (timestamp, source, region, event_type, severity, risk_score, confidence, threat_dna, action)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    item.event.timestamp,
                    item.event.source,
                    item.event.region,
                    item.event.event_type,
                    item.event.severity,
                    item.risk_score,
                    item.confidence,
                    item.threat_dna,
                    action,
                ),
            )
        conn.commit()

    national_summary = aggregate_updates([build_local_update(assessments)])

    return {
        "records": len(assessments),
        "ledger_valid": ledger.verify_chain(),
        "national_summary": national_summary,
        "projection": simulate_next_24h(assessments),
    }


def fetch_dashboard_data() -> dict[str, Any]:
    with get_connection() as conn:
        incidents = [dict(row) for row in conn.execute("SELECT * FROM incidents ORDER BY risk_score DESC, id DESC")]
        by_severity = [
            dict(row)
            for row in conn.execute(
                "SELECT severity, COUNT(*) as count FROM incidents GROUP BY severity ORDER BY count DESC"
            )
        ]
        by_region = [
            dict(row)
            for row in conn.execute(
                "SELECT region, COUNT(*) as count FROM incidents GROUP BY region ORDER BY count DESC"
            )
        ]

    high_risk = sum(1 for i in incidents if i["risk_score"] >= 12)

    return {
        "incidents": incidents,
        "metrics": {
            "total_incidents": len(incidents),
            "high_risk_incidents": high_risk,
            "auto_containment": sum(1 for i in incidents if i["action"] != "log_only"),
            "unique_sources": len({i["source"] for i in incidents}),
        },
        "by_severity": by_severity,
        "by_region": by_region,
    }


def render_dashboard(data: dict[str, Any]) -> str:
    metric_cards = f"""
      <div class='card'><h3>Total Incidents</h3><div class='metric'>{data['metrics']['total_incidents']}</div></div>
      <div class='card'><h3>High-Risk Incidents</h3><div class='metric'>{data['metrics']['high_risk_incidents']}</div></div>
      <div class='card'><h3>Auto Containment Actions</h3><div class='metric'>{data['metrics']['auto_containment']}</div></div>
      <div class='card'><h3>Unique Sources</h3><div class='metric'>{data['metrics']['unique_sources']}</div></div>
    """

    severity_items = "".join(
        f"<li><strong>{html.escape(row['severity'])}</strong>: {row['count']}</li>" for row in data["by_severity"]
    )
    region_items = "".join(
        f"<li><strong>{html.escape(row['region'])}</strong>: {row['count']}</li>" for row in data["by_region"]
    )

    rows = []
    for item in data["incidents"]:
        rows.append(
            "<tr>"
            f"<td>{item['id']}</td>"
            f"<td>{html.escape(item['timestamp'])}</td>"
            f"<td>{html.escape(item['source'])}</td>"
            f"<td>{html.escape(item['region'])}</td>"
            f"<td>{html.escape(item['event_type'])}</td>"
            f"<td><span class='pill {html.escape(item['severity'])}'>{html.escape(item['severity'])}</span></td>"
            f"<td>{item['risk_score']}</td>"
            f"<td>{html.escape(item['action'])}</td>"
            "</tr>"
        )

    table_rows = "".join(rows)

    return f"""<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8' />
<meta name='viewport' content='width=device-width, initial-scale=1.0' />
<title>RTCMAS-IC Dashboard</title>
<style>
body {{ font-family: Arial, sans-serif; margin: 0; background: #f5f7fb; color: #1a2433; }}
header {{ background: #0d2a4c; color: white; padding: 1rem 1.5rem; }}
.container {{ padding: 1.2rem 1.5rem; }}
.grid {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 1rem; margin-bottom: 1rem; }}
.card {{ background: white; border-radius: 10px; padding: 1rem; box-shadow: 0 2px 10px rgba(0,0,0,0.08); }}
.card h3 {{ margin: 0; color: #345; font-size: .9rem; }}
.metric {{ margin-top: .45rem; font-size: 1.6rem; font-weight: 700; }}
table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; }}
th, td {{ padding: .6rem .5rem; border-bottom: 1px solid #e6ebf2; font-size: .9rem; text-align: left; }}
th {{ background: #1f4876; color: white; }}
.pill {{ border-radius: 999px; padding: .15rem .45rem; font-size: .8rem; color: white; }}
.low {{ background: #5d8f3b; }} .medium {{ background: #b88713; }} .high {{ background: #bf5400; }} .critical {{ background: #b00020; }}
.sections {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem; }}
ul {{ margin: .5rem 0 0 1rem; }}
</style>
</head>
<body>
<header>
  <h1>RTCMAS-IC National Threat Monitoring Dashboard</h1>
  <div>Prototype: integrated data processing, federated summary, blockchain-style incident traceability, and response logic</div>
</header>
<div class='container'>
  <div class='grid'>{metric_cards}</div>
  <div class='sections'>
    <div class='card'><h3>Incidents by Severity</h3><ul>{severity_items}</ul></div>
    <div class='card'><h3>Incidents by Region</h3><ul>{region_items}</ul></div>
  </div>
  <div class='card'>
    <h3>Incident Stream</h3>
    <table>
      <thead><tr><th>ID</th><th>Timestamp</th><th>Source</th><th>Region</th><th>Type</th><th>Severity</th><th>Risk</th><th>Action</th></tr></thead>
      <tbody>{table_rows}</tbody>
    </table>
  </div>
</div>
</body>
</html>"""


class RequestHandler(BaseHTTPRequestHandler):
    def _send(self, body: str, status: int = 200, content_type: str = "text/html") -> None:
        encoded = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path == "/":
            self._send(render_dashboard(fetch_dashboard_data()))
            return
        if parsed.path == "/api/incidents":
            self._send(json.dumps(fetch_dashboard_data()), content_type="application/json")
            return
        if parsed.path == "/api/projection":
            assessments = assess_events(collect_from_csv(CSV_PATH))
            self._send(json.dumps(simulate_next_24h(assessments)), content_type="application/json")
            return
        self._send("Not found", status=404, content_type="text/plain")


def run(host: str = "0.0.0.0", port: int = 5000) -> None:
    seed_data(force_refresh=True)
    server = HTTPServer((host, port), RequestHandler)
    print(f"RTCMAS-IC dashboard running on http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
