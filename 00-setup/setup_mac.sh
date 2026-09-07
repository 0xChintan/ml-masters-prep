#!/usr/bin/env bash
# Setup script for macOS & Linux

echo "=== Setting up Python environment (macOS/Linux) ==="
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r 00-setup/requirements.txt

echo ""
echo "=== Running verification ==="
python3 00-setup/verify_setup.py

