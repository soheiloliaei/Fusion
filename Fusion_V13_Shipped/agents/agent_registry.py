#!/usr/bin/env python3
"""
Agent Registry – Fusion v13.0
Centralized agent management and discovery system.
"""

import os
import importlib.util
from pathlib import Path

# Import all available agents
from agents.vp_design_agent import VPOfDesignAgent
from agents.design_technologist import DesignTechnologistAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.product_navigator import ProductNavigatorAgent
from agents.strategy_pilot import StrategyPilotAgent
from agents.vp_of_design import VPOfDesignAgent
from agents.vp_of_product import VPOfProductAgent
from agents.prompt_master_agent import PromptMasterAgent

# Dictionary to hold all registered agents
AGENTS = {}

def register_agent(agent_class):
    """Decorator to register agent classes."""
    AGENTS[agent_class.__name__] = agent_class
    return agent_class

# Register all agents
register_agent(VPOfDesignAgent)  # AI-first design guru
register_agent(DesignTechnologistAgent)
register_agent(EvaluatorAgent)
register_agent(ProductNavigatorAgent)
register_agent(StrategyPilotAgent)
register_agent(VPOfDesignAgent)
register_agent(VPOfProductAgent)
register_agent(PromptMasterAgent)

def discover_agents(agent_dir: str = "agents"):
    """
    Dynamically discovers and registers agents from the specified directory.
    This allows for adding new agents without modifying agent_registry.py directly.
    """
    current_dir = Path(__file__).parent
    full_agent_dir = current_dir / agent_dir

    if not full_agent_dir.is_dir():
        print(f"Warning: Agent directory '{full_agent_dir}' not found for dynamic discovery.")
        return

    for agent_file in full_agent_dir.glob("*.py"):
        if agent_file.name == "__init__.py" or agent_file.name == Path(__file__).name:
            continue  # Skip __init__.py and agent_registry.py itself

        module_name = agent_file.stem
        spec = importlib.util.spec_from_file_location(module_name, agent_file)
        if spec is None:
            continue
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
            # Iterate through module's attributes to find classes that are agents
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if isinstance(attribute, type) and issubclass(attribute, object) and attribute.__name__.endswith("Agent") and attribute.__name__ != "PromptMasterAgent":
                    if attribute.__name__ not in AGENTS:
                        register_agent(attribute)
                        print(f"Dynamically registered agent: {attribute.__name__}")
        except Exception as e:
            print(f"Error loading agent from {agent_file}: {e}")

# Agent mapping for easy access
AGENT_MAPPING = {
    "vp_of_design": VPOfDesignAgent,  # AI-first design guru
    "design_technologist": DesignTechnologistAgent,
    "evaluator": EvaluatorAgent,
    "product_navigator": ProductNavigatorAgent,
    "strategy_pilot": StrategyPilotAgent,
    "vp_of_product": VPOfProductAgent,
    "prompt_master": PromptMasterAgent
}

def get_agent(agent_name: str):
    """Get an agent instance by name."""
    agent_class = AGENT_MAPPING.get(agent_name)
    if agent_class:
        return agent_class()
    else:
        raise ValueError(f"Agent '{agent_name}' not found. Available agents: {list(AGENT_MAPPING.keys())}")

# Example usage
if __name__ == "__main__":
    print("🎯 Available Agents:")
    for name, agent_class in AGENT_MAPPING.items():
        print(f"  - {name}: {agent_class.__name__}")
    
    # Test VP of Design Agent
    vp_design = get_agent("vp_of_design")
    print(f"\n🎨 VP of Design Agent: {vp_design.__class__.__name__}")
