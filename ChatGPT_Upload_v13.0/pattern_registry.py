"""
Pattern Registry (Fusion v13)
----------------------------
Pattern-based fallback and enhancement logic for the ExecutionChainOrchestrator
"""

from typing import Dict, List, Any, Optional
import json
import re
from datetime import datetime

# Pattern definitions
PATTERNS = {
    "stepwise_insight_synthesis": {
        "name": "Stepwise Insight Synthesis",
        "description": "Break down complex problems into step-by-step insights",
        "triggers": ["complex", "complicated", "difficult", "challenging", "multi-step"],
        "confidence_boost": 0.15,
        "implementation": "stepwise_breakdown"
    },
    "critique_then_rewrite": {
        "name": "Critique Then Rewrite",
        "description": "Critically analyze output and provide improved version",
        "triggers": ["review", "improve", "enhance", "better", "optimize"],
        "confidence_boost": 0.20,
        "implementation": "critique_and_rewrite"
    },
    "role_directive": {
        "name": "Role Directive",
        "description": "Apply specific role-based thinking to the problem",
        "triggers": ["role", "perspective", "viewpoint", "lens", "approach"],
        "confidence_boost": 0.10,
        "implementation": "role_based_analysis"
    }
}

def fallback_to_pattern(output: Dict[str, Any]) -> Optional[str]:
    """
    Determine if fallback to pattern is needed based on output quality
    """
    if not isinstance(output, dict):
        return None
    
    # Check for low quality indicators
    quality_metrics = output.get("metrics", {})
    overall_score = output.get("overall_score", 0.0)
    
    # If overall score is low, suggest patterns
    if overall_score < 0.8:
        return "critique_then_rewrite"
    
    # Check specific metric failures
    failed_metrics = []
    for metric, score in quality_metrics.items():
        if score < 0.8:
            failed_metrics.append(metric)
    
    # Suggest patterns based on failed metrics
    if "clarity_score" in failed_metrics:
        return "stepwise_insight_synthesis"
    elif "completeness" in failed_metrics:
        return "role_directive"
    elif "actionability" in failed_metrics:
        return "critique_then_rewrite"
    
    return None

def get_pattern_metadata(pattern_name: str) -> Optional[Dict[str, Any]]:
    """
    Get metadata for a specific pattern
    """
    return PATTERNS.get(pattern_name)

def apply_pattern(pattern_name: str, content: str, context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Apply a specific pattern to content
    """
    pattern = PATTERNS.get(pattern_name)
    if not pattern:
        return {"error": f"Pattern {pattern_name} not found"}
    
    return {
        "pattern_applied": pattern_name,
        "enhanced_content": content + "\n\n[Pattern applied: " + pattern["name"] + "]",
        "confidence_boost": pattern["confidence_boost"],
        "timestamp": datetime.now().isoformat()
    }
