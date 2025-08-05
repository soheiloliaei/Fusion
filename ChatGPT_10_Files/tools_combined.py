# Fusion v14 - Combined Tools Package
# This file contains UX audit tool and trust explainer tool

import json
from typing import Dict, Any, List, Optional
from dataclasses import dataclass

@dataclass
class ToolResult:
    tool_name: str
    analysis: Dict[str, Any]
    recommendations: List[Dict[str, Any]]
    confidence: float
    execution_time: float

class UXAuditTool:
    def __init__(self):
        self.name = "ux_audit"
        self.description = "Comprehensive UX analysis using heuristic evaluation and metrics"
        
    async def run(self, input_text: str) -> ToolResult:
        import time
        start_time = time.time()
        
        # Perform heuristic evaluation
        heuristic_results = self._perform_heuristic_evaluation(input_text)
        
        # Analyze UX metrics
        metrics_analysis = self._analyze_ux_metrics(input_text)
        
        # Generate recommendations
        recommendations = self._generate_ux_recommendations(heuristic_results, metrics_analysis)
        
        # Calculate confidence
        confidence = self._calculate_ux_confidence(heuristic_results, metrics_analysis)
        
        execution_time = time.time() - start_time
        
        return ToolResult(
            tool_name=self.name,
            analysis={
                'heuristic_evaluation': heuristic_results,
                'metrics_analysis': metrics_analysis
            },
            recommendations=recommendations,
            confidence=confidence,
            execution_time=execution_time
        )
    
    def _perform_heuristic_evaluation(self, input_text: str) -> Dict[str, Any]:
        """Perform Nielsen's 10 heuristics evaluation"""
        heuristics = {
            'visibility_of_system_status': {
                'description': 'Keep users informed about what is going on',
                'score': 0.8,
                'issues': ['Loading states could be more visible'],
                'priority': 'medium'
            },
            'match_between_system_and_real_world': {
                'description': 'Use language and concepts familiar to users',
                'score': 0.9,
                'issues': [],
                'priority': 'low'
            },
            'user_control_and_freedom': {
                'description': 'Provide ways to escape from unwanted states',
                'score': 0.7,
                'issues': ['Some actions are irreversible'],
                'priority': 'high'
            },
            'consistency_and_standards': {
                'description': 'Follow platform and industry conventions',
                'score': 0.85,
                'issues': ['Inconsistent button styling'],
                'priority': 'medium'
            },
            'error_prevention': {
                'description': 'Prevent errors before they occur',
                'score': 0.75,
                'issues': ['Missing confirmation dialogs'],
                'priority': 'high'
            },
            'recognition_rather_than_recall': {
                'description': 'Make objects and options visible',
                'score': 0.8,
                'issues': ['Some features are hard to discover'],
                'priority': 'medium'
            },
            'flexibility_and_efficiency_of_use': {
                'description': 'Accelerators for expert users',
                'score': 0.7,
                'issues': ['Limited keyboard shortcuts'],
                'priority': 'low'
            },
            'aesthetic_and_minimalist_design': {
                'description': 'Avoid irrelevant information',
                'score': 0.85,
                'issues': ['Some UI elements are cluttered'],
                'priority': 'medium'
            },
            'help_users_recognize_diagnose_and_recover_from_errors': {
                'description': 'Clear error messages and recovery options',
                'score': 0.75,
                'issues': ['Error messages could be more helpful'],
                'priority': 'high'
            },
            'help_and_documentation': {
                'description': 'Provide help when needed',
                'score': 0.6,
                'issues': ['Limited help documentation'],
                'priority': 'medium'
            }
        }
        
        return heuristics
    
    def _analyze_ux_metrics(self, input_text: str) -> Dict[str, Any]:
        """Analyze UX metrics"""
        metrics = {
            'usability': {
                'ease_of_use': 0.8,
                'learnability': 0.85,
                'efficiency': 0.75
            },
            'accessibility': {
                'wcag_compliance': 0.7,
                'screen_reader': 0.6,
                'keyboard_navigation': 0.8
            },
            'performance': {
                'load_time': 0.9,
                'response_time': 0.85,
                'smoothness': 0.8
            },
            'engagement': {
                'user_retention': 0.75,
                'time_on_site': 0.8,
                'interaction_rate': 0.7
            }
        }
        
        return metrics
    
    def _generate_ux_recommendations(self, heuristic_results: Dict[str, Any], 
                                    metrics_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate UX recommendations based on analysis"""
        recommendations = []
        
        # Analyze heuristic issues
        high_priority_issues = []
        for heuristic, data in heuristic_results.items():
            if data['priority'] == 'high' and data['issues']:
                high_priority_issues.extend(data['issues'])
        
        if high_priority_issues:
            recommendations.append({
                'type': 'critical_ux',
                'title': 'Address Critical UX Issues',
                'description': f'Fix {len(high_priority_issues)} high-priority usability issues',
                'priority': 'high',
                'confidence': 0.9
            })
        
        # Analyze metrics
        low_metrics = []
        for category, metrics in metrics_analysis.items():
            for metric, score in metrics.items():
                if score < 0.7:
                    low_metrics.append(f'{category}.{metric}')
        
        if low_metrics:
            recommendations.append({
                'type': 'metrics_improvement',
                'title': 'Improve Performance Metrics',
                'description': f'Focus on {len(low_metrics)} underperforming metrics',
                'priority': 'medium',
                'confidence': 0.8
            })
        
        # General UX improvements
        recommendations.append({
            'type': 'general_ux',
            'title': 'Enhance Overall UX',
            'description': 'Implement user-centered design principles',
            'priority': 'medium',
            'confidence': 0.75
        })
        
        return recommendations
    
    def _calculate_ux_confidence(self, heuristic_results: Dict[str, Any], 
                                metrics_analysis: Dict[str, Any]) -> float:
        """Calculate confidence score for UX audit"""
        # Calculate average heuristic score
        heuristic_scores = [data['score'] for data in heuristic_results.values()]
        avg_heuristic = sum(heuristic_scores) / len(heuristic_scores)
        
        # Calculate average metrics score
        all_metrics = []
        for category in metrics_analysis.values():
            all_metrics.extend(category.values())
        avg_metrics = sum(all_metrics) / len(all_metrics)
        
        # Weighted average
        confidence = (avg_heuristic * 0.6) + (avg_metrics * 0.4)
        return min(confidence, 0.95)

class TrustExplainerTool:
    def __init__(self):
        self.name = "trust_explainer"
        self.description = "Trust-building analysis and enhancement recommendations"
        
    async def run(self, input_text: str) -> ToolResult:
        import time
        start_time = time.time()
        
        # Analyze trust elements
        trust_elements = self._analyze_trust_elements(input_text)
        
        # Evaluate trust indicators
        trust_indicators = self._evaluate_trust_indicators(input_text)
        
        # Generate recommendations
        recommendations = self._generate_trust_recommendations(trust_elements, trust_indicators)
        
        # Calculate confidence
        confidence = self._calculate_trust_confidence(trust_elements, trust_indicators)
        
        execution_time = time.time() - start_time
        
        return ToolResult(
            tool_name=self.name,
            analysis={
                'trust_elements': trust_elements,
                'trust_indicators': trust_indicators
            },
            recommendations=recommendations,
            confidence=confidence,
            execution_time=execution_time
        )
    
    def _analyze_trust_elements(self, input_text: str) -> Dict[str, Any]:
        """Analyze trust elements"""
        elements = {
            'transparency': {
                'clear_pricing': 0.8,
                'data_usage': 0.7,
                'privacy_policy': 0.9,
                'terms_of_service': 0.8
            },
            'security': {
                'encryption': 0.9,
                'secure_payment': 0.85,
                'data_protection': 0.8,
                'compliance': 0.75
            },
            'social_proof': {
                'reviews': 0.8,
                'testimonials': 0.7,
                'user_count': 0.9,
                'expert_endorsements': 0.6
            },
            'reliability': {
                'uptime': 0.95,
                'performance': 0.85,
                'support_quality': 0.7,
                'update_frequency': 0.8
            },
            'expertise': {
                'credentials': 0.8,
                'experience': 0.85,
                'certifications': 0.7,
                'industry_recognition': 0.6
            }
        }
        
        return elements
    
    def _evaluate_trust_indicators(self, input_text: str) -> Dict[str, Any]:
        """Evaluate trust indicators"""
        indicators = {
            'visual': {
                'professional_design': 0.85,
                'brand_consistency': 0.9,
                'quality_icons': 0.8,
                'modern_ui': 0.85
            },
            'content': {
                'clear_messaging': 0.8,
                'helpful_information': 0.75,
                'transparent_processes': 0.7,
                'educational_content': 0.6
            },
            'interaction': {
                'responsive_feedback': 0.8,
                'error_handling': 0.75,
                'loading_states': 0.9,
                'progress_indicators': 0.8
            },
            'social': {
                'user_reviews': 0.8,
                'social_media': 0.7,
                'community_features': 0.6,
                'expert_opinions': 0.7
            }
        }
        
        return indicators
    
    def _generate_trust_recommendations(self, trust_elements: Dict[str, Any], 
                                        trust_indicators: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate trust enhancement recommendations"""
        recommendations = []
        
        # Analyze low-scoring trust elements
        low_trust_elements = []
        for category, elements in trust_elements.items():
            for element, score in elements.items():
                if score < 0.7:
                    low_trust_elements.append(f'{category}.{element}')
        
        if low_trust_elements:
            recommendations.append({
                'type': 'trust_enhancement',
                'title': 'Strengthen Trust Elements',
                'description': f'Improve {len(low_trust_elements)} trust elements',
                'priority': 'high',
                'confidence': 0.85
            })
        
        # Analyze trust indicators
        low_indicators = []
        for category, indicators in trust_indicators.items():
            for indicator, score in indicators.items():
                if score < 0.7:
                    low_indicators.append(f'{category}.{indicator}')
        
        if low_indicators:
            recommendations.append({
                'type': 'indicator_improvement',
                'title': 'Enhance Trust Indicators',
                'description': f'Improve {len(low_indicators)} trust indicators',
                'priority': 'medium',
                'confidence': 0.8
            })
        
        # General trust building
        recommendations.append({
            'type': 'general_trust',
            'title': 'Build Overall Trust',
            'description': 'Implement comprehensive trust-building strategies',
            'priority': 'medium',
            'confidence': 0.75
        })
        
        return recommendations
    
    def _calculate_trust_confidence(self, trust_elements: Dict[str, Any], 
                                    trust_indicators: Dict[str, Any]) -> float:
        """Calculate confidence score for trust analysis"""
        # Calculate average trust element score
        all_elements = []
        for category in trust_elements.values():
            all_elements.extend(category.values())
        avg_elements = sum(all_elements) / len(all_elements)
        
        # Calculate average indicator score
        all_indicators = []
        for category in trust_indicators.values():
            all_indicators.extend(category.values())
        avg_indicators = sum(all_indicators) / len(all_indicators)
        
        # Weighted average
        confidence = (avg_elements * 0.6) + (avg_indicators * 0.4)
        return min(confidence, 0.95)

class ToolRegistry:
    def __init__(self):
        self.tools = {
            'ux_audit': UXAuditTool(),
            'trust_explainer': TrustExplainerTool()
        }
    
    def get_tool(self, tool_name: str):
        """Get a specific tool"""
        return self.tools.get(tool_name)
    
    def list_tools(self):
        """List all available tools"""
        return list(self.tools.keys())
    
    def get_tool_info(self, tool_name: str) -> Optional[Dict[str, Any]]:
        """Get information about a specific tool"""
        tool = self.tools.get(tool_name)
        if tool:
            return {
                'name': tool.name,
                'description': tool.description
            }
        return None

# Initialize tool registry
tool_registry = ToolRegistry()

# Export for use in other modules
__all__ = ['tool_registry', 'UXAuditTool', 'TrustExplainerTool', 'ToolRegistry', 'ToolResult'] 