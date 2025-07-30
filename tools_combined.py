#!/usr/bin/env python3

# Import tools from the design intelligence module
from agents.design_designintelligence import (
    figma_parser_tool,
    image_parser_tool,
    motion_analysis_tool,
    run_design_pipeline,
    analyze_figma_frame,
    analyze_uploaded_image,
    analyze_motion_design
)

# Export all tools and functions
__all__ = [
    'figma_parser_tool',
    'image_parser_tool', 
    'motion_analysis_tool',
    'run_design_pipeline',
    'analyze_figma_frame',
    'analyze_uploaded_image',
    'analyze_motion_design'
]

# Tool registry for easy access
TOOL_REGISTRY = {
    "figma_parser": figma_parser_tool,
    "image_parser": image_parser_tool,
    "motion_analyzer": motion_analysis_tool,
    "design_pipeline": run_design_pipeline,
    "figma_analyzer": analyze_figma_frame,
    "image_analyzer": analyze_uploaded_image,
    "motion_analyzer": analyze_motion_design
}

def get_tool(tool_name: str):
    """Get a tool by name"""
    return TOOL_REGISTRY.get(tool_name) 