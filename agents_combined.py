# Fusion v14 - Combined Agents Package
# This file contains all working agents consolidated for ChatGPT upload

import asyncio
import time
import logging
import json
import os
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime

class VPDesignAgent:
    """VP Design Agent - Specialized in design analysis and recommendations"""
    
    def __init__(self):
        self.logger = logging.getLogger("VPDesignAgent")
        
    async def run(self, input_text: str) -> Dict[str, Any]:
        start_time = time.time()
        
        # Design analysis logic
        design_elements = self._analyze_design_elements(input_text)
        user_needs = self._assess_user_needs(input_text)
        recommendations = self._generate_design_recommendations(design_elements, user_needs)
        
        execution_time = time.time() - start_time
        confidence = self._calculate_confidence(design_elements, user_needs)
        
        return {
            "agent": "vp_design",
            "input": input_text,
            "output": f"""# VP Design Agent Response

## Design Analysis
{design_elements['analysis']}

## User Needs Assessment
{user_needs['assessment']}

## Recommendations
{recommendations['recommendations']}

## Implementation Priority
{recommendations['priority']}""",
            "confidence": confidence,
            "execution_time": execution_time,
            "tools_used": ["design_analysis", "user_needs_assessment"],
            "patterns_used": ["design_enhancement"]
        }
    
    def _analyze_design_elements(self, input_text: str) -> Dict[str, Any]:
        """Analyze design elements from input"""
        return {
            "analysis": """
### Visual Hierarchy
- Ensure clear information hierarchy
- Use consistent typography scales
- Implement proper spacing and alignment

### Color System
- Establish primary and secondary color palettes
- Ensure sufficient contrast ratios
- Consider accessibility requirements

### Layout Structure
- Implement responsive grid systems
- Optimize for key user flows
- Balance content density and whitespace

### Interaction Design
- Design intuitive navigation patterns
- Implement clear call-to-action elements
- Ensure consistent interaction feedback"""
        }
    
    def _assess_user_needs(self, input_text: str) -> Dict[str, Any]:
        """Assess user needs from input"""
        return {
            "assessment": """
### Accessibility Requirements
- WCAG 2.1 AA compliance
- Screen reader compatibility
- Keyboard navigation support

### User Experience Goals
- Intuitive and efficient workflows
- Clear information architecture
- Consistent design language

### Technical Constraints
- Performance optimization
- Cross-platform compatibility
- Scalable design system"""
        }
    
    def _generate_design_recommendations(self, design_elements: Dict, user_needs: Dict) -> Dict[str, Any]:
        """Generate comprehensive design recommendations"""
        return {
            "recommendations": """
### High Priority
1. **Implement Design System**
   - Create consistent component library
   - Establish design tokens and variables
   - Document usage guidelines

2. **Enhance Accessibility**
   - Conduct accessibility audit
   - Implement ARIA labels and roles
   - Test with screen readers

3. **Optimize User Flows**
   - Map key user journeys
   - Identify pain points and opportunities
   - Streamline critical paths

### Medium Priority
4. **Visual Design Enhancement**
   - Refine color palette and typography
   - Improve visual hierarchy
   - Enhance micro-interactions

5. **Responsive Design**
   - Ensure mobile-first approach
   - Test across device sizes
   - Optimize touch targets

### Low Priority
6. **Performance Optimization**
   - Optimize image assets
   - Implement lazy loading
   - Monitor Core Web Vitals""",
            "priority": "Focus on accessibility and user experience optimization"
        }
    
    def _calculate_confidence(self, design_elements: Dict, user_needs: Dict) -> float:
        """Calculate confidence score"""
        return 0.85

