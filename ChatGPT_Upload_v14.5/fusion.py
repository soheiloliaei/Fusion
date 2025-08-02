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

# Import individual agents from agents directory
from agents.ai_interaction_designer_agent import AIInteractionDesignerAgent
from agents.component_librarian_agent import ComponentLibrarianAgent
from agents.content_designer_agent import ContentDesignerAgent
from agents.creative_director_agent import CreativeDirectorAgent
from agents.deck_narrator_agent import DeckNarratorAgent
from agents.design_technologist_agent import DesignTechnologistAgent
from agents.dispatcher_agent import DispatcherAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.feedback_amplifier_agent import FeedbackAmplifierAgent
from agents.market_analyst_agent import MarketAnalystAgent
from agents.portfolio_editor_agent import PortfolioEditorAgent
from agents.principal_designer_agent import PrincipalDesignerAgent
from agents.product_historian_agent import ProductHistorianAgent
from agents.product_navigator_agent import ProductNavigatorAgent
from agents.prompt_master_agent import PromptMasterAgent
from agents.research_summarizer_agent import ResearchSummarizerAgent
from agents.strategy_archivist_agent import StrategyArchivistAgent
from agents.strategy_pilot_agent import StrategyPilotAgent
from agents.vp_design_agent import VPDesignAgent
from agents.vp_of_design_agent import VPOfDesignAgent
from agents.vp_of_product_agent import VPOfProductAgent
from agents.workflow_optimizer_agent import WorkflowOptimizerAgent

# Import combined agents for additional functionality
from agents_combined import (
    SurprisalCriticAgent, NarrativeDivergenceAgent, LongformCreativeChain,
    NarrativeFreshnessRater, StructuralClarityChecker, VoiceMatchEvaluator,
    RewriteAdvisor, NarrativeQualityChain, RewriteLoopAgent,
    DesignJudgmentEngine, PromptArchitectAgent, AINativeUXDesigner, DesignPolishAgent, DesignSystemEngineer
)
from synthetic_reasoner_agent import SyntheticReasonerAgent
from autocritique_loop import AutoCritiqueLoop
import json
from pattern_registry import pattern_templates
from debug_ui import log_agent_debug, set_debug_verbose, get_debug_summary, save_debug_session
from execution_orchestrator_v14 import ExecutionOrchestrator
from task_classifier_agent import TaskClassifierAgent
from voice_modulation_engine import VoiceModulationEngine

print("🧠 DEBUG: fusion.py top-level code executed")

# Load fallback config
try:
    with open("fallback_trigger_config.json", "r") as f:
        fallback_config = json.load(f)
except FileNotFoundError:
    fallback_config = {
        "risk_threshold": 0.65,
        "default_fallback_agent": "rewrite_loop_agent",
        "pattern_routing": {
            "vp_design": "rewrite_loop_agent",
            "evaluator": "creative_director",
            "creative_director": "rewrite_loop_agent"
        }
    }

# Pattern fallback engine
def risk_pattern_override(user_input, agent_name, synthetic_meta):
    """
    🧠 Sprint 3 – Pattern Prompt Override
    
    If risk is high, override the prompt structure (not just agent)
    Enable pattern-based prompt rerouting from config or registry
    """
    threshold = fallback_config.get("risk_threshold", 0.65)
    if synthetic_meta["risk_score"] <= threshold:
        return user_input  # no change

    pattern_key = fallback_config["pattern_routing"].get(agent_name)
    if not pattern_key:
        return user_input

    fallback_prompt = pattern_templates.get(pattern_key)
    if not fallback_prompt:
        return user_input

    print(f"🧠 Using fallback pattern: {pattern_key}")
    # Inject pattern into user_input (pre-pended instruction)
    return f"{fallback_prompt}\n\n{user_input}"

# Util: maps string name to agent class instance
def get_agent_by_name(name):
    from agents_combined import (
        VPDesignAgent,
        PromptArchitectAgent,
        CreativeDirectorAgent,
        EvaluatorAgent,
        RewriteLoopAgent,
        # Add any additional agents here
    )
    mapping = {
        "vp_design": VPDesignAgent(),
        "prompt_architect": PromptArchitectAgent(),
        "creative_director": CreativeDirectorAgent(),
        "evaluator": EvaluatorAgent(),
        "rewrite_loop_agent": RewriteLoopAgent(),
    }
    return mapping.get(name)

