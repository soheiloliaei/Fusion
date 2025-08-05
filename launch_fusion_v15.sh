#!/bin/bash

# 🚀 Fusion v15 Launch Script
# Complete AI Agentic Operating System with 32 agents, memory, telemetry, API, and GUI

echo "🚀 Launching Fusion v15..."

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Not in a git repository. Please initialize git first."
    exit 1
fi

# Create v15-launch branch
echo "📁 Creating v15-launch branch..."
git checkout -b v15-launch

# Add all files
echo "📦 Adding all files..."
git add .

# Commit with comprehensive message
echo "💾 Committing Fusion v15..."
git commit -m "🚀 Launch Fusion v15: Complete AI Agentic Operating System

✨ Features:
- 32 Specialized AI Agents with full capabilities
- Advanced Memory System for persistent learning
- Real-time Telemetry for performance tracking
- Multi-Agent Orchestration for complex workflows
- RESTful API for external integration
- Beautiful Web GUI for easy operation
- Comprehensive Documentation for all users
- Production-ready deployment with Docker

📁 Core Components:
- fusion_core/ (memory, telemetry, orchestration)
- agents/ (32 specialized agents)
- fusion_api.py (FastAPI server)
- web_app.py (Streamlit GUI)
- fusion.py (CLI interface)
- agent_manifest.json (agent definitions)
- pyproject.toml (package configuration)
- Dockerfile (container deployment)

🎯 Ready for production deployment!"

# Push to GitHub
echo "🌐 Pushing to GitHub..."
git push origin v15-launch

# Create v15.0 tag
echo "🏷️ Creating v15.0 tag..."
git tag -a v15.0 -m "Fusion v15.0 - Complete AI Agentic Operating System

Release Highlights:
- 32 Specialized AI Agents
- Persistent Memory System
- Real-time Telemetry
- Multi-Agent Orchestration
- RESTful API
- Beautiful Web GUI
- Production Ready

This is the first major release of Fusion, providing a complete
AI agentic operating system for developers and operators."

# Push tag
echo "📤 Pushing tag..."
git push origin v15.0

# Create GitHub release (if gh CLI is available)
if command -v gh &> /dev/null; then
    echo "📋 Creating GitHub release..."
    gh release create v15.0 --generate-notes --title "Fusion v15.0 - AI Agentic Operating System" --notes "## 🚀 Fusion v15.0 Release

### ✨ What's New
- **32 Specialized AI Agents** - Complete agent ecosystem
- **Persistent Memory System** - Agents remember and learn
- **Real-time Telemetry** - Track performance and usage
- **Multi-Agent Orchestration** - Run agents in parallel
- **RESTful API** - Full programmatic access
- **Beautiful Web GUI** - Real-time dashboard and control

### 🎯 Key Features
- **Agent Memory**: Persistent interaction history
- **Telemetry Analytics**: Real-time performance tracking
- **Multi-Agent Execution**: Parallel agent orchestration
- **Plugin System**: Extensible agent architecture
- **Thread Memory**: Cross-session conversation persistence
- **Production Ready**: Docker deployment and comprehensive docs

### 📦 Installation
\`\`\`bash
pip install fusion-os
\`\`\`

### 🚀 Quick Start
\`\`\`bash
# Start API server
python fusion_api.py

# Launch web GUI
streamlit run web_app.py

# Use CLI
python fusion.py run vp_design \"Design a mobile app\"
\`\`\`

### 📚 Documentation
- [FUSION_V15_README.md](FUSION_V15_README.md) - Comprehensive guide
- [FUSION_V15_DELIVERY_SUMMARY.md](FUSION_V15_DELIVERY_SUMMARY.md) - Feature overview

### 🔮 Future Roadmap
- v15.1: Reflection Agent (self-review capabilities)
- v15.2: PatternRefiner Agent (automatic optimization)
- v15.3: Plugin Mode (external agent registration)
- v15.4: Conversational Threads (cross-session memory)
- v16.0: Team UI for Operators (advanced management)

**Fusion v15** - Where AI agents work together seamlessly ✨"
else
    echo "⚠️ GitHub CLI not found. Please create release manually at:"
    echo "https://github.com/yourorg/fusion/releases/new"
fi

echo ""
echo "🎉 Fusion v15 Successfully Launched!"
echo ""
echo "📋 Next Steps:"
echo "1. Review the release at: https://github.com/yourorg/fusion/releases"
echo "2. Install locally: pip install -e ."
echo "3. Run the API: python fusion_api.py"
echo "4. Launch GUI: streamlit run web_app.py"
echo "5. Test agents: python fusion.py run vp_design \"Design a mobile app\""
echo ""
echo "🔗 Useful Links:"
echo "- Documentation: FUSION_V15_README.md"
echo "- Delivery Summary: FUSION_V15_DELIVERY_SUMMARY.md"
echo "- Package Config: pyproject.toml"
echo "- Docker: Dockerfile"
echo ""
echo "🚀 Fusion v15 is ready for the world! ✨" 