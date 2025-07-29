#!/usr/bin/env python3
"""
Product Navigator Agent - Fusion v14
Maps feature requirements, dev viability, edge cases, complexity scoring
"""

import asyncio
import time
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime

class ProductNavigatorAgent:
    """
    Product Navigator Agent - Fusion v14
    Maps feature requirements, dev viability, edge cases, complexity scoring
    """
    
    def __init__(self):
        self.logger = logging.getLogger("ProductNavigatorAgent")
        
        # Feature complexity levels
        self.complexity_levels = {
            "simple": {
                "score": 1,
                "description": "Basic functionality with minimal dependencies",
                "dev_time": "1-3 days",
                "risk_level": "low"
            },
            "medium": {
                "score": 2,
                "description": "Standard features with moderate complexity",
                "dev_time": "1-2 weeks",
                "risk_level": "medium"
            },
            "complex": {
                "score": 3,
                "description": "Advanced features with multiple integrations",
                "dev_time": "2-4 weeks",
                "risk_level": "high"
            },
            "expert": {
                "score": 4,
                "description": "Highly sophisticated features with custom logic",
                "dev_time": "1-2 months",
                "risk_level": "very_high"
            }
        }
        
        # Development viability factors
        self.viability_factors = {
            "technical_feasibility": ["api_availability", "framework_support", "performance_requirements"],
            "resource_availability": ["developer_skills", "time_constraints", "budget_limitations"],
            "business_impact": ["user_value", "revenue_potential", "market_demand"],
            "risk_assessment": ["security_concerns", "compliance_requirements", "scalability_needs"]
        }
        
        # Edge case categories
        self.edge_case_categories = {
            "user_experience": ["empty_states", "error_handling", "loading_states", "offline_behavior"],
            "data_handling": ["large_datasets", "data_validation", "caching_strategies", "sync_issues"],
            "performance": ["slow_networks", "memory_usage", "battery_consumption", "device_compatibility"],
            "security": ["input_validation", "authentication_edge_cases", "data_privacy", "xss_prevention"],
            "integration": ["api_failures", "third_party_dependencies", "version_compatibility", "rate_limiting"]
        }
        
        # Decision criteria weights
        self.decision_weights = {
            "technical_feasibility": 0.3,
            "business_value": 0.25,
            "development_effort": 0.2,
            "risk_level": 0.15,
            "user_impact": 0.1
        }
        
    async def run_async(self, prompt: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main async execution method for Product Navigator Agent
        """
        start_time = time.time()
        self.logger.info("Product Navigator Agent starting analysis")
        
        try:
            # Analyze feature requirements
            feature_analysis = await self._analyze_feature_requirements(prompt)
            
            # Assess development viability
            viability_assessment = await self._assess_development_viability(prompt, feature_analysis)
            
            # Identify edge cases
            edge_case_analysis = await self._identify_edge_cases(prompt, feature_analysis)
            
            # Calculate complexity score
            complexity_scoring = await self._calculate_complexity_score(prompt, feature_analysis, edge_case_analysis)
            
            # Generate decision recommendations
            decision_recommendations = await self._generate_decision_recommendations(prompt, feature_analysis, viability_assessment, complexity_scoring)
            
            # Create enhanced output
            enhanced_output = await self._create_enhanced_output(prompt, feature_analysis, viability_assessment, edge_case_analysis, complexity_scoring, decision_recommendations)
            
            execution_time = time.time() - start_time
            confidence = self._calculate_confidence(feature_analysis, viability_assessment, complexity_scoring)
            
            self.logger.info(f"Product Navigator Agent completed in {execution_time:.2f}s")
            
            return {
                "output": enhanced_output,
                "enhanced_output": enhanced_output,
                "confidence": confidence,
                "feature_analysis": feature_analysis,
                "viability_assessment": viability_assessment,
                "edge_case_analysis": edge_case_analysis,
                "complexity_scoring": complexity_scoring,
                "decision_recommendations": decision_recommendations,
                "execution_time": execution_time,
                "shared_state": {
                    "feature_type": feature_analysis.get("feature_type"),
                    "complexity_level": complexity_scoring.get("level"),
                    "viability_score": viability_assessment.get("overall_score"),
                    "edge_case_count": len(edge_case_analysis.get("identified_cases", [])),
                    "recommendation": decision_recommendations.get("primary_recommendation"),
                    "analysis_timestamp": datetime.now().timestamp()
                }
            }
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.error(f"Product Navigator Agent failed: {e}")
            return {
                "error": str(e),
                "confidence": 0.0,
                "execution_time": execution_time
            }
    
    async def _analyze_feature_requirements(self, prompt: str) -> Dict[str, Any]:
        """Analyze feature requirements from prompt"""
        
        # Detect feature type
        feature_type = self._detect_feature_type(prompt)
        
        # Extract functional requirements
        functional_requirements = self._extract_functional_requirements(prompt)
        
        # Identify technical dependencies
        technical_dependencies = self._identify_technical_dependencies(prompt)
        
        # Assess user impact
        user_impact = self._assess_user_impact(prompt)
        
        return {
            "feature_type": feature_type,
            "functional_requirements": functional_requirements,
            "technical_dependencies": technical_dependencies,
            "user_impact": user_impact,
            "business_context": self._extract_business_context(prompt)
        }
    
    async def _assess_development_viability(self, prompt: str, feature_analysis: Dict) -> Dict[str, Any]:
        """Assess development viability"""
        
        # Evaluate technical feasibility
        technical_feasibility = self._evaluate_technical_feasibility(prompt, feature_analysis)
        
        # Assess resource availability
        resource_availability = self._assess_resource_availability(prompt, feature_analysis)
        
        # Calculate business impact
        business_impact = self._calculate_business_impact(prompt, feature_analysis)
        
        # Evaluate risks
        risk_evaluation = self._evaluate_risks(prompt, feature_analysis)
        
        return {
            "technical_feasibility": technical_feasibility,
            "resource_availability": resource_availability,
            "business_impact": business_impact,
            "risk_evaluation": risk_evaluation,
            "overall_score": self._calculate_viability_score(technical_feasibility, resource_availability, business_impact, risk_evaluation)
        }
    
    async def _identify_edge_cases(self, prompt: str, feature_analysis: Dict) -> Dict[str, Any]:
        """Identify potential edge cases"""
        
        # Identify UX edge cases
        ux_edge_cases = self._identify_ux_edge_cases(prompt, feature_analysis)
        
        # Identify data handling edge cases
        data_edge_cases = self._identify_data_edge_cases(prompt, feature_analysis)
        
        # Identify performance edge cases
        performance_edge_cases = self._identify_performance_edge_cases(prompt, feature_analysis)
        
        # Identify security edge cases
        security_edge_cases = self._identify_security_edge_cases(prompt, feature_analysis)
        
        # Identify integration edge cases
        integration_edge_cases = self._identify_integration_edge_cases(prompt, feature_analysis)
        
        return {
            "identified_cases": {
                "user_experience": ux_edge_cases,
                "data_handling": data_edge_cases,
                "performance": performance_edge_cases,
                "security": security_edge_cases,
                "integration": integration_edge_cases
            },
            "total_edge_cases": len(ux_edge_cases) + len(data_edge_cases) + len(performance_edge_cases) + len(security_edge_cases) + len(integration_edge_cases),
            "critical_edge_cases": self._identify_critical_edge_cases(ux_edge_cases, data_edge_cases, performance_edge_cases, security_edge_cases, integration_edge_cases)
        }
    
    async def _calculate_complexity_score(self, prompt: str, feature_analysis: Dict, edge_case_analysis: Dict) -> Dict[str, Any]:
        """Calculate complexity score"""
        
        # Analyze complexity factors
        complexity_factors = self._analyze_complexity_factors(prompt, feature_analysis, edge_case_analysis)
        
        # Calculate weighted score
        weighted_score = self._calculate_weighted_complexity_score(complexity_factors)
        
        # Determine complexity level
        complexity_level = self._determine_complexity_level(weighted_score)
        
        # Estimate development effort
        development_effort = self._estimate_development_effort(complexity_level, feature_analysis)
        
        return {
            "factors": complexity_factors,
            "weighted_score": weighted_score,
            "level": complexity_level,
            "development_effort": development_effort,
            "risk_assessment": self._assess_complexity_risks(complexity_level, edge_case_analysis)
        }
    
    async def _generate_decision_recommendations(self, prompt: str, feature_analysis: Dict, viability_assessment: Dict, complexity_scoring: Dict) -> Dict[str, Any]:
        """Generate decision recommendations"""
        
        # Analyze decision factors
        decision_factors = self._analyze_decision_factors(feature_analysis, viability_assessment, complexity_scoring)
        
        # Generate primary recommendation
        primary_recommendation = self._generate_primary_recommendation(decision_factors)
        
        # Create alternative options
        alternative_options = self._create_alternative_options(decision_factors)
        
        # Generate implementation roadmap
        implementation_roadmap = self._generate_implementation_roadmap(primary_recommendation, complexity_scoring)
        
        return {
            "decision_factors": decision_factors,
            "primary_recommendation": primary_recommendation,
            "alternative_options": alternative_options,
            "implementation_roadmap": implementation_roadmap,
            "success_metrics": self._define_success_metrics(feature_analysis, primary_recommendation)
        }
    
    async def _create_enhanced_output(self, prompt: str, feature_analysis: Dict, viability_assessment: Dict, edge_case_analysis: Dict, complexity_scoring: Dict, decision_recommendations: Dict) -> str:
        """Create enhanced output with comprehensive analysis"""
        
        return f"""# Product Navigator Analysis & Recommendations

## Original Request
{prompt}

## Feature Analysis

### Feature Type
**Type:** {feature_analysis.get('feature_type', 'unknown')}
**User Impact:** {feature_analysis.get('user_impact', 'medium')}

### Functional Requirements
{', '.join(feature_analysis.get('functional_requirements', ['None detected']))}

### Technical Dependencies
{', '.join(feature_analysis.get('technical_dependencies', ['None detected']))}

## Development Viability

### Overall Viability Score
**Score:** {viability_assessment.get('overall_score', 0):.2f}/1.00

### Technical Feasibility
**Score:** {viability_assessment.get('technical_feasibility', {}).get('score', 0):.2f}/1.00
**Factors:** {', '.join(viability_assessment.get('technical_feasibility', {}).get('factors', ['None']))}

### Business Impact
**Score:** {viability_assessment.get('business_impact', {}).get('score', 0):.2f}/1.00
**Value:** {viability_assessment.get('business_impact', {}).get('value', 'medium')}

## Edge Case Analysis

### Identified Edge Cases
**Total:** {edge_case_analysis.get('total_edge_cases', 0)} cases
**Critical:** {len(edge_case_analysis.get('critical_edge_cases', []))} critical cases

### Categories
{self._format_edge_case_categories(edge_case_analysis.get('identified_cases', {}))}

## Complexity Assessment

### Complexity Level
**Level:** {complexity_scoring.get('level', 'unknown').upper()}
**Score:** {complexity_scoring.get('weighted_score', 0):.1f}/4.0
**Development Effort:** {complexity_scoring.get('development_effort', {}).get('estimate', 'Unknown')}

### Risk Assessment
**Risk Level:** {complexity_scoring.get('risk_assessment', {}).get('level', 'unknown')}
**Mitigation Strategies:** {', '.join(complexity_scoring.get('risk_assessment', {}).get('strategies', ['None']))}

## Decision Recommendations

### Primary Recommendation
**Recommendation:** {decision_recommendations.get('primary_recommendation', 'No recommendation')}
**Confidence:** {decision_recommendations.get('decision_factors', {}).get('confidence', 0):.2f}/1.00

### Alternative Options
{self._format_alternative_options(decision_recommendations.get('alternative_options', []))}

### Implementation Roadmap
{self._format_implementation_roadmap(decision_recommendations.get('implementation_roadmap', {}))}

### Success Metrics
{', '.join(decision_recommendations.get('success_metrics', ['None defined']))}

## Product Navigator Confidence
**Score:** {self._calculate_confidence(feature_analysis, viability_assessment, complexity_scoring):.2f}/1.00

*Generated by Fusion v14 Product Navigator Agent*"""
    
    def _detect_feature_type(self, prompt: str) -> str:
        """Detect feature type from prompt"""
        prompt_lower = prompt.lower()
        
        if "tracker" in prompt_lower or "tracking" in prompt_lower:
            return "tracking_feature"
        elif "dispute" in prompt_lower or "conflict" in prompt_lower:
            return "dispute_resolution"
        elif "payment" in prompt_lower or "billing" in prompt_lower:
            return "payment_feature"
        elif "notification" in prompt_lower or "alert" in prompt_lower:
            return "notification_system"
        elif "report" in prompt_lower or "analytics" in prompt_lower:
            return "reporting_feature"
        elif "search" in prompt_lower or "filter" in prompt_lower:
            return "search_feature"
        elif "integration" in prompt_lower or "api" in prompt_lower:
            return "integration_feature"
        else:
            return "custom_feature"
    
    def _extract_functional_requirements(self, prompt: str) -> List[str]:
        """Extract functional requirements from prompt"""
        requirements = []
        prompt_lower = prompt.lower()
        
        if "track" in prompt_lower:
            requirements.append("data_tracking")
            
        if "store" in prompt_lower or "save" in prompt_lower:
            requirements.append("data_persistence")
            
        if "display" in prompt_lower or "show" in prompt_lower:
            requirements.append("data_visualization")
            
        if "update" in prompt_lower or "modify" in prompt_lower:
            requirements.append("data_modification")
            
        if "search" in prompt_lower or "filter" in prompt_lower:
            requirements.append("data_filtering")
            
        if "export" in prompt_lower or "download" in prompt_lower:
            requirements.append("data_export")
            
        return requirements
    
    def _identify_technical_dependencies(self, prompt: str) -> List[str]:
        """Identify technical dependencies"""
        dependencies = []
        prompt_lower = prompt.lower()
        
        if "database" in prompt_lower or "storage" in prompt_lower:
            dependencies.append("database_system")
            
        if "api" in prompt_lower or "external" in prompt_lower:
            dependencies.append("external_apis")
            
        if "authentication" in prompt_lower or "login" in prompt_lower:
            dependencies.append("auth_system")
            
        if "real-time" in prompt_lower or "live" in prompt_lower:
            dependencies.append("real_time_system")
            
        if "mobile" in prompt_lower or "responsive" in prompt_lower:
            dependencies.append("mobile_support")
            
        return dependencies
    
    def _assess_user_impact(self, prompt: str) -> str:
        """Assess user impact level"""
        prompt_lower = prompt.lower()
        
        if any(word in prompt_lower for word in ["critical", "essential", "core"]):
            return "high"
        elif any(word in prompt_lower for word in ["important", "valuable", "useful"]):
            return "medium"
        else:
            return "low"
    
    def _extract_business_context(self, prompt: str) -> Dict[str, Any]:
        """Extract business context from prompt"""
        context = {}
        prompt_lower = prompt.lower()
        
        if "revenue" in prompt_lower or "profit" in prompt_lower:
            context["revenue_impact"] = "high"
            
        if "user" in prompt_lower or "customer" in prompt_lower:
            context["user_impact"] = "high"
            
        if "compliance" in prompt_lower or "legal" in prompt_lower:
            context["compliance_requirements"] = True
            
        return context
    
    def _evaluate_technical_feasibility(self, prompt: str, feature_analysis: Dict) -> Dict[str, Any]:
        """Evaluate technical feasibility"""
        factors = []
        score = 0.8  # Base score
        
        # Check for known technical challenges
        if "real-time" in prompt.lower():
            factors.append("real_time_synchronization")
            score -= 0.1
            
        if "large_data" in prompt.lower() or "scale" in prompt.lower():
            factors.append("scalability_requirements")
            score -= 0.1
            
        if "integration" in prompt.lower():
            factors.append("external_integration")
            score -= 0.05
            
        return {
            "score": max(score, 0.0),
            "factors": factors,
            "feasible": score > 0.6
        }
    
    def _assess_resource_availability(self, prompt: str, feature_analysis: Dict) -> Dict[str, Any]:
        """Assess resource availability"""
        return {
            "developer_availability": "high",
            "time_constraints": "medium",
            "budget_availability": "high",
            "skill_requirements": self._assess_skill_requirements(feature_analysis)
        }
    
    def _assess_skill_requirements(self, feature_analysis: Dict) -> str:
        """Assess required skills"""
        dependencies = feature_analysis.get("technical_dependencies", [])
        
        if "real_time_system" in dependencies:
            return "advanced"
        elif "external_apis" in dependencies:
            return "intermediate"
        else:
            return "basic"
    
    def _calculate_business_impact(self, prompt: str, feature_analysis: Dict) -> Dict[str, Any]:
        """Calculate business impact"""
        user_impact = feature_analysis.get("user_impact", "low")
        
        impact_scores = {
            "high": 0.9,
            "medium": 0.7,
            "low": 0.5
        }
        
        return {
            "score": impact_scores.get(user_impact, 0.5),
            "value": user_impact,
            "revenue_potential": "medium" if user_impact == "high" else "low"
        }
    
    def _evaluate_risks(self, prompt: str, feature_analysis: Dict) -> Dict[str, Any]:
        """Evaluate potential risks"""
        risks = []
        risk_level = "low"
        
        if "data" in prompt.lower():
            risks.append("data_security")
            risk_level = "medium"
            
        if "external" in prompt.lower() or "api" in prompt.lower():
            risks.append("external_dependencies")
            risk_level = "medium"
            
        if "real-time" in prompt.lower():
            risks.append("performance_risks")
            risk_level = "high"
            
        return {
            "identified_risks": risks,
            "risk_level": risk_level,
            "mitigation_strategies": self._generate_mitigation_strategies(risks)
        }
    
    def _generate_mitigation_strategies(self, risks: List[str]) -> List[str]:
        """Generate risk mitigation strategies"""
        strategies = []
        
        for risk in risks:
            if risk == "data_security":
                strategies.append("Implement proper data encryption and access controls")
            elif risk == "external_dependencies":
                strategies.append("Add fallback mechanisms and error handling")
            elif risk == "performance_risks":
                strategies.append("Implement caching and optimization strategies")
                
        return strategies
    
    def _calculate_viability_score(self, technical_feasibility: Dict, resource_availability: Dict, business_impact: Dict, risk_evaluation: Dict) -> float:
        """Calculate overall viability score"""
        scores = [
            technical_feasibility.get("score", 0.0),
            business_impact.get("score", 0.0),
            0.8 if resource_availability.get("developer_availability") == "high" else 0.5,
            0.9 if risk_evaluation.get("risk_level") == "low" else 0.6
        ]
        
        return sum(scores) / len(scores)
    
    def _identify_ux_edge_cases(self, prompt: str, feature_analysis: Dict) -> List[str]:
        """Identify UX edge cases"""
        cases = []
        prompt_lower = prompt.lower()
        
        if "data" in prompt_lower:
            cases.extend(["empty_state", "loading_state", "error_state"])
            
        if "user" in prompt_lower:
            cases.extend(["new_user_experience", "power_user_experience"])
            
        if "mobile" in prompt_lower:
            cases.extend(["small_screen_layout", "touch_interactions"])
            
        return cases
    
    def _identify_data_edge_cases(self, prompt: str, feature_analysis: Dict) -> List[str]:
        """Identify data handling edge cases"""
        cases = []
        prompt_lower = prompt.lower()
        
        if "track" in prompt_lower:
            cases.extend(["data_validation", "duplicate_entries", "data_corruption"])
            
        if "large" in prompt_lower or "many" in prompt_lower:
            cases.extend(["performance_with_large_datasets", "memory_usage"])
            
        if "sync" in prompt_lower or "real-time" in prompt_lower:
            cases.extend(["sync_conflicts", "offline_behavior", "data_consistency"])
            
        return cases
    
    def _identify_performance_edge_cases(self, prompt: str, feature_analysis: Dict) -> List[str]:
        """Identify performance edge cases"""
        cases = []
        prompt_lower = prompt.lower()
        
        cases.extend(["slow_network_conditions", "high_latency", "memory_leaks"])
        
        if "real-time" in prompt_lower:
            cases.extend(["real_time_performance", "concurrent_users"])
            
        if "large" in prompt_lower:
            cases.extend(["large_data_processing", "scalability_limits"])
            
        return cases
    
    def _identify_security_edge_cases(self, prompt: str, feature_analysis: Dict) -> List[str]:
        """Identify security edge cases"""
        cases = []
        prompt_lower = prompt.lower()
        
        if "data" in prompt_lower:
            cases.extend(["input_validation", "sql_injection", "xss_attacks"])
            
        if "user" in prompt_lower:
            cases.extend(["authentication_bypass", "session_management", "privilege_escalation"])
            
        if "external" in prompt_lower:
            cases.extend(["api_security", "data_transmission_security"])
            
        return cases
    
    def _identify_integration_edge_cases(self, prompt: str, feature_analysis: Dict) -> List[str]:
        """Identify integration edge cases"""
        cases = []
        prompt_lower = prompt.lower()
        
        if "api" in prompt_lower or "external" in prompt_lower:
            cases.extend(["api_failures", "rate_limiting", "version_compatibility"])
            
        if "third-party" in prompt_lower:
            cases.extend(["dependency_failures", "service_outages"])
            
        return cases
    
    def _identify_critical_edge_cases(self, ux_cases: List[str], data_cases: List[str], performance_cases: List[str], security_cases: List[str], integration_cases: List[str]) -> List[str]:
        """Identify critical edge cases"""
        critical_cases = []
        
        # Security cases are always critical
        critical_cases.extend(security_cases)
        
        # Data corruption cases are critical
        if "data_corruption" in data_cases:
            critical_cases.append("data_corruption")
            
        # Performance cases that affect core functionality
        if "memory_leaks" in performance_cases:
            critical_cases.append("memory_leaks")
            
        return critical_cases
    
    def _analyze_complexity_factors(self, prompt: str, feature_analysis: Dict, edge_case_analysis: Dict) -> Dict[str, float]:
        """Analyze complexity factors"""
        factors = {
            "technical_complexity": 0.0,
            "integration_complexity": 0.0,
            "data_complexity": 0.0,
            "user_experience_complexity": 0.0,
            "security_complexity": 0.0
        }
        
        # Technical complexity
        dependencies = feature_analysis.get("technical_dependencies", [])
        if "real_time_system" in dependencies:
            factors["technical_complexity"] += 0.3
        if "external_apis" in dependencies:
            factors["integration_complexity"] += 0.2
            
        # Data complexity
        if "data_tracking" in feature_analysis.get("functional_requirements", []):
            factors["data_complexity"] += 0.2
            
        # Security complexity
        security_cases = edge_case_analysis.get("identified_cases", {}).get("security", [])
        if security_cases:
            factors["security_complexity"] += 0.2
            
        return factors
    
    def _calculate_weighted_complexity_score(self, factors: Dict[str, float]) -> float:
        """Calculate weighted complexity score"""
        weights = {
            "technical_complexity": 0.3,
            "integration_complexity": 0.25,
            "data_complexity": 0.2,
            "user_experience_complexity": 0.15,
            "security_complexity": 0.1
        }
        
        weighted_score = sum(factors[factor] * weights[factor] for factor in factors)
        return min(weighted_score, 4.0)
    
    def _determine_complexity_level(self, score: float) -> str:
        """Determine complexity level based on score"""
        if score <= 1.0:
            return "simple"
        elif score <= 2.0:
            return "medium"
        elif score <= 3.0:
            return "complex"
        else:
            return "expert"
    
    def _estimate_development_effort(self, complexity_level: str, feature_analysis: Dict) -> Dict[str, Any]:
        """Estimate development effort"""
        level_info = self.complexity_levels.get(complexity_level, self.complexity_levels["medium"])
        
        return {
            "estimate": level_info["dev_time"],
            "description": level_info["description"],
            "risk_level": level_info["risk_level"]
        }
    
    def _assess_complexity_risks(self, complexity_level: str, edge_case_analysis: Dict) -> Dict[str, Any]:
        """Assess risks based on complexity"""
        level_info = self.complexity_levels.get(complexity_level, self.complexity_levels["medium"])
        
        strategies = []
        if complexity_level in ["complex", "expert"]:
            strategies.extend([
                "Implement comprehensive testing strategy",
                "Add monitoring and alerting",
                "Plan for iterative development"
            ])
            
        return {
            "level": level_info["risk_level"],
            "strategies": strategies
        }
    
    def _analyze_decision_factors(self, feature_analysis: Dict, viability_assessment: Dict, complexity_scoring: Dict) -> Dict[str, Any]:
        """Analyze decision factors"""
        factors = {}
        
        # Technical feasibility
        factors["technical_feasibility"] = viability_assessment.get("technical_feasibility", {}).get("score", 0.0)
        
        # Business value
        factors["business_value"] = viability_assessment.get("business_impact", {}).get("score", 0.0)
        
        # Development effort
        complexity_score = complexity_scoring.get("weighted_score", 0.0)
        factors["development_effort"] = 1.0 - (complexity_score / 4.0)  # Invert for effort
        
        # Risk level
        risk_level = complexity_scoring.get("risk_assessment", {}).get("level", "low")
        risk_scores = {"low": 0.9, "medium": 0.7, "high": 0.5, "very_high": 0.3}
        factors["risk_level"] = risk_scores.get(risk_level, 0.7)
        
        # User impact
        user_impact = feature_analysis.get("user_impact", "low")
        impact_scores = {"high": 0.9, "medium": 0.7, "low": 0.5}
        factors["user_impact"] = impact_scores.get(user_impact, 0.5)
        
        return factors
    
    def _generate_primary_recommendation(self, decision_factors: Dict[str, Any]) -> str:
        """Generate primary recommendation"""
        # Calculate weighted score
        weighted_score = sum(
            decision_factors[factor] * self.decision_weights[factor]
            for factor in self.decision_weights
            if factor in decision_factors
        )
        
        if weighted_score > 0.8:
            return "Proceed with development"
        elif weighted_score > 0.6:
            return "Proceed with modifications"
        elif weighted_score > 0.4:
            return "Consider alternative approach"
        else:
            return "Reconsider or postpone"
    
    def _create_alternative_options(self, decision_factors: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Create alternative options"""
        options = []
        
        # Option 1: Simplified version
        if decision_factors.get("development_effort", 0.5) < 0.7:
            options.append({
                "name": "Simplified Version",
                "description": "Develop core functionality with reduced scope",
                "pros": ["Faster development", "Lower risk", "Easier testing"],
                "cons": ["Reduced functionality", "Limited user value"]
            })
            
        # Option 2: Phased approach
        options.append({
            "name": "Phased Development",
            "description": "Implement in stages with iterative releases",
            "pros": ["Manageable risk", "User feedback", "Flexible timeline"],
            "cons": ["Longer timeline", "Integration complexity"]
        })
        
        return options
    
    def _generate_implementation_roadmap(self, recommendation: str, complexity_scoring: Dict) -> Dict[str, Any]:
        """Generate implementation roadmap"""
        if recommendation == "Proceed with development":
            return {
                "phase_1": "Requirements gathering and technical design",
                "phase_2": "Core development and testing",
                "phase_3": "Integration and deployment",
                "timeline": complexity_scoring.get("development_effort", {}).get("estimate", "Unknown")
            }
        else:
            return {
                "phase_1": "Reassess requirements and constraints",
                "phase_2": "Develop alternative approach",
                "phase_3": "Implement with modifications",
                "timeline": "Extended timeline"
            }
    
    def _define_success_metrics(self, feature_analysis: Dict, recommendation: str) -> List[str]:
        """Define success metrics"""
        metrics = []
        
        if recommendation == "Proceed with development":
            metrics.extend([
                "Feature completion within timeline",
                "User adoption rate",
                "Performance benchmarks met",
                "Bug-free deployment"
            ])
        else:
            metrics.extend([
                "Risk mitigation success",
                "Alternative approach validation",
                "Cost-benefit analysis completion"
            ])
            
        return metrics
    
    def _format_edge_case_categories(self, identified_cases: Dict) -> str:
        """Format edge case categories for output"""
        formatted = []
        
        for category, cases in identified_cases.items():
            if cases:
                formatted.append(f"**{category.replace('_', ' ').title()}:** {', '.join(cases)}")
                
        return "\n".join(formatted) if formatted else "No edge cases identified"
    
    def _format_alternative_options(self, options: List[Dict]) -> str:
        """Format alternative options for output"""
        if not options:
            return "No alternative options available"
            
        formatted = []
        for option in options:
            formatted.append(f"**{option['name']}:** {option['description']}")
            formatted.append(f"  Pros: {', '.join(option['pros'])}")
            formatted.append(f"  Cons: {', '.join(option['cons'])}")
            formatted.append("")
            
        return "\n".join(formatted)
    
    def _format_implementation_roadmap(self, roadmap: Dict) -> str:
        """Format implementation roadmap for output"""
        if not roadmap:
            return "No roadmap available"
            
        formatted = []
        for phase, description in roadmap.items():
            if phase != "timeline":
                formatted.append(f"**{phase.replace('_', ' ').title()}:** {description}")
                
        formatted.append(f"**Timeline:** {roadmap.get('timeline', 'Unknown')}")
        
        return "\n".join(formatted)
    
    def _calculate_confidence(self, feature_analysis: Dict, viability_assessment: Dict, complexity_scoring: Dict) -> float:
        """Calculate confidence score"""
        base_confidence = 0.8
        
        # Boost for clear feature type
        if feature_analysis.get("feature_type") != "custom_feature":
            base_confidence += 0.05
            
        # Boost for high viability score
        viability_score = viability_assessment.get("overall_score", 0.0)
        if viability_score > 0.7:
            base_confidence += 0.05
            
        # Boost for reasonable complexity
        complexity_score = complexity_scoring.get("weighted_score", 0.0)
        if 1.0 <= complexity_score <= 3.0:
            base_confidence += 0.05
            
        return min(base_confidence, 0.95) 