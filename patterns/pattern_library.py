#!/usr/bin/env python3
"""
Pattern Library - Fusion v13.0
Central library of design and problem-solving patterns
"""

class PatternLibrary:
    def __init__(self):
        self.patterns = {
            "design_patterns": {
                "user_onboarding": {
                    "description": "Progressive disclosure of features",
                    "best_practices": [
                        "Start with core functionality",
                        "Provide immediate value",
                        "Guide users step-by-step"
                    ],
                    "examples": ["Slack", "Notion", "Figma"]
                },
                "data_visualization": {
                    "description": "Clear and intuitive data presentation",
                    "best_practices": [
                        "Use appropriate chart types",
                        "Provide context and labels",
                        "Enable interactivity"
                    ],
                    "examples": ["Tableau", "PowerBI", "Chart.js"]
                },
                "responsive_design": {
                    "description": "Adaptive layouts for all devices",
                    "best_practices": [
                        "Mobile-first approach",
                        "Flexible grids",
                        "Touch-friendly interactions"
                    ],
                    "examples": ["Bootstrap", "Material Design", "Tailwind"]
                }
            },
            "problem_solving_patterns": {
                "divide_and_conquer": {
                    "description": "Break complex problems into smaller parts",
                    "application": "System architecture, algorithm design",
                    "steps": [
                        "Identify sub-problems",
                        "Solve each independently",
                        "Combine solutions"
                    ]
                },
                "iterative_improvement": {
                    "description": "Continuous refinement through feedback",
                    "application": "Product development, user experience",
                    "steps": [
                        "Build initial version",
                        "Gather feedback",
                        "Iterate and improve"
                    ]
                },
                "pattern_matching": {
                    "description": "Recognize and apply known solutions",
                    "application": "Code reuse, design systems",
                    "steps": [
                        "Identify similar problems",
                        "Adapt existing solutions",
                        "Customize for context"
                    ]
                }
            }
        }
    
    def get_pattern(self, category, pattern_name):
        """Get a specific pattern by category and name"""
        if category in self.patterns and pattern_name in self.patterns[category]:
            return self.patterns[category][pattern_name]
        return None
    
    def list_patterns(self, category=None):
        """List all patterns or patterns in a category"""
        if category:
            return list(self.patterns.get(category, {}).keys())
        return {cat: list(patterns.keys()) for cat, patterns in self.patterns.items()}
    
    def apply_pattern(self, pattern_name, context):
        """Apply a pattern to a specific context"""
        pattern = self.get_pattern("design_patterns", pattern_name) or self.get_pattern("problem_solving_patterns", pattern_name)
        
        if pattern:
            return {
                "pattern_applied": pattern_name,
                "description": pattern["description"],
                "recommendations": pattern.get("best_practices", pattern.get("steps", [])),
                "context": context
            }
        return None
    
    def suggest_patterns(self, problem_description):
        """Suggest relevant patterns based on problem description"""
        suggestions = []
        
        for category, patterns in self.patterns.items():
            for pattern_name, pattern in patterns.items():
                if any(keyword in problem_description.lower() for keyword in pattern["description"].lower().split()):
                    suggestions.append({
                        "category": category,
                        "pattern": pattern_name,
                        "relevance": "high"
                    })
        
        return suggestions

# Example usage
if __name__ == "__main__":
    library = PatternLibrary()
    
    # Get a specific pattern
    onboarding_pattern = library.get_pattern("design_patterns", "user_onboarding")
    print("User Onboarding Pattern:", onboarding_pattern)
    
    # Apply a pattern
    result = library.apply_pattern("responsive_design", "Mobile app development")
    print("Applied Pattern:", result)
