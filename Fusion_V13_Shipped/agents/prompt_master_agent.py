#!/usr/bin/env python3
"""
Prompt Master Agent - Fusion v13.0
Controls prompt logic, fallback, logging, and editing
"""

import re
import json
from typing import Dict, List, Optional

class PromptMasterAgent:
    def __init__(self):
        self.prompt_history = []
        self.safety_patterns = [
            r"delete.*all",
            r"format.*disk",
            r"sudo.*rm.*-rf",
            r"password.*\d{4,}",
            r"credit.*card.*\d{4}",
            r"ssn.*\d{3}-\d{2}-\d{4}"
        ]
        self.clarity_indicators = [
            "unclear", "vague", "confusing", "ambiguous",
            "not specific", "too broad", "unclear goal"
        ]
    
    def evaluate_prompt(self, raw_input: str) -> Dict[str, any]:
        """
        Evaluate and potentially modify a prompt for safety and clarity
        """
        evaluation = {
            "original": raw_input,
            "modified": raw_input,
            "safety_score": 1.0,
            "clarity_score": 1.0,
            "warnings": [],
            "suggestions": []
        }
        
        # Safety check
        safety_issues = self._check_safety(raw_input)
        if safety_issues:
            evaluation["safety_score"] = 0.3
            evaluation["warnings"].extend(safety_issues)
            evaluation["modified"] = self._sanitize_prompt(raw_input)
        
        # Clarity check
        clarity_issues = self._check_clarity(raw_input)
        if clarity_issues:
            evaluation["clarity_score"] = 0.7
            evaluation["suggestions"].extend(clarity_issues)
            evaluation["modified"] = self._improve_clarity(raw_input)
        
        # Log prompt
        self.prompt_history.append({
            "timestamp": self._get_timestamp(),
            "original": raw_input,
            "evaluation": evaluation
        })
        
        return evaluation
    
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
        
        return issues
    
    def _sanitize_prompt(self, prompt: str) -> str:
        """Sanitize potentially unsafe prompts"""
        # Remove or replace potentially dangerous patterns
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
        
        return improved
    
    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().isoformat()
    
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

# Example usage
if __name__ == "__main__":
    prompt_master = PromptMasterAgent()
    
    # Test evaluation
    test_prompt = "Design a feature for user management"
    result = prompt_master.evaluate_prompt(test_prompt)
    
    print("Prompt Evaluation Result:")
    print(f"Safety Score: {result['safety_score']}")
    print(f"Clarity Score: {result['clarity_score']}")
    print(f"Modified: {result['modified']}")
