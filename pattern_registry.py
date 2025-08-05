#!/usr/bin/env python3
"""
Pattern Registry - Fusion v14.5
Contains all fallback pattern templates for agent routing
"""

pattern_templates = {
    "fallback_clarify_then_critique": "First clarify ambiguous terms. Then critique the design proposal step by step.",
    "fallback_metric_narrative": "Evaluate this with accessibility, hierarchy, and visual clarity scores, then explain each.",
    "fallback_soften_for_exec": "Rewrite this in a way that sounds less critical and more executive-friendly.",
    "fallback_safe_design": "Propose only minimal, conservative improvements to avoid unintended harm.",
    "fallback_user_centric": "Focus on user needs and accessibility in all recommendations.",
    "fallback_systematic": "Use systematic methodology with clear steps and reasoning.",
    "fallback_creative_safe": "Provide creative solutions while maintaining safety and accessibility standards.",
    "fallback_technical_clarity": "Explain technical concepts clearly and provide implementation guidance.",
    "fallback_strategic_alignment": "Align recommendations with business strategy and stakeholder needs.",
    "fallback_innovation_balanced": "Balance innovation with proven design patterns and user expectations."
}

# Pattern descriptions for debugging
pattern_descriptions = {
    "fallback_clarify_then_critique": "Used when input contains ambiguous terms. First clarifies, then provides structured critique.",
    "fallback_metric_narrative": "Used for evaluative tasks. Provides quantitative scores with narrative explanations.",
    "fallback_soften_for_exec": "Used for executive-sensitive content. Rewrites to be less critical and more business-friendly.",
    "fallback_safe_design": "Used when risk is high. Proposes only conservative, safe improvements.",
    "fallback_user_centric": "Used for user experience tasks. Prioritizes user needs and accessibility.",
    "fallback_systematic": "Used for complex tasks. Provides structured, step-by-step methodology.",
    "fallback_creative_safe": "Used for creative tasks with high risk. Balances creativity with safety.",
    "fallback_technical_clarity": "Used for technical tasks. Ensures clear technical communication.",
    "fallback_strategic_alignment": "Used for strategic tasks. Aligns with business objectives.",
    "fallback_innovation_balanced": "Used for innovative tasks. Balances innovation with proven patterns."
}

# Pattern triggers (when to use each pattern)
pattern_triggers = {
    "fallback_clarify_then_critique": ["ambiguous", "unclear", "vague", "confusing"],
    "fallback_metric_narrative": ["evaluate", "assess", "score", "rate", "measure"],
    "fallback_soften_for_exec": ["executive", "leadership", "stakeholder", "business"],
    "fallback_safe_design": ["risk", "danger", "harm", "safety", "conservative"],
    "fallback_user_centric": ["user", "accessibility", "inclusive", "experience"],
    "fallback_systematic": ["complex", "systematic", "methodical", "structured"],
    "fallback_creative_safe": ["creative", "innovative", "artistic", "design"],
    "fallback_technical_clarity": ["technical", "implementation", "code", "system"],
    "fallback_strategic_alignment": ["strategy", "business", "market", "competitive"],
    "fallback_innovation_balanced": ["innovation", "new", "novel", "cutting-edge"]
}

def get_pattern_template(pattern_name: str) -> str:
    """Get pattern template by name"""
    return pattern_templates.get(pattern_name, "")

def get_pattern_description(pattern_name: str) -> str:
    """Get pattern description by name"""
    return pattern_descriptions.get(pattern_name, "No description available")

def get_pattern_triggers(pattern_name: str) -> list:
    """Get pattern triggers by name"""
    return pattern_triggers.get(pattern_name, [])

def list_all_patterns() -> dict:
    """List all available patterns with descriptions"""
    return {
        name: {
            "template": template,
            "description": pattern_descriptions.get(name, "No description"),
            "triggers": pattern_triggers.get(name, [])
        }
        for name, template in pattern_templates.items()
    }

def find_pattern_by_triggers(input_text: str) -> str:
    """Find the best pattern based on input text triggers"""
    input_lower = input_text.lower()
    best_pattern = "fallback_systematic"  # Default
    max_matches = 0
    
    for pattern_name, triggers in pattern_triggers.items():
        matches = sum(1 for trigger in triggers if trigger in input_lower)
        if matches > max_matches:
            max_matches = matches
            best_pattern = pattern_name
    
    return best_pattern

def get_pattern_for_agent(agent_name: str, input_text: str = "") -> str:
    """Get the appropriate pattern for a specific agent"""
    # Default patterns for each agent type
    agent_patterns = {
        "vp_design": "fallback_clarify_then_critique",
        "evaluator": "fallback_metric_narrative", 
        "creative_director": "fallback_soften_for_exec",
        "design_technologist": "fallback_safe_design",
        "product_navigator": "fallback_user_centric",
        "strategy_pilot": "fallback_systematic",
        "vp_of_design": "fallback_soften_for_exec",
        "vp_of_product": "fallback_soften_for_exec",
        "principal_designer": "fallback_clarify_then_critique",
        "component_librarian": "fallback_safe_design",
        "content_designer": "fallback_user_centric",
        "ai_interaction_designer": "fallback_safe_design",
        "strategy_archivist": "fallback_systematic",
        "market_analyst": "fallback_metric_narrative",
        "workflow_optimizer": "fallback_systematic",
        "product_historian": "fallback_systematic",
        "deck_narrator": "fallback_soften_for_exec",
        "portfolio_editor": "fallback_user_centric",
        "research_summarizer": "fallback_systematic",
        "feedback_amplifier": "fallback_metric_narrative",
        "prompt_master": "fallback_systematic",
        "dispatcher": "fallback_systematic"
    }
    
    # Get default pattern for agent
    default_pattern = agent_patterns.get(agent_name, "fallback_systematic")
    
    # If input text is provided, try to find a better pattern
    if input_text:
        trigger_pattern = find_pattern_by_triggers(input_text)
        # Use trigger pattern if it's more specific than default
        if trigger_pattern != "fallback_systematic":
            return trigger_pattern
    
    return default_pattern 