#!/usr/bin/env python3
"""
Fusion Web App - Streamlit Frontend for Agent Selection, Chaining, Pattern Testing, and Voice Input
"""

import streamlit as st
import asyncio
import json
import sys
import os
from typing import Dict, Any, List
from datetime import datetime

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import Fusion modules
try:
    from debug_ui import get_debug_summary, save_debug_session, set_debug_verbose
    from agent_choreographer import get_choreographer
    from pattern_tester import get_pattern_tester
    from voice_input import get_voice_input
    from pattern_registry import pattern_templates
    
    # Load fallback config
    try:
        with open("fallback_trigger_config.json", "r") as f:
            fallback_config = json.load(f)
    except FileNotFoundError:
        fallback_config = {"risk_threshold": 0.65}
except ImportError as e:
    st.error(f"Failed to import Fusion modules: {e}")
    st.stop()

# Import all agent classes
try:
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
    
    from agents_combined import (
        SurprisalCriticAgent, NarrativeDivergenceAgent, LongformCreativeChain,
        NarrativeFreshnessRater, StructuralClarityChecker, VoiceMatchEvaluator,
        RewriteAdvisor, NarrativeQualityChain, RewriteLoopAgent,
        DesignJudgmentEngine, PromptArchitectAgent, AINativeUXDesigner, 
        DesignPolishAgent, DesignSystemEngineer
    )
    
    from autocritique_loop import AutoCritiqueLoop
    
    from fusion import risk_aware_agent_runner
except ImportError as e:
    st.error(f"Failed to import agent modules: {e}")
    st.stop()

# Agent map for web app
AGENT_MAP = {
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

def init_session_state():
    """Initialize session state variables"""
    if 'debug_enabled' not in st.session_state:
        st.session_state.debug_enabled = False
    if 'last_result' not in st.session_state:
        st.session_state.last_result = None

def run_async_in_streamlit(coro):
    """Run async function in Streamlit"""
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    return loop.run_until_complete(coro)

def page_run():
    """Page for running individual agents"""
    st.header("🤖 Run Agent")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        agent_name = st.selectbox(
            "Select Agent",
            options=list(AGENT_MAP.keys()),
            help="Choose an agent to run"
        )
        
        input_prompt = st.text_area(
            "Input Prompt",
            height=100,
            placeholder="Enter your prompt here..."
        )
        
        debug_mode = st.checkbox("Enable debug output", value=st.session_state.debug_enabled)
        st.session_state.debug_enabled = debug_mode
        set_debug_verbose(debug_mode)
    
    with col2:
        st.subheader("Agent Info")
        if agent_name in AGENT_MAP:
            # Get agent description from manifest
            try:
                with open("agent_manifest.json", "r") as f:
                    manifest = json.load(f)
                    agent_info = manifest.get(agent_name, {})
                    st.write(f"**Role:** {agent_info.get('role', 'No description available')}")
                    st.write(f"**Fallback:** {agent_info.get('fallback_pattern', 'None')}")
            except FileNotFoundError:
                st.write("Agent manifest not found")
    
    if st.button("🚀 Run Agent", type="primary"):
        if not input_prompt.strip():
            st.error("Please enter a prompt")
            return
        
        with st.spinner(f"Running {agent_name}..."):
            try:
                # Get agent and run
                agent_class = AGENT_MAP[agent_name]
                agent = agent_class()
                
                result = run_async_in_streamlit(
                    risk_aware_agent_runner(input_prompt, agent, agent_name)
                )
                
                st.session_state.last_result = result
                
                # Display results
                st.success("✅ Agent completed successfully!")
                
                # Show synthetic meta if debug enabled
                if debug_mode:
                    st.subheader("🧠 Synthetic Reasoning")
                    synthetic_meta = result.get("synthetic_meta", {})
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Risk Score", f"{synthetic_meta.get('risk_score', 0):.2f}")
                    with col2:
                        st.metric("Pattern Triggered", "Yes" if result.get("routed", False) else "No")
                    
                    with st.expander("Synthetic Thoughts"):
                        for thought in synthetic_meta.get("synthetic_thoughts", []):
                            st.write(f"• {thought}")
                    
                    with st.expander("Internal Questions"):
                        for query in synthetic_meta.get("synthetic_queries", []):
                            st.write(f"→ {query}")
                
                # Show agent output
                st.subheader("🎨 Agent Output")
                agent_output = result.get("agent_output", {})
                
                if isinstance(agent_output, dict) and "output" in agent_output:
                    st.markdown(agent_output["output"])
                    
                    # Show additional details in expander
                    with st.expander("Additional Details"):
                        st.json(agent_output)
                else:
                    st.json(agent_output)
                
            except Exception as e:
                st.error(f"Error running agent: {str(e)}")

def page_chain():
    """Page for running agent chains"""
    st.header("🔗 Agent Chains")
    
    choreographer = get_choreographer()
    available_chains = choreographer.get_available_chains()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        chain_name = st.selectbox(
            "Select Chain",
            options=available_chains,
            help="Choose a predefined agent chain"
        )
        
        input_prompt = st.text_area(
            "Input Prompt",
            height=100,
            placeholder="Enter your prompt for the chain..."
        )
        
        debug_mode = st.checkbox("Enable debug output", value=st.session_state.debug_enabled)
    
    with col2:
        st.subheader("Chain Info")
        if chain_name:
            agents_in_chain = choreographer.get_chain_agents(chain_name)
            st.write(f"**Agents:** {len(agents_in_chain)}")
            for i, agent in enumerate(agents_in_chain, 1):
                st.write(f"{i}. {agent}")
    
    if st.button("⚡ Execute Chain", type="primary"):
        if not input_prompt.strip():
            st.error("Please enter a prompt")
            return
        
        with st.spinner(f"Executing chain '{chain_name}'..."):
            try:
                result = run_async_in_streamlit(
                    choreographer.execute_chain(chain_name, input_prompt, AGENT_MAP, debug_mode)
                )
                
                st.success(f"✅ Chain '{chain_name}' completed!")
                
                # Show chain summary
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Steps Completed", f"{result['agents_executed']}/{result['total_agents']}")
                with col2:
                    st.metric("Duration", f"{result['execution_duration']:.2f}s")
                with col3:
                    st.metric("Success", "✅" if result['success'] else "❌")
                
                # Show each step
                st.subheader("🔄 Chain Steps")
                for step_result in result['results']:
                    with st.expander(f"Step {step_result['step']}: {step_result['agent_name']}"):
                        if 'error' in step_result:
                            st.error(f"Error: {step_result['error']}")
                        else:
                            if debug_mode:
                                synthetic_meta = step_result.get('synthetic_meta', {})
                                st.write(f"**Risk Score:** {synthetic_meta.get('risk_score', 0):.2f}")
                            
                            output = step_result.get('output', {})
                            if isinstance(output, dict) and 'output' in output:
                                st.markdown(output['output'][:500] + ("..." if len(output['output']) > 500 else ""))
                            else:
                                st.write(str(output)[:500] + ("..." if len(str(output)) > 500 else ""))
                
            except Exception as e:
                st.error(f"Error executing chain: {str(e)}")

def page_patterns():
    """Page for testing fallback patterns"""
    st.header("🧩 Pattern Testing")
    
    tester = get_pattern_tester()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        agent_name = st.selectbox(
            "Select Agent",
            options=list(AGENT_MAP.keys()),
            help="Choose an agent to test patterns on"
        )
        
        pattern_name = st.selectbox(
            "Select Pattern",
            options=list(pattern_templates.keys()),
            help="Choose a fallback pattern to test"
        )
        
        input_prompt = st.text_area(
            "Test Prompt",
            height=100,
            placeholder="Enter a prompt to test the pattern with..."
        )
    
    with col2:
        st.subheader("Pattern Details")
        if pattern_name:
            pattern_content = pattern_templates.get(pattern_name, "")
            st.write(f"**Pattern:** {pattern_name}")
            st.text_area("Content", value=pattern_content, height=150, disabled=True)
    
    if st.button("🧪 Test Pattern", type="primary"):
        if not input_prompt.strip():
            st.error("Please enter a test prompt")
            return
        
        with st.spinner(f"Testing pattern '{pattern_name}' on '{agent_name}'..."):
            try:
                result = run_async_in_streamlit(
                    tester.test_pattern_override(agent_name, input_prompt, pattern_name, AGENT_MAP)
                )
                
                st.success("✅ Pattern test completed!")
                
                # Show effectiveness metrics
                effectiveness = result['comparison']['pattern_effectiveness']
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Effectiveness Score", f"{effectiveness['overall_score']:.2f}")
                with col2:
                    st.metric("Verdict", effectiveness['verdict'])
                with col3:
                    risk_change = result['comparison']['risk_score_change']
                    st.metric("Risk Change", f"{risk_change:+.2f}")
                
                # Show comparison
                st.subheader("📊 Comparison Results")
                
                tab1, tab2 = st.tabs(["Normal Execution", "Pattern Override"])
                
                with tab1:
                    normal_output = result['normal_execution']['output']
                    if isinstance(normal_output, dict) and 'output' in normal_output:
                        st.markdown(normal_output['output'])
                    else:
                        st.json(normal_output)
                
                with tab2:
                    pattern_output = result['pattern_execution']['output']
                    if isinstance(pattern_output, dict) and 'output' in pattern_output:
                        st.markdown(pattern_output['output'])
                    else:
                        st.json(pattern_output)
                
                # Show test summary
                summary = tester.get_test_summary()
                st.info(f"Session Summary: {summary['total_tests']} tests, avg effectiveness: {summary['average_effectiveness']}")
                
            except Exception as e:
                st.error(f"Error testing pattern: {str(e)}")

def page_voice():
    """Page for voice input"""
    st.header("🎤 Voice Input")
    
    voice_input = get_voice_input()
    available_methods = voice_input.get_available_methods()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        agent_name = st.selectbox(
            "Select Agent",
            options=list(AGENT_MAP.keys()),
            help="Choose an agent to process voice input"
        )
        
        method_options = [k for k, v in available_methods.items() if v]
        method = st.selectbox(
            "Input Method",
            options=method_options,
            help="Choose voice input method"
        )
        
        if method != "manual":
            duration = st.slider("Recording Duration (seconds)", min_value=1, max_value=30, value=5)
        else:
            duration = 5
            text_input = st.text_area(
                "Manual Text Input",
                height=100,
                placeholder="Enter text manually (since voice input isn't available)..."
            )
    
    with col2:
        st.subheader("Available Methods")
        for method_name, available in available_methods.items():
            status = "✅" if available else "❌"
            st.write(f"{status} {method_name}")
        
        st.subheader("Voice Settings")
        risk_threshold = st.slider("Risk Threshold", min_value=0.0, max_value=1.0, value=0.8, step=0.1)
        st.write("High-risk utterances above this threshold will require confirmation")
    
    if st.button("🎙️ Start Voice Input", type="primary"):
        if method == "manual" and not text_input.strip():
            st.error("Please enter text manually")
            return
        
        with st.spinner(f"Processing voice input with {agent_name}..."):
            try:
                if method == "manual":
                    # Simulate manual voice input
                    result = {
                        "success": True,
                        "transcript": text_input,
                        "agent_name": agent_name,
                        "method_used": "manual",
                        "duration": duration,
                        "risk_score": 0.3,  # Simulated
                        "high_risk": False,
                        "timestamp": datetime.now().isoformat()
                    }
                    
                    # Run the agent
                    agent_class = AGENT_MAP[agent_name]
                    agent = agent_class()
                    
                    agent_result = run_async_in_streamlit(
                        risk_aware_agent_runner(text_input, agent, agent_name)
                    )
                    
                    result.update({
                        "synthetic_meta": agent_result.get("synthetic_meta", {}),
                        "agent_output": agent_result.get("agent_output", {}),
                        "routed": agent_result.get("routed", False),
                        "risk_score": agent_result.get("synthetic_meta", {}).get("risk_score", 0.3)
                    })
                else:
                    result = run_async_in_streamlit(
                        voice_input.process_voice_input(agent_name, AGENT_MAP, method, duration, risk_threshold)
                    )
                
                if result["success"]:
                    st.success("✅ Voice input processed successfully!")
                    
                    # Show results
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Method", result["method_used"])
                    with col2:
                        st.metric("Risk Score", f"{result['risk_score']:.2f}")
                    with col3:
                        st.metric("High Risk", "⚠️" if result.get("high_risk", False) else "✅")
                    
                    # Show transcript
                    st.subheader("📝 Transcript")
                    st.text_area("Voice to Text", value=result["transcript"], height=100, disabled=True)
                    
                    # Show agent output
                    st.subheader("🤖 Agent Response")
                    agent_output = result.get("agent_output", {})
                    if isinstance(agent_output, dict) and "output" in agent_output:
                        st.markdown(agent_output["output"])
                    else:
                        st.json(agent_output)
                    
                    # Show session summary
                    summary = voice_input.get_session_summary()
                    st.info(f"Session Summary: {summary['total_sessions']} sessions, {summary['success_rate']*100:.1f}% success rate")
                else:
                    st.error(f"Voice input failed: {result.get('error', 'Unknown error')}")
                
            except Exception as e:
                st.error(f"Error processing voice input: {str(e)}")

def page_config():
    """Page for configuration management"""
    st.header("⚙️ Configuration")
    
    tab1, tab2, tab3 = st.tabs(["Fallback Config", "Agent Manifest", "Debug Logs"])
    
    with tab1:
        st.subheader("Fallback Trigger Configuration")
        
        try:
            with open("fallback_trigger_config.json", "r") as f:
                config = json.load(f)
            
            # Edit risk threshold
            new_threshold = st.slider(
                "Risk Threshold",
                min_value=0.0, max_value=1.0, 
                value=config.get("risk_threshold", 0.65),
                step=0.05
            )
            
            # Edit default fallback agent
            new_default = st.selectbox(
                "Default Fallback Agent",
                options=list(AGENT_MAP.keys()),
                index=list(AGENT_MAP.keys()).index(config.get("default_fallback_agent", "rewrite_loop")) if config.get("default_fallback_agent") in AGENT_MAP else 0
            )
            
            # Show pattern routing
            st.subheader("Pattern Routing")
            pattern_routing = config.get("pattern_routing", {})
            
            # Allow editing of pattern routing
            edited_routing = {}
            for agent, pattern in pattern_routing.items():
                new_pattern = st.selectbox(
                    f"Pattern for {agent}",
                    options=list(pattern_templates.keys()),
                    index=list(pattern_templates.keys()).index(pattern) if pattern in pattern_templates else 0,
                    key=f"pattern_{agent}"
                )
                edited_routing[agent] = new_pattern
            
            if st.button("💾 Save Configuration"):
                new_config = {
                    "risk_threshold": new_threshold,
                    "default_fallback_agent": new_default,
                    "pattern_routing": edited_routing
                }
                
                with open("fallback_trigger_config.json", "w") as f:
                    json.dump(new_config, f, indent=2)
                
                st.success("Configuration saved!")
                st.rerun()
        
        except FileNotFoundError:
            st.error("Fallback configuration file not found")
    
    with tab2:
        st.subheader("Agent Manifest")
        
        try:
            with open("agent_manifest.json", "r") as f:
                manifest = json.load(f)
            
            # Show agent information
            for agent_name, agent_info in manifest.items():
                with st.expander(f"{agent_name}"):
                    st.write(f"**Role:** {agent_info.get('role', 'No description')}")
                    st.write(f"**Fallback Pattern:** {agent_info.get('fallback_pattern', 'None')}")
        
        except FileNotFoundError:
            st.error("Agent manifest file not found")
    
    with tab3:
        st.subheader("Debug & Logs")
        
        # Debug summary
        summary = get_debug_summary()
        if summary['total_runs'] > 0:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Runs", summary['total_runs'])
            with col2:
                st.metric("Average Risk", f"{summary['average_risk']:.3f}")
            with col3:
                st.metric("Patterns Triggered", summary['patterns_triggered'])
            
            st.write(f"**Agents Used:** {', '.join(summary['agents_used'])}")
        else:
            st.info("No debug data available")
        
        if st.button("📁 Save Debug Session"):
            save_debug_session()
            st.success("Debug session saved!")

def main():
    """Main Streamlit app"""
    st.set_page_config(
        page_title="Fusion OS",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    init_session_state()
    
    # Sidebar navigation
    st.sidebar.title("🤖 Fusion OS")
    st.sidebar.markdown("AI-Native Design Intelligence System")
    
    page = st.sidebar.radio(
        "Navigate",
        ["🚀 Run Agent", "🔗 Agent Chains", "🧩 Pattern Testing", "🎤 Voice Input", "⚙️ Configuration"]
    )
    
    # Show system status
    st.sidebar.markdown("---")
    st.sidebar.subheader("System Status")
    st.sidebar.write(f"✅ Agents: {len(AGENT_MAP)}")
    st.sidebar.write(f"✅ Patterns: {len(pattern_templates)}")
    
    # Route to pages
    if page == "🚀 Run Agent":
        page_run()
    elif page == "🔗 Agent Chains":
        page_chain()
    elif page == "🧩 Pattern Testing":
        page_patterns()
    elif page == "🎤 Voice Input":
        page_voice()
    elif page == "⚙️ Configuration":
        page_config()

if __name__ == "__main__":
    main()