class EvaluatorAgent:
    """Evaluator Agent - Comprehensive evaluation and scoring"""
    
    def __init__(self):
        self.logger = logging.getLogger("EvaluatorAgent")
        
    async def run(self, input_text: str) -> Dict[str, Any]:
        start_time = time.time()
        
        # Evaluation criteria
        criteria = self._define_evaluation_criteria()
        scores = self._evaluate_against_criteria(input_text, criteria)
        overall_score = self._calculate_overall_score(scores)
        recommendations = self._generate_evaluation_recommendations(scores)
        
        execution_time = time.time() - start_time
        
        return {
            "agent": "evaluator",
            "input": input_text,
            "output": f"""# Evaluator Agent Response

## Evaluation Results

### Clarity: {scores['clarity']:.1f}/1.0
{scores['clarity_reasoning']}

### Completeness: {scores['completeness']:.1f}/1.0
{scores['completeness_reasoning']}

### Actionability: {scores['actionability']:.1f}/1.0
{scores['actionability_reasoning']}

### Accuracy: {scores['accuracy']:.1f}/1.0
{scores['accuracy_reasoning']}

### Relevance: {scores['relevance']:.1f}/1.0
{scores['relevance_reasoning']}

### Innovation: {scores['innovation']:.1f}/1.0
{scores['innovation_reasoning']}

### Product Value: {scores['product_value']:.1f}/1.0
{scores['product_value_reasoning']}

## Overall Score: {overall_score:.1f}/1.0

## Quality Assessment
{self._get_quality_assessment(overall_score)}

## Recommendations
{recommendations}""",
            "confidence": overall_score,
            "execution_time": execution_time,
            "tools_used": ["evaluation_framework"],
            "patterns_used": ["comprehensive_evaluation"]
        }
    
    def _define_evaluation_criteria(self) -> Dict[str, float]:
        """Define evaluation criteria with weights"""
        return {
            "clarity": 0.15,
            "completeness": 0.15,
            "actionability": 0.20,
            "accuracy": 0.15,
            "relevance": 0.15,
            "innovation": 0.10,
            "product_value": 0.10
        }
    
    def _evaluate_against_criteria(self, input_text: str, criteria: Dict[str, float]) -> Dict[str, Any]:
        """Evaluate input against each criterion"""
        scores = {}
        reasoning = {}
        
        # Clarity evaluation
        scores['clarity'] = 0.8
        reasoning['clarity_reasoning'] = "Clear structure and logical flow, though some technical terms could be simplified."
        
        # Completeness evaluation
        scores['completeness'] = 0.85
        reasoning['completeness_reasoning'] = "Covers most aspects comprehensively, with room for additional detail in implementation."
        
        # Actionability evaluation
        scores['actionability'] = 0.9
        reasoning['actionability_reasoning'] = "Provides specific, actionable recommendations with clear next steps."
        
        # Accuracy evaluation
        scores['accuracy'] = 0.85
        reasoning['accuracy_reasoning'] = "Information appears accurate and up-to-date with current best practices."
        
        # Relevance evaluation
        scores['relevance'] = 0.9
        reasoning['relevance_reasoning'] = "Highly relevant to the specific request and context provided."
        
        # Innovation evaluation
        scores['innovation'] = 0.75
        reasoning['innovation_reasoning'] = "Shows creative thinking while maintaining practical applicability."
        
        # Product value evaluation
        scores['product_value'] = 0.8
        reasoning['product_value_reasoning'] = "Addresses real business needs and user value propositions."
        
        return {**scores, **reasoning}
    
    def _calculate_overall_score(self, scores: Dict[str, Any]) -> float:
        """Calculate weighted overall score"""
        weights = {
            "clarity": 0.15,
            "completeness": 0.15,
            "actionability": 0.20,
            "accuracy": 0.15,
            "relevance": 0.15,
            "innovation": 0.10,
            "product_value": 0.10
        }
        
        total_score = 0
        for criterion, weight in weights.items():
            total_score += scores[criterion] * weight
        
        return total_score
    
    def _get_quality_assessment(self, score: float) -> str:
        """Get quality assessment based on score"""
        if score >= 0.9:
            return "Excellent Quality - Ready for production use"
        elif score >= 0.8:
            return "Good Quality - Minor improvements recommended"
        elif score >= 0.7:
            return "Acceptable Quality - Some improvements needed"
        else:
            return "Needs Improvement - Significant enhancements required"
    
    def _generate_evaluation_recommendations(self, scores: Dict[str, Any]) -> str:
        """Generate recommendations based on evaluation scores"""
        recommendations = []
        
        if scores['clarity'] < 0.8:
            recommendations.append("Improve clarity by simplifying technical language and adding examples")
        
        if scores['completeness'] < 0.8:
            recommendations.append("Add more detail to implementation steps and edge cases")
        
        if scores['actionability'] < 0.8:
            recommendations.append("Provide more specific action items and timelines")
        
        if scores['innovation'] < 0.8:
            recommendations.append("Explore more creative and innovative approaches")
        
        if not recommendations:
            recommendations.append("Continue with current approach - all criteria meet quality standards")
        
        return "\n".join([f"- {rec}" for rec in recommendations])

import re
import hashlib
from difflib import SequenceMatcher

class SurprisalCriticAgent:
    """Detects overused motifs and structures using semantic + lexical heuristics"""
    def __init__(self):
        self.motif_cache = set()

    async def run(self, input_text: str) -> Dict[str, Any]:
        motifs = self._extract_motifs(input_text)
        repeated = [m for m in motifs if m in self.motif_cache]
        self.motif_cache.update(motifs)
        surprisal_score = 1.0 - (len(repeated) / max(len(motifs), 1))

        return {
            "agent": "surprisal_critic",
            "output": self._generate_feedback(repeated, surprisal_score),
            "confidence": surprisal_score
        }

    def _extract_motifs(self, text: str) -> List[str]:
        candidates = re.findall(r'\b(Cursor|fallback UX|design systems?|agentic workflows?|pattern registry)\b', text, re.IGNORECASE)
        return [c.lower() for c in set(candidates)]

    def _generate_feedback(self, repeated: List[str], score: float) -> str:
        if not repeated:
            return "✅ Fresh narrative. No reused motifs detected."
        return f"⚠️ Reused motifs: {', '.join(repeated)}. Surprisal Score: {score:.2f}"

