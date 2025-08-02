#!/usr/bin/env python3
"""
Test script to validate web app components
"""

import os
import sys
import json

def test_imports():
    """Test if all required modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        from debug_ui import get_debug_summary
        print("✅ debug_ui imported")
    except ImportError as e:
        print(f"❌ debug_ui import failed: {e}")
        return False
    
    try:
        from agent_choreographer import get_choreographer
        print("✅ agent_choreographer imported")
    except ImportError as e:
        print(f"❌ agent_choreographer import failed: {e}")
        return False
    
    try:
        from pattern_tester import get_pattern_tester
        print("✅ pattern_tester imported")
    except ImportError as e:
        print(f"❌ pattern_tester import failed: {e}")
        return False
    
    try:
        from voice_input import get_voice_input
        print("✅ voice_input imported")
    except ImportError as e:
        print(f"❌ voice_input import failed: {e}")
        return False
    
    try:
        from pattern_registry import pattern_templates
        print(f"✅ pattern_registry imported ({len(pattern_templates)} patterns)")
    except ImportError as e:
        print(f"❌ pattern_registry import failed: {e}")
        return False
    
    return True

def test_config_files():
    """Test if configuration files exist"""
    print("\n📁 Testing configuration files...")
    
    files_to_check = [
        "agent_manifest.json",
        "fallback_trigger_config.json",
        "agent_chains.json"
    ]
    
    all_exist = True
    for filename in files_to_check:
        if os.path.exists(filename):
            print(f"✅ {filename} exists")
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
                print(f"   📊 Contains {len(data)} items")
            except json.JSONDecodeError:
                print(f"   ⚠️  Invalid JSON in {filename}")
        else:
            print(f"❌ {filename} missing")
            all_exist = False
    
    return all_exist

def test_agent_imports():
    """Test if agent classes can be imported"""
    print("\n🤖 Testing agent imports...")
    
    agent_imports = [
        ("agents.vp_design_agent", "VPDesignAgent"),
        ("agents.evaluator_agent", "EvaluatorAgent"),
        ("agents.creative_director_agent", "CreativeDirectorAgent"),
        ("agents_combined", "RewriteLoopAgent"),
        ("agents_combined", "PromptArchitectAgent")
    ]
    
    success_count = 0
    for module_name, class_name in agent_imports:
        try:
            module = __import__(module_name, fromlist=[class_name])
            agent_class = getattr(module, class_name)
            print(f"✅ {class_name} imported from {module_name}")
            success_count += 1
        except ImportError as e:
            print(f"❌ Failed to import {class_name} from {module_name}: {e}")
        except AttributeError as e:
            print(f"❌ {class_name} not found in {module_name}: {e}")
    
    print(f"📊 Successfully imported {success_count}/{len(agent_imports)} agent classes")
    return success_count == len(agent_imports)

def test_async_functionality():
    """Test async functionality"""
    print("\n⚡ Testing async functionality...")
    
    try:
        import asyncio
        
        async def test_async():
            return "async works"
        
        # Test if we can run async code
        result = asyncio.run(test_async())
        print(f"✅ Async test passed: {result}")
        return True
    except Exception as e:
        print(f"❌ Async test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Fusion Web App Component Tests")
    print("="*50)
    
    tests = [
        ("Module Imports", test_imports),
        ("Configuration Files", test_config_files),
        ("Agent Imports", test_agent_imports),
        ("Async Functionality", test_async_functionality)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n🔍 {test_name}")
        print("-" * 30)
        result = test_func()
        results.append((test_name, result))
    
    print("\n" + "="*50)
    print("📊 TEST SUMMARY")
    print("="*50)
    
    all_passed = True
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
        if not result:
            all_passed = False
    
    print("\n" + "="*50)
    if all_passed:
        print("🎉 ALL TESTS PASSED! Web app components are ready.")
        print("🌐 You can now run: python3 start_web_app.py")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)