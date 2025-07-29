# Fusion v14 Master Prompt

## System Overview

Fusion v14 is a programmable agent OS that orchestrates specialized agents and tools to provide comprehensive design analysis, evaluation, and recommendations. The system operates asynchronously with sophisticated memory management and pattern-based fallback mechanisms.

## Core Architecture

### Agent System
- **VP Design Agent**: Specialized in design analysis, user-centered design principles, and accessibility compliance
- **Evaluator Agent**: Comprehensive evaluation across multiple criteria with confidence scoring
- **Tool Integration**: Modular tools (UX Audit, Trust Explainer) that enhance agent capabilities
- **Pattern Registry**: Intelligent pattern matching and fallback for optimal performance

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

**Evaluation Process**:
- Context extraction from input
- Multi-criteria evaluation with weighted scoring
- Reasoning generation for each criterion
- Overall confidence calculation
- Detailed evaluation report generation

**Quality Assessment**:
- Excellent Quality (≥0.9): Ready for production use
- Good Quality (≥0.8): Minor improvements recommended
- Acceptable Quality (≥0.7): Some improvements needed
- Needs Improvement (<0.7): Significant enhancements required

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

**Output**: Comprehensive UX audit report with specific recommendations

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

**Output**: Trust enhancement plan with specific implementation strategies

## Pattern System

### Pattern Registry
**Purpose**: Intelligent pattern management with fallback mechanisms

**Built-in Patterns**:
1. **design_enhancement**: Apply design principles and accessibility
2. **ux_audit**: Perform comprehensive UX audit
3. **trust_building**: Analyze and enhance trust elements
4. **comprehensive_evaluation**: Full evaluation with detailed scoring
5. **basic_evaluation**: Essential evaluation criteria

**Pattern Features**:
- Smart pattern matching based on input keywords
- Confidence-based pattern application
- Fallback system for low-confidence results
- Performance tracking and statistics
- Custom pattern creation capabilities

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

**Context Summary Includes**:
- Session ID and timestamp
- Total interactions and average confidence
- Memory size and shared state keys
- Recent interaction history
- Pattern memory statistics

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

### Logging and Debugging
- **Structured Logging**: All operations logged with timestamps
- **Error Tracking**: Detailed error information for debugging
- **Performance Monitoring**: Execution time and resource usage
- **Debug Mode**: Enhanced logging for development

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

### Custom Configuration
- Modify `.fusion.json` for system settings
- Add custom agents to enabled_agents list
- Configure tool-specific settings
- Set pattern fallback preferences

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

## Future Enhancements

### Planned Features
- **MCP Integration**: Connect to external services (GitHub, Figma, etc.)
- **Multi-modal Support**: Handle images, documents, and voice input
- **Advanced Learning**: Pattern performance-based learning
- **External APIs**: Integration with design and development tools
- **Professional UI**: Web-based interface for non-technical users

### Architecture Evolution
- **Microservices**: Decompose into independent services
- **Plugin System**: Dynamic loading of agents and tools
- **Distributed Execution**: Multi-node agent orchestration
- **Real-time Collaboration**: Multi-user simultaneous usage

This master prompt provides comprehensive guidance for understanding and using Fusion v14, ensuring consistent behavior across all system components while maintaining flexibility for future enhancements. 