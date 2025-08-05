#!/usr/bin/env python3
"""
PatternRefiner Agent - Fusion v15.2
Adjust fallback patterns over time based on telemetry data.
"""

import json
import os
import glob
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from collections import defaultdict

class PatternRefinerAgent:
    def __init__(self, telemetry_log_path: str = "fusion_telemetry", 
                 config_path: str = "fallback_trigger_config.json"):
        self.telemetry_path = telemetry_log_path
        self.config_path = config_path
        self.analysis_window_days = 7  # Analyze last 7 days
        
    def analyze_telemetry(self) -> Dict[str, Any]:
        """
        Analyze telemetry data to identify patterns that frequently failed.
        
        Returns:
            Dictionary with analysis results
        """
        analysis = {
            "underperforming_agents": [],
            "high_fallback_agents": [],
            "success_rate_by_agent": {},
            "common_failure_patterns": [],
            "recommendations": []
        }
        
        # Load telemetry files
        telemetry_files = glob.glob(f"{self.telemetry_path}/*.json")
        
        if not telemetry_files:
            print("⚠️ No telemetry files found for analysis")
            return analysis
        
        # Analyze each telemetry file
        all_events = []
        agent_stats = defaultdict(lambda: {
            "total_runs": 0,
            "successful_runs": 0,
            "fallback_count": 0,
            "avg_confidence": 0.0,
            "avg_execution_time": 0.0
        })
        
        cutoff_date = datetime.now() - timedelta(days=self.analysis_window_days)
        
        for file_path in telemetry_files:
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    
                # Filter events within analysis window
                for event in data.get("events", []):
                    event_time = datetime.fromisoformat(event.get("timestamp", ""))
                    if event_time >= cutoff_date:
                        all_events.append(event)
                        
                        agent_name = event.get("agent", "unknown")
                        agent_stats[agent_name]["total_runs"] += 1
                        
                        if event.get("success", True):
                            agent_stats[agent_name]["successful_runs"] += 1
                        
                        if event.get("fallback"):
                            agent_stats[agent_name]["fallback_count"] += 1
                        
                        # Update averages
                        confidence = event.get("confidence", 0.0)
                        execution_time = event.get("execution_time", 0.0)
                        
                        current_avg_conf = agent_stats[agent_name]["avg_confidence"]
                        current_avg_time = agent_stats[agent_name]["avg_execution_time"]
                        total_runs = agent_stats[agent_name]["total_runs"]
                        
                        agent_stats[agent_name]["avg_confidence"] = (
                            (current_avg_conf * (total_runs - 1) + confidence) / total_runs
                        )
                        agent_stats[agent_name]["avg_execution_time"] = (
                            (current_avg_time * (total_runs - 1) + execution_time) / total_runs
                        )
                        
            except Exception as e:
                print(f"⚠️ Error reading telemetry file {file_path}: {e}")
        
        # Calculate success rates and identify underperforming agents
        for agent_name, stats in agent_stats.items():
            if stats["total_runs"] > 0:
                success_rate = stats["successful_runs"] / stats["total_runs"]
                fallback_rate = stats["fallback_count"] / stats["total_runs"]
                
                agent_stats[agent_name]["success_rate"] = success_rate
                agent_stats[agent_name]["fallback_rate"] = fallback_rate
                
                # Identify underperforming agents
                if success_rate < 0.7:
                    analysis["underperforming_agents"].append({
                        "agent": agent_name,
                        "success_rate": success_rate,
                        "fallback_rate": fallback_rate,
                        "avg_confidence": stats["avg_confidence"]
                    })
                
                # Identify high fallback agents
                if fallback_rate > 0.3:
                    analysis["high_fallback_agents"].append({
                        "agent": agent_name,
                        "fallback_rate": fallback_rate,
                        "success_rate": success_rate
                    })
                
                analysis["success_rate_by_agent"][agent_name] = success_rate
        
        # Identify common failure patterns
        failure_patterns = defaultdict(int)
        for event in all_events:
            if not event.get("success", True):
                failure_type = event.get("fallback", "unknown_error")
                failure_patterns[failure_type] += 1
        
        analysis["common_failure_patterns"] = [
            {"pattern": pattern, "count": count}
            for pattern, count in failure_patterns.items()
        ]
        
        return analysis
    
    def suggest_updates(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Propose changes to fallback_trigger_config.json based on analysis.
        
        Args:
            analysis: Results from analyze_telemetry()
            
        Returns:
            Dictionary with suggested configuration updates
        """
        suggestions = {
            "agent_thresholds": {},
            "fallback_rules": {},
            "routing_improvements": {},
            "general_recommendations": []
        }
        
        # Adjust confidence thresholds for underperforming agents
        for agent_info in analysis["underperforming_agents"]:
            agent_name = agent_info["agent"]
            current_success_rate = agent_info["success_rate"]
            
            # Lower threshold for agents with low success rates
            if current_success_rate < 0.5:
                suggestions["agent_thresholds"][agent_name] = {
                    "confidence_threshold": 0.6,  # Lower threshold
                    "reason": f"Low success rate ({current_success_rate:.2%})"
                }
            elif current_success_rate < 0.7:
                suggestions["agent_thresholds"][agent_name] = {
                    "confidence_threshold": 0.75,  # Moderate threshold
                    "reason": f"Moderate success rate ({current_success_rate:.2%})"
                }
        
        # Improve fallback rules for high fallback agents
        for agent_info in analysis["high_fallback_agents"]:
            agent_name = agent_info["agent"]
            fallback_rate = agent_info["fallback_rate"]
            
            suggestions["fallback_rules"][agent_name] = {
                "max_retries": 2,  # Reduce retries
                "fallback_agent": "evaluator",  # Use evaluator as fallback
                "reason": f"High fallback rate ({fallback_rate:.2%})"
            }
        
        # Routing improvements based on success rates
        success_rates = analysis["success_rate_by_agent"]
        if success_rates:
            # Find best performing agents
            best_agents = sorted(success_rates.items(), key=lambda x: x[1], reverse=True)[:5]
            
            suggestions["routing_improvements"] = {
                "primary_agents": [agent for agent, rate in best_agents if rate > 0.8],
                "secondary_agents": [agent for agent, rate in best_agents if 0.6 <= rate <= 0.8],
                "fallback_agents": [agent for agent, rate in success_rates.items() if rate < 0.6]
            }
        
        # General recommendations
        if analysis["underperforming_agents"]:
            suggestions["general_recommendations"].append(
                "Consider retraining or updating underperforming agents"
            )
        
        if analysis["high_fallback_agents"]:
            suggestions["general_recommendations"].append(
                "Review and optimize fallback chains for high-fallback agents"
            )
        
        if analysis["common_failure_patterns"]:
            suggestions["general_recommendations"].append(
                "Investigate common failure patterns and implement preventive measures"
            )
        
        return suggestions
    
    def apply_suggestions(self, suggestions: Dict[str, Any]) -> bool:
        """
        Apply suggested updates to the configuration file.
        
        Args:
            suggestions: Suggested updates from suggest_updates()
            
        Returns:
            True if successfully applied, False otherwise
        """
        try:
            # Load current config
            current_config = {}
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r') as f:
                    current_config = json.load(f)
            
            # Apply agent threshold updates
            if "agent_thresholds" in suggestions:
                if "agents" not in current_config:
                    current_config["agents"] = {}
                
                for agent_name, threshold_info in suggestions["agent_thresholds"].items():
                    if agent_name not in current_config["agents"]:
                        current_config["agents"][agent_name] = {}
                    
                    current_config["agents"][agent_name]["confidence_threshold"] = threshold_info["confidence_threshold"]
                    current_config["agents"][agent_name]["update_reason"] = threshold_info["reason"]
            
            # Apply fallback rule updates
            if "fallback_rules" in suggestions:
                if "fallback_rules" not in current_config:
                    current_config["fallback_rules"] = {}
                
                for agent_name, rule_info in suggestions["fallback_rules"].items():
                    current_config["fallback_rules"][agent_name] = rule_info
            
            # Apply routing improvements
            if "routing_improvements" in suggestions:
                current_config["routing_improvements"] = suggestions["routing_improvements"]
            
            # Save updated config
            with open(self.config_path, 'w') as f:
                json.dump(current_config, f, indent=2)
            
            print(f"✅ Applied configuration updates to {self.config_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error applying suggestions: {e}")
            return False
    
    def run_daily_analysis(self) -> Dict[str, Any]:
        """
        Run daily pattern analysis and apply updates.
        
        Returns:
            Dictionary with analysis results and applied changes
        """
        print("🔍 Running daily pattern analysis...")
        
        # Analyze telemetry
        analysis = self.analyze_telemetry()
        
        # Generate suggestions
        suggestions = self.suggest_updates(analysis)
        
        # Apply suggestions
        applied = self.apply_suggestions(suggestions)
        
        return {
            "analysis": analysis,
            "suggestions": suggestions,
            "applied": applied,
            "timestamp": datetime.now().isoformat()
        }

# Example usage
def main():
    """Example of using PatternRefinerAgent."""
    refiner = PatternRefinerAgent()
    
    # Run daily analysis
    results = refiner.run_daily_analysis()
    
    print("📊 Analysis Results:")
    print(f"Underperforming agents: {len(results['analysis']['underperforming_agents'])}")
    print(f"High fallback agents: {len(results['analysis']['high_fallback_agents'])}")
    print(f"Suggestions applied: {results['applied']}")

if __name__ == "__main__":
    main() 