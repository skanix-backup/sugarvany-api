#!/bin/bash

# Set environment
export ENVIRONMENT=production

# Activate virtual environment if using one
# source .venv/bin/activate  # Uncomment if using virtual environment

# Run Uvicorn with production settings
uvicorn sugarvany_api.interface.api.app:app \
    --host 0.0.0.0 \
    --port 8000 \
    --workers 2 \
    --log-level info \
    --proxy-headers \
    --forwarded-allow-ips '*' \
    --timeout-keep-alive 120