async def risk_aware_agent_runner(user_input, primary_agent, agent_name):
    """
    🧠 Sprint 3 – LLM-Powered Synthetic Reasoning + Pattern Prompt Override
    
    Goal:
    1. Replace static synthetic thoughts with LLM-generated ones
    2. If risk is high, override the prompt structure (not just agent)
    3. Enable pattern-based prompt rerouting from config or registry
    """
    # 1. Run LLM-powered reasoning
    reasoner = SyntheticReasonerAgent()
    synthetic_meta = reasoner.run(user_input, agent_name)

    # 2. Optionally override prompt with pattern
    final_input = risk_pattern_override(user_input, agent_name, synthetic_meta)
    
    # 3. Log debug information
    fallback_pattern = None
    if synthetic_meta["risk_score"] > fallback_config.get("risk_threshold", 0.65):
        fallback_pattern = fallback_config["pattern_routing"].get(agent_name)
    
    log_agent_debug(agent_name, synthetic_meta, fallback_pattern)

    # 4. Run agent with potentially modified input
    # Handle both run() and run_async() methods
    if hasattr(primary_agent, 'run'):
        agent_output = await primary_agent.run(final_input)
    elif hasattr(primary_agent, 'run_async'):
        agent_output = await primary_agent.run_async(final_input, {})
    else:
        raise AttributeError(f"Agent {agent_name} has no run() or run_async() method")

    return {
        "synthetic_meta": synthetic_meta,
        "routed": synthetic_meta["risk_score"] > fallback_config.get("risk_threshold", 0.65),
        "agent_output": agent_output
    }

