# Fusion v14 - AI-Native Operating System

Fusion v14 is a complete AI-Native Operating System — not just an orchestration system, but a programmable agent OS with full debugging, chaining, pattern testing, voice input, and web interface capabilities.

## 🚀 What's New in Fusion v14.3

### **Sprint 5-9 Complete: From Intelligence to OS**
- **🧪 Debug UI**: Complete synthetic reasoning visualization with `--debug` flag
- **🧵 Agent Choreographer**: Multi-agent chain execution with 5 predefined workflows
- **🧩 Pattern Testing**: Live fallback pattern effectiveness testing and comparison
- **🗣️ Voice Input**: Voice-to-text agent processing with risk detection
- **🛜 Web App**: Complete Streamlit interface with 5 pages for all functionality

### **All 31 Agents Working**
- **Core Design Agents (6)**: vp_design, creative_director, design_technologist, principal_designer, vp_of_design, vp_of_product
- **Strategy & Product Agents (4)**: product_navigator, strategy_pilot, product_historian, market_analyst
- **Content & Communication Agents (4)**: content_designer, deck_narrator, portfolio_editor, research_summarizer
- **Component & System Agents (3)**: component_librarian, ai_interaction_designer, workflow_optimizer
- **Intelligence & Orchestration Agents (4)**: evaluator, prompt_master, dispatcher, strategy_archivist
- **Feedback & Analysis Agents (1)**: feedback_amplifier
- **Advanced Combined Agents (9)**: surprisal_critic, narrative_divergence, rewrite_loop, prompt_architect, design_polish_agent, longform_creative_chain, narrative_freshness_rater, structural_clarity_checker, voice_match_evaluator, rewrite_advisor, narrative_quality_chain, autocritique_loop, design_judgment_engine, ai_native_ux_designer, design_system_engineer

### **Synthetic Reasoning Layer**
Every agent now includes:
- **5 Synthetic Thoughts** - Internal reflections and risk assessment
- **5 Internal Questions** - Self-interrogation before acting
- **Risk Score (0.0-1.0)** - Automatic risk assessment for fallback triggering

### **Pattern Override System**
- **6 Fallback Patterns** - Intelligent prompt override for high-risk scenarios
- **Risk-Based Routing** - Automatic pattern application when risk_score > 0.65
- **Pattern Effectiveness** - Live testing and scoring of pattern effectiveness

## 📁 Current Project Structure

```
Fusion_v14/
├── fusion.py                      # Main CLI runner with all commands
├── debug_ui.py                    # Debug visualization system
├── agent_choreographer.py         # Multi-agent chain execution
├── pattern_tester.py              # Pattern effectiveness testing
├── voice_input.py                 # Voice-to-text processing
├── web_app.py                     # Complete Streamlit web interface
├── start_web_app.py               # Web app launcher
├── test_web_app.py                # Component validation
├── agent_manifest.json            # All 31 agents documented
├── fallback_trigger_config.json   # Risk routing configuration
├── agent_chains.json              # Predefined agent chains
├── pattern_registry.py            # Fallback pattern templates
├── synthetic_reasoner_agent.py    # Meta-agent for introspection
├── .fusion.json                   # Configuration file
├── core/
│   ├── fusion_context.py          # Shared state + memory
│   └── execution_orchestrator_v14.py # Async orchestrator
├── agents/                        # 22 individual agent files
│   ├── vp_design_agent.py
│   ├── evaluator_agent.py
│   ├── creative_director_agent.py
│   └── ... (19 more agents)
├── agents_combined.py             # 9 additional combined agents
├── tools/
│   ├── ux_audit_tool.py           # UX critique tool
│   └── trust_explainer_tool.py    # Trust analysis tool
├── patterns/
│   └── pattern_registry.py        # Pattern management
├── web/
│   └── requirements.txt           # Web app dependencies
└── analytics/                     # Analytics and metrics
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Git repository (for auto-push functionality)
- Streamlit (optional, for web interface): `pip install streamlit`

### Quick Start
1. **Clone or navigate to the Fusion v14 directory**
   ```bash
   cd ~/fusion_v14
   ```

2. **Test all components**
   ```bash
   python3 test_web_app.py
   ```

3. **Run Fusion CLI**
   ```bash
   python3 fusion.py --help
   ```

4. **Start Web Interface** (if streamlit available)
   ```bash
   python3 start_web_app.py
   ```

## 🎯 Complete CLI Interface

### All Available Commands
```bash
# Individual agent execution with debug
python3 fusion.py --debug run vp_design "Design a mobile app interface"

