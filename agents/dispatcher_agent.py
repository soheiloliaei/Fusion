#!/usr/bin/env python3
"""
Dispatcher Agent - Fusion v14
Parses prompt type and selects optimal agent(s) with fallback support
"""

import asyncio
import time
import logging
import json
import os
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime

class DispatcherAgent:
    """
    Dispatcher Agent - Fusion v14
    Parses prompt type and selects optimal agent(s) with fallback support
    """
    
    def __init__(self):
        self.logger = logging.getLogger("DispatcherAgent")
        self.scorecard_file = "memory/agent_scorecard.json"
        
        # Initialize scorecard if it doesn't exist
        self._ensure_scorecard_file()
        
        # Agent routing heuristics
        self.routing_heuristics = {
            "design": {
                "keywords": ["design", "ui", "ux", "interface", "layout", "visual", "user experience"],
                "primary_agents": ["principal_designer", "vp_of_design"],
                "fallback_agents": ["design_technologist", "evaluator"],
                "confidence_threshold": 0.7
            },
            "strategy": {
                "keywords": ["strategy", "roadmap", "planning", "business", "market", "executive"],
                "primary_agents": ["strategy_pilot", "vp_of_product"],
                "fallback_agents": ["market_analyst", "evaluator"],
                "confidence_threshold": 0.7
            },
            "technical": {
                "keywords": ["code", "implementation", "technical", "development", "component", "system"],
                "primary_agents": ["design_technologist", "component_librarian"],
                "fallback_agents": ["product_navigator", "evaluator"],
                "confidence_threshold": 0.7
            },
            "content": {
                "keywords": ["content", "copy", "text", "narrative", "story", "communication"],
                "primary_agents": ["content_designer", "deck_narrator"],
                "fallback_agents": ["feedback_amplifier", "evaluator"],
                "confidence_threshold": 0.7
            },
            "analysis": {
                "keywords": ["analyze", "evaluate", "assess", "review", "examine", "study"],
                "primary_agents": ["evaluator", "market_analyst"],
                "fallback_agents": ["strategy_archivist", "research_summarizer"],
                "confidence_threshold": 0.7
            },
            "creative": {
                "keywords": ["creative", "innovative", "artistic", "cinematic", "visual", "design"],
                "primary_agents": ["creative_director", "principal_designer"],
                "fallback_agents": ["vp_of_design", "evaluator"],
                "confidence_threshold": 0.7
            }
        }
    
    def _ensure_scorecard_file(self):
        """Ensure agent scorecard file exists"""
        os.makedirs("memory", exist_ok=True)
        
        if not os.path.exists(self.scorecard_file):
            with open(self.scorecard_file, 'w') as f:
                json.dump({
                    "agents": {
                        "vp_design": {"success_rate": 0.85, "avg_confidence": 0.88, "specialties": ["design", "evaluation"]},
                        "evaluator": {"success_rate": 0.90, "avg_confidence": 0.92, "specialties": ["analysis", "quality"]},
                        "creative_director": {"success_rate": 0.82, "avg_confidence": 0.85, "specialties": ["creative", "strategy"]},
                        "design_technologist": {"success_rate": 0.88, "avg_confidence": 0.90, "specialties": ["technical", "implementation"]},
                        "product_navigator": {"success_rate": 0.87, "avg_confidence": 0.89, "specialties": ["product", "strategy"]},
                        "strategy_pilot": {"success_rate": 0.89, "avg_confidence": 0.91, "specialties": ["strategy", "planning"]},
                        "vp_of_design": {"success_rate": 0.86, "avg_confidence": 0.88, "specialties": ["design", "executive"]},
                        "vp_of_product": {"success_rate": 0.88, "avg_confidence": 0.90, "specialties": ["product", "executive"]},
                        "principal_designer": {"success_rate": 0.84, "avg_confidence": 0.87, "specialties": ["design", "collaboration"]},
                        "component_librarian": {"success_rate": 0.86, "avg_confidence": 0.89, "specialties": ["technical", "components"]},
                        "content_designer": {"success_rate": 0.83, "avg_confidence": 0.86, "specialties": ["content", "copy"]},
                        "ai_interaction_designer": {"success_rate": 0.85, "avg_confidence": 0.88, "specialties": ["ai", "interaction"]},
                        "strategy_archivist": {"success_rate": 0.81, "avg_confidence": 0.84, "specialties": ["knowledge", "documentation"]},
                        "market_analyst": {"success_rate": 0.87, "avg_confidence": 0.89, "specialties": ["market", "analysis"]},
                        "workflow_optimizer": {"success_rate": 0.83, "avg_confidence": 0.86, "specialties": ["process", "optimization"]},
                        "product_historian": {"success_rate": 0.82, "avg_confidence": 0.85, "specialties": ["history", "context"]},
                        "deck_narrator": {"success_rate": 0.84, "avg_confidence": 0.87, "specialties": ["narrative", "presentation"]},
                        "portfolio_editor": {"success_rate": 0.85, "avg_confidence": 0.88, "specialties": ["curation", "presentation"]},
                        "research_summarizer": {"success_rate": 0.86, "avg_confidence": 0.89, "specialties": ["research", "synthesis"]},
                        "feedback_amplifier": {"success_rate": 0.84, "avg_confidence": 0.87, "specialties": ["feedback", "improvement"]}
                    },
                    "metadata": {
                        "last_updated": datetime.now().isoformat(),
                        "version": "1.0"
                    }
                }, f)
    
    async def _read_scorecard(self) -> Dict[str, Any]:
        """Read agent scorecard from JSON file"""
        try:
            with open(self.scorecard_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Error reading scorecard: {e}")
            return {"agents": {}, "metadata": {}}
    
    async def _analyze_prompt_type(self, prompt: str) -> Tuple[str, float, List[str]]:
        """Analyze prompt and return type, confidence, and suggested agents"""
        prompt_lower = prompt.lower()
        
        best_type = "general"
        best_confidence = 0.0
        suggested_agents = []
        
        for prompt_type, heuristic in self.routing_heuristics.items():
            keywords = heuristic.get("keywords", [])
            confidence = 0.0
            
            # Calculate confidence based on keyword matches
            for keyword in keywords:
                if keyword in prompt_lower:
                    confidence += 0.15
            
            if confidence > best_confidence:
                best_confidence = confidence
                best_type = prompt_type
                suggested_agents = heuristic.get("primary_agents", [])
        
        return best_type, min(best_confidence, 1.0), suggested_agents
    
    async def _get_agent_scores(self, agent_names: List[str]) -> Dict[str, float]:
        """Get performance scores for agents"""
        scorecard = await self._read_scorecard()
        agent_scores = {}
        
        for agent_name in agent_names:
            agent_data = scorecard.get("agents", {}).get(agent_name, {})
            # Calculate composite score
            success_rate = agent_data.get("success_rate", 0.8)
            avg_confidence = agent_data.get("avg_confidence", 0.8)
            composite_score = (success_rate + avg_confidence) / 2
            agent_scores[agent_name] = composite_score
        
        return agent_scores
    
    async def _select_optimal_agents(self, prompt_type: str, confidence: float, 
                                   suggested_agents: List[str]) -> Tuple[List[str], List[str]]:
        """Select optimal agents based on prompt type and confidence"""
        
        if confidence < 0.5:
            # Low confidence - use general agents
            primary_agents = ["evaluator", "vp_design"]
            fallback_agents = ["creative_director", "product_navigator"]
        else:
            # Get agent scores for suggested agents
            agent_scores = await self._get_agent_scores(suggested_agents)
            
            # Sort by score and select top performers
            sorted_agents = sorted(agent_scores.items(), key=lambda x: x[1], reverse=True)
            primary_agents = [agent for agent, score in sorted_agents[:2]]
            
            # Get fallback agents from heuristic
            heuristic = self.routing_heuristics.get(prompt_type, {})
            fallback_agents = heuristic.get("fallback_agents", ["evaluator"])
        
        return primary_agents, fallback_agents
    
    async def _should_trigger_fallback(self, confidence: float, prompt_type: str) -> bool:
        """Determine if fallback should be triggered"""
        heuristic = self.routing_heuristics.get(prompt_type, {})
        threshold = heuristic.get("confidence_threshold", 0.7)
        return confidence < threshold
    
    async def run_async(self, prompt: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main async execution method for Dispatcher Agent
        """
        start_time = time.time()
        self.logger.info("Dispatcher Agent starting analysis")
        
        try:
            # Analyze prompt type
            prompt_type, confidence, suggested_agents = await self._analyze_prompt_type(prompt)
            
            # Select optimal agents
            primary_agents, fallback_agents = await self._select_optimal_agents(
                prompt_type, confidence, suggested_agents
            )
            
            # Determine if fallback is needed
            fallback_needed = await self._should_trigger_fallback(confidence, prompt_type)
            
            # Get agent scores for all selected agents
            all_agents = primary_agents + fallback_agents
            agent_scores = await self._get_agent_scores(all_agents)
            
            # Create enhanced output
            enhanced_output = f"""# Dispatcher Agent Response

## Original Request
{prompt}

## Prompt Analysis
**Prompt Type:** {prompt_type}
**Confidence:** {confidence:.2f}/1.00
**Suggested Agents:** {', '.join(suggested_agents) if suggested_agents else 'None'}

## Agent Selection
**Primary Agents:** {', '.join(primary_agents)}
**Fallback Agents:** {', '.join(fallback_agents)}
**Fallback Triggered:** {'Yes' if fallback_needed else 'No'}

## Agent Performance Scores
{chr(10).join([f"- **{agent}:** {score:.3f}" for agent, score in agent_scores.items()])}

## Routing Decision
**Decision:** {'Use primary agents with fallback' if fallback_needed else 'Use primary agents only'}
**Reasoning:** {'Low confidence requires fallback support' if fallback_needed else 'High confidence allows direct routing'}

## Recommendations
- **Primary Route:** {' → '.join(primary_agents)}
- **Fallback Route:** {' → '.join(fallback_agents) if fallback_needed else 'Not needed'}
- **Expected Performance:** {'High' if confidence >= 0.8 else 'Medium' if confidence >= 0.6 else 'Low'}

## Dispatcher Confidence
**Score:** {confidence:.2f}/1.00

*Generated by Fusion v14 Dispatcher Agent*"""
            
            execution_time = time.time() - start_time
            
            self.logger.info(f"Dispatcher Agent completed in {execution_time:.2f}s")
            
            return {
                "output": enhanced_output,
                "enhanced_output": enhanced_output,
                "confidence": confidence,
                "execution_time": execution_time,
                "shared_state": {
                    "prompt_type": prompt_type,
                    "primary_agents": primary_agents,
                    "fallback_agents": fallback_agents,
                    "fallback_needed": fallback_needed,
                    "agent_scores": agent_scores,
                    "analysis_timestamp": datetime.now().timestamp()
                }
            }
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.error(f"Dispatcher Agent failed: {e}")
            return {
                "error": str(e),
                "confidence": 0.0,
                "execution_time": execution_time
            } 