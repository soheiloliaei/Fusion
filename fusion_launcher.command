#!/bin/bash

echo "🚀 Launching Fusion v14.3..."

# CONFIG
REPO_URL="https://github.com/soheiloliaei/Fusion.git"
LOCAL_REPO="$HOME/fusion"
UPLOAD_DIR="$LOCAL_REPO/ChatGPT_Upload_v14.3"
CONFIG_FILE=".fusion.json"

# Step 1: Clone repo if it doesn't exist
if [ ! -d "$LOCAL_REPO" ]; then
  echo "📁 Cloning Fusion repo..."
  git clone "$REPO_URL" "$LOCAL_REPO"
else
  echo "🔄 Pulling latest from Fusion repo..."
  cd "$LOCAL_REPO" && git pull
fi

# Step 2: Ensure upload directory exists
mkdir -p "$UPLOAD_DIR"

# Step 3: Copy latest core files
echo "📦 Syncing files into ChatGPT_Upload..."
cp "$LOCAL_REPO"/fusion.py "$UPLOAD_DIR"
cp "$LOCAL_REPO"/master_prompt/master_prompt_main.md "$UPLOAD_DIR"
cp "$LOCAL_REPO"/master_prompt/master_prompt_8000.md "$UPLOAD_DIR"
cp "$LOCAL_REPO"/README.md "$UPLOAD_DIR"
cp "$LOCAL_REPO"/agents_combined.py "$UPLOAD_DIR"
cp "$LOCAL_REPO"/tools_combined.py "$UPLOAD_DIR"
cp "$LOCAL_REPO"/execution_orchestrator_v14.py "$UPLOAD_DIR"
cp "$LOCAL_REPO"/fusion_context.py "$UPLOAD_DIR"
cp "$LOCAL_REPO"/memory_system.py "$UPLOAD_DIR"
cp "$LOCAL_REPO"/patterns/pattern_registry.py "$UPLOAD_DIR"

# Step 4: Add .fusion.json for local runs
echo "🛠️ Adding config..."
cp "$LOCAL_REPO/$CONFIG_FILE" "$UPLOAD_DIR" 2>/dev/null || echo "{}" > "$UPLOAD_DIR/$CONFIG_FILE"

# Step 5: Show Fusion help (optional)
cd "$LOCAL_REPO"
echo "🎬 Fusion v14.3 Commands Available:"
python3 fusion.py --help

echo "✅ Fusion v14.3 is ready in ChatGPT_Upload_v14.3"
