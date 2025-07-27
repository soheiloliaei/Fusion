"""
ExecutionChainOrchestrator (Fusion v13)
---------------------------------------
Routes napkin-style inputs through Strategy → Design → Prototype → QA.

Agents used:
- StrategyPilot
- ProductNavigator
- DesignTechnologist
- VPOfDesign
- EvaluatorAgent

Chains used:
- Product Strategy Chain
- Figma to Prototype Chain
- Quality Validation Chain

Pattern fallback and confidence-based routing embedded.
"""

from typing import Dict, List, Any, Optional
import json
from datetime import datetime

# Placeholder imports - will be replaced with actual agent implementations
class StrategyPilot:
    def develop_strategy(self, input_prompt):
        return {"strategy": "placeholder", "confidence": 0.8}

class ProductNavigator:
    def navigate_product(self, strategy):
        return {"product_spec": "placeholder", "confidence": 0.8}

class DesignTechnologist:
    def analyze_design(self, strategy):
        return {"design": "placeholder", "confidence": 0.8}
    
    def generate_code(self, design):
        return {"code": "placeholder", "confidence": 0.8}

class VPOfDesign:
    def review_design(self, design):
        return {"review": "placeholder", "confidence": 0.8}

class VPOfProduct:
    def validate_strategy(self, strategy):
        return {"validation": "placeholder", "confidence": 0.8}

class EvaluatorAgent:
    def evaluate_output(self, output, context):
        return {
            "metrics": {
                "clarity_score": 0.85,
                "completeness": 0.8,
                "actionability": 0.8,
                "accuracy": 0.8,
                "relevance": 0.8,
                "innovation": 0.8,
                "product_value": 0.8,
                "slt_quality": 0.8
            },
            "overall_score": 0.8
        }

