#!/bin/bash

echo "🧠 ChatGPT Fusion v14.3 Launcher"
echo "=================================="

# First, sync the latest files
echo "📦 Syncing latest files..."
~/fusion/chatgpt_sync.command

echo ""
echo "🎯 ChatGPT Setup Instructions:"
echo "=============================="
echo ""
echo "1️⃣ Link GitHub Repository:"
echo "   https://github.com/soheiloliaei/Fusion.git"
echo ""
echo "2️⃣ Upload Files:"
echo "   ~/fusion/ChatGPT_Upload_v14.3/"
echo ""
echo "3️⃣ Master Prompt Options:"
echo ""

# Show the trimmed version for copy-paste
echo "📄 TRIMMED VERSION (Under 8000 tokens):"
echo "----------------------------------------"
cat ~/fusion/master_prompt/master_prompt_8000.md
echo ""
echo "----------------------------------------"
echo ""

# Show the full version for reference
echo "📄 FULL VERSION (Complete documentation):"
echo "----------------------------------------"
echo "File: ~/fusion/master_prompt/master_prompt_main.md"
echo "Size: $(wc -c < ~/fusion/master_prompt/master_prompt_main.md) characters"
echo "Use: For complete development reference"
echo ""

echo "✅ Setup Complete!"
echo "🎯 You can now use Fusion v14.3 in ChatGPT"
echo ""
echo "💡 Tip: Use the trimmed version for ChatGPT, full version for development" 