"""
Creative Director Patterns – Rewrite and critique logic
"""

def apply_creative_critique(input_prompt, output):
    feedback = []
    score_lift = 0.1
    enhanced = output

    if "too verbose" in output or "unclear" in output:
        feedback.append("Output is unclear or verbose. Needs more punch.")
        enhanced = output.replace("too verbose", "concise").replace("unclear", "sharp and direct")
        score_lift = 0.2
    if "value" not in output.lower():
        feedback.append("Missing clear value proposition.")
        enhanced += " → Refocus on the outcome or benefit."

    if not feedback:
        feedback.append("Output is solid, but consider adding edge or provocation.")

    return {
        "feedback": feedback,
        "enhanced": enhanced,
        "score_lift": score_lift
    }
