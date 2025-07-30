#!/bin/bash

# === Auto-Sync Script ===
# This script automatically syncs ChatGPT files when you push to GitHub

echo "🤖 Auto-Sync: Updating ChatGPT files..."

# Update ChatGPT_Upload_v14.3 with latest files
~/fusion/chatgpt_sync.command

# Optional: Auto-upload to ChatGPT (if you have API access)
# This would require ChatGPT API integration

echo "✅ Auto-sync complete! ChatGPT files are now up-to-date."
echo "📁 Files ready at: ~/fusion/ChatGPT_Upload_v14.3/"
echo "🎯 Upload these files to ChatGPT for latest version" 