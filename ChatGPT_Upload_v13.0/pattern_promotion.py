"""
Pattern Promotion Engine (Fusion v13)
-------------------------------------
Automatically promotes effective fallback patterns for reuse.
"""

from typing import List, Dict
import json
import os

PROMOTION_LOG_PATH = os.path.expanduser("~/fusion_v13/analytics/pattern_promotion_log.json")

def load_promotions() -> List[Dict]:
    if os.path.exists(PROMOTION_LOG_PATH):
        with open(PROMOTION_LOG_PATH, "r") as f:
            return json.load(f)
    return []

def save_promotions(promotions: List[Dict]):
    with open(PROMOTION_LOG_PATH, "w") as f:
        json.dump(promotions, f, indent=2)

def promote_pattern(pattern_name: str, original_prompt: str, improvement_score: float):
    promotions = load_promotions()
    promotions.append({
        "pattern": pattern_name,
        "original_prompt": original_prompt,
        "improvement_score": improvement_score
    })
    save_promotions(promotions)

def get_top_promoted_patterns(threshold: float = 0.15) -> List[str]:
    promotions = load_promotions()
    score_map = {}
    for promo in promotions:
        name = promo["pattern"]
        score = promo["improvement_score"]
        if name in score_map:
            score_map[name].append(score)
        else:
            score_map[name] = [score]
    return [k for k, scores in score_map.items() if sum(scores)/len(scores) >= threshold]
