#!/usr/bin/env python3
"""
VP of Design Agent - Fusion v14
Acts as a design executive reviewing design decisions, aligning with vision, critiquing system health, and advising on cross-functional impact
"""

import asyncio
import time
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime

class VPOfDesignAgent:
    """
    VP of Design Agent - Fusion v14
    Acts as a design executive reviewing design decisions, aligning with vision, critiquing system health, and advising on cross-functional impact
    """
    
    def __init__(self):
        self.logger = logging.getLogger("VPOfDesignAgent")
        
        # Design leadership principles
        self.design_leadership_principles = {
            "strategic_alignment": ["business_objectives", "user_needs", "design_vision"],
            "system_thinking": ["design_systems", "component_libraries", "design_tokens"],
            "cross_functional_collaboration": ["engineering_partnership", "product_alignment", "stakeholder_communication"],
            "quality_assurance": ["design_reviews", "usability_testing", "accessibility_compliance"],
            "innovation_culture": ["design_thinking", "experimentation", "continuous_improvement"]
        }
        
        # Design system health indicators
        self.system_health_indicators = {
            "consistency": ["design_tokens", "component_reuse", "style_guidelines"],
            "scalability": ["modular_architecture", "responsive_patterns", "platform_agnostic"],
            "accessibility": ["wcag_compliance", "inclusive_design", "usability_testing"],
            "performance": ["design_efficiency", "load_times", "user_experience_metrics"],
            "maintainability": ["documentation", "version_control", "design_ops"]
        }
        
        # Design maturity levels
        self.design_maturity_levels = {
            "ad_hoc": {
                "description": "No formal design process",
                "characteristics": ["reactive_design", "inconsistent_quality", "limited_collaboration"],
                "improvement_areas": ["establish_processes", "create_guidelines", "build_team"]
            },
            "repeatable": {
                "description": "Basic design processes in place",
                "characteristics": ["consistent_quality", "basic_guidelines", "team_collaboration"],
                "improvement_areas": ["standardize_processes", "expand_guidelines", "enhance_tools"]
            },
            "defined": {
                "description": "Well-defined design system",
                "characteristics": ["design_system", "comprehensive_guidelines", "cross_functional_work"],
                "improvement_areas": ["optimize_processes", "enhance_automation", "measure_impact"]
            },
            "managed": {
                "description": "Data-driven design decisions",
                "characteristics": ["metrics_driven", "continuous_improvement", "predictable_outcomes"],
                "improvement_areas": ["advanced_analytics", "ai_integration", "predictive_design"]
            },
            "optimizing": {
                "description": "Continuous design innovation",
                "characteristics": ["innovation_culture", "rapid_iteration", "market_leadership"],
                "improvement_areas": ["sustain_innovation", "scale_impact", "future_vision"]
            }
        }
        
        # Cross-functional impact areas
        self.cross_functional_impact = {
            "engineering": ["development_velocity", "code_quality", "technical_debt"],
            "product": ["feature_adoption", "user_satisfaction", "business_metrics"],
            "marketing": ["brand_consistency", "user_acquisition", "conversion_rates"],
            "customer_support": ["user_onboarding", "support_efficiency", "customer_satisfaction"]
        }
        
    async def run_async(self, prompt: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main async execution method for VP of Design Agent
        """
        start_time = time.time()
        self.logger.info("VP of Design Agent starting analysis")
        
        try:
            # Review design decisions
            design_review = await self._review_design_decisions(prompt)
            
            # Assess vision alignment
            vision_alignment = await self._assess_vision_alignment(prompt, design_review)
            
            # Critique system health
            system_health_critique = await self._critique_system_health(prompt, design_review)
            
            # Analyze cross-functional impact
            cross_functional_impact = await self._analyze_cross_functional_impact(prompt, design_review)
            
            # Create enhanced output
            enhanced_output = await self._create_enhanced_output(prompt, design_review, vision_alignment, system_health_critique, cross_functional_impact)
            
            execution_time = time.time() - start_time
            confidence = self._calculate_confidence(design_review, vision_alignment, system_health_critique)
            
            self.logger.info(f"VP of Design Agent completed in {execution_time:.2f}s")
            
            return {
                "output": enhanced_output,
                "enhanced_output": enhanced_output,
                "confidence": confidence,
                "design_review": design_review,
                "vision_alignment": vision_alignment,
                "system_health_critique": system_health_critique,
                "cross_functional_impact": cross_functional_impact,
                "execution_time": execution_time,
                "shared_state": {
                    "design_maturity": design_review.get("maturity_level"),
                    "vision_alignment_score": vision_alignment.get("alignment_score"),
                    "system_health_score": system_health_critique.get("overall_health"),
                    "impact_areas": len(cross_functional_impact.get("impact_areas", [])),
                    "analysis_timestamp": datetime.now().timestamp()
                }
            }
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.error(f"VP of Design Agent failed: {e}")
            return {
                "error": str(e),
                "confidence": 0.0,
                "execution_time": execution_time
            }
    
    async def _review_design_decisions(self, prompt: str) -> Dict[str, Any]:
        """Review design decisions and provide executive perspective"""
        
        # Analyze design approach
        design_approach = self._analyze_design_approach(prompt)
        
        # Assess design quality
        design_quality = self._assess_design_quality(prompt)
        
        # Evaluate design maturity
        design_maturity = self._evaluate_design_maturity(prompt)
        
        # Identify improvement opportunities
        improvement_opportunities = self._identify_improvement_opportunities(prompt, design_approach, design_quality)
        
        return {
            "design_approach": design_approach,
            "design_quality": design_quality,
            "maturity_level": design_maturity,
            "improvement_opportunities": improvement_opportunities,
            "strategic_recommendations": self._generate_strategic_recommendations(design_approach, design_quality, design_maturity)
        }
    
    async def _assess_vision_alignment(self, prompt: str, design_review: Dict) -> Dict[str, Any]:
        """Assess alignment with design vision and business objectives"""
        
        # Evaluate strategic alignment
        strategic_alignment = self._evaluate_strategic_alignment(prompt, design_review)
        
        # Assess user-centered focus
        user_centered_focus = self._assess_user_centered_focus(prompt, design_review)
        
        # Review innovation alignment
        innovation_alignment = self._review_innovation_alignment(prompt, design_review)
        
        # Calculate overall alignment score
        alignment_score = self._calculate_alignment_score(strategic_alignment, user_centered_focus, innovation_alignment)
        
        return {
            "strategic_alignment": strategic_alignment,
            "user_centered_focus": user_centered_focus,
            "innovation_alignment": innovation_alignment,
            "alignment_score": alignment_score,
            "alignment_gaps": self._identify_alignment_gaps(strategic_alignment, user_centered_focus, innovation_alignment)
        }
    
    async def _critique_system_health(self, prompt: str, design_review: Dict) -> Dict[str, Any]:
        """Critique design system health and sustainability"""
        
        # Assess design system maturity
        system_maturity = self._assess_system_maturity(prompt, design_review)
        
        # Evaluate consistency and coherence
        consistency_coherence = self._evaluate_consistency_coherence(prompt, design_review)
        
        # Review scalability and maintainability
        scalability_maintainability = self._review_scalability_maintainability(prompt, design_review)
        
        # Assess accessibility and inclusivity
        accessibility_inclusivity = self._assess_accessibility_inclusivity(prompt, design_review)
        
        # Calculate overall health score
        overall_health = self._calculate_health_score(system_maturity, consistency_coherence, scalability_maintainability, accessibility_inclusivity)
        
        return {
            "system_maturity": system_maturity,
            "consistency_coherence": consistency_coherence,
            "scalability_maintainability": scalability_maintainability,
            "accessibility_inclusivity": accessibility_inclusivity,
            "overall_health": overall_health,
            "health_improvements": self._identify_health_improvements(system_maturity, consistency_coherence, scalability_maintainability, accessibility_inclusivity)
        }
    
    async def _analyze_cross_functional_impact(self, prompt: str, design_review: Dict) -> Dict[str, Any]:
        """Analyze cross-functional impact of design decisions"""
        
        # Analyze engineering impact
        engineering_impact = self._analyze_engineering_impact(prompt, design_review)
        
        # Assess product impact
        product_impact = self._assess_product_impact(prompt, design_review)
        
        # Review marketing impact
        marketing_impact = self._review_marketing_impact(prompt, design_review)
        
        # Evaluate customer support impact
        customer_support_impact = self._evaluate_customer_support_impact(prompt, design_review)
        
        return {
            "impact_areas": {
                "engineering": engineering_impact,
                "product": product_impact,
                "marketing": marketing_impact,
                "customer_support": customer_support_impact
            },
            "overall_impact": self._calculate_overall_impact(engineering_impact, product_impact, marketing_impact, customer_support_impact),
            "collaboration_recommendations": self._generate_collaboration_recommendations(engineering_impact, product_impact, marketing_impact, customer_support_impact)
        }
    
    async def _create_enhanced_output(self, prompt: str, design_review: Dict, vision_alignment: Dict, system_health_critique: Dict, cross_functional_impact: Dict) -> str:
        """Create enhanced output with executive design perspective"""
        
        return f"""# VP of Design Executive Review

## Original Request
{prompt}

## Design Decision Review

### Design Approach
**Approach:** {design_review.get('design_approach', {}).get('type', 'unknown')}
**Quality Score:** {design_review.get('design_quality', {}).get('score', 0):.2f}/1.00
**Maturity Level:** {design_review.get('maturity_level', 'unknown').upper()}

### Strategic Recommendations
{', '.join(design_review.get('strategic_recommendations', ['None provided']))}

### Improvement Opportunities
{', '.join(design_review.get('improvement_opportunities', ['None identified']))}

## Vision Alignment Assessment

### Alignment Score
**Score:** {vision_alignment.get('alignment_score', 0):.2f}/1.00

### Strategic Alignment
{vision_alignment.get('strategic_alignment', {}).get('assessment', 'Not assessed')}

### User-Centered Focus
{vision_alignment.get('user_centered_focus', {}).get('assessment', 'Not assessed')}

### Innovation Alignment
{vision_alignment.get('innovation_alignment', {}).get('assessment', 'Not assessed')}

### Alignment Gaps
{', '.join(vision_alignment.get('alignment_gaps', ['None identified']))}

## Design System Health Critique

### Overall Health Score
**Score:** {system_health_critique.get('overall_health', 0):.2f}/1.00

### System Maturity
**Level:** {system_health_critique.get('system_maturity', {}).get('level', 'unknown')}
**Assessment:** {system_health_critique.get('system_maturity', {}).get('assessment', 'Not assessed')}

### Consistency & Coherence
**Score:** {system_health_critique.get('consistency_coherence', {}).get('score', 0):.2f}/1.00
**Issues:** {', '.join(system_health_critique.get('consistency_coherence', {}).get('issues', ['None identified']))}

### Scalability & Maintainability
**Score:** {system_health_critique.get('scalability_maintainability', {}).get('score', 0):.2f}/1.00
**Assessment:** {system_health_critique.get('scalability_maintainability', {}).get('assessment', 'Not assessed')}

### Accessibility & Inclusivity
**Score:** {system_health_critique.get('accessibility_inclusivity', {}).get('score', 0):.2f}/1.00
**Compliance:** {system_health_critique.get('accessibility_inclusivity', {}).get('compliance_level', 'unknown')}

### Health Improvements
{', '.join(system_health_critique.get('health_improvements', ['None identified']))}

## Cross-Functional Impact Analysis

### Engineering Impact
**Velocity:** {cross_functional_impact.get('impact_areas', {}).get('engineering', {}).get('development_velocity', 'unknown')}
**Quality:** {cross_functional_impact.get('impact_areas', {}).get('engineering', {}).get('code_quality', 'unknown')}

### Product Impact
**Adoption:** {cross_functional_impact.get('impact_areas', {}).get('product', {}).get('feature_adoption', 'unknown')}
**Satisfaction:** {cross_functional_impact.get('impact_areas', {}).get('product', {}).get('user_satisfaction', 'unknown')}

### Marketing Impact
**Brand Consistency:** {cross_functional_impact.get('impact_areas', {}).get('marketing', {}).get('brand_consistency', 'unknown')}
**Conversion:** {cross_functional_impact.get('impact_areas', {}).get('marketing', {}).get('conversion_rates', 'unknown')}

### Customer Support Impact
**Onboarding:** {cross_functional_impact.get('impact_areas', {}).get('customer_support', {}).get('user_onboarding', 'unknown')}
**Efficiency:** {cross_functional_impact.get('impact_areas', {}).get('customer_support', {}).get('support_efficiency', 'unknown')}

### Overall Impact
**Score:** {cross_functional_impact.get('overall_impact', {}).get('score', 0):.2f}/1.00
**Assessment:** {cross_functional_impact.get('overall_impact', {}).get('assessment', 'Not assessed')}

### Collaboration Recommendations
{', '.join(cross_functional_impact.get('collaboration_recommendations', ['None provided']))}

## Executive Confidence
**Score:** {self._calculate_confidence(design_review, vision_alignment, system_health_critique):.2f}/1.00

*Generated by Fusion v14 VP of Design Agent*"""
    
    def _analyze_design_approach(self, prompt: str) -> Dict[str, Any]:
        """Analyze the design approach being used"""
        prompt_lower = prompt.lower()
        
        if "user-centered" in prompt_lower or "user research" in prompt_lower:
            return {"type": "user_centered", "strength": "high", "focus": "user_needs"}
        elif "data-driven" in prompt_lower or "analytics" in prompt_lower:
            return {"type": "data_driven", "strength": "medium", "focus": "metrics"}
        elif "design system" in prompt_lower or "components" in prompt_lower:
            return {"type": "systematic", "strength": "high", "focus": "consistency"}
        else:
            return {"type": "general", "strength": "medium", "focus": "balanced"}
    
    def _assess_design_quality(self, prompt: str) -> Dict[str, Any]:
        """Assess the quality of design decisions"""
        prompt_lower = prompt.lower()
        
        quality_factors = []
        score = 0.7  # Base score
        
        if "accessibility" in prompt_lower:
            quality_factors.append("accessibility_compliance")
            score += 0.1
            
        if "usability" in prompt_lower or "user experience" in prompt_lower:
            quality_factors.append("usability_focus")
            score += 0.1
            
        if "consistency" in prompt_lower:
            quality_factors.append("design_consistency")
            score += 0.05
            
        if "innovation" in prompt_lower:
            quality_factors.append("innovation_quality")
            score += 0.05
            
        return {
            "score": min(score, 1.0),
            "factors": quality_factors,
            "assessment": self._generate_quality_assessment(score)
        }
    
    def _evaluate_design_maturity(self, prompt: str) -> str:
        """Evaluate design maturity level"""
        prompt_lower = prompt.lower()
        
        if "design system" in prompt_lower and "mature" in prompt_lower:
            return "managed"
        elif "design system" in prompt_lower:
            return "defined"
        elif "process" in prompt_lower or "guidelines" in prompt_lower:
            return "repeatable"
        elif "ad hoc" in prompt_lower or "reactive" in prompt_lower:
            return "ad_hoc"
        else:
            return "repeatable"
    
    def _identify_improvement_opportunities(self, prompt: str, design_approach: Dict, design_quality: Dict) -> List[str]:
        """Identify improvement opportunities"""
        opportunities = []
        
        if design_approach.get("type") == "general":
            opportunities.append("adopt_user_centered_design")
            
        if design_quality.get("score", 0) < 0.8:
            opportunities.append("enhance_quality_processes")
            
        if "accessibility" not in prompt.lower():
            opportunities.append("improve_accessibility_focus")
            
        return opportunities
    
    def _generate_strategic_recommendations(self, design_approach: Dict, design_quality: Dict, design_maturity: str) -> List[str]:
        """Generate strategic recommendations"""
        recommendations = []
        
        if design_approach.get("type") == "general":
            recommendations.append("Establish clear design principles and vision")
            
        if design_quality.get("score", 0) < 0.8:
            recommendations.append("Implement comprehensive quality assurance processes")
            
        if design_maturity in ["ad_hoc", "repeatable"]:
            recommendations.append("Invest in design system development")
            
        return recommendations
    
    def _evaluate_strategic_alignment(self, prompt: str, design_review: Dict) -> Dict[str, Any]:
        """Evaluate strategic alignment"""
        prompt_lower = prompt.lower()
        
        alignment_factors = []
        score = 0.7
        
        if "business" in prompt_lower or "strategy" in prompt_lower:
            alignment_factors.append("business_objectives")
            score += 0.1
            
        if "user" in prompt_lower:
            alignment_factors.append("user_needs")
            score += 0.1
            
        if "vision" in prompt_lower:
            alignment_factors.append("design_vision")
            score += 0.1
            
        return {
            "score": min(score, 1.0),
            "factors": alignment_factors,
            "assessment": "Good alignment with strategic objectives"
        }
    
    def _assess_user_centered_focus(self, prompt: str, design_review: Dict) -> Dict[str, Any]:
        """Assess user-centered focus"""
        prompt_lower = prompt.lower()
        
        focus_factors = []
        score = 0.6
        
        if "user research" in prompt_lower:
            focus_factors.append("user_research")
            score += 0.2
            
        if "usability" in prompt_lower:
            focus_factors.append("usability_testing")
            score += 0.1
            
        if "user experience" in prompt_lower:
            focus_factors.append("ux_focus")
            score += 0.1
            
        return {
            "score": min(score, 1.0),
            "factors": focus_factors,
            "assessment": "Moderate user-centered focus"
        }
    
    def _review_innovation_alignment(self, prompt: str, design_review: Dict) -> Dict[str, Any]:
        """Review innovation alignment"""
        prompt_lower = prompt.lower()
        
        innovation_factors = []
        score = 0.5
        
        if "innovation" in prompt_lower:
            innovation_factors.append("innovation_focus")
            score += 0.2
            
        if "experimentation" in prompt_lower:
            innovation_factors.append("experimentation")
            score += 0.2
            
        if "cutting_edge" in prompt_lower:
            innovation_factors.append("advanced_techniques")
            score += 0.1
            
        return {
            "score": min(score, 1.0),
            "factors": innovation_factors,
            "assessment": "Standard innovation approach"
        }
    
    def _calculate_alignment_score(self, strategic_alignment: Dict, user_centered_focus: Dict, innovation_alignment: Dict) -> float:
        """Calculate overall alignment score"""
        scores = [
            strategic_alignment.get("score", 0.0),
            user_centered_focus.get("score", 0.0),
            innovation_alignment.get("score", 0.0)
        ]
        
        return sum(scores) / len(scores)
    
    def _identify_alignment_gaps(self, strategic_alignment: Dict, user_centered_focus: Dict, innovation_alignment: Dict) -> List[str]:
        """Identify alignment gaps"""
        gaps = []
        
        if strategic_alignment.get("score", 0.0) < 0.7:
            gaps.append("strategic_alignment")
            
        if user_centered_focus.get("score", 0.0) < 0.7:
            gaps.append("user_centered_focus")
            
        if innovation_alignment.get("score", 0.0) < 0.6:
            gaps.append("innovation_alignment")
            
        return gaps
    
    def _assess_system_maturity(self, prompt: str, design_review: Dict) -> Dict[str, Any]:
        """Assess design system maturity"""
        maturity_level = design_review.get("maturity_level", "repeatable")
        maturity_info = self.design_maturity_levels.get(maturity_level, self.design_maturity_levels["repeatable"])
        
        return {
            "level": maturity_level,
            "description": maturity_info["description"],
            "characteristics": maturity_info["characteristics"],
            "improvement_areas": maturity_info["improvement_areas"],
            "assessment": f"Design system is at {maturity_level} maturity level"
        }
    
    def _evaluate_consistency_coherence(self, prompt: str, design_review: Dict) -> Dict[str, Any]:
        """Evaluate consistency and coherence"""
        prompt_lower = prompt.lower()
        
        issues = []
        score = 0.8
        
        if "inconsistent" in prompt_lower:
            issues.append("design_inconsistency")
            score -= 0.2
            
        if "fragmented" in prompt_lower:
            issues.append("fragmented_experience")
            score -= 0.1
            
        return {
            "score": max(score, 0.0),
            "issues": issues,
            "assessment": "Good consistency and coherence"
        }
    
    def _review_scalability_maintainability(self, prompt: str, design_review: Dict) -> Dict[str, Any]:
        """Review scalability and maintainability"""
        prompt_lower = prompt.lower()
        
        score = 0.7
        
        if "scalable" in prompt_lower:
            score += 0.1
            
        if "maintainable" in prompt_lower:
            score += 0.1
            
        if "modular" in prompt_lower:
            score += 0.1
            
        return {
            "score": min(score, 1.0),
            "assessment": "Moderate scalability and maintainability"
        }
    
    def _assess_accessibility_inclusivity(self, prompt: str, design_review: Dict) -> Dict[str, Any]:
        """Assess accessibility and inclusivity"""
        prompt_lower = prompt.lower()
        
        compliance_level = "basic"
        score = 0.6
        
        if "accessibility" in prompt_lower:
            compliance_level = "comprehensive"
            score += 0.2
            
        if "inclusive" in prompt_lower:
            score += 0.1
            
        if "wcag" in prompt_lower:
            score += 0.1
            
        return {
            "score": min(score, 1.0),
            "compliance_level": compliance_level,
            "assessment": "Basic accessibility compliance"
        }
    
    def _calculate_health_score(self, system_maturity: Dict, consistency_coherence: Dict, scalability_maintainability: Dict, accessibility_inclusivity: Dict) -> float:
        """Calculate overall health score"""
        scores = [
            consistency_coherence.get("score", 0.0),
            scalability_maintainability.get("score", 0.0),
            accessibility_inclusivity.get("score", 0.0)
        ]
        
        # Boost for higher maturity levels
        maturity_boost = {"managed": 0.1, "defined": 0.05, "repeatable": 0.0, "ad_hoc": -0.1}
        maturity_level = system_maturity.get("level", "repeatable")
        scores.append(0.7 + maturity_boost.get(maturity_level, 0.0))
        
        return sum(scores) / len(scores)
    
    def _identify_health_improvements(self, system_maturity: Dict, consistency_coherence: Dict, scalability_maintainability: Dict, accessibility_inclusivity: Dict) -> List[str]:
        """Identify health improvements"""
        improvements = []
        
        if consistency_coherence.get("score", 0.0) < 0.8:
            improvements.append("enhance_design_consistency")
            
        if scalability_maintainability.get("score", 0.0) < 0.8:
            improvements.append("improve_scalability")
            
        if accessibility_inclusivity.get("score", 0.0) < 0.8:
            improvements.append("strengthen_accessibility")
            
        return improvements
    
    def _analyze_engineering_impact(self, prompt: str, design_review: Dict) -> Dict[str, Any]:
        """Analyze impact on engineering"""
        return {
            "development_velocity": "improved",
            "code_quality": "enhanced",
            "technical_debt": "reduced",
            "assessment": "Positive impact on engineering efficiency"
        }
    
    def _assess_product_impact(self, prompt: str, design_review: Dict) -> Dict[str, Any]:
        """Assess impact on product"""
        return {
            "feature_adoption": "increased",
            "user_satisfaction": "improved",
            "business_metrics": "positive",
            "assessment": "Strong positive impact on product metrics"
        }
    
    def _review_marketing_impact(self, prompt: str, design_review: Dict) -> Dict[str, Any]:
        """Review impact on marketing"""
        return {
            "brand_consistency": "maintained",
            "user_acquisition": "improved",
            "conversion_rates": "enhanced",
            "assessment": "Good alignment with marketing objectives"
        }
    
    def _evaluate_customer_support_impact(self, prompt: str, design_review: Dict) -> Dict[str, Any]:
        """Evaluate impact on customer support"""
        return {
            "user_onboarding": "simplified",
            "support_efficiency": "improved",
            "customer_satisfaction": "enhanced",
            "assessment": "Reduced support burden through better UX"
        }
    
    def _calculate_overall_impact(self, engineering_impact: Dict, product_impact: Dict, marketing_impact: Dict, customer_support_impact: Dict) -> Dict[str, Any]:
        """Calculate overall cross-functional impact"""
        return {
            "score": 0.85,
            "assessment": "Strong positive impact across all functions",
            "summary": "Design decisions are well-aligned with cross-functional objectives"
        }
    
    def _generate_collaboration_recommendations(self, engineering_impact: Dict, product_impact: Dict, marketing_impact: Dict, customer_support_impact: Dict) -> List[str]:
        """Generate collaboration recommendations"""
        return [
            "Establish regular design-engineering sync meetings",
            "Create shared success metrics across functions",
            "Implement cross-functional design reviews",
            "Develop shared design system governance"
        ]
    
    def _generate_quality_assessment(self, score: float) -> str:
        """Generate quality assessment based on score"""
        if score >= 0.9:
            return "Excellent design quality"
        elif score >= 0.8:
            return "Good design quality"
        elif score >= 0.7:
            return "Satisfactory design quality"
        else:
            return "Needs improvement in design quality"
    
    def _calculate_confidence(self, design_review: Dict, vision_alignment: Dict, system_health_critique: Dict) -> float:
        """Calculate confidence score"""
        base_confidence = 0.8
        
        # Boost for clear design approach
        if design_review.get("design_approach", {}).get("type") != "general":
            base_confidence += 0.05
            
        # Boost for good alignment
        if vision_alignment.get("alignment_score", 0.0) > 0.7:
            base_confidence += 0.05
            
        # Boost for healthy system
        if system_health_critique.get("overall_health", 0.0) > 0.7:
            base_confidence += 0.05
            
        return min(base_confidence, 0.95) 