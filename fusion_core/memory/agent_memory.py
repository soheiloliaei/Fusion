# fusion_core/memory/agent_memory.py

import json
import os
from typing import List, Dict, Any
from datetime import datetime

class AgentMemory:
    def __init__(self, agent_name: str, memory_dir="fusion_memory"):
        self.agent_name = agent_name
        self.memory_path = os.path.join(memory_dir, f"{agent_name}.json")
        os.makedirs(memory_dir, exist_ok=True)
        self._load()

    def _load(self):
        """Load existing memory or create new memory file"""
        if os.path.exists(self.memory_path):
            with open(self.memory_path, "r") as f:
                self.data = json.load(f)
        else:
            self.data = {
                "agent_name": self.agent_name,
                "created_at": datetime.now().isoformat(),
                "history": [],
                "metadata": {
                    "total_runs": 0,
                    "last_run": None,
                    "success_rate": 0.0
                }
            }

    def append(self, input_text: str, output_text: str, metadata: Dict[str, Any] = None):
        """Append a new interaction to memory"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "input": input_text,
            "output": output_text,
            "metadata": metadata or {}
        }
        
        self.data["history"].append(entry)
        self.data["metadata"]["total_runs"] += 1
        self.data["metadata"]["last_run"] = datetime.now().isoformat()
        
        # Calculate success rate (simple heuristic)
        if len(self.data["history"]) > 0:
            successful_runs = sum(1 for entry in self.data["history"] 
                               if entry.get("metadata", {}).get("success", True))
            self.data["metadata"]["success_rate"] = successful_runs / len(self.data["history"])
        
        self._save()

    def _save(self):
        """Save memory to disk"""
        with open(self.memory_path, "w") as f:
            json.dump(self.data, f, indent=2)

    def get_last(self, n: int = 1) -> List[Dict[str, Any]]:
        """Get the last n interactions"""
        return self.data["history"][-n:] if self.data["history"] else []

    def get_context(self, max_entries: int = 5) -> str:
        """Get recent context for agent awareness"""
        recent = self.get_last(max_entries)
        if not recent:
            return ""
        
        context = f"Recent interactions for {self.agent_name}:\n"
        for entry in recent:
            context += f"- Input: {entry['input'][:100]}...\n"
            context += f"  Output: {entry['output'][:100]}...\n"
            context += f"  Time: {entry['timestamp']}\n\n"
        
        return context

    def get_metadata(self) -> Dict[str, Any]:
        """Get agent metadata and statistics"""
        return self.data["metadata"]

    def clear(self):
        """Clear all memory (use with caution)"""
        self.data["history"] = []
        self.data["metadata"]["total_runs"] = 0
        self.data["metadata"]["last_run"] = None
        self.data["metadata"]["success_rate"] = 0.0
        self._save()

    def search(self, query: str) -> List[Dict[str, Any]]:
        """Search through memory for relevant entries"""
        results = []
        query_lower = query.lower()
        
        for entry in self.data["history"]:
            if (query_lower in entry["input"].lower() or 
                query_lower in entry["output"].lower()):
                results.append(entry)
        
        return results 