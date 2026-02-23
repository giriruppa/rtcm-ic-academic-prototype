#!/usr/bin/env bash
set -euo pipefail

python3 -c "from dashboard.app import seed_data; print(seed_data(force_refresh=True))"
echo "Setup complete. Run: python3 dashboard/app.py"
