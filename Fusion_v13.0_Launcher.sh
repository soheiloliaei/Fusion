#!/bin/bash
echo "🚀 Installing Fusion v13.0 to your Cursor project"
mkdir -p fusion_v13.0
cp -r ~/fusion_v13/* ./fusion_v13.0/
echo "✅ Files copied"
echo "🧠 Running setup..."
python3 -c "import sys; sys.path.append('./fusion_v13.0'); from core.execution_chain_orchestrator import ExecutionChainOrchestrator; print('🎉 Fusion v13.0 Installed')"
