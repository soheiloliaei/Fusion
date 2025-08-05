#!/usr/bin/env python3
"""
Fusion v14.5 - AI-Native Operating System
Programmable agent OS with universal prompt handling
"""

import argparse
import asyncio
import sys
import json

# Import agents from combined file
from agents_combined import (
    VPDesignAgent, EvaluatorAgent, CreativeDirectorAgent, DesignTechnologistAgent,
    ProductNavigatorAgent, StrategyPilotAgent, VPOfDesignAgent, VPOfProductAgent,
    PromptMasterAgent, DispatcherAgent, PrincipalDesignerAgent, ComponentLibrarianAgent,
    ContentDesignerAgent, AIInteractionDesignerAgent, StrategyArchivistAgent,
    MarketAnalystAgent, WorkflowOptimizerAgent, ProductHistorianAgent,
    DeckNarratorAgent, PortfolioEditorAgent, ResearchSummarizerAgent, FeedbackAmplifierAgent
)
from core.execution_orchestrator_v14 import ExecutionOrchestrator

# Import Sprint 5-9 components
from synthetic_reasoner_agent import SyntheticReasonerAgent

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

# Universal handler for Cursor integration
def get_agent_by_name(agent_name: str):
    """Get agent instance by name"""
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
        "dispatcher": DispatcherAgent,
    }
    
    agent_class = agent_map.get(agent_name)
    if not agent_class:
        raise ValueError(f"Unknown agent: {agent_name}")
    return agent_class()

def get_fallback_config():
    """Load fallback configuration"""
    try:
        with open("fallback_trigger_config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "risk_threshold": 0.65,
            "default_fallback_agent": "rewrite_loop",
            "pattern_routing": {
                "vp_design": "fallback_clarify_then_critique",
                "evaluator": "fallback_metric_narrative",
                "creative_director": "fallback_soften_for_exec"
            }
        }

def get_pattern_templates():
    """Get pattern templates"""
    return {
        "fallback_clarify_then_critique": "First clarify ambiguous terms. Then critique the design proposal step by step.",
        "fallback_metric_narrative": "Evaluate this with accessibility, hierarchy, and visual clarity scores, then explain each.",
        "fallback_soften_for_exec": "Rewrite this in a way that sounds less critical and more executive-friendly.",
        "fallback_safe_design": "Propose only minimal, conservative improvements to avoid unintended harm.",
        "fallback_user_centric": "Focus on user needs and accessibility in all recommendations.",
        "fallback_systematic": "Use systematic methodology with clear steps and reasoning."
    }

