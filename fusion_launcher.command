#!/bin/bash

echo "🧠 Initializing Fusion v14.3 Launcher..."

FUSION_REPO="https://github.com/soheiloliaei/Fusion.git"
FUSION_DIR=".fusion_engine"

if [ -d "$FUSION_DIR" ]; then
  echo "♻️  Removing existing $FUSION_DIR..."
  rm -rf "$FUSION_DIR"
fi

echo "📥 Cloning Fusion from GitHub..."
git clone --depth=1 "$FUSION_REPO" "$FUSION_DIR"

cd "$FUSION_DIR"
rm -rf .git .github LICENSE README.md docs tests scripts
cd ..

if [ ! -f ".gitignore" ]; then
  touch .gitignore
fi

# Add fusion directory to .gitignore (optional)
if ! grep -q "$FUSION_DIR" .gitignore; then
  echo "$FUSION_DIR/" >> .gitignore
  echo "✅ Added $FUSION_DIR to .gitignore"
fi

echo "✅ Fusion is now available at: $FUSION_DIR"
echo "👉 Run with: python3 $FUSION_DIR/fusion.py pipeline 'your task here'"
