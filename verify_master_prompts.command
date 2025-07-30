#!/bin/bash

echo "🔍 Verifying Master Prompt Files..."
echo "=================================="

# Check local master_prompt directory
echo "📁 Local master_prompt/ directory:"
if [ -f "master_prompt/master_prompt_main.md" ]; then
    echo "✅ master_prompt_main.md exists ($(wc -c < master_prompt/master_prompt_main.md) chars)"
else
    echo "❌ master_prompt_main.md MISSING"
fi

if [ -f "master_prompt/master_prompt_8000.md" ]; then
    echo "✅ master_prompt_8000.md exists ($(wc -c < master_prompt/master_prompt_8000.md) chars)"
else
    echo "❌ master_prompt_8000.md MISSING"
fi

echo ""

# Check ChatGPT upload directory
echo "📁 ChatGPT_Upload_v14.3/ directory:"
if [ -f "ChatGPT_Upload_v14.3/master_prompt_main.md" ]; then
    echo "✅ master_prompt_main.md exists ($(wc -c < ChatGPT_Upload_v14.3/master_prompt_main.md) chars)"
else
    echo "❌ master_prompt_main.md MISSING"
fi

if [ -f "ChatGPT_Upload_v14.3/master_prompt_8000.md" ]; then
    echo "✅ master_prompt_8000.md exists ($(wc -c < ChatGPT_Upload_v14.3/master_prompt_8000.md) chars)"
else
    echo "❌ master_prompt_8000.md MISSING"
fi

echo ""

# Check git status
echo "📦 Git Status:"
if git ls-files | grep -q "master_prompt_main.md"; then
    echo "✅ master_prompt_main.md tracked in git"
else
    echo "❌ master_prompt_main.md NOT tracked in git"
fi

if git ls-files | grep -q "master_prompt_8000.md"; then
    echo "✅ master_prompt_8000.md tracked in git"
else
    echo "❌ master_prompt_8000.md NOT tracked in git"
fi

echo ""
echo "🎯 Verification Complete!"
echo "📋 See MASTER_PROMPT_RULES.md for complete guidelines" 