# Multi-agent chain execution
python3 fusion.py chain design_pipeline "Design a new support tile for BTC"

# Pattern effectiveness testing
python3 fusion.py test-pattern evaluator fallback_metric_narrative "Test this design"

# Voice-to-text agent processing
python3 fusion.py voice strategy_pilot --method manual

# Legacy pipeline mode
python3 fusion.py pipeline "Create a user-friendly dashboard"

# Task classification
python3 fusion.py brief "I need to design a checkout flow"

# Design Intelligence Stack
python3 fusion.py design_chain "Create a landing page design"
python3 fusion.py tile_mode "Design a notification tile"
python3 fusion.py autocritique "Review this design proposal"
```

### Debug Mode Features
```bash
# Enable synthetic reasoning display
python3 fusion.py --debug run creative_director "Create a visual story"

# Output shows:
# 🧠 Synthetic Thoughts (5 items)
# ❓ Internal Questions (5 items) 
# ⚠️ Risk Score: 0.41
# 🔄 Fallback Pattern (if triggered)
```

### Agent Chain Execution
```bash
# Predefined chains available:
# - design_pipeline: vp_design → evaluator → rewrite_loop
# - narrative_loop: deck_narrator → surprisal_critic → rewrite_loop
# - strategy_chain: strategy_pilot → market_analyst → creative_director
# - content_flow: content_designer → voice_match_evaluator → rewrite_advisor
# - product_journey: product_navigator → user_experience_analyst → design_technologist

python3 fusion.py chain narrative_loop "Create a compelling story about our AI product"
```

### Pattern Testing
```bash
# Test effectiveness of fallback patterns:
# - fallback_clarify_then_critique
# - fallback_metric_narrative  
# - fallback_soften_for_exec
# - fallback_safe_design
# - fallback_user_centric
# - fallback_systematic

python3 fusion.py test-pattern rewrite_loop fallback_clarify_then_critique "Improve this design"
```

### Voice Input
```bash
# Voice input methods:
# - whisper (OpenAI Whisper, if available)
# - speech_recognition (Google Speech Recognition, if available)  
# - manual (text input fallback, always available)
# - auto (automatic method selection)

