#!/bin/bash
set -e

# Check Python version
if command -v python3.10 &>/dev/null; then
    PYTHON_CMD=python3.10
else
    echo "Python 3.10 is required but not found."
    exit 1
fi

# Create virtual environment
if [ ! -d "venv" ]; then
    $PYTHON_CMD -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
