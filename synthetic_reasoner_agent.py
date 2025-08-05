#!/usr/bin/env python3
"""
Synthetic Reasoner Agent - Fusion v14.5
Provides synthetic reasoning, risk assessment, and fallback routing
"""

import json
import random
from typing import Dict, List, Any

class SyntheticReasonerAgent:
    """
    Synthetic Reasoner Agent for Fusion v14.5
    Provides synthetic reasoning, risk assessment, and fallback routing
    """
    
    def __init__(self):
        self.risk_patterns = {
            "ambiguous_terms": 0.3,
            "complex_requirements": 0.4,
            "technical_depth": 0.25,
            "executive_sensitivity": 0.35,
            "design_criticism": 0.45,
            "accessibility_concerns": 0.3,
            "innovation_risk": 0.4,
            "user_experience": 0.25
        }
        
        self.synthetic_thought_templates = [
            "Analyzing the input for potential ambiguity and clarity issues...",
            "Considering the technical complexity and implementation feasibility...",
            "Evaluating the executive sensitivity and business impact...",
            "Assessing design criticism potential and user experience implications...",
            "Examining accessibility and inclusivity considerations...",
            "Reviewing innovation risk and market positioning...",
            "Analyzing user experience flow and interaction patterns...",
            "Considering stakeholder alignment and communication needs..."
        ]
        
        self.synthetic_query_templates = [
            "What are the ambiguous terms that need clarification?",
            "How complex are the technical requirements?",
            "What is the executive sensitivity level?",
            "Are there potential design criticism points?",
            "What accessibility considerations are involved?",
            "What innovation risks should be considered?",
            "How does this impact user experience?",
            "What stakeholder concerns might arise?"
        ]
    
    def run(self, user_input: str, agent_name: str) -> Dict[str, Any]:
        """
        Run synthetic reasoning on user input
        Returns synthetic thoughts, queries, and risk assessment
        """
        print(f"🧠 SyntheticReasonerAgent: Analyzing input for {agent_name}")
        
        # Generate synthetic thoughts
        synthetic_thoughts = self._generate_synthetic_thoughts(user_input, agent_name)
        
        # Generate synthetic queries
        synthetic_queries = self._generate_synthetic_queries(user_input, agent_name)
        
        # Calculate risk score
        risk_score = self._calculate_risk_score(user_input, agent_name)
        
        return {
            "synthetic_thoughts": synthetic_thoughts,
            "synthetic_queries": synthetic_queries,
            "risk_score": risk_score,
            "agent_name": agent_name,
            "input_length": len(user_input)
        }
    
    def _generate_synthetic_thoughts(self, user_input: str, agent_name: str) -> List[str]:
        """Generate synthetic thoughts based on input and agent"""
        thoughts = []
        
        # Select 5 relevant thoughts based on input content
        selected_templates = random.sample(self.synthetic_thought_templates, 5)
        
        for template in selected_templates:
            # Customize based on agent type
            if "design" in agent_name.lower():
                thought = f"Design-focused: {template}"
            elif "evaluator" in agent_name.lower():
                thought = f"Evaluation-focused: {template}"
            elif "creative" in agent_name.lower():
                thought = f"Creative-focused: {template}"
            else:
                thought = f"General: {template}"
            
            thoughts.append(thought)
        
        return thoughts
    
    def _generate_synthetic_queries(self, user_input: str, agent_name: str) -> List[str]:
        """Generate synthetic queries based on input and agent"""
        queries = []
        
        # Select 5 relevant queries based on input content
        selected_templates = random.sample(self.synthetic_query_templates, 5)
        
        for template in selected_templates:
            # Customize based on agent type
            if "design" in agent_name.lower():
                query = f"Design Analysis: {template}"
            elif "evaluator" in agent_name.lower():
                query = f"Evaluation Criteria: {template}"
            elif "creative" in agent_name.lower():
                query = f"Creative Direction: {template}"
            else:
                query = f"General Analysis: {template}"
            
            queries.append(query)
        
        return queries
    
    def _calculate_risk_score(self, user_input: str, agent_name: str) -> float:
        """Calculate risk score based on input content and agent type"""
        base_risk = 0.3
        
        # Adjust based on input length
        if len(user_input) > 200:
            base_risk += 0.1
        elif len(user_input) < 50:
            base_risk += 0.05
        
        # Adjust based on agent type
        if "evaluator" in agent_name.lower():
            base_risk += 0.15  # Evaluators often provide criticism
        elif "creative" in agent_name.lower():
            base_risk += 0.1   # Creative agents may be innovative
        elif "vp" in agent_name.lower():
            base_risk += 0.2   # VP agents have high stakes
        
        # Adjust based on content keywords
        risk_keywords = ["critique", "problem", "issue", "fail", "wrong", "bad", "terrible"]
        for keyword in risk_keywords:
            if keyword.lower() in user_input.lower():
                base_risk += 0.05
        
        # Add some randomness for realistic variation
        base_risk += random.uniform(-0.1, 0.1)
        
        # Ensure score is between 0 and 1
        return max(0.0, min(1.0, base_risk))
    
    def get_risk_assessment(self, user_input: str, agent_name: str) -> Dict[str, Any]:
        """Get detailed risk assessment"""
        risk_score = self._calculate_risk_score(user_input, agent_name)
        
        if risk_score < 0.4:
            risk_level = "LOW"
            recommendation = "Proceed with normal execution"
        elif risk_score < 0.7:
            risk_level = "MEDIUM"
            recommendation = "Consider fallback pattern"
        else:
            risk_level = "HIGH"
            recommendation = "Use fallback pattern"
        
        return {
            "risk_score": risk_score,
            "risk_level": risk_level,
            "recommendation": recommendation,
            "agent_name": agent_name
        } 