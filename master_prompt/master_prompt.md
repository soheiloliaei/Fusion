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
