# 🤖 Fusion v15 - AI Agentic Operating System

> **The most advanced AI agent orchestration system with memory, telemetry, and real-time GUI**

[![Fusion v15](https://img.shields.io/badge/Fusion-v15.0.0-blue.svg)](https://github.com/yourorg/fusion)
[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 **What's New in v15**

### ✨ **Core Features**
- **32 Specialized AI Agents** - Complete agent ecosystem
- **Persistent Memory System** - Agents remember and learn
- **Real-time Telemetry** - Track performance and usage
- **Multi-Agent Orchestration** - Run agents in parallel
- **RESTful API** - Full programmatic access
- **Beautiful Web GUI** - Real-time dashboard and control

### 🧠 **Agent Memory System**
```python
from fusion_core.memory.agent_memory import AgentMemory

memory = AgentMemory("vp_design")
memory.append("Design a mobile app", "Created wireframes...")
context = memory.get_context()  # Recent interactions
```

### 📊 **Telemetry & Analytics**
```python
from fusion_core.telemetry.agent_telemetry import AgentTelemetryLogger

telemetry = AgentTelemetryLogger()
telemetry.log_event("vp_design", "input", "output", confidence=0.95)
stats = telemetry.get_session_stats()
```

### ⚡ **Multi-Agent Orchestration**
```python
from fusion_core.orchestration.multi_agent_orchestrator import MultiAgentOrchestrator

orchestrator = MultiAgentOrchestrator(agents)
result = await orchestrator.run_parallel("Design a website", ["vp_design", "creative_director"])
```

## 🛠 **Quick Start**

### 1. **Installation**

```bash
# Clone the repository
git clone https://github.com/yourorg/fusion.git
cd fusion

# Install dependencies
pip install -e .

# Or install directly
pip install fusion-os
```

### 2. **Run the API Server**

```bash
# Start the Fusion API
python fusion_api.py

# API will be available at http://localhost:8000
```

### 3. **Launch the Web GUI**

```bash
# Start the Streamlit interface
streamlit run web_app.py

# GUI will be available at http://localhost:8501
```

### 4. **Use the CLI**

```bash
# Run a single agent
python fusion.py run vp_design "Design a mobile app interface"

# Run the full pipeline
python fusion.py pipeline "Create a complete design system"
```

## 🎯 **32 Specialized Agents**

### **Core Design Agents**
- `vp_design` - VP of Design leadership
- `creative_director` - Creative direction and vision
- `principal_designer` - Principal design architect
- `design_system_engineer` - Design system specialist
- `component_librarian` - Component management

### **AI & Interaction Agents**
- `ai_native_ux_designer` - AI-native UX design
- `ai_interaction_designer` - AI-human interaction design
- `prompt_architect` - Advanced prompt engineering
- `prompt_master` - Prompt optimization

### **Evaluation & Quality Agents**
- `evaluator` - Quality assessment and critique
- `design_judgment_engine` - Design judgment analysis
- `design_polish_agent` - Design refinement
- `structural_clarity_checker` - Structural analysis
- `surprisal_critic` - Novelty and surprise evaluation

### **Narrative & Content Agents**
- `narrative_divergence` - Narrative divergence analysis
- `narrative_freshness_rater` - Content freshness evaluation
- `narrative_quality_chain` - Content quality pipeline
- `voice_match_evaluator` - Voice and tone matching
- `content_designer` - Content strategy
- `deck_narrator` - Presentation design

### **Product & Strategy Agents**
- `vp_of_product` - Product strategy leadership
- `product_navigator` - Product navigation
- `strategy_pilot` - Strategic execution
- `market_analyst` - Market intelligence
- `product_historian` - Product evolution tracking

### **Workflow & Process Agents**
- `workflow_optimizer` - Process optimization
- `dispatcher` - Agent routing and coordination
- `feedback_amplifier` - Feedback processing
- `research_summarizer` - Research synthesis

### **Creative Chain Agents**
- `longform_creative_chain` - Long-form content creation
- `rewrite_advisor` - Content rewriting guidance
- `rewrite_loop` - Iterative content improvement

## 📡 **API Reference**

### **Core Endpoints**

```bash
# Get system status
GET /status

# List all agents
GET /agents

# Run single agent
POST /run
{
  "agent": "vp_design",
  "input": "Design a mobile app",
  "use_memory": true,
  "use_telemetry": true
}

# Run multiple agents in parallel
POST /run_parallel
{
  "agents": ["vp_design", "creative_director"],
  "input": "Create a design system",
  "use_evaluator": true
}

# Get agent memory
GET /memory/{agent_name}

# Get telemetry data
GET /telemetry
```

### **Python Client Example**

```python
import requests

# Run an agent
response = requests.post("http://localhost:8000/run", json={
    "agent": "vp_design",
    "input": "Design a mobile app interface"
})

result = response.json()
print(f"Agent: {result['agent']}")
print(f"Output: {result['output']}")
print(f"Confidence: {result['confidence']}")
```

## 🎨 **Web GUI Features**

### **Real-time Dashboard**
- Live agent status and performance
- Real-time telemetry visualization
- Agent usage statistics
- Session analytics

### **Agent Runner**
- Dropdown selection for all 32 agents
- Input prompt interface
- Real-time execution feedback
- Agent output display

### **Telemetry Explorer**
- Session statistics
- Agent performance metrics
- Export capabilities (JSON/CSV)
- Historical data analysis

### **Memory Browser**
- Agent interaction history
- Context retrieval
- Memory search functionality
- Success rate tracking

## 🧠 **Memory System**

### **Agent Memory**
Each agent maintains persistent memory of interactions:

```python
# Agent remembers previous interactions
memory = AgentMemory("vp_design")
memory.append("Design mobile app", "Created wireframes...")
memory.append("Design website", "Built component library...")

# Retrieve recent context
context = memory.get_context()  # Last 5 interactions
```

### **Thread Memory**
Persistent conversations across sessions:

```python
# Thread-based memory
thread = ThreadMemory("user123", "project456")
thread.append("User request", "Agent response")
thread.append("Follow-up", "Updated response")
```

## 📊 **Telemetry System**

### **Real-time Metrics**
- Agent execution times
- Confidence scores
- Fallback rates
- Success rates
- Token usage

### **Session Analytics**
- Total events per session
- Agent usage patterns
- Performance trends
- Error tracking

### **Export Capabilities**
```python
# Export telemetry data
telemetry.export_to_csv("session_data.csv")
telemetry.export_to_json("session_data.json")
```

## 🔧 **Configuration**

### **Agent Manifest**
```json
{
  "system_info": {
    "version": "v15.0.0",
    "description": "Fusion v15 Agent Manifest"
  },
  "agents": {
    "vp_design": {
      "role": "Design Lead",
      "capabilities": ["wireframe", "critique", "strategy"],
      "memory_enabled": true,
      "telemetry_enabled": true,
      "confidence_threshold": 0.8
    }
  }
}
```

### **Environment Variables**
```bash
# API Configuration
FUSION_API_HOST=0.0.0.0
FUSION_API_PORT=8000

# Memory Configuration
FUSION_MEMORY_DIR=fusion_memory
FUSION_TELEMETRY_DIR=fusion_telemetry

# Agent Configuration
FUSION_AGENT_TIMEOUT=30
FUSION_MAX_PARALLEL_AGENTS=10
```

## 🐳 **Docker Deployment**

```dockerfile
FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "fusion_api:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# Build and run
docker build -t fusion-v15 .
docker run -p 8000:8000 fusion-v15
```

## 🧪 **Testing**

### **Unit Tests**
```bash
# Run all tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_agents.py
```

### **Integration Tests**
```bash
# Test API endpoints
python -m pytest tests/test_api.py

# Test web interface
python -m pytest tests/test_web.py
```

## 📈 **Performance**

### **Benchmarks**
- **Agent Loading**: ~2.3s for all 32 agents
- **Memory Operations**: <100ms for context retrieval
- **Telemetry Logging**: <50ms per event
- **Parallel Execution**: Up to 10 agents simultaneously

### **Scalability**
- **Memory**: Persistent disk storage with configurable retention
- **Telemetry**: Session-based with export capabilities
- **API**: RESTful with async support
- **GUI**: Real-time updates with WebSocket support

## 🤝 **Contributing**

### **Adding New Agents**
1. Create agent file in `agents/`
2. Inherit from base agent class
3. Implement `run()` method
4. Add to `agent_manifest.json`
5. Test with `python fusion.py run your_agent "test input"`

### **Plugin System**
```python
# Register external agent
from fusion_plugin_registry import register_agent

class MyCustomAgent:
    async def run(self, input_text):
        return "Custom agent output"

register_agent(MyCustomAgent)
```

## 📄 **License**

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 **Acknowledgments**

- Built with ❤️ using Python 3.8+
- Powered by 32 specialized AI agents
- Real-time telemetry and memory systems
- Beautiful web interface with Streamlit

---

**Fusion v15** - Where AI agents work together seamlessly ✨

*Ready to revolutionize your AI workflows? Get started with Fusion v15 today!* 