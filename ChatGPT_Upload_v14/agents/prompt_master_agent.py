#!/usr/bin/env python3
"""
Prompt Master Agent - Fusion v14
Handles pattern matching, stylistic adherence, fallback suggestion with memory-aware learning
"""

import asyncio
import time
import logging
import json
import os
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime

class PromptMasterAgent:
    """
    Prompt Master Agent - Fusion v14
    Handles pattern matching, stylistic adherence, fallback suggestion with memory-aware learning
    """
    
    def __init__(self):
        self.logger = logging.getLogger("PromptMasterAgent")
        self.memory_file = "memory/agent_memory.json"
        self.pattern_file = "memory/pattern_registry.json"
        
        # Initialize memory and pattern files if they don't exist
        self._ensure_memory_files()
        
    def _ensure_memory_files(self):
        """Ensure memory and pattern files exist"""
        os.makedirs("memory", exist_ok=True)
        
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, 'w') as f:
                json.dump({"prompt_master": []}, f)
                
        if not os.path.exists(self.pattern_file):
            with open(self.pattern_file, 'w') as f:
                json.dump({
                    "patterns": {
                        "design_focused": {
                            "keywords": ["design", "ui", "ux", "interface", "layout", "visual"],
                            "suggested_agents": ["principal_designer", "vp_of_design", "design_technologist"],
                            "confidence_threshold": 0.8
                        },
                        "strategy_focused": {
                            "keywords": ["strategy", "roadmap", "planning", "business", "market"],
                            "suggested_agents": ["strategy_pilot", "vp_of_product", "market_analyst"],
                            "confidence_threshold": 0.8
                        },
                        "technical_focused": {
                            "keywords": ["code", "implementation", "technical", "development", "component"],
                            "suggested_agents": ["design_technologist", "component_librarian", "product_navigator"],
                            "confidence_threshold": 0.8
                        },
                        "content_focused": {
                            "keywords": ["content", "copy", "text", "narrative", "story"],
                            "suggested_agents": ["content_designer", "deck_narrator", "feedback_amplifier"],
                            "confidence_threshold": 0.8
                        }
                    }
                }, f)
    
    async def _read_memory(self) -> Dict[str, Any]:
        """Read agent memory from JSON file"""
        try:
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Error reading memory: {e}")
            return {"prompt_master": []}
    
    async def _write_memory(self, memory_data: Dict[str, Any]):
        """Write agent memory to JSON file"""
        try:
            with open(self.memory_file, 'w') as f:
                json.dump(memory_data, f, indent=2)
        except Exception as e:
            self.logger.error(f"Error writing memory: {e}")
    
    async def _read_patterns(self) -> Dict[str, Any]:
        """Read pattern registry from JSON file"""
        try:
            with open(self.pattern_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Error reading patterns: {e}")
            return {"patterns": {}}
    
    async def _analyze_prompt_pattern(self, prompt: str) -> Tuple[str, float, List[str]]:
        """Analyze prompt and return pattern type, confidence, and suggested agents"""
        patterns = await self._read_patterns()
        prompt_lower = prompt.lower()
        
        best_pattern = "general"
        best_confidence = 0.0
        suggested_agents = []
        
        for pattern_name, pattern_data in patterns.get("patterns", {}).items():
            keywords = pattern_data.get("keywords", [])
            confidence = 0.0
            
            # Calculate confidence based on keyword matches
            for keyword in keywords:
                if keyword in prompt_lower:
                    confidence += 0.2
            
            if confidence > best_confidence:
                best_confidence = confidence
                best_pattern = pattern_name
                suggested_agents = pattern_data.get("suggested_agents", [])
        
        return best_pattern, min(best_confidence, 1.0), suggested_agents
    
    async def _get_memory_insights(self, prompt: str) -> Dict[str, Any]:
        """Get insights from past prompt-response pairs"""
        memory = await self._read_memory()
        prompt_memory = memory.get("prompt_master", [])
        
        insights = {
            "similar_prompts": [],
            "successful_patterns": [],
            "fallback_triggers": []
        }
        
        prompt_lower = prompt.lower()
        
        for entry in prompt_memory[-10:]:  # Check last 10 entries
            if entry.get("prompt"):
                entry_lower = entry["prompt"].lower()
                
                # Check for similar prompts
                if any(word in entry_lower for word in prompt_lower.split()[:3]):
                    insights["similar_prompts"].append(entry)
                
                # Check for successful patterns
                if entry.get("confidence", 0) > 0.8:
                    insights["successful_patterns"].append(entry)
                
                # Check for fallback triggers
                if entry.get("fallback_flag", False):
                    insights["fallback_triggers"].append(entry)
        
        return insights
    
    async def _rewrite_prompt(self, prompt: str, pattern: str, insights: Dict[str, Any]) -> str:
        """Rewrite prompt based on pattern and memory insights"""
        rewritten = prompt
        
        # Apply pattern-specific enhancements
        if pattern == "design_focused":
            if "design" not in prompt.lower():
                rewritten = f"Design-focused: {prompt}"
        elif pattern == "strategy_focused":
            if "strategy" not in prompt.lower():
                rewritten = f"Strategic planning: {prompt}"
        elif pattern == "technical_focused":
            if "technical" not in prompt.lower():
                rewritten = f"Technical implementation: {prompt}"
        elif pattern == "content_focused":
            if "content" not in prompt.lower():
                rewritten = f"Content and copy: {prompt}"
        
        # Apply memory insights
        if insights["successful_patterns"]:
            best_pattern = max(insights["successful_patterns"], 
                             key=lambda x: x.get("confidence", 0))
            if best_pattern.get("prompt"):
                # Add successful elements from past prompts
                rewritten = f"{rewritten} (incorporating successful patterns from similar requests)"
        
        return rewritten
    
    async def run_async(self, prompt: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main async execution method for Prompt Master Agent
        """
        start_time = time.time()
        self.logger.info("Prompt Master Agent starting analysis")
        
        try:
            # Analyze prompt pattern
            pattern, confidence, suggested_agents = await self._analyze_prompt_pattern(prompt)
            
            # Get memory insights
            insights = await self._get_memory_insights(prompt)
            
            # Rewrite prompt based on pattern and insights
            rewritten_prompt = await self._rewrite_prompt(prompt, pattern, insights)
            
            # Determine if fallback is needed
            fallback_needed = confidence < 0.7
            fallback_agents = suggested_agents if fallback_needed else []
            
            # Create enhanced output
            enhanced_output = f"""# Prompt Master Agent Response

## Original Request
{prompt}

## Pattern Analysis
**Pattern Type:** {pattern}
**Confidence:** {confidence:.2f}/1.00
**Suggested Agents:** {', '.join(suggested_agents) if suggested_agents else 'None'}

## Memory Insights
**Similar Prompts Found:** {len(insights['similar_prompts'])}
**Successful Patterns:** {len(insights['successful_patterns'])}
**Fallback Triggers:** {len(insights['fallback_triggers'])}

## Rewritten Prompt
{rewritten_prompt}

## Fallback Analysis
**Fallback Needed:** {'Yes' if fallback_needed else 'No'}
**Fallback Agents:** {', '.join(fallback_agents) if fallback_agents else 'None'}

## Recommendations
- **Primary Pattern:** {pattern}
- **Confidence Level:** {'High' if confidence >= 0.8 else 'Medium' if confidence >= 0.6 else 'Low'}
- **Suggested Approach:** {'Use suggested agents' if suggested_agents else 'General processing'}

## Prompt Master Confidence
**Score:** {confidence:.2f}/1.00

*Generated by Fusion v14 Prompt Master Agent*"""
            
            execution_time = time.time() - start_time
            
            # Store in memory
            memory_data = await self._read_memory()
            memory_entry = {
                "agent_name": "prompt_master",
                "prompt": prompt,
                "response": enhanced_output,
                "confidence": confidence,
                "fallback_flag": fallback_needed,
                "pattern": pattern,
                "suggested_agents": suggested_agents,
                "timestamp": datetime.now().isoformat()
            }
            
            memory_data["prompt_master"] = memory_data.get("prompt_master", []) + [memory_entry]
            # Keep only last 20 entries
            memory_data["prompt_master"] = memory_data["prompt_master"][-20:]
            await self._write_memory(memory_data)
            
            self.logger.info(f"Prompt Master Agent completed in {execution_time:.2f}s")
            
            return {
                "output": enhanced_output,
                "enhanced_output": enhanced_output,
                "confidence": confidence,
                "execution_time": execution_time,
                "shared_state": {
                    "pattern_type": pattern,
                    "suggested_agents": suggested_agents,
                    "fallback_needed": fallback_needed,
                    "rewritten_prompt": rewritten_prompt,
                    "memory_insights": insights,
                    "analysis_timestamp": datetime.now().timestamp()
                }
            }
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.error(f"Prompt Master Agent failed: {e}")
            return {
                "error": str(e),
                "confidence": 0.0,
                "execution_time": execution_time
            }
