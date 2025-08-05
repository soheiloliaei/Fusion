#!/bin/bash

echo "🚀 Installing Fusion v15..."

# Set working directory
PROJECT_DIR=$(pwd)
FUSION_DIR="$PROJECT_DIR/fusion_v15"
CHATGPT_DIR="$PROJECT_DIR/ChatGPT_Upload_v15"

# Clean and prepare ChatGPT upload folder
rm -rf "$CHATGPT_DIR"
mkdir -p "$CHATGPT_DIR"

# Copy core files (under 20 files)
cp -r fusion_core "$CHATGPT_DIR/"
cp fusion_api.py web_app.py fusion.py "$CHATGPT_DIR/"
cp agent_manifest.json requirements.txt pyproject.toml Dockerfile "$CHATGPT_DIR/"
cp FUSION_V15_README.md FUSION_V15_DELIVERY_SUMMARY.md "$CHATGPT_DIR/"
cp prompt_master_short.md "$CHATGPT_DIR/"
cp prompt_master_main.md "$CHATGPT_DIR/"

echo "📁 Copied all files to ChatGPT_Upload_v15"

# Install + launch API + GUI
echo "⚙️ Setting up Fusion v15..."
pip install -e .
streamlit run web_app.py &

echo "✅ Fusion v15 launched. Visit your browser!" 