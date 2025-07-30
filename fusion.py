#!/usr/bin/env python3
"""
Fusion v14 - CLI Runner
Programmable agent OS for design and evaluation
"""

import argparse
import asyncio
import sys

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

# Companion Agents
from agents.principal_designer_agent import PrincipalDesignerAgent
from agents.component_librarian_agent import ComponentLibrarianAgent
from agents.content_designer_agent import ContentDesignerAgent
from agents.ai_interaction_designer_agent import AIInteractionDesignerAgent

# Meta Agents
from agents.strategy_archivist_agent import StrategyArchivistAgent
from agents.market_analyst_agent import MarketAnalystAgent
from agents.workflow_optimizer_agent import WorkflowOptimizerAgent
from agents.product_historian_agent import ProductHistorianAgent

# Narrative & Content Agents
from agents.deck_narrator_agent import DeckNarratorAgent
from agents.portfolio_editor_agent import PortfolioEditorAgent
from agents.research_summarizer_agent import ResearchSummarizerAgent
from agents.feedback_amplifier_agent import FeedbackAmplifierAgent
from core.execution_orchestrator_v14 import ExecutionOrchestrator

print("🧠 DEBUG: fusion.py top-level code executed")

def main():
    parser = argparse.ArgumentParser(description="Fusion v14 CLI")
    subparsers = parser.add_subparsers(dest="command")

    # 'run' command: single agent
    run_parser = subparsers.add_parser("run", help="Run a single agent")
    run_parser.add_argument("agent", type=str, help="Agent name (e.g., vp_design)")
    run_parser.add_argument("input", nargs=argparse.REMAINDER, help="Input prompt")

    # 'pipeline' command: full pipeline execution
    pipeline_parser = subparsers.add_parser("pipeline", help="Run pipeline with prompt")
    pipeline_parser.add_argument("input", nargs=argparse.REMAINDER, help="Pipeline input")

    # Parse args
    args = parser.parse_args()
    print(f"🛠 DEBUG: Parsed args = {args}")

    if args.command == "run":
        if not args.input:
            print("❌ Error: 'run' command requires input")
            sys.exit(1)

        input_text = " ".join(args.input)
        print(f"🚀 Running agent '{args.agent}' on input: {input_text}")

        # Dynamic agent loading
        agent_map = {
            # Core Agents
            "vp_design": VPDesignAgent,
            "evaluator": EvaluatorAgent,
            "creative_director": CreativeDirectorAgent,
            "design_technologist": DesignTechnologistAgent,
            "product_navigator": ProductNavigatorAgent,
            
            # Strategic Agents
            "strategy_pilot": StrategyPilotAgent,
            "vp_of_design": VPOfDesignAgent,
            "vp_of_product": VPOfProductAgent,
            
            # Companion Agents
            "principal_designer": PrincipalDesignerAgent,
            "component_librarian": ComponentLibrarianAgent,
            "content_designer": ContentDesignerAgent,
            "ai_interaction_designer": AIInteractionDesignerAgent,
            
            # Meta Agents
            "strategy_archivist": StrategyArchivistAgent,
            "market_analyst": MarketAnalystAgent,
            "workflow_optimizer": WorkflowOptimizerAgent,
            "product_historian": ProductHistorianAgent,
            
            # Narrative & Content Agents
            "deck_narrator": DeckNarratorAgent,
            "portfolio_editor": PortfolioEditorAgent,
            "research_summarizer": ResearchSummarizerAgent,
            "feedback_amplifier": FeedbackAmplifierAgent,
            
            # Intelligence & Orchestration Agents
            "prompt_master": PromptMasterAgent,
            "dispatcher": DispatcherAgent
        }
        
        if args.agent in agent_map:
            # All agents are now working
            agent_class = agent_map[args.agent]
            agent = agent_class()
            output = asyncio.run(agent.run_async(input_text, {}))
            print(f"🎨 Output from {args.agent}:\n{output}")
        else:
            print(f"❌ Error: Unknown agent '{args.agent}'")
            print(f"Available agents: {', '.join(agent_map.keys())}")
            sys.exit(1)

    elif args.command == "pipeline":
        if not args.input:
            print("❌ Error: 'pipeline' command requires input")
            sys.exit(1)

        input_text = " ".join(args.input)
        print(f"⚙️ Running pipeline on: {input_text}")

        from core.fusion_context import FusionContext
        context = FusionContext({})
        orchestrator = ExecutionOrchestrator(context)
        
        # Register agents and tools
        from tools.ux_audit_tool import UXAuditTool
        from tools.trust_explainer_tool import TrustExplainerTool
        
        # Register ALL 22 agents explicitly
        print("📝 Registering all 22 agents...")
        
        # Core Agents (8)
        orchestrator.register_agent("vp_design", VPDesignAgent())
        orchestrator.register_agent("evaluator", EvaluatorAgent())
        orchestrator.register_agent("creative_director", CreativeDirectorAgent())
        orchestrator.register_agent("design_technologist", DesignTechnologistAgent())
        orchestrator.register_agent("product_navigator", ProductNavigatorAgent())
        orchestrator.register_agent("strategy_pilot", StrategyPilotAgent())
        orchestrator.register_agent("vp_of_design", VPOfDesignAgent())
        orchestrator.register_agent("vp_of_product", VPOfProductAgent())
        
        # Companion Agents (4)
        orchestrator.register_agent("principal_designer", PrincipalDesignerAgent())
        orchestrator.register_agent("component_librarian", ComponentLibrarianAgent())
        orchestrator.register_agent("content_designer", ContentDesignerAgent())
        orchestrator.register_agent("ai_interaction_designer", AIInteractionDesignerAgent())
        
        # Meta Agents (4)
        orchestrator.register_agent("strategy_archivist", StrategyArchivistAgent())
        orchestrator.register_agent("market_analyst", MarketAnalystAgent())
        orchestrator.register_agent("workflow_optimizer", WorkflowOptimizerAgent())
        orchestrator.register_agent("product_historian", ProductHistorianAgent())
        
        # Narrative & Content Agents (4)
        orchestrator.register_agent("deck_narrator", DeckNarratorAgent())
        orchestrator.register_agent("portfolio_editor", PortfolioEditorAgent())
        orchestrator.register_agent("research_summarizer", ResearchSummarizerAgent())
        orchestrator.register_agent("feedback_amplifier", FeedbackAmplifierAgent())
        
        # Intelligence & Orchestration Agents (2)
        orchestrator.register_agent("prompt_master", PromptMasterAgent())
        orchestrator.register_agent("dispatcher", DispatcherAgent())
        
        # Register tools
        orchestrator.register_tool("ux_audit", UXAuditTool())
        orchestrator.register_tool("trust_explainer", TrustExplainerTool())
        
        print(f"✅ Registered {len(orchestrator.agents)} agents:")
        for i, agent_name in enumerate(orchestrator.agents.keys(), 1):
            print(f"  {i:2d}. {agent_name}")
        
        # Define smart agent sequence for pipeline
        # This ensures all 22 agents are used in a logical order
        agent_sequence = [
            # 1. Strategy & Planning Phase
            "strategy_pilot",      # Strategic planning
            "product_navigator",   # Product strategy
            "market_analyst",      # Market analysis
            "product_historian",   # Product context
            
            # 2. Design & Creative Phase
            "creative_director",   # Creative vision
            "vp_design",          # Design analysis
            "design_technologist", # Technical design
            "principal_designer",  # Principal expertise
            "component_librarian", # Component system
            
            # 3. Content & Communication Phase
            "content_designer",    # Content creation
            "ai_interaction_designer", # AI interactions
            "deck_narrator",      # Presentations
            "portfolio_editor",    # Portfolio management
            
            # 4. Research & Analysis Phase
            "research_summarizer", # Research synthesis
            "strategy_archivist",  # Strategy documentation
            "feedback_amplifier",  # Feedback processing
            
            # 5. Leadership & Evaluation Phase
            "vp_of_design",       # VP Design review
            "vp_of_product",      # VP Product review
            "evaluator",          # Final evaluation
            
            # 6. Intelligence & Orchestration Phase
            "prompt_master",      # Pattern optimization
            "dispatcher",         # Final coordination
            "workflow_optimizer"  # Workflow optimization
        ]
        
        print(f"\n🚀 Executing pipeline with {len(agent_sequence)} agents in sequence:")
        for i, agent in enumerate(agent_sequence, 1):
            print(f"  {i:2d}. {agent}")
        
        output = asyncio.run(orchestrator.execute_pipeline(input_text, agent_sequence))
        print(f"🧩 Pipeline Output:\n{output}")

    else:
        print("❌ Error: Unknown command. Use 'run' or 'pipeline'")
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    print("🧠 DEBUG: Entering main()")
    main() 