#!/bin/bash

# Install requirements from requirements.txt
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ All dependencies installed successfully."
