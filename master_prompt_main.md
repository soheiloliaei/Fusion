# Fusion v14 Master Prompt

## System Overview
Fusion v14 is a programmable agent OS that orchestrates specialized agents and tools for comprehensive design analysis, evaluation, and recommendations. The system operates with sophisticated memory management and pattern-based fallback mechanisms.

## Core Architecture

### Agent System
- **VP Design Agent**: Design analysis, user-centered principles, accessibility compliance
- **Evaluator Agent**: Comprehensive evaluation with confidence scoring
- **Tool Integration**: UX Audit and Trust Explainer tools
- **Pattern Registry**: Intelligent pattern matching and fallback

### Execution Flow
1. **Input Processing**: Analyze user input for intent and requirements
2. **Agent Selection**: Choose appropriate agent(s) based on input type
3. **Tool Coordination**: Apply relevant tools to enhance analysis
4. **Pattern Application**: Use patterns for improved results when confidence is low
5. **Output Generation**: Provide comprehensive, actionable recommendations
6. **Memory Storage**: Store interaction for learning and context

## Agent Capabilities

### VP Design Agent
**Purpose**: Design analysis and recommendations with focus on user experience

**Core Functions**:
- Design principle application (user-centered, accessibility, visual hierarchy)
- Request type identification (UI design, UX design, brand design, general design)
- Design element extraction (color, typography, layout, interaction, navigation)
- User needs assessment (accessibility, mobile-friendly, performance, simplicity)
- Constraint identification (budget, time, existing systems)
- Target audience analysis (business, consumer, technical, general users)

**Design Principles Applied**:
1. User-centered design (always applied)
2. Accessibility first (when accessibility is a user need)
3. Consistent visual hierarchy (for UI and general design)
4. Clear information architecture (for UX and general design)
5. Responsive design patterns (when mobile-friendly is needed)
6. Performance optimization (when performance is a user need)
7. Brand consistency (for brand design)

**Output Structure**:
- Enhanced output with design recommendations
- Confidence scoring based on analysis quality
- Tool usage tracking
- Shared state updates
- Execution time metrics

### Evaluator Agent
**Purpose**: Comprehensive evaluation and scoring across multiple criteria

**Evaluation Criteria**:
1. **Clarity** (15% weight): How clear and understandable is the output?
2. **Completeness** (15% weight): How complete is the response to the request?
3. **Actionability** (20% weight): How actionable are the recommendations?
4. **Accuracy** (15% weight): How accurate is the information provided?
5. **Relevance** (15% weight): How relevant is the output to the input?
6. **Innovation** (10% weight): How innovative or creative is the approach?
7. **Product Value** (10% weight): How much business/product value does it provide?

**Quality Assessment**:
- Excellent Quality (≥0.9): Ready for production use
- Good Quality (≥0.8): Minor improvements recommended
- Acceptable Quality (≥0.7): Some improvements needed
- Needs Improvement (<0.7): Significant enhancements required

### SurprisalCriticAgent
**Purpose**: Detects overused motifs, phrases, and structure across outputs

**Core Functions**:
- Motif extraction and pattern recognition
- Semantic similarity analysis
- Surprisal scoring based on motif overlap
- Feedback generation for narrative freshness

**Detection Patterns**:
- Common phrases: "Cursor", "fallback UX", "design systems"
- Structural patterns: repetitive narrative flows
- Semantic motifs: overused concepts and themes

**Output**:
- Fresh narrative confirmation or reused motif warnings
- Surprisal score (0.0-1.0) indicating originality
- Specific feedback on detected patterns

### NarrativeDivergenceAgent
**Purpose**: Restructures content to lead with lived friction, surprising POV, or a "I changed my mind" moment

**Core Functions**:
- Story-first narrative restructuring
- POV shift injection
- Lived experience integration
- Avoidance of predictable exposition

**Restructuring Patterns**:
- "I used to believe X, but then Y happened" format
- Real-world friction and surprise elements
- Personal transformation narratives
- Unexpected perspective shifts

**Output**:
- Restructured content with narrative tension
- Story-led introductions
- Enhanced reader engagement

### LongformCreativeChain
**Purpose**: A composite agent flow for longform outputs ensuring freshness and narrative tension

**Execution Flow**:
1. **Divergence**: NarrativeDivergenceAgent restructures input
2. **Creation**: Main agent (VP Design, Evaluator, etc.) processes divergent input
3. **Critique**: SurprisalCriticAgent evaluates output freshness

