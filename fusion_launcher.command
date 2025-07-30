#!/bin/bash

# === Fusion v14.3 Launcher ===

# SETTINGS
REPO_URL="https://github.com/soheiloliaei/Fusion.git"
INSTALL_DIR="$HOME/Desktop/fusion"

echo "🚀 Installing Fusion v14.3..."

# CLONE or PULL REPO
if [ -d "$INSTALL_DIR/.git" ]; then
  echo "📦 Repo found. Pulling latest..."
  cd "$INSTALL_DIR"
  git pull
else
  echo "📥 Cloning Fusion repo..."
  git clone "$REPO_URL" "$INSTALL_DIR"
fi

# SETUP
cd "$INSTALL_DIR"

echo "🔧 Creating upload folder..."
rm -rf ChatGPT_Upload_v14.3
mkdir -p ChatGPT_Upload_v14.3

echo "📂 Copying core files to ChatGPT_Upload..."
cp fusion.py ChatGPT_Upload_v14.3/
cp master_prompt/master_prompt_main.md ChatGPT_Upload_v14.3/
cp master_prompt/master_prompt_8000.md ChatGPT_Upload_v14.3/
cp README.md ChatGPT_Upload_v14.3/
cp agents_combined.py ChatGPT_Upload_v14.3/
cp tools_combined.py ChatGPT_Upload_v14.3/
cp execution_orchestrator_v14.py ChatGPT_Upload_v14.3/
cp fusion_context.py ChatGPT_Upload_v14.3/
cp memory_system.py ChatGPT_Upload_v14.3/
cp patterns/pattern_registry.py ChatGPT_Upload_v14.3/
cp .fusion.json ChatGPT_Upload_v14.3/config.json 2>/dev/null || echo "⚠️ .fusion.json not found, using fallback"

echo "📦 Creating Python venv..."
python3 -m venv .venv
source .venv/bin/activate

echo "⬇️ Installing dependencies..."
pip install -r requirements.txt 2>/dev/null || echo "⚠️ No requirements.txt found — skipping pip install"

echo "✅ Fusion v14.3 installed at $INSTALL_DIR"
open -a Terminal "$INSTALL_DIR"

echo "🎯 Ready to run:"
echo "  cd ~/Desktop/fusion"
echo "  python3 fusion.py run vp_design 'Design a user-friendly dashboard'"

exit 0
