#!/bin/bash

echo "🚀 Launching Fusion v14.5..."

# Change to the script directory
cd "$(dirname "$0")"

echo "📁 Project: $(pwd)"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not installed"
    exit 1
fi

# Check if required files exist
if [ ! -f "fusion.py" ]; then
    echo "❌ Error: fusion.py not found"
    exit 1
fi

if [ ! -f "synthetic_reasoner_agent.py" ]; then
    echo "❌ Error: synthetic_reasoner_agent.py not found"
    exit 1
fi

# Load Fusion bootstrap system
echo "🛡️ Loading Fusion v14.5 bootstrap system..."
python3 -c "
try:
    import cursor_init
    print('✅ Fusion v14.5 bootstrap loaded successfully')
    print('🎯 You can now use: ask(\"your prompt\", \"agent\")')
    print('🤖 Auto-agent: ask_auto(\"your prompt\")')
    print('🔗 Chain support: ask_chain(\"prompt\", [\"agent1\", \"agent2\"])')
except Exception as e:
    print(f'⚠️ Bootstrap failed: {e}')
    print('Continuing with standard Fusion...')
"
bootstrap_status=$?

# Run help to confirm CLI setup
echo "🔧 Testing Fusion v14.5 setup..."
python3 fusion.py --help

echo "✅ Fusion v14.5 is ready!"
echo ""
echo "🎯 Usage Options:"
echo "   1. Native Cursor (recommended):"
echo "      import cursor_init"
echo "      ask('your prompt', 'agent')"
echo ""
echo "   2. CLI mode:"
echo "      python3 fusion.py run [agent] [input]"
echo "      python3 fusion.py pipeline [input]"
echo ""
echo "   3. Auto-agent selection:"
echo "      ask_auto('your prompt')"
echo ""
echo "   4. Multi-agent chains:"
echo "      ask_chain('prompt', ['agent1', 'agent2'])"
echo ""

if [ $bootstrap_status -eq 0 ]; then
    echo "🛡️ Bootstrap system is ACTIVE - Native Fusion experience enabled"
else
    echo "⚠️ Bootstrap not available - using standard Fusion"
fi 