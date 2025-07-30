#!/bin/bash

# === ChatGPT GitHub Sync Script ===
# Automatically syncs ChatGPT with latest GitHub updates

echo "🔄 ChatGPT GitHub Sync Script"
echo "================================"

# Check if we're in the right directory
if [ ! -f "fusion.py" ]; then
    echo "❌ Error: Run this script from the fusion directory"
    exit 1
fi

# Step 1: Pull latest changes from GitHub
echo "📥 Pulling latest changes from GitHub..."
git pull origin main

# Step 2: Update ChatGPT_Upload folder
echo "📦 Updating ChatGPT_Upload folder..."
./fusion_push.command

# Step 3: Show sync status
echo ""
echo "✅ Sync Complete!"
echo "📁 GitHub Repo: https://github.com/soheiloliaei/Fusion.git"
echo "📁 Local Files: ~/Desktop/fusion/ChatGPT_Upload/"
echo ""
echo "🎯 For ChatGPT:"
echo "1. Link: https://github.com/soheiloliaei/Fusion.git"
echo "2. Upload: ~/Desktop/fusion/ChatGPT_Upload/ (for optimized files)"
echo ""
echo "📝 Usage:"
echo "   ./chatgpt_sync.command  # Run this after any GitHub updates" 