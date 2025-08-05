#!/bin/bash

# Fusion v14 Portable Installer
# Drop this file into any Cursor project to enable Fusion v14

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Installing Fusion v14 to your Cursor project${NC}"
echo -e "${BLUE}============================================================${NC}"

# Get current directory
CURRENT_DIR=$(pwd)
FUSION_DIR="$CURRENT_DIR/fusion_v14"

echo -e "${BLUE}📍 Current directory: $CURRENT_DIR${NC}"
echo -e "${BLUE}📁 Installing to: $FUSION_DIR${NC}"

# Create fusion_v14 directory
if [ -d "$FUSION_DIR" ]; then
    echo -e "${YELLOW}⚠️  fusion_v14 directory already exists. Updating...${NC}"
    rm -rf "$FUSION_DIR"
fi

mkdir -p "$FUSION_DIR"
echo -e "${GREEN}✅ Created fusion_v14 directory${NC}"

# Copy all Fusion v14 files from the source
SOURCE_DIR="/Users/soheil/Desktop/Fusion_v14"

if [ ! -d "$SOURCE_DIR" ]; then
    echo -e "${RED}❌ Error: Fusion v14 source directory not found at $SOURCE_DIR${NC}"
    echo "Please ensure Fusion v14 is properly installed on your system."
    exit 1
fi

echo -e "${BLUE}📦 Copying Fusion v14 files...${NC}"

# Copy essential directories and files
FILES_TO_COPY=(
    "agents"
    "core"
    "tools"
    "patterns"
    "analytics"
    "fusion.py"
    "master_prompt.md"
    "README.md"
    "VERSION.txt"
    ".fusion.json"
)

for ITEM in "${FILES_TO_COPY[@]}"
do
    if [ -e "$SOURCE_DIR/$ITEM" ]; then
        cp -R "$SOURCE_DIR/$ITEM" "$FUSION_DIR/"
        echo -e "${GREEN}✅ Copied $ITEM${NC}"
    else
        echo -e "${YELLOW}⚠️  $ITEM not found in source, skipping...${NC}"
    fi
done

# Create ChatGPT_10_Files package
echo -e "${BLUE}📦 Creating ChatGPT upload package...${NC}"
CHATGPT_DIR="$FUSION_DIR/ChatGPT_10_Files"
mkdir -p "$CHATGPT_DIR"

# Copy ChatGPT-optimized files
CHATGPT_FILES=(
    "fusion.py"
    "master_prompt.md"
    "README.md"
    "VERSION.txt"
    "agents_combined.py"
    "memory_system.py"
    "tools_combined.py"
    "README_10_FILES.md"
)

for ITEM in "${CHATGPT_FILES[@]}"
do
    if [ -e "$SOURCE_DIR/ChatGPT_10_Files/$ITEM" ]; then
        cp "$SOURCE_DIR/ChatGPT_10_Files/$ITEM" "$CHATGPT_DIR/"
        echo -e "${GREEN}✅ Copied ChatGPT $ITEM${NC}"
    else
        echo -e "${YELLOW}⚠️  ChatGPT $ITEM not found, skipping...${NC}"
    fi
done

# Copy core and tools directories for ChatGPT package
if [ -d "$SOURCE_DIR/ChatGPT_10_Files/core" ]; then
    cp -R "$SOURCE_DIR/ChatGPT_10_Files/core" "$CHATGPT_DIR/"
    echo -e "${GREEN}✅ Copied ChatGPT core directory${NC}"
fi

if [ -d "$SOURCE_DIR/ChatGPT_10_Files/tools" ]; then
    cp -R "$SOURCE_DIR/ChatGPT_10_Files/tools" "$CHATGPT_DIR/"
    echo -e "${GREEN}✅ Copied ChatGPT tools directory${NC}"
fi

# Create a portable launcher for this project
cat > "$FUSION_DIR/fusion_launch.command" << 'EOF'
#!/bin/bash

# Fusion v14 Launcher for this project
cd "$(dirname "$0")"

echo "🚀 Launching Fusion v14..."
echo "📁 Project: $(pwd)"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not installed"
    exit 1
fi

# Run Fusion v14
python3 fusion.py "$@"
EOF

chmod +x "$FUSION_DIR/fusion_launch.command"

# Create a quick test script
cat > "$FUSION_DIR/test_fusion.py" << 'EOF'
#!/usr/bin/env python3

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from fusion import main
    print("✅ Fusion v14 is ready!")
    print("🎯 Run: python3 fusion.py run vp_design 'Your design prompt'")
    print("🚀 Or double-click: fusion_launch.command")
except ImportError as e:
    print(f"❌ Error importing Fusion v14: {e}")
    print("Please ensure all files are properly copied.")
EOF

chmod +x "$FUSION_DIR/test_fusion.py"

echo ""
echo -e "${GREEN}🎉 Fusion v14 Installation Complete!${NC}"
echo -e "${BLUE}============================================================${NC}"
echo -e "${GREEN}✅ Installed in: $FUSION_DIR${NC}"
echo -e "${GREEN}✅ ChatGPT package: $CHATGPT_DIR${NC}"
echo ""
echo -e "${BLUE}🚀 Quick Start:${NC}"
echo -e "${GREEN}   cd $FUSION_DIR${NC}"
echo -e "${GREEN}   python3 fusion.py run vp_design 'Design a mobile app interface'${NC}"
echo -e "${GREEN}   python3 fusion.py run evaluator 'Evaluate this design proposal'${NC}"
echo ""
echo -e "${BLUE}🎯 Available Commands:${NC}"
echo -e "${GREEN}   python3 fusion.py run <agent> <input>${NC}"
echo -e "${GREEN}   python3 fusion.py pipeline <input>${NC}"
echo -e "${GREEN}   python3 fusion.py pattern <input>${NC}"
echo -e "${GREEN}   python3 fusion.py status${NC}"
echo -e "${GREEN}   python3 fusion.py help${NC}"
echo ""
echo -e "${BLUE}📦 ChatGPT Upload:${NC}"
echo -e "${GREEN}   Upload the entire $CHATGPT_DIR folder to ChatGPT${NC}"
echo -e "${GREEN}   Contains 10 optimized files for ChatGPT limits${NC}"
echo ""
echo -e "${BLUE}🎨 Available Agents:${NC}"
echo -e "${GREEN}   - vp_design: Design analysis and recommendations${NC}"
echo -e "${GREEN}   - evaluator: Comprehensive evaluation and scoring${NC}"
echo -e "${GREEN}   - creative_director: Creative strategy and direction${NC}"
echo -e "${GREEN}   - prompt_master: Pattern matching and optimization${NC}"
echo ""
echo -e "${BLUE}🛠️  Available Tools:${NC}"
echo -e "${GREEN}   - UX Audit Tool: Heuristic evaluation and metrics${NC}"
echo -e "${GREEN}   - Trust Explainer Tool: Trust-building analysis${NC}"
echo ""
echo -e "${BLUE}🧠 Features:${NC}"
echo -e "${GREEN}   - 24 specialized agents${NC}"
echo -e "${GREEN}   - Memory management and pattern recognition${NC}"
echo -e "${GREEN}   - Confidence-based fallback mechanisms${NC}"
echo -e "${GREEN}   - Comprehensive evaluation and scoring${NC}"
echo -e "${GREEN}   - Design analysis and recommendations${NC}"
echo ""
echo -e "${GREEN}🎉 Your Cursor project is now Fusion v14 enabled!${NC}" 