python3 fusion.py voice vp_design --method auto --duration 10
```

## 🌐 Web Application

### Starting the Web App
```bash
python3 start_web_app.py
# Opens at http://localhost:8501
```

### Web App Pages
1. **🚀 Run Agent** - Individual agent execution with debug visualization
2. **🔗 Agent Chains** - Chain selection and multi-agent execution  
3. **🧩 Pattern Testing** - Live pattern effectiveness testing
4. **🎤 Voice Input** - Voice-to-agent processing interface
5. **⚙️ Configuration** - Live config editing and debug analytics

### Web App Features
- **Agent Selection** - All 31 agents available via dropdown
- **Debug Toggle** - Real-time synthetic reasoning display
- **Chain Execution** - Visual progress through multi-agent workflows
- **Pattern Comparison** - Side-by-side normal vs pattern execution
- **Live Configuration** - Edit fallback configs and view debug logs
- **Session Analytics** - Real-time usage statistics and effectiveness metrics

## 🤖 Synthetic Reasoning System

### How It Works
Every agent now runs through a **SyntheticReasonerAgent** that provides:

```python
# Example synthetic reasoning output:
{
  "synthetic_thoughts": [
    "The user might expect both critique and rewrite.",
    "It's unclear whether Tailwind or Markdown output is preferred.", 
    "This may trigger fallback pattern if confidence is low.",
    "The input lacks specific context about target audience.",
    "Need to clarify if this is for internal or external stakeholders."
  ],
  "synthetic_queries": [
    "Should I use the Executive Rewriter pattern?",
    "Is the user expecting structured output?", 
    "Should this pass through RewriteLoopAgent after critique?",
    "What level of detail is appropriate for this request?",
    "Are there any sensitive aspects I should avoid?"
  ],
  "risk_score": 0.41
}
```

### Risk-Based Fallback
- **Risk Threshold**: 0.65 (configurable)
- **Automatic Pattern Override**: When risk_score > threshold
- **6 Fallback Patterns**: Different strategies for high-risk scenarios
- **Pattern Effectiveness Tracking**: Automatic scoring and analytics

## 🧵 Agent Choreographer

### Predefined Chains
```json
{
  "design_pipeline": ["vp_design", "evaluator", "rewrite_loop"],
  "narrative_loop": ["deck_narrator", "surprisal_critic", "rewrite_loop"], 
  "strategy_chain": ["strategy_pilot", "market_analyst", "creative_director"],
  "content_flow": ["content_designer", "voice_match_evaluator", "rewrite_advisor"],
  "product_journey": ["product_navigator", "user_experience_analyst", "design_technologist"]
}
```

### Chain Features
- **Sequential Execution** - Output of each agent becomes input to next
- **Synthetic Meta Preservation** - Risk scoring maintained across chain
- **High-Risk Stopping** - Automatic halt if risk_score > 0.9
- **Execution Analytics** - Duration, success rate, step completion tracking
- **JSON Output** - Complete results with metadata for each step

## 🧩 Pattern Testing System

### Available Patterns
- **fallback_clarify_then_critique** - "First clarify ambiguous terms. Then critique step-by-step."
- **fallback_metric_narrative** - "Evaluate using: clarity, hierarchy, tone, accessibility. Then explain."
- **fallback_soften_for_exec** - "Rewrite to be executive-friendly and strategic in tone."
- **fallback_safe_design** - "Propose only minimal, conservative improvements to avoid unintended harm."
- **fallback_user_centric** - "Focus on user needs and accessibility in all recommendations."
- **fallback_systematic** - "Use systematic methodology with clear steps and reasoning."

### Pattern Testing Features
- **A/B Comparison** - Normal execution vs pattern override
- **Effectiveness Scoring** - 0.0-1.0 effectiveness rating
- **Risk Impact Analysis** - Before/after risk score comparison
- **Output Change Detection** - Automatic similarity analysis
- **Session Analytics** - Pattern performance tracking across tests

## 🗣️ Voice Input System

### Voice Processing Pipeline
1. **Audio Capture** - Record voice input (or manual text fallback)
2. **Transcription** - Convert to text via Whisper or Speech Recognition
3. **Risk Assessment** - Run through synthetic reasoning
4. **High-Risk Confirmation** - User confirmation for risk_score > 0.8
5. **Agent Processing** - Full agent execution with voice input
6. **Session Logging** - Complete voice session tracking

### Voice Input Methods
- **Whisper** - OpenAI Whisper integration (best quality)
- **Speech Recognition** - Google Speech Recognition (fallback)
- **Manual** - Text input (always available)
- **Auto** - Automatic method selection based on availability

## 🔧 Configuration Files

### Agent Manifest (`agent_manifest.json`)
Documents all 31 agents with roles and fallback patterns:
```json
{
  "vp_design": {
    "role": "VP Design Agent – high-level UI evaluator and recommender",
    "fallback_pattern": "fallback_clarify_then_critique"
  },
  "creative_director": {
    "role": "Owns visual and narrative direction for design outputs", 
    "fallback_pattern": "fallback_soften_for_exec"
  }
  // ... 29 more agents
}
```

### Fallback Configuration (`fallback_trigger_config.json`)
```json
{
  "risk_threshold": 0.65,
  "default_fallback_agent": "rewrite_loop",
  "pattern_routing": {
    "vp_design": "fallback_clarify_then_critique",
    "creative_director": "fallback_soften_for_exec",
    "evaluator": "fallback_metric_narrative"
    // ... mappings for all 31 agents
  }
}
```

### Agent Chains (`agent_chains.json`)
```json
{
  "design_pipeline": ["vp_design", "evaluator", "rewrite_loop"],
  "narrative_loop": ["deck_narrator", "surprisal_critic", "rewrite_loop"],
  // ... 3 more predefined chains
}
```

## 📊 System Analytics

### Debug Analytics
- **Total Runs** - Number of agent executions
- **Average Risk** - Mean risk score across sessions
- **Patterns Triggered** - Fallback pattern activation count
- **Agents Used** - Distribution of agent usage
- **Session Tracking** - Complete execution logs

### Chain Analytics  
- **Execution Duration** - Time per chain and per step
- **Success Rate** - Percentage of successful chain completions
- **Step Completion** - Individual agent success within chains
- **Error Tracking** - Failed steps and error patterns

### Pattern Analytics
- **Effectiveness Scores** - Pattern performance ratings
- **Risk Reduction** - Impact on risk scores
- **Output Changes** - Degree of modification caused by patterns
- **Usage Distribution** - Most/least effective patterns

### Voice Analytics
- **Method Usage** - Distribution of voice input methods
- **Success Rate** - Transcription and processing success
- **Risk Distribution** - Voice input risk score patterns
- **Session History** - Complete voice interaction logs

## 🚀 Advanced Features

### Custom Chain Creation
```python
# Add new agent chain
from agent_choreographer import get_choreographer
choreographer = get_choreographer()
choreographer.add_chain("custom_flow", ["agent1", "agent2", "agent3"])
```

### Pattern Effectiveness Testing
```python
# Test pattern effectiveness
from pattern_tester import get_pattern_tester
tester = get_pattern_tester()
result = await tester.test_pattern_override("agent_name", "input", "pattern_name", agent_map)
```

### Voice Input Integration
```python
# Process voice input
from voice_input import get_voice_input
voice_input = get_voice_input()
result = await voice_input.process_voice_input("agent_name", agent_map, "auto", 5)
```

### Debug Session Management
```python
# Manage debug sessions
from debug_ui import save_debug_session, get_debug_summary
save_debug_session("session_name.json")
summary = get_debug_summary()
```

## 🎯 Evolution: v13 → v14.3

| Feature | Fusion v13 | Fusion v14.3 |
|---------|------------|---------------|
| **Architecture** | Sequential orchestration | AI-Native Operating System |
| **Agents** | 5 basic agents | 31 specialized agents |
| **Synthetic Reasoning** | None | 5 thoughts + 5 queries per agent |
| **Risk Assessment** | None | Automatic 0.0-1.0 risk scoring |
| **Pattern Override** | None | 6 intelligent fallback patterns |
| **Multi-Agent Chains** | None | 5 predefined + custom chains |
| **Debug Visibility** | None | Complete synthetic reasoning display |
| **Pattern Testing** | None | Live effectiveness testing |
| **Voice Input** | None | Voice-to-text with risk detection |
| **Web Interface** | None | Complete 5-page Streamlit app |
| **CLI Commands** | 3 basic commands | 9 comprehensive commands |
| **Configuration** | Hardcoded | JSON-based with live editing |
| **Analytics** | None | Comprehensive session tracking |

## 🎉 Deployment Ready

### Production Interfaces
1. **CLI Interface** - `python3 fusion.py [command]` (always available)
2. **Web Interface** - `python3 start_web_app.py` (when streamlit available)
3. **Python API** - Direct import and programmatic usage

### Verification
```bash
# Test all components
python3 test_web_app.py