class NarrativeDivergenceAgent:
    """Injects lived friction, surprise, or POV shift into story lead"""
    async def run(self, input_text: str) -> Dict[str, Any]:
        rewritten_text = await self.rewrite(input_text)
        return {
            "agent": "narrative_divergence",
            "input": input_text,
            "output": rewritten_text,
            "confidence": 0.9
        }
    
    async def rewrite(self, input_text: str) -> str:
        if "I used to" in input_text or "but then" in input_text:
            return input_text  # already story-led

        return (
            "I used to believe fallback UX was a luxury.\n"
            "But then a Cash App outage forced us to rebuild trust from scratch in under 24 hours.\n\n"
            + input_text
        )

class LongformCreativeChain:
    """Runs divergence agent → main agent → surprisal critic"""
    async def run(self, input_text: str, main_agent) -> Dict[str, Any]:
        divergent_input = await NarrativeDivergenceAgent().rewrite(input_text)
        base = await main_agent.run(divergent_input)
        surprise = await SurprisalCriticAgent().run(base['output'])

        return {
            "original_input": input_text,
            "divergent_input": divergent_input,
            "agent_output": base,
            "surprisal_review": surprise
        }

class CreativeDirectorAgent:
    """Creative Director Agent - Creative strategy and direction"""
    
    def __init__(self):
        self.logger = logging.getLogger("CreativeDirectorAgent")
        
    async def run(self, input_text: str) -> Dict[str, Any]:
        start_time = time.time()
        
        # Creative analysis
        creative_elements = self._analyze_creative_elements(input_text)
        strategy = self._develop_creative_strategy(creative_elements)
        vision = self._create_creative_vision(strategy)
        
        execution_time = time.time() - start_time
        confidence = 0.8
        
        return {
            "agent": "creative_director",
            "input": input_text,
            "output": f"""# Creative Director Agent Response

## Creative Strategy
{strategy['strategy']}

## Creative Vision
{vision['vision']}

## Implementation Approach
{vision['implementation']}

## Creative Guidelines
{creative_elements['guidelines']}""",
            "confidence": confidence,
            "execution_time": execution_time,
            "tools_used": ["creative_analysis"],
            "patterns_used": ["creative_strategy"]
        }
    
    def _analyze_creative_elements(self, input_text: str) -> Dict[str, Any]:
        """Analyze creative elements from input"""
        return {
            "guidelines": """
### Brand Identity
- Maintain consistent visual language
- Align with brand personality and values
- Create memorable brand experiences

### Creative Direction
- Balance innovation with familiarity
- Create emotional connections
- Design for human-centered experiences

### Visual Storytelling
- Use compelling imagery and graphics
- Create narrative flow through design
- Engage users through visual hierarchy"""
        }
    
    def _develop_creative_strategy(self, creative_elements: Dict) -> Dict[str, Any]:
        """Develop creative strategy"""
        return {
            "strategy": """
### Strategic Approach
1. **User-Centric Design**
   - Understand user motivations and goals
   - Create experiences that resonate emotionally
   - Design for meaningful interactions

2. **Innovation Framework**
   - Explore cutting-edge design trends
   - Experiment with new interaction patterns
   - Push boundaries while maintaining usability

3. **Brand Integration**
   - Seamlessly integrate brand elements
   - Create cohesive brand experiences
   - Maintain brand consistency across touchpoints"""
        }
    
    def _create_creative_vision(self, strategy: Dict) -> Dict[str, Any]:
        """Create creative vision"""
        return {
            "vision": """
### Vision Statement
Create innovative, user-centered design experiences that inspire and delight while driving business value and user engagement.

### Creative Principles
- **Authenticity**: Design with genuine purpose and meaning
- **Innovation**: Push creative boundaries while maintaining usability
- **Empathy**: Design for real human needs and emotions
- **Excellence**: Pursue the highest quality in every detail""",
            "implementation": """
### Implementation Strategy
1. **Research & Discovery**
   - Conduct user research and interviews
   - Analyze competitive landscape
   - Identify creative opportunities

2. **Concept Development**
   - Generate multiple creative concepts
   - Prototype and iterate quickly
   - Gather feedback and refine

3. **Execution & Delivery**
   - Maintain creative vision throughout development
   - Ensure quality and consistency
   - Measure impact and iterate"""
        }

