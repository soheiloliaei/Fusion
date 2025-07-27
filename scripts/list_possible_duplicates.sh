#!/bin/bash

# Fusion v13 Duplicate File Detection Script
# This script identifies potential duplicate files for safe cleanup

echo "🔍 FUSION V13 DUPLICATE FILE DETECTION"
echo "======================================"
echo ""

# Check if we're in the fusion_v13 directory
if [[ ! -d "~/fusion_v13" ]]; then
    echo "❌ Error: This script must be run from the fusion_v13 directory"
    exit 1
fi

echo "📁 Scanning for duplicate files..."
echo ""

# Find all files and generate MD5 hashes
find . -type f -exec md5sum {} + | sort | uniq -w32 -dD

echo ""
echo "✅ Duplicate detection complete."
echo "📋 Review the output above for potential duplicates."
echo "⚠️  DO NOT DELETE without explicit approval from Soheil."
