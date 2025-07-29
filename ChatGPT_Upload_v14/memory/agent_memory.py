#!/usr/bin/env python3
"""
Agent Memory System - Fusion v14
Async read/write functions to store each agent's last 3 runs with memory keys
"""

import asyncio
import json
import os
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime

class AgentMemory:
    """
    Agent Memory System - Fusion v14
    Async read/write functions to store each agent's last 3 runs
    """
    
    def __init__(self, memory_file: str = "memory/agent_memory.json"):
        self.logger = logging.getLogger("AgentMemory")
        self.memory_file = memory_file
        self.max_entries_per_agent = 3
        
        # Ensure memory directory exists
        os.makedirs(os.path.dirname(memory_file), exist_ok=True)
        
        # Initialize memory file if it doesn't exist
        if not os.path.exists(memory_file):
            self._initialize_memory_file()
    
    def _initialize_memory_file(self):
        """Initialize memory file with empty structure"""
        initial_memory = {
            "agents": {},
            "metadata": {
                "created": datetime.now().isoformat(),
                "version": "1.0",
                "max_entries_per_agent": self.max_entries_per_agent
            }
        }
        
        with open(self.memory_file, 'w') as f:
            json.dump(initial_memory, f, indent=2)
    
    async def read_memory(self) -> Dict[str, Any]:
        """Read agent memory from JSON file"""
        try:
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Error reading memory: {e}")
            return {"agents": {}, "metadata": {}}
    
    async def write_memory(self, memory_data: Dict[str, Any]):
        """Write agent memory to JSON file"""
        try:
            with open(self.memory_file, 'w') as f:
                json.dump(memory_data, f, indent=2)
        except Exception as e:
            self.logger.error(f"Error writing memory: {e}")
    
    async def store_agent_run(self, agent_name: str, prompt: str, response: str, 
                             confidence: float, fallback_flag: bool = False, 
                             additional_data: Dict[str, Any] = None) -> bool:
        """
        Store an agent's run in memory
        
        Args:
            agent_name: Name of the agent
            prompt: Input prompt
            response: Agent response
            confidence: Confidence score
            fallback_flag: Whether fallback was triggered
            additional_data: Any additional data to store
            
        Returns:
            bool: Success status
        """
        try:
            memory_data = await self.read_memory()
            
            # Create memory entry
            memory_entry = {
                "agent_name": agent_name,
                "prompt": prompt,
                "response": response,
                "confidence": confidence,
                "fallback_flag": fallback_flag,
                "timestamp": datetime.now().isoformat(),
                "additional_data": additional_data or {}
            }
            
            # Get or create agent memory list
            if agent_name not in memory_data.get("agents", {}):
                memory_data["agents"][agent_name] = []
            
            # Add new entry
            memory_data["agents"][agent_name].append(memory_entry)
            
            # Keep only last N entries per agent
            memory_data["agents"][agent_name] = memory_data["agents"][agent_name][-self.max_entries_per_agent:]
            
            # Update metadata
            memory_data["metadata"]["last_updated"] = datetime.now().isoformat()
            memory_data["metadata"]["total_entries"] = sum(len(entries) for entries in memory_data["agents"].values())
            
            await self.write_memory(memory_data)
            return True
            
        except Exception as e:
            self.logger.error(f"Error storing agent run: {e}")
            return False
    
    async def get_agent_memory(self, agent_name: str) -> List[Dict[str, Any]]:
        """Get memory entries for a specific agent"""
        try:
            memory_data = await self.read_memory()
            return memory_data.get("agents", {}).get(agent_name, [])
        except Exception as e:
            self.logger.error(f"Error getting agent memory: {e}")
            return []
    
    async def get_all_memory(self) -> Dict[str, Any]:
        """Get all memory data"""
        return await self.read_memory()
    
    async def get_agent_insights(self, agent_name: str) -> Dict[str, Any]:
        """Get insights from agent's memory"""
        try:
            agent_memory = await self.get_agent_memory(agent_name)
            
            if not agent_memory:
                return {
                    "total_runs": 0,
                    "average_confidence": 0.0,
                    "fallback_rate": 0.0,
                    "recent_trends": "No data available"
                }
            
            # Calculate insights
            total_runs = len(agent_memory)
            average_confidence = sum(entry.get("confidence", 0) for entry in agent_memory) / total_runs
            fallback_count = sum(1 for entry in agent_memory if entry.get("fallback_flag", False))
            fallback_rate = fallback_count / total_runs if total_runs > 0 else 0.0
            
            # Analyze recent trends
            recent_entries = agent_memory[-3:]  # Last 3 entries
            if len(recent_entries) >= 2:
                recent_confidence = sum(entry.get("confidence", 0) for entry in recent_entries) / len(recent_entries)
                if recent_confidence > average_confidence:
                    trend = "Improving"
                elif recent_confidence < average_confidence:
                    trend = "Declining"
                else:
                    trend = "Stable"
            else:
                trend = "Insufficient data"
            
            return {
                "total_runs": total_runs,
                "average_confidence": round(average_confidence, 3),
                "fallback_rate": round(fallback_rate, 3),
                "recent_trends": trend,
                "last_run": agent_memory[-1].get("timestamp") if agent_memory else None
            }
            
        except Exception as e:
            self.logger.error(f"Error getting agent insights: {e}")
            return {
                "total_runs": 0,
                "average_confidence": 0.0,
                "fallback_rate": 0.0,
                "recent_trends": "Error occurred"
            }
    
    async def get_similar_prompts(self, prompt: str, agent_name: str = None) -> List[Dict[str, Any]]:
        """Find similar prompts from memory"""
        try:
            memory_data = await self.read_memory()
            similar_prompts = []
            
            prompt_words = set(prompt.lower().split())
            
            for agent, entries in memory_data.get("agents", {}).items():
                if agent_name and agent != agent_name:
                    continue
                    
                for entry in entries:
                    entry_prompt = entry.get("prompt", "")
                    entry_words = set(entry_prompt.lower().split())
                    
                    # Calculate similarity (simple word overlap)
                    common_words = prompt_words.intersection(entry_words)
                    similarity = len(common_words) / max(len(prompt_words), 1)
                    
                    if similarity > 0.3:  # 30% word overlap threshold
                        similar_prompts.append({
                            "agent": agent,
                            "prompt": entry_prompt,
                            "response": entry.get("response", ""),
                            "confidence": entry.get("confidence", 0),
                            "similarity": round(similarity, 3),
                            "timestamp": entry.get("timestamp", "")
                        })
            
            # Sort by similarity
            similar_prompts.sort(key=lambda x: x["similarity"], reverse=True)
            return similar_prompts[:5]  # Return top 5
            
        except Exception as e:
            self.logger.error(f"Error finding similar prompts: {e}")
            return []
    
    async def clear_agent_memory(self, agent_name: str) -> bool:
        """Clear memory for a specific agent"""
        try:
            memory_data = await self.read_memory()
            if agent_name in memory_data.get("agents", {}):
                del memory_data["agents"][agent_name]
                await self.write_memory(memory_data)
                return True
            return False
        except Exception as e:
            self.logger.error(f"Error clearing agent memory: {e}")
            return False
    
    async def clear_all_memory(self) -> bool:
        """Clear all memory"""
        try:
            self._initialize_memory_file()
            return True
        except Exception as e:
            self.logger.error(f"Error clearing all memory: {e}")
            return False
    
    async def export_memory(self, filename: str = None) -> str:
        """Export memory to file"""
        try:
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"memory/agent_memory_export_{timestamp}.json"
            
            memory_data = await self.read_memory()
            with open(filename, 'w') as f:
                json.dump(memory_data, f, indent=2)
            
            return filename
        except Exception as e:
            self.logger.error(f"Error exporting memory: {e}")
            return ""
    
    async def get_memory_stats(self) -> Dict[str, Any]:
        """Get memory statistics"""
        try:
            memory_data = await self.read_memory()
            agents = memory_data.get("agents", {})
            
            total_agents = len(agents)
            total_entries = sum(len(entries) for entries in agents.values())
            
            agent_stats = {}
            for agent_name, entries in agents.items():
                if entries:
                    avg_confidence = sum(entry.get("confidence", 0) for entry in entries) / len(entries)
                    fallback_rate = sum(1 for entry in entries if entry.get("fallback_flag", False)) / len(entries)
                    
                    agent_stats[agent_name] = {
                        "entries": len(entries),
                        "avg_confidence": round(avg_confidence, 3),
                        "fallback_rate": round(fallback_rate, 3),
                        "last_run": entries[-1].get("timestamp") if entries else None
                    }
            
            return {
                "total_agents": total_agents,
                "total_entries": total_entries,
                "agent_stats": agent_stats,
                "metadata": memory_data.get("metadata", {})
            }
            
        except Exception as e:
            self.logger.error(f"Error getting memory stats: {e}")
            return {
                "total_agents": 0,
                "total_entries": 0,
                "agent_stats": {},
                "metadata": {}
            }

# Global memory instance
agent_memory = AgentMemory() 