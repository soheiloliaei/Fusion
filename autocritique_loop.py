#!/usr/bin/env python3

from agents_combined import (
    EvaluatorAgent,
    NarrativeQualityChain,
    RewriteAdvisor
)
from voice_modulation_engine import VoiceModulationEngine

class AutoCritiqueLoop:
    def __init__(self, voice="executive"):
        self.evaluator = EvaluatorAgent()
        self.rater = NarrativeQualityChain()
        self.rewriter = RewriteAdvisor()
        self.voice_engine = VoiceModulationEngine()
        self.voice = voice

    async def run(self, text: str):
        evaluation = await self.evaluator.run(text)
        score_result = await self.rater.run(text)
        rewrite = await self.rewriter.run(text)
        modulated = self.voice_engine.apply_voice(text, self.voice)

        return {
            "evaluation": evaluation,
            **score_result,
            "recommendations": rewrite.get("suggestions", []),
            "modulated_instruction": modulated
        } 