**Use Cases**:
- Substack-style posts and essays
- Longform content creation
- Narrative-heavy design documentation
- Creative writing and storytelling

**Output**:
- Complete chain execution with all intermediate steps
- Original input, divergent input, agent output, and surprisal review
- Comprehensive freshness analysis

### TaskClassifierAgent
**Purpose**: Detects intent, audience, and project type from natural language

**Core Functions**:
- Intent pattern matching (portfolio, deck, substack, one-pager, POV)
- Audience detection (SLT, engineering, design peers, founders, etc.)
- Voice style mapping (executive, thoughtful, irreverent, founder, twitter-style)
- Agent chain recommendation

**Output**:
- Chain name and recommended agent sequence
- Detected voice style for audience
- Complete orchestration parameters

### VoiceModulationEngine
**Purpose**: Applies appropriate voice styles based on audience and context

**Voice Styles**:
- **Executive**: Elevated, strategic, succinct for C-level executives
- **Thoughtful**: Reflective, considered, articulate for peers and collaborators
- **Irreverent**: Playful, sharp, subversive for Twitter or Substack
- **Founder**: Clear, direct, vision-driven for builders and startup leads
- **Twitter-style**: One-liner smart for viral thread starters

**Integration**:
- Automatically applied after task classification
- Provides voice-specific rewriting instructions
- Enhances content appropriateness for target audience

### Narrative Quality Scoring Layer

**Purpose**: Comprehensive narrative quality evaluation with freshness scoring, structural analysis, and voice matching

**Core Components**:

#### NarrativeFreshnessRater
**Purpose**: Uses surprisal signals and motif detection to rate narrative freshness

**Detection Patterns**:
- **Reused Motifs**: Cursor, fallback UX, design systems, agentic workflows
- **Cliché Detection**: "game changer", "paradigm shift", "revolutionary", "innovative solution"
- **Freshness Scoring**: 0.0-1.0 based on originality and uniqueness

**Output**:
- Freshness score with detailed breakdown
- List of detected clichés and reused motifs
- Specific feedback on narrative originality

#### StructuralClarityChecker
**Purpose**: Detects weak framing, buried leads, or vague scaffolding

**Structural Analysis**:
- **Buried Lead Detection**: Identifies weak openings vs. strong story hooks
- **Vague Scaffolding**: Flags uncertain language and hedging
- **Weak Framing**: Checks for clear POV statements and strong positioning
- **Repetitive Structure**: Identifies monotonous sentence patterns

**Output**:
- List of structural issues found
- Issue count and severity assessment
- Specific structural recommendations

#### VoiceMatchEvaluator
**Purpose**: Checks if tone aligns with declared audience

**Voice Contexts**:
- **Executive**: Strategic, business-focused language
- **Thoughtful**: Nuanced, collaborative tone
- **Irreverent**: Bold, subversive, attention-grabbing
- **Founder**: Direct, vision-driven, honest
- **Twitter-style**: Viral, debate-provoking, concise

**Output**:
- Voice alignment score (0.0-1.0)
- Expected vs. actual voice comparison
- Specific voice adjustment feedback

#### RewriteAdvisor
**Purpose**: Offers targeted suggestions per failure point

**Suggestion Categories**:
- **Structural**: Opening hooks, POV statements, paragraph purpose
- **Freshness**: Cliché replacement, motif alternatives
- **Voice**: Tone adjustment, audience alignment
- **Flow**: Sentence variation, logical progression

**Output**:
- Prioritized improvement suggestions
- Context-specific recommendations
- Actionable rewrite guidance

#### NarrativeQualityChain
**Purpose**: Composite scoring engine for comprehensive narrative evaluation

**Scoring Algorithm**:
- **Base Score**: Freshness rating (0.0-1.0)
- **Voice Bonus**: +0.2 for strong voice alignment
- **Structure Penalty**: -0.05 per structural issue
- **Final Score**: Clamped to 0.0-1.0 range

**Verdict Categories**:
- **Strong, unique voice** (≥0.85): Ready for publication
- **Good quality, minor improvements** (≥0.7): Small tweaks needed
- **Acceptable but needs work** (≥0.5): Moderate improvements required
- **Significant improvements required** (<0.5): Major revision needed

