#!/usr/bin/env python3

import asyncio
from autocritique_loop import AutoCritiqueLoop

async def test_autocritique():
    # Test different content types and voices
    test_cases = [
        {
            "text": "Here's a draft of my POV on fallback UX for SLT. It's a game changer that will shift the paradigm of user experience design. The innovative solution provides a seamless experience that is cutting edge and data-driven.",
            "voice": "executive"
        },
        {
            "text": "I used to believe fallback UX was a luxury. But then a Cash App outage forced us to rebuild trust from scratch in under 24 hours. The real issue is that most teams don't understand the vision behind resilient design.",
            "voice": "founder"
        },
        {
            "text": "The strategic implementation of fallback UX patterns demonstrates measurable ROI improvements in user retention and satisfaction metrics across enterprise deployments.",
            "voice": "thoughtful"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n=== Test Case {i}: {test_case['voice'].upper()} VOICE ===")
        print(f"Content: {test_case['text'][:80]}...")
        
        loop = AutoCritiqueLoop(voice=test_case["voice"])
        result = await loop.run(test_case["text"])
        
        print(f"Score: {result['score']}")
        print(f"Verdict: {result['verdict']}")
        print(f"Issues: {result['issues']}")
        print(f"Voice Feedback: {result['voice_feedback']}")
        print(f"Recommendations: {result['recommendations'][:2]}...")
        print(f"Modulated Instruction: {result['modulated_instruction'][:100]}...")
        
        if result.get('freshness_details', {}).get('clichés'):
            print(f"Clichés Found: {result['freshness_details']['clichés']}")

if __name__ == "__main__":
    asyncio.run(test_autocritique()) 