#!/usr/bin/env python3
"""
Fusion v14 - CLI Runner
Programmable agent OS for design and evaluation
"""

import argparse
import asyncio
import json
import sys
from typing import Dict, Any

from agents_combined import (
    VPDesignAgent, EvaluatorAgent, CreativeDirectorAgent, PromptMasterAgent,
    SurprisalCriticAgent, NarrativeDivergenceAgent, LongformCreativeChain,
    NarrativeFreshnessRater, StructuralClarityChecker, VoiceMatchEvaluator,
    RewriteAdvisor, NarrativeQualityChain, RewriteLoopAgent,
    DesignJudgmentEngine, PromptArchitectAgent, AINativeUXDesigner, DesignPolishAgent, DesignSystemEngineer
)
from synthetic_reasoner_agent import SyntheticReasonerAgent
from autocritique_loop import AutoCritiqueLoop
from execution_orchestrator_v14 import ExecutionOrchestrator
from task_classifier_agent import TaskClassifierAgent
from voice_modulation_engine import VoiceModulationEngine

print("🧠 DEBUG: fusion.py top-level code executed")

async def run_with_reasoning(user_input, agent):
    """Run agent with synthetic reasoning meta-agent"""
    reasoner = SyntheticReasonerAgent()
    agent_name = getattr(agent, "__class__", type(agent)).__name__
    meta = reasoner.run(user_input, agent_name)

    print("\n🧠 Synthetic Thoughts:")
    for t in meta["synthetic_thoughts"]:
        print(f"  - {t}")
    print("❓ Internal Questions:")
    for q in meta["synthetic_queries"]:
        print(f"  → {q}")
    print(f"⚠️ Risk Score: {meta['risk_score']}\n")

    # 🧠 Optional for Sprint 2:
    # if meta['risk_score'] > 0.65: trigger fallback routing

    return await agent.run(user_input)

async def run_design_chain(prompt: str) -> Dict[str, Any]:
    """Full DesignChain workspace - end-to-end design flow orchestration"""
    # Step 1: Interpret declarations
    prompt_result = await PromptArchitectAgent().run(prompt)
    
    # Step 2: Generate wireframes
    ux_result = await AINativeUXDesigner().run(prompt)
    
    # Step 3: Evaluate raw output
    judgment_result = await DesignJudgmentEngine().run(prompt)
    
    # Step 4: Polish design
    polish_result = await DesignPolishAgent().run(prompt)
    
    # Step 5: Tokenize for system
    token_result = await DesignSystemEngineer().run(prompt)
    
    return {
        "declarations": prompt_result,
        "wireframe": ux_result,
        "critique": judgment_result,
        "polish": polish_result,
        "tokens": token_result,
    }

async def run_tile_prototyping_mode(prompt: str) -> Dict[str, Any]:
    """CopilotTile prototyping mode - focused on AI-powered tiles"""
    tile_logic = await PromptArchitectAgent().run(prompt)
    wireframe = await AINativeUXDesigner().run(prompt)
    tokens = await DesignSystemEngineer().run(prompt)
    return {
        "tile_logic": tile_logic,
        "wireframe": wireframe,
        "tailwind_tokens": tokens
    }

async def run_design_autocritique_loop(prompt_or_frame: str) -> Dict[str, Any]:
    """Auto-Critique loop - live design quality feedback"""
    critique = await DesignJudgmentEngine().run(prompt_or_frame)
    polish = await DesignPolishAgent().run(prompt_or_frame)
    return {
        "critique": critique,
        "polish_recommendations": polish
    }

