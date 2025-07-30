"""
Pattern Registry - Fusion v14
Pattern fallback and metadata management
"""

import json
import time
from typing import Dict, Any, List, Optional
from datetime import datetime
import logging

class PatternRegistry:
    """
    Pattern Registry - Fusion v14
    Manages patterns with fallback mechanisms and metadata
    """
    
    def __init__(self):
        self.logger = logging.getLogger("PatternRegistry")
        self.patterns = {}
        self.pattern_metadata = {}
        self.fallback_patterns = {}
        self.pattern_usage_stats = {}
        
        # Initialize default patterns
        self._initialize_default_patterns()
        
    def _initialize_default_patterns(self):
        """Initialize default patterns for Fusion v14"""
        
        # Design enhancement patterns
        self.register_pattern("design_enhancement", {
            "type": "prompt_enhancement",
            "agent": "vp_design",
            "enhancement": "Apply user-centered design principles and ensure accessibility compliance. Focus on visual hierarchy, consistency, and user experience optimization.",
            "confidence_threshold": 0.8,
            "fallback_patterns": ["ux_audit", "trust_building"],
            "metadata": {
                "category": "design",
                "tags": ["ui", "ux", "accessibility"],
                "created": datetime.now().isoformat(),
                "version": "1.0"
            }
        })
        
        # UX audit patterns
        self.register_pattern("ux_audit", {
            "type": "tool_enhancement",
            "agent": "vp_design",
            "tools": ["ux_audit_tool"],
            "enhancement": "Perform comprehensive UX audit using heuristic evaluation and metrics analysis.",
            "confidence_threshold": 0.85,
            "fallback_patterns": ["design_enhancement"],
            "metadata": {
                "category": "ux",
                "tags": ["audit", "heuristics", "metrics"],
                "created": datetime.now().isoformat(),
                "version": "1.0"
            }
        })
        
        # Trust building patterns
        self.register_pattern("trust_building", {
            "type": "tool_enhancement",
            "agent": "vp_design",
            "tools": ["trust_explainer_tool"],
            "enhancement": "Analyze and enhance trust-building elements in the user experience.",
            "confidence_threshold": 0.8,
            "fallback_patterns": ["design_enhancement"],
            "metadata": {
                "category": "trust",
                "tags": ["transparency", "security", "social_proof"],
                "created": datetime.now().isoformat(),
                "version": "1.0"
            }
        })
        
        # Evaluation patterns
        self.register_pattern("comprehensive_evaluation", {
            "type": "agent_enhancement",
            "agent": "evaluator",
            "enhancement": "Perform comprehensive evaluation across all criteria with detailed scoring and recommendations.",
            "confidence_threshold": 0.9,
            "fallback_patterns": ["basic_evaluation"],
            "metadata": {
                "category": "evaluation",
                "tags": ["scoring", "analysis", "recommendations"],
                "created": datetime.now().isoformat(),
                "version": "1.0"
            }
        })
        
        # Basic evaluation fallback
        self.register_pattern("basic_evaluation", {
            "type": "agent_enhancement",
            "agent": "evaluator",
            "enhancement": "Perform basic evaluation with essential criteria.",
            "confidence_threshold": 0.7,
            "fallback_patterns": [],
            "metadata": {
                "category": "evaluation",
                "tags": ["basic", "essential"],
                "created": datetime.now().isoformat(),
                "version": "1.0"
            }
        })
        
    def register_pattern(self, name: str, pattern_data: Dict[str, Any]) -> None:
        """Register a new pattern"""
        
        if name in self.patterns:
            self.logger.warning(f"Pattern {name} already exists, updating...")
            
        self.patterns[name] = pattern_data
        self.pattern_metadata[name] = pattern_data.get("metadata", {})
        self.pattern_usage_stats[name] = {
            "usage_count": 0,
            "success_count": 0,
            "last_used": None,
            "avg_confidence": 0.0
        }
        
        # Set up fallback patterns
        fallback_patterns = pattern_data.get("fallback_patterns", [])
        self.fallback_patterns[name] = fallback_patterns
        
        self.logger.info(f"Registered pattern: {name}")
        
    def get_pattern(self, name: str) -> Optional[Dict[str, Any]]:
        """Get a pattern by name"""
        return self.patterns.get(name)
        
    def list_patterns(self, category: str = None) -> List[str]:
        """List all patterns, optionally filtered by category"""
        
        if category:
            return [name for name, metadata in self.pattern_metadata.items() 
                   if metadata.get("category") == category]
        else:
            return list(self.patterns.keys())
            
    def find_best_pattern(self, input_prompt: str, context: Dict[str, Any] = None) -> str:
        """Find the best pattern for a given input"""
        
        # Simple pattern matching based on keywords
        prompt_lower = input_prompt.lower()
        
        # Design-related patterns
        if any(word in prompt_lower for word in ["design", "ui", "ux", "interface"]):
            if "audit" in prompt_lower or "evaluate" in prompt_lower:
                return "ux_audit"
            elif "trust" in prompt_lower or "confidence" in prompt_lower:
                return "trust_building"
            else:
                return "design_enhancement"
                
        # Evaluation-related patterns
        elif any(word in prompt_lower for word in ["evaluate", "assess", "score", "analyze"]):
            return "comprehensive_evaluation"
            
        # Default to design enhancement
        return "design_enhancement"
        
    def get_fallback_patterns(self, pattern_name: str) -> List[str]:
        """Get fallback patterns for a given pattern"""
        return self.fallback_patterns.get(pattern_name, [])
        
    def should_apply_pattern(self, pattern_name: str, confidence: float) -> bool:
        """Determine if a pattern should be applied based on confidence"""
        
        pattern = self.patterns.get(pattern_name)
        if not pattern:
            return False
            
        threshold = pattern.get("confidence_threshold", 0.8)
        return confidence < threshold
        
    def get_pattern_enhancement(self, pattern_name: str) -> str:
        """Get the enhancement prompt for a pattern"""
        
        pattern = self.patterns.get(pattern_name)
        if not pattern:
            return ""
            
        return pattern.get("enhancement", "")
        
    def get_pattern_tools(self, pattern_name: str) -> List[str]:
        """Get the tools required for a pattern"""
        
        pattern = self.patterns.get(pattern_name)
        if not pattern:
            return []
            
        return pattern.get("tools", [])
        
    def record_pattern_usage(self, pattern_name: str, confidence: float, success: bool = True) -> None:
        """Record pattern usage statistics"""
        
        if pattern_name not in self.pattern_usage_stats:
            self.pattern_usage_stats[pattern_name] = {
                "usage_count": 0,
                "success_count": 0,
                "last_used": None,
                "avg_confidence": 0.0
            }
            
        stats = self.pattern_usage_stats[pattern_name]
        stats["usage_count"] += 1
        stats["last_used"] = datetime.now().isoformat()
        
        if success:
            stats["success_count"] += 1
            
        # Update average confidence
        current_avg = stats["avg_confidence"]
        usage_count = stats["usage_count"]
        stats["avg_confidence"] = ((current_avg * (usage_count - 1)) + confidence) / usage_count
        
        self.logger.info(f"Recorded usage for pattern {pattern_name}: confidence={confidence:.2f}, success={success}")
        
    def get_pattern_stats(self, pattern_name: str) -> Dict[str, Any]:
        """Get statistics for a specific pattern"""
        
        stats = self.pattern_usage_stats.get(pattern_name, {})
        metadata = self.pattern_metadata.get(pattern_name, {})
        
        return {
            "name": pattern_name,
            "usage_count": stats.get("usage_count", 0),
            "success_count": stats.get("success_count", 0),
            "success_rate": stats.get("success_count", 0) / max(stats.get("usage_count", 1), 1),
            "avg_confidence": stats.get("avg_confidence", 0.0),
            "last_used": stats.get("last_used"),
            "metadata": metadata
        }
        
    def get_all_pattern_stats(self) -> Dict[str, Any]:
        """Get statistics for all patterns"""
        
        all_stats = {}
        for pattern_name in self.patterns.keys():
            all_stats[pattern_name] = self.get_pattern_stats(pattern_name)
            
        return all_stats
        
    def get_top_patterns(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get top performing patterns"""
        
        all_stats = self.get_all_pattern_stats()
        
        # Sort by success rate and usage count
        sorted_patterns = sorted(
            all_stats.values(),
            key=lambda x: (x["success_rate"], x["usage_count"]),
            reverse=True
        )
        
        return sorted_patterns[:limit]
        
    def export_patterns(self, filepath: str) -> None:
        """Export patterns to JSON file"""
        
        export_data = {
            "patterns": self.patterns,
            "metadata": self.pattern_metadata,
            "fallback_patterns": self.fallback_patterns,
            "usage_stats": self.pattern_usage_stats,
            "export_timestamp": datetime.now().isoformat()
        }
        
        with open(filepath, 'w') as f:
            json.dump(export_data, f, indent=2)
            
        self.logger.info(f"Exported patterns to {filepath}")
        
    def import_patterns(self, filepath: str) -> None:
        """Import patterns from JSON file"""
        
        try:
            with open(filepath, 'r') as f:
                import_data = json.load(f)
                
            self.patterns.update(import_data.get("patterns", {}))
            self.pattern_metadata.update(import_data.get("metadata", {}))
            self.fallback_patterns.update(import_data.get("fallback_patterns", {}))
            self.pattern_usage_stats.update(import_data.get("usage_stats", {}))
            
            self.logger.info(f"Imported patterns from {filepath}")
            
        except Exception as e:
            self.logger.error(f"Failed to import patterns: {e}")
            
    def create_custom_pattern(self, name: str, pattern_type: str, agent: str,
                            enhancement: str, tools: List[str] = None,
                            confidence_threshold: float = 0.8,
                            fallback_patterns: List[str] = None,
                            category: str = "custom",
                            tags: List[str] = None) -> None:
        """Create a custom pattern"""
        
        pattern_data = {
            "type": pattern_type,
            "agent": agent,
            "enhancement": enhancement,
            "tools": tools or [],
            "confidence_threshold": confidence_threshold,
            "fallback_patterns": fallback_patterns or [],
            "metadata": {
                "category": category,
                "tags": tags or [],
                "created": datetime.now().isoformat(),
                "version": "1.0",
                "custom": True
            }
        }
        
        self.register_pattern(name, pattern_data)
        self.logger.info(f"Created custom pattern: {name}")
        
    def get_pattern_summary(self) -> str:
        """Get a summary of all patterns"""
        
        summary = f"# Pattern Registry Summary\n\n"
        summary += f"**Total Patterns:** {len(self.patterns)}\n"
        summary += f"**Categories:** {', '.join(set(meta.get('category', 'unknown') for meta in self.pattern_metadata.values()))}\n\n"
        
        summary += f"## Pattern Categories\n\n"
        
        categories = {}
        for name, metadata in self.pattern_metadata.items():
            category = metadata.get("category", "unknown")
            if category not in categories:
                categories[category] = []
            categories[category].append(name)
            
        for category, patterns in categories.items():
            summary += f"### {category.title()}\n"
            for pattern in patterns:
                stats = self.get_pattern_stats(pattern)
                summary += f"- **{pattern}:** {stats['usage_count']} uses, {stats['success_rate']:.2f} success rate\n"
            summary += "\n"
            
        return summary
