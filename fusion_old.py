#!/usr/bin/env python3
"""
Fusion v14 - CLI Runner
Programmable agent OS for design and evaluation
"""

import asyncio
import json
import sys
import argparse
from pathlib import Path
from typing import Dict, Any, Optional

# Import Fusion v14 components
# from core.fusion_context import FusionContext
# from core.execution_orchestrator_v14 import ExecutionOrchestrator
# from agents.vp_design_agent import VPDesignAgent
# from agents.evaluator_agent import EvaluatorAgent
# from tools.ux_audit_tool import UXAuditTool
# from tools.trust_explainer_tool import TrustExplainerTool
# from patterns.pattern_registry import PatternRegistry

class FusionCLI:
    """
    Fusion v14 CLI Runner
    Main entry point for the programmable agent OS
    """
    
    def __init__(self, config_path: str = ".fusion.json"):
        self.config_path = config_path
        # self.config = self._load_config()
        # self.context = FusionContext(self.config)
        # self.orchestrator = ExecutionOrchestrator(self.context)
        # self.pattern_registry = PatternRegistry()
        
        # Initialize agents and tools
        # self._initialize_agents()
        # self._initialize_tools()
        # self._initialize_patterns()
        
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from .fusion.json"""
        
        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
            print(f"✅ Loaded configuration from {self.config_path}")
            return config
        except FileNotFoundError:
            print(f"⚠️ Configuration file {self.config_path} not found, using defaults")
            return {
                "version": "v14.0",
                "entry": "fusion.py",
                "max_prompt_tokens": 8000,
                "enabled_agents": ["vp_design", "evaluator"],
                "tools_enabled": True,
                "github_push": True,
                "async_mode": True,
                "memory_enabled": True,
                "pattern_fallback": True,
                "auto_commit": True,
                "debug_mode": False,
                "log_level": "INFO"
            }
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing configuration file: {e}")
            sys.exit(1)
            
    def _initialize_agents(self):
        """Initialize agents with the orchestrator"""
        
        enabled_agents = self.config.get("enabled_agents", [])
        
        if "vp_design" in enabled_agents:
            vp_design_agent = VPDesignAgent()
            self.orchestrator.register_agent("vp_design", vp_design_agent)
            print("✅ Registered VP Design Agent")
            
        if "evaluator" in enabled_agents:
            evaluator_agent = EvaluatorAgent()
            self.orchestrator.register_agent("evaluator", evaluator_agent)
            print("✅ Registered Evaluator Agent")
            
    def _initialize_tools(self):
        """Initialize tools with the orchestrator"""
        
        if self.config.get("tools_enabled", True):
            ux_audit_tool = UXAuditTool()
            self.orchestrator.register_tool("ux_audit", ux_audit_tool)
            print("✅ Registered UX Audit Tool")
            
            trust_explainer_tool = TrustExplainerTool()
            self.orchestrator.register_tool("trust_explainer", trust_explainer_tool)
            print("✅ Registered Trust Explainer Tool")
            
    def _initialize_patterns(self):
        """Initialize patterns with the orchestrator"""
        
        if self.config.get("pattern_fallback", True):
            # Register all patterns from the registry
            for pattern_name, pattern_data in self.pattern_registry.patterns.items():
                self.orchestrator.register_pattern(pattern_name, pattern_data)
            print(f"✅ Registered {len(self.pattern_registry.patterns)} patterns")
            
    async def run_single_agent(self, agent_name: str, input_prompt: str) -> Dict[str, Any]:
        """Run a single agent with the given input"""
        
        print(f"🚀 Running {agent_name} agent...")
        
        try:
            result = await self.orchestrator.execute_agent(agent_name, input_prompt)
            return result
        except Exception as e:
            print(f"❌ Error running {agent_name} agent: {e}")
            return {"error": str(e)}
            
    async def run_pipeline(self, input_prompt: str, agent_sequence: Optional[list] = None) -> Dict[str, Any]:
        """Run a pipeline of agents"""
        
        if agent_sequence is None:
            agent_sequence = list(self.orchestrator.agents.keys())
            
        print(f"🚀 Running pipeline with agents: {', '.join(agent_sequence)}")
        
        try:
            result = await self.orchestrator.execute_pipeline(input_prompt, agent_sequence)
            return result
        except Exception as e:
            print(f"❌ Error running pipeline: {e}")
            return {"error": str(e)}
            
    async def run_with_pattern_fallback(self, input_prompt: str, primary_agent: str) -> Dict[str, Any]:
        """Run with pattern fallback"""
        
        print(f"🚀 Running {primary_agent} with pattern fallback...")
        
        try:
            # Find the best pattern for this input
            best_pattern = self.pattern_registry.find_best_pattern(input_prompt)
            fallback_patterns = self.pattern_registry.get_fallback_patterns(best_pattern)
            
            result = await self.orchestrator.execute_with_pattern_fallback(
                input_prompt, primary_agent, fallback_patterns
            )
            return result
        except Exception as e:
            print(f"❌ Error running with pattern fallback: {e}")
            return {"error": str(e)}
            
    def show_status(self):
        """Show current Fusion v14 status"""
        
        print("\n" + "="*50)
        print("FUSION v14 STATUS")
        print("="*50)
        
        # Configuration
        print(f"Version: {self.config.get('version', 'unknown')}")
        print(f"Max Prompt Tokens: {self.config.get('max_prompt_tokens', 8000)}")
        print(f"Enabled Agents: {', '.join(self.config.get('enabled_agents', []))}")
        print(f"Tools Enabled: {self.config.get('tools_enabled', True)}")
        print(f"Pattern Fallback: {self.config.get('pattern_fallback', True)}")
        
        # Orchestrator stats
        stats = self.orchestrator.get_orchestrator_stats()
        print(f"\nRegistered Agents: {len(stats['registered_agents'])}")
        print(f"Registered Tools: {len(stats['registered_tools'])}")
        print(f"Registered Patterns: {len(stats['registered_patterns'])}")
        
        # Context stats
        context_stats = stats['context_stats']
        print(f"\nTotal Interactions: {context_stats.get('total_interactions', 0)}")
        print(f"Average Confidence: {context_stats.get('avg_confidence', 0.0):.2f}")
        print(f"Memory Size: {context_stats.get('memory_size', 0)}")
        
        # Pattern stats
        top_patterns = self.pattern_registry.get_top_patterns(3)
        if top_patterns:
            print(f"\nTop Patterns:")
            for pattern in top_patterns:
                print(f"- {pattern['name']}: {pattern['usage_count']} uses, {pattern['success_rate']:.2f} success rate")
                
        print("="*50)
        
    def show_help(self):
        """Show help information"""
        
        help_text = """
