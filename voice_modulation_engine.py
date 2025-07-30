# voice_modulation_engine.py

class VoiceModulationEngine:
    def __init__(self):
        self.styles = {
            "executive": {
                "summary": "Elevated, strategic, succinct. Speaks to senior leaders.",
                "postfix": "Rewrite this as if it's being sent to C-level executives. Prioritize clarity, strategic framing, and remove any fluff.",
            },
            "thoughtful": {
                "summary": "Reflective, considered, articulate. Meant for peers and collaborators.",
                "postfix": "Make this thoughtful and nuanced, like you're explaining to a close collaborator. Avoid oversimplification.",
            },
            "irreverent": {
                "summary": "Playful, sharp, a little subversive. Perfect for Twitter or Substack.",
                "postfix": "Make this cheeky, high-signal, and irreverent. Break expectations and don't be afraid to be bold.",
            },
            "founder": {
                "summary": "Clear, direct, vision-driven. Ideal for builders and startup leads.",
                "postfix": "Make this sound like it's from a founder. Crisp, honest, and rooted in a vision or frustration.",
            },
            "twitter-style": {
                "summary": "One-liner smart. Designed to grab attention and start discussion.",
                "postfix": "Rewrite this as a viral Twitter thread starter. Max 2 sentences. Must provoke curiosity or debate.",
            },
        }

    def apply_voice(self, text: str, voice: str) -> str:
        if voice not in self.styles:
            return text  # fallback if unknown voice
        postfix = self.styles[voice]["postfix"]
        return f"{text.strip()}\n\n{postfix}" 