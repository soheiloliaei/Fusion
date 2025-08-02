import json
import asyncio
from typing import List, Dict, Any, Optional
from datetime import datetime

class AgentChoreographer:
    def __init__(self):
        self.chains = self._load_chains()
        self.execution_history = []
    
    def _load_chains(self) -> Dict[str, List[str]]:
        """Load agent chains from JSON file"""
        try:
            with open("agent_chains.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            # Default chains
            default_chains = {
                "design_pipeline": ["vp_design", "evaluator", "rewrite_loop"],
                "narrative_loop": ["deck_narrator", "surprisal_critic", "rewrite_loop"],
                "strategy_chain": ["strategy_pilot", "market_analyst", "creative_director"],
                "content_flow": ["content_designer", "voice_match_evaluator", "rewrite_advisor"],
                "product_journey": ["product_navigator", "user_experience_analyst", "design_technologist"]
            }
            # Save default chains
            with open("agent_chains.json", "w") as f:
                json.dump(default_chains, f, indent=2)
            return default_chains
    
    def get_available_chains(self) -> List[str]:
        """Get list of available chain names"""
        return list(self.chains.keys())
    
    def get_chain_agents(self, chain_name: str) -> List[str]:
        """Get agents in a specific chain"""
        return self.chains.get(chain_name, [])
    
    async def execute_chain(self, chain_name: str, user_input: str, 
                          agent_map: Dict[str, Any], debug_mode: bool = False) -> Dict[str, Any]:
        """
        Execute a chain of agents with synthetic reasoning preserved
        
        Args:
            chain_name: Name of the chain to execute
            user_input: User's input prompt
            agent_map: Mapping of agent names to agent classes
            debug_mode: Whether to show debug output
            
        Returns:
            Dictionary with chain results and metadata
        """
        if chain_name not in self.chains:
            raise ValueError(f"Chain '{chain_name}' not found. Available chains: {list(self.chains.keys())}")
        
        chain_agents = self.chains[chain_name]
        chain_results = []
        current_input = user_input
        chain_start_time = datetime.now()
        
        print(f"🔄 Executing chain: {chain_name}")
        print(f"📋 Agents: {' → '.join(chain_agents)}")
        print(f"📝 Input: {user_input[:100]}{'...' if len(user_input) > 100 else ''}")
        print("="*60)
        
        for i, agent_name in enumerate(chain_agents, 1):
            if agent_name not in agent_map:
                print(f"⚠️  Warning: Agent '{agent_name}' not found, skipping...")
                continue
            
            print(f"\n🎯 Step {i}/{len(chain_agents)}: {agent_name}")
            
            try:
                # Get agent instance
                agent_class = agent_map[agent_name]
                agent = agent_class()
                
                # Execute agent with risk-aware runner
                from fusion import risk_aware_agent_runner
                result = await risk_aware_agent_runner(current_input, agent, agent_name)
                
                # Check for high-risk scenarios
                if result.get("synthetic_meta", {}).get("risk_score", 0.0) > 0.9:
                    print(f"🚨 HIGH RISK DETECTED ({result['synthetic_meta']['risk_score']:.2f}) - Stopping chain")
                    break
                
                # Update input for next agent
                agent_output = result.get("agent_output", {})
                if isinstance(agent_output, dict):
                    current_input = agent_output.get("output", str(agent_output))
                else:
                    current_input = str(agent_output)
                
                # Store result
                chain_results.append({
                    "step": i,
                    "agent_name": agent_name,
                    "input": current_input,
                    "output": agent_output,
                    "synthetic_meta": result.get("synthetic_meta", {}),
                    "routed": result.get("routed", False),
                    "execution_time": datetime.now().isoformat()
                })
                
                print(f"✅ {agent_name} completed")
                
            except Exception as e:
                print(f"❌ Error in {agent_name}: {str(e)}")
                chain_results.append({
                    "step": i,
                    "agent_name": agent_name,
                    "error": str(e),
                    "execution_time": datetime.now().isoformat()
                })
                break
        
        chain_end_time = datetime.now()
        execution_duration = (chain_end_time - chain_start_time).total_seconds()
        
        # Create chain summary
        chain_summary = {
            "chain_name": chain_name,
            "user_input": user_input,
            "agents_executed": len(chain_results),
            "total_agents": len(chain_agents),
            "execution_duration": execution_duration,
            "start_time": chain_start_time.isoformat(),
            "end_time": chain_end_time.isoformat(),
            "results": chain_results,
            "success": len(chain_results) == len(chain_agents)
        }
        
        # Log to execution history
        self.execution_history.append(chain_summary)
        
        # Print summary
        print(f"\n{'='*60}")
        print(f"🎬 Chain '{chain_name}' completed")
        print(f"⏱️  Duration: {execution_duration:.2f}s")
        print(f"✅ Success: {chain_summary['success']}")
        print(f"📊 Steps completed: {chain_summary['agents_executed']}/{chain_summary['total_agents']}")
        print(f"{'='*60}")
        
        return chain_summary
    
    def add_chain(self, chain_name: str, agent_list: List[str]) -> None:
        """Add a new agent chain"""
        self.chains[chain_name] = agent_list
        self._save_chains()
        print(f"✅ Added chain '{chain_name}' with {len(agent_list)} agents")
    
    def remove_chain(self, chain_name: str) -> None:
        """Remove an agent chain"""
        if chain_name in self.chains:
            del self.chains[chain_name]
            self._save_chains()
            print(f"✅ Removed chain '{chain_name}'")
        else:
            print(f"❌ Chain '{chain_name}' not found")
    
    def _save_chains(self) -> None:
        """Save chains to JSON file"""
        with open("agent_chains.json", "w") as f:
            json.dump(self.chains, f, indent=2)
    
    def get_execution_history(self) -> List[Dict[str, Any]]:
        """Get execution history"""
        return self.execution_history
    
    def save_execution_log(self, filename: str = None) -> None:
        """Save execution history to file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"chain_execution_log_{timestamp}.json"
        
        with open(filename, "w") as f:
            json.dump({
                "session_timestamp": datetime.now().isoformat(),
                "chains": self.chains,
                "execution_history": self.execution_history
            }, f, indent=2)
        
        print(f"📁 Chain execution log saved to: {filename}")

# Global choreographer instance
choreographer = AgentChoreographer()

def get_choreographer() -> AgentChoreographer:
    """Get the global choreographer instance"""
    return choreographer 