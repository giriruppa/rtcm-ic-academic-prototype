# RTCMAS-IC Academic Prototype

A runnable prototype of the **Real-Time Cyber Threat Monitoring and Alert System for Indian Cyberspace (RTCMAS-IC)** covering:
- **Frontend:** browser dashboard for threat monitoring
- **Backend:** event ingestion, anomaly scoring, federated summary, immutable incident logging simulation, response policy logic
- **Database:** SQLite-backed incident storage
- **Data processing:** CSV normalization, risk scoring, and cyber-twin projection

## Repository Structure
- `dashboard/app.py` — stdlib HTTP server + API endpoints + DB orchestration
- `dataset/sample_logs.csv` — sample cyber telemetry dataset
- `dataset/rtcmas.db` — SQLite database (generated at runtime)
- `edge_node/` — telemetry collection and anomaly detection
- `federated_learning/` — local model summaries and aggregation
- `blockchain_layer/` — incident ledger simulation and smart contract response rules
- `cyber_twin/` — next-24h threat projection
- `docs/annexure3b-invention-disclosure.md` — Annexure 3B document

## Quick Start
```bash
./setup.sh
python3 dashboard/app.py
```
Open: `http://localhost:5000`

## API Endpoints
- `GET /api/incidents` — incident list + summary metrics
- `GET /api/projection` — projected next-24h event distribution

## Notes
This is an academic prototype to demonstrate integrated flow and architecture, not a production-grade cybersecurity deployment.
