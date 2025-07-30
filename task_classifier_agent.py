# task_classifier_agent.py

class TaskClassifierAgent:
    def __init__(self):
        self.audience_to_voice = {
            "SLT": "executive",
            "senior leadership": "executive",
            "product lead": "executive",
            "eng lead": "thoughtful",
            "engineering": "thoughtful",
            "design peers": "thoughtful",
            "adobe": "executive",
            "twitter": "twitter-style",
            "substack": "irreverent",
            "founders": "founder",
        }

        self.intent_patterns = {
            "portfolio": {
                "chain": "PortfolioChain",
                "agents": ["vp_design", "content_designer", "evaluator"],
            },
            "deck": {
                "chain": "DeckNarrationChain",
                "agents": ["vp_design", "strategist", "content_designer"],
            },
            "substack": {
                "chain": "LongformCreativeChain",
                "agents": ["longform_writer", "surprisal_critic", "narrative_divergence"],
            },
            "one-pager": {
                "chain": "OnePagerChain",
                "agents": ["vp_design", "evaluator", "content_designer"],
            },
            "pov": {
                "chain": "POVDeclarationChain",
                "agents": ["vp_product", "vp_design", "content_designer"],
            },
        }

    def classify(self, input_text: str):
        text = input_text.lower()

        intent_match = None
        for pattern in self.intent_patterns:
            if pattern in text:
                intent_match = pattern
                break

        if not intent_match:
            intent_match = "one-pager"

        chain_info = self.intent_patterns[intent_match]

        detected_voice = "thoughtful"
        for audience, voice in self.audience_to_voice.items():
            if audience in text:
                detected_voice = voice
                break

        return {
            "chain_name": chain_info["chain"],
            "agent_chain": chain_info["agents"],
            "voice": detected_voice,
        } 