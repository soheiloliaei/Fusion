#!/usr/bin/env python3
"""
Fusion Plugin Registry - v15.3
Allow external devs to register agents/tools without editing core files.
"""

import os
import json
import importlib
import inspect
from typing import Dict, List, Any, Optional, Type
from pathlib import Path

# Global plugin registries
PLUGIN_AGENTS = []
PLUGIN_TOOLS = []
PLUGIN_CONFIGS = {}

class PluginRegistry:
    """Central registry for Fusion plugins."""
    
    def __init__(self, plugins_dir: str = "plugins"):
        self.plugins_dir = Path(plugins_dir)
        self.plugins_dir.mkdir(exist_ok=True)
        self.agent_registry = {}
        self.tool_registry = {}
        self.config_registry = {}
        
    def register_agent(self, agent_class: Type, agent_name: Optional[str] = None) -> bool:
        """
        Register an agent class.
        
        Args:
            agent_class: The agent class to register
            agent_name: Optional custom name for the agent
            
        Returns:
            True if successfully registered
        """
        try:
            # Get agent name
            if agent_name is None:
                agent_name = agent_class.__name__
            
            # Validate agent class
            if not hasattr(agent_class, 'run'):
                print(f"❌ Agent {agent_name} must have a 'run' method")
                return False
            
            # Register the agent
            self.agent_registry[agent_name] = agent_class
            PLUGIN_AGENTS.append(agent_class)
            
            print(f"✅ Registered plugin agent: {agent_name}")
            return True
            
        except Exception as e:
            print(f"❌ Error registering agent {agent_name}: {e}")
            return False
    
    def register_tool(self, tool_class: Type, tool_name: Optional[str] = None) -> bool:
        """
        Register a tool class.
        
        Args:
            tool_class: The tool class to register
            tool_name: Optional custom name for the tool
            
        Returns:
            True if successfully registered
        """
        try:
            # Get tool name
            if tool_name is None:
                tool_name = tool_class.__name__
            
            # Validate tool class
            if not hasattr(tool_class, 'execute'):
                print(f"❌ Tool {tool_name} must have an 'execute' method")
                return False
            
            # Register the tool
            self.tool_registry[tool_name] = tool_class
            PLUGIN_TOOLS.append(tool_class)
            
            print(f"✅ Registered plugin tool: {tool_name}")
            return True
            
        except Exception as e:
            print(f"❌ Error registering tool {tool_name}: {e}")
            return False
    
    def register_config(self, config_name: str, config_data: Dict[str, Any]) -> bool:
        """
        Register configuration data.
        
        Args:
            config_name: Name of the configuration
            config_data: Configuration dictionary
            
        Returns:
            True if successfully registered
        """
        try:
            self.config_registry[config_name] = config_data
            PLUGIN_CONFIGS[config_name] = config_data
            
            print(f"✅ Registered plugin config: {config_name}")
            return True
            
        except Exception as e:
            print(f"❌ Error registering config {config_name}: {e}")
            return False
    
    def discover_plugins(self) -> Dict[str, Any]:
        """
        Automatically discover and load plugins from the plugins directory.
        
        Returns:
            Dictionary with discovery results
        """
        discovery_results = {
            "agents_found": 0,
            "tools_found": 0,
            "configs_found": 0,
            "errors": []
        }
        
        if not self.plugins_dir.exists():
            print(f"⚠️ Plugins directory {self.plugins_dir} does not exist")
            return discovery_results
        
        # Discover Python files in plugins directory
        for py_file in self.plugins_dir.glob("*.py"):
            if py_file.name.startswith("__"):
                continue
                
            try:
                # Import the plugin module
                module_name = f"plugins.{py_file.stem}"
                module = importlib.import_module(module_name)
                
                # Look for agent classes
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj) and name.endswith('Agent'):
                        if self.register_agent(obj, name):
                            discovery_results["agents_found"] += 1
                    
                    elif inspect.isclass(obj) and name.endswith('Tool'):
                        if self.register_tool(obj, name):
                            discovery_results["tools_found"] += 1
                
                # Look for configuration
                if hasattr(module, 'PLUGIN_CONFIG'):
                    config = getattr(module, 'PLUGIN_CONFIG')
                    if isinstance(config, dict):
                        config_name = py_file.stem
                        if self.register_config(config_name, config):
                            discovery_results["configs_found"] += 1
                            
            except Exception as e:
                error_msg = f"Error loading plugin {py_file.name}: {e}"
                discovery_results["errors"].append(error_msg)
                print(f"❌ {error_msg}")
        
        return discovery_results
    
    def get_agent(self, agent_name: str) -> Optional[Type]:
        """Get a registered agent class."""
        return self.agent_registry.get(agent_name)
    
    def get_tool(self, tool_name: str) -> Optional[Type]:
        """Get a registered tool class."""
        return self.tool_registry.get(tool_name)
    
    def get_config(self, config_name: str) -> Optional[Dict[str, Any]]:
        """Get a registered configuration."""
        return self.config_registry.get(config_name)
    
    def list_agents(self) -> List[str]:
        """List all registered agent names."""
        return list(self.agent_registry.keys())
    
    def list_tools(self) -> List[str]:
        """List all registered tool names."""
        return list(self.tool_registry.keys())
    
    def list_configs(self) -> List[str]:
        """List all registered configuration names."""
        return list(self.config_registry.keys())
    
    def export_registry(self, file_path: str = "plugin_registry.json") -> bool:
        """
        Export the current registry to a JSON file.
        
        Args:
            file_path: Path to save the registry
            
        Returns:
            True if successfully exported
        """
        try:
            registry_data = {
                "agents": {
                    name: {
                        "class_name": agent_class.__name__,
                        "module": agent_class.__module__
                    }
                    for name, agent_class in self.agent_registry.items()
                },
                "tools": {
                    name: {
                        "class_name": tool_class.__name__,
                        "module": tool_class.__module__
                    }
                    for name, tool_class in self.tool_registry.items()
                },
                "configs": self.config_registry,
                "export_timestamp": importlib.util.find_spec("datetime").loader.load_module("datetime").datetime.now().isoformat()
            }
            
            with open(file_path, 'w') as f:
                json.dump(registry_data, f, indent=2)
            
            print(f"✅ Exported registry to {file_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error exporting registry: {e}")
            return False

