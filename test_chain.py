#!/usr/bin/env python3

import asyncio
from agents_combined import LongformCreativeChain, VPDesignAgent

async def test_chain():
    chain = LongformCreativeChain()
    main_agent = VPDesignAgent()
    
    result = await chain.run("Here's a post about Cursor and fallback UX again...", main_agent)
    print("=== LongformCreativeChain Test ===")
    print(f"Original Input: {result['original_input']}")
    print(f"Divergent Input: {result['divergent_input']}")
    print(f"Agent Output: {result['agent_output']['output'][:200]}...")
    print(f"Surprisal Review: {result['surprisal_review']['output']}")

if __name__ == "__main__":
    asyncio.run(test_chain()) 