#!/bin/bash

# Fusion v14 SDK Installer
# This script installs Fusion v14 with all 22 agents

echo "🚀 Fusion v14 SDK Installer"
echo "================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not installed."
    echo "Please install Python 3 from https://python.org"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Check if the SDK archive exists
if [ ! -f "Fusion_v14_SDK.tar.gz" ]; then
    echo "❌ Error: Fusion_v14_SDK.tar.gz not found in current directory"
    echo "Please make sure the SDK file is in the same directory as this installer"
    exit 1
fi

echo "✅ SDK archive found"

# Create installation directory
INSTALL_DIR="$HOME/Fusion_v14"
echo "📁 Installing to: $INSTALL_DIR"

# Extract the SDK
echo "📦 Extracting Fusion v14 SDK..."
tar -xzf Fusion_v14_SDK.tar.gz

# Move to installation directory
if [ -d "$INSTALL_DIR" ]; then
    echo "⚠️  Installation directory already exists. Backing up..."
    mv "$INSTALL_DIR" "$INSTALL_DIR.backup.$(date +%Y%m%d_%H%M%S)"
fi

mv fusion_v14_portable "$INSTALL_DIR"
echo "✅ SDK extracted to $INSTALL_DIR"

# Make launcher executable
chmod +x "$INSTALL_DIR/Fusion_v14_Launcher.command"

# Create desktop shortcut
echo "🖥️  Creating desktop shortcut..."
cp "$INSTALL_DIR/Fusion_v14_Launcher.command" ~/Desktop/Fusion_v14_Launcher.command
chmod +x ~/Desktop/Fusion_v14_Launcher.command

# Test the installation
echo "🧪 Testing installation..."
cd "$INSTALL_DIR"
if python3 fusion.py run vp_design "Test installation" > /dev/null 2>&1; then
    echo "✅ Installation test successful!"
else
    echo "⚠️  Installation test failed, but SDK may still work"
fi

echo ""
echo "🎉 Fusion v14 SDK Installation Complete!"
echo "========================================"
echo ""
echo "📁 Installation location: $INSTALL_DIR"
echo "🖥️  Desktop shortcut: ~/Desktop/Fusion_v14_Launcher.command"
echo ""
echo "🚀 How to use:"
echo "1. Double-click Fusion_v14_Launcher.command on desktop"
echo "2. Or run: cd $INSTALL_DIR && ./Fusion_v14_Launcher.command"
echo "3. Or run agents: cd $INSTALL_DIR && python3 fusion.py run vp_design 'Your prompt'"
echo ""
echo "📊 Available: 22 agents across 5 categories"
echo "🎯 Ready to use: Design, Strategy, Evaluation, and more!"
echo ""
echo "Press any key to exit..."
read -n 1 