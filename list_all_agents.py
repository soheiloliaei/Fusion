#!/usr/bin/env python3
"""
List All Available Agents - Fusion v14
Shows all available agents and how to use them
"""

import sys
import os

# Add the current directory to Python path
sys.path.append('.')

def list_all_agents():
    """List all available agents with their descriptions"""
    
    print("🚀 Fusion v14 - All Available Agents")
    print("=" * 60)
    
    # Core Agents
    print("\n🎯 CORE AGENTS:")
    core_agents = {
        "vp_design": "Design analysis and recommendations",
        "evaluator": "Comprehensive evaluation and scoring", 
        "creative_director": "Creative strategy and vision",
        "design_technologist": "Technical design implementation",
        "product_navigator": "Product strategy and navigation",
        "strategy_pilot": "Strategic planning and execution",
        "vp_of_design": "VP of Design leadership",
        "vp_of_product": "VP of Product leadership"
    }
    
    for agent, description in core_agents.items():
        print(f"  • {agent}: {description}")
    
    # Companion Agents
    print("\n🤝 COMPANION AGENTS:")
    companion_agents = {
        "principal_designer": "Principal design expertise",
        "component_librarian": "Component library management",
        "content_designer": "Content and copy design",
        "ai_interaction_designer": "AI interaction design"
    }
    
    for agent, description in companion_agents.items():
        print(f"  • {agent}: {description}")
    
    # Meta Agents
    print("\n🧠 META AGENTS:")
    meta_agents = {
        "strategy_archivist": "Strategy documentation and archiving",
        "market_analyst": "Market analysis and insights",
        "workflow_optimizer": "Workflow optimization",
        "product_historian": "Product history and context"
    }
    
    for agent, description in meta_agents.items():
        print(f"  • {agent}: {description}")
    
    # Narrative & Content Agents
    print("\n📝 NARRATIVE & CONTENT AGENTS:")
    narrative_agents = {
        "deck_narrator": "Presentation and deck creation",
        "portfolio_editor": "Portfolio management",
        "research_summarizer": "Research summarization",
        "feedback_amplifier": "Feedback processing and amplification"
    }
    
    for agent, description in narrative_agents.items():
        print(f"  • {agent}: {description}")
    
    # Intelligence & Orchestration Agents
    print("\n🎛️ INTELLIGENCE & ORCHESTRATION AGENTS:")
    intelligence_agents = {
        "prompt_master": "Pattern matching and prompt optimization",
        "dispatcher": "Agent coordination and routing"
    }
    
    for agent, description in intelligence_agents.items():
        print(f"  • {agent}: {description}")
    
    print("\n" + "=" * 60)
    print("📊 TOTAL: 22 agents available")
    print("\n🚀 HOW TO USE:")
    print("1. Single agent: python3 fusion.py run <agent_name> <prompt>")
    print("2. Full pipeline: python3 fusion.py pipeline <prompt>")
    print("\n💡 EXAMPLES:")
    print("  python3 fusion.py run vp_design 'Design a mobile app for task management'")
    print("  python3 fusion.py run creative_director 'Create a brand identity for a tech startup'")
    print("  python3 fusion.py run evaluator 'Evaluate this design proposal'")
    print("  python3 fusion.py pipeline 'Design a complete user experience for an e-commerce platform'")

def test_agent_imports():
    """Test that all agents can be imported successfully"""
    print("\n🔍 Testing Agent Imports...")
    
    agents_to_test = [
        "agents.vp_design_agent.VPDesignAgent",
        "agents.evaluator_agent.EvaluatorAgent", 
        "agents.creative_director_agent.CreativeDirectorAgent",
        "agents.design_technologist_agent.DesignTechnologistAgent",
        "agents.product_navigator_agent.ProductNavigatorAgent",
        "agents.strategy_pilot_agent.StrategyPilotAgent",
        "agents.vp_of_design_agent.VPOfDesignAgent",
        "agents.vp_of_product_agent.VPOfProductAgent",
        "agents.prompt_master_agent.PromptMasterAgent",
        "agents.dispatcher_agent.DispatcherAgent",
        "agents.principal_designer_agent.PrincipalDesignerAgent",
        "agents.component_librarian_agent.ComponentLibrarianAgent",
        "agents.content_designer_agent.ContentDesignerAgent",
        "agents.ai_interaction_designer_agent.AIInteractionDesignerAgent",
        "agents.strategy_archivist_agent.StrategyArchivistAgent",
        "agents.market_analyst_agent.MarketAnalystAgent",
        "agents.workflow_optimizer_agent.WorkflowOptimizerAgent",
        "agents.product_historian_agent.ProductHistorianAgent",
        "agents.deck_narrator_agent.DeckNarratorAgent",
        "agents.portfolio_editor_agent.PortfolioEditorAgent",
        "agents.research_summarizer_agent.ResearchSummarizerAgent",
        "agents.feedback_amplifier_agent.FeedbackAmplifierAgent"
    ]
    
    failed_imports = []
    
    for agent_import in agents_to_test:
        try:
            module_name, class_name = agent_import.rsplit('.', 1)
            module = __import__(module_name, fromlist=[class_name])
            agent_class = getattr(module, class_name)
            print(f"  ✅ {class_name}")
        except Exception as e:
            print(f"  ❌ {class_name}: {e}")
            failed_imports.append(agent_import)
    
    if failed_imports:
        print(f"\n⚠️  {len(failed_imports)} agents failed to import")
    else:
        print(f"\n🎉 All {len(agents_to_test)} agents imported successfully!")

if __name__ == "__main__":
    list_all_agents()
    test_agent_imports() 