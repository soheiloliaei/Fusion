# Fusion v14 - Master Prompt

## Overview
Fusion v14 is an advanced agent-based system for design, development, and strategic planning. It consists of 22 specialized agents organized into 5 categories, each with specific capabilities and expertise.

## Agent Categories

### Core Agents
- **vp_design**: Design critique and enhancement
- **evaluator**: Comprehensive evaluation and scoring
- **creative_director**: Creative strategy and direction

### Strategic Agents  
- **strategy_pilot**: Long-range strategic planning
- **vp_of_design**: Design executive decisions
- **vp_of_product**: Product executive decisions

### Technical Agents
- **design_technologist**: Figma-to-code conversion
- **product_navigator**: Feature analysis and complexity scoring

### Companion Agents
- **principal_designer**: AI-native design partner
- **component_librarian**: Design system management
- **content_designer**: Microcopy and content strategy
- **ai_interaction_designer**: AI-human interaction patterns

### Meta Agents
- **strategy_archivist**: Strategic knowledge management
- **market_analyst**: Market trends and competitive analysis
- **workflow_optimizer**: Process optimization
- **product_historian**: Product evolution tracking

### Narrative & Content Agents
- **deck_narrator**: Compelling narratives and presentations
- **portfolio_editor**: Design work curation
- **research_summarizer**: Research synthesis
- **feedback_amplifier**: User feedback analysis

### Intelligence & Orchestration Agents
- **prompt_master**: Pattern matching and prompt optimization
- **dispatcher**: Intelligent agent routing

## Usage

### Single Agent Execution
```bash
python3 fusion.py run [agent_name] "your prompt"
```

### Pipeline Execution
```bash
python3 fusion.py pipeline "your prompt"
```

## Key Features

### Memory System
- Each agent maintains memory of past interactions
- Pattern recognition and learning capabilities
- Confidence scoring and fallback mechanisms

### Intelligent Routing
- Dispatcher agent analyzes prompts and routes to optimal agents
- Fallback chains for low-confidence scenarios
- Performance-based agent selection

### Structured Output
- All agents provide structured, actionable results
- Confidence scoring for quality assessment
- Shared state management across pipeline

## Agent Capabilities

### Design & UX
- UI/UX design critique and enhancement
- Accessibility-first design principles
- Component library management
- Design system token extraction

### Strategy & Planning
- Long-range strategic roadmaps
- Competitive analysis and simulation
- Business goal prioritization
- Market opportunity identification

### Technical Implementation
- Figma-to-code conversion (Tailwind/React)
- Component complexity analysis
- Development viability assessment
- Technical architecture planning

### Content & Communication
- Microcopy and content strategy
- Stakeholder-ready narratives
- Research synthesis and summarization
- User feedback amplification

### Intelligence & Orchestration
- Prompt pattern recognition
- Intelligent agent routing
- Memory-based learning
- Fallback chain management

## System Architecture

### Core Components
- **fusion.py**: Main CLI runner
- **execution_orchestrator_v14.py**: Pipeline orchestration
- **agent_memory.py**: Memory management system
- **pattern_registry.json**: Pattern definitions

### Memory & Learning
- JSON-based memory storage
- Pattern recognition from past interactions
- Confidence scoring and trend analysis
- Similar prompt detection

### Quality Assurance
- Comprehensive evaluation criteria
- Confidence scoring for all outputs
- Fallback mechanisms for low-confidence scenarios
- Structured output validation

## Best Practices

### Prompt Engineering
- Be specific about desired outcomes
- Include context and constraints
- Specify target audience when relevant
- Use clear action verbs

### Agent Selection
- Use dispatcher for automatic routing
- Leverage specialized agents for domain-specific tasks
- Consider pipeline execution for complex workflows
- Monitor confidence scores for quality assurance

### Memory Utilization
- Agents learn from past interactions
- Similar prompts trigger pattern recognition
- Confidence improves with usage
- Fallback chains ensure reliability

## Integration Points

### Design Tools
- Figma integration for design-to-code
- Component library management
- Design system token extraction
- Accessibility compliance checking

### Development Workflow
- Technical feasibility assessment
- Complexity scoring for features
- Edge case identification
- Implementation roadmap planning

### Strategic Planning
- Market analysis and competitive intelligence
- Long-range strategic roadmaps
- Business goal alignment
- Risk assessment and mitigation

## Quality Metrics

### Confidence Scoring
- All agents provide 0.0-1.0 confidence scores
- Threshold-based fallback triggers
- Performance tracking and improvement
- Pattern-based confidence calculation

### Evaluation Criteria
- Clarity and comprehensibility
- Completeness of response
- Actionability of recommendations
- Accuracy and relevance
- Innovation and creativity
- Business value contribution

## Future Enhancements

### Planned Features
- Advanced pattern recognition
- Cross-agent collaboration
- Real-time learning and adaptation
- Enhanced fallback mechanisms
- Performance optimization

### Scalability
- Modular agent architecture
- Pluggable memory systems
- Extensible pattern registry
- Configurable routing heuristics

## Support & Maintenance

### Troubleshooting
- Check agent availability with `python3 fusion.py run [agent] "test"`
- Monitor confidence scores for quality issues
- Review memory patterns for learning insights
- Validate pipeline execution for complex workflows

### Performance Optimization
- Memory-based pattern recognition
- Confidence-based routing decisions
- Fallback chain optimization
- Structured output validation

---

*Fusion v14 - Advanced Agent-Based Design & Development System* 