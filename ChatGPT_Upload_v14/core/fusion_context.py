"""
Fusion Context - Fusion v14
Shared state and memory management for the agent OS
"""

import json
import asyncio
from typing import Dict, Any, List, Optional
from datetime import datetime
from dataclasses import dataclass, asdict
import logging

@dataclass
class MemoryEntry:
    timestamp: str
    agent_name: str
    input_prompt: str
    output: Dict[str, Any]
    confidence: float
    tools_used: List[str]
    execution_time: float
    pattern_applied: Optional[str] = None

class FusionContext:
    """
    Shared state and memory management for Fusion v14
    Provides context across all agents and tools
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.shared_state: Dict[str, Any] = {}
        self.memory: List[MemoryEntry] = []
        self.pattern_memory: Dict[str, Any] = {}
        self.execution_history: List[Dict[str, Any]] = []
        self.current_session_id = datetime.now().isoformat()
        
        # Setup logging
        logging.basicConfig(
            level=getattr(logging, config.get("log_level", "INFO")),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger("FusionContext")
        
    async def store_interaction(self, agent_name: str, input_prompt: str, 
                              output: Dict[str, Any], confidence: float = 0.8,
                              tools_used: List[str] = None, execution_time: float = 0.0,
                              pattern_applied: str = None) -> None:
        """Store an agent interaction in memory"""
        
        entry = MemoryEntry(
            timestamp=datetime.now().isoformat(),
            agent_name=agent_name,
            input_prompt=input_prompt,
            output=output,
            confidence=confidence,
            tools_used=tools_used or [],
            execution_time=execution_time,
            pattern_applied=pattern_applied
        )
        
        self.memory.append(entry)
        self.logger.info(f"Stored interaction for {agent_name} with confidence {confidence}")
        
    def get_shared_state(self, key: str, default: Any = None) -> Any:
        """Get value from shared state"""
        return self.shared_state.get(key, default)
        
    def set_shared_state(self, key: str, value: Any) -> None:
        """Set value in shared state"""
        self.shared_state[key] = value
        self.logger.debug(f"Set shared state {key}: {value}")
        
    def get_relevant_memory(self, query: str, limit: int = 5) -> List[MemoryEntry]:
        """Get relevant memory entries based on query similarity"""
        # Simple keyword matching for now
        relevant = []
        query_lower = query.lower()
        
        for entry in reversed(self.memory):
            if any(word in entry.input_prompt.lower() for word in query_lower.split()):
                relevant.append(entry)
                if len(relevant) >= limit:
                    break
                    
        return relevant
        
    def get_pattern_memory(self, pattern_name: str) -> Dict[str, Any]:
        """Get pattern memory for a specific pattern"""
        return self.pattern_memory.get(pattern_name, {})
        
    def store_pattern_memory(self, pattern_name: str, data: Dict[str, Any]) -> None:
        """Store pattern-specific memory"""
        if pattern_name not in self.pattern_memory:
            self.pattern_memory[pattern_name] = {}
        self.pattern_memory[pattern_name].update(data)
        
    def get_execution_stats(self) -> Dict[str, Any]:
        """Get execution statistics"""
        if not self.memory:
            return {"total_interactions": 0, "avg_confidence": 0.0}
            
        total_interactions = len(self.memory)
        avg_confidence = sum(entry.confidence for entry in self.memory) / total_interactions
        avg_execution_time = sum(entry.execution_time for entry in self.memory) / total_interactions
        
        return {
            "total_interactions": total_interactions,
            "avg_confidence": avg_confidence,
            "avg_execution_time": avg_execution_time,
            "session_id": self.current_session_id,
            "memory_size": len(self.memory)
        }
        
    def clear_memory(self) -> None:
        """Clear all memory (use with caution)"""
        self.memory.clear()
        self.pattern_memory.clear()
        self.shared_state.clear()
        self.logger.info("Memory cleared")
        
    def export_memory(self, filepath: str) -> None:
        """Export memory to JSON file"""
        memory_data = {
            "session_id": self.current_session_id,
            "memory": [asdict(entry) for entry in self.memory],
            "pattern_memory": self.pattern_memory,
            "shared_state": self.shared_state
        }
        
        with open(filepath, 'w') as f:
            json.dump(memory_data, f, indent=2)
            
        self.logger.info(f"Memory exported to {filepath}")
        
    def import_memory(self, filepath: str) -> None:
        """Import memory from JSON file"""
        try:
            with open(filepath, 'r') as f:
                memory_data = json.load(f)
                
            # Import memory entries
            for entry_data in memory_data.get("memory", []):
                entry = MemoryEntry(**entry_data)
                self.memory.append(entry)
                
            # Import pattern memory
            self.pattern_memory.update(memory_data.get("pattern_memory", {}))
            
            # Import shared state
            self.shared_state.update(memory_data.get("shared_state", {}))
            
            self.logger.info(f"Memory imported from {filepath}")
            
        except Exception as e:
            self.logger.error(f"Failed to import memory: {e}")
            
    def get_context_summary(self) -> str:
        """Get a summary of current context"""
        stats = self.get_execution_stats()
        recent_memory = self.memory[-5:] if self.memory else []
        
        summary = f"""
Fusion v14 Context Summary:
- Session ID: {self.current_session_id}
- Total Interactions: {stats['total_interactions']}
- Average Confidence: {stats['avg_confidence']:.2f}
- Memory Size: {stats['memory_size']}
- Shared State Keys: {list(self.shared_state.keys())}
- Pattern Memory Keys: {list(self.pattern_memory.keys())}

Recent Interactions:
"""
        
        for entry in recent_memory:
            summary += f"- {entry.agent_name}: {entry.input_prompt[:50]}... (confidence: {entry.confidence:.2f})\n"
            
        return summary 