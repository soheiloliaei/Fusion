"""
PatternPromoter (Fusion v13)
----------------------------
Scans execution memory for high-quality outputs and promotes them into reusable patterns.
"""

from datetime import datetime
from typing import List, Dict, Any
import os

PROMOTED_PATTERNS_PATH = "patterns/pattern_library.py"

class PatternPromoter:
    def __init__(self, threshold: float = 0.95):
        self.threshold = threshold

    def promote_from_memory(self, memory: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Analyze memory entries and promote high-quality outputs into reusable patterns.
        """
        promoted = []
        
        for run in memory:
            # Extract quality metrics
            result = run.get("result", {})
            overall_score = result.get("overall_score", 0)
            quality_metrics = result.get("quality_metrics", {})
            
            # Check if this run meets promotion threshold
            if overall_score >= self.threshold:
                prompt = run.get("input", "").strip()
                code_output = result.get("code", {}).get("output", "").strip()
                
                if prompt and code_output:
                    pattern_name = f"auto_promoted_{len(promoted)+1}"
                    pattern = {
                        "name": pattern_name,
                        "source_prompt": prompt,
                        "generated_code": code_output,
                        "score": overall_score,
                        "quality_metrics": quality_metrics,
                        "timestamp": datetime.now().isoformat(),
                        "original_run": run
                    }
                    promoted.append(pattern)
        
        # Write promoted patterns to library
        if promoted:
            self._write_patterns(promoted)
        
        return promoted

    def analyze_memory_quality(self, memory: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analyze memory quality and provide insights for pattern promotion.
        """
        if not memory:
            return {"total_runs": 0, "promotable_runs": 0, "avg_score": 0}
        
        total_runs = len(memory)
        promotable_runs = 0
        total_score = 0
        high_quality_runs = []
        
        for run in memory:
            result = run.get("result", {})
            score = result.get("overall_score", 0)
            total_score += score
            
            if score >= self.threshold:
                promotable_runs += 1
                high_quality_runs.append({
                    "prompt": run.get("input", ""),
                    "score": score,
                    "timestamp": run.get("timestamp", "")
                })
        
        avg_score = total_score / total_runs if total_runs > 0 else 0
        
        return {
            "total_runs": total_runs,
            "promotable_runs": promotable_runs,
            "avg_score": avg_score,
            "promotion_rate": promotable_runs / total_runs if total_runs > 0 else 0,
            "high_quality_runs": high_quality_runs
        }