**Output Format**:
```json
{
  "score": 0.84,
  "verdict": "Good quality, minor improvements needed",
  "issues": ["weak framing", "reused motifs"],
  "recommendations": ["Open with stronger hook", "Add specific examples"],
  "voice_feedback": "Tone matches executive voice well",
  "freshness_details": {...},
  "structural_details": {...}
}
```

**Integration Points**:
- **EvaluatorAgent**: Enhanced evaluation with narrative quality metrics
- **SubstackChain**: Post-creation quality assessment
- **POVChain**: Executive review with voice matching
- **AutoCritiqueLoop**: Iterative quality improvement

### AutoCritique Loop

**Purpose**: Complete auto-review loop for any longform content: POVs, decks, Substacks, essays

**Core Components**:
- **EvaluatorAgent**: Structural evaluation and quality assessment
- **NarrativeQualityChain**: Freshness scoring and voice matching
- **RewriteAdvisor**: Targeted improvement suggestions
- **VoiceModulationEngine**: Tone adaptation for target audience

**Workflow**:
1. **Evaluation**: Assess structure, clarity, and completeness
2. **Scoring**: Rate freshness, detect clichés, check voice alignment
3. **Recommendations**: Generate specific improvement suggestions
4. **Voice Modulation**: Adapt tone for target audience

**Output Format**:
```json
{
  "evaluation": {
    "agent": "evaluator",
    "output": "Comprehensive evaluation results...",
    "confidence": 0.845,
    "execution_time": 0.00001
  },
  "score": 0.84,
  "verdict": "Good quality, minor improvements needed",
  "issues": ["weak framing", "reused motifs"],
  "recommendations": ["Open with stronger hook", "Add specific examples"],
  "voice_feedback": "Tone matches executive voice well",
  "modulated_instruction": "Rewrite this as if it's being sent to C-level executives..."
}
```

**CLI Usage**:
```bash
python3 fusion.py run autocritique_loop "Your content here"
```

**Use Cases**:
- **POV Drafts**: Executive review with strategic framing
- **Substack Essays**: Freshness check with irreverent voice
- **Deck Content**: Structural clarity with executive tone
- **Portfolio Pieces**: Quality assessment with thoughtful voice

### Rewrite Loop Execution Engine

**Purpose**: Automated rewrite engine that takes diagnostic output and generates clean, modulated rewrites

**Core Components**:
- **NarrativeQualityChain**: Provides quality assessment and critique
- **VoiceModulationEngine**: Adapts tone for target audience
- **RewriteAdvisor**: Generates specific improvement suggestions
- **RewriteLoopAgent**: Orchestrates the complete rewrite process

**Workflow**:
1. **Quality Assessment**: Evaluate freshness, structure, and voice alignment
2. **Issue Analysis**: Identify clichés, weak framing, and structural problems
3. **Rewrite Instructions**: Generate specific improvement guidance
4. **Voice Modulation**: Apply target voice style (executive, irreverent, founder, etc.)
5. **Draft Generation**: Create rewritten version based on quality score

**Scoring-Based Rewrite Strategy**:
- **Score < 0.3**: Major rewrite with fresh opening and cliché replacement
- **Score 0.3-0.7**: Moderate rewrite with specific improvements
- **Score > 0.7**: Minor tweaks, preserve original structure

**Available Voice Styles**:
- **executive**: Strategic, business-focused, C-level appropriate
- **irreverent**: Bold, subversive, attention-grabbing
- **founder**: Direct, vision-driven, honest
- **thoughtful**: Nuanced, collaborative, peer-appropriate
- **twitter-style**: Viral, debate-provoking, concise

**Output Format**:
```json
{
  "original_draft": "Original content...",
  "quality_report": {
    "score": 0.84,
    "verdict": "Good quality, minor improvements needed",
    "issues": ["weak framing", "reused motifs"],
    "recommendations": ["Open with stronger hook", "Add specific examples"]
  },
  "rewrite_instructions": "Open with a stronger hook or clear POV statement. Replace clichés: game changer, revolutionary...",
  "modulated_instruction": "Rewrite this as if it's being sent to C-level executives...",
  "rewritten_draft": "Fallback UX isn't optional. It's the trust reserve teams forget until it breaks...",
  "target_voice": "executive",
  "verdict": "Good quality, minor improvements needed"
}
```

