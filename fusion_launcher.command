#!/bin/bash

echo "🚀 Installing Fusion v14.3 in current directory..."

# CONFIG
REPO_URL="https://github.com/soheiloliaei/Fusion.git"
LOCAL_REPO="$HOME/fusion"
CURRENT_DIR="$(pwd)"

# Step 1: Clone repo if it doesn't exist locally
if [ ! -d "$LOCAL_REPO" ]; then
  echo "📁 Cloning Fusion repo..."
  git clone "$REPO_URL" "$LOCAL_REPO"
else
  echo "🔄 Pulling latest from Fusion repo..."
  cd "$LOCAL_REPO" && git pull && cd "$CURRENT_DIR"
fi

# Step 2: Copy all Fusion files to current directory
echo "📦 Installing Fusion files in current directory..."

# Check if we're in the fusion directory itself
if [ "$CURRENT_DIR" = "$LOCAL_REPO" ]; then
  echo "ℹ️ Already in Fusion directory - files are ready!"
else
  # Core Fusion files
  cp "$LOCAL_REPO"/fusion.py "$CURRENT_DIR/" 2>/dev/null || echo "⚠️ fusion.py not found"
  cp "$LOCAL_REPO"/agents_combined.py "$CURRENT_DIR/" 2>/dev/null || echo "⚠️ agents_combined.py not found"
  cp "$LOCAL_REPO"/tools_combined.py "$CURRENT_DIR/" 2>/dev/null || echo "⚠️ tools_combined.py not found"
  cp "$LOCAL_REPO"/execution_orchestrator_v14.py "$CURRENT_DIR/" 2>/dev/null || echo "⚠️ execution_orchestrator_v14.py not found"
  cp "$LOCAL_REPO"/fusion_context.py "$CURRENT_DIR/" 2>/dev/null || echo "⚠️ fusion_context.py not found"
  cp "$LOCAL_REPO"/memory_system.py "$CURRENT_DIR/" 2>/dev/null || echo "⚠️ memory_system.py not found"
  cp "$LOCAL_REPO"/autocritique_loop.py "$CURRENT_DIR/" 2>/dev/null || echo "⚠️ autocritique_loop.py not found"
  cp "$LOCAL_REPO"/task_classifier_agent.py "$CURRENT_DIR/" 2>/dev/null || echo "⚠️ task_classifier_agent.py not found"
  cp "$LOCAL_REPO"/voice_modulation_engine.py "$CURRENT_DIR/" 2>/dev/null || echo "⚠️ voice_modulation_engine.py not found"

  # Master prompt files
  cp "$LOCAL_REPO"/master_prompt/master_prompt_main.md "$CURRENT_DIR/" 2>/dev/null || echo "⚠️ master_prompt_main.md not found"
  cp "$LOCAL_REPO"/master_prompt/master_prompt_8000.md "$CURRENT_DIR/" 2>/dev/null || echo "⚠️ master_prompt_8000.md not found"

  # Pattern files
  cp "$LOCAL_REPO"/patterns/pattern_registry.py "$CURRENT_DIR/" 2>/dev/null || echo "⚠️ pattern_registry.py not found"

  # Config and docs
  cp "$LOCAL_REPO"/.fusion.json "$CURRENT_DIR/" 2>/dev/null || echo "{}" > "$CURRENT_DIR/.fusion.json"
  cp "$LOCAL_REPO"/README.md "$CURRENT_DIR/" 2>/dev/null || echo "⚠️ README.md not found"

  # Create directories if they don't exist
  mkdir -p "$CURRENT_DIR/master_prompt" 2>/dev/null
  mkdir -p "$CURRENT_DIR/patterns" 2>/dev/null
  mkdir -p "$CURRENT_DIR/agents" 2>/dev/null
  mkdir -p "$CURRENT_DIR/tools" 2>/dev/null

  # Copy additional files to their proper directories
  cp "$LOCAL_REPO"/master_prompt/*.md "$CURRENT_DIR/master_prompt/" 2>/dev/null || echo "⚠️ master_prompt files not found"
  cp "$LOCAL_REPO"/patterns/*.py "$CURRENT_DIR/patterns/" 2>/dev/null || echo "⚠️ pattern files not found"
fi

# Step 3: Make fusion.py executable
chmod +x "$CURRENT_DIR/fusion.py" 2>/dev/null

# Step 4: Show what was installed
echo ""
echo "✅ Fusion v14.3 installed in: $CURRENT_DIR"
echo ""
echo "📁 Files installed:"
ls -la "$CURRENT_DIR" | grep -E "(fusion|master_prompt|agents|tools|patterns)" | head -10
echo ""

# Step 5: Show available commands
echo "🎬 Fusion v14.3 Commands Available:"
python3 "$CURRENT_DIR/fusion.py" --help

echo ""
echo "🎯 Your project is now Fusion-enabled!"
echo "💡 Run: python3 fusion.py run vp_design 'your design task'"
