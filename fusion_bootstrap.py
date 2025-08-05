#!/usr/bin/env python3
"""
Fusion Bootstrap - Auto-launch Fusion v15
Detects Fusion context and boots API + GUI automatically
"""

import os
import sys
import subprocess
import time
import threading
from pathlib import Path

class FusionBootstrap:
    def __init__(self):
        self.project_dir = Path.cwd()
        self.fusion_detected = False
        self.api_process = None
        self.gui_process = None
        
    def detect_fusion(self) -> bool:
        """Detect if we're in a Fusion project."""
        fusion_indicators = [
            "fusion_core/",
            "fusion_api.py",
            "web_app.py",
            "agent_manifest.json"
        ]
        
        for indicator in fusion_indicators:
            if not (self.project_dir / indicator).exists():
                return False
        
        self.fusion_detected = True
        print("🤖 Fusion v15 detected!")
        return True
    
    def install_dependencies(self):
        """Install Fusion dependencies."""
        try:
            print("📦 Installing Fusion dependencies...")
            subprocess.run([sys.executable, "-m", "pip", "install", "-e", "."], 
                         check=True, capture_output=True)
            print("✅ Dependencies installed")
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Warning: Could not install dependencies: {e}")
    
    def launch_api(self):
        """Launch Fusion API server."""
        try:
            print("🚀 Launching Fusion API...")
            self.api_process = subprocess.Popen([
                sys.executable, "fusion_api.py"
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Wait a moment for API to start
            time.sleep(3)
            print("✅ Fusion API launched on http://localhost:8000")
            
        except Exception as e:
            print(f"❌ Error launching API: {e}")
    
    def launch_gui(self):
        """Launch Fusion GUI."""
        try:
            print("🎨 Launching Fusion GUI...")
            self.gui_process = subprocess.Popen([
                sys.executable, "-m", "streamlit", "run", "web_app.py"
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Wait a moment for GUI to start
            time.sleep(5)
            print("✅ Fusion GUI launched on http://localhost:8501")
            
        except Exception as e:
            print(f"❌ Error launching GUI: {e}")
    
    def create_chatgpt_upload(self):
        """Create ChatGPT upload folder with core files."""
        chatgpt_dir = self.project_dir / "ChatGPT_Upload_v15"
        chatgpt_dir.mkdir(exist_ok=True)
        
        # Core files to copy (under 20 files)
        files_to_copy = [
            "fusion_core/",
            "fusion_api.py",
            "web_app.py", 
            "fusion.py",
            "agent_manifest.json",
            "requirements.txt",
            "pyproject.toml",
            "Dockerfile",
            "FUSION_V15_README.md",
            "FUSION_V15_DELIVERY_SUMMARY.md"
        ]
        
        # Add prompt masters if they exist
        if (self.project_dir / "prompt_master_short.md").exists():
            files_to_copy.append("prompt_master_short.md")
        if (self.project_dir / "prompt_master_main.md").exists():
            files_to_copy.append("prompt_master_main.md")
        
        print("📁 Creating ChatGPT upload folder...")
        for file_path in files_to_copy:
            src = self.project_dir / file_path
            dst = chatgpt_dir / file_path
            
            if src.exists():
                if src.is_dir():
                    subprocess.run(["cp", "-r", str(src), str(dst)])
                else:
                    subprocess.run(["cp", str(src), str(dst)])
        
        print(f"✅ ChatGPT upload folder created: {chatgpt_dir}")
        return chatgpt_dir
    
    def run(self):
        """Main bootstrap process."""
        print("🧠 Fusion Bootstrap v15")
        print("=" * 50)
        
        # Detect Fusion
        if not self.detect_fusion():
            print("❌ Fusion v15 not detected in current directory")
            print("Please run this from a Fusion project directory")
            return False
        
        # Install dependencies
        self.install_dependencies()
        
        # Create ChatGPT upload folder
        chatgpt_dir = self.create_chatgpt_upload()
        
        # Launch API in background
        api_thread = threading.Thread(target=self.launch_api)
        api_thread.daemon = True
        api_thread.start()
        
        # Launch GUI in background
        gui_thread = threading.Thread(target=self.launch_gui)
        gui_thread.daemon = True
        gui_thread.start()
        
        print("\n🎉 Fusion v15 Auto-Launch Complete!")
        print("=" * 50)
        print("🌐 API: http://localhost:8000")
        print("🎨 GUI: http://localhost:8501")
        print("📁 ChatGPT Upload: ChatGPT_Upload_v15/")
        print("\nPress Ctrl+C to stop all services")
        
        try:
            # Keep running
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Shutting down Fusion v15...")
            if self.api_process:
                self.api_process.terminate()
            if self.gui_process:
                self.gui_process.terminate()
            print("✅ Fusion v15 stopped")
        
        return True

def main():
    """Main entry point."""
    bootstrap = FusionBootstrap()
    return bootstrap.run()

if __name__ == "__main__":
    main() 