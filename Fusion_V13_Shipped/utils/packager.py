import os, shutil

def generate_launch_file(version):
    with open(f"Fusion_v{version}_Launcher.sh", "w") as f:
        f.write(f"""#!/bin/bash
echo "🚀 Installing Fusion v{version} to your Cursor project"
mkdir -p fusion_v{version}
cp -r ~/fusion_v13/* ./fusion_v{version}/
echo "✅ Files copied"
echo "🧠 Running setup..."
python3 -c "import sys; sys.path.append('./fusion_v{version}'); from core.execution_chain_orchestrator import ExecutionChainOrchestrator; print('🎉 Fusion v{version} Installed')"
""")
    print(f"✅ Launch File created: Fusion_v{version}_Launcher.sh")

def generate_chatgpt_upload_package(version):
    os.makedirs(f"ChatGPT_Upload_v{version}", exist_ok=True)
    essential_files = [
        "core/execution_chain_orchestrator.py",
        "agents/agent_registry.py",
        "patterns/creative_director_patterns.py",
        "agents/creative_director_agent.py",
        "quality/quality_config.json",
        "prompt_patterns.py",
        "prompt_pattern_registry.py",
        "chains_complete.json",
        "quality_complete.py",
        "evaluator_metrics.py",
        "requirements.txt",
    ]
    for file in essential_files:
        dest = os.path.join(f"ChatGPT_Upload_v{version}", os.path.basename(file))
        src = os.path.expanduser(f"~/fusion_v13/{file}")
        if os.path.exists(src):
            shutil.copyfile(src, dest)
        else:
            print(f"⚠️ Warning: {src} not found, skipping...")
    with open(f"ChatGPT_Upload_v{version}/README.txt", "w") as f:
        f.write("💡 Upload all files to ChatGPT and paste `master_prompt.md` manually.\n")
    print("✅ ChatGPT Upload Package ready.")

def push_github_updates(version):
    os.system("cd ~/fusion_v13 && git add . && git commit -m '🚀 Fusion v{} Release'".format(version))
    os.system("cd ~/fusion_v13 && git push origin main")
    os.system("cd ~/fusion_v13 && git tag v{} && git push origin v{}".format(version, version))
    print("✅ GitHub push and version tag complete.")
