import json
import asyncio
from typing import Dict, Any, List, Optional
from datetime import datetime
from pattern_registry import pattern_templates

class PatternTester:
    def __init__(self):
        self.test_log = []
        self.available_patterns = list(pattern_templates.keys())
    
    def get_available_agents(self) -> List[str]:
        """Get list of available agents for testing"""
        return [
            "vp_design", "creative_director", "design_technologist", "principal_designer",
            "vp_of_design", "vp_of_product", "product_navigator", "strategy_pilot",
            "product_historian", "market_analyst", "content_designer", "deck_narrator",
            "portfolio_editor", "research_summarizer", "component_librarian",
            "ai_interaction_designer", "workflow_optimizer", "evaluator", "prompt_master",
            "dispatcher", "strategy_archivist", "feedback_amplifier", "surprisal_critic",
            "narrative_divergence", "rewrite_loop", "prompt_architect", "design_polish_agent",
            "longform_creative_chain", "narrative_freshness_rater", "structural_clarity_checker",
            "voice_match_evaluator", "rewrite_advisor", "narrative_quality_chain",
            "autocritique_loop", "design_judgment_engine", "ai_native_ux_designer",
            "design_system_engineer"
        ]
    
    def get_available_patterns(self) -> List[str]:
        """Get list of available fallback patterns"""
        return self.available_patterns
    
    def show_pattern_details(self, pattern_name: str) -> Optional[str]:
        """Show details of a specific pattern"""
        return pattern_templates.get(pattern_name)
    
    async def test_pattern_override(self, agent_name: str, input_prompt: str, 
                                  pattern_name: str, agent_map: Dict[str, Any]) -> Dict[str, Any]:
        """
        Test a specific fallback pattern by simulating high-risk scenario
        
        Args:
            agent_name: Name of the agent to test
            input_prompt: Input prompt for the agent
            pattern_name: Name of the pattern to test
            agent_map: Mapping of agent names to agent classes
            
        Returns:
            Dictionary with test results
        """
        if agent_name not in agent_map:
            raise ValueError(f"Agent '{agent_name}' not found in agent map")
        
        if pattern_name not in pattern_templates:
            raise ValueError(f"Pattern '{pattern_name}' not found. Available: {list(pattern_templates.keys())}")
        
        print(f"🧪 Testing Pattern Override")
        print(f"🎯 Agent: {agent_name}")
        print(f"🔄 Pattern: {pattern_name}")
        print(f"📝 Input: {input_prompt[:100]}{'...' if len(input_prompt) > 100 else ''}")
        print("="*60)
        
        # Get agent instance
        agent_class = agent_map[agent_name]
        agent = agent_class()
        
        # Step 1: Run agent normally (without pattern override)
        print("🔍 Step 1: Normal Agent Execution")
        from fusion import risk_aware_agent_runner
        normal_result = await risk_aware_agent_runner(input_prompt, agent, agent_name)
        
        # Step 2: Force pattern override by injecting pattern
        print("\n🧬 Step 2: Pattern Override Execution")
        pattern_prompt = pattern_templates[pattern_name]
        modified_input = f"{pattern_prompt}\n\n{input_prompt}"
        
        # Run with modified input
        pattern_result = await risk_aware_agent_runner(modified_input, agent, agent_name)
        
        # Create test summary
        test_summary = {
            "test_timestamp": datetime.now().isoformat(),
            "agent_name": agent_name,
            "pattern_name": pattern_name,
            "original_input": input_prompt,
            "pattern_prompt": pattern_prompt,
            "modified_input": modified_input,
            "normal_execution": {
                "synthetic_meta": normal_result.get("synthetic_meta", {}),
                "output": normal_result.get("agent_output", {}),
                "routed": normal_result.get("routed", False)
            },
            "pattern_execution": {
                "synthetic_meta": pattern_result.get("synthetic_meta", {}),
                "output": pattern_result.get("agent_output", {}),
                "routed": pattern_result.get("routed", False)
            },
            "comparison": {
                "risk_score_change": (
                    pattern_result.get("synthetic_meta", {}).get("risk_score", 0.0) - 
                    normal_result.get("synthetic_meta", {}).get("risk_score", 0.0)
                ),
                "output_changed": str(normal_result.get("agent_output", {})) != str(pattern_result.get("agent_output", {})),
                "pattern_effectiveness": self._evaluate_pattern_effectiveness(normal_result, pattern_result)
            }
        }
        
        # Log the test
        self.test_log.append(test_summary)
        
        # Print comparison
        self._print_test_comparison(test_summary)
        
        return test_summary
    
    def _evaluate_pattern_effectiveness(self, normal_result: Dict[str, Any], 
                                      pattern_result: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate how effective the pattern override was"""
        normal_output = str(normal_result.get("agent_output", {}))
        pattern_output = str(pattern_result.get("agent_output", {}))
        
        normal_risk = normal_result.get("synthetic_meta", {}).get("risk_score", 0.0)
        pattern_risk = pattern_result.get("synthetic_meta", {}).get("risk_score", 0.0)
        
        effectiveness = {
            "output_length_change": len(pattern_output) - len(normal_output),
            "risk_reduction": normal_risk - pattern_risk,
            "output_similarity": self._calculate_similarity(normal_output, pattern_output),
            "pattern_applied": "fallback" in pattern_output.lower() or "clarify" in pattern_output.lower()
        }
        
        # Overall effectiveness score
        score = 0.0
        if effectiveness["risk_reduction"] > 0:
            score += 0.3
        if effectiveness["output_length_change"] > 50:  # More detailed output
            score += 0.2
        if effectiveness["pattern_applied"]:
            score += 0.3
        if effectiveness["output_similarity"] < 0.8:  # Meaningful change
            score += 0.2
        
        effectiveness["overall_score"] = min(score, 1.0)
        effectiveness["verdict"] = self._get_effectiveness_verdict(effectiveness["overall_score"])
        
        return effectiveness
    
    def _calculate_similarity(self, text1: str, text2: str) -> float:
        """Simple similarity calculation between two texts"""
        if not text1 or not text2:
            return 0.0
        
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union) if union else 0.0
    
    def _get_effectiveness_verdict(self, score: float) -> str:
        """Get effectiveness verdict based on score"""
        if score >= 0.8:
            return "Highly Effective"
        elif score >= 0.6:
            return "Moderately Effective"
        elif score >= 0.4:
            return "Somewhat Effective"
        else:
            return "Low Effectiveness"
    
    def _print_test_comparison(self, test_summary: Dict[str, Any]) -> None:
        """Print formatted test comparison"""
        print(f"\n{'='*60}")
        print(f"📊 PATTERN TEST RESULTS")
        print(f"{'='*60}")
        
        print(f"🎯 Agent: {test_summary['agent_name']}")
        print(f"🔄 Pattern: {test_summary['pattern_name']}")
        
        # Risk Score Comparison
        normal_risk = test_summary['normal_execution']['synthetic_meta'].get('risk_score', 0.0)
        pattern_risk = test_summary['pattern_execution']['synthetic_meta'].get('risk_score', 0.0)
        risk_change = test_summary['comparison']['risk_score_change']
        
        print(f"\n⚠️  Risk Score Comparison:")
        print(f"   Normal: {normal_risk:.2f}")
        print(f"   Pattern: {pattern_risk:.2f}")
        print(f"   Change: {risk_change:+.2f}")
        
        # Effectiveness
        effectiveness = test_summary['comparison']['pattern_effectiveness']
        print(f"\n📈 Pattern Effectiveness:")
        print(f"   Overall Score: {effectiveness['overall_score']:.2f}")
        print(f"   Verdict: {effectiveness['verdict']}")
        print(f"   Output Changed: {test_summary['comparison']['output_changed']}")
        print(f"   Risk Reduction: {effectiveness['risk_reduction']:+.2f}")
        
        print(f"{'='*60}\n")
    
    def save_test_log(self, filename: str = None) -> None:
        """Save test log to JSON file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"pattern_test_log_{timestamp}.json"
        
        with open(filename, "w") as f:
            json.dump({
                "session_timestamp": datetime.now().isoformat(),
                "tests_conducted": len(self.test_log),
                "test_results": self.test_log
            }, f, indent=2)
        
        print(f"📁 Pattern test log saved to: {filename}")
    
    def get_test_summary(self) -> Dict[str, Any]:
        """Get summary of all tests conducted"""
        if not self.test_log:
            return {"total_tests": 0, "average_effectiveness": 0.0}
        
        total_tests = len(self.test_log)
        avg_effectiveness = sum(
            test['comparison']['pattern_effectiveness']['overall_score'] 
            for test in self.test_log
        ) / total_tests
        
        agents_tested = list(set(test['agent_name'] for test in self.test_log))
        patterns_tested = list(set(test['pattern_name'] for test in self.test_log))
        
        return {
            "total_tests": total_tests,
            "average_effectiveness": round(avg_effectiveness, 3),
            "agents_tested": agents_tested,
            "patterns_tested": patterns_tested,
            "most_effective_pattern": self._get_most_effective_pattern(),
            "most_tested_agent": self._get_most_tested_agent()
        }
    
    def _get_most_effective_pattern(self) -> Optional[str]:
        """Get the most effective pattern based on test results"""
        if not self.test_log:
            return None
        
        pattern_scores = {}
        for test in self.test_log:
            pattern = test['pattern_name']
            score = test['comparison']['pattern_effectiveness']['overall_score']
            
            if pattern not in pattern_scores:
                pattern_scores[pattern] = []
            pattern_scores[pattern].append(score)
        
        # Calculate average score for each pattern
        avg_scores = {
            pattern: sum(scores) / len(scores) 
            for pattern, scores in pattern_scores.items()
        }
        
        return max(avg_scores.items(), key=lambda x: x[1])[0] if avg_scores else None
    
    def _get_most_tested_agent(self) -> Optional[str]:
        """Get the most tested agent"""
        if not self.test_log:
            return None
        
        agent_counts = {}
        for test in self.test_log:
            agent = test['agent_name']
            agent_counts[agent] = agent_counts.get(agent, 0) + 1
        
        return max(agent_counts.items(), key=lambda x: x[1])[0] if agent_counts else None

# Global pattern tester instance
pattern_tester = PatternTester()

def get_pattern_tester() -> PatternTester:
    """Get the global pattern tester instance"""
    return pattern_tester