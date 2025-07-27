"""
Pattern Memory Loader (Fusion v13)
----------------------------------
Loads top promoted patterns into orchestrator memory at runtime.
"""

from analytics.pattern_promotion import get_top_promoted_patterns
from patterns.pattern_registry import PATTERNS

def load_promoted_patterns() -> dict:
    top_patterns = get_top_promoted_patterns()
    loaded = {}
    for pattern_name in top_patterns:
        pattern_data = PATTERNS.get(pattern_name, {})
        if pattern_data:
            loaded[pattern_name] = pattern_data
    return loaded
