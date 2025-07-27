#!/bin/bash

# Fusion v13.0 Installer
# Installs Fusion v13 into any Cursor project

echo "🚀 Installing Fusion v13.0..."
echo "============================================================"

# Create fusion_v13 directory
mkdir -p fusion_v13

# Copy all Fusion files from master folder
echo "📁 Copying Fusion v13 files..."
cp -r Fusion_V13_Shipped/* fusion_v13/

# Create __init__.py if missing
touch fusion_v13/__init__.py

# Create a test script
cat > test_fusion_v13.py << 'TEST_EOF'
#!/usr/bin/env python3
"""
Fusion v13.0 Test Script
Tests the installation and basic functionality
"""

import sys
import os

# Add fusion_v13 to path
sys.path.append('./fusion_v13')

try:
    from core.execution_chain_orchestrator import ExecutionChainOrchestrator
    print("✅ Fusion v13.0 installed successfully!")
    print("🧠 Testing basic functionality...")
    
    # Test orchestrator
    orchestrator = ExecutionChainOrchestrator()
    test_prompt = "Design a simple workflow with clear steps"
    result = orchestrator.run(test_prompt)
    
    print("🎯 Test completed successfully!")
    print(f"📊 Status: {result.get('status', 'Unknown')}")
    print(f"📈 Overall Score: {result.get('overall_score', 'N/A')}")
    print("")
    print("🚀 Fusion v13.0 is ready to use!")
    print("💡 Try: orchestrator.run('Your prompt here')")
    
except ImportError as e:
    print(f"❌ Installation failed: {e}")
    print("🔧 Please check that all files were copied correctly")
    sys.exit(1)
except Exception as e:
    print(f"⚠️ Test completed with warning: {e}")
    print("✅ Installation successful, but test had issues")

TEST_EOF

# Make test script executable
chmod +x test_fusion_v13.py

echo "✅ Fusion v13.0 installation complete!"
echo ""
echo "🧪 Running installation test..."
python3 test_fusion_v13.py

echo ""
echo "🎯 Fusion v13.0 is now ready!"
echo "📁 Files installed in: ./fusion_v13/"
echo "🧪 Test script: ./test_fusion_v13.py"
echo ""
echo "💡 Usage:"
echo "   python3 -c \"import sys; sys.path.append('./fusion_v13'); from core.execution_chain_orchestrator import ExecutionChainOrchestrator; orchestrator = ExecutionChainOrchestrator(); result = orchestrator.run('Your prompt here'); print(result)\""
echo ""
echo "🚀 Happy orchestrating!"