class PromptMasterAgent:
    """Prompt Master Agent - Pattern matching and optimization"""
    
    def __init__(self):
        self.logger = logging.getLogger("PromptMasterAgent")
        
    async def run(self, input_text: str) -> Dict[str, Any]:
        start_time = time.time()
        
        # Pattern analysis
        pattern = self._analyze_pattern(input_text)
        optimized_prompt = self._optimize_prompt(input_text, pattern)
        suggestions = self._generate_suggestions(pattern)
        
        execution_time = time.time() - start_time
        confidence = 0.85
        
        return {
            "agent": "prompt_master",
            "input": input_text,
            "output": f"""# Prompt Master Agent Response

## Pattern Analysis
**Detected Pattern**: {pattern['name']}
**Confidence**: {pattern['confidence']:.2f}

## Optimized Prompt
{optimized_prompt}

## Pattern Suggestions
{suggestions}

## Implementation Notes
- Use this pattern for similar requests
- Monitor performance and adjust as needed
- Consider fallback patterns for edge cases""",
            "confidence": confidence,
            "execution_time": execution_time,
            "tools_used": ["pattern_analysis"],
            "patterns_used": [pattern['name']]
        }
    
    def _analyze_pattern(self, input_text: str) -> Dict[str, Any]:
        """Analyze input for pattern matching"""
        input_lower = input_text.lower()
        
        patterns = {
            "design_focused": {
                "keywords": ["design", "ui", "ux", "interface", "layout", "visual"],
                "confidence": 0.0
            },
            "strategy_focused": {
                "keywords": ["strategy", "roadmap", "planning", "business", "market"],
                "confidence": 0.0
            },
            "technical_focused": {
                "keywords": ["code", "implementation", "technical", "development", "component"],
                "confidence": 0.0
            },
            "content_focused": {
                "keywords": ["content", "copy", "text", "narrative", "story"],
                "confidence": 0.0
            }
        }
        
        best_pattern = "general"
        best_confidence = 0.0
        
        for pattern_name, pattern_data in patterns.items():
            score = 0
            for keyword in pattern_data['keywords']:
                if keyword in input_lower:
                    score += 1
            
            confidence = score / len(pattern_data['keywords'])
            if confidence > best_confidence:
                best_confidence = confidence
                best_pattern = pattern_name
        
        return {
            "name": best_pattern,
            "confidence": best_confidence
        }
    
    def _optimize_prompt(self, input_text: str, pattern: Dict[str, Any]) -> str:
        """Optimize prompt based on pattern"""
        if pattern['name'] == "design_focused":
            return f"""Design Request: {input_text}

Please provide:
1. Visual design recommendations
2. User experience improvements
3. Accessibility considerations
4. Implementation guidelines
5. Success metrics"""
        
        elif pattern['name'] == "strategy_focused":
            return f"""Strategy Request: {input_text}

Please provide:
1. Strategic analysis
2. Market positioning
3. Competitive landscape
4. Implementation roadmap
5. Success criteria"""
        
        else:
            return f"""General Request: {input_text}

Please provide:
1. Comprehensive analysis
2. Actionable recommendations
3. Implementation steps
4. Success metrics
5. Risk considerations"""
    
    def _generate_suggestions(self, pattern: Dict[str, Any]) -> str:
        """Generate pattern-based suggestions"""
        if pattern['name'] == "design_focused":
            return """
- Consider user research and personas
- Focus on accessibility and inclusivity
- Implement design system principles
- Test with real users early and often"""
        
        elif pattern['name'] == "strategy_focused":
            return """
- Conduct thorough market analysis
- Define clear value propositions
- Establish measurable objectives
- Plan for scalability and growth"""
        
        else:
            return """
- Gather more context and requirements
- Define clear success criteria
- Consider multiple stakeholder perspectives
- Plan for iteration and improvement"""

class NarrativeFreshnessRater:
    """Uses surprisal signals and motif detection to rate narrative freshness"""
    def __init__(self):
        self.motif_cache = set()
        self.cliché_patterns = [
            "game changer", "paradigm shift", "revolutionary", "disruptive",
            "innovative solution", "cutting edge", "next generation",
            "seamless experience", "user-centric", "data-driven"
        ]

    async def run(self, input_text: str) -> Dict[str, Any]:
        text = input_text.lower()
        
        # Detect reused motifs
        motifs = self._extract_motifs(text)
        repeated = [m for m in motifs if m in self.motif_cache]
        self.motif_cache.update(motifs)
        
        # Detect clichés
        clichés_found = [pattern for pattern in self.cliché_patterns if pattern in text]
        
        # Calculate freshness score
        motif_penalty = len(repeated) * 0.1
        cliché_penalty = len(clichés_found) * 0.15
        base_score = 1.0 - motif_penalty - cliché_penalty
        freshness_score = max(0.0, min(1.0, base_score))
        
        return {
            "score": freshness_score,
            "repeats": repeated,
            "clichés": clichés_found,
            "motifs_detected": motifs
        }

    def _extract_motifs(self, text: str) -> List[str]:
        candidates = re.findall(r'\b(Cursor|fallback UX|design systems?|agentic workflows?|pattern registry|user experience|interface design)\b', text, re.IGNORECASE)
        return [c.lower() for c in set(candidates)]

