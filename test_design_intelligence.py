#!/usr/bin/env python3

import asyncio
import sys
import os

# Add the current directory to the path so we can import from agents
sys.path.append('.')

from agents.design_designintelligence import (
    run_design_pipeline,
    analyze_figma_frame,
    analyze_uploaded_image,
    analyze_motion_design
)

async def test_design_intelligence():
    """Test all design intelligence functions"""
    
    print("🧠 Testing Full AI-Native Design Intelligence Stack")
    print("=" * 60)
    
    # Test 1: Full Design Pipeline
    print("\n1️⃣ Testing Design Pipeline")
    print("-" * 30)
    design_prompt = "Design a fallback UX tile for failed Bitcoin withdrawals"
    pipeline_result = await run_design_pipeline(design_prompt)
    print(f"✅ Design Pipeline Complete")
    print(f"   - Tile Logic: {pipeline_result['tile_logic']['detected_declaration']}")
    print(f"   - Wireframe: {pipeline_result['wireframe']['layout_type']}")
    print(f"   - Critique Score: {pipeline_result['critique']['heuristics_score']}")
    print(f"   - Polish Applied: {len(pipeline_result['polish']['fixes_applied'])} fixes")
    print(f"   - MCP Ready: {pipeline_result['mcp_ready']}")
    
    # Test 2: Figma Analysis
    print("\n2️⃣ Testing Figma Analysis")
    print("-" * 30)
    figma_url = "https://www.figma.com/file/abc123/bitcoin-wallet-design"
    figma_result = await analyze_figma_frame(figma_url)
    print(f"✅ Figma Analysis Complete")
    print(f"   - File ID: {figma_result['file_id']}")
    print(f"   - Frames Analyzed: {figma_result['frames_analyzed']}")
    print(f"   - Components: {figma_result['components_detected']}")
    print(f"   - Issues Found: {len(figma_result['layout_issues'])}")
    print(f"   - Accessibility Score: {figma_result['accessibility_score']}")
    
    # Test 3: Image Analysis
    print("\n3️⃣ Testing Image Analysis")
    print("-" * 30)
    # Create a mock image path for testing
    mock_image_path = "/Users/soheil/Desktop/bitcoin_case_page.png"
    image_result = await analyze_uploaded_image(mock_image_path)
    print(f"✅ Image Analysis Complete")
    if 'error' in image_result:
        print(f"   - Error: {image_result['error']}")
    else:
        print(f"   - Dimensions: {image_result['dimensions']}")
        print(f"   - Visual Hierarchy: {image_result['design_analysis']['visual_hierarchy']}")
        print(f"   - Clarity Score: {image_result['heuristic_scores']['clarity']}")
        print(f"   - Apple Alignment: {image_result['industry_comparison']['apple_alignment']}")
        print(f"   - Recommendations: {len(image_result['recommendations'])}")
    
    # Test 4: Motion Analysis
    print("\n4️⃣ Testing Motion Analysis")
    print("-" * 30)
    # Create a mock motion file path for testing
    mock_motion_path = "/Users/soheil/Desktop/loading_animation.gif"
    motion_result = await analyze_motion_design(mock_motion_path)
    print(f"✅ Motion Analysis Complete")
    if 'error' in motion_result:
        print(f"   - Error: {motion_result['error']}")
    else:
        print(f"   - Format: {motion_result['format']}")
        print(f"   - Duration: {motion_result['duration']}")
        print(f"   - Frame Count: {motion_result['frame_count']}")
        print(f"   - Easing: {motion_result['motion_analysis']['easing_curves']}")
        print(f"   - Performance Score: {motion_result['performance_metrics']['optimization_score']}")
        print(f"   - Recommendations: {len(motion_result['recommendations'])}")
    
    print("\n🎉 All Design Intelligence Tests Complete!")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(test_design_intelligence()) 