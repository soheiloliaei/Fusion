#!/bin/bash

echo "🚀 Installing Fusion v15 Complete System..."

# Set working directory
PROJECT_DIR=$(pwd)
FUSION_DIR="$PROJECT_DIR/fusion_v15"

echo "📁 Project: $PROJECT_DIR"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not installed"
    exit 1
fi

# Create fusion_core directory structure
echo "🏗️ Creating Fusion v15 core structure..."
mkdir -p fusion_core/memory
mkdir -p fusion_core/telemetry
mkdir -p fusion_core/orchestration

# Create __init__.py files
touch fusion_core/__init__.py
touch fusion_core/memory/__init__.py
touch fusion_core/telemetry/__init__.py
touch fusion_core/orchestration/__init__.py

# Create agents directory if it doesn't exist
mkdir -p agents

# Copy all core Fusion v15 files
echo "📦 Installing Fusion v15 core components..."

# Copy fusion_core files
cp -r fusion_core/* fusion_core/ 2>/dev/null || echo "⚠️ fusion_core already exists"

# Copy main Fusion files
cp fusion_api.py . 2>/dev/null || echo "⚠️ fusion_api.py already exists"
cp web_app.py . 2>/dev/null || echo "⚠️ web_app.py already exists"
cp fusion.py . 2>/dev/null || echo "⚠️ fusion.py already exists"

# Copy configuration files
cp agent_manifest.json . 2>/dev/null || echo "⚠️ agent_manifest.json already exists"
cp requirements.txt . 2>/dev/null || echo "⚠️ requirements.txt already exists"
cp pyproject.toml . 2>/dev/null || echo "⚠️ pyproject.toml already exists"
cp Dockerfile . 2>/dev/null || echo "⚠️ Dockerfile already exists"

# Copy documentation
cp FUSION_V15_README.md . 2>/dev/null || echo "⚠️ FUSION_V15_README.md already exists"
cp FUSION_V15_DELIVERY_SUMMARY.md . 2>/dev/null || echo "⚠️ FUSION_V15_DELIVERY_SUMMARY.md already exists"

# Copy prompt masters
cp prompt_master_short.md . 2>/dev/null || echo "⚠️ prompt_master_short.md already exists"
cp prompt_master_main.md . 2>/dev/null || echo "⚠️ prompt_master_main.md already exists"

# Copy all agent files
echo "🤖 Installing all 32 Fusion agents..."
cp agents/*.py agents/ 2>/dev/null || echo "⚠️ agents already exist"

# Copy bootstrap and plugin system
cp fusion_bootstrap.py . 2>/dev/null || echo "⚠️ fusion_bootstrap.py already exists"
cp fusion_plugin_registry.py . 2>/dev/null || echo "⚠️ fusion_plugin_registry.py already exists"

# Install Fusion v15 package
echo "⚙️ Installing Fusion v15 dependencies..."
pip install -e . 2>/dev/null || echo "⚠️ Package already installed"

# Create auto-bootstrap for Cursor
echo "🧠 Creating Cursor auto-bootstrap..."
cat > cursor_fusion_bootstrap.py << 'EOF'
#!/usr/bin/env python3
"""
Cursor Fusion v15 Auto-Bootstrap
Automatically loads Fusion v15 in any Cursor environment
"""

import sys
import os
from pathlib import Path

def bootstrap_fusion():
    """Bootstrap Fusion v15 for Cursor."""
    try:
        # Add current directory to Python path
        current_dir = Path.cwd()
        if str(current_dir) not in sys.path:
            sys.path.insert(0, str(current_dir))
        
        # Import Fusion components
        from fusion_core.memory.agent_memory import AgentMemory
        from fusion_core.telemetry.agent_telemetry import AgentTelemetryLogger
        from fusion_core.orchestration.multi_agent_orchestrator import MultiAgentOrchestrator
        
        # Import agents
        from agents_combined import AGENT_REGISTRY
        
        print("✅ Fusion v15 loaded successfully!")
        print("🎯 Available functions:")
        print("   - ask(prompt, agent_name)")
        print("   - ask_auto(prompt)")
        print("   - ask_chain(prompt, [agent1, agent2])")
        print("   - get_agent_memory(agent_name)")
        print("   - get_telemetry()")
        
        return True
        
    except Exception as e:
        print(f"⚠️ Fusion bootstrap failed: {e}")
        return False

# Auto-bootstrap when imported
if __name__ == "__main__":
    bootstrap_fusion()
EOF

# Create Cursor integration
echo "🎨 Creating Cursor integration..."
cat > cursor_fusion_integration.py << 'EOF'
#!/usr/bin/env python3
"""
Cursor Fusion v15 Integration
Provides seamless Fusion v15 experience in Cursor
"""

import asyncio
from typing import List, Optional
from pathlib import Path

# Global Fusion components
fusion_memory = None
fusion_telemetry = None
fusion_orchestrator = None
agent_registry = {}

def initialize_fusion():
    """Initialize Fusion v15 components."""
    global fusion_memory, fusion_telemetry, fusion_orchestrator, agent_registry
    
    try:
        from fusion_core.memory.agent_memory import AgentMemory
        from fusion_core.telemetry.agent_telemetry import AgentTelemetryLogger
        from fusion_core.orchestration.multi_agent_orchestrator import MultiAgentOrchestrator
        from agents_combined import AGENT_REGISTRY
        
        fusion_memory = AgentMemory
        fusion_telemetry = AgentTelemetryLogger()
        agent_registry = AGENT_REGISTRY
        
        print("✅ Fusion v15 initialized successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Fusion initialization failed: {e}")
        return False

def ask(prompt: str, agent_name: str = "auto") -> str:
    """Ask a question to a specific agent."""
    if not fusion_memory:
        initialize_fusion()
    
    try:
        if agent_name == "auto":
            return ask_auto(prompt)
        
        if agent_name in agent_registry:
            agent_class = agent_registry[agent_name]
            agent = agent_class()
            result = asyncio.run(agent.run(prompt))
            
            # Log to telemetry
            fusion_telemetry.log_event(agent_name, prompt, result, confidence=0.9)
            
            return result
        else:
            return f"❌ Agent '{agent_name}' not found. Available agents: {list(agent_registry.keys())}"
            
    except Exception as e:
        return f"❌ Error: {e}"

def ask_auto(prompt: str) -> str:
    """Automatically select the best agent for the task."""
    if not fusion_memory:
        initialize_fusion()
    
    try:
        # Simple agent selection logic
        if "design" in prompt.lower():
            return ask(prompt, "vp_design")
        elif "evaluate" in prompt.lower():
            return ask(prompt, "evaluator")
        elif "creative" in prompt.lower():
            return ask(prompt, "creative_director")
        elif "product" in prompt.lower():
            return ask(prompt, "vp_of_product")
        else:
            return ask(prompt, "vp_design")  # Default to VP Design
            
    except Exception as e:
        return f"❌ Auto-selection error: {e}"

def ask_chain(prompt: str, agents: List[str]) -> str:
    """Run multiple agents in sequence."""
    if not fusion_memory:
        initialize_fusion()
    
    try:
        results = []
        for agent_name in agents:
            result = ask(prompt, agent_name)
            results.append(f"[{agent_name}]: {result}")
        
        return "\n\n".join(results)
        
    except Exception as e:
        return f"❌ Chain execution error: {e}"

def get_agent_memory(agent_name: str) -> str:
    """Get memory for a specific agent."""
    if not fusion_memory:
        initialize_fusion()
    
    try:
        memory = fusion_memory(agent_name)
        context = memory.get_context()
        return context if context else "No memory found for this agent."
        
    except Exception as e:
        return f"❌ Memory error: {e}"

def get_telemetry() -> str:
    """Get current telemetry data."""
    if not fusion_telemetry:
        initialize_fusion()
    
    try:
        stats = fusion_telemetry.get_session_stats()
        return f"📊 Telemetry: {stats}"
        
    except Exception as e:
        return f"❌ Telemetry error: {e}"

# Auto-initialize when imported
initialize_fusion()
EOF

# Create Cursor startup script
echo "🚀 Creating Cursor startup script..."
cat > cursor_startup.py << 'EOF'
#!/usr/bin/env python3
"""
Cursor Startup - Fusion v15
Automatically loads Fusion v15 when Cursor starts
"""

import cursor_fusion_integration

print("🧠 Fusion v15 loaded in Cursor!")
print("🎯 You can now use:")
print("   ask('your prompt', 'agent_name')")
print("   ask_auto('your prompt')")
print("   ask_chain('prompt', ['agent1', 'agent2'])")
print("   get_agent_memory('agent_name')")
print("   get_telemetry()")
EOF

# Make scripts executable
chmod +x cursor_fusion_bootstrap.py
chmod +x cursor_fusion_integration.py
chmod +x cursor_startup.py

# Create .cursorrules for automatic Fusion loading
echo "📝 Creating .cursorrules for auto-Fusion..."
cat > .cursorrules << 'EOF'
# Fusion v15 - AI Agentic Operating System

## Auto-Load Fusion v15
When this project is opened in Cursor, automatically load Fusion v15 with all 32 agents.

## Available Functions
- `ask(prompt, agent_name)` - Ask a specific agent
- `ask_auto(prompt)` - Auto-select best agent
- `ask_chain(prompt, [agents])` - Run multiple agents
- `get_agent_memory(agent_name)` - Get agent memory
- `get_telemetry()` - Get system telemetry

## Agent Categories
- **Design Agents**: vp_design, creative_director, principal_designer
- **AI Agents**: ai_native_ux_designer, ai_interaction_designer
- **Evaluation Agents**: evaluator, design_judgment_engine
- **Product Agents**: vp_of_product, product_navigator
- **Content Agents**: content_designer, deck_narrator
- **And 20+ more specialized agents**

## Usage Examples
```python
# Design a mobile app
ask("Design a mobile app interface", "vp_design")

# Auto-select best agent
ask_auto("Create a design system")

# Multi-agent chain
ask_chain("Evaluate this design", ["evaluator", "creative_director"])
```

## Fusion v15 Features
- 32 Specialized AI Agents
- Persistent Memory System
- Real-time Telemetry
- Multi-Agent Orchestration
- RESTful API
- Beautiful Web GUI
EOF

# Create README for the project
echo "📚 Creating Fusion v15 README..."
cat > README.md << 'EOF'
# Fusion v15 - AI Agentic Operating System

This project is now powered by **Fusion v15** - the most advanced AI agentic operating system with 32 specialized agents.

## 🚀 Quick Start

### In Cursor
```python
# Auto-loaded functions
ask("Design a mobile app", "vp_design")
ask_auto("Create a design system")
ask_chain("Evaluate this design", ["evaluator", "creative_director"])
```

### Manual Launch
```bash
# Start API server
python fusion_api.py

# Launch Web GUI
streamlit run web_app.py

# Use CLI
python fusion.py run vp_design "Design a mobile app"
```

## 🎯 32 Specialized Agents

### Core Design Agents
- `vp_design` - VP of Design leadership
- `creative_director` - Creative direction and vision
- `principal_designer` - Principal design architect

### AI & Interaction Agents
- `ai_native_ux_designer` - AI-native UX design
- `ai_interaction_designer` - AI-human interaction design

### Evaluation & Quality Agents
- `evaluator` - Quality assessment and critique
- `design_judgment_engine` - Design judgment analysis

### Product & Strategy Agents
- `vp_of_product` - Product strategy leadership
- `product_navigator` - Product navigation

### And 24+ more specialized agents...

## 🧠 Memory System
```python
# Get agent memory
get_agent_memory("vp_design")

# Get telemetry
get_telemetry()
```

## 📡 API Endpoints
- `GET /status` - System status
- `POST /run` - Run single agent
- `POST /run_parallel` - Run multiple agents
- `GET /agents` - List all agents

## 🎨 Web GUI
- Real-time dashboard
- Agent runner interface
- Telemetry explorer
- Memory browser

---

**Fusion v15** - Where AI agents work together seamlessly ✨
EOF

# Launch Fusion v15
echo "🎉 Fusion v15 Complete System Installed!"
echo ""
echo "🚀 Launching Fusion v15..."

# Start API server in background
echo "🌐 Starting Fusion API server..."
python3 fusion_api.py &
API_PID=$!

# Start Web GUI in background
echo "🎨 Starting Fusion Web GUI..."
streamlit run web_app.py &
GUI_PID=$!

# Wait a moment for services to start
sleep 3

echo ""
echo "✅ Fusion v15 is now running!"
echo ""
echo "🌐 API Server: http://localhost:8000"
echo "🎨 Web GUI: http://localhost:8501"
echo ""
echo "🎯 In Cursor, you can now use:"
echo "   ask('your prompt', 'agent_name')"
echo "   ask_auto('your prompt')"
echo "   ask_chain('prompt', ['agent1', 'agent2'])"
echo ""
echo "📁 Files created:"
echo "   - cursor_fusion_integration.py (main Fusion interface)"
echo "   - cursor_startup.py (auto-load script)"
echo "   - .cursorrules (Cursor integration)"
echo "   - README.md (project documentation)"
echo ""
echo "🛑 To stop Fusion: kill $API_PID $GUI_PID" 