async def handle_user_prompt(user_input: str, agent_name: str):
    """
    Universal handler for all user prompts in Cursor
    Provides full synthetic reasoning, risk assessment, and fallback routing
    """
    print(f"\n🚀 FUSION v14.5 - Processing: {agent_name}")
    print(f"📝 Input: {user_input}")
    print("=" * 60)
    
    # Step 1: Synthetic Reasoning
    reasoner = SyntheticReasonerAgent()
    synthetic_meta = reasoner.run(user_input, agent_name)
    
    # Step 2: Display Debug Information
    print("\n🧠 SYNTHETIC REASONING:")
    print("💭 Synthetic Thoughts:")
    for i, thought in enumerate(synthetic_meta["synthetic_thoughts"], 1):
        print(f"  {i}. {thought}")
    
    print("\n❓ Internal Questions:")
    for i, question in enumerate(synthetic_meta["synthetic_queries"], 1):
        print(f"  {i}. {question}")
    
    print(f"\n⚠️  Risk Score: {synthetic_meta['risk_score']:.2f}")
    
    # Step 3: Risk Assessment and Pattern Routing
    config = get_fallback_config()
    risk_threshold = config.get("risk_threshold", 0.65)
    pattern_templates = get_pattern_templates()
    
    # Get agent instance
    agent = get_agent_by_name(agent_name)
    
    # Check if risk is high enough to trigger fallback
    if synthetic_meta["risk_score"] > risk_threshold:
        fallback_pattern = config["pattern_routing"].get(agent_name, "fallback_clarify_then_critique")
        pattern_prompt = pattern_templates.get(fallback_pattern, "")
        
        print(f"\n🔁 RISK TRIGGERED FALLBACK:")
        print(f"   Pattern: {fallback_pattern}")
        print(f"   Threshold: {risk_threshold:.2f} (Risk: {synthetic_meta['risk_score']:.2f})")
        print(f"   Applied: {pattern_prompt}")
        
        modified_input = f"{pattern_prompt}\n\n{user_input}"
        print(f"\n📝 Modified Input: {modified_input[:100]}...")
        
        # Run agent with pattern override
        try:
            if hasattr(agent, 'run_async'):
                result = await agent.run_async(modified_input, {})
            else:
                result = await agent.run(modified_input)
        except Exception as e:
            print(f"❌ Agent execution failed: {e}")
            result = f"Error: {e}"
    else:
        print(f"\n✅ NORMAL EXECUTION (Risk: {synthetic_meta['risk_score']:.2f} < {risk_threshold:.2f})")
        
        # Run agent normally
        try:
            if hasattr(agent, 'run_async'):
                result = await agent.run_async(user_input, {})
            else:
                result = await agent.run(user_input)
        except Exception as e:
            print(f"❌ Agent execution failed: {e}")
            result = f"Error: {e}"
    
    # Step 4: Display Results
    print("\n" + "=" * 60)
    print("🎯 AGENT OUTPUT:")
    print(result)
    print("=" * 60)
    
    return {
        "synthetic_meta": synthetic_meta,
        "risk_triggered_fallback": synthetic_meta["risk_score"] > risk_threshold,
        "fallback_pattern": config["pattern_routing"].get(agent_name, "fallback_clarify_then_critique") if synthetic_meta["risk_score"] > risk_threshold else None,
        "agent_output": result
    }

# -------------------------------
# 🧠 FUSION NATURAL PROMPT PARSER
# -------------------------------

# This allows you to run Fusion with natural language like:
#   "using Fusion: design a support tile for Bitcoin errors"
#   "activate Fusion with evaluator: critique this concept"
#   "activate Fusion chain: design_pipeline for a new Gen Z wallet"
# Instead of writing: await handle_user_prompt(...)

import re

# 🧩 Main parser function
def parse_and_run(prompt: str):
    """
    Takes a natural language command and routes it to the correct Fusion call.
    Supported formats:
    - 'using Fusion: [prompt]'
    - 'activate Fusion with [agent_name]: [prompt]'
    - 'activate Fusion chain: [chain_name] for [goal]'
    """
    prompt = prompt.strip()

    # Match "activate Fusion chain: design_pipeline for XYZ"
    match_chain = re.match(r"(using|activate) fusion chain: (\w+)(?: for| to)? (.+)", prompt, re.IGNORECASE)
    if match_chain:
        _, chain_name, goal = match_chain.groups()
        print(f"🔄 Running Fusion chain: {chain_name} for goal: {goal}")
        # For now, route to vp_design agent since we don't have chain implementation yet
        return asyncio.run(handle_user_prompt(goal.strip(), "vp_design"))

    # Match "activate Fusion with agent_name: prompt"
    match_agent = re.match(r"(using|activate) fusion(?: with (\w+))?: (.+)", prompt, re.IGNORECASE)
    if match_agent:
        _, agent_name, content = match_agent.groups()
        agent_name = agent_name or "vp_design"
        print(f"🔄 Running Fusion with agent: {agent_name}")
        return asyncio.run(handle_user_prompt(content.strip(), agent_name.strip()))

    # Fallback if format not recognized
    raise ValueError(
        "🛑 Prompt not recognized. Try:\n"
        "- using Fusion: [your task]\n"
        "- activate Fusion with [agent]: [your task]\n"
        "- activate Fusion chain: [chain] for [your goal]"
    )

# -------------------------------
# ✅ END OF NATURAL PROMPT PARSER
# -------------------------------

if __name__ == "__main__":
    print("🧠 DEBUG: Entering main()")
    main() 