# Global registry instance
plugin_registry = PluginRegistry()

# Convenience functions for external developers
def register_agent(agent_class: Type, agent_name: Optional[str] = None) -> bool:
    """Register an agent class with the global registry."""
    return plugin_registry.register_agent(agent_class, agent_name)

def register_tool(tool_class: Type, tool_name: Optional[str] = None) -> bool:
    """Register a tool class with the global registry."""
    return plugin_registry.register_tool(tool_class, tool_name)

def register_config(config_name: str, config_data: Dict[str, Any]) -> bool:
    """Register configuration data with the global registry."""
    return plugin_registry.register_config(config_name, config_data)

def discover_plugins() -> Dict[str, Any]:
    """Discover and load all plugins."""
    return plugin_registry.discover_plugins()

# Example plugin agent
class ExamplePluginAgent:
    """Example plugin agent for demonstration."""
    
    def __init__(self):
        self.name = "example_plugin_agent"
    
    async def run(self, input_text: str) -> str:
        """Run the plugin agent."""
        return f"Plugin agent processed: {input_text}"

# Example plugin tool
class ExamplePluginTool:
    """Example plugin tool for demonstration."""
    
    def __init__(self):
        self.name = "example_plugin_tool"
    
    def execute(self, input_data: Any) -> Any:
        """Execute the plugin tool."""
        return f"Plugin tool executed: {input_data}"

# Example plugin configuration
EXAMPLE_PLUGIN_CONFIG = {
    "agent_settings": {
        "confidence_threshold": 0.8,
        "max_retries": 3
    },
    "tool_settings": {
        "timeout": 30,
        "cache_enabled": True
    }
}

# Auto-register example plugins
if __name__ == "__main__":
    # Register example plugins
    register_agent(ExamplePluginAgent, "example_agent")
    register_tool(ExamplePluginTool, "example_tool")
    register_config("example_config", EXAMPLE_PLUGIN_CONFIG)
    
    # Discover plugins
    results = discover_plugins()
    
    print("🔌 Plugin Registry Status:")
    print(f"Agents: {len(plugin_registry.list_agents())}")
    print(f"Tools: {len(plugin_registry.list_tools())}")
    print(f"Configs: {len(plugin_registry.list_configs())}")
    print(f"Discovery results: {results}")
    
    # Export registry
    plugin_registry.export_registry() 