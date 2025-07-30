#!/bin/bash

echo "🔁 Syncing ChatGPT_Upload..."

# Set the correct project directory (where the actual files are)
PROJECT_DIR=~/fusion
UPLOAD_DIR="$PROJECT_DIR/ChatGPT_Upload_v14.3"

# Change to the project directory
cd "$PROJECT_DIR"

# Clean and recreate upload directory
rm -rf "$UPLOAD_DIR"
mkdir -p "$UPLOAD_DIR"

# Copy core files into upload folder
cp fusion.py "$UPLOAD_DIR/"
cp master_prompt/master_prompt_8000.md "$UPLOAD_DIR/master_prompt.md"
cp README.md "$UPLOAD_DIR/"
cp agents_combined.py "$UPLOAD_DIR/"
cp tools_combined.py "$UPLOAD_DIR/"
cp execution_orchestrator_v14.py "$UPLOAD_DIR/"
cp fusion_context.py "$UPLOAD_DIR/"
cp memory_system.py "$UPLOAD_DIR/"
cp patterns/pattern_registry.py "$UPLOAD_DIR/"
cp .fusion.json "$UPLOAD_DIR/config.json"

echo "✅ Files prepared in $UPLOAD_DIR"
echo "📝 Using master_prompt_8000.md (under 8000 tokens)"
open "$UPLOAD_DIR"