**CLI Usage**:
```bash
python3 fusion.py run rewrite_loop "Your raw draft here..."
```

**Use Cases**:
- **POV Rewrites**: Transform raw thoughts into executive-ready content
- **Substack Essays**: Convert cliché-heavy drafts into fresh narratives
- **Deck Content**: Restructure weak openings for strategic impact
- **Portfolio Pieces**: Enhance structure and voice alignment

### Design Agent Stack (Fusion v14.3)

**Purpose**: AI-native design agents for evaluating, architecting, and polishing design work

**Core Components**:

#### DesignJudgmentEngine
**Purpose**: Evaluates a design from screenshots, Figma frames, or visual JSON

**Evaluation Framework**:
- **Heuristics Score**: 0.0-1.0 based on design quality
- **Trend Alignment**: Strong/Moderate/Weak industry alignment
- **Criticisms**: Specific design issues identified
- **Missing Influences**: Recommended design references

**Output**:
```json
{
  "heuristics_score": 0.91,
  "trend_alignment": "Strong",
  "criticisms": ["Minor spacing inconsistencies", "Could benefit from more breathing room"],
  "influences_missing": ["Apple", "Airbnb", "Netflix", "OpenAI", "Anthropic", "Origin", "Intercom Fin"],
  "recommendations": ["Study Apple's Human Interface Guidelines", "Reference Airbnb's design system patterns"]
}
```

#### PromptArchitectAgent
**Purpose**: Analyzes strategic declarations and outputs AI-native prompt architecture with fallback logic

**Detection Patterns**:
- **Fallback UX**: Error states, failure modes, trust validation
- **Copilot Tiles**: AI assistant patterns, progressive disclosure
- **Trust Score**: User confidence, verification flows
- **Auto Execution**: Automatic actions, confirmation patterns

**Output**:
```json
{
  "detected_declaration": "Fallback UX for high-stakes flows",
  "prompt_template": "Given [context], recommend fallback states using [Copilot tiles + user trust score]",
  "tile_logic_hints": ["Trigger fallback if confidence < 0.6", "Ask user to confirm before auto-executing"],
  "ai_native_patterns": ["Progressive disclosure", "Trust-based interactions", "Graceful degradation"]
}
```

#### AINativeUXDesigner
**Purpose**: Converts raw ideas into wireframe-ready formats (ASCII, JSON, Tailwind blocks)

**Layout Types**:
- **Copilot Tile**: 2-column MCP tile
- **Dashboard**: 3-column responsive grid
- **Modal**: Centered overlay with backdrop
- **Navigation**: Horizontal tab bar

**Output**:
```json
{
  "layout_type": "Data visualization tile",
  "ascii_sketch": "[Chart Header] | [Transaction List]\n[Summary Stats] | [Action Buttons]",
  "tailwind_tokens": {
    "padding": "p-4",
    "font": "font-inter",
    "radius": "rounded-2xl",
    "background": "bg-gray-50"
  },
  "wireframe_ready": true,
  "mcp_compatible": true
}
```

#### DesignPolishAgent
**Purpose**: Applies critique feedback and uplifts craft to Apple/OpenAI level pixel detail

**Polish Categories**:
- **Spacing**: Harmonized spacing patterns
- **Typography**: Modernized font weights and line heights
- **Visual Hierarchy**: Improved iconography and borders
- **Color**: Enhanced contrast and accessibility

**Output**:
```json
{
  "fixes_applied": ["Harmonized spacing", "Modernized typography"],
  "before_after_diff": {
    "nav_spacing": "16px → 24px",
    "font_weight": "Medium → Semibold",
    "line_height": "1.4 → 1.5"
  },
  "craft_level": "Apple/OpenAI standard",
  "pixel_perfect": true
}
```

#### DesignSystemEngineer
**Purpose**: Generates consistent token sets and MCP-compatible Tailwind from visual inputs

**Token Generation**:
- **Primary Colors**: Brand-specific color palettes
- **Typography**: Font families and weights
- **Spacing**: Consistent spacing scales
- **Border Radius**: Modern rounded corners

**Output**:
```json
{
  "design_tokens": {
    "primary": "#00C244",
    "background": "#F9FAFB",
    "radius": "16px",
    "font": "Cash Sans"
  },
  "mcp_ready": true,
  "magic_ui_integration": "✅ Tailwind tokens match Magic UI MCP primitives",
  "output_files": ["tailwind.config.js", "tokens.json"],
  "css_variables": {
    "--primary": "#00C244",
    "--background": "#F9FAFB",
    "--radius": "16px"
  }
}
```