async def main():
    parser = argparse.ArgumentParser(description="Fusion v14 CLI")
    subparsers = parser.add_subparsers(dest="command")

    # 'run' command: single agent
    run_parser = subparsers.add_parser("run", help="Run a single agent")
    run_parser.add_argument("agent", type=str, help="Agent name (e.g., vp_design)")
    run_parser.add_argument("input", nargs=argparse.REMAINDER, help="Input prompt")

    # 'pipeline' command: full pipeline execution
    pipeline_parser = subparsers.add_parser("pipeline", help="Run pipeline with prompt")
    pipeline_parser.add_argument("input", nargs=argparse.REMAINDER, help="Pipeline input")

    # 'brief' command: task classification
    brief_parser = subparsers.add_parser("brief", help="Classify task intent and audience")
    brief_parser.add_argument("input", nargs=argparse.REMAINDER, help="Brief description")
    
    # Design Intelligence Stack commands
    design_chain_parser = subparsers.add_parser("design_chain", help="Full DesignChain workspace - end-to-end design flow")
    design_chain_parser.add_argument("prompt", nargs=argparse.REMAINDER, help="Design prompt")
    
    tile_mode_parser = subparsers.add_parser("tile_mode", help="CopilotTile prototyping mode - focused on AI-powered tiles")
    tile_mode_parser.add_argument("prompt", nargs=argparse.REMAINDER, help="Tile design prompt")
    
    autocritique_parser = subparsers.add_parser("autocritique", help="Auto-Critique loop - live design quality feedback")
    autocritique_parser.add_argument("design_input", nargs=argparse.REMAINDER, help="Design input to critique")

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
            "prompt_master": PromptMasterAgent,
            
            # Narrative Freshness Agents (v14.1)
            "surprisal_critic": SurprisalCriticAgent,
            "narrative_divergence": NarrativeDivergenceAgent,
            "longform_creative_chain": LongformCreativeChain,
            "narrative_freshness_rater": NarrativeFreshnessRater,
            "structural_clarity_checker": StructuralClarityChecker,
            "voice_match_evaluator": VoiceMatchEvaluator,
            "rewrite_advisor": RewriteAdvisor,
            "narrative_quality_chain": NarrativeQualityChain,
            "autocritique_loop": AutoCritiqueLoop,
            "rewrite_loop": RewriteLoopAgent,
            "design_judgment_engine": DesignJudgmentEngine,
            "prompt_architect": PromptArchitectAgent,
            "ai_native_ux_designer": AINativeUXDesigner,
            "design_polish_agent": DesignPolishAgent,
            "design_system_engineer": DesignSystemEngineer
        }
        
        if args.agent in agent_map:
            # All agents are now working
            agent_class = agent_map[args.agent]
            agent = agent_class()
            output = await run_with_reasoning(input_text, agent)
            print(f"🎨 Output from {args.agent}:\n{output}")
        else:
            print(f"❌ Error: Unknown agent '{args.agent}'")
            print(f"Available agents: {', '.join(agent_map.keys())}")
            sys.exit(1)

    elif args.command == "brief":
        if not args.input:
            print("❌ Error: 'brief' command requires input")
            sys.exit(1)

        brief_input = " ".join(args.input)
        classifier = TaskClassifierAgent()
        result = classifier.classify(brief_input)
        print("🧠 Task Classifier Result:")
        print(f"Chain: {result['chain_name']}")
        print(f"Agents: {result['agent_chain']}")
        print(f"Voice: {result['voice']}")

        modulator = VoiceModulationEngine()
        example_output = "Here's a draft memo about fallback UX and modular interface scaffolds."
        modulated = modulator.apply_voice(example_output, result["voice"])
        print("\n🎙 Modulated Sample Output:")
        print(modulated)
    
    elif args.command == "design_chain":
        if not args.prompt:
            print("❌ Error: 'design_chain' command requires a prompt")
            sys.exit(1)
        design_prompt = " ".join(args.prompt)
        print(f"🧠 Running DesignChain workspace on: {design_prompt}")
        result = await run_design_chain(design_prompt)
        print("🎨 DesignChain Result:")
        print(json.dumps(result, indent=2))
    
    elif args.command == "tile_mode":
        if not args.prompt:
            print("❌ Error: 'tile_mode' command requires a prompt")
            sys.exit(1)
        tile_prompt = " ".join(args.prompt)
        print(f"🧩 Running CopilotTile prototyping mode on: {tile_prompt}")
        result = await run_tile_prototyping_mode(tile_prompt)
        print("🎨 Tile Mode Result:")
        print(json.dumps(result, indent=2))
    
    elif args.command == "autocritique":
        if not args.design_input:
            print("❌ Error: 'autocritique' command requires design input")
            sys.exit(1)
        design_input = " ".join(args.design_input)
        print(f"🪞 Running Auto-Critique loop on: {design_input}")
        result = await run_design_autocritique_loop(design_input)
        print("🎨 Auto-Critique Result:")
        print(json.dumps(result, indent=2))

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
    asyncio.run(main()) 