async def run_with_reasoning(user_input, agent):
    """Run agent with synthetic reasoning meta-agent (Sprint 1 version)"""
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
    parser.add_argument("--debug", action="store_true", help="Enable debug output with synthetic reasoning details")
    subparsers = parser.add_subparsers(dest="command")

    # 'run' command: single agent
    run_parser = subparsers.add_parser("run", help="Run a single agent")
    run_parser.add_argument("agent", type=str, help="Agent name (e.g., vp_design)")
    run_parser.add_argument("input", nargs=argparse.REMAINDER, help="Input prompt")

    # 'pipeline' command: full pipeline execution
    pipeline_parser = subparsers.add_parser("pipeline", help="Run pipeline with prompt")
    pipeline_parser.add_argument("input", nargs=argparse.REMAINDER, help="Pipeline input")
    
    # 'chain' command: execute agent chains
    chain_parser = subparsers.add_parser("chain", help="Execute a chain of agents")
    chain_parser.add_argument("chain_name", type=str, help="Chain name (e.g., design_pipeline)")
    chain_parser.add_argument("input", nargs=argparse.REMAINDER, help="Input prompt")
    
    # 'test-pattern' command: test fallback patterns
    test_pattern_parser = subparsers.add_parser("test-pattern", help="Test fallback pattern overrides")
    test_pattern_parser.add_argument("agent_name", type=str, help="Agent name to test")
    test_pattern_parser.add_argument("pattern_name", type=str, help="Pattern name to test")
    test_pattern_parser.add_argument("input", nargs=argparse.REMAINDER, help="Input prompt")
    
    # 'voice' command: voice-to-text input
    voice_parser = subparsers.add_parser("voice", help="Voice input to agent")
    voice_parser.add_argument("agent_name", type=str, help="Agent name to run")
    voice_parser.add_argument("--method", choices=["whisper", "speech_recognition", "manual", "auto"], 
                             default="auto", help="Voice input method")
    voice_parser.add_argument("--duration", type=int, default=5, help="Recording duration in seconds")

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
    
    # Set debug verbosity
    if args.debug:
        set_debug_verbose(True)
        print("🔍 Debug mode enabled - showing synthetic reasoning details")

    if args.command == "run":
        if not args.input:
            print("❌ Error: 'run' command requires input")
            sys.exit(1)

        input_text = " ".join(args.input)
        print(f"🚀 Running agent '{args.agent}' on input: {input_text}")

        # Dynamic agent loading - All 31 Agents
        agent_map = {
            # Core Design Agents (6)
            "vp_design": VPDesignAgent,
            "creative_director": CreativeDirectorAgent,
            "design_technologist": DesignTechnologistAgent,
            "principal_designer": PrincipalDesignerAgent,
            "vp_of_design": VPOfDesignAgent,
            "vp_of_product": VPOfProductAgent,
            
            # Strategy & Product Agents (4)
            "product_navigator": ProductNavigatorAgent,
            "strategy_pilot": StrategyPilotAgent,
            "product_historian": ProductHistorianAgent,
            "market_analyst": MarketAnalystAgent,
            
            # Content & Communication Agents (4)
            "content_designer": ContentDesignerAgent,
            "deck_narrator": DeckNarratorAgent,
            "portfolio_editor": PortfolioEditorAgent,
            "research_summarizer": ResearchSummarizerAgent,
            
            # Component & System Agents (3)
            "component_librarian": ComponentLibrarianAgent,
            "ai_interaction_designer": AIInteractionDesignerAgent,
            "workflow_optimizer": WorkflowOptimizerAgent,
            
            # Intelligence & Orchestration Agents (4)
            "evaluator": EvaluatorAgent,
            "prompt_master": PromptMasterAgent,
            "dispatcher": DispatcherAgent,
            "strategy_archivist": StrategyArchivistAgent,
            
            # Feedback & Analysis Agents (1)
            "feedback_amplifier": FeedbackAmplifierAgent,
            
            # Additional Combined Agents (9)
            "surprisal_critic": SurprisalCriticAgent,
            "narrative_divergence": NarrativeDivergenceAgent,
            "rewrite_loop": RewriteLoopAgent,
            "prompt_architect": PromptArchitectAgent,
            "design_polish_agent": DesignPolishAgent,
            "longform_creative_chain": LongformCreativeChain,
            "narrative_freshness_rater": NarrativeFreshnessRater,
            "structural_clarity_checker": StructuralClarityChecker,
            "voice_match_evaluator": VoiceMatchEvaluator,
            "rewrite_advisor": RewriteAdvisor,
            "narrative_quality_chain": NarrativeQualityChain,
            "autocritique_loop": AutoCritiqueLoop,
            "design_judgment_engine": DesignJudgmentEngine,
            "ai_native_ux_designer": AINativeUXDesigner,
            "design_system_engineer": DesignSystemEngineer
        }
        
        if args.agent in agent_map:
            # All agents are now working
            agent_class = agent_map[args.agent]
            agent = agent_class()
            agent_name = args.agent
            result = await risk_aware_agent_runner(input_text, agent, agent_name)
            
            if result.get("routed", False):
                print(f"🔁 Pattern override applied to {agent_name}")
                print(f"🎨 Output from {agent_name}:\n{result['agent_output']}")
            else:
                print(f"🎨 Output from {agent_name}:\n{result['agent_output']}")
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
        
        # Core Design Agents (6)
        orchestrator.register_agent("vp_design", VPDesignAgent())
        orchestrator.register_agent("creative_director", CreativeDirectorAgent())
        orchestrator.register_agent("design_technologist", DesignTechnologistAgent())
        orchestrator.register_agent("principal_designer", PrincipalDesignerAgent())
        orchestrator.register_agent("vp_of_design", VPOfDesignAgent())
        orchestrator.register_agent("vp_of_product", VPOfProductAgent())
        
        # Strategy & Product Agents (4)
        orchestrator.register_agent("product_navigator", ProductNavigatorAgent())
        orchestrator.register_agent("strategy_pilot", StrategyPilotAgent())
        orchestrator.register_agent("product_historian", ProductHistorianAgent())
        orchestrator.register_agent("market_analyst", MarketAnalystAgent())
        
        # Content & Communication Agents (4)
        orchestrator.register_agent("content_designer", ContentDesignerAgent())
        orchestrator.register_agent("deck_narrator", DeckNarratorAgent())
        orchestrator.register_agent("portfolio_editor", PortfolioEditorAgent())
        orchestrator.register_agent("research_summarizer", ResearchSummarizerAgent())
        
        # Component & System Agents (3)
        orchestrator.register_agent("component_librarian", ComponentLibrarianAgent())
        orchestrator.register_agent("ai_interaction_designer", AIInteractionDesignerAgent())
        orchestrator.register_agent("workflow_optimizer", WorkflowOptimizerAgent())
        
        # Intelligence & Orchestration Agents (4)
        orchestrator.register_agent("evaluator", EvaluatorAgent())
        orchestrator.register_agent("prompt_master", PromptMasterAgent())
        orchestrator.register_agent("dispatcher", DispatcherAgent())
        orchestrator.register_agent("strategy_archivist", StrategyArchivistAgent())
        
        # Feedback & Analysis Agents (2)
        orchestrator.register_agent("feedback_amplifier", FeedbackAmplifierAgent())
        
        # Additional Combined Agents (9)
        orchestrator.register_agent("surprisal_critic", SurprisalCriticAgent())
        orchestrator.register_agent("narrative_divergence", NarrativeDivergenceAgent())
        orchestrator.register_agent("rewrite_loop", RewriteLoopAgent())
        orchestrator.register_agent("prompt_architect", PromptArchitectAgent())
        orchestrator.register_agent("design_polish_agent", DesignPolishAgent())
        orchestrator.register_agent("longform_creative_chain", LongformCreativeChain())
        orchestrator.register_agent("narrative_freshness_rater", NarrativeFreshnessRater())
        orchestrator.register_agent("structural_clarity_checker", StructuralClarityChecker())
        orchestrator.register_agent("voice_match_evaluator", VoiceMatchEvaluator())
        orchestrator.register_agent("rewrite_advisor", RewriteAdvisor())
        orchestrator.register_agent("narrative_quality_chain", NarrativeQualityChain())
        
        # Register tools
        orchestrator.register_tool("ux_audit", UXAuditTool())
        orchestrator.register_tool("trust_explainer", TrustExplainerTool())
        
        # Execute pipeline
        agent_sequence = ["vp_design", "evaluator", "rewrite_loop"]
        result = await orchestrator.execute_pipeline(input_text, agent_sequence)
        print("🎨 Pipeline Result:")
        print(json.dumps(result, indent=2))
    
    elif args.command == "chain":
        if not args.input:
            print("❌ Error: 'chain' command requires input")
            sys.exit(1)
        
        chain_name = args.chain_name
        input_text = " ".join(args.input)
        print(f"🔄 Executing chain '{chain_name}' on: {input_text}")
        
        # Import choreographer
        from agent_choreographer import get_choreographer
        choreographer = get_choreographer()
        
        # Get agent map (same as in run command)
        agent_map = {
            # Core Design Agents (6)
            "vp_design": VPDesignAgent,
            "creative_director": CreativeDirectorAgent,
            "design_technologist": DesignTechnologistAgent,
            "principal_designer": PrincipalDesignerAgent,
            "vp_of_design": VPOfDesignAgent,
            "vp_of_product": VPOfProductAgent,
            
            # Strategy & Product Agents (4)
            "product_navigator": ProductNavigatorAgent,
            "strategy_pilot": StrategyPilotAgent,
            "product_historian": ProductHistorianAgent,
            "market_analyst": MarketAnalystAgent,
            
            # Content & Communication Agents (4)
            "content_designer": ContentDesignerAgent,
            "deck_narrator": DeckNarratorAgent,
            "portfolio_editor": PortfolioEditorAgent,
            "research_summarizer": ResearchSummarizerAgent,
            
            # Component & System Agents (3)
            "component_librarian": ComponentLibrarianAgent,
            "ai_interaction_designer": AIInteractionDesignerAgent,
            "workflow_optimizer": WorkflowOptimizerAgent,
            
            # Intelligence & Orchestration Agents (4)
            "evaluator": EvaluatorAgent,
            "prompt_master": PromptMasterAgent,
            "dispatcher": DispatcherAgent,
            "strategy_archivist": StrategyArchivistAgent,
            
            # Feedback & Analysis Agents (1)
            "feedback_amplifier": FeedbackAmplifierAgent,
            
            # Additional Combined Agents (9)
            "surprisal_critic": SurprisalCriticAgent,
            "narrative_divergence": NarrativeDivergenceAgent,
            "rewrite_loop": RewriteLoopAgent,
            "prompt_architect": PromptArchitectAgent,
            "design_polish_agent": DesignPolishAgent,
            "longform_creative_chain": LongformCreativeChain,
            "narrative_freshness_rater": NarrativeFreshnessRater,
            "structural_clarity_checker": StructuralClarityChecker,
            "voice_match_evaluator": VoiceMatchEvaluator,
            "rewrite_advisor": RewriteAdvisor,
            "narrative_quality_chain": NarrativeQualityChain,
            "autocritique_loop": AutoCritiqueLoop,
            "design_judgment_engine": DesignJudgmentEngine,
            "ai_native_ux_designer": AINativeUXDesigner,
            "design_system_engineer": DesignSystemEngineer
        }
        
        # Execute chain
        result = await choreographer.execute_chain(chain_name, input_text, agent_map, args.debug)
        print("🎬 Chain Result:")
        print(json.dumps(result, indent=2))
    
    elif args.command == "test-pattern":
        if not args.input:
            print("❌ Error: 'test-pattern' command requires input")
            sys.exit(1)
        
        agent_name = args.agent_name
        pattern_name = args.pattern_name
        input_text = " ".join(args.input)
        
        print(f"🧪 Testing pattern '{pattern_name}' on agent '{agent_name}'")
        
        # Import pattern tester
        from pattern_tester import get_pattern_tester
        tester = get_pattern_tester()
        
        # Get agent map (same as in chain command)
        agent_map = {
            # Core Design Agents (6)
            "vp_design": VPDesignAgent,
            "creative_director": CreativeDirectorAgent,
            "design_technologist": DesignTechnologistAgent,
            "principal_designer": PrincipalDesignerAgent,
            "vp_of_design": VPOfDesignAgent,
            "vp_of_product": VPOfProductAgent,
            
            # Strategy & Product Agents (4)
            "product_navigator": ProductNavigatorAgent,
            "strategy_pilot": StrategyPilotAgent,
            "product_historian": ProductHistorianAgent,
            "market_analyst": MarketAnalystAgent,
            
            # Content & Communication Agents (4)
            "content_designer": ContentDesignerAgent,
            "deck_narrator": DeckNarratorAgent,
            "portfolio_editor": PortfolioEditorAgent,
            "research_summarizer": ResearchSummarizerAgent,
            
            # Component & System Agents (3)
            "component_librarian": ComponentLibrarianAgent,
            "ai_interaction_designer": AIInteractionDesignerAgent,
            "workflow_optimizer": WorkflowOptimizerAgent,
            
            # Intelligence & Orchestration Agents (4)
            "evaluator": EvaluatorAgent,
            "prompt_master": PromptMasterAgent,
            "dispatcher": DispatcherAgent,
            "strategy_archivist": StrategyArchivistAgent,
            
            # Feedback & Analysis Agents (1)
            "feedback_amplifier": FeedbackAmplifierAgent,
            
            # Additional Combined Agents (9)
            "surprisal_critic": SurprisalCriticAgent,
            "narrative_divergence": NarrativeDivergenceAgent,
            "rewrite_loop": RewriteLoopAgent,
            "prompt_architect": PromptArchitectAgent,
            "design_polish_agent": DesignPolishAgent,
            "longform_creative_chain": LongformCreativeChain,
            "narrative_freshness_rater": NarrativeFreshnessRater,
            "structural_clarity_checker": StructuralClarityChecker,
            "voice_match_evaluator": VoiceMatchEvaluator,
            "rewrite_advisor": RewriteAdvisor,
            "narrative_quality_chain": NarrativeQualityChain,
            "autocritique_loop": AutoCritiqueLoop,
            "design_judgment_engine": DesignJudgmentEngine,
            "ai_native_ux_designer": AINativeUXDesigner,
            "design_system_engineer": DesignSystemEngineer
        }
        
        # Test the pattern
        try:
            result = await tester.test_pattern_override(agent_name, input_text, pattern_name, agent_map)
            print("\n🧪 Pattern Test Complete!")
            
            # Show summary
            summary = tester.get_test_summary()
            print(f"📊 Session Summary: {summary['total_tests']} tests, avg effectiveness: {summary['average_effectiveness']}")
            
        except ValueError as e:
            print(f"❌ Error: {e}")
            print(f"🎯 Available agents: {', '.join(tester.get_available_agents()[:10])}...")
            print(f"🔄 Available patterns: {', '.join(tester.get_available_patterns())}")
            sys.exit(1)
    
    elif args.command == "voice":
        agent_name = args.agent_name
        method = args.method
        duration = args.duration
        
        print(f"🎤 Voice Input for agent '{agent_name}'")
        
        # Import voice input
        from voice_input import get_voice_input
        voice_input = get_voice_input()
        
        # Show available methods
        methods = voice_input.get_available_methods()
        print(f"🔊 Available methods: {[k for k, v in methods.items() if v]}")
        
        # Get agent map (same as other commands)
        agent_map = {
            # Core Design Agents (6)
            "vp_design": VPDesignAgent,
            "creative_director": CreativeDirectorAgent,
            "design_technologist": DesignTechnologistAgent,
            "principal_designer": PrincipalDesignerAgent,
            "vp_of_design": VPOfDesignAgent,
            "vp_of_product": VPOfProductAgent,
            
            # Strategy & Product Agents (4)
            "product_navigator": ProductNavigatorAgent,
            "strategy_pilot": StrategyPilotAgent,
            "product_historian": ProductHistorianAgent,
            "market_analyst": MarketAnalystAgent,
            
            # Content & Communication Agents (4)
            "content_designer": ContentDesignerAgent,
            "deck_narrator": DeckNarratorAgent,
            "portfolio_editor": PortfolioEditorAgent,
            "research_summarizer": ResearchSummarizerAgent,
            
            # Component & System Agents (3)
            "component_librarian": ComponentLibrarianAgent,
            "ai_interaction_designer": AIInteractionDesignerAgent,
            "workflow_optimizer": WorkflowOptimizerAgent,
            
            # Intelligence & Orchestration Agents (4)
            "evaluator": EvaluatorAgent,
            "prompt_master": PromptMasterAgent,
            "dispatcher": DispatcherAgent,
            "strategy_archivist": StrategyArchivistAgent,
            
            # Feedback & Analysis Agents (1)
            "feedback_amplifier": FeedbackAmplifierAgent,
            
            # Additional Combined Agents (9)
            "surprisal_critic": SurprisalCriticAgent,
            "narrative_divergence": NarrativeDivergenceAgent,
            "rewrite_loop": RewriteLoopAgent,
            "prompt_architect": PromptArchitectAgent,
            "design_polish_agent": DesignPolishAgent,
            "longform_creative_chain": LongformCreativeChain,
            "narrative_freshness_rater": NarrativeFreshnessRater,
            "structural_clarity_checker": StructuralClarityChecker,
            "voice_match_evaluator": VoiceMatchEvaluator,
            "rewrite_advisor": RewriteAdvisor,
            "narrative_quality_chain": NarrativeQualityChain,
            "autocritique_loop": AutoCritiqueLoop,
            "design_judgment_engine": DesignJudgmentEngine,
            "ai_native_ux_designer": AINativeUXDesigner,
            "design_system_engineer": DesignSystemEngineer
        }
        
        # Process voice input
        try:
            result = await voice_input.process_voice_input(agent_name, agent_map, method, duration)
            
            if result["success"]:
                print("\n🎉 Voice Input Complete!")
                print(f"📝 Transcript: {result['transcript']}")
                print(f"🤖 Agent: {result['agent_name']}")
                print(f"⚠️  Risk Score: {result['risk_score']:.2f}")
                print(f"🎙️  Method: {result['method_used']}")
                
                # Show agent output summary
                agent_output = result.get("agent_output", {})
                if isinstance(agent_output, dict) and "output" in agent_output:
                    output_preview = str(agent_output["output"])[:200]
                    print(f"🎨 Output Preview: {output_preview}{'...' if len(str(agent_output['output'])) > 200 else ''}")
                
                # Show session summary
                summary = voice_input.get_session_summary()
                print(f"📊 Session Summary: {summary['total_sessions']} sessions, {summary['success_rate']*100:.1f}% success rate")
            else:
                print(f"❌ Voice input failed: {result.get('error', 'Unknown error')}")
                
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)

    else:
        print("❌ Error: Unknown command. Use 'run' or 'pipeline'")
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    print("🧠 DEBUG: Entering main()")
    asyncio.run(main()) 