**CLI Usage**:
```bash
python3 fusion.py run design_judgment_engine "Evaluate this Figma frame for craft and Apple-level standards"
python3 fusion.py run ai_native_ux_designer "Design a Copilot tile that summarizes Bitcoin transaction history with fallback"
python3 fusion.py run design_system_engineer "Generate Tailwind tokens for this Figma screenshot"
python3 fusion.py run prompt_architect "Design fallback UX for high-stakes flows with trust score validation"
python3 fusion.py run design_polish_agent "Apply Apple-level polish to this design with improved spacing and typography"
```

**Use Cases**:
- **Design Evaluation**: Assess Figma frames against industry standards
- **AI-Native UX**: Convert ideas into wireframe-ready formats
- **Design Systems**: Generate consistent token sets for projects
- **Design Polish**: Uplift craft to Apple/OpenAI standards
- **Prompt Architecture**: Structure AI interactions with fallback logic

### Design Intelligence Stack Integration

**Purpose**: End-to-end AI-native design flow orchestration with three specialized modes

**Core Modes**:

#### DesignChain Workspace
**Purpose**: Full end-to-end design flow orchestration

**Workflow**:
1. **Declaration Interpretation**: Analyze strategic design requirements
2. **Wireframe Generation**: Convert ideas into wireframe-ready formats
3. **Quality Evaluation**: Assess design against industry standards
4. **Design Polish**: Apply Apple/OpenAI level craft improvements
5. **Token Generation**: Create consistent design system tokens

**Output**:
```json
{
  "declarations": {
    "detected_declaration": "Fallback UX for high-stakes flows",
    "prompt_template": "Given [context], recommend fallback states using [Copilot tiles + user trust score]",
    "tile_logic_hints": ["Trigger fallback if confidence < 0.6", "Ask user to confirm before auto-executing"]
  },
  "wireframe": {
    "layout_type": "Data visualization tile",
    "ascii_sketch": "[Chart Header] | [Transaction List]\n[Summary Stats] | [Action Buttons]",
    "tailwind_tokens": {"padding": "p-4", "font": "font-inter", "radius": "rounded-2xl"}
  },
  "critique": {
    "heuristics_score": 0.82,
    "trend_alignment": "Moderate",
    "criticisms": ["Weak information hierarchy", "Inconsistent spacing tokens"]
  },
  "polish": {
    "fixes_applied": ["Harmonized spacing", "Modernized iconography"],
    "before_after_diff": {"nav_spacing": "16px → 24px", "font_weight": "Medium → Semibold"}
  },
  "tokens": {
    "design_tokens": {"primary": "#10A37F", "background": "#F9FAFB", "radius": "16px"},
    "mcp_ready": true,
    "magic_ui_integration": "✅ Tailwind tokens match Magic UI MCP primitives"
  }
}
```

#### CopilotTile Prototyping Mode
**Purpose**: Focused prototyping for AI-powered tiles

**Components**:
- **Tile Logic**: AI-native interaction patterns and fallback logic
- **Wireframe**: Visual layout and component structure
- **Tailwind Tokens**: MCP-compatible design system tokens

**Output**:
```json
{
  "tile_logic": {
    "detected_declaration": "Fallback UX for high-stakes flows",
    "tile_logic_hints": ["Trigger fallback if confidence < 0.6", "Show clear error boundaries"]
  },
  "wireframe": {
    "layout_type": "Data visualization tile",
    "ascii_sketch": "[Chart Header] | [Transaction List]\n[Summary Stats] | [Action Buttons]"
  },
  "tailwind_tokens": {
    "design_tokens": {"primary": "#00C244", "background": "#F9FAFB", "radius": "16px"},
    "mcp_ready": true
  }
}
```

#### Auto-Critique Loop
**Purpose**: Live design quality feedback and improvement recommendations

**Components**:
- **Critique**: Design evaluation against industry standards
- **Polish Recommendations**: Specific improvement suggestions