# Expected output:
# ✅ PASS Module Imports
# ✅ PASS Configuration Files  
# ✅ PASS Agent Imports
# ✅ PASS Async Functionality
# 🎉 ALL TESTS PASSED! Web app components are ready.
```

### Production Status
- ✅ **31 Agents Working** - All individual and combined agents operational
- ✅ **Debug System** - Complete synthetic reasoning visibility
- ✅ **Chain Execution** - Multi-agent workflow orchestration
- ✅ **Pattern Testing** - Live fallback effectiveness evaluation  
- ✅ **Voice Processing** - Voice-to-text with risk assessment
- ✅ **Web Application** - Full-featured interface for all functionality
- ✅ **Configuration Management** - Live editing and analytics
- ✅ **Session Analytics** - Comprehensive tracking and reporting

## 🎬 Real Examples

### Debug Mode in Action
```bash
$ python3 fusion.py --debug run vp_design "Design a checkout flow"

🔍 Debug mode enabled - showing synthetic reasoning details
🚀 Running agent 'vp_design' on input: Design a checkout flow

============================================================
🧠 AGENT DEBUG: vp_design (23:47:58)
============================================================
⚠️  Risk Score: 0.41

🧠 Synthetic Thoughts (5):
  1. The user might expect both critique and rewrite.
  2. It's unclear whether Tailwind or Markdown output is preferred.
  3. This may trigger fallback pattern if confidence is low.
  4. The input lacks specific context about target audience.
  5. Need to clarify if this is for internal or external stakeholders.

