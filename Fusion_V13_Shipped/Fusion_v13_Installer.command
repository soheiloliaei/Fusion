#!/bin/bash

echo "🚀 Installing Fusion v13.0 with VP of Design..."
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
echo "🎨 VP of Design agent ready for AI-first critique"

# Optional GitHub and ChatGPT packaging
read -p "📦 Do you want to package for ChatGPT? (y/n): " package_choice
if [[ "$package_choice" == "y" ]]; then
  echo "🚀 Running ChatGPT packaging with VP of Design..."
  python3 fusion_launcher.py package
fi

read -p "🌐 Do you want to push to GitHub? (y/n): " push_choice
if [[ "$push_choice" == "y" ]]; then
  echo "🚀 Pushing to GitHub with VP of Design transformation..."
  python3 fusion_launcher.py push
fi

echo ""
echo "🎯 Fusion v13.0 with VP of Design is now fully installed and ready to use!"
echo "📁 Installed in: ./fusion_v13/"
echo "🎨 VP of Design agent provides AI-first design critique"
echo "💡 Run with: orchestrator.run('Your prompt here')"
echo ""
echo "🎨 VP of Design Features:"
echo "   - User-centric design thinking"
echo "   - Design system alignment"
echo "   - Accessibility & inclusion"
echo "   - Business impact through design"
echo "   - Technical feasibility"
echo "   - AI-first design thinking"