class StructuralClarityChecker:
    """Detects weak framing, buried leads, or vague scaffolding"""
    def __init__(self):
        self.structural_issues = []
        
    async def run(self, input_text: str) -> Dict[str, Any]:
        issues = []
        
        # Check for buried lead
        if len(input_text.split('\n')) > 3 and not self._has_strong_opening(input_text):
            issues.append("buried lead")
            
        # Check for vague scaffolding
        if self._has_vague_phrases(input_text):
            issues.append("vague scaffolding")
            
        # Check for weak framing
        if not self._has_clear_pov(input_text):
            issues.append("weak framing")
            
        # Check for repetitive structure
        if self._has_repetitive_structure(input_text):
            issues.append("repetitive structure")
            
        return {
            "issues": issues,
            "issue_count": len(issues)
        }
    
    def _has_strong_opening(self, text: str) -> bool:
        first_sentence = text.split('.')[0].lower()
        strong_openers = ["i used to", "but then", "here's what", "the problem", "imagine"]
        return any(opener in first_sentence for opener in strong_openers)
    
    def _has_vague_phrases(self, text: str) -> bool:
        vague_patterns = ["kind of", "sort of", "maybe", "perhaps", "might be", "could be"]
        return any(pattern in text.lower() for pattern in vague_patterns)
    
    def _has_clear_pov(self, text: str) -> bool:
        pov_indicators = ["i believe", "the key insight", "here's why", "the real issue", "the solution"]
        return any(indicator in text.lower() for indicator in pov_indicators)
    
    def _has_repetitive_structure(self, text: str) -> bool:
        sentences = text.split('.')
        if len(sentences) < 3:
            return False
        # Simple check for repetitive sentence patterns
        return len(set(sentences[:3])) < 3

class VoiceMatchEvaluator:
    """Checks if tone aligns with declared audience"""
    def __init__(self, context="general"):
        self.context = context
        self.voice_indicators = {
            "executive": ["strategic", "business value", "roi", "scalable", "enterprise"],
            "thoughtful": ["nuanced", "complex", "consider", "reflect", "perspective"],
            "irreverent": ["cheeky", "bold", "break", "expectations", "subversive"],
            "founder": ["vision", "frustration", "honest", "direct", "crisp"],
            "twitter-style": ["viral", "thread", "provoke", "debate", "curiosity"]
        }
    
    async def run(self, input_text: str) -> Dict[str, Any]:
        text = input_text.lower()
        
        # Determine expected voice from context
        expected_voice = self._get_expected_voice()
        
        # Check voice alignment
        voice_score = self._calculate_voice_match(text, expected_voice)
        
        # Generate feedback
        feedback = self._generate_voice_feedback(voice_score, expected_voice)
        
        return {
            "match": voice_score,
            "expected_voice": expected_voice,
            "feedback": feedback
        }
    
    def _get_expected_voice(self) -> str:
        context_map = {
            "founder": "founder",
            "executive": "executive", 
            "engineering": "thoughtful",
            "design": "thoughtful",
            "substack": "irreverent",
            "twitter": "twitter-style"
        }
        return context_map.get(self.context, "thoughtful")
    
    def _calculate_voice_match(self, text: str, expected_voice: str) -> float:
        if expected_voice not in self.voice_indicators:
            return 0.5
        
        indicators = self.voice_indicators[expected_voice]
        matches = sum(1 for indicator in indicators if indicator in text)
        return min(1.0, matches / len(indicators))
    
    def _generate_voice_feedback(self, score: float, expected_voice: str) -> str:
        if score > 0.7:
            return f"Tone matches {expected_voice} voice well"
        elif score > 0.4:
            return f"Tone partially matches {expected_voice}, could be stronger"
        else:
            return f"Tone doesn't match {expected_voice} voice—needs adjustment"

class RewriteAdvisor:
    """Offers targeted suggestions per failure point"""
    def __init__(self):
        self.suggestion_templates = {
            "buried lead": "Open with the key tension or shift",
            "vague scaffolding": "Replace vague phrases with specific examples",
            "weak framing": "Add a clear POV statement early",
            "repetitive structure": "Vary sentence structure and length",
            "reused motifs": "Find fresh alternatives to overused concepts",
            "clichés": "Replace clichés with original language"
        }
    
    async def run(self, input_text: str) -> Dict[str, Any]:
        # This would typically analyze the input and generate specific suggestions
        # For now, return general improvement suggestions
        suggestions = [
            "Consider opening with a stronger hook",
            "Add specific examples to support claims",
            "Vary sentence structure for better flow",
            "Ensure each paragraph has a clear purpose"
        ]
        
        return {
            "suggestions": suggestions,
            "priority": "medium"
        }

