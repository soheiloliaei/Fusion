"""
Evaluator Agent - Fusion v14
Async evaluator with scoring and context logging
"""

import asyncio
import time
from typing import Dict, Any, List, Optional
import logging
import json
from memory.agent_memory import agent_memory

class EvaluatorAgent:
    """
    Evaluator Agent - Fusion v14
    Provides comprehensive evaluation and scoring of outputs
    """
    
    def __init__(self):
        self.logger = logging.getLogger("EvaluatorAgent")
        self.evaluation_criteria = {
            "clarity": {"weight": 0.15, "description": "How clear and understandable is the output?"},
            "completeness": {"weight": 0.15, "description": "How complete is the response to the request?"},
            "actionability": {"weight": 0.20, "description": "How actionable are the recommendations?"},
            "accuracy": {"weight": 0.15, "description": "How accurate is the information provided?"},
            "relevance": {"weight": 0.15, "description": "How relevant is the output to the input?"},
            "innovation": {"weight": 0.10, "description": "How innovative or creative is the approach?"},
            "product_value": {"weight": 0.10, "description": "How much business/product value does it provide?"}
        }
        
    async def run(self, input_prompt: str, tools: Dict[str, Any] = None) -> Dict[str, Any]:
        """Main async execution method"""
        return await self.run_async(input_prompt, tools)
        
    async def run_async(self, input_prompt: str, tools: Dict[str, Any] = None) -> Dict[str, Any]:
        """Async evaluation with comprehensive scoring"""
        
        start_time = time.time()
        
        try:
            self.logger.info("Evaluator Agent starting analysis")
            
            # Step 1: Extract context from input
            context = await self._extract_evaluation_context(input_prompt)
            
            # Step 2: Perform comprehensive evaluation
            evaluation_results = await self._perform_evaluation(input_prompt, context)
            
            # Step 3: Calculate overall score
            overall_score = self._calculate_overall_score(evaluation_results)
            
            # Step 4: Generate evaluation report
            evaluation_report = await self._generate_evaluation_report(
                input_prompt, evaluation_results, overall_score
            )
            
            execution_time = time.time() - start_time
            
            # Store in memory
            await agent_memory.store_agent_run(
                agent_name="evaluator",
                prompt=input_prompt,
                response=evaluation_report,
                confidence=overall_score,
                fallback_flag=False,
                additional_data={
                    "evaluation_results": evaluation_results,
                    "context": context
                }
            )
            
            result = {
                "output": evaluation_report,
                "enhanced_output": evaluation_report,
                "confidence": overall_score,
                "evaluation_results": evaluation_results,
                "overall_score": overall_score,
                "execution_time": execution_time,
                "shared_state": {
                    "evaluation_timestamp": time.time(),
                    "evaluation_criteria": self.evaluation_criteria
                }
            }
            
            self.logger.info(f"Evaluator Agent completed in {execution_time:.2f}s with score {overall_score:.2f}")
            return result
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.error(f"Evaluator Agent failed: {e}")
            
            return {
                "error": str(e),
                "confidence": 0.0,
                "execution_time": execution_time
            }
            
    async def _extract_evaluation_context(self, input_prompt: str) -> Dict[str, Any]:
        """Extract context for evaluation from the input prompt"""
        
        context = {
            "input_type": self._identify_input_type(input_prompt),
            "complexity_level": self._assess_complexity(input_prompt),
            "domain": self._identify_domain(input_prompt),
            "urgency": self._assess_urgency(input_prompt),
            "stakeholders": self._identify_stakeholders(input_prompt)
        }
        
        # Simulate async processing
        await asyncio.sleep(0.05)
        
        return context
        
    async def _perform_evaluation(self, input_prompt: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Perform comprehensive evaluation across all criteria"""
        
        evaluation_results = {}
        
        for criterion, config in self.evaluation_criteria.items():
            score = await self._evaluate_criterion(criterion, input_prompt, context)
            evaluation_results[criterion] = {
                "score": score,
                "weight": config["weight"],
                "description": config["description"],
                "reasoning": self._generate_reasoning(criterion, score, context)
            }
            
        return evaluation_results
        
    async def _evaluate_criterion(self, criterion: str, input_prompt: str, 
                                context: Dict[str, Any]) -> float:
        """Evaluate a specific criterion"""
        
        # Simulate async evaluation
        await asyncio.sleep(0.02)
        
        # Base scoring logic based on criterion
        if criterion == "clarity":
            return self._evaluate_clarity(input_prompt, context)
        elif criterion == "completeness":
            return self._evaluate_completeness(input_prompt, context)
        elif criterion == "actionability":
            return self._evaluate_actionability(input_prompt, context)
        elif criterion == "accuracy":
            return self._evaluate_accuracy(input_prompt, context)
        elif criterion == "relevance":
            return self._evaluate_relevance(input_prompt, context)
        elif criterion == "innovation":
            return self._evaluate_innovation(input_prompt, context)
        elif criterion == "product_value":
            return self._evaluate_product_value(input_prompt, context)
        else:
            return 0.7  # Default score
            
    def _evaluate_clarity(self, input_prompt: str, context: Dict[str, Any]) -> float:
        """Evaluate clarity of the input"""
        score = 0.7  # Base score
        
        # Adjust based on input characteristics
        if len(input_prompt.split()) > 50:
            score += 0.1  # Detailed input
        if any(word in input_prompt.lower() for word in ["clear", "specific", "detailed"]):
            score += 0.1
        if context.get("complexity_level") == "high":
            score -= 0.1  # Complex inputs may be less clear
            
        return min(score, 1.0)
        
    def _evaluate_completeness(self, input_prompt: str, context: Dict[str, Any]) -> float:
        """Evaluate completeness of the input"""
        score = 0.7  # Base score
        
        # Check for completeness indicators
        completeness_indicators = [
            "requirements", "specifications", "details", "context",
            "background", "goals", "objectives", "constraints"
        ]
        
        for indicator in completeness_indicators:
            if indicator in input_prompt.lower():
                score += 0.05
                
        return min(score, 1.0)
        
    def _evaluate_actionability(self, input_prompt: str, context: Dict[str, Any]) -> float:
        """Evaluate actionability of the input"""
        score = 0.7  # Base score
        
        # Check for actionable elements
        actionable_indicators = [
            "implement", "create", "build", "design", "develop",
            "improve", "optimize", "enhance", "solve", "fix"
        ]
        
        for indicator in actionable_indicators:
            if indicator in input_prompt.lower():
                score += 0.05
                
        return min(score, 1.0)
        
    def _evaluate_accuracy(self, input_prompt: str, context: Dict[str, Any]) -> float:
        """Evaluate accuracy potential of the input"""
        score = 0.7  # Base score
        
        # Check for accuracy indicators
        accuracy_indicators = [
            "data", "metrics", "measurements", "standards", "guidelines",
            "best practices", "research", "analysis"
        ]
        
        for indicator in accuracy_indicators:
            if indicator in input_prompt.lower():
                score += 0.05
                
        return min(score, 1.0)
        
    def _evaluate_relevance(self, input_prompt: str, context: Dict[str, Any]) -> float:
        """Evaluate relevance of the input"""
        score = 0.8  # Base score (most inputs are relevant)
        
        # Check for relevance indicators
        if context.get("domain") in ["design", "ux", "ui", "product"]:
            score += 0.1  # Domain-specific relevance
            
        return min(score, 1.0)
        
    def _evaluate_innovation(self, input_prompt: str, context: Dict[str, Any]) -> float:
        """Evaluate innovation potential"""
        score = 0.6  # Base score
        
        # Check for innovation indicators
        innovation_indicators = [
            "innovative", "creative", "novel", "unique", "breakthrough",
            "revolutionary", "cutting-edge", "next-generation"
        ]
        
        for indicator in innovation_indicators:
            if indicator in input_prompt.lower():
                score += 0.1
                
        return min(score, 1.0)
        
    def _evaluate_product_value(self, input_prompt: str, context: Dict[str, Any]) -> float:
        """Evaluate product/business value"""
        score = 0.7  # Base score
        
        # Check for business value indicators
        value_indicators = [
            "business", "product", "market", "customer", "user",
            "revenue", "growth", "impact", "value", "ROI"
        ]
        
        for indicator in value_indicators:
            if indicator in input_prompt.lower():
                score += 0.05
                
        return min(score, 1.0)
        
    def _calculate_overall_score(self, evaluation_results: Dict[str, Any]) -> float:
        """Calculate weighted overall score"""
        
        total_score = 0.0
        total_weight = 0.0
        
        for criterion, result in evaluation_results.items():
            score = result["score"]
            weight = result["weight"]
            
            total_score += score * weight
            total_weight += weight
            
        if total_weight > 0:
            return total_score / total_weight
        else:
            return 0.0
            
    async def _generate_evaluation_report(self, input_prompt: str, 
                                       evaluation_results: Dict[str, Any],
                                       overall_score: float) -> str:
        """Generate comprehensive evaluation report"""
        
        report = f"# Fusion v14 Evaluation Report\n\n"
        report += f"## Input Analysis\n"
        report += f"**Input:** {input_prompt[:100]}{'...' if len(input_prompt) > 100 else ''}\n\n"
        
        report += f"## Overall Score: {overall_score:.2f}/1.00\n\n"
        
        report += f"## Detailed Evaluation\n\n"
        
        for criterion, result in evaluation_results.items():
            report += f"### {criterion.title()}\n"
            report += f"**Score:** {result['score']:.2f}/1.00\n"
            report += f"**Weight:** {result['weight']:.2f}\n"
            report += f"**Description:** {result['description']}\n"
            report += f"**Reasoning:** {result['reasoning']}\n\n"
            
        report += f"## Recommendations\n\n"
        
        # Generate recommendations based on low scores
        low_scores = [(criterion, result) for criterion, result in evaluation_results.items() 
                     if result['score'] < 0.7]
        
        if low_scores:
            report += f"**Areas for Improvement:**\n"
            for criterion, result in low_scores:
                report += f"- **{criterion.title()}:** {self._get_improvement_suggestion(criterion)}\n"
        else:
            report += f"✅ All criteria meet quality standards\n"
            
        report += f"\n## Quality Assessment\n\n"
        
        if overall_score >= 0.9:
            report += f"🟢 **Excellent Quality** - Ready for production use\n"
        elif overall_score >= 0.8:
            report += f"🟡 **Good Quality** - Minor improvements recommended\n"
        elif overall_score >= 0.7:
            report += f"🟠 **Acceptable Quality** - Some improvements needed\n"
        else:
            report += f"🔴 **Needs Improvement** - Significant enhancements required\n"
            
        return report
        
    def _generate_reasoning(self, criterion: str, score: float, context: Dict[str, Any]) -> str:
        """Generate reasoning for a criterion score"""
        
        reasoning_templates = {
            "clarity": {
                "high": "Input provides clear, well-structured information",
                "medium": "Input is generally clear but could benefit from more detail",
                "low": "Input lacks clarity and needs better structure"
            },
            "completeness": {
                "high": "Input covers all necessary aspects comprehensively",
                "medium": "Input covers most aspects but may miss some details",
                "low": "Input is incomplete and needs additional information"
            },
            "actionability": {
                "high": "Input provides clear, actionable guidance",
                "medium": "Input provides some actionable elements",
                "low": "Input lacks actionable components"
            },
            "accuracy": {
                "high": "Input appears accurate and well-researched",
                "medium": "Input shows reasonable accuracy",
                "low": "Input may contain inaccuracies or needs verification"
            },
            "relevance": {
                "high": "Input is highly relevant to the domain",
                "medium": "Input is generally relevant",
                "low": "Input may not be fully relevant to the context"
            },
            "innovation": {
                "high": "Input demonstrates innovative thinking",
                "medium": "Input shows some creative elements",
                "low": "Input lacks innovative approaches"
            },
            "product_value": {
                "high": "Input has strong business/product value",
                "medium": "Input has moderate business value",
                "low": "Input may lack clear business value"
            }
        }
        
        if score >= 0.8:
            level = "high"
        elif score >= 0.6:
            level = "medium"
        else:
            level = "low"
            
        return reasoning_templates.get(criterion, {}).get(level, "Score based on evaluation criteria")
        
    def _get_improvement_suggestion(self, criterion: str) -> str:
        """Get improvement suggestion for a criterion"""
        
        suggestions = {
            "clarity": "Provide more specific details and structure the information better",
            "completeness": "Include additional context, requirements, and specifications",
            "actionability": "Add specific steps, recommendations, or implementation guidance",
            "accuracy": "Include data, research, or references to support claims",
            "relevance": "Focus more on the specific domain and context",
            "innovation": "Consider more creative or novel approaches",
            "product_value": "Emphasize business impact and measurable outcomes"
        }
        
        return suggestions.get(criterion, "Consider improving this aspect")
        
    def _identify_input_type(self, input_prompt: str) -> str:
        """Identify the type of input"""
        prompt_lower = input_prompt.lower()
        
        if any(word in prompt_lower for word in ["design", "ui", "ux", "interface"]):
            return "design_request"
        elif any(word in prompt_lower for word in ["evaluate", "assess", "review"]):
            return "evaluation_request"
        elif any(word in prompt_lower for word in ["create", "build", "develop"]):
            return "creation_request"
        else:
            return "general_request"
            
    def _assess_complexity(self, input_prompt: str) -> str:
        """Assess the complexity of the input"""
        word_count = len(input_prompt.split())
        
        if word_count > 100:
            return "high"
        elif word_count > 50:
            return "medium"
        else:
            return "low"
            
    def _identify_domain(self, input_prompt: str) -> str:
        """Identify the domain of the input"""
        prompt_lower = input_prompt.lower()
        
        domains = {
            "design": ["design", "ui", "ux", "interface", "visual"],
            "development": ["code", "programming", "development", "technical"],
            "business": ["business", "strategy", "marketing", "product"],
            "analysis": ["analysis", "research", "data", "metrics"]
        }
        
        for domain, keywords in domains.items():
            if any(keyword in prompt_lower for keyword in keywords):
                return domain
                
        return "general"
        
    def _assess_urgency(self, input_prompt: str) -> str:
        """Assess the urgency of the input"""
        prompt_lower = input_prompt.lower()
        
        urgency_indicators = ["urgent", "asap", "immediate", "quick", "fast", "deadline"]
        
        if any(indicator in prompt_lower for indicator in urgency_indicators):
            return "high"
        else:
            return "normal"
            
    def _identify_stakeholders(self, input_prompt: str) -> List[str]:
        """Identify stakeholders mentioned in the input"""
        stakeholders = []
        prompt_lower = input_prompt.lower()
        
        stakeholder_keywords = {
            "users": ["user", "customer", "end-user"],
            "developers": ["developer", "engineer", "programmer"],
            "designers": ["designer", "ux", "ui"],
            "managers": ["manager", "stakeholder", "client"],
            "business": ["business", "product", "marketing"]
        }
        
        for stakeholder, keywords in stakeholder_keywords.items():
            if any(keyword in prompt_lower for keyword in keywords):
                stakeholders.append(stakeholder)
                
        return stakeholders
