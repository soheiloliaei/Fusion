"""
UX Audit Tool - Fusion v14
Modular tool for UX critique and analysis
"""

import asyncio
import time
from typing import Dict, Any, List, Optional
import logging

class UXAuditTool:
    """
    UX Audit Tool - Fusion v14
    Provides comprehensive UX analysis and recommendations
    """
    
    def __init__(self):
        self.logger = logging.getLogger("UXAuditTool")
        self.ux_heuristics = [
            "Visibility of system status",
            "Match between system and real world",
            "User control and freedom",
            "Consistency and standards",
            "Error prevention",
            "Recognition rather than recall",
            "Flexibility and efficiency of use",
            "Aesthetic and minimalist design",
            "Help users recognize, diagnose, and recover from errors",
            "Help and documentation"
        ]
        
        self.ux_metrics = {
            "usability": ["ease_of_use", "learnability", "efficiency"],
            "accessibility": ["wcag_compliance", "screen_reader", "keyboard_navigation"],
            "performance": ["load_time", "response_time", "smoothness"],
            "engagement": ["user_retention", "time_on_site", "interaction_rate"]
        }
        
    async def run(self, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """Main async execution method"""
        return await self.run_async(analysis_data)
        
    async def run_async(self, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """Async UX audit with comprehensive analysis"""
        
        start_time = time.time()
        
        try:
            self.logger.info("UX Audit Tool starting analysis")
            
            # Step 1: Extract UX context from analysis data
            ux_context = self._extract_ux_context(analysis_data)
            
            # Step 2: Perform heuristic evaluation
            heuristic_results = await self._perform_heuristic_evaluation(ux_context)
            
            # Step 3: Analyze UX metrics
            metrics_analysis = await self._analyze_ux_metrics(ux_context)
            
            # Step 4: Generate UX recommendations
            ux_recommendations = await self._generate_ux_recommendations(
                heuristic_results, metrics_analysis
            )
            
            # Step 5: Create UX audit report
            audit_report = await self._create_ux_audit_report(
                ux_context, heuristic_results, metrics_analysis, ux_recommendations
            )
            
            execution_time = time.time() - start_time
            
            result = {
                "output": audit_report,
                "ux_analysis": {
                    "context": ux_context,
                    "heuristic_results": heuristic_results,
                    "metrics_analysis": metrics_analysis,
                    "recommendations": ux_recommendations
                },
                "confidence": self._calculate_ux_confidence(heuristic_results, metrics_analysis),
                "execution_time": execution_time
            }
            
            self.logger.info(f"UX Audit Tool completed in {execution_time:.2f}s")
            return result
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.error(f"UX Audit Tool failed: {e}")
            
            return {
                "error": str(e),
                "confidence": 0.0,
                "execution_time": execution_time
            }
            
    def _extract_ux_context(self, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract UX-specific context from analysis data"""
        
        context = {
            "request_type": analysis_data.get("request_type", "general"),
            "design_elements": analysis_data.get("design_elements", []),
            "user_needs": analysis_data.get("user_needs", []),
            "target_audience": analysis_data.get("target_audience", "general_users"),
            "constraints": analysis_data.get("constraints", [])
        }
        
        # Add UX-specific analysis
        context["ux_focus_areas"] = self._identify_ux_focus_areas(context)
        context["accessibility_requirements"] = self._assess_accessibility_requirements(context)
        context["usability_priorities"] = self._determine_usability_priorities(context)
        
        return context
        
    def _identify_ux_focus_areas(self, context: Dict[str, Any]) -> List[str]:
        """Identify UX focus areas based on context"""
        
        focus_areas = []
        
        if "ui" in context.get("request_type", ""):
            focus_areas.extend(["visual_design", "interaction_design", "information_architecture"])
        if "ux" in context.get("request_type", ""):
            focus_areas.extend(["user_research", "user_journey", "usability_testing"])
        if "accessibility" in context.get("user_needs", []):
            focus_areas.append("accessibility")
        if "mobile_friendly" in context.get("user_needs", []):
            focus_areas.append("responsive_design")
        if "performance" in context.get("user_needs", []):
            focus_areas.append("performance_optimization")
            
        return focus_areas
        
    def _assess_accessibility_requirements(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Assess accessibility requirements"""
        
        requirements = {
            "wcag_level": "AA",  # Default to AA compliance
            "screen_reader_support": True,
            "keyboard_navigation": True,
            "color_contrast": True,
            "text_scaling": True
        }
        
        if "accessibility" in context.get("user_needs", []):
            requirements["wcag_level"] = "AAA"  # Higher compliance for accessibility-focused projects
            
        return requirements
        
    def _determine_usability_priorities(self, context: Dict[str, Any]) -> List[str]:
        """Determine usability priorities based on context"""
        
        priorities = ["ease_of_use", "learnability"]
        
        if context.get("target_audience") == "technical_users":
            priorities.append("efficiency")
        elif context.get("target_audience") == "business_users":
            priorities.append("productivity")
        elif context.get("target_audience") == "consumer_users":
            priorities.append("engagement")
            
        return priorities
        
    async def _perform_heuristic_evaluation(self, ux_context: Dict[str, Any]) -> Dict[str, Any]:
        """Perform heuristic evaluation using Nielsen's heuristics"""
        
        heuristic_results = {}
        
        for heuristic in self.ux_heuristics:
            score = await self._evaluate_heuristic(heuristic, ux_context)
            heuristic_results[heuristic] = {
                "score": score,
                "priority": self._determine_heuristic_priority(heuristic, ux_context),
                "recommendations": self._generate_heuristic_recommendations(heuristic, score)
            }
            
        return heuristic_results
        
    async def _evaluate_heuristic(self, heuristic: str, ux_context: Dict[str, Any]) -> float:
        """Evaluate a specific UX heuristic"""
        
        # Simulate async evaluation
        await asyncio.sleep(0.01)
        
        # Base scoring based on heuristic relevance to context
        base_score = 0.7
        
        # Adjust score based on context relevance
        if heuristic == "Visibility of system status" and "interaction_design" in ux_context.get("ux_focus_areas", []):
            base_score += 0.1
        elif heuristic == "Match between system and real world" and "user_research" in ux_context.get("ux_focus_areas", []):
            base_score += 0.1
        elif heuristic == "Accessibility" and "accessibility" in ux_context.get("ux_focus_areas", []):
            base_score += 0.15
        elif heuristic == "Aesthetic and minimalist design" and "visual_design" in ux_context.get("ux_focus_areas", []):
            base_score += 0.1
            
        return min(base_score, 1.0)
        
    def _determine_heuristic_priority(self, heuristic: str, ux_context: Dict[str, Any]) -> str:
        """Determine priority for a heuristic based on context"""
        
        high_priority_heuristics = {
            "Visibility of system status": ["interaction_design", "user_journey"],
            "Match between system and real world": ["user_research", "information_architecture"],
            "User control and freedom": ["interaction_design", "user_journey"],
            "Consistency and standards": ["visual_design", "interaction_design"],
            "Error prevention": ["usability_testing", "user_journey"],
            "Recognition rather than recall": ["information_architecture", "interaction_design"],
            "Flexibility and efficiency of use": ["user_research", "usability_testing"],
            "Aesthetic and minimalist design": ["visual_design"],
            "Help users recognize, diagnose, and recover from errors": ["usability_testing", "user_journey"],
            "Help and documentation": ["user_research", "usability_testing"]
        }
        
        focus_areas = ux_context.get("ux_focus_areas", [])
        relevant_areas = high_priority_heuristics.get(heuristic, [])
        
        if any(area in focus_areas for area in relevant_areas):
            return "high"
        else:
            return "medium"
            
    def _generate_heuristic_recommendations(self, heuristic: str, score: float) -> List[str]:
        """Generate recommendations for a heuristic based on score"""
        
        recommendations = []
        
        if score < 0.7:
            if heuristic == "Visibility of system status":
                recommendations.append("Implement clear loading states and progress indicators")
                recommendations.append("Provide immediate feedback for user actions")
            elif heuristic == "Match between system and real world":
                recommendations.append("Use familiar language and concepts from the user's domain")
                recommendations.append("Follow established conventions and patterns")
            elif heuristic == "User control and freedom":
                recommendations.append("Provide clear exit options and undo functionality")
                recommendations.append("Allow users to easily navigate back and forth")
            elif heuristic == "Consistency and standards":
                recommendations.append("Maintain consistent design patterns throughout the interface")
                recommendations.append("Follow platform-specific design guidelines")
            elif heuristic == "Error prevention":
                recommendations.append("Implement validation and confirmation for critical actions")
                recommendations.append("Design interfaces that prevent common user errors")
            elif heuristic == "Recognition rather than recall":
                recommendations.append("Make options and actions visible rather than hidden")
                recommendations.append("Provide clear navigation and search functionality")
            elif heuristic == "Flexibility and efficiency of use":
                recommendations.append("Offer shortcuts and accelerators for expert users")
                recommendations.append("Allow customization of workflows")
            elif heuristic == "Aesthetic and minimalist design":
                recommendations.append("Remove unnecessary elements and focus on essential content")
                recommendations.append("Use whitespace effectively to improve readability")
            elif heuristic == "Help users recognize, diagnose, and recover from errors":
                recommendations.append("Provide clear, actionable error messages")
                recommendations.append("Offer suggestions for error resolution")
            elif heuristic == "Help and documentation":
                recommendations.append("Provide contextual help and tooltips")
                recommendations.append("Create comprehensive but accessible documentation")
                
        return recommendations
        
    async def _analyze_ux_metrics(self, ux_context: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze UX metrics based on context"""
        
        metrics_analysis = {}
        
        for category, metrics in self.ux_metrics.items():
            category_analysis = {}
            for metric in metrics:
                score = await self._evaluate_ux_metric(metric, ux_context)
                category_analysis[metric] = {
                    "score": score,
                    "importance": self._determine_metric_importance(metric, ux_context),
                    "improvement_opportunities": self._identify_improvement_opportunities(metric, score)
                }
            metrics_analysis[category] = category_analysis
            
        return metrics_analysis
        
    async def _evaluate_ux_metric(self, metric: str, ux_context: Dict[str, Any]) -> float:
        """Evaluate a specific UX metric"""
        
        # Simulate async evaluation
        await asyncio.sleep(0.01)
        
        base_score = 0.7
        
        # Adjust score based on metric relevance
        if metric == "ease_of_use" and "usability_testing" in ux_context.get("ux_focus_areas", []):
            base_score += 0.1
        elif metric == "learnability" and "user_research" in ux_context.get("ux_focus_areas", []):
            base_score += 0.1
        elif metric == "wcag_compliance" and "accessibility" in ux_context.get("ux_focus_areas", []):
            base_score += 0.15
        elif metric == "load_time" and "performance_optimization" in ux_context.get("ux_focus_areas", []):
            base_score += 0.1
            
        return min(base_score, 1.0)
        
    def _determine_metric_importance(self, metric: str, ux_context: Dict[str, Any]) -> str:
        """Determine importance of a UX metric based on context"""
        
        high_importance_metrics = {
            "ease_of_use": ["usability_testing", "user_journey"],
            "learnability": ["user_research", "information_architecture"],
            "efficiency": ["user_research", "usability_testing"],
            "wcag_compliance": ["accessibility"],
            "screen_reader": ["accessibility"],
            "keyboard_navigation": ["accessibility"],
            "load_time": ["performance_optimization"],
            "response_time": ["performance_optimization"],
            "smoothness": ["performance_optimization"],
            "user_retention": ["user_research", "engagement"],
            "time_on_site": ["user_research", "engagement"],
            "interaction_rate": ["user_research", "engagement"]
        }
        
        focus_areas = ux_context.get("ux_focus_areas", [])
        relevant_areas = high_importance_metrics.get(metric, [])
        
        if any(area in focus_areas for area in relevant_areas):
            return "high"
        else:
            return "medium"
            
    def _identify_improvement_opportunities(self, metric: str, score: float) -> List[str]:
        """Identify improvement opportunities for a UX metric"""
        
        opportunities = []
        
        if score < 0.7:
            if metric == "ease_of_use":
                opportunities.append("Simplify complex workflows")
                opportunities.append("Reduce cognitive load")
            elif metric == "learnability":
                opportunities.append("Provide onboarding and tutorials")
                opportunities.append("Use progressive disclosure")
            elif metric == "efficiency":
                opportunities.append("Add keyboard shortcuts")
                opportunities.append("Optimize common tasks")
            elif metric == "wcag_compliance":
                opportunities.append("Implement proper semantic HTML")
                opportunities.append("Ensure sufficient color contrast")
            elif metric == "load_time":
                opportunities.append("Optimize images and assets")
                opportunities.append("Implement lazy loading")
            elif metric == "user_retention":
                opportunities.append("Improve user engagement")
                opportunities.append("Add gamification elements")
                
        return opportunities
        
    async def _generate_ux_recommendations(self, heuristic_results: Dict[str, Any],
                                         metrics_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate comprehensive UX recommendations"""
        
        recommendations = []
        
        # Generate recommendations from heuristic evaluation
        for heuristic, result in heuristic_results.items():
            if result["score"] < 0.7:
                recommendations.append({
                    "type": "heuristic_improvement",
                    "title": f"Improve {heuristic}",
                    "description": f"Address {heuristic} to enhance user experience",
                    "priority": result["priority"],
                    "confidence": 0.9,
                    "specific_recommendations": result["recommendations"]
                })
                
        # Generate recommendations from metrics analysis
        for category, metrics in metrics_analysis.items():
            for metric, analysis in metrics.items():
                if analysis["score"] < 0.7:
                    recommendations.append({
                        "type": "metric_improvement",
                        "title": f"Enhance {metric.replace('_', ' ').title()}",
                        "description": f"Improve {metric} for better {category}",
                        "priority": analysis["importance"],
                        "confidence": 0.85,
                        "improvement_opportunities": analysis["improvement_opportunities"]
                    })
                    
        return recommendations
        
    async def _create_ux_audit_report(self, ux_context: Dict[str, Any],
                                    heuristic_results: Dict[str, Any],
                                    metrics_analysis: Dict[str, Any],
                                    ux_recommendations: List[Dict[str, Any]]) -> str:
        """Create comprehensive UX audit report"""
        
        report = f"# UX Audit Report\n\n"
        
        report += f"## UX Context Analysis\n\n"
        report += f"**Request Type:** {ux_context.get('request_type', 'general')}\n"
        report += f"**Target Audience:** {ux_context.get('target_audience', 'general_users')}\n"
        report += f"**UX Focus Areas:** {', '.join(ux_context.get('ux_focus_areas', []))}\n"
        report += f"**Accessibility Requirements:** {ux_context.get('accessibility_requirements', {})}\n\n"
        
        report += f"## Heuristic Evaluation Results\n\n"
        
        for heuristic, result in heuristic_results.items():
            report += f"### {heuristic}\n"
            report += f"**Score:** {result['score']:.2f}/1.00\n"
            report += f"**Priority:** {result['priority']}\n"
            if result['recommendations']:
                report += f"**Recommendations:**\n"
                for rec in result['recommendations']:
                    report += f"- {rec}\n"
            report += "\n"
            
        report += f"## UX Metrics Analysis\n\n"
        
        for category, metrics in metrics_analysis.items():
            report += f"### {category.title()}\n"
            for metric, analysis in metrics.items():
                report += f"**{metric.replace('_', ' ').title()}:** {analysis['score']:.2f}/1.00 "
                report += f"(Importance: {analysis['importance']})\n"
            report += "\n"
            
        report += f"## Key UX Recommendations\n\n"
        
        for i, rec in enumerate(ux_recommendations, 1):
            report += f"### {i}. {rec['title']}\n"
            report += f"**Type:** {rec['type']}\n"
            report += f"**Priority:** {rec['priority']}\n"
            report += f"**Description:** {rec['description']}\n"
            report += f"**Confidence:** {rec['confidence']:.2f}\n\n"
            
        return report
        
    def _calculate_ux_confidence(self, heuristic_results: Dict[str, Any],
                               metrics_analysis: Dict[str, Any]) -> float:
        """Calculate confidence score for UX audit"""
        
        # Calculate average heuristic score
        heuristic_scores = [result["score"] for result in heuristic_results.values()]
        avg_heuristic_score = sum(heuristic_scores) / len(heuristic_scores) if heuristic_scores else 0.7
        
        # Calculate average metrics score
        all_metric_scores = []
        for category in metrics_analysis.values():
            for metric in category.values():
                all_metric_scores.append(metric["score"])
        avg_metrics_score = sum(all_metric_scores) / len(all_metric_scores) if all_metric_scores else 0.7
        
        # Weighted average (heuristics 60%, metrics 40%)
        confidence = (avg_heuristic_score * 0.6) + (avg_metrics_score * 0.4)
        
        return min(confidence, 0.95) 