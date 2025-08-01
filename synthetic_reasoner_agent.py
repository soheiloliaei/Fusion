# synthetic_reasoner_agent.py

class SyntheticReasonerAgent:
    def __init__(self, context=None):
        self.context = context or {}

    def run(self, user_input, target_agent_name):
        prompt = f"""
You are the inner thought process for agent: {target_agent_name}.
Before this agent acts, you will:

1. Generate 3–5 *synthetic thoughts* (what are the hidden challenges, assumptions, or ambiguities?)
2. Ask 3–5 *synthetic queries* (what would you ask yourself before acting?)
3. Output a *risk_score* from 0.0 to 1.0 (how risky is it to act on this without clarification?)

User input: "{user_input}"
""".strip()

        # 🧪 Simulated output for Sprint 1 (Replace with LLM call in Sprint 2)
        return {
            "synthetic_thoughts": [
                "The user might expect both critique and rewrite.",
                "It's unclear whether Tailwind or Markdown output is preferred.",
                "This may trigger fallback pattern if confidence is low."
            ],
            "synthetic_queries": [
                "Should I use the Executive Rewriter pattern?",
                "Is the user expecting structured output?",
                "Should this pass through RewriteLoopAgent after critique?"
            ],
            "risk_score": 0.41
        } 