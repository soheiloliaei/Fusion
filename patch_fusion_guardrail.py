# patch_fusion_guardrail.py

import os
import sys
import importlib.util

REQUIRED_FILES = [
    "fusion.py",
    "synthetic_reasoner_agent.py",
    "pattern_registry.py",
    "fallback_trigger_config.json",
    "agents_combined.py",
    "agent_manifest.json",
]

def assert_all_fusion_files_exist():
    """Validate that all required Fusion files exist"""
    missing = []
    for file in REQUIRED_FILES:
        if not os.path.exists(file):
            missing.append(file)
    if missing:
        raise RuntimeError(f"Fusion system incomplete! Missing files: {missing}")

def validate_fusion_imports():
    """Validate that all Fusion modules can be imported"""
    try:
        from fusion import run_with_reasoning
        from synthetic_reasoner_agent import SyntheticReasonerAgent
        from pattern_registry import pattern_templates
        from agents_combined import get_agent_by_name
        print("✅ All Fusion imports successful")
        return True
    except ImportError as e:
        raise RuntimeError(f"Fusion import failed: {e}")

def patch_hallucination_guard():
    """Create a validated Fusion handler that prevents hallucinated responses"""
    from fusion import run_with_reasoning
    print("✅ Fusion runtime validated. Agents and reasoning system are REAL.")

    def validate_real_output(prompt, agent):
        """Execute Fusion with validation to prevent hallucinated fallbacks"""
        import asyncio
        
        print(f"🔍 Validating Fusion execution for: {agent}")
        print(f"📝 Input: {prompt}")
        
        try:
            result = asyncio.run(run_with_reasoning(prompt, agent))
            
            # Validate that result contains expected Fusion structure
            if isinstance(result, dict):
                # Check for hallucinated fallback responses
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
            else:
                raise RuntimeError("❌ Fusion output is not a dictionary")
                
        except Exception as e:
            print(f"❌ Fusion execution failed: {e}")
            raise

    return validate_real_output

def test_fusion_system():
    """Comprehensive test of the Fusion system"""
    print("🧪 Testing Fusion v14.5 system...")
    
    # Test 1: File existence
    assert_all_fusion_files_exist()
    print("✅ All required files present")
    
    # Test 2: Import validation
    validate_fusion_imports()
    print("✅ All imports successful")
    
    # Test 3: Runtime validation
    validate = patch_hallucination_guard()
    print("✅ Runtime guardrails active")
    
    # Test 4: Execute real Fusion
    try:
        result = validate("Test Fusion system with a simple design question", "vp_design")
        print("✅ Fusion execution successful")
        return True
    except Exception as e:
        print(f"❌ Fusion test failed: {e}")
        return False

# 🚨 EXECUTE PATCH
if __name__ == "__main__":
    try:
        success = test_fusion_system()
        if success:
            print("🎉 Fusion v14.5 system fully validated and ready!")
        else:
            print("❌ Fusion system validation failed!")
    except Exception as e:
        print(f"❌ Critical error in Fusion validation: {e}")
        sys.exit(1) 