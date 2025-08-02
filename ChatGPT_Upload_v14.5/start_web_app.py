#!/usr/bin/env python3
"""
Fusion Web App Launcher
"""

import subprocess
import sys
import os

def main():
    """Launch the Fusion web app"""
    print("🚀 Starting Fusion Web App...")
    
    # Check if streamlit is installed
    try:
        import streamlit
        print("✅ Streamlit found")
    except ImportError:
        print("❌ Streamlit not found. Install with: pip install streamlit")
        return
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    web_app_path = os.path.join(script_dir, "web_app.py")
    
    if not os.path.exists(web_app_path):
        print(f"❌ Web app not found at: {web_app_path}")
        return
    
    print(f"📁 Running from: {script_dir}")
    print(f"🌐 Starting web app at: http://localhost:8501")
    print("🔍 Use Ctrl+C to stop the server")
    
    # Start streamlit
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", web_app_path,
            "--server.port", "8501",
            "--server.headless", "false",
            "--browser.gatherUsageStats", "false"
        ], cwd=script_dir)
    except KeyboardInterrupt:
        print("\n🛑 Web app stopped")
    except Exception as e:
        print(f"❌ Error starting web app: {e}")

if __name__ == "__main__":
    main()