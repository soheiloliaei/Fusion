#!/bin/bash

echo "🔁 Syncing ChatGPT_Upload..."

# Clean and recreate upload directory
rm -rf ChatGPT_Upload_v14.3
mkdir -p ChatGPT_Upload_v14.3

# Copy core files into upload folder (using relative paths)
cp fusion.py ChatGPT_Upload_v14.3/
cp master_prompt/master_prompt.md ChatGPT_Upload_v14.3/
cp README.md ChatGPT_Upload_v14.3/
cp agents_combined.py ChatGPT_Upload_v14.3/
cp tools_combined.py ChatGPT_Upload_v14.3/
cp execution_orchestrator_v14.py ChatGPT_Upload_v14.3/
cp fusion_context.py ChatGPT_Upload_v14.3/
cp memory_system.py ChatGPT_Upload_v14.3/
cp patterns/pattern_registry.py ChatGPT_Upload_v14.3/
cp .fusion.json ChatGPT_Upload_v14.3/config.json

echo "✅ Files prepared in ChatGPT_Upload_v14.3"
open ChatGPT_Upload_v14.3
