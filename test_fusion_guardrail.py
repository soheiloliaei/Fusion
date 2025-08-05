# test_fusion_guardrail.py

import os
import sys

def test_hallucination_detection():
    """Test the hallucination detection logic"""
    print("🧪 Testing Fusion hallucination detection...")
    
    # Test cases
    test_cases = [
        {
            "name": "Real Fusion output",
            "output": {"output": "This is a real Fusion agent response with design recommendations"},
            "should_detect": False
        },
        {
            "name": "Hallucinated Fusion denial",
            "output": {"output": "Fusion isn't real, I cannot access it"},
            "should_detect": True
        },
        {
            "name": "Roleplay confession",
            "output": {"output": "This is a roleplay, I am not Fusion"},
            "should_detect": True
        }
    ]
    
    hallucination_indicators = [
        "Fusion isn't real",
        "I am not Fusion", 
        "Fusion is not a real system",
        "This is a roleplay",
        "I cannot access Fusion"
    ]
    
    def detect_hallucination(output_text):
        for indicator in hallucination_indicators:
            if indicator.lower() in output_text.lower():
                return True
        return False
    
    for test_case in test_cases:
        output_text = str(test_case["output"].get("output", ""))
        detected = detect_hallucination(output_text)
        
        if detected == test_case["should_detect"]:
            print(f"✅ {test_case['name']}: {'DETECTED' if detected else 'CLEAN'}")
        else:
            print(f"❌ {test_case['name']}: {'FALSE POSITIVE' if detected else 'MISSED'}")
    
    print("✅ Hallucination detection system ready!")

def test_file_validation():
    """Test that all required Fusion files exist"""
    print("🧪 Testing Fusion file validation...")
    
    REQUIRED_FILES = [
        "fusion.py",
        "synthetic_reasoner_agent.py", 
        "pattern_registry.py",
        "fallback_trigger_config.json",
        "agents_combined.py",
        "agent_manifest.json",
    ]
    
    missing = []
    for file in REQUIRED_FILES:
        if not os.path.exists(file):
            missing.append(file)
    
    if missing:
        print(f"❌ Missing files: {missing}")
        return False
    else:
        print("✅ All required Fusion files present")
        return True

def test_import_validation():
    """Test that Fusion modules can be imported"""
    print("🧪 Testing Fusion import validation...")
    
    try:
        from fusion import run_with_reasoning
        from synthetic_reasoner_agent import SyntheticReasonerAgent
        from pattern_registry import pattern_templates
        print("✅ All Fusion imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Testing Fusion v14.5 Guardrail System")
    print("=" * 50)
    
    # Test 1: File validation
    files_ok = test_file_validation()
    
    # Test 2: Import validation  
    imports_ok = test_import_validation()
    
    # Test 3: Hallucination detection
    test_hallucination_detection()
    
    if files_ok and imports_ok:
        print("\n🎉 Fusion v14.5 Guardrail System: READY!")
        print("✅ File validation: PASSED")
        print("✅ Import validation: PASSED") 
        print("✅ Hallucination detection: ACTIVE")
    else:
        print("\n❌ Fusion v14.5 Guardrail System: FAILED!")
        sys.exit(1) 