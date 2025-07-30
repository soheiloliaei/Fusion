#!/bin/bash

# === Fusion Unified Repo Setup: fusion_push.command ===
# 📁 Directory: ~/fusion
# 🗂 Upload context: fusion/ChatGPT_Upload/
# 📝 Version info tracked in: fusion/README.md

cd ~/fusion

# 🔁 Step 1: Clean old upload dir
rm -rf ChatGPT_Upload/*
echo "🧹 Cleaned old ChatGPT_Upload"

# 📦 Step 2: Copy trimmed files into upload folder (under 10)
cp fusion.py ChatGPT_Upload/
cp fusion_context.py ChatGPT_Upload/
cp agents_combined.py ChatGPT_Upload/
cp tools_combined.py ChatGPT_Upload/
cp memory_system.py ChatGPT_Upload/
cp execution_orchestrator_v14.py ChatGPT_Upload/
cp patterns/pattern_registry.py ChatGPT_Upload/
cp README.md ChatGPT_Upload/
cp .fusion.json ChatGPT_Upload/config.json

# ✂️ Step 3: Trim and copy Master Prompt (auto-trim under 8000 tokens)
tail -c 7900 master_prompt/master_prompt.md > ChatGPT_Upload/master_prompt.md

# 🧪 Step 4: Validate file count
count=$(ls ChatGPT_Upload | wc -l)
if [ "$count" -gt 10 ]; then
  echo "❌ Too many files in ChatGPT_Upload ($count). Limit = 10."
  exit 1
fi

echo "✅ ChatGPT Upload folder ready with $count files"
echo "👉 Upload from: ~/fusion/ChatGPT_Upload/" 