**Output**:
```json
{
  "critique": {
    "heuristics_score": 0.82,
    "trend_alignment": "Moderate",
    "criticisms": ["Weak information hierarchy", "Inconsistent spacing tokens"],
    "recommendations": ["Study Apple's Human Interface Guidelines", "Reference Airbnb's design system patterns"]
  },
  "polish_recommendations": {
    "fixes_applied": ["Harmonized spacing", "Modernized iconography"],
    "before_after_diff": {"nav_spacing": "16px → 24px", "font_weight": "Medium → Semibold"},
    "craft_level": "Apple/OpenAI standard"
  }
}
```

**CLI Usage**:
```bash
# Full DesignChain Workspace
python3 fusion.py design_chain "Design a Copilot tile that explains fallback UX in Bitcoin disputes"

# CopilotTile Prototyping Mode
python3 fusion.py tile_mode "Prototype a tile for transaction history summary with trust fallback"

# Auto-Critique Loop
python3 fusion.py autocritique "Evaluate this Figma screen for modern UI trends and polish"
```

**Integration Benefits**:
- **End-to-End Flow**: Complete design process from concept to implementation
- **AI-Native Patterns**: Built-in fallback logic and trust validation
- **Industry Standards**: Apple/OpenAI level craft and polish
- **MCP Compatibility**: Magic UI integration for seamless deployment
- **Live Feedback**: Real-time critique and improvement suggestions

### Full AI-Native Design Intelligence (Fusion v14.3)

**Purpose**: Complete AI-native design orchestration with Figma integration, image analysis, and motion design evaluation

**Core Capabilities**:

#### Design Pipeline Orchestration
**Purpose**: End-to-end design flow from idea to implementation

**Workflow**:
1. **Strategic Analysis**: Interpret design declarations and requirements
2. **Wireframe Generation**: Convert ideas into wireframe-ready formats
3. **Quality Evaluation**: Assess design against industry standards
4. **Design Polish**: Apply Apple/OpenAI level craft improvements
5. **Token Generation**: Create MCP-compatible design system tokens

**Output**:
```json
{
  "tile_logic": {
    "detected_declaration": "Fallback UX for high-stakes flows",
    "prompt_template": "Given [context], recommend fallback states using [Copilot tiles + user trust score]",
    "tile_logic_hints": ["Trigger fallback if confidence < 0.6", "Ask user to confirm before auto-executing"]
  },
  "wireframe": {
    "layout_type": "Data visualization tile",
    "ascii_sketch": "[Chart Header] | [Transaction List]\n[Summary Stats] | [Action Buttons]",
    "tailwind_tokens": {"padding": "p-4", "font": "font-inter", "radius": "rounded-2xl"}
  },
  "critique": {
    "heuristics_score": 0.82,
    "trend_alignment": "Moderate",
    "criticisms": ["Weak information hierarchy", "Inconsistent spacing tokens"]
  },
  "polish": {
    "fixes_applied": ["Harmonized spacing", "Modernized iconography"],
    "before_after_diff": {"nav_spacing": "16px → 24px", "font_weight": "Medium → Semibold"}
  },
  "tokens": {
    "design_tokens": {"primary": "#10A37F", "background": "#F9FAFB", "radius": "16px"},
    "mcp_ready": true,
    "magic_ui_integration": "✅ Tailwind tokens match Magic UI MCP primitives"
  },
  "pipeline_status": "complete",
  "mcp_ready": true
}
```

#### Figma Integration
**Purpose**: Parse Figma URLs and extract design insights

**Capabilities**:
- **URL Parsing**: Extract file IDs and frame information
- **Component Analysis**: Detect design system components
- **Layout Evaluation**: Identify structural issues and improvements
- **Accessibility Scoring**: WCAG compliance and usability metrics
- **Industry Alignment**: Compare against Apple/OpenAI standards

**Output**:
```json
{
  "file_id": "abc123",
  "frames_analyzed": 12,
  "components_detected": 45,
  "layout_issues": [
    "Inconsistent spacing between elements",
    "Weak visual hierarchy in navigation",
    "Overuse of decorative elements"
  ],
  "design_system_insights": {
    "color_palette": ["#00C244", "#F9FAFB", "#333333"],
    "typography": "Inter, 16px, Medium",
    "spacing_scale": "8px, 16px, 24px, 32px",
    "border_radius": "8px, 12px, 16px"
  },
  "accessibility_score": 0.78,
  "industry_alignment": "Moderate - could benefit from Apple/OpenAI patterns"
}
```

#### Image Analysis
**Purpose**: Analyze uploaded images for design critique