❓ Internal Questions (5):
  1. Should I use the Executive Rewriter pattern?
  2. Is the user expecting structured output?
  3. Should this pass through RewriteLoopAgent after critique?
  4. What level of detail is appropriate for this request?
  5. Are there any sensitive aspects I should avoid?
============================================================
```

### Chain Execution Example
```bash
$ python3 fusion.py chain design_pipeline "Create a support tile"

🔄 Executing chain: design_pipeline
📋 Agents: vp_design → evaluator → rewrite_loop
📝 Input: Create a support tile
============================================================

🎯 Step 1/3: vp_design
✅ vp_design completed

🎯 Step 2/3: evaluator  
✅ evaluator completed

🎯 Step 3/3: rewrite_loop
✅ rewrite_loop completed

============================================================
🎬 Chain 'design_pipeline' completed
⏱️  Duration: 0.31s
✅ Success: True
📊 Steps completed: 3/3
============================================================
```

### Pattern Testing Example
```bash
$ python3 fusion.py test-pattern evaluator fallback_metric_narrative "Test design"

🧪 Testing Pattern Override
🎯 Agent: evaluator
🔄 Pattern: fallback_metric_narrative
📝 Input: Test design
============================================================
🔍 Step 1: Normal Agent Execution
🧬 Step 2: Pattern Override Execution
============================================================
📊 PATTERN TEST RESULTS
============================================================
⚠️  Risk Score Comparison:
   Normal: 0.41
   Pattern: 0.41
   Change: +0.00

📈 Pattern Effectiveness:
   Overall Score: 0.20
   Verdict: Low Effectiveness
   Output Changed: True
   Risk Reduction: +0.00
============================================================
```

## 🤝 Contributing

Fusion v14.3 is designed for maximum extensibility:

1. **Add New Agents** - Follow the async pattern with synthetic reasoning
2. **Create Tools** - Build modular tools for specific capabilities  
3. **Define Patterns** - Register custom fallback patterns
4. **Build Chains** - Create custom multi-agent workflows
5. **Extend Web UI** - Add new pages to the Streamlit interface

## 📝 License

This project is part of the Fusion ecosystem. See individual component licenses for details.

---

**Fusion v14.3** - From Agent Toolkit to AI-Native Operating System 🚀

*Complete with Debug UI, Agent Choreographer, Pattern Testing, Voice Input, and Web Interface*