#!/usr/bin/env python3
"""
Agents Combined - Fusion v14.5
Combines all 32 agents for easy access
"""

# Import all agents from individual files
from agents.vp_design_agent import VPDesignAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.creative_director_agent import CreativeDirectorAgent
from agents.design_technologist_agent import DesignTechnologistAgent
from agents.product_navigator_agent import ProductNavigatorAgent
from agents.strategy_pilot_agent import StrategyPilotAgent
from agents.vp_of_design_agent import VPOfDesignAgent
from agents.vp_of_product_agent import VPOfProductAgent
from agents.prompt_master_agent import PromptMasterAgent
from agents.dispatcher_agent import DispatcherAgent
from agents.principal_designer_agent import PrincipalDesignerAgent
from agents.component_librarian_agent import ComponentLibrarianAgent
from agents.content_designer_agent import ContentDesignerAgent
from agents.ai_interaction_designer_agent import AIInteractionDesignerAgent
from agents.strategy_archivist_agent import StrategyArchivistAgent
from agents.market_analyst_agent import MarketAnalystAgent
from agents.workflow_optimizer_agent import WorkflowOptimizerAgent
from agents.product_historian_agent import ProductHistorianAgent
from agents.deck_narrator_agent import DeckNarratorAgent
from agents.portfolio_editor_agent import PortfolioEditorAgent
from agents.research_summarizer_agent import ResearchSummarizerAgent
from agents.feedback_amplifier_agent import FeedbackAmplifierAgent

# Agent registry for easy access - ALL 32 AGENTS
AGENT_REGISTRY = {
    # ✅ 1. Core Design & Strategy Agents (8)
    "vp_design": VPDesignAgent,
    "evaluator": EvaluatorAgent,
    "creative_director": CreativeDirectorAgent,
    "prompt_master": PromptMasterAgent,
    "vp_of_design": VPOfDesignAgent,
    "vp_of_product": VPOfProductAgent,
    "product_navigator": ProductNavigatorAgent,
    "strategy_pilot": StrategyPilotAgent,
    
    # ✅ 2. Narrative Quality System (10)
    "narrative_freshness_rater": "NarrativeFreshnessRaterAgent",
    "surprisal_critic": "SurprisalCriticAgent",
    "narrative_divergence": "NarrativeDivergenceAgent",
    "structural_clarity_checker": "StructuralClarityCheckerAgent",
    "voice_match_evaluator": "VoiceMatchEvaluatorAgent",
    "rewrite_advisor": "RewriteAdvisorAgent",
    "narrative_quality_chain": "NarrativeQualityChainAgent",
    "rewrite_loop": "RewriteLoopAgent",
    "longform_creative_chain": "LongformCreativeChainAgent",
    "deck_narrator": DeckNarratorAgent,
    
    # ✅ 3. Design Intelligence Stack (6)
    "design_judgment_engine": "DesignJudgmentEngineAgent",
    "ai_native_ux_designer": "AINativeUXDesignerAgent",
    "prompt_architect": "PromptArchitectAgent",
    "design_polish_agent": "DesignPolishAgent",
    "design_system_engineer": "DesignSystemEngineerAgent",
    "component_librarian": ComponentLibrarianAgent,
    
    # ✅ 4. Utility & Meta Agents (5)
    "dispatcher": DispatcherAgent,
    "principal_designer": PrincipalDesignerAgent,
    "content_designer": ContentDesignerAgent,
    "market_analyst": MarketAnalystAgent,
    "workflow_optimizer": WorkflowOptimizerAgent,
    
    # ✅ 5. Research & Data Agents (3)
    "research_summarizer": ResearchSummarizerAgent,
    "product_historian": ProductHistorianAgent,
    "feedback_amplifier": FeedbackAmplifierAgent
}

# Agent categories for auto-selection
AGENT_CATEGORIES = {
    "design": ["vp_design", "creative_director", "principal_designer", "design_technologist"],
    "evaluation": ["evaluator", "surprisal_critic", "structural_clarity_checker"],
    "narrative": ["narrative_freshness_rater", "narrative_divergence", "voice_match_evaluator"],
    "strategy": ["strategy_pilot", "vp_of_design", "vp_of_product"],
    "content": ["content_designer", "deck_narrator", "portfolio_editor"],
    "research": ["research_summarizer", "market_analyst", "product_historian"],
    "feedback": ["feedback_amplifier", "rewrite_advisor", "rewrite_loop"],
    "technical": ["design_system_engineer", "component_librarian", "ai_interaction_designer"],
    "executive": ["vp_of_design", "vp_of_product", "strategy_pilot"],
    "creative": ["creative_director", "narrative_quality_chain", "longform_creative_chain"]
}

def get_agent_by_name(agent_name: str):
    """Get agent class by name"""
    agent_class = AGENT_REGISTRY.get(agent_name)
    if not agent_class:
        raise ValueError(f"Unknown agent: {agent_name}")
    return agent_class()

def list_all_agents():
    """List all available agents"""
    return list(AGENT_REGISTRY.keys())

def get_agent_instance(agent_name: str):
    """Get agent instance by name"""
    agent_class = AGENT_REGISTRY.get(agent_name)
    if not agent_class:
        raise ValueError(f"Unknown agent: {agent_name}")
    return agent_class()

def get_agents_by_category(category: str):
    """Get agents by category"""
    return AGENT_CATEGORIES.get(category, [])

def auto_select_agent(prompt: str) -> str:
    """Auto-select the best agent based on prompt content"""
    prompt_lower = prompt.lower()
    
    # Enhanced agent selection logic
    agent_mapping = {
        # Design-focused
        "design": "vp_design",
        "ui": "vp_design",
        "ux": "vp_design",
        "interface": "vp_design",
        "visual": "creative_director",
        "creative": "creative_director",
        
        # Evaluation-focused
        "evaluate": "evaluator",
        "critique": "evaluator",
        "assess": "evaluator",
        "review": "evaluator",
        "quality": "evaluator",
        
        # Narrative-focused
        "story": "narrative_freshness_rater",
        "narrative": "narrative_divergence",
        "voice": "voice_match_evaluator",
        "tone": "voice_match_evaluator",
        
        # Strategy-focused
        "strategy": "strategy_pilot",
        "business": "vp_of_product",
        "executive": "vp_of_design",
        "product": "product_navigator",
        
        # Content-focused
        "content": "content_designer",
        "copy": "content_designer",
        "presentation": "deck_narrator",
        "portfolio": "portfolio_editor",
        
        # Research-focused
        "research": "research_summarizer",
        "market": "market_analyst",
        "history": "product_historian",
        
        # Feedback-focused
        "feedback": "feedback_amplifier",
        "improve": "rewrite_advisor",
        "rewrite": "rewrite_loop",
        
        # Technical-focused
        "technical": "design_technologist",
        "system": "design_system_engineer",
        "component": "component_librarian",
        "ai": "ai_interaction_designer",
        
        # Prompt-focused
        "prompt": "prompt_master",
        "architect": "prompt_architect",
        
        # Workflow-focused
        "workflow": "workflow_optimizer",
        "process": "workflow_optimizer",
        "optimize": "workflow_optimizer"
    }
    
    # Find the best matching agent
    selected_agent = "vp_design"  # Default
    for keyword, agent in agent_mapping.items():
        if keyword in prompt_lower:
            selected_agent = agent
            break
    
    return selected_agent

def get_agent_count():
    """Get total number of agents"""
    return len(AGENT_REGISTRY)

def get_agent_categories():
    """Get all agent categories"""
    return list(AGENT_CATEGORIES.keys()) 