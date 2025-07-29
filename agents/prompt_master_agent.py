#!/usr/bin/env python3
"""
Prompt Master Agent - Fusion v14
Handles pattern matching, fallback chain logic, and prompt optimization
"""

import asyncio
import re
import json
import time
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime

class PromptMasterAgent:
    """
    Prompt Master Agent - Fusion v14
    Handles pattern matching, fallback chain logic, and prompt optimization
    """
    
    def __init__(self):
        self.logger = logging.getLogger("PromptMasterAgent")
        self.prompt_history = []
        
        # Safety patterns for prompt validation
        self.safety_patterns = [
            r"delete.*all",
            r"format.*disk", 
            r"sudo.*rm.*-rf",
            r"password.*\d{4,}",
            r"credit.*card.*\d{4}",
            r"ssn.*\d{3}-\d{2}-\d{4}",
            r"api.*key.*[a-zA-Z0-9]{20,}",
            r"secret.*[a-zA-Z0-9]{10,}"
        ]
        
        # Clarity indicators for prompt improvement
        self.clarity_indicators = [
            "unclear", "vague", "confusing", "ambiguous",
            "not specific", "too broad", "unclear goal",
            "something", "anything", "whatever"
        ]
        
        # Pattern matching for different prompt types
        self.prompt_patterns = {
            "design_request": {
                "patterns": [r"design.*", r"create.*design", r"build.*ui", r"make.*interface"],
                "fallback": "design_enhancement",
                "confidence": 0.9
            },
            "analysis_request": {
                "patterns": [r"analyze.*", r"evaluate.*", r"assess.*", r"review.*"],
                "fallback": "analysis_enhancement", 
                "confidence": 0.85
            },
            "creative_request": {
                "patterns": [r"creative.*", r"innovative.*", r"cinematic.*", r"artistic.*"],
                "fallback": "creative_enhancement",
                "confidence": 0.95
            },
            "technical_request": {
                "patterns": [r"technical.*", r"code.*", r"implementation.*", r"development.*"],
                "fallback": "technical_enhancement",
                "confidence": 0.8
            },
            "business_request": {
                "patterns": [r"business.*", r"strategy.*", r"executive.*", r"management.*"],
                "fallback": "business_enhancement",
                "confidence": 0.85
            }
        }
        
        # Fallback chain logic
        self.fallback_chains = {
            "design_enhancement": ["vp_design", "creative_director", "evaluator"],
            "analysis_enhancement": ["evaluator", "vp_design", "creative_director"],
            "creative_enhancement": ["creative_director", "vp_design", "evaluator"],
            "technical_enhancement": ["design_technologist", "vp_design", "evaluator"],
            "business_enhancement": ["strategy_pilot", "vp_design", "evaluator"]
        }
        
    async def run_async(self, prompt: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main async execution method for Prompt Master Agent
        """
        start_time = time.time()
        self.logger.info("Prompt Master Agent starting analysis")
        
        try:
            # Evaluate prompt for safety and clarity
            prompt_evaluation = await self._evaluate_prompt(prompt)
            
            # Identify prompt type and pattern
            pattern_analysis = await self._analyze_prompt_pattern(prompt)
            
            # Generate fallback chain
            fallback_chain = await self._generate_fallback_chain(prompt_evaluation, pattern_analysis)
            
            # Optimize prompt for better results
            optimized_prompt = await self._optimize_prompt(prompt, prompt_evaluation, pattern_analysis)
            
            # Create enhanced output
            enhanced_output = await self._create_enhanced_output(prompt, prompt_evaluation, pattern_analysis, fallback_chain, optimized_prompt)
            
            execution_time = time.time() - start_time
            confidence = self._calculate_confidence(prompt_evaluation, pattern_analysis)
            
            self.logger.info(f"Prompt Master Agent completed in {execution_time:.2f}s")
            
            return {
                "output": enhanced_output,
                "enhanced_output": enhanced_output,
                "confidence": confidence,
                "prompt_evaluation": prompt_evaluation,
                "pattern_analysis": pattern_analysis,
                "fallback_chain": fallback_chain,
                "optimized_prompt": optimized_prompt,
                "execution_time": execution_time,
                "shared_state": {
                    "prompt_type": pattern_analysis.get("detected_type"),
                    "safety_score": prompt_evaluation.get("safety_score"),
                    "clarity_score": prompt_evaluation.get("clarity_score"),
                    "fallback_chain": fallback_chain,
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
    
    async def _evaluate_prompt(self, prompt: str) -> Dict[str, Any]:
        """Evaluate prompt for safety and clarity"""
        
        # Safety check
        safety_issues = self._check_safety(prompt)
        safety_score = 1.0 if not safety_issues else 0.3
        
        # Clarity check
        clarity_issues = self._check_clarity(prompt)
        clarity_score = 1.0 if not clarity_issues else 0.7
        
        # Generate suggestions
        suggestions = self._generate_suggestions(prompt, safety_issues, clarity_issues)
        
        # Log prompt
        self._log_prompt(prompt, safety_score, clarity_score, safety_issues, clarity_issues)
        
        return {
            "original": prompt,
            "safety_score": safety_score,
            "clarity_score": clarity_score,
            "safety_issues": safety_issues,
            "clarity_issues": clarity_issues,
            "suggestions": suggestions,
            "overall_score": (safety_score + clarity_score) / 2
        }
    
    async def _analyze_prompt_pattern(self, prompt: str) -> Dict[str, Any]:
        """Analyze prompt for pattern matching"""
        
        prompt_lower = prompt.lower()
        detected_type = "general"
        confidence = 0.5
        matched_patterns = []
        
        # Check against known patterns
        for pattern_type, pattern_data in self.prompt_patterns.items():
            for pattern in pattern_data["patterns"]:
                if re.search(pattern, prompt_lower):
                    detected_type = pattern_type
                    confidence = pattern_data["confidence"]
                    matched_patterns.append(pattern)
                    break
            if detected_type != "general":
                break
        
        return {
            "detected_type": detected_type,
            "confidence": confidence,
            "matched_patterns": matched_patterns,
            "fallback_type": self.prompt_patterns.get(detected_type, {}).get("fallback", "general_enhancement")
        }
    
    async def _generate_fallback_chain(self, prompt_evaluation: Dict, pattern_analysis: Dict) -> List[str]:
        """Generate fallback chain based on prompt type and evaluation"""
        
        fallback_type = pattern_analysis.get("fallback_type", "general_enhancement")
        fallback_chain = self.fallback_chains.get(fallback_type, ["vp_design", "evaluator"])
        
        # Adjust chain based on safety and clarity scores
        if prompt_evaluation.get("safety_score", 1.0) < 0.5:
            # Add safety-focused agents
            fallback_chain = ["evaluator"] + fallback_chain
        
        if prompt_evaluation.get("clarity_score", 1.0) < 0.7:
            # Add clarity-focused agents
            fallback_chain = ["creative_director"] + fallback_chain
        
        return fallback_chain
    
    async def _optimize_prompt(self, prompt: str, prompt_evaluation: Dict, pattern_analysis: Dict) -> str:
        """Optimize prompt for better results"""
        
        optimized = prompt
        
        # Apply safety improvements
        if prompt_evaluation.get("safety_score", 1.0) < 1.0:
            optimized = self._sanitize_prompt(optimized)
        
        # Apply clarity improvements
        if prompt_evaluation.get("clarity_score", 1.0) < 1.0:
            optimized = self._improve_clarity(optimized)
        
        # Add context based on pattern type
        pattern_type = pattern_analysis.get("detected_type", "general")
        if pattern_type != "general":
            optimized = self._add_pattern_context(optimized, pattern_type)
        
        return optimized
    
    async def _create_enhanced_output(self, prompt: str, prompt_evaluation: Dict, pattern_analysis: Dict, fallback_chain: List[str], optimized_prompt: str) -> str:
        """Create enhanced output with analysis and recommendations"""
        
        return f"""# Prompt Master Analysis & Optimization

## Original Prompt
{prompt}

## Prompt Evaluation

### Safety Analysis
**Score:** {prompt_evaluation.get('safety_score', 0):.2f}/1.00
**Issues:** {', '.join(prompt_evaluation.get('safety_issues', ['None detected']))}

### Clarity Analysis  
**Score:** {prompt_evaluation.get('clarity_score', 0):.2f}/1.00
**Issues:** {', '.join(prompt_evaluation.get('clarity_issues', ['None detected']))}

## Pattern Analysis

### Detected Type
**Type:** {pattern_analysis.get('detected_type', 'general')}
**Confidence:** {pattern_analysis.get('confidence', 0):.2f}/1.00
**Matched Patterns:** {', '.join(pattern_analysis.get('matched_patterns', ['None']))}

## Fallback Chain
**Recommended Agent Sequence:** {' → '.join(fallback_chain)}

## Optimized Prompt
```
{optimized_prompt}
```

## Recommendations
{prompt_evaluation.get('suggestions', ['No specific recommendations needed'])}

## Prompt Master Confidence
**Score:** {self._calculate_confidence(prompt_evaluation, pattern_analysis):.2f}/1.00

*Generated by Fusion v14 Prompt Master Agent*"""
    
    def _check_safety(self, prompt: str) -> List[str]:
        """Check for potentially unsafe patterns"""
        issues = []
        prompt_lower = prompt.lower()
        
        for pattern in self.safety_patterns:
            if re.search(pattern, prompt_lower):
                issues.append(f"Potential safety issue detected: {pattern}")
        
        return issues
    
    def _check_clarity(self, prompt: str) -> List[str]:
        """Check for clarity issues"""
        issues = []
        prompt_lower = prompt.lower()
        
        # Check for vague language
        if len(prompt.split()) < 5:
            issues.append("Prompt is too short - consider adding more context")
        
        if any(indicator in prompt_lower for indicator in self.clarity_indicators):
            issues.append("Prompt contains unclear language")
        
        # Check for missing specificity
        if "something" in prompt_lower or "anything" in prompt_lower:
            issues.append("Prompt is too vague - be more specific")
        
        # Check for missing context
        if not any(word in prompt_lower for word in ["design", "create", "build", "analyze", "evaluate", "review"]):
            issues.append("Prompt lacks clear action verb")
        
        return issues
    
    def _generate_suggestions(self, prompt: str, safety_issues: List[str], clarity_issues: List[str]) -> List[str]:
        """Generate improvement suggestions"""
        suggestions = []
        
        if safety_issues:
            suggestions.append("• Review prompt for sensitive information")
            suggestions.append("• Consider using placeholder data for testing")
        
        if clarity_issues:
            suggestions.append("• Add specific requirements and constraints")
            suggestions.append("• Include target audience and context")
            suggestions.append("• Specify desired output format")
        
        if not safety_issues and not clarity_issues:
            suggestions.append("• Prompt is well-formed and ready for processing")
        
        return suggestions
    
    def _sanitize_prompt(self, prompt: str) -> str:
        """Sanitize potentially unsafe prompts"""
        sanitized = prompt
        for pattern in self.safety_patterns:
            sanitized = re.sub(pattern, "[REDACTED]", sanitized, flags=re.IGNORECASE)
        return sanitized
    
    def _improve_clarity(self, prompt: str) -> str:
        """Improve prompt clarity"""
        improved = prompt
        
        # Add context if too short
        if len(prompt.split()) < 5:
            improved = f"Please provide a detailed response to: {prompt}"
        
        # Replace vague terms
        improved = improved.replace("something", "specific requirements")
        improved = improved.replace("anything", "concrete examples")
        improved = improved.replace("whatever", "specific details")
        
        return improved
    
    def _add_pattern_context(self, prompt: str, pattern_type: str) -> str:
        """Add context based on pattern type"""
        context_map = {
            "design_request": "Focus on user experience and visual design principles. ",
            "analysis_request": "Provide detailed analysis with supporting evidence. ",
            "creative_request": "Emphasize creativity and innovative approaches. ",
            "technical_request": "Include technical specifications and implementation details. ",
            "business_request": "Consider business impact and strategic implications. "
        }
        
        context = context_map.get(pattern_type, "")
        return context + prompt
    
    def _log_prompt(self, prompt: str, safety_score: float, clarity_score: float, safety_issues: List[str], clarity_issues: List[str]):
        """Log prompt for analysis"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "safety_score": safety_score,
            "clarity_score": clarity_score,
            "safety_issues": safety_issues,
            "clarity_issues": clarity_issues,
            "overall_score": (safety_score + clarity_score) / 2
        }
        
        self.prompt_history.append(log_entry)
        
        # Keep only last 100 entries
        if len(self.prompt_history) > 100:
            self.prompt_history = self.prompt_history[-100:]
    
    def _calculate_confidence(self, prompt_evaluation: Dict, pattern_analysis: Dict) -> float:
        """Calculate confidence score"""
        base_confidence = 0.8
        
        # Boost for high safety and clarity scores
        safety_score = prompt_evaluation.get("safety_score", 1.0)
        clarity_score = prompt_evaluation.get("clarity_score", 1.0)
        
        if safety_score > 0.8 and clarity_score > 0.8:
            base_confidence += 0.1
        
        # Boost for clear pattern detection
        pattern_confidence = pattern_analysis.get("confidence", 0.5)
        if pattern_confidence > 0.8:
            base_confidence += 0.05
        
        return min(base_confidence, 0.95)
    
    def get_prompt_history(self, limit: int = 10) -> List[Dict]:
        """Get recent prompt history"""
        return self.prompt_history[-limit:]
    
    def clear_history(self):
        """Clear prompt history"""
        self.prompt_history = []
    
    def export_history(self, filename: str = "prompt_history.json"):
        """Export prompt history to file"""
        with open(filename, 'w') as f:
            json.dump(self.prompt_history, f, indent=2)
        return filename
