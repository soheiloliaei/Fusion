"""
PatternMatcher (Fusion v13)
----------------------------
Detects matching patterns based on keywords and quality metrics
"""

from typing import Dict, Any, Optional, List
from patterns.pattern_registry import PATTERNS

class PatternMatcher:
    def __init__(self):
        self.patterns = PATTERNS

    def match_by_keywords(self, prompt: str) -> Optional[str]:
        prompt = prompt.lower()
        for key, pattern in self.patterns.items():
            triggers = pattern.get("triggers", [])
            if any(trigger in prompt for trigger in triggers):
                return key
        return None

    def match_by_quality(self, quality_metrics: Dict[str, float], overall_score: float) -> Optional[str]:
        if overall_score < 0.8:
            return "critique_then_rewrite"
        for metric, score in quality_metrics.items():
            if metric == "clarity_score" and score < 0.75:
                return "stepwise_insight_synthesis"
            elif metric == "completeness" and score < 0.75:
                return "role_directive"
        return None

    def match(self, prompt: str, quality: Dict[str, Any]) -> Dict[str, Any]:
        overall_score = quality.get("overall_score", 1.0)
        metrics = quality.get("quality_metrics", {})
        keyword_match = self.match_by_keywords(prompt)
        quality_match = self.match_by_quality(metrics, overall_score)

        if keyword_match:
            return {"match_type": "keyword", "pattern": keyword_match}
        elif quality_match:
            return {"match_type": "quality", "pattern": quality_match}
        else:
            return {"match_type": "none", "pattern": None}