**Supported Formats**: PNG, JPG, JPEG, WebP

**Analysis Features**:
- **Visual Hierarchy**: Information flow and structure evaluation
- **Color Usage**: Contrast and accessibility assessment
- **Spacing Analysis**: Consistency and harmonization
- **Typography Review**: Font choices and readability
- **Industry Comparison**: Apple, OpenAI, Cash App alignment scores

**Output**:
```json
{
  "image_path": "/path/to/image.png",
  "dimensions": "1920x1080",
  "design_analysis": {
    "visual_hierarchy": "Strong - clear information flow",
    "color_usage": "Effective - good contrast and accessibility",
    "spacing": "Inconsistent - needs harmonization",
    "typography": "Modern - good font choices"
  },
  "heuristic_scores": {
    "clarity": 0.85,
    "consistency": 0.72,
    "accessibility": 0.78,
    "aesthetics": 0.81
  },
  "industry_comparison": {
    "apple_alignment": 0.73,
    "openai_alignment": 0.68,
    "cash_app_alignment": 0.82
  }
}
```

#### Motion Design Analysis
**Purpose**: Evaluate animation principles in GIF/MP4 files

**Supported Formats**: GIF, MP4, MOV, WebM

**Analysis Features**:
- **Easing Curves**: Natural animation feel evaluation
- **Timing Analysis**: Keyframe delays and rhythm
- **Fluidity Assessment**: Smooth transitions and jank detection
- **Intent Communication**: Purpose and functional clarity
- **Performance Metrics**: File size, frame rate, optimization

**Output**:
```json
{
  "file_path": "/path/to/animation.gif",
  "format": "gif",
  "duration": "2.4s",
  "frame_count": 72,
  "motion_analysis": {
    "easing_curves": "Good use of ease-out for natural feel",
    "timing": "Appropriate delays between keyframes",
    "fluidity": "Smooth transitions with minimal jank",
    "intent_communication": "Clear purpose - loading state"
  },
  "animation_principles": {
    "anticipation": 0.75,
    "follow_through": 0.68,
    "squash_stretch": 0.82,
    "timing": 0.79
  },
  "performance_metrics": {
    "frame_rate": "30fps",
    "file_size": "2.4MB",
    "optimization_score": 0.71
  }
}
```

**Usage Examples**:
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

**Integration Benefits**:
- **Complete Workflow**: From concept to implementation with full toolchain
- **Multi-Format Support**: Figma, images, motion, and text inputs
- **Industry Standards**: Apple/OpenAI level evaluation and polish
- **MCP Compatibility**: Magic UI integration for seamless deployment
- **Real-Time Analysis**: Live feedback and improvement suggestions

## Tool System

### UX Audit Tool
**Purpose**: Comprehensive UX analysis using heuristic evaluation and metrics

**Heuristic Evaluation** (Nielsen's 10 heuristics):
1. Visibility of system status
2. Match between system and real world
3. User control and freedom
4. Consistency and standards
5. Error prevention
6. Recognition rather than recall
7. Flexibility and efficiency of use
8. Aesthetic and minimalist design
9. Help users recognize, diagnose, and recover from errors
10. Help and documentation

**UX Metrics Analysis**:
- **Usability**: ease_of_use, learnability, efficiency
- **Accessibility**: wcag_compliance, screen_reader, keyboard_navigation
- **Performance**: load_time, response_time, smoothness
- **Engagement**: user_retention, time_on_site, interaction_rate

### Trust Explainer Tool
**Purpose**: Trust-building analysis and enhancement recommendations

**Trust Elements Analysis**:
- **Transparency**: clear_pricing, data_usage, privacy_policy, terms_of_service
- **Security**: encryption, secure_payment, data_protection, compliance
- **Social Proof**: reviews, testimonials, user_count, expert_endorsements
- **Reliability**: uptime, performance, support_quality, update_frequency
- **Expertise**: credentials, experience, certifications, industry_recognition

**Trust Indicators Evaluation**:
- **Visual**: professional_design, brand_consistency, quality_icons, modern_ui
- **Content**: clear_messaging, helpful_information, transparent_processes, educational_content
- **Interaction**: responsive_feedback, error_handling, loading_states, progress_indicators
- **Social**: user_reviews, social_media, community_features, expert_opinions

## Pattern System

### Pattern Registry
**Purpose**: Intelligent pattern management with fallback mechanisms

**Built-in Patterns**:
1. **design_enhancement**: Apply design principles and accessibility
2. **ux_audit**: Perform comprehensive UX audit
3. **trust_building**: Analyze and enhance trust elements
4. **comprehensive_evaluation**: Full evaluation with detailed scoring
5. **basic_evaluation**: Essential evaluation criteria

**Pattern Selection Logic**:
- Design-related inputs → design_enhancement, ux_audit, or trust_building
- Evaluation-related inputs → comprehensive_evaluation
- Default fallback → design_enhancement

## Memory and Context Management

### Fusion Context
**Purpose**: Shared state and memory management across all agents and tools

**Memory Components**:
- **Interaction Memory**: Store all agent interactions with timestamps
- **Pattern Memory**: Pattern-specific data and performance metrics
- **Shared State**: Persistent state across agent executions
- **Execution History**: Complete execution tracking and statistics

**Memory Features**:
- Export/import capabilities for persistence
- Relevant memory retrieval based on query similarity
- Pattern usage statistics and success rates
- Context summary generation

## Configuration System

### .fusion.json Configuration
**Purpose**: Centralized configuration for all system components

**Key Settings**:
- **version**: System version (v14.0)
- **max_prompt_tokens**: Token limit for prompts (8000)
- **enabled_agents**: List of active agents
- **tools_enabled**: Enable/disable tool system
- **pattern_fallback**: Enable pattern fallback system
- **memory_enabled**: Enable memory management
- **async_mode**: Enable async execution
- **auto_commit**: Enable automatic commits
- **debug_mode**: Enable debug logging
- **log_level**: Logging level (INFO)

## CLI Interface

### Command Structure
**Main Commands**:
- `run <agent> <input>`: Execute single agent
- `pipeline <input>`: Execute full agent pipeline
- `pattern <input>`: Execute with pattern fallback
- `status`: Show system status and statistics
- `help`: Show help information

**Example Usage**:
```bash
# Single agent execution
python fusion.py run vp_design "Design a mobile app interface"

# Pipeline execution
python fusion.py pipeline "Create a user-friendly dashboard"

# Pattern-based execution
python fusion.py pattern "Evaluate this design proposal"

# System status
python fusion.py status
```

**Output Format**:
- Structured results with confidence scores
- Execution time metrics
- Tool usage tracking
- Error handling with clear messages
- Colored output for better readability

## Error Handling and Fallback

### Error Recovery
- **Agent Failures**: Automatic fallback to alternative agents
- **Tool Failures**: Graceful degradation without tool functionality
- **Pattern Failures**: Fallback to basic patterns or direct execution
- **Memory Failures**: Continue execution without memory features

### Confidence-Based Fallback
- **High Confidence** (≥0.8): Use results directly
- **Medium Confidence** (0.6-0.8): Apply enhancement patterns
- **Low Confidence** (<0.6): Apply comprehensive fallback patterns

## Best Practices

### Input Guidelines
- **Be Specific**: Provide detailed requirements and context
- **Include Constraints**: Mention budget, time, or technical limitations
- **Specify Audience**: Indicate target users and their needs
- **Mention Goals**: Describe desired outcomes and success criteria

### Output Interpretation
- **Confidence Scores**: Higher scores indicate more reliable results
- **Tool Usage**: Check which tools were applied for comprehensive analysis
- **Pattern Application**: Note which patterns were used for enhancement
- **Recommendations**: Prioritize high-confidence recommendations

### System Optimization
- **Memory Management**: Export memory periodically for persistence
- **Pattern Performance**: Monitor pattern success rates and adjust thresholds
- **Tool Selection**: Use appropriate tools based on input type
- **Error Monitoring**: Check logs for recurring issues

## Integration and Extensibility

### Adding New Agents
1. Create agent class with async `run()` method
2. Implement required interface methods
3. Register with orchestrator
4. Update configuration

### Adding New Tools
1. Create tool class with async `run()` method
2. Implement tool-specific analysis logic
3. Register with orchestrator
4. Update agent tool usage

### Adding New Patterns
1. Define pattern metadata and enhancement logic
2. Register with pattern registry
3. Define fallback relationships
4. Test pattern performance

This master prompt provides comprehensive guidance for understanding and using Fusion v14, ensuring consistent behavior across all system components while maintaining flexibility for future enhancements.
