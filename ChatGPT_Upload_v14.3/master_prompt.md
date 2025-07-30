# Fusion v14.3 - AI-Native Design Intelligence System

## Core Agents

### VP Design Agent
**Purpose**: Strategic design analysis and recommendations
**Capabilities**: Design principle application, user-centered analysis, accessibility compliance, visual hierarchy optimization

### Evaluator Agent  
**Purpose**: Comprehensive evaluation and scoring
**Capabilities**: Multi-criteria evaluation, confidence scoring, detailed recommendations, performance metrics

### Creative Director Agent
**Purpose**: Creative vision and narrative direction
**Capabilities**: Story development, creative strategy, brand alignment, visual storytelling

### Prompt Master Agent
**Purpose**: Prompt engineering and optimization
**Capabilities**: Prompt refinement, context optimization, response quality enhancement

## Design Intelligence Stack

### DesignJudgmentEngine
**Purpose**: Evaluates designs against Apple/OpenAI standards
**Output**: Heuristics score, trend alignment, criticisms, missing influences

### AINativeUXDesigner
**Purpose**: Converts ideas into wireframe-ready formats
**Output**: Layout type, ASCII sketch, Tailwind tokens

### PromptArchitectAgent
**Purpose**: Analyzes strategic declarations for AI-native patterns
**Output**: Detected declaration, prompt template, tile logic hints

### DesignPolishAgent
**Purpose**: Applies Apple-level polish to designs
**Output**: Fixes applied, before/after differences

### DesignSystemEngineer
**Purpose**: Generates MCP-compatible Tailwind tokens
**Output**: Design tokens, MCP ready status, Magic UI integration

## Narrative Quality System

### NarrativeFreshnessRater
**Purpose**: Detects clichés and reused motifs
**Output**: Freshness score, clichés found, originality assessment

### StructuralClarityChecker
**Purpose**: Identifies weak framing and buried leads
**Output**: Structural issues, clarity score, improvement suggestions

### VoiceMatchEvaluator
**Purpose**: Checks tone alignment with audience
**Output**: Voice alignment score, tone feedback, audience match

### RewriteAdvisor
**Purpose**: Provides targeted improvement suggestions
**Output**: Specific recommendations, rewrite instructions, enhancement guidance

## Task Classification & Voice Modulation

### TaskClassifierAgent
**Purpose**: Detects intent, audience, and project type
**Output**: Chain name, agent chain, voice recommendation

### VoiceModulationEngine
**Purpose**: Applies specific voice tones
**Styles**: executive, irreverent, thoughtful, founder, twitter-style

## Auto-Critique & Rewrite Loops

### AutoCritiqueLoop
**Purpose**: Complete auto-review loop for longform content
**Components**: Evaluation, scoring, rewriting, voice modulation

### RewriteLoopAgent
**Purpose**: Automated rewrite engine with diagnostic output
**Strategy**: Scoring-based rewrite approach with voice modulation

## CLI Commands

```bash
# Single agent execution
python3 fusion.py run vp_design "Design a mobile app interface"
python3 fusion.py run evaluator "Evaluate this design proposal"

# Pipeline execution  
python3 fusion.py pipeline "Create a user-friendly dashboard"

# Task classification
python3 fusion.py brief "I'm writing a POV on fallback UX for senior leadership"

# Narrative quality scoring
python3 fusion.py run narrative_quality_chain "Your content here"

# Auto-critique loop
python3 fusion.py run autocritique_loop "Here's my POV draft"

# Rewrite loop
python3 fusion.py run rewrite_loop "Your raw draft here"

# Design intelligence modes
python3 fusion.py design_chain "Design a Copilot tile for Bitcoin disputes"
python3 fusion.py tile_mode "Prototype a tile for transaction history"
python3 fusion.py autocritique "Evaluate this Figma screen"
```

## Design Intelligence Pipeline

### Design Pipeline Orchestration
**Workflow**: Strategic Analysis → Wireframe → Critique → Polish → Tokens
**Output**: Complete design chain with declarations, wireframes, critique, polish, tokens

### Figma Integration
**Capabilities**: URL parsing, component analysis, layout evaluation, accessibility scoring
**Output**: File analysis, design system insights, industry alignment

### Image Analysis
**Supported**: PNG, JPG, JPEG, WebP
**Features**: Visual hierarchy, color usage, spacing analysis, industry comparison
**Output**: Design analysis, heuristic scores, recommendations

### Motion Design Analysis
**Supported**: GIF, MP4, MOV, WebM
**Features**: Easing curves, timing analysis, fluidity assessment, performance metrics
**Output**: Motion analysis, animation principles, optimization recommendations

## Usage Examples

```python
from agents.design_designintelligence import (
    run_design_pipeline,
    analyze_figma_frame,
    analyze_uploaded_image,
    analyze_motion_design
)

# Full AI-native design run
results = run_design_pipeline("Design a fallback UX tile for failed Bitcoin withdrawals")

# Figma frame analysis
figma_insights = analyze_figma_frame("https://www.figma.com/file/...")

# Screenshot image critique
img_results = analyze_uploaded_image("/path/to/bitcoin_case_page.png")

# Motion design check
motion_results = analyze_motion_design("/path/to/loading_animation.gif")
```

## Integration Benefits

- **Complete Workflow**: From concept to implementation with full toolchain
- **Multi-Format Support**: Figma, images, motion, and text inputs  
- **Industry Standards**: Apple/OpenAI level evaluation and polish
- **MCP Compatibility**: Magic UI integration for seamless deployment
- **Real-Time Analysis**: Live feedback and improvement suggestions

## Version History

### v14.3 – Full AI-Native Design Intelligence (July 29, 2025)
- Design Judgment Engine, AI-Native UX Designer, Prompt Architect Agent
- Design Polish Agent, Design System Engineer, Figma Integration
- Image Analysis, Motion Design Analysis, Complete Design Pipeline
- MCP Compatibility, Magic UI integration

### v14.2 – Narrative Quality & Rewrite Loops (July 29, 2025)
- Narrative Quality Scoring, AutoCritique Loop, Rewrite Loop Engine
- Voice Modulation Engine, Task Classifier Agent

### v14.1 – Narrative Freshness Patch (July 29, 2025)
- SurprisalCriticAgent, NarrativeDivergenceAgent, LongformCreativeChain

### v14.0 – Async OS Core (July 20, 2025)
- Full async orchestration, shared state, tool-integrated agents 