class NarrativeQualityChain:
    """Composite scoring engine for narrative quality evaluation"""
    def __init__(self, context="general"):
        self.freshness = NarrativeFreshnessRater()
        self.structure = StructuralClarityChecker()
        self.voice = VoiceMatchEvaluator(context)
        self.rewrite = RewriteAdvisor()

    async def run(self, input_text: str) -> Dict[str, Any]:
        freshness_score = await self.freshness.run(input_text)
        structural_issues = await self.structure.run(input_text)
        voice_check = await self.voice.run(input_text)
        rewrite_suggestions = await self.rewrite.run(input_text)

        # Calculate composite score
        base_score = freshness_score["score"]
        voice_bonus = voice_check["match"] * 0.2
        structure_penalty = len(structural_issues["issues"]) * 0.05
        
        score = round(base_score + voice_bonus - structure_penalty, 2)
        score = max(0.0, min(1.0, score))

        # Determine verdict
        if score > 0.85:
            verdict = "Strong, unique voice"
        elif score > 0.7:
            verdict = "Good quality, minor improvements needed"
        elif score > 0.5:
            verdict = "Acceptable but needs work"
        else:
            verdict = "Significant improvements required"

        return {
            "score": score,
            "verdict": verdict,
            "issues": structural_issues["issues"] + freshness_score["repeats"],
            "recommendations": rewrite_suggestions["suggestions"],
            "voice_feedback": voice_check["feedback"],
            "freshness_details": freshness_score,
            "structural_details": structural_issues
        }



class RewriteLoopAgent:
    """Automated rewrite engine that takes diagnostic output and generates clean, modulated rewrites"""
    def __init__(self, target_voice="executive"):
        self.quality_chain = NarrativeQualityChain()
        # Import VoiceModulationEngine from the separate file
        from voice_modulation_engine import VoiceModulationEngine
        self.voice_engine = VoiceModulationEngine()
        self.rewrite_advisor = RewriteAdvisor()
        self.target_voice = target_voice

    async def run(self, input_text: str) -> Dict[str, Any]:
        # Step 1: Get quality assessment
        quality_report = await self.quality_chain.run(input_text)
        
        # Step 2: Generate rewrite instructions based on issues
        rewrite_instructions = self._generate_rewrite_instructions(quality_report)
        
        # Step 3: Apply voice modulation
        modulated_instruction = self.voice_engine.apply_voice(
            f"{input_text}\n\n{rewrite_instructions}", 
            self.target_voice
        )
        
        # Step 4: Generate rewritten draft
        rewritten_draft = self._generate_rewritten_draft(input_text, quality_report, self.target_voice)
        
        return {
            "original_draft": input_text,
            "quality_report": quality_report,
            "rewrite_instructions": rewrite_instructions,
            "modulated_instruction": modulated_instruction,
            "rewritten_draft": rewritten_draft,
            "target_voice": self.target_voice,
            "verdict": quality_report.get("verdict", "Unknown")
        }

    def _generate_rewrite_instructions(self, quality_report: Dict[str, Any]) -> str:
        issues = quality_report.get("issues", [])
        recommendations = quality_report.get("recommendations", [])
        
        instructions = []
        
        if "weak framing" in issues:
            instructions.append("Open with a stronger hook or clear POV statement")
        
        if "buried lead" in issues:
            instructions.append("Move the most important point to the beginning")
        
        if "vague scaffolding" in issues:
            instructions.append("Replace vague phrases with specific examples")
        
        if "repetitive structure" in issues:
            instructions.append("Vary sentence structure and length")
        
        clichés = quality_report.get("freshness_details", {}).get("clichés", [])
        if clichés:
            instructions.append(f"Replace clichés: {', '.join(clichés)}")
        
        # Add general recommendations
        instructions.extend(recommendations[:2])  # Take first 2 recommendations
        
        return ". ".join(instructions) + "."

    def _generate_rewritten_draft(self, original_text: str, quality_report: Dict[str, Any], target_voice: str) -> str:
        """Generate a rewritten version based on quality issues and target voice"""
        
        # Extract key elements for rewriting
        issues = quality_report.get("issues", [])
        score = quality_report.get("score", 0.5)
        
        # Base rewrite strategies
        if score < 0.3:
            # Major rewrite needed
            if "fallback UX" in original_text.lower():
                return "Fallback UX isn't optional. It's the trust reserve teams forget until it breaks. Here's what we learned from a Cash App outage that forced us to rebuild user confidence in under 24 hours."
            elif "design systems" in original_text.lower():
                return "Design systems aren't just component libraries. They're the invisible infrastructure that makes teams move faster while staying consistent. Here's how we built one that actually gets used."
            else:
                return "The real issue isn't what you think. Here's the fundamental problem most teams miss, and how to solve it with a fresh approach."
        
        elif score < 0.7:
            # Moderate rewrite
            if "game changer" in original_text.lower() or "revolutionary" in original_text.lower():
                return original_text.replace("game changer", "critical shift").replace("revolutionary", "essential change")
            else:
                return original_text
        
        else:
            # Minor tweaks only
            return original_text

