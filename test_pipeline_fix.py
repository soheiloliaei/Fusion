#!/usr/bin/env python3
"""
Test script to debug pipeline registration
"""

import asyncio
import sys

# Add current directory to path
sys.path.append('.')

from core.fusion_context import FusionContext
from core.execution_orchestrator_v14 import ExecutionOrchestrator

# Import all agents
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

async def test_pipeline():
    """Test the pipeline with all agents"""
    
    print("🧪 Testing Pipeline Registration")
    print("=" * 50)
    
    # Create context and orchestrator
    context = FusionContext({})
    orchestrator = ExecutionOrchestrator(context)
    
    # Register all agents
    agents_to_register = {
        "vp_design": VPDesignAgent(),
        "evaluator": EvaluatorAgent(),
        "creative_director": CreativeDirectorAgent(),
        "design_technologist": DesignTechnologistAgent(),
        "product_navigator": ProductNavigatorAgent(),
        "strategy_pilot": StrategyPilotAgent(),
        "vp_of_design": VPOfDesignAgent(),
        "vp_of_product": VPOfProductAgent(),
        "prompt_master": PromptMasterAgent(),
        "dispatcher": DispatcherAgent(),
        "principal_designer": PrincipalDesignerAgent(),
        "component_librarian": ComponentLibrarianAgent(),
        "content_designer": ContentDesignerAgent(),
        "ai_interaction_designer": AIInteractionDesignerAgent(),
        "strategy_archivist": StrategyArchivistAgent(),
        "market_analyst": MarketAnalystAgent(),
        "workflow_optimizer": WorkflowOptimizerAgent(),
        "product_historian": ProductHistorianAgent(),
        "deck_narrator": DeckNarratorAgent(),
        "portfolio_editor": PortfolioEditorAgent(),
        "research_summarizer": ResearchSummarizerAgent(),
        "feedback_amplifier": FeedbackAmplifierAgent()
    }
    
    print(f"📝 Registering {len(agents_to_register)} agents...")
    
    for name, agent in agents_to_register.items():
        try:
            orchestrator.register_agent(name, agent)
            print(f"  ✅ {name}")
        except Exception as e:
            print(f"  ❌ {name}: {e}")
    
    print(f"\n📊 Registered agents: {list(orchestrator.agents.keys())}")
    print(f"📊 Total agents: {len(orchestrator.agents)}")
    
    # Test pipeline with all agents
    agent_sequence = list(orchestrator.agents.keys())
    print(f"\n🚀 Testing pipeline with {len(agent_sequence)} agents:")
    for i, agent in enumerate(agent_sequence, 1):
        print(f"  {i:2d}. {agent}")
    
    # Run a quick test (just first 3 agents to avoid long execution)
    test_sequence = agent_sequence[:3]
    print(f"\n🧪 Quick test with first 3 agents: {test_sequence}")
    
    try:
        result = await orchestrator.execute_pipeline("Test mobile app design", test_sequence)
        print(f"✅ Pipeline test successful!")
        print(f"📊 Executed {len(result.get('results', {}))} agents")
    except Exception as e:
        print(f"❌ Pipeline test failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_pipeline()) 