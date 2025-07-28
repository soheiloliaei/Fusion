#!/bin/bash

echo "🚀 Installing Fusion v13.0..."
echo "============================================================"

SOURCE_DIR="./fusion_v13"
TARGET_DIR="./fusion_v13"
FILES=(
  "agents"
  "patterns"
  "core"
  "fusion_launcher.py"
  "master_prompt.md"
  "Fusion_v13_Installer.command"
  "Fusion_v13.0_Launcher.sh"
  "README.md"
)

for ITEM in "${FILES[@]}"
do
  if [ -e "$TARGET_DIR/$ITEM" ]; then
    echo "⚠️  $ITEM already exists. Skipping..."
  else
    cp -R "$SOURCE_DIR/$ITEM" "$TARGET_DIR/$ITEM"
    echo "✅  Copied $ITEM"
  fi
done

echo ""
echo "✅ All required files are now in place."

# Optional GitHub and ChatGPT packaging
read -p "📦 Do you want to package for ChatGPT? (y/n): " package_choice
if [[ "$package_choice" == "y" ]]; then
  echo "🚀 Running ChatGPT packaging..."
  python3 fusion_launcher.py package
fi

read -p "🌐 Do you want to push to GitHub? (y/n): " push_choice
if [[ "$push_choice" == "y" ]]; then
  echo "🚀 Pushing to GitHub..."
  python3 fusion_launcher.py push
fi

echo ""
echo "🎯 Fusion v13.0 is now fully installed and ready to use!"
echo "📁 Installed in: ./fusion_v13/"
echo "💡 Run with: orchestrator.run('Your prompt here')"
