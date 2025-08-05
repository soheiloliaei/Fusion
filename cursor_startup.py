# cursor_startup.py
# 
# Copy this into Cursor's startup or run at the beginning of each session
# This automatically loads the Fusion v14.5 guardrail system

import sys
import os

def load_fusion_guardrail():
    """Load Fusion v14.5 guardrail system automatically"""
    try:
        # Add current directory to path if needed
        if os.getcwd() not in sys.path:
            sys.path.insert(0, os.getcwd())
        
        # Import and validate Fusion system
        from fusion_guardrail_usage import validate_fusion_system, safe_fusion_run
        
        # Validate the system
        validate_fusion_system()
        
        # Make safe_fusion_run available globally
        globals()['safe_fusion_run'] = safe_fusion_run
        
        print("🛡️ Fusion v14.5 guardrail system loaded successfully!")
        print("✅ You can now use: safe_fusion_run('your prompt', 'agent_name')")
        print("✅ Hallucination protection is ACTIVE")
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to load Fusion guardrail system: {e}")
        return False

# Auto-load when this file is imported
if __name__ == "__main__":
    load_fusion_guardrail()
else:
    # Auto-load when imported
    load_fusion_guardrail() 