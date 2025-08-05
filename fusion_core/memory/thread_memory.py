#!/usr/bin/env python3
"""
Thread Memory - Fusion v15.4
Agents persist memory across user sessions and reuse context intelligently.
"""

import json
import os
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from pathlib import Path

class ThreadMemory:
    """Persistent conversation memory across user sessions."""
    
    def __init__(self, user_id: str, thread_id: str, memory_dir: str = "thread_memory"):
        self.user_id = user_id
        self.thread_id = thread_id
        self.memory_dir = Path(memory_dir)
        self.memory_dir.mkdir(exist_ok=True)
        
        # Create user and thread directories
        self.user_dir = self.memory_dir / user_id
        self.user_dir.mkdir(exist_ok=True)
        
        self.thread_dir = self.user_dir / thread_id
        self.thread_dir.mkdir(exist_ok=True)
        
        # Memory file paths
        self.history_file = self.thread_dir / "history.json"
        self.summary_file = self.thread_dir / "summary.json"
        self.context_file = self.thread_dir / "context.json"
        
        # Load existing memory
        self.history = self._load_history()
        self.summary = self._load_summary()
        self.context = self._load_context()
    
    def _load_history(self) -> List[Dict[str, Any]]:
        """Load conversation history."""
        if self.history_file.exists():
            try:
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ Error loading history: {e}")
        return []
    
    def _load_summary(self) -> Dict[str, Any]:
        """Load conversation summary."""
        if self.summary_file.exists():
            try:
                with open(self.summary_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ Error loading summary: {e}")
        return {
            "created_at": datetime.now().isoformat(),
            "total_interactions": 0,
            "topics": [],
            "key_insights": [],
            "user_preferences": {}
        }
    
    def _load_context(self) -> Dict[str, Any]:
        """Load conversation context."""
        if self.context_file.exists():
            try:
                with open(self.context_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ Error loading context: {e}")
        return {
            "current_topic": None,
            "conversation_style": "professional",
            "user_expertise_level": "intermediate",
            "preferred_agents": [],
            "session_start": datetime.now().isoformat()
        }
    
    def append(self, input_text: str, output_text: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        """
        Append a new interaction to the thread memory.
        
        Args:
            input_text: User input
            output_text: Agent output
            metadata: Additional metadata (agent, confidence, etc.)
        """
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "input": input_text,
            "output": output_text,
            "metadata": metadata or {}
        }
        
        self.history.append(interaction)
        self.summary["total_interactions"] += 1
        
        # Update context based on interaction
        self._update_context(interaction)
        
        # Save to disk
        self._save_history()
        self._save_summary()
        self._save_context()
    
    def _update_context(self, interaction: Dict[str, Any]) -> None:
        """Update conversation context based on new interaction."""
        input_text = interaction["input"].lower()
        output_text = interaction["output"].lower()
        
        # Detect conversation style
        if any(word in input_text for word in ["casual", "informal", "hey", "hi"]):
            self.context["conversation_style"] = "casual"
        elif any(word in input_text for word in ["formal", "professional", "sir", "madam"]):
            self.context["conversation_style"] = "formal"
        
        # Detect expertise level
        technical_terms = ["api", "endpoint", "integration", "deployment", "architecture"]
        if any(term in input_text for term in technical_terms):
            self.context["user_expertise_level"] = "expert"
        elif any(term in input_text for term in ["how", "what", "explain", "help"]):
            self.context["user_expertise_level"] = "beginner"
        
        # Track preferred agents
        if "metadata" in interaction and "agent" in interaction["metadata"]:
            agent_name = interaction["metadata"]["agent"]
            if agent_name not in self.context["preferred_agents"]:
                self.context["preferred_agents"].append(agent_name)
        
        # Update current topic (simple keyword detection)
        topics = ["design", "development", "analysis", "strategy", "content", "evaluation"]
        for topic in topics:
            if topic in input_text or topic in output_text:
                self.context["current_topic"] = topic
                break
    
    def get_context(self, max_interactions: int = 5) -> str:
        """
        Get recent context for agent awareness.
        
        Args:
            max_interactions: Maximum number of recent interactions to include
            
        Returns:
            Formatted context string
        """
        if not self.history:
            return ""
        
        # Get recent interactions
        recent = self.history[-max_interactions:]
        
        context_parts = [
            f"Thread: {self.thread_id}",
            f"User: {self.user_id}",
            f"Style: {self.context['conversation_style']}",
            f"Expertise: {self.context['user_expertise_level']}",
            f"Topic: {self.context['current_topic'] or 'general'}",
            f"Preferred agents: {', '.join(self.context['preferred_agents'])}",
            "",
            "Recent interactions:"
        ]
        
        for interaction in recent:
            timestamp = datetime.fromisoformat(interaction["timestamp"]).strftime("%H:%M")
            context_parts.append(f"[{timestamp}] User: {interaction['input'][:100]}...")
            context_parts.append(f"[{timestamp}] Agent: {interaction['output'][:100]}...")
            context_parts.append("")
        
        return "\n".join(context_parts)
    
    def get_summary(self) -> Dict[str, Any]:
        """Get conversation summary."""
        return {
            "thread_id": self.thread_id,
            "user_id": self.user_id,
            "total_interactions": len(self.history),
            "conversation_style": self.context["conversation_style"],
            "user_expertise_level": self.context["user_expertise_level"],
            "current_topic": self.context["current_topic"],
            "preferred_agents": self.context["preferred_agents"],
            "created_at": self.summary["created_at"],
            "last_interaction": self.history[-1]["timestamp"] if self.history else None
        }
    
    def search(self, query: str) -> List[Dict[str, Any]]:
        """
        Search through thread memory.
        
        Args:
            query: Search query
            
        Returns:
            List of matching interactions
        """
        query_lower = query.lower()
        results = []
        
        for interaction in self.history:
            if (query_lower in interaction["input"].lower() or
                query_lower in interaction["output"].lower()):
                results.append(interaction)
        
        return results
    
    def get_insights(self) -> Dict[str, Any]:
        """Generate insights from the conversation."""
        if not self.history:
            return {}
        
        insights = {
            "conversation_duration": self._calculate_duration(),
            "interaction_frequency": self._calculate_frequency(),
            "common_topics": self._extract_topics(),
            "user_satisfaction": self._estimate_satisfaction(),
            "agent_performance": self._analyze_agent_performance()
        }
        
        return insights
    
    def _calculate_duration(self) -> str:
        """Calculate conversation duration."""
        if len(self.history) < 2:
            return "0 minutes"
        
        first_time = datetime.fromisoformat(self.history[0]["timestamp"])
        last_time = datetime.fromisoformat(self.history[-1]["timestamp"])
        duration = last_time - first_time
        
        minutes = duration.total_seconds() / 60
        return f"{minutes:.1f} minutes"
    
    def _calculate_frequency(self) -> str:
        """Calculate interaction frequency."""
        if len(self.history) < 2:
            return "N/A"
        
        first_time = datetime.fromisoformat(self.history[0]["timestamp"])
        last_time = datetime.fromisoformat(self.history[-1]["timestamp"])
        duration = last_time - first_time
        
        if duration.total_seconds() == 0:
            return "N/A"
        
        frequency = len(self.history) / (duration.total_seconds() / 60)
        return f"{frequency:.1f} interactions/minute"
    
    def _extract_topics(self) -> List[str]:
        """Extract common topics from conversation."""
        topics = ["design", "development", "analysis", "strategy", "content", "evaluation"]
        topic_counts = {topic: 0 for topic in topics}
        
        for interaction in self.history:
            text = f"{interaction['input']} {interaction['output']}".lower()
            for topic in topics:
                if topic in text:
                    topic_counts[topic] += 1
        
        return [topic for topic, count in topic_counts.items() if count > 0]
    
    def _estimate_satisfaction(self) -> str:
        """Estimate user satisfaction based on interaction patterns."""
        if not self.history:
            return "Unknown"
        
        # Simple heuristic based on interaction length and frequency
        avg_input_length = sum(len(i["input"]) for i in self.history) / len(self.history)
        avg_output_length = sum(len(i["output"]) for i in self.history) / len(self.history)
        
        if avg_input_length > 100 and avg_output_length > 200:
            return "High"
        elif avg_input_length > 50 and avg_output_length > 100:
            return "Medium"
        else:
            return "Low"
    
    def _analyze_agent_performance(self) -> Dict[str, Any]:
        """Analyze agent performance in this thread."""
        agent_stats = {}
        
        for interaction in self.history:
            if "metadata" in interaction and "agent" in interaction["metadata"]:
                agent_name = interaction["metadata"]["agent"]
                if agent_name not in agent_stats:
                    agent_stats[agent_name] = {
                        "count": 0,
                        "avg_confidence": 0.0,
                        "total_confidence": 0.0
                    }
                
                agent_stats[agent_name]["count"] += 1
                confidence = interaction["metadata"].get("confidence", 0.0)
                agent_stats[agent_name]["total_confidence"] += confidence
        
        # Calculate averages
        for agent_name, stats in agent_stats.items():
            if stats["count"] > 0:
                stats["avg_confidence"] = stats["total_confidence"] / stats["count"]
        
        return agent_stats
    
    def _save_history(self) -> None:
        """Save history to disk."""
        try:
            with open(self.history_file, 'w') as f:
                json.dump(self.history, f, indent=2)
        except Exception as e:
            print(f"❌ Error saving history: {e}")
    
    def _save_summary(self) -> None:
        """Save summary to disk."""
        try:
            with open(self.summary_file, 'w') as f:
                json.dump(self.summary, f, indent=2)
        except Exception as e:
            print(f"❌ Error saving summary: {e}")
    
    def _save_context(self) -> None:
        """Save context to disk."""
        try:
            with open(self.context_file, 'w') as f:
                json.dump(self.context, f, indent=2)
        except Exception as e:
            print(f"❌ Error saving context: {e}")
    
    def clear(self) -> None:
        """Clear all thread memory."""
        self.history = []
        self.summary = {
            "created_at": datetime.now().isoformat(),
            "total_interactions": 0,
            "topics": [],
            "key_insights": [],
            "user_preferences": {}
        }
        self.context = {
            "current_topic": None,
            "conversation_style": "professional",
            "user_expertise_level": "intermediate",
            "preferred_agents": [],
            "session_start": datetime.now().isoformat()
        }
        
        self._save_history()
        self._save_summary()
        self._save_context()

# Example usage
def main():
    """Example of using ThreadMemory."""
    # Create thread memory
    thread = ThreadMemory("user123", "project456")
    
    # Add some interactions
    thread.append(
        "Design a mobile app interface",
        "I'll create a modern, user-friendly mobile app interface with intuitive navigation...",
        {"agent": "vp_design", "confidence": 0.9}
    )
    
    thread.append(
        "Make it more colorful",
        "I'll add vibrant colors and engaging visual elements to make the interface more appealing...",
        {"agent": "creative_director", "confidence": 0.85}
    )
    
    # Get context
    context = thread.get_context()
    print("🧠 Thread Context:")
    print(context)
    
    # Get insights
    insights = thread.get_insights()
    print("\n📊 Thread Insights:")
    print(json.dumps(insights, indent=2))

if __name__ == "__main__":
    main() 