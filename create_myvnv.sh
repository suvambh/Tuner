#!/bin/bash

ENV_NAME=${1:-venv}
REQ_FILE="requirements.txt"

echo "🔧 Creating virtual environment: $ENV_NAME"
python3.11 -m venv "$ENV_NAME"

echo "✅ Virtual environment created."

echo "📦 Activating environment and installing packages..."
source "$ENV_NAME/bin/activate"

if [ -f "$REQ_FILE" ]; then
    pip install --upgrade pip
    pip install -r "$REQ_FILE"
    echo "📦 Installed packages from $REQ_FILE"
else
    echo "❌ requirements.txt not found."
    echo "⚠️  No packages were installed."
fi

pip freeze > "$ENV_NAME/locked_requirements.txt"
echo "📄 Locked requirements saved to $ENV_NAME/locked_requirements.txt"
echo "✅ Done. To activate later, run: source $ENV_NAME/bin/activate"
