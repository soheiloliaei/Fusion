#!/usr/bin/env python3
"""
Evaluator Agent - Fusion v13.0
Evaluates output quality and provides scoring
"""

class EvaluatorAgent:
    def __init__(self):
        self.name = "Evaluator Agent"
        self.role = "Quality evaluation and scoring"
        self.scoring_criteria = {
            "clarity": 0.2,
            "completeness": 0.2,
            "actionability": 0.2,
            "innovation": 0.15,
            "feasibility": 0.15,
            "value_proposition": 0.1
        }
    
    def evaluate_output(self, output, criteria=None):
        """Evaluate the quality of an output"""
        if criteria is None:
            criteria = self.scoring_criteria
        
        scores = {}
        total_score = 0
        
        for criterion, weight in criteria.items():
            score = self._score_criterion(output, criterion)
            scores[criterion] = score
            total_score += score * weight
        
        return {
            "overall_score": round(total_score, 3),
            "detailed_scores": scores,
            "feedback": self._generate_feedback(scores),
            "recommendations": self._generate_recommendations(scores)
        }
    
    def _score_criterion(self, output, criterion):
        """Score a specific criterion"""
        if criterion == "clarity":
            return min(1.0, len(output.split()) / 50)  # More content = better clarity
        elif criterion == "completeness":
            return 0.8 if "complete" in output.lower() else 0.6
        elif criterion == "actionability":
            return 0.9 if any(word in output.lower() for word in ["step", "action", "implement"]) else 0.5
        elif criterion == "innovation":
            return 0.7 if any(word in output.lower() for word in ["innovative", "novel", "unique"]) else 0.5
        elif criterion == "feasibility":
            return 0.8 if "feasible" in output.lower() else 0.6
        elif criterion == "value_proposition":
            return 0.9 if "value" in output.lower() else 0.5
        return 0.5
    
    def _generate_feedback(self, scores):
        """Generate feedback based on scores"""
        feedback = []
        for criterion, score in scores.items():
            if score < 0.6:
                feedback.append(f"Improve {criterion}: Current score {score:.2f}")
            elif score > 0.8:
                feedback.append(f"Excellent {criterion}: Score {score:.2f}")
        return feedback
    
    def _generate_recommendations(self, scores):
        """Generate improvement recommendations"""
        recommendations = []
        low_scores = {k: v for k, v in scores.items() if v < 0.6}
        
        if "clarity" in low_scores:
            recommendations.append("Add more specific details and examples")
        if "completeness" in low_scores:
            recommendations.append("Cover all aspects of the requirement")
        if "actionability" in low_scores:
            recommendations.append("Include specific next steps and actions")
        
        return recommendations
