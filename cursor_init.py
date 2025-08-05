# cursor_init.py
# Automatically runs at project load to make Fusion fully native inside Cursor

import sys
import os
import asyncio

def fusion_bootstrap():
    """Bootstrap Fusion v14.5 to be fully native in Cursor"""
    if os.getcwd() not in sys.path:
        sys.path.insert(0, os.getcwd())

    try:
        from fusion_guardrail_usage import validate_fusion_system, safe_fusion_run
        from fusion import run_with_reasoning

        # Validate the system
        validate_fusion_system()
        
        # Make Fusion functions globally available
        globals()["fusion"] = run_with_reasoning  # Direct function access
        globals()["ask"] = safe_fusion_run        # Friendly alias for natural prompts
        
        # Add chain functionality
        globals()["ask_chain"] = run_agent_chain  # Multi-agent chains
        
        # Add auto-agent selection
        globals()["ask_auto"] = auto_select_agent  # Automatic agent selection
        
        print("✅ Fusion v14.5 Loaded — Just use: ask('your prompt', 'agent')")
        print("🛡️ Guardrails, fallback, and debug are all ACTIVE")
        print("🔗 Chain support: ask_chain('prompt', ['agent1', 'agent2'])")
        print("🤖 Auto-agent: ask_auto('prompt') - automatically selects best agent")

    except Exception as e:
        print(f"❌ Failed to auto-load Fusion: {e}")

def run_agent_chain(prompt, agent_list):
    """Run multiple agents in sequence on the same prompt"""
    import asyncio
    from fusion_guardrail_usage import safe_fusion_run
    
    print(f"🔗 Running agent chain: {agent_list}")
    print(f"📝 Input: {prompt}")
    
    results = []
    for i, agent in enumerate(agent_list, 1):
        print(f"\n🔄 Step {i}: {agent}")
        try:
            result = asyncio.run(safe_fusion_run(prompt, agent))
            results.append({
                "agent": agent,
                "result": result
            })
            print(f"✅ {agent} completed")
        except Exception as e:
            print(f"❌ {agent} failed: {e}")
            results.append({
                "agent": agent,
                "error": str(e)
            })
    
    return {
        "prompt": prompt,
        "chain": agent_list,
        "results": results
    }

def auto_select_agent(prompt):
    """Automatically select the best agent based on prompt content"""
    import asyncio
    from fusion_guardrail_usage import safe_fusion_run
    from agents_combined import auto_select_agent as enhanced_auto_select
    
    selected_agent = enhanced_auto_select(prompt)
    print(f"🤖 Auto-selected agent: {selected_agent}")
    return asyncio.run(safe_fusion_run(prompt, selected_agent))

# Auto-bootstrap when imported
fusion_bootstrap()

# Also expose functions in the module namespace
__all__ = ['ask', 'ask_chain', 'ask_auto', 'fusion', 'run_agent_chain', 'auto_select_agent'] 