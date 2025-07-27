"""
Prompt Patterns (Fusion v13)
----------------------------
Pattern application functions for transforming prompts.
"""

def apply_pattern(pattern_name: str, prompt: str) -> str:
    """
    Returns a transformed prompt using the named pattern.
    """
    if pattern_name == "stepwise_insight_synthesis":
        return f"Break this down step by step: {prompt}"
    elif pattern_name == "critique_then_rewrite":
        return f"Critique this first, then rewrite clearly: {prompt}"
    elif pattern_name == "role_directive":
        return f"Write this as a VP of Design: {prompt}"
    else:
        return prompt  # fallback
