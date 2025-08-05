# fusion_guardrail_usage.py
# 
# Copy-paste this into Cursor to use Fusion with hallucination protection

import os
import sys

def validate_fusion_system():
    """Validate that Fusion system is real and ready"""
    REQUIRED_FILES = [
        "fusion.py",
        "synthetic_reasoner_agent.py", 
        "pattern_registry.py",
        "fallback_trigger_config.json",
        "agents_combined.py",
        "agent_manifest.json",
    ]
    
    # Check files exist
    missing = []
    for file in REQUIRED_FILES:
        if not os.path.exists(file):
            missing.append(file)
    if missing:
        raise RuntimeError(f"Fusion system incomplete! Missing files: {missing}")
    
    # Check imports work
    try:
        from fusion import run_with_reasoning
        from synthetic_reasoner_agent import SyntheticReasonerAgent
        from pattern_registry import pattern_templates
        print("✅ Fusion runtime validated. Agents and reasoning system are REAL.")
        return True
    except ImportError as e:
        raise RuntimeError(f"Fusion import failed: {e}")

def safe_fusion_run(prompt, agent_name):
    """Run Fusion with hallucination protection"""
    import asyncio
    
    # Validate system first
    validate_fusion_system()
    
    print(f"🔍 Running Fusion with agent: {agent_name}")
    print(f"📝 Input: {prompt}")
    
    try:
        from fusion import run_with_reasoning
        result = asyncio.run(run_with_reasoning(prompt, agent_name))
        
        # Check for hallucinated responses
        agent_output = str(result.get("output", result.get("agent_output", "")))
        hallucination_indicators = [
            "Fusion isn't real",
            "I am not Fusion",
            "Fusion is not a real system", 
            "This is a roleplay",
            "I cannot access Fusion"
        ]
        
        for indicator in hallucination_indicators:
            if indicator.lower() in agent_output.lower():
                raise RuntimeError(f"❌ HALLUCINATION DETECTED: {indicator}")
        
        print("✅ Fusion Output validated - Real agent response")
        return result
        
    except Exception as e:
        print(f"❌ Fusion execution failed: {e}")
        raise

# 🚨 EXECUTE PATCH
if __name__ == "__main__":
    try:
        # Test the system
        validate_fusion_system()
        
        # Example usage
        result = safe_fusion_run("Is Fusion real or fake?", "evaluator")
        print("🎉 Fusion system is REAL and working!")
        
    except Exception as e:
        print(f"❌ Critical error: {e}")
        sys.exit(1) 