#!/usr/bin/env python3
"""
Reflection Agent - Fusion v15.1
Agents that review their own output and retry if confidence is low.
"""

import asyncio
import time
from typing import Any, Dict, Optional
from agents.evaluator_agent import EvaluatorAgent

class ReflectionAgent:
    def __init__(self, evaluator: Optional[EvaluatorAgent] = None, max_retries: int = 3):
        self.evaluator = evaluator or EvaluatorAgent()
        self.max_retries = max_retries
        self.retry_count = 0
        
    async def run(self, agent: Any, input_text: str, confidence_threshold: float = 0.7) -> str:
        """
        Run an agent with reflection and retry logic.
        
        Args:
            agent: The agent to run
            input_text: Input prompt for the agent
            confidence_threshold: Minimum confidence score to accept output
            
        Returns:
            The final agent output after reflection/retry
        """
        self.retry_count = 0
        
        while self.retry_count < self.max_retries:
            # Run the agent
            start_time = time.time()
            output = await agent.run(input_text)
            execution_time = time.time() - start_time
            
            # Evaluate the output
            evaluation_prompt = f"""
            Evaluate this agent output for quality and completeness:
            
            Input: {input_text}
            Output: {output}
            Execution Time: {execution_time:.2f}s
            
            Provide a confidence score (0-1) and brief evaluation.
            """
            
            evaluation_result = await self.evaluator.run(evaluation_prompt)
            
            # Extract confidence score (simple heuristic)
            confidence_score = self._extract_confidence(evaluation_result)
            
            print(f"🔍 Reflection Agent: Confidence = {confidence_score:.2f}")
            
            # Check if output meets confidence threshold
            if confidence_score >= confidence_threshold:
                print(f"✅ Output accepted (confidence: {confidence_score:.2f})")
                return output
            else:
                self.retry_count += 1
                print(f"🔄 Retrying due to low confidence ({confidence_score:.2f} < {confidence_threshold})")
                
                # Enhance the input for retry
                enhanced_input = self._enhance_input(input_text, output, evaluation_result)
                input_text = enhanced_input
                
                if self.retry_count >= self.max_retries:
                    print(f"⚠️ Max retries reached ({self.max_retries}), returning best attempt")
                    return output
        
        return output
    
    def _extract_confidence(self, evaluation_text: str) -> float:
        """Extract confidence score from evaluation text."""
        try:
            # Look for confidence indicators
            if "confidence:" in evaluation_text.lower():
                confidence_part = evaluation_text.lower().split("confidence:")[1].split()[0]
                return float(confidence_part)
            elif "score:" in evaluation_text.lower():
                score_part = evaluation_text.lower().split("score:")[1].split()[0]
                return float(score_part)
            else:
                # Default confidence based on text length and keywords
                positive_keywords = ["good", "excellent", "complete", "thorough", "detailed"]
                negative_keywords = ["poor", "incomplete", "vague", "unclear", "missing"]
                
                text_lower = evaluation_text.lower()
                positive_count = sum(1 for word in positive_keywords if word in text_lower)
                negative_count = sum(1 for word in negative_keywords if word in text_lower)
                
                if positive_count > negative_count:
                    return 0.8
                elif negative_count > positive_count:
                    return 0.3
                else:
                    return 0.6
        except:
            return 0.5  # Default confidence
    
    def _enhance_input(self, original_input: str, previous_output: str, evaluation: str) -> str:
        """Enhance the input based on previous output and evaluation."""
        enhancement = f"""
        Previous attempt: {previous_output}
        Evaluation: {evaluation}
        
        Please improve upon the previous response. Consider:
        - Address any gaps or missing elements
        - Provide more specific and actionable details
        - Ensure completeness and clarity
        - Focus on the original request: {original_input}
        """
        
        return f"{original_input}\n\n{enhancement}"
    
    def get_retry_stats(self) -> Dict[str, Any]:
        """Get retry statistics."""
        return {
            "retry_count": self.retry_count,
            "max_retries": self.max_retries,
            "retry_rate": self.retry_count / self.max_retries if self.max_retries > 0 else 0
        }

# Example usage
async def main():
    """Example of using ReflectionAgent."""
    from agents.vp_design_agent import VPDesignAgent
    
    # Initialize reflection agent
    reflection_agent = ReflectionAgent(max_retries=3)
    
    # Create a VP Design agent
    vp_design = VPDesignAgent()
    
    # Run with reflection
    result = await reflection_agent.run(
        vp_design, 
        "Design a mobile app interface for a food delivery service",
        confidence_threshold=0.8
    )
    
    print(f"Final result: {result}")
    print(f"Retry stats: {reflection_agent.get_retry_stats()}")

if __name__ == "__main__":
    asyncio.run(main()) 