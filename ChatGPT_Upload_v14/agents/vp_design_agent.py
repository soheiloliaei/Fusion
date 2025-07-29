"""
VP Design Agent - Fusion v14
Refactored as tool runner with async capabilities
"""

import asyncio
import time
from typing import Dict, Any, List, Optional
import logging
from memory.agent_memory import agent_memory

class VPDesignAgent:
    """
    VP Design Agent - Fusion v14
    Handles design critique, enhancement, and tool coordination
    """
    
    def __init__(self):
        self.logger = logging.getLogger("VPDesignAgent")
        self.design_principles = [
            "User-centered design",
            "Accessibility first",
            "Consistent visual hierarchy",
            "Clear information architecture",
            "Responsive design patterns",
            "Performance optimization",
            "Brand consistency"
        ]
        
    async def run(self, input_prompt: str, tools: Dict[str, Any] = None) -> Dict[str, Any]:
        """Main async execution method"""
        return await self.run_async(input_prompt, tools)
        
    async def run_async(self, input_prompt: str, tools: Dict[str, Any] = None) -> Dict[str, Any]:
        """Async execution with tool coordination"""
        
        start_time = time.time()
        tools_used = []
        
        try:
            self.logger.info("VP Design Agent starting analysis")
            
            # Step 1: Analyze the design request
            analysis = await self._analyze_design_request(input_prompt)
            
            # Step 2: Apply design tools if available
            enhanced_analysis = analysis
            if tools:
                enhanced_analysis = await self._apply_design_tools(analysis, tools, tools_used)
                
            # Step 3: Generate design recommendations
            recommendations = await self._generate_design_recommendations(enhanced_analysis)
            
            # Step 4: Create enhanced output
            enhanced_output = await self._create_enhanced_output(input_prompt, recommendations)
            
            execution_time = time.time() - start_time
            
            confidence = self._calculate_confidence(enhanced_analysis, recommendations)
            
            # Store in memory
            await agent_memory.store_agent_run(
                agent_name="vp_design",
                prompt=input_prompt,
                response=enhanced_output,
                confidence=confidence,
                fallback_flag=False,
                additional_data={
                    "design_analysis": enhanced_analysis,
                    "recommendations": recommendations,
                    "tools_used": tools_used
                }
            )
            
            result = {
                "output": enhanced_output,
                "enhanced_output": enhanced_output,
                "confidence": confidence,
                "design_analysis": enhanced_analysis,
                "recommendations": recommendations,
                "tools_used": tools_used,
                "execution_time": execution_time,
                "shared_state": {
                    "design_principles_applied": self.design_principles,
                    "analysis_timestamp": time.time()
                }
            }
            
            self.logger.info(f"VP Design Agent completed in {execution_time:.2f}s")
            return result
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.error(f"VP Design Agent failed: {e}")
            
            return {
                "error": str(e),
                "confidence": 0.0,
                "tools_used": tools_used,
                "execution_time": execution_time
            }
            
    async def _analyze_design_request(self, input_prompt: str) -> Dict[str, Any]:
        """Analyze the design request and extract key information"""
        
        analysis = {
            "request_type": self._identify_request_type(input_prompt),
            "design_elements": self._extract_design_elements(input_prompt),
            "user_needs": self._identify_user_needs(input_prompt),
            "constraints": self._identify_constraints(input_prompt),
            "target_audience": self._identify_target_audience(input_prompt)
        }
        
        # Simulate async processing
        await asyncio.sleep(0.1)
        
        return analysis
        
    async def _apply_design_tools(self, analysis: Dict[str, Any], 
                                tools: Dict[str, Any], tools_used: List[str]) -> Dict[str, Any]:
        """Apply available design tools to enhance analysis"""
        
        enhanced_analysis = analysis.copy()
        
        # Apply UX audit tool if available
        if "ux_audit" in tools:
            try:
                ux_audit_result = await tools["ux_audit"].run(analysis)
                enhanced_analysis["ux_audit"] = ux_audit_result
                tools_used.append("ux_audit")
                self.logger.info("Applied UX audit tool")
            except Exception as e:
                self.logger.warning(f"UX audit tool failed: {e}")
                
        # Apply trust explainer tool if available
        if "trust_explainer" in tools:
            try:
                trust_result = await tools["trust_explainer"].run(analysis)
                enhanced_analysis["trust_analysis"] = trust_result
                tools_used.append("trust_explainer")
                self.logger.info("Applied trust explainer tool")
            except Exception as e:
                self.logger.warning(f"Trust explainer tool failed: {e}")
                
        return enhanced_analysis
        
    async def _generate_design_recommendations(self, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate design recommendations based on analysis"""
        
        recommendations = []
        
        # Generate recommendations based on design principles
        for principle in self.design_principles:
            if self._should_apply_principle(principle, analysis):
                recommendation = await self._create_recommendation(principle, analysis)
                recommendations.append(recommendation)
                
        # Add specific recommendations based on analysis
        if analysis.get("request_type") == "ui_design":
            recommendations.append({
                "type": "ui_improvement",
                "title": "Enhance Visual Hierarchy",
                "description": "Implement clear visual hierarchy to improve user navigation",
                "priority": "high",
                "confidence": 0.9
            })
            
        if analysis.get("request_type") == "ux_design":
            recommendations.append({
                "type": "ux_improvement", 
                "title": "Optimize User Flow",
                "description": "Streamline user journey to reduce friction points",
                "priority": "high",
                "confidence": 0.85
            })
            
        return recommendations
        
    async def _create_enhanced_output(self, input_prompt: str, 
                                    recommendations: List[Dict[str, Any]]) -> str:
        """Create enhanced output with design recommendations"""
        
        output = f"# Design Analysis & Recommendations\n\n"
        output += f"## Original Request\n{input_prompt}\n\n"
        
        output += "## Key Recommendations\n\n"
        
        for i, rec in enumerate(recommendations, 1):
            output += f"### {i}. {rec['title']}\n"
            output += f"**Type:** {rec['type']}\n"
            output += f"**Priority:** {rec['priority']}\n"
            output += f"**Description:** {rec['description']}\n"
            output += f"**Confidence:** {rec['confidence']:.2f}\n\n"
            
        output += "## Implementation Notes\n\n"
        output += "- Apply design principles systematically\n"
        output += "- Test with target audience\n"
        output += "- Iterate based on feedback\n"
        output += "- Monitor performance metrics\n"
        
        return output
        
    def _identify_request_type(self, input_prompt: str) -> str:
        """Identify the type of design request"""
        prompt_lower = input_prompt.lower()
        
        if any(word in prompt_lower for word in ["ui", "interface", "visual"]):
            return "ui_design"
        elif any(word in prompt_lower for word in ["ux", "user experience", "flow"]):
            return "ux_design"
        elif any(word in prompt_lower for word in ["brand", "identity", "logo"]):
            return "brand_design"
        else:
            return "general_design"
            
    def _extract_design_elements(self, input_prompt: str) -> List[str]:
        """Extract design elements from the prompt"""
        elements = []
        prompt_lower = input_prompt.lower()
        
        design_keywords = {
            "color": ["color", "palette", "hue", "theme"],
            "typography": ["font", "text", "typography", "typeface"],
            "layout": ["layout", "grid", "spacing", "alignment"],
            "interaction": ["button", "click", "hover", "animation"],
            "navigation": ["menu", "nav", "breadcrumb", "sidebar"]
        }
        
        for element, keywords in design_keywords.items():
            if any(keyword in prompt_lower for keyword in keywords):
                elements.append(element)
                
        return elements
        
    def _identify_user_needs(self, input_prompt: str) -> List[str]:
        """Identify user needs from the prompt"""
        needs = []
        prompt_lower = input_prompt.lower()
        
        if "accessibility" in prompt_lower or "accessible" in prompt_lower:
            needs.append("accessibility")
        if "mobile" in prompt_lower or "responsive" in prompt_lower:
            needs.append("mobile_friendly")
        if "fast" in prompt_lower or "performance" in prompt_lower:
            needs.append("performance")
        if "simple" in prompt_lower or "easy" in prompt_lower:
            needs.append("simplicity")
            
        return needs
        
    def _identify_constraints(self, input_prompt: str) -> List[str]:
        """Identify design constraints from the prompt"""
        constraints = []
        prompt_lower = input_prompt.lower()
        
        if "budget" in prompt_lower or "cost" in prompt_lower:
            constraints.append("budget_limited")
        if "time" in prompt_lower or "deadline" in prompt_lower:
            constraints.append("time_constrained")
        if "existing" in prompt_lower or "legacy" in prompt_lower:
            constraints.append("existing_system")
            
        return constraints
        
    def _identify_target_audience(self, input_prompt: str) -> str:
        """Identify target audience from the prompt"""
        prompt_lower = input_prompt.lower()
        
        if "business" in prompt_lower or "enterprise" in prompt_lower:
            return "business_users"
        elif "consumer" in prompt_lower or "personal" in prompt_lower:
            return "consumer_users"
        elif "developer" in prompt_lower or "technical" in prompt_lower:
            return "technical_users"
        else:
            return "general_users"
            
    def _should_apply_principle(self, principle: str, analysis: Dict[str, Any]) -> bool:
        """Determine if a design principle should be applied"""
        
        if principle == "User-centered design":
            return True  # Always apply
        elif principle == "Accessibility first":
            return "accessibility" in analysis.get("user_needs", [])
        elif principle == "Consistent visual hierarchy":
            return analysis.get("request_type") in ["ui_design", "general_design"]
        elif principle == "Clear information architecture":
            return analysis.get("request_type") in ["ux_design", "general_design"]
        elif principle == "Responsive design patterns":
            return "mobile_friendly" in analysis.get("user_needs", [])
        elif principle == "Performance optimization":
            return "performance" in analysis.get("user_needs", [])
        elif principle == "Brand consistency":
            return analysis.get("request_type") == "brand_design"
            
        return False
        
    async def _create_recommendation(self, principle: str, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Create a specific recommendation based on a design principle"""
        
        recommendation_map = {
            "User-centered design": {
                "type": "ux_improvement",
                "title": "Implement User-Centered Design",
                "description": "Focus on user needs and behaviors throughout the design process",
                "priority": "high",
                "confidence": 0.95
            },
            "Accessibility first": {
                "type": "accessibility",
                "title": "Ensure Accessibility Compliance",
                "description": "Implement WCAG guidelines and ensure inclusive design",
                "priority": "high",
                "confidence": 0.9
            },
            "Consistent visual hierarchy": {
                "type": "ui_improvement",
                "title": "Establish Visual Hierarchy",
                "description": "Use typography, color, and spacing to create clear information hierarchy",
                "priority": "medium",
                "confidence": 0.85
            },
            "Clear information architecture": {
                "type": "ux_improvement",
                "title": "Optimize Information Architecture",
                "description": "Organize content and navigation for intuitive user flow",
                "priority": "high",
                "confidence": 0.9
            },
            "Responsive design patterns": {
                "type": "technical",
                "title": "Implement Responsive Design",
                "description": "Ensure optimal experience across all device sizes",
                "priority": "medium",
                "confidence": 0.8
            },
            "Performance optimization": {
                "type": "technical",
                "title": "Optimize Performance",
                "description": "Ensure fast loading times and smooth interactions",
                "priority": "medium",
                "confidence": 0.8
            },
            "Brand consistency": {
                "type": "brand",
                "title": "Maintain Brand Consistency",
                "description": "Ensure design elements align with brand guidelines",
                "priority": "medium",
                "confidence": 0.85
            }
        }
        
        return recommendation_map.get(principle, {
            "type": "general",
            "title": f"Apply {principle}",
            "description": f"Implement {principle} in the design",
            "priority": "medium",
            "confidence": 0.8
        })
        
    def _calculate_confidence(self, analysis: Dict[str, Any], 
                           recommendations: List[Dict[str, Any]]) -> float:
        """Calculate confidence score based on analysis quality and recommendations"""
        
        base_confidence = 0.8
        
        # Adjust based on analysis completeness
        if len(analysis.get("design_elements", [])) > 0:
            base_confidence += 0.05
        if len(analysis.get("user_needs", [])) > 0:
            base_confidence += 0.05
        if len(analysis.get("constraints", [])) > 0:
            base_confidence += 0.05
            
        # Adjust based on recommendation quality
        if recommendations:
            avg_rec_confidence = sum(r.get("confidence", 0.8) for r in recommendations) / len(recommendations)
            base_confidence = (base_confidence + avg_rec_confidence) / 2
            
        return min(base_confidence, 0.95)  # Cap at 0.95 