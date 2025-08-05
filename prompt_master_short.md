# Fusion v15 - AI Agentic Operating System

## 🚀 Quick Start

Fusion v15 is a complete AI agentic operating system with 32 specialized agents, memory, telemetry, and real-time GUI.

### Core Features
- **32 Specialized AI Agents** - Complete agent ecosystem
- **Persistent Memory System** - Agents remember and learn
- **Real-time Telemetry** - Track performance and usage
- **Multi-Agent Orchestration** - Run agents in parallel
- **RESTful API** - Full programmatic access
- **Beautiful Web GUI** - Real-time dashboard and control

### Installation
```bash
pip install -e .
```

### Launch
```bash
# API Server
python fusion_api.py

# Web GUI
streamlit run web_app.py

# CLI
python fusion.py run vp_design "Design a mobile app"
```

## 🎯 32 Specialized Agents

### Core Design Agents
- `vp_design` - VP of Design leadership
- `creative_director` - Creative direction and vision
- `principal_designer` - Principal design architect
- `design_system_engineer` - Design system specialist
- `component_librarian` - Component management

### AI & Interaction Agents
- `ai_native_ux_designer` - AI-native UX design
- `ai_interaction_designer` - AI-human interaction design
- `prompt_architect` - Advanced prompt engineering
- `prompt_master` - Prompt optimization

### Evaluation & Quality Agents
- `evaluator` - Quality assessment and critique
- `design_judgment_engine` - Design judgment analysis
- `design_polish_agent` - Design refinement
- `structural_clarity_checker` - Structural analysis
- `surprisal_critic` - Novelty and surprise evaluation

### Narrative & Content Agents
- `narrative_divergence` - Narrative divergence analysis
- `narrative_freshness_rater` - Content freshness evaluation
- `narrative_quality_chain` - Content quality pipeline
- `voice_match_evaluator` - Voice and tone matching
- `content_designer` - Content strategy
- `deck_narrator` - Presentation design

### Product & Strategy Agents
- `vp_of_product` - Product strategy leadership
- `product_navigator` - Product navigation
- `strategy_pilot` - Strategic execution
- `market_analyst` - Market intelligence
- `product_historian` - Product evolution tracking

### Workflow & Process Agents
- `workflow_optimizer` - Process optimization
- `dispatcher` - Agent routing and coordination
- `feedback_amplifier` - Feedback processing
- `research_summarizer` - Research synthesis

### Creative Chain Agents
- `longform_creative_chain` - Long-form content creation
- `rewrite_advisor` - Content rewriting guidance
- `rewrite_loop` - Iterative content improvement

## 📡 API Reference

### Core Endpoints
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
```

## 🧠 Memory System

### Agent Memory
```python
from fusion_core.memory.agent_memory import AgentMemory

memory = AgentMemory("vp_design")
memory.append("Design a mobile app", "Created wireframes...")
context = memory.get_context()  # Recent interactions
```

### Thread Memory
```python
from fusion_core.memory.thread_memory import ThreadMemory

thread = ThreadMemory("user123", "project456")
thread.append("User request", "Agent response")
thread.append("Follow-up", "Updated response")
```

## 📊 Telemetry System

### Real-time Metrics
- Agent execution times
- Confidence scores
- Fallback rates
- Success rates
- Token usage

### Export Capabilities
```python
from fusion_core.telemetry.agent_telemetry import AgentTelemetryLogger

telemetry = AgentTelemetryLogger()
telemetry.log_event("vp_design", "input", "output", confidence=0.95)
telemetry.export_to_csv("session_data.csv")
```

## 🔧 Configuration

### Agent Manifest
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

## 🐳 Docker Deployment

```dockerfile
FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "fusion_api:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🔮 Future Roadmap

### v15.1: Reflection Agent
- Self-review capabilities
- Confidence-based retry logic
- Automatic quality assessment

### v15.2: PatternRefiner Agent
- Telemetry-based optimization
- Automatic configuration updates
- Performance pattern analysis

### v15.3: Plugin Mode
- External agent registration
- Dynamic plugin loading
- Community agent ecosystem

### v15.4: Conversational Threads
- Cross-session memory
- Persistent conversations
- Intelligent context reuse

### v16.0: Team UI for Operators
- Real-time agent management
- Live telemetry dashboard
- Visual workflow builder

## 🤝 Contributing

### Adding New Agents
1. Create agent file in `agents/`
2. Inherit from base agent class
3. Implement `run()` method
4. Add to `agent_manifest.json`
5. Test with `python fusion.py run your_agent "test input"`

### Plugin System
```python
from fusion_plugin_registry import register_agent

class MyCustomAgent:
    async def run(self, input_text):
        return "Custom agent output"

register_agent(MyCustomAgent)
```

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

**Fusion v15** - Where AI agents work together seamlessly ✨

*Ready to revolutionize your AI workflows? Get started with Fusion v15 today!* 