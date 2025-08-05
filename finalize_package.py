#!/usr/bin/env python3
# Finalize Fusion v14.5 packaging and GitHub deployment

import os
import shutil
import subprocess
from datetime import datetime

def finalize_fusion_package():
    print("📦 Finalizing Fusion v14.5 packaging and GitHub sync...")

    # Define all paths
    fusion_dir = os.getcwd()
    chatgpt_dir = os.path.join(fusion_dir, "ChatGPT_Upload_v14.5")
    os.makedirs(chatgpt_dir, exist_ok=True)

    # ✅ Copy all key Fusion files into the ChatGPT folder
    files_to_copy = [
        "fusion.py", "agents_combined.py", "synthetic_reasoner_agent.py",
        "agent_manifest.json", "fallback_trigger_config.json", "pattern_registry.py",
        "cursor_init.py", "fusion_guardrail_usage.py", "working_chain_example.py",
        "cursor_startup.py", "patch_fusion_guardrail.py", "test_fusion_guardrail.py"
    ]
    
    copied_files = []
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy(file, chatgpt_dir)
            copied_files.append(file)
            print(f"✅ Copied: {file}")
        else:
            print(f"⚠️ Missing: {file}")
    
    print(f"📁 Total files copied: {len(copied_files)}")

    # ✅ Create master prompt versions
    master_main = "master_prompt_main.md"
    if os.path.exists(master_main):
        shutil.copy(master_main, os.path.join(chatgpt_dir, "master_prompt_main.md"))
        print("✅ Copied: master_prompt_main.md")
        
        with open(master_main, "r") as f:
            content = f.read()
        
        # Create truncated version
        truncated_content = content[:4000] + "\n\n[Content truncated for token limits]"
        with open(os.path.join(chatgpt_dir, "master_prompt_under8000.md"), "w") as f:
            f.write(truncated_content)
        print("✅ Created: master_prompt_under8000.md")
    else:
        print("⚠️ master_prompt_main.md not found")

    # ✅ Update launcher.command
    launcher = os.path.join(fusion_dir, "fusion_launch.command")
    launcher_content = f"""#!/bin/bash
echo "🚀 Launching Fusion v14.5..."
cd "{fusion_dir}"
echo "📁 Project: $(pwd)"
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not installed"
    exit 1
fi
echo "🛡️ Loading Fusion v14.5 bootstrap system..."
python3 -c "
try:
    import cursor_init
    print('✅ Fusion v14.5 bootstrap loaded successfully')
    print('🎯 You can now use: ask(\"your prompt\", \"agent\")')
    print('🤖 Auto-agent: ask_auto(\"your prompt\")')
    print('🔗 Chain support: ask_chain(\"prompt\", [\"agent1\", \"agent2\"])')
except Exception as e:
    print(f'⚠️ Bootstrap failed: {{e}}')
    print('Continuing with standard Fusion...')
"
bootstrap_status=$?
python3 fusion.py --help
echo "✅ Fusion v14.5 is ready!"
"""
    
    with open(launcher, "w") as f:
        f.write(launcher_content)
    os.chmod(launcher, 0o755)
    print("✅ Updated: fusion_launch.command")

    # ✅ Update README.md for GitHub
    readme_content = f"""# Fusion v14.5 – AI-Native Agentic OS

**Updated:** {datetime.now().strftime('%Y-%m-%d')}

This repo contains the full Fusion v14.5 system with:

- ✅ Agent orchestration (22 agents)
- ✅ Synthetic reasoning (thoughts, questions, risk)
- ✅ Pattern fallback logic
- ✅ Auto-agent selection + chaining
- ✅ Hallucination guardrails
- ✅ CLI-free runtime (use `ask()`, `ask_chain()`, `ask_auto()`)

## How to Use

1. **Start with `fusion_launch.command`**
2. Open Cursor Python cell and just type:

```python
ask("Design a fallback UX tile for Bitcoin support", "vp_design")
ask_auto("Critique this flow for usability and agentic alignment")
ask_chain("Evaluate and rewrite this support pattern", ["evaluator", "vp_of_product"])
```

## Key Files

| File                         | Purpose                    |
| ---------------------------- | -------------------------- |
| `fusion.py`                  | Fusion orchestrator        |
| `cursor_init.py`             | Bootstrap system           |
| `agents_combined.py`         | All agent definitions      |
| `fusion_guardrail_usage.py`  | Hallucination protection   |
| `pattern_registry.py`        | Fallback pattern logic     |
| `agent_manifest.json`        | Agent definitions          |
| `master_prompt_main.md`      | Full system prompt         |
| `master_prompt_under8000.md` | Truncated for token limits |

> Built for full-stack developers and AI-native designers. You're not just using agents — you're orchestrating an entire system.

## Launch Commands

```bash
./fusion_launch.command
```

## Contact

DM for onboarding, custom chains, or enterprise deployment.
"""
    
    with open("README.md", "w") as f:
        f.write(readme_content)
    print("✅ Updated: README.md")

    # ✅ GitHub commit
    print("🔄 Committing to GitHub...")
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Finalize Fusion v14.5: Launcher, ChatGPT folder, README, all patches"])
    subprocess.run(["git", "push"])
    print("✅ Pushed to GitHub")

    print("✅ Fusion v14.5 packaged, synced to GitHub, and ready to share.")

if __name__ == "__main__":
    finalize_fusion_package() 