#!/bin/bash

echo "📄 Fusion v14.3 Master Prompt (Trimmed Version)"
echo "================================================"
echo ""
echo "Copy the content below into ChatGPT:"
echo ""

cat ~/fusion/master_prompt/master_prompt_8000.md

echo ""
echo "================================================"
echo "✅ Ready to copy-paste into ChatGPT!"
echo "📝 Size: $(wc -c < ~/fusion/master_prompt/master_prompt_8000.md) characters (under 8000 tokens)" 