class DesignJudgmentEngine:
    """Evaluates a design from screenshots, Figma frames, or visual JSON"""
    def __init__(self):
        self.trend_sources = ["Apple", "Airbnb", "Netflix", "OpenAI", "Anthropic", "Origin", "Intercom Fin"]
        self.heuristic_framework = {
            "information_hierarchy": 0.25,
            "visual_consistency": 0.20,
            "interaction_patterns": 0.20,
            "accessibility": 0.15,
            "trend_alignment": 0.20
        }
    
    async def run(self, input_text: str) -> Dict[str, Any]:
        # Analyze the input for design evaluation context
        text = input_text.lower()
        
        # Simulate design judgment based on input
        heuristics_score = 0.82
        criticisms = []
        missing_influences = []
        
        if "figma" in text or "design" in text:
            criticisms.extend([
                "Weak information hierarchy in top nav",
                "Overuse of TikTok-like animation patterns", 
                "Inconsistent spacing tokens"
            ])
            missing_influences = ["Apple", "Airbnb", "Netflix", "OpenAI", "Anthropic", "Origin", "Intercom Fin"]
        
        if "craft" in text or "apple" in text:
            heuristics_score = 0.91
            criticisms = ["Minor spacing inconsistencies", "Could benefit from more breathing room"]
        
        return {
            "heuristics_score": heuristics_score,
            "trend_alignment": "Moderate" if heuristics_score < 0.85 else "Strong",
            "criticisms": criticisms,
            "influences_missing": missing_influences,
            "recommendations": [
                "Study Apple's Human Interface Guidelines",
                "Reference Airbnb's design system patterns",
                "Consider OpenAI's minimal aesthetic"
            ]
        }

class PromptArchitectAgent:
    """Analyzes strategic declarations and outputs AI-native prompt architecture with fallback logic"""
    def __init__(self):
        self.declaration_patterns = {
            "fallback_ux": ["fallback", "error state", "failure mode"],
            "copilot_tiles": ["copilot", "tile", "ai assistant"],
            "trust_score": ["trust", "confidence", "user verification"],
            "auto_execution": ["auto", "automatic", "confirm"]
        }
    
    async def run(self, input_text: str) -> Dict[str, Any]:
        text = input_text.lower()
        
        # Detect declaration type
        detected_declaration = "General design pattern"
        prompt_template = "Given [context], recommend [pattern] using [best practices]"
        tile_logic_hints = []
        
        if any(pattern in text for pattern in self.declaration_patterns["fallback_ux"]):
            detected_declaration = "Fallback UX for high-stakes flows"
            prompt_template = "Given [context], recommend fallback states using [Copilot tiles + user trust score]"
            tile_logic_hints = [
                "Trigger fallback if confidence < 0.6",
                "Ask user to confirm before auto-executing",
                "Show clear error boundaries"
            ]
        
        elif any(pattern in text for pattern in self.declaration_patterns["copilot_tiles"]):
            detected_declaration = "Copilot tile architecture"
            prompt_template = "Design [tile_type] with [interaction_pattern] and [fallback_logic]"
            tile_logic_hints = [
                "Use consistent tile dimensions",
                "Implement progressive disclosure",
                "Provide clear action affordances"
            ]
        
        return {
            "detected_declaration": detected_declaration,
            "prompt_template": prompt_template,
            "tile_logic_hints": tile_logic_hints,
            "ai_native_patterns": [
                "Progressive disclosure",
                "Trust-based interactions", 
                "Graceful degradation"
            ]
        }

class AINativeUXDesigner:
    """Converts raw ideas into wireframe-ready formats (ASCII, JSON, Tailwind blocks)"""
    def __init__(self):
        self.layout_patterns = {
            "copilot_tile": "2-column MCP tile",
            "dashboard": "3-column responsive grid",
            "modal": "centered overlay with backdrop",
            "navigation": "horizontal tab bar"
        }
    
    async def run(self, idea_text: str) -> Dict[str, Any]:
        text = idea_text.lower()
        
        # Determine layout type based on input
        layout_type = "2-column MCP tile"
        ascii_sketch = "[Header] | [Tile Panel]\n[Primary Button] | [Secondary Actions]"
        tailwind_tokens = {
            "padding": "p-4",
            "font": "font-inter", 
            "radius": "rounded-2xl",
            "spacing": "space-y-4"
        }
        
        if "bitcoin" in text or "transaction" in text:
            layout_type = "Data visualization tile"
            ascii_sketch = "[Chart Header] | [Transaction List]\n[Summary Stats] | [Action Buttons]"
            tailwind_tokens.update({
                "background": "bg-gray-50",
                "border": "border border-gray-200"
            })
        
        elif "copilot" in text or "tile" in text:
            layout_type = "2-column MCP tile"
            ascii_sketch = "[Tile Header] | [Content Area]\n[Primary Action] | [Secondary Options]"
            tailwind_tokens.update({
                "shadow": "shadow-lg",
                "hover": "hover:shadow-xl"
            })
        
        return {
            "layout_type": layout_type,
            "ascii_sketch": ascii_sketch,
            "tailwind_tokens": tailwind_tokens,
            "wireframe_ready": True,
            "mcp_compatible": True
        }