Fusion v14 - Programmable Agent OS

USAGE:
    python fusion.py [COMMAND] [OPTIONS]

COMMANDS:
    run <agent> <input>     Run a single agent
    pipeline <input>         Run the full pipeline
    pattern <input>          Run with pattern fallback
    status                   Show current status
    help                     Show this help

EXAMPLES:
    python fusion.py run vp_design "Design a mobile app interface"
    python fusion.py pipeline "Create a user-friendly dashboard"
    python fusion.py pattern "Evaluate this design proposal"
    python fusion.py status

AGENTS:
    vp_design    - VP Design Agent (design analysis and recommendations)
    evaluator    - Evaluator Agent (comprehensive evaluation and scoring)

TOOLS:
    ux_audit     - UX Audit Tool (heuristic evaluation and metrics)
    trust_explainer - Trust Explainer Tool (trust-building analysis)

PATTERNS:
    design_enhancement    - Apply design principles and accessibility
    ux_audit            - Perform comprehensive UX audit
    trust_building      - Analyze and enhance trust elements
    comprehensive_evaluation - Full evaluation with detailed scoring
        """
        
        print(help_text)
        
    async def main(self):
        """Main CLI entry point"""
        print("DEBUG: Entering main function")
        
        parser = argparse.ArgumentParser(description="Fusion v14 - Programmable Agent OS")
        parser.add_argument("command", nargs="?", help="Command to execute")
        parser.add_argument("agent", nargs="?", help="Agent name (for run command)")
        parser.add_argument("input", nargs="*", help="Input prompt")
        parser.add_argument("--config", default=".fusion.json", help="Configuration file path")
        
        args = parser.parse_args()
        print(f"DEBUG: After parse_args - command={args.command}, agent={args.agent}, input={args.input}")
        print(f"DEBUG: sys.argv = {sys.argv}")
        
        # Update config path if specified
        if args.config != ".fusion.json":
            self.config_path = args.config
            self.config = self._load_config()
            
        if not args.command or args.command == "help":
            self.show_help()
            return
            
        if args.command == "status":
            self.show_status()
            return
            
        # Handle input parsing correctly
        input_text = ""
        if args.command == "run":
            # For run command: command agent input
            if args.input:
                input_text = " ".join(args.input)
        elif args.command in ["pipeline", "pattern"]:
            # For pipeline/pattern commands: command input
            # The agent argument is actually the input for these commands
            if args.agent:
                input_text = args.agent
            if args.input:
                input_text += " " + " ".join(args.input)
        

            
        if args.command == "run":
            if not args.agent or not input_text:
                print("❌ Error: 'run' command requires both agent and input")
                print("Usage: python fusion.py run <agent> <input>")
                return
                
            result = await self.run_single_agent(args.agent, input_text)
            self._display_result(result)
            
        elif args.command == "pipeline":
            print(f"DEBUG: pipeline command, input_text='{input_text}'")
            if not input_text:
                print("❌ Error: 'pipeline' command requires input")
                print("Usage: python fusion.py pipeline <input>")
                return
                
            result = await self.run_pipeline(input_text)
            self._display_result(result)
            
        elif args.command == "pattern":
            if not input_text:
                print("❌ Error: 'pattern' command requires input")
                print("Usage: python fusion.py pattern <input>")
                return
                
            result = await self.run_with_pattern_fallback(input_text, "vp_design")
            self._display_result(result)
            
        else:
            print(f"❌ Unknown command: {args.command}")
            self.show_help()
            
    def _display_result(self, result: Dict[str, Any]):
        """Display execution result"""
        
        if "error" in result:
            print(f"❌ Error: {result['error']}")
            return
            
        print("\n" + "="*50)
        print("EXECUTION RESULT")
        print("="*50)
        
        if "output" in result:
            print(result["output"])
        elif "enhanced_output" in result:
            print(result["enhanced_output"])
        elif "final_output" in result:
            print(result["final_output"])
            
        if "confidence" in result:
            print(f"\nConfidence: {result['confidence']:.2f}")
            
        if "execution_time" in result:
            print(f"Execution Time: {result['execution_time']:.2f}s")
            
        if "total_execution_time" in result:
            print(f"Total Execution Time: {result['total_execution_time']:.2f}s")
            
        print("="*50)

def main():
    """Main entry point"""
    
    try:
        cli = FusionCLI()
        asyncio.run(cli.main())
    except KeyboardInterrupt:
        print("\n👋 Fusion v14 stopped by user")
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 