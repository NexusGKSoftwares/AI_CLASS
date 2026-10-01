#!/bin/bash
# ==============================================================================
# Helper Script to Launch Jupyter Lab for AI Practical Class
# ==============================================================================

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
    echo "====================================================="
    echo "   Launching Jupyter Lab with AI Class Environment "
    echo "====================================================="
    jupyter lab labs/interactive_ai_lab.ipynb
else
    echo "Error: Virtual environment not found at .venv"
    exit 1
fi
