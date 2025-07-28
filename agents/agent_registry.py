#!/usr/bin/env python3
"""
Agent Registry - Fusion v13.0
Central registry for all Fusion agents
"""

from .creative_director_agent import CreativeDirectorAgent
from .prompt_master_agent import PromptMasterAgent

# Core Fusion v13.0 Agents
AGENTS = {
    "creative_director": CreativeDirectorAgent(),
    "prompt_master": PromptMasterAgent(),
    "strategy_pilot": None,  # Placeholder for future implementation
    "vp_of_product": None,   # Placeholder for future implementation
    "vp_of_design": None,    # Placeholder for future implementation
    "evaluator_agent": None, # Placeholder for future implementation
    "product_navigator": None, # Placeholder for future implementation
    "design_technologist": None, # Placeholder for future implementation
}

def get_agent(agent_name: str):
    """Get an agent by name"""
    return AGENTS.get(agent_name)

def list_agents():
    """List all available agents"""
    return list(AGENTS.keys())

def register_agent(name: str, agent_instance):
    """Register a new agent"""
    AGENTS[name] = agent_instance

def discover_agents():
    """Auto-discover agents from agents/ directory"""
    import os
    import importlib
    
    agents_dir = os.path.dirname(__file__)
    discovered = []
    
    for filename in os.listdir(agents_dir):
        if filename.endswith('_agent.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Remove .py
            try:
                module = importlib.import_module(f'.{module_name}', package='agents')
                if hasattr(module, module_name.replace('_', '').title() + 'Agent'):
                    agent_class = getattr(module, module_name.replace('_', '').title() + 'Agent')
                    agent_instance = agent_class()
                    register_agent(module_name, agent_instance)
                    discovered.append(module_name)
                    print(f"✅ Discovered agent: {module_name}")
            except Exception as e:
                print(f"⚠️ Failed to load agent {module_name}: {e}")
    
    return discovered

# Auto-discover agents on import
if __name__ == "__main__":
    print("🔍 Discovering agents...")
    discovered = discover_agents()
    print(f"✅ Found {len(discovered)} agents: {discovered}")
