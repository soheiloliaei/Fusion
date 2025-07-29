"""
Creative Director Agent – Fusion v14
Orchestrates tone, audience, creativity, and cinematic storytelling.
"""

import asyncio
import time
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime

class CreativeDirectorAgent:
    """
    Creative Director Agent - Fusion v14
    Orchestrates tone, audience targeting, creativity, and cinematic storytelling
    """
    
    def __init__(self):
        self.logger = logging.getLogger("CreativeDirectorAgent")
        self.creative_principles = [
            "emotional_resonance",
            "visual_hierarchy", 
            "narrative_flow",
            "audience_empathy",
            "brand_consistency",
            "innovation_spark",
            "cultural_relevance"
        ]
        
        self.tone_mapping = {
            "cinematic": ["dramatic", "immersive", "storytelling", "visual_impact"],
            "professional": ["trustworthy", "competent", "reliable", "authoritative"],
            "friendly": ["approachable", "warm", "helpful", "conversational"],
            "innovative": ["cutting_edge", "creative", "bold", "forward_thinking"],
            "luxury": ["premium", "exclusive", "sophisticated", "refined"]
        }
        
        self.audience_personas = {
            "executive": ["decision_maker", "time_constrained", "results_focused"],
            "creative": ["visual_thinking", "inspiration_seeking", "aesthetic_appreciation"],
            "technical": ["detail_oriented", "logic_driven", "efficiency_focused"],
            "consumer": ["user_experience", "emotional_connection", "practical_value"]
        }
        
    async def run_async(self, prompt: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main async execution method for Creative Director Agent
        """
        start_time = time.time()
        self.logger.info("Creative Director Agent starting analysis")
        
        try:
            # Analyze the prompt for creative direction
            creative_analysis = await self._analyze_creative_direction(prompt)
            
            # Determine target audience and tone
            audience_insights = await self._identify_audience_and_tone(prompt)
            
            # Generate creative strategy
            creative_strategy = await self._generate_creative_strategy(prompt, creative_analysis, audience_insights)
            
            # Apply cinematic storytelling principles
            cinematic_elements = await self._apply_cinematic_principles(prompt, creative_strategy)
            
            # Create enhanced output
            enhanced_output = await self._create_enhanced_output(prompt, creative_strategy, cinematic_elements)
            
            execution_time = time.time() - start_time
            confidence = self._calculate_confidence(creative_analysis, audience_insights, cinematic_elements)
            
            self.logger.info(f"Creative Director Agent completed in {execution_time:.2f}s")
            
            return {
                "output": enhanced_output,
                "enhanced_output": enhanced_output,
                "confidence": confidence,
                "creative_analysis": creative_analysis,
                "audience_insights": audience_insights,
                "creative_strategy": creative_strategy,
                "cinematic_elements": cinematic_elements,
                "execution_time": execution_time,
                "shared_state": {
                    "creative_principles_applied": self.creative_principles,
                    "tone_detected": audience_insights.get("detected_tone"),
                    "target_audience": audience_insights.get("primary_audience"),
                    "cinematic_style": cinematic_elements.get("style"),
                    "analysis_timestamp": datetime.now().timestamp()
                }
            }
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.error(f"Creative Director Agent failed: {e}")
            return {
                "error": str(e),
                "confidence": 0.0,
                "execution_time": execution_time
            }
    
    async def _analyze_creative_direction(self, prompt: str) -> Dict[str, Any]:
        """Analyze the prompt for creative direction and opportunities"""
        
        # Extract creative keywords and themes
        creative_keywords = self._extract_creative_keywords(prompt)
        
        # Identify emotional undertones
        emotional_undertones = self._identify_emotional_undertones(prompt)
        
        # Detect visual and narrative elements
        visual_elements = self._detect_visual_elements(prompt)
        
        return {
            "creative_keywords": creative_keywords,
            "emotional_undertones": emotional_undertones,
            "visual_elements": visual_elements,
            "creative_opportunities": self._identify_creative_opportunities(prompt)
        }
    
    async def _identify_audience_and_tone(self, prompt: str) -> Dict[str, Any]:
        """Identify target audience and appropriate tone"""
        
        # Analyze prompt for audience indicators
        audience_indicators = self._analyze_audience_indicators(prompt)
        
        # Determine primary audience
        primary_audience = self._determine_primary_audience(audience_indicators)
        
        # Detect tone requirements
        detected_tone = self._detect_tone_requirements(prompt)
        
        # Map tone to creative principles
        tone_principles = self._map_tone_to_principles(detected_tone)
        
        return {
            "primary_audience": primary_audience,
            "detected_tone": detected_tone,
            "tone_principles": tone_principles,
            "audience_indicators": audience_indicators
        }
    
    async def _generate_creative_strategy(self, prompt: str, creative_analysis: Dict, audience_insights: Dict) -> Dict[str, Any]:
        """Generate comprehensive creative strategy"""
        
        # Create visual hierarchy strategy
        visual_strategy = self._create_visual_strategy(creative_analysis, audience_insights)
        
        # Develop narrative approach
        narrative_approach = self._develop_narrative_approach(prompt, creative_analysis)
        
        # Design emotional journey
        emotional_journey = self._design_emotional_journey(creative_analysis, audience_insights)
        
        # Craft brand integration
        brand_integration = self._craft_brand_integration(creative_analysis, audience_insights)
        
        return {
            "visual_strategy": visual_strategy,
            "narrative_approach": narrative_approach,
            "emotional_journey": emotional_journey,
            "brand_integration": brand_integration,
            "creative_guidelines": self._generate_creative_guidelines(creative_analysis, audience_insights)
        }
    
    async def _apply_cinematic_principles(self, prompt: str, creative_strategy: Dict) -> Dict[str, Any]:
        """Apply cinematic storytelling principles"""
        
        # Analyze for cinematic opportunities
        cinematic_opportunities = self._analyze_cinematic_opportunities(prompt)
        
        # Create visual storytelling elements
        visual_storytelling = self._create_visual_storytelling(cinematic_opportunities)
        
        # Design dramatic pacing
        dramatic_pacing = self._design_dramatic_pacing(creative_strategy)
        
        # Craft emotional crescendos
        emotional_crescendos = self._craft_emotional_crescendos(creative_strategy)
        
        return {
            "style": self._determine_cinematic_style(prompt),
            "visual_storytelling": visual_storytelling,
            "dramatic_pacing": dramatic_pacing,
            "emotional_crescendos": emotional_crescendos,
            "cinematic_opportunities": cinematic_opportunities
        }
    
    async def _create_enhanced_output(self, prompt: str, creative_strategy: Dict, cinematic_elements: Dict) -> str:
        """Create enhanced creative output"""
        
        # Build creative framework
        creative_framework = self._build_creative_framework(prompt, creative_strategy)
        
        # Apply cinematic enhancements
        cinematic_enhancements = self._apply_cinematic_enhancements(creative_framework, cinematic_elements)
        
        # Craft final narrative
        final_narrative = self._craft_final_narrative(creative_framework, cinematic_enhancements)
        
        return f"""# Creative Director Analysis & Strategy

## Original Request
{prompt}

## Creative Strategy

### Visual Approach
{creative_strategy['visual_strategy']}

### Narrative Direction  
{creative_strategy['narrative_approach']}

### Emotional Journey
{creative_strategy['emotional_journey']}

### Cinematic Elements
{cinematic_elements['visual_storytelling']}

## Implementation Guidelines

{creative_strategy['creative_guidelines']}

## Creative Confidence
**Score:** {self._calculate_confidence({}, {}, cinematic_elements):.2f}/1.00

*Generated by Fusion v14 Creative Director Agent*"""
    
    def _extract_creative_keywords(self, prompt: str) -> List[str]:
        """Extract creative keywords from prompt"""
        keywords = []
        prompt_lower = prompt.lower()
        
        if "cinematic" in prompt_lower or "movie" in prompt_lower:
            keywords.extend(["visual_storytelling", "dramatic_impact", "immersive_experience"])
        
        if "creative" in prompt_lower or "design" in prompt_lower:
            keywords.extend(["innovation", "aesthetic_appeal", "visual_hierarchy"])
            
        if "tile" in prompt_lower or "dashboard" in prompt_lower:
            keywords.extend(["information_architecture", "user_experience", "visual_clarity"])
            
        return keywords
    
    def _identify_emotional_undertones(self, prompt: str) -> List[str]:
        """Identify emotional undertones in the prompt"""
        emotions = []
        prompt_lower = prompt.lower()
        
        if "cinematic" in prompt_lower or "dramatic" in prompt_lower:
            emotions.append("dramatic_tension")
            
        if "trust" in prompt_lower or "reliable" in prompt_lower:
            emotions.append("trust_building")
            
        if "creative" in prompt_lower or "innovative" in prompt_lower:
            emotions.append("inspiration")
            
        return emotions
    
    def _detect_visual_elements(self, prompt: str) -> List[str]:
        """Detect visual elements mentioned in prompt"""
        elements = []
        prompt_lower = prompt.lower()
        
        if "tile" in prompt_lower:
            elements.extend(["card_layout", "information_density", "visual_hierarchy"])
            
        if "dashboard" in prompt_lower:
            elements.extend(["data_visualization", "navigation", "overview_layout"])
            
        if "cinematic" in prompt_lower:
            elements.extend(["dramatic_lighting", "composition", "visual_impact"])
            
        return elements
    
    def _identify_creative_opportunities(self, prompt: str) -> List[str]:
        """Identify creative opportunities in the prompt"""
        opportunities = []
        prompt_lower = prompt.lower()
        
        if "cinematic" in prompt_lower:
            opportunities.extend(["visual_storytelling", "dramatic_composition", "emotional_resonance"])
            
        if "tile" in prompt_lower:
            opportunities.extend(["information_architecture", "visual_clarity", "user_experience"])
            
        return opportunities
    
    def _analyze_audience_indicators(self, prompt: str) -> Dict[str, Any]:
        """Analyze prompt for audience indicators"""
        indicators = {}
        prompt_lower = prompt.lower()
        
        if "executive" in prompt_lower or "business" in prompt_lower:
            indicators["executive"] = 0.8
            
        if "creative" in prompt_lower or "design" in prompt_lower:
            indicators["creative"] = 0.9
            
        if "technical" in prompt_lower or "developer" in prompt_lower:
            indicators["technical"] = 0.7
            
        return indicators
    
    def _determine_primary_audience(self, audience_indicators: Dict) -> str:
        """Determine primary audience based on indicators"""
        if not audience_indicators:
            return "general"
            
        return max(audience_indicators, key=audience_indicators.get)
    
    def _detect_tone_requirements(self, prompt: str) -> str:
        """Detect tone requirements from prompt"""
        prompt_lower = prompt.lower()
        
        if "cinematic" in prompt_lower or "dramatic" in prompt_lower:
            return "cinematic"
        elif "professional" in prompt_lower or "business" in prompt_lower:
            return "professional"
        elif "friendly" in prompt_lower or "approachable" in prompt_lower:
            return "friendly"
        elif "innovative" in prompt_lower or "creative" in prompt_lower:
            return "innovative"
        else:
            return "professional"
    
    def _map_tone_to_principles(self, tone: str) -> List[str]:
        """Map tone to creative principles"""
        return self.tone_mapping.get(tone, self.tone_mapping["professional"])
    
    def _create_visual_strategy(self, creative_analysis: Dict, audience_insights: Dict) -> str:
        """Create visual strategy based on analysis"""
        strategy = []
        
        if "cinematic" in audience_insights.get("detected_tone", ""):
            strategy.append("• Implement dramatic visual hierarchy with strong contrast")
            strategy.append("• Use cinematic composition principles for visual impact")
            strategy.append("• Create immersive visual storytelling elements")
            
        if "visual_elements" in creative_analysis:
            strategy.append("• Optimize information architecture for visual clarity")
            strategy.append("• Apply consistent visual design principles")
            
        return "\n".join(strategy)
    
    def _develop_narrative_approach(self, prompt: str, creative_analysis: Dict) -> str:
        """Develop narrative approach"""
        approach = []
        
        if "cinematic" in prompt.lower():
            approach.append("• Create compelling visual narrative with dramatic pacing")
            approach.append("• Design emotional journey with clear story arc")
            approach.append("• Implement visual storytelling techniques")
            
        return "\n".join(approach)
    
    def _design_emotional_journey(self, creative_analysis: Dict, audience_insights: Dict) -> str:
        """Design emotional journey"""
        journey = []
        
        if "dramatic_tension" in creative_analysis.get("emotional_undertones", []):
            journey.append("• Build dramatic tension through visual composition")
            journey.append("• Create emotional crescendos and resolution")
            
        return "\n".join(journey)
    
    def _craft_brand_integration(self, creative_analysis: Dict, audience_insights: Dict) -> str:
        """Craft brand integration strategy"""
        return "• Maintain brand consistency while enhancing creative impact"
    
    def _generate_creative_guidelines(self, creative_analysis: Dict, audience_insights: Dict) -> str:
        """Generate creative guidelines"""
        guidelines = []
        
        guidelines.append("• Focus on visual storytelling and emotional resonance")
        guidelines.append("• Apply cinematic principles for dramatic impact")
        guidelines.append("• Maintain brand consistency and user experience")
        guidelines.append("• Test with target audience for emotional response")
        
        return "\n".join(guidelines)
    
    def _analyze_cinematic_opportunities(self, prompt: str) -> List[str]:
        """Analyze cinematic opportunities"""
        opportunities = []
        
        if "cinematic" in prompt.lower():
            opportunities.extend([
                "dramatic_lighting",
                "visual_composition", 
                "emotional_pacing",
                "story_arc_structure"
            ])
            
        return opportunities
    
    def _create_visual_storytelling(self, opportunities: List[str]) -> str:
        """Create visual storytelling elements"""
        elements = []
        
        if "dramatic_lighting" in opportunities:
            elements.append("• Implement dramatic lighting for visual impact")
            
        if "visual_composition" in opportunities:
            elements.append("• Apply cinematic composition principles")
            
        return "\n".join(elements)
    
    def _design_dramatic_pacing(self, creative_strategy: Dict) -> str:
        """Design dramatic pacing"""
        return "• Create visual rhythm with dramatic tension and resolution"
    
    def _craft_emotional_crescendos(self, creative_strategy: Dict) -> str:
        """Craft emotional crescendos"""
        return "• Build emotional intensity through visual progression"
    
    def _determine_cinematic_style(self, prompt: str) -> str:
        """Determine cinematic style"""
        if "cinematic" in prompt.lower():
            return "dramatic_cinematic"
        return "professional_cinematic"
    
    def _build_creative_framework(self, prompt: str, creative_strategy: Dict) -> Dict[str, Any]:
        """Build creative framework"""
        return {
            "visual_approach": creative_strategy.get("visual_strategy", ""),
            "narrative_direction": creative_strategy.get("narrative_approach", ""),
            "emotional_journey": creative_strategy.get("emotional_journey", "")
        }
    
    def _apply_cinematic_enhancements(self, framework: Dict, cinematic_elements: Dict) -> Dict[str, Any]:
        """Apply cinematic enhancements"""
        return {
            "visual_storytelling": cinematic_elements.get("visual_storytelling", ""),
            "dramatic_pacing": cinematic_elements.get("dramatic_pacing", ""),
            "emotional_crescendos": cinematic_elements.get("emotional_crescendos", "")
        }
    
    def _craft_final_narrative(self, framework: Dict, enhancements: Dict) -> str:
        """Craft final narrative"""
        return "Cinematic visual storytelling with dramatic impact and emotional resonance"
    
    def _calculate_confidence(self, creative_analysis: Dict, audience_insights: Dict, cinematic_elements: Dict) -> float:
        """Calculate confidence score"""
        base_confidence = 0.85
        
        # Boost confidence for cinematic elements
        if cinematic_elements.get("style") == "dramatic_cinematic":
            base_confidence += 0.05
            
        # Boost for clear audience identification
        if audience_insights.get("primary_audience"):
            base_confidence += 0.05
            
        return min(base_confidence, 0.95)
