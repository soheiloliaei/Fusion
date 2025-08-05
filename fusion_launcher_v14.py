#!/usr/bin/env python3
"""
Fusion v14 Launcher - Shows all available agents and proper usage
"""

import sys
import os
import subprocess

def show_available_agents():
    """Show all available agents with descriptions"""
    print("🚀 Fusion v14 - All Available Agents")
    print("=" * 60)
    
    agents = {
        # Core Agents
        "vp_design": "Design analysis and recommendations",
        "evaluator": "Comprehensive evaluation and scoring", 
        "creative_director": "Creative strategy and vision",
        "design_technologist": "Technical design implementation",
        "product_navigator": "Product strategy and navigation",
        "strategy_pilot": "Strategic planning and execution",
        "vp_of_design": "VP of Design leadership",
        "vp_of_product": "VP of Product leadership",
        
        # Companion Agents
        "principal_designer": "Principal design expertise",
        "component_librarian": "Component library management",
        "content_designer": "Content and copy design",
        "ai_interaction_designer": "AI interaction design",
        
        # Meta Agents
        "strategy_archivist": "Strategy documentation and archiving",
        "market_analyst": "Market analysis and insights",
        "workflow_optimizer": "Workflow optimization",
        "product_historian": "Product history and context",
        
        # Narrative & Content Agents
        "deck_narrator": "Presentation and deck creation",
        "portfolio_editor": "Portfolio management",
        "research_summarizer": "Research summarization",
        "feedback_amplifier": "Feedback processing and amplification",
        
        # Intelligence & Orchestration Agents
        "prompt_master": "Pattern matching and prompt optimization",
        "dispatcher": "Agent coordination and routing"
    }
    
    for agent, description in agents.items():
        print(f"  • {agent}: {description}")
    
    print(f"\n📊 TOTAL: {len(agents)} agents available")
    print("\n🚀 HOW TO USE:")
    print("1. Single agent: python3 fusion.py run <agent_name> <prompt>")
    print("2. Full pipeline: python3 fusion.py pipeline <prompt>")
    print("\n💡 EXAMPLES:")
    print("  python3 fusion.py run vp_design 'Design a mobile app for task management'")
    print("  python3 fusion.py run creative_director 'Create a brand identity for a tech startup'")
    print("  python3 fusion.py run evaluator 'Evaluate this design proposal'")
    print("  python3 fusion.py pipeline 'Design a complete user experience for an e-commerce platform'")

def run_single_agent(agent_name, prompt):
    """Run a single agent with the given prompt"""
    if not os.path.exists("fusion.py"):
        print("❌ Error: fusion.py not found in current directory")
        return
    
    cmd = ["python3", "fusion.py", "run", agent_name] + prompt.split()
    print(f"🚀 Running: {' '.join(cmd)}")
    print("=" * 60)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except Exception as e:
        print(f"❌ Error running agent: {e}")

def run_pipeline(prompt):
    """Run the full pipeline with the given prompt"""
    if not os.path.exists("fusion.py"):
        print("❌ Error: fusion.py not found in current directory")
        return
    
    cmd = ["python3", "fusion.py", "pipeline"] + prompt.split()
    print(f"🚀 Running pipeline: {' '.join(cmd)}")
    print("=" * 60)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except Exception as e:
        print(f"❌ Error running pipeline: {e}")

def main():
    if len(sys.argv) < 2:
        show_available_agents()
        return
    
    command = sys.argv[1]
    
    if command == "list":
        show_available_agents()
    
    elif command == "run":
        if len(sys.argv) < 4:
            print("❌ Usage: python3 fusion_launcher_v14.py run <agent_name> <prompt>")
            return
        agent_name = sys.argv[2]
        prompt = " ".join(sys.argv[3:])
        run_single_agent(agent_name, prompt)
    
    elif command == "pipeline":
        if len(sys.argv) < 3:
            print("❌ Usage: python3 fusion_launcher_v14.py pipeline <prompt>")
            return
        prompt = " ".join(sys.argv[2:])
        run_pipeline(prompt)
    
    else:
        print(f"❌ Unknown command: {command}")
        print("Available commands: list, run, pipeline")
        show_available_agents()

if __name__ == "__main__":
    main() 