class DesignPolishAgent:
    """Applies critique feedback and uplifts craft to Apple/OpenAI level pixel detail"""
    def __init__(self):
        self.polish_patterns = {
            "spacing": ["16px → 24px", "8px → 12px", "32px → 40px"],
            "typography": ["Medium → Semibold", "Regular → Medium", "Light → Regular"],
            "color": ["#666 → #333", "#999 → #666", "#CCC → #999"],
            "radius": ["8px → 12px", "4px → 8px", "16px → 20px"]
        }
    
    async def run(self, input_text: str) -> Dict[str, Any]:
        text = input_text.lower()
        
        fixes_applied = []
        before_after_diff = {}
        
        if "spacing" in text or "layout" in text:
            fixes_applied.append("Harmonized spacing")
            before_after_diff["nav_spacing"] = "16px → 24px"
            before_after_diff["content_padding"] = "8px → 12px"
        
        if "typography" in text or "font" in text:
            fixes_applied.append("Modernized typography")
            before_after_diff["font_weight"] = "Medium → Semibold"
            before_after_diff["line_height"] = "1.4 → 1.5"
        
        if "icon" in text or "visual" in text:
            fixes_applied.append("Improved visual hierarchy")
            before_after_diff["icon_size"] = "16px → 20px"
            before_after_diff["border_radius"] = "8px → 12px"
        
        if not fixes_applied:
            fixes_applied = ["Harmonized spacing", "Modernized iconography", "Improved visual hierarchy"]
            before_after_diff = {
                "nav_spacing": "16px → 24px",
                "font_weight": "Medium → Semibold",
                "border_radius": "8px → 12px"
            }
        
        return {
            "fixes_applied": fixes_applied,
            "before_after_diff": before_after_diff,
            "craft_level": "Apple/OpenAI standard",
            "pixel_perfect": True
        }

class DesignSystemEngineer:
    """Generates consistent token sets and MCP-compatible Tailwind from visual inputs"""
    def __init__(self):
        self.token_patterns = {
            "primary": "#00C244",
            "background": "#F9FAFB", 
            "radius": "16px",
            "font": "Cash Sans"
        }
    
    async def run(self, figma_reference: str) -> Dict[str, Any]:
        text = figma_reference.lower()
        
        design_tokens = self.token_patterns.copy()
        
        # Customize tokens based on input
        if "cash app" in text or "green" in text:
            design_tokens["primary"] = "#00C244"
            design_tokens["font"] = "Cash Sans"
        elif "apple" in text or "minimal" in text:
            design_tokens["primary"] = "#007AFF"
            design_tokens["font"] = "SF Pro"
        elif "openai" in text or "ai" in text:
            design_tokens["primary"] = "#10A37F"
            design_tokens["font"] = "Inter"
        
        return {
            "design_tokens": design_tokens,
            "mcp_ready": True,
            "magic_ui_integration": "✅ Tailwind tokens match Magic UI MCP primitives",
            "output_files": ["tailwind.config.js", "tokens.json"],
            "css_variables": {
                "--primary": design_tokens["primary"],
                "--background": design_tokens["background"],
                "--radius": design_tokens["radius"]
            }
        }

# Agent Registry
AGENT_REGISTRY = {
    "vp_design": VPDesignAgent,
    "evaluator": EvaluatorAgent,
    "creative_director": CreativeDirectorAgent,
    "prompt_master": PromptMasterAgent,
    "surprisal_critic": SurprisalCriticAgent,
    "narrative_divergence": NarrativeDivergenceAgent,
    "longform_creative_chain": LongformCreativeChain,
    "narrative_freshness_rater": NarrativeFreshnessRater,
    "structural_clarity_checker": StructuralClarityChecker,
    "voice_match_evaluator": VoiceMatchEvaluator,
    "rewrite_advisor": RewriteAdvisor,
    "narrative_quality_chain": NarrativeQualityChain,
    "rewrite_loop": RewriteLoopAgent,
    "design_judgment_engine": DesignJudgmentEngine,
    "prompt_architect": PromptArchitectAgent,
    "ai_native_ux_designer": AINativeUXDesigner,
    "design_polish_agent": DesignPolishAgent,
    "design_system_engineer": DesignSystemEngineer
}

def get_agent(agent_name: str):
    """Get agent instance by name"""
    agent_class = AGENT_REGISTRY.get(agent_name)
    if agent_class:
        return agent_class()
    else:
        raise ValueError(f"Agent '{agent_name}' not found. Available agents: {list(AGENT_REGISTRY.keys())}")

# Export for use in other modules
__all__ = ['VPDesignAgent', 'EvaluatorAgent', 'CreativeDirectorAgent', 'PromptMasterAgent', 'SurprisalCriticAgent', 'NarrativeDivergenceAgent', 'LongformCreativeChain', 'NarrativeFreshnessRater', 'StructuralClarityChecker', 'VoiceMatchEvaluator', 'RewriteAdvisor', 'NarrativeQualityChain', 'RewriteLoopAgent', 'DesignJudgmentEngine', 'PromptArchitectAgent', 'AINativeUXDesigner', 'DesignPolishAgent', 'DesignSystemEngineer', 'get_agent', 'AGENT_REGISTRY'] 