"""
Creative Director Agent – Fusion v13
Applies critique, rewrite, and elevation to improve final output.
"""
from patterns.creative_director_patterns import apply_creative_critique

class CreativeDirectorAgent:
    def critique_output(self, input_prompt, final_output):
        critique = apply_creative_critique(input_prompt, final_output)
        return {
            "enhanced_output": critique.get("enhanced"),
            "feedback": critique.get("feedback"),
            "score_lift": critique.get("score_lift", 0.1)
        }