class ExecutionChainOrchestrator:
    def __init__(self):
        self.memory = []
        self.confidence_threshold = 0.95
        self.fallback_routes = {
            "strategy_failure": "ProductNavigator",
            "design_failure": "VPOfDesign", 
            "code_failure": "DesignTechnologist",
            "qa_failure": "EvaluatorAgent"
        }
        self.agents = {
            "strategy": StrategyPilot(),
            "product": ProductNavigator(),
            "design": DesignTechnologist(),
            "vp_design": VPOfDesign(),
            "vp_product": VPOfProduct(),
            "evaluator": EvaluatorAgent()
        }
        
    def run(self, input_prompt: str) -> Dict[str, Any]:
        """
        Main orchestration method - routes input through complete pipeline
        """
        print(f"🚀 FUSION V13: Processing input: {input_prompt[:50]}...")
        
        try:
            # Step 1: Strategy Development
            print("📋 Step 1: Strategy Development")
            strategy = self._execute_strategy_phase(input_prompt)
            
            # Step 2: Product Navigation
            print("🎯 Step 2: Product Navigation")
            product_spec = self._execute_product_phase(strategy)
            
            # Step 3: Design Analysis
            print("🎨 Step 3: Design Analysis")
            design = self._execute_design_phase(product_spec)
            
            # Step 4: Code Generation
            print("💻 Step 4: Code Generation")
            code = self._execute_code_phase(design)
            
            # Step 5: Quality Assessment
            print("🔍 Step 5: Quality Assessment")
            quality = self._execute_qa_phase(code, product_spec)
            
            # Step 6: Final Decision
            print("🎯 Step 6: Final Decision")
            result = self._make_final_decision(code, quality)
            
            # Store in memory
            self._store_in_memory(input_prompt, result)
            
            return result
            
        except Exception as e:
            print(f"❌ Orchestration failed: {str(e)}")
            return self._handle_failure(input_prompt, e)
    
    def _execute_strategy_phase(self, input_prompt: str) -> Dict[str, Any]:
        """Execute strategy development phase"""
        strategy = self.agents["strategy"].develop_strategy(input_prompt)
        
        # Validate strategy with VP of Product
        validated_strategy = self.agents["vp_product"].validate_strategy(strategy)
        
        if validated_strategy.get("confidence", 0) < self.confidence_threshold:
            print(f"⚠️ Strategy confidence low ({validated_strategy.get('confidence', 0)}), using fallback")
            # Could implement fallback logic here
        
        return validated_strategy
    
    def _execute_product_phase(self, strategy: Dict[str, Any]) -> Dict[str, Any]:
        """Execute product navigation phase"""
        product_spec = self.agents["product"].navigate_product(strategy)
        return product_spec
    
    def _execute_design_phase(self, product_spec: Dict[str, Any]) -> Dict[str, Any]:
        """Execute design analysis phase"""
        design = self.agents["design"].analyze_design(product_spec)
        
        # Review design with VP of Design
        reviewed_design = self.agents["vp_design"].review_design(design)
        
        return reviewed_design
    
    def _execute_code_phase(self, design: Dict[str, Any]) -> Dict[str, Any]:
        """Execute code generation phase"""
        code = self.agents["design"].generate_code(design)
        return code
    
    def _execute_qa_phase(self, code: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute quality assessment phase"""
        quality = self.agents["evaluator"].evaluate_output(code, context)
        return quality
    
    def _make_final_decision(self, code: Dict[str, Any], quality: Dict[str, Any]) -> Dict[str, Any]:
        """Make final decision based on quality metrics"""
        overall_score = quality.get("overall_score", 0)
        clarity_score = quality.get("metrics", {}).get("clarity_score", 0)
        
        if overall_score >= self.confidence_threshold and clarity_score >= self.confidence_threshold:
            return {
                "status": "✅ SUCCESS",
                "code": code,
                "quality_metrics": quality.get("metrics", {}),
                "overall_score": overall_score,
                "timestamp": datetime.now().isoformat(),
                "confidence": "high"
            }
        else:
            return {
                "status": "⚠️ REVIEW NEEDED",
                "code": code,
                "quality_metrics": quality.get("metrics", {}),
                "overall_score": overall_score,
                "timestamp": datetime.now().isoformat(),
                "confidence": "low",
                "recommendations": self._generate_recommendations(quality)
            }
    
    def _generate_recommendations(self, quality: Dict[str, Any]) -> List[str]:
        """Generate improvement recommendations based on quality metrics"""
        recommendations = []
        metrics = quality.get("metrics", {})
        
        if metrics.get("clarity_score", 0) < self.confidence_threshold:
            recommendations.append("Improve clarity and structure of output")
        
        if metrics.get("completeness", 0) < self.confidence_threshold:
            recommendations.append("Add missing components or details")
        
        if metrics.get("actionability", 0) < self.confidence_threshold:
            recommendations.append("Provide more specific, actionable steps")
        
        return recommendations
    
    def _store_in_memory(self, input_prompt: str, result: Dict[str, Any]):
        """Store execution result in memory for learning"""
        memory_entry = {
            "input": input_prompt,
            "result": result,
            "timestamp": datetime.now().isoformat(),
            "success": result.get("status") == "✅ SUCCESS"
        }
        self.memory.append(memory_entry)
        
        # Keep only last 100 entries
        if len(self.memory) > 100:
            self.memory = self.memory[-100:]
    
    def _handle_failure(self, input_prompt: str, error: Exception) -> Dict[str, Any]:
        """Handle orchestration failures gracefully"""
        return {
            "status": "❌ FAILED",
            "error": str(error),
            "input": input_prompt,
            "timestamp": datetime.now().isoformat(),
            "recommendations": [
                "Check input format and clarity",
                "Verify all required agents are available",
                "Review error logs for specific issues"
            ]
        }
    
    def get_memory_stats(self) -> Dict[str, Any]:
        """Get statistics about orchestration memory"""
        if not self.memory:
            return {"total_executions": 0, "success_rate": 0}
        
        total = len(self.memory)
        successful = sum(1 for entry in self.memory if entry.get("success", False))
        
        return {
            "total_executions": total,
            "successful_executions": successful,
            "success_rate": successful / total if total > 0 else 0,
            "recent_executions": self.memory[-10:] if len(self.memory) >= 10 else self.memory
        }

# Example usage
if __name__ == "__main__":
    orchestrator = ExecutionChainOrchestrator()
    
    # Test with sample input
    test_input = "Design a modular Copilot tile that proactively monitors user workflows"
    result = orchestrator.run(test_input)
    
    print(f"\n🎯 RESULT: {result['status']}")
    print(f"📊 Overall Score: {result.get('overall_score', 'N/A')}")
    print(f"📈 Quality Metrics: {json.dumps(result.get('quality_metrics', {}), indent=2)}")
    
    # Show memory stats
    stats = orchestrator.get_memory_stats()
    print(f"\n📋 Memory Stats: {stats['total_executions']} executions, {stats['success_rate']:.1%} success rate")

    def promote_patterns(self):
        """
        Analyze past executions and promote high-quality outputs into reusable patterns.
        """
        from patterns.pattern_promoter import PatternPromoter
        promoter = PatternPromoter()
        promoted = promoter.promote_from_memory(self.memory)
        return promoted

    def match_patterns(self, prompt: str, result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run pattern matching engine on prompt and quality scores
        """
        from patterns.pattern_matcher import PatternMatcher
        matcher = PatternMatcher()
        return matcher.match(prompt, result)

    def apply_pattern(self, pattern_name: str, prompt: str) -> str:
        """
        Apply a known pattern to transform the input prompt.
        """
        from prompt_patterns import apply_pattern
        return apply_pattern(pattern_name, prompt)

    def log_pattern_feedback(self, pattern_name: str, original_prompt: str, improved_score: float):
        """
        Log pattern performance into feedback history.
        """
        from datetime import datetime
        feedback_log = {
            "pattern": pattern_name,
            "original_prompt": original_prompt,
            "improved_score": improved_score,
            "timestamp": datetime.now().isoformat()
        }
        self.memory.append({"feedback": feedback_log})

    def promote_successful_pattern(self, pattern_name: str, original_prompt: str, improvement_score: float):
        """
        Promote successful fallback patterns based on improvement score
        """
        from analytics.pattern_promotion import promote_pattern
        if improvement_score >= 0.15:
            promote_pattern(pattern_name, original_prompt, improvement_score)
            print(f"🚀 Pattern '{pattern_name}' promoted with score {improvement_score}")

    def auto_trigger_pattern(self, prompt: str) -> str:
        """
        Check promotion log and pre-apply top patterns if triggers match.
        """
        from analytics.pattern_promotion import get_top_promoted_patterns
        from prompt_patterns import apply_pattern
        from patterns.pattern_matcher import PatternMatcher

        top_patterns = get_top_promoted_patterns()
        matcher = PatternMatcher()

        for pattern in top_patterns:
            triggers = matcher.patterns[pattern].get("triggers", [])
            if any(trigger in prompt.lower() for trigger in triggers):
                print(f"🚀 Auto-triggered pattern '{pattern}' based on historical promotions")
                return apply_pattern(pattern, prompt)

        return prompt

    def load_pattern_memory(self):
        """
        Load top promoted patterns into orchestrator memory
        """
        from analytics.pattern_memory_loader import load_promoted_patterns
        promoted_patterns = load_promoted_patterns()
        self.memory.append({"promoted_patterns": promoted_patterns})
        print(f"🧠 Loaded {len(promoted_patterns)} promoted patterns into memory")

    def load_pattern_memory(self):
        """
        Load top promoted patterns into orchestrator memory
        """
        from analytics.pattern_memory_loader import load_promoted_patterns
        promoted_patterns = load_promoted_patterns()
        self.memory.append({"promoted_patterns": promoted_patterns})
        print(f"🧠 Loaded {len(promoted_patterns)} promoted patterns into memory")

    def run_with_creative_director(self, prompt: str):
        result = self.run(prompt)
        from agents.creative_director_agent import CreativeDirectorAgent
        cd_agent = CreativeDirectorAgent()
        critique = cd_agent.critique_output(prompt, result.get("final_output", ""))
        result["final_output"] = critique["enhanced_output"]
        result["creative_director_feedback"] = critique["feedback"]
        result["score_lift"] = critique["score_lift"]
        result["status"] = "reviewed"
        return result
