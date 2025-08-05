# Fusion v14 - Memory System
# This file contains memory management, pattern recognition, and context management

import json
import time
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict
import hashlib

@dataclass
class MemoryEntry:
    timestamp: float
    agent_name: str
    input_text: str
    output: str
    confidence: float
    patterns_used: List[str]
    tools_used: List[str]
    execution_time: float

@dataclass
class PatternMemory:
    pattern_name: str
    usage_count: int
    success_rate: float
    last_used: float
    performance_metrics: Dict[str, Any]

class AgentMemory:
    def __init__(self):
        self.memory_file = "agent_memory.json"
        self.pattern_file = "pattern_registry.json"
        self.memory = []
        self.patterns = {}
        self.shared_state = {}
        
    def load_memory(self):
        """Load memory from file"""
        try:
            with open(self.memory_file, 'r') as f:
                data = json.load(f)
                self.memory = data.get('memory', [])
                self.patterns = data.get('patterns', {})
                self.shared_state = data.get('shared_state', {})
        except FileNotFoundError:
            self.memory = []
            self.patterns = {}
            self.shared_state = {}
    
    def save_memory(self):
        """Save memory to file"""
        data = {
            'memory': self.memory,
            'patterns': self.patterns,
            'shared_state': self.shared_state,
            'last_updated': time.time()
        }
        with open(self.memory_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def add_memory_entry(self, entry: MemoryEntry):
        """Add a new memory entry"""
        self.memory.append(asdict(entry))
        self._update_patterns(entry)
        self.save_memory()
    
    def _update_patterns(self, entry: MemoryEntry):
        """Update pattern statistics"""
        for pattern in entry.patterns_used:
            if pattern not in self.patterns:
                self.patterns[pattern] = {
                    'usage_count': 0,
                    'success_rate': 0.0,
                    'last_used': 0.0,
                    'performance_metrics': {}
                }
            
            pattern_data = self.patterns[pattern]
            pattern_data['usage_count'] += 1
            pattern_data['last_used'] = entry.timestamp
            
            # Update success rate based on confidence
            if entry.confidence > 0.7:
                pattern_data['success_rate'] = (
                    (pattern_data['success_rate'] * (pattern_data['usage_count'] - 1) + 1.0) 
                    / pattern_data['usage_count']
                )
    
    def get_relevant_memory(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Get memory entries relevant to the query"""
        # Simple relevance scoring based on keyword matching
        query_words = set(query.lower().split())
        
        scored_entries = []
        for entry in self.memory:
            entry_words = set(entry['input_text'].lower().split())
            overlap = len(query_words.intersection(entry_words))
            relevance_score = overlap / max(len(query_words), 1)
            
            if relevance_score > 0.1:  # Minimum relevance threshold
                scored_entries.append({
                    'entry': entry,
                    'relevance_score': relevance_score
                })
        
        # Sort by relevance and return top results
        scored_entries.sort(key=lambda x: x['relevance_score'], reverse=True)
        return [entry['entry'] for entry in scored_entries[:limit]]
    
    def get_pattern_performance(self, pattern_name: str) -> Optional[Dict[str, Any]]:
        """Get performance statistics for a specific pattern"""
        return self.patterns.get(pattern_name)
    
    def get_top_patterns(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get top performing patterns"""
        pattern_list = []
        for name, data in self.patterns.items():
            pattern_list.append({
                'name': name,
                **data
            })
        
        # Sort by success rate and usage count
        pattern_list.sort(key=lambda x: (x['success_rate'], x['usage_count']), reverse=True)
        return pattern_list[:limit]
    
    def update_shared_state(self, key: str, value: Any):
        """Update shared state"""
        self.shared_state[key] = value
        self.save_memory()
    
    def get_shared_state(self, key: str, default: Any = None) -> Any:
        """Get value from shared state"""
        return self.shared_state.get(key, default)
    
    def get_memory_summary(self) -> Dict[str, Any]:
        """Get summary of memory system"""
        return {
            'total_entries': len(self.memory),
            'total_patterns': len(self.patterns),
            'shared_state_keys': list(self.shared_state.keys()),
            'recent_entries': self.memory[-5:] if self.memory else [],
            'top_patterns': self.get_top_patterns(3)
        }

class PatternRegistry:
    def __init__(self):
        self.patterns = {
            'design_enhancement': {
                'description': 'Apply design principles and accessibility',
                'keywords': ['design', 'ui', 'ux', 'interface', 'layout'],
                'confidence_threshold': 0.6,
                'fallback_pattern': 'basic_evaluation'
            },
            'ux_audit': {
                'description': 'Perform comprehensive UX audit',
                'keywords': ['audit', 'evaluate', 'review', 'ux', 'usability'],
                'confidence_threshold': 0.7,
                'fallback_pattern': 'design_enhancement'
            },
            'trust_building': {
                'description': 'Analyze and enhance trust elements',
                'keywords': ['trust', 'security', 'privacy', 'reliability'],
                'confidence_threshold': 0.6,
                'fallback_pattern': 'design_enhancement'
            },
            'comprehensive_evaluation': {
                'description': 'Full evaluation with detailed scoring',
                'keywords': ['evaluate', 'assess', 'score', 'analyze'],
                'confidence_threshold': 0.8,
                'fallback_pattern': 'basic_evaluation'
            },
            'basic_evaluation': {
                'description': 'Essential evaluation criteria',
                'keywords': ['check', 'review', 'basic', 'simple'],
                'confidence_threshold': 0.5,
                'fallback_pattern': None
            }
        }
    
    def match_pattern(self, input_text: str) -> str:
        """Match input to the most appropriate pattern"""
        input_lower = input_text.lower()
        best_pattern = None
        best_score = 0
        
        for pattern_name, pattern_data in self.patterns.items():
            score = 0
            for keyword in pattern_data['keywords']:
                if keyword in input_lower:
                    score += 1
            
            if score > best_score:
                best_score = score
                best_pattern = pattern_name
        
        return best_pattern or 'design_enhancement'
    
    def get_pattern_info(self, pattern_name: str) -> Optional[Dict[str, Any]]:
        """Get information about a specific pattern"""
        return self.patterns.get(pattern_name)
    
    def get_fallback_pattern(self, pattern_name: str) -> Optional[str]:
        """Get fallback pattern for a given pattern"""
        pattern_info = self.patterns.get(pattern_name)
        return pattern_info.get('fallback_pattern') if pattern_info else None
    
    def list_patterns(self) -> List[str]:
        """List all available patterns"""
        return list(self.patterns.keys())

class FusionContext:
    def __init__(self):
        self.memory = AgentMemory()
        self.pattern_registry = PatternRegistry()
        self.session_id = self._generate_session_id()
        self.start_time = time.time()
        
    def _generate_session_id(self) -> str:
        """Generate unique session ID"""
        timestamp = str(time.time())
        return hashlib.md5(timestamp.encode()).hexdigest()[:8]
    
    def get_context_summary(self) -> Dict[str, Any]:
        """Get summary of current context"""
        memory_summary = self.memory.get_memory_summary()
        
        return {
            'session_id': self.session_id,
            'session_start': self.start_time,
            'session_duration': time.time() - self.start_time,
            'memory_entries': memory_summary['total_entries'],
            'patterns_available': len(self.pattern_registry.list_patterns()),
            'shared_state_keys': memory_summary['shared_state_keys'],
            'recent_interactions': memory_summary['recent_entries'][-3:],
            'top_patterns': memory_summary['top_patterns']
        }
    
    def add_interaction(self, agent_name: str, input_text: str, output: str, 
                        confidence: float, patterns_used: List[str], 
                        tools_used: List[str], execution_time: float):
        """Add a new interaction to memory"""
        entry = MemoryEntry(
            timestamp=time.time(),
            agent_name=agent_name,
            input_text=input_text,
            output=output,
            confidence=confidence,
            patterns_used=patterns_used,
            tools_used=tools_used,
            execution_time=execution_time
        )
        self.memory.add_memory_entry(entry)
    
    def get_relevant_context(self, query: str) -> List[Dict[str, Any]]:
        """Get relevant context for a query"""
        return self.memory.get_relevant_memory(query)
    
    def match_pattern_for_input(self, input_text: str) -> str:
        """Match input to appropriate pattern"""
        return self.pattern_registry.match_pattern(input_text)
    
    def export_context(self, filename: str = None):
        """Export context to file"""
        if filename is None:
            filename = f"fusion_context_{self.session_id}.json"
        
        context_data = {
            'session_id': self.session_id,
            'start_time': self.start_time,
            'context_summary': self.get_context_summary(),
            'memory': self.memory.memory,
            'patterns': self.memory.patterns,
            'shared_state': self.memory.shared_state
        }
        
        with open(filename, 'w') as f:
            json.dump(context_data, f, indent=2)
        
        return filename

# Initialize global context
fusion_context = FusionContext()

# Export for use in other modules
__all__ = ['fusion_context', 'AgentMemory', 'PatternRegistry', 'FusionContext', 'MemoryEntry'] 