#!/usr/bin/env python3

import asyncio
from agents_combined import NarrativeQualityChain

async def test_narrative_quality():
    # Test different contexts and content types
    test_cases = [
        {
            "context": "founder",
            "content": "I used to believe fallback UX was a luxury. But then a Cash App outage forced us to rebuild trust from scratch in under 24 hours. The real issue is that most teams don't understand the vision behind resilient design."
        },
        {
            "context": "substack", 
            "content": "This is a revolutionary game changer that will disrupt the paradigm of user experience design. The innovative solution provides a seamless experience that is cutting edge and data-driven."
        },
        {
            "context": "executive",
            "content": "The strategic implementation of fallback UX patterns demonstrates measurable ROI improvements in user retention and satisfaction metrics."
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n=== Test Case {i}: {test_case['context'].upper()} ===")
        print(f"Content: {test_case['content'][:100]}...")
        
        chain = NarrativeQualityChain(context=test_case["context"])
        result = await chain.run(test_case["content"])
        
        print(f"Score: {result['score']}")
        print(f"Verdict: {result['verdict']}")
        print(f"Issues: {result['issues']}")
        print(f"Voice Feedback: {result['voice_feedback']}")
        print(f"Recommendations: {result['recommendations'][:2]}...")
        
        if result['freshness_details']['clichés']:
            print(f"Clichés Found: {result['freshness_details']['clichés']}")

if __name__ == "__main__":
    asyncio.run(test_narrative_quality()) 