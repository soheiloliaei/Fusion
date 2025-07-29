#!/usr/bin/env python3
"""
Design Technologist Agent - Fusion v14
Handles Figma-to-code fidelity, token extraction, Tailwind/React mapping
"""

import asyncio
import time
import logging
import re
from typing import Dict, Any, List, Optional
from datetime import datetime

class DesignTechnologistAgent:
    """
    Design Technologist Agent - Fusion v14
    Handles Figma-to-code fidelity, token extraction, Tailwind/React mapping
    """
    
    def __init__(self):
        self.logger = logging.getLogger("DesignTechnologistAgent")
        
        # Design token categories
        self.token_categories = {
            "colors": ["primary", "secondary", "accent", "neutral", "success", "warning", "error"],
            "typography": ["font_family", "font_size", "font_weight", "line_height", "letter_spacing"],
            "spacing": ["padding", "margin", "gap", "border_radius"],
            "shadows": ["box_shadow", "drop_shadow"],
            "breakpoints": ["sm", "md", "lg", "xl", "2xl"]
        }
        
        # Tailwind utility mapping
        self.tailwind_mapping = {
            "colors": {
                "primary": "blue-500",
                "secondary": "gray-500", 
                "accent": "purple-500",
                "success": "green-500",
                "warning": "yellow-500",
                "error": "red-500"
            },
            "spacing": {
                "xs": "1",
                "sm": "2", 
                "md": "4",
                "lg": "6",
                "xl": "8",
                "2xl": "12"
            },
            "typography": {
                "h1": "text-4xl font-bold",
                "h2": "text-3xl font-semibold",
                "h3": "text-2xl font-medium",
                "body": "text-base",
                "caption": "text-sm text-gray-600"
            }
        }
        
        # Component complexity levels
        self.complexity_levels = {
            "simple": ["button", "input", "label", "icon"],
            "medium": ["card", "modal", "dropdown", "tabs"],
            "complex": ["data_table", "chart", "form_wizard", "multi_step"]
        }
        
        # Accessibility patterns
        self.accessibility_patterns = {
            "semantic_html": ["button", "nav", "main", "section", "article"],
            "aria_labels": ["aria-label", "aria-describedby", "aria-expanded"],
            "keyboard_navigation": ["tabindex", "onKeyDown", "focus_management"],
            "color_contrast": ["text-white", "text-black", "bg-opacity"],
            "screen_reader": ["sr-only", "aria-hidden", "role"]
        }
        
    async def run_async(self, prompt: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main async execution method for Design Technologist Agent
        """
        start_time = time.time()
        self.logger.info("Design Technologist Agent starting analysis")
        
        try:
            # Analyze design requirements
            design_analysis = await self._analyze_design_requirements(prompt)
            
            # Extract design tokens
            token_extraction = await self._extract_design_tokens(prompt, design_analysis)
            
            # Map to Tailwind utilities
            tailwind_mapping = await self._map_to_tailwind(prompt, token_extraction)
            
            # Generate React component structure
            react_structure = await self._generate_react_structure(prompt, design_analysis, tailwind_mapping)
            
            # Apply accessibility patterns
            accessibility_implementation = await self._apply_accessibility_patterns(prompt, react_structure)
            
            # Create enhanced output
            enhanced_output = await self._create_enhanced_output(prompt, design_analysis, token_extraction, tailwind_mapping, react_structure, accessibility_implementation)
            
            execution_time = time.time() - start_time
            confidence = self._calculate_confidence(design_analysis, token_extraction, tailwind_mapping)
            
            self.logger.info(f"Design Technologist Agent completed in {execution_time:.2f}s")
            
            return {
                "output": enhanced_output,
                "enhanced_output": enhanced_output,
                "confidence": confidence,
                "design_analysis": design_analysis,
                "token_extraction": token_extraction,
                "tailwind_mapping": tailwind_mapping,
                "react_structure": react_structure,
                "accessibility_implementation": accessibility_implementation,
                "execution_time": execution_time,
                "shared_state": {
                    "component_type": design_analysis.get("component_type"),
                    "complexity_level": design_analysis.get("complexity_level"),
                    "token_count": len(token_extraction.get("extracted_tokens", [])),
                    "tailwind_classes": len(tailwind_mapping.get("utility_classes", [])),
                    "accessibility_score": accessibility_implementation.get("score"),
                    "analysis_timestamp": datetime.now().timestamp()
                }
            }
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.error(f"Design Technologist Agent failed: {e}")
            return {
                "error": str(e),
                "confidence": 0.0,
                "execution_time": execution_time
            }
    
    async def _analyze_design_requirements(self, prompt: str) -> Dict[str, Any]:
        """Analyze design requirements from prompt"""
        
        # Detect component type
        component_type = self._detect_component_type(prompt)
        
        # Assess complexity level
        complexity_level = self._assess_complexity_level(prompt, component_type)
        
        # Identify design patterns
        design_patterns = self._identify_design_patterns(prompt)
        
        # Extract visual requirements
        visual_requirements = self._extract_visual_requirements(prompt)
        
        return {
            "component_type": component_type,
            "complexity_level": complexity_level,
            "design_patterns": design_patterns,
            "visual_requirements": visual_requirements,
            "interaction_requirements": self._extract_interaction_requirements(prompt)
        }
    
    async def _extract_design_tokens(self, prompt: str, design_analysis: Dict) -> Dict[str, Any]:
        """Extract design tokens from prompt and analysis"""
        
        # Extract color tokens
        color_tokens = self._extract_color_tokens(prompt)
        
        # Extract typography tokens
        typography_tokens = self._extract_typography_tokens(prompt)
        
        # Extract spacing tokens
        spacing_tokens = self._extract_spacing_tokens(prompt)
        
        # Extract shadow tokens
        shadow_tokens = self._extract_shadow_tokens(prompt)
        
        return {
            "extracted_tokens": {
                "colors": color_tokens,
                "typography": typography_tokens,
                "spacing": spacing_tokens,
                "shadows": shadow_tokens
            },
            "token_categories": self._categorize_tokens(color_tokens, typography_tokens, spacing_tokens, shadow_tokens)
        }
    
    async def _map_to_tailwind(self, prompt: str, token_extraction: Dict) -> Dict[str, Any]:
        """Map extracted tokens to Tailwind utilities"""
        
        # Map color tokens
        color_utilities = self._map_color_tokens(token_extraction.get("extracted_tokens", {}).get("colors", []))
        
        # Map typography tokens
        typography_utilities = self._map_typography_tokens(token_extraction.get("extracted_tokens", {}).get("typography", []))
        
        # Map spacing tokens
        spacing_utilities = self._map_spacing_tokens(token_extraction.get("extracted_tokens", {}).get("spacing", []))
        
        # Map shadow tokens
        shadow_utilities = self._map_shadow_tokens(token_extraction.get("extracted_tokens", {}).get("shadows", []))
        
        return {
            "utility_classes": {
                "colors": color_utilities,
                "typography": typography_utilities,
                "spacing": spacing_utilities,
                "shadows": shadow_utilities
            },
            "custom_css": self._generate_custom_css(token_extraction),
            "responsive_utilities": self._generate_responsive_utilities(prompt)
        }
    
    async def _generate_react_structure(self, prompt: str, design_analysis: Dict, tailwind_mapping: Dict) -> Dict[str, Any]:
        """Generate React component structure"""
        
        # Determine component structure
        component_structure = self._determine_component_structure(design_analysis)
        
        # Generate props interface
        props_interface = self._generate_props_interface(design_analysis)
        
        # Create component template
        component_template = self._create_component_template(component_structure, props_interface, tailwind_mapping)
        
        # Add state management
        state_management = self._add_state_management(design_analysis)
        
        return {
            "component_structure": component_structure,
            "props_interface": props_interface,
            "component_template": component_template,
            "state_management": state_management,
            "imports": self._generate_imports(design_analysis)
        }
    
    async def _apply_accessibility_patterns(self, prompt: str, react_structure: Dict) -> Dict[str, Any]:
        """Apply accessibility patterns to React structure"""
        
        # Identify accessibility requirements
        accessibility_requirements = self._identify_accessibility_requirements(prompt)
        
        # Apply semantic HTML
        semantic_html = self._apply_semantic_html(react_structure, accessibility_requirements)
        
        # Add ARIA attributes
        aria_attributes = self._add_aria_attributes(react_structure, accessibility_requirements)
        
        # Implement keyboard navigation
        keyboard_navigation = self._implement_keyboard_navigation(react_structure, accessibility_requirements)
        
        # Add screen reader support
        screen_reader_support = self._add_screen_reader_support(react_structure, accessibility_requirements)
        
        return {
            "requirements": accessibility_requirements,
            "semantic_html": semantic_html,
            "aria_attributes": aria_attributes,
            "keyboard_navigation": keyboard_navigation,
            "screen_reader_support": screen_reader_support,
            "score": self._calculate_accessibility_score(accessibility_requirements, semantic_html, aria_attributes)
        }
    
    async def _create_enhanced_output(self, prompt: str, design_analysis: Dict, token_extraction: Dict, tailwind_mapping: Dict, react_structure: Dict, accessibility_implementation: Dict) -> str:
        """Create enhanced output with technical specifications"""
        
        return f"""# Design Technologist Analysis & Implementation

## Original Request
{prompt}

## Design Analysis

### Component Type
**Type:** {design_analysis.get('component_type', 'unknown')}
**Complexity:** {design_analysis.get('complexity_level', 'medium')}

### Design Patterns
{', '.join(design_analysis.get('design_patterns', ['None detected']))}

## Token Extraction

### Extracted Tokens
**Colors:** {len(token_extraction.get('extracted_tokens', {}).get('colors', []))} tokens
**Typography:** {len(token_extraction.get('extracted_tokens', {}).get('typography', []))} tokens  
**Spacing:** {len(token_extraction.get('extracted_tokens', {}).get('spacing', []))} tokens
**Shadows:** {len(token_extraction.get('extracted_tokens', {}).get('shadows', []))} tokens

## Tailwind Implementation

### Utility Classes
```css
{self._format_tailwind_classes(tailwind_mapping.get('utility_classes', {}))}
```

### Custom CSS
```css
{tailwind_mapping.get('custom_css', '/* No custom CSS needed */')}
```

## React Component Structure

### Component Template
```tsx
{react_structure.get('component_template', '// Component template not generated')}
```

### Props Interface
```typescript
{react_structure.get('props_interface', '// Props interface not generated')}
```

## Accessibility Implementation

### Accessibility Score
**Score:** {accessibility_implementation.get('score', 0):.2f}/1.00

### Applied Patterns
{', '.join(accessibility_implementation.get('requirements', ['None detected']))}

## Technical Confidence
**Score:** {self._calculate_confidence(design_analysis, token_extraction, tailwind_mapping):.2f}/1.00

*Generated by Fusion v14 Design Technologist Agent*"""
    
    def _detect_component_type(self, prompt: str) -> str:
        """Detect component type from prompt"""
        prompt_lower = prompt.lower()
        
        if "button" in prompt_lower:
            return "button"
        elif "input" in prompt_lower or "form" in prompt_lower:
            return "input"
        elif "card" in prompt_lower:
            return "card"
        elif "modal" in prompt_lower or "dialog" in prompt_lower:
            return "modal"
        elif "table" in prompt_lower or "data" in prompt_lower:
            return "data_table"
        elif "chart" in prompt_lower or "graph" in prompt_lower:
            return "chart"
        elif "navigation" in prompt_lower or "nav" in prompt_lower:
            return "navigation"
        else:
            return "custom"
    
    def _assess_complexity_level(self, prompt: str, component_type: str) -> str:
        """Assess component complexity level"""
        prompt_lower = prompt.lower()
        
        # Check for complexity indicators
        if any(word in prompt_lower for word in ["complex", "advanced", "sophisticated", "multi-step"]):
            return "complex"
        elif any(word in prompt_lower for word in ["simple", "basic", "minimal"]):
            return "simple"
        else:
            # Default based on component type
            if component_type in self.complexity_levels["simple"]:
                return "simple"
            elif component_type in self.complexity_levels["complex"]:
                return "complex"
            else:
                return "medium"
    
    def _identify_design_patterns(self, prompt: str) -> List[str]:
        """Identify design patterns in prompt"""
        patterns = []
        prompt_lower = prompt.lower()
        
        if "responsive" in prompt_lower:
            patterns.append("responsive_design")
        
        if "dark" in prompt_lower or "theme" in prompt_lower:
            patterns.append("theme_support")
            
        if "animation" in prompt_lower or "transition" in prompt_lower:
            patterns.append("animation")
            
        if "grid" in prompt_lower or "flex" in prompt_lower:
            patterns.append("layout_system")
            
        return patterns
    
    def _extract_visual_requirements(self, prompt: str) -> List[str]:
        """Extract visual requirements from prompt"""
        requirements = []
        prompt_lower = prompt.lower()
        
        if "rounded" in prompt_lower or "border-radius" in prompt_lower:
            requirements.append("rounded_corners")
            
        if "shadow" in prompt_lower or "elevation" in prompt_lower:
            requirements.append("shadow_effects")
            
        if "gradient" in prompt_lower:
            requirements.append("gradient_backgrounds")
            
        if "border" in prompt_lower:
            requirements.append("border_styling")
            
        return requirements
    
    def _extract_interaction_requirements(self, prompt: str) -> List[str]:
        """Extract interaction requirements from prompt"""
        requirements = []
        prompt_lower = prompt.lower()
        
        if "hover" in prompt_lower:
            requirements.append("hover_effects")
            
        if "click" in prompt_lower or "onClick" in prompt_lower:
            requirements.append("click_handlers")
            
        if "focus" in prompt_lower:
            requirements.append("focus_states")
            
        if "loading" in prompt_lower:
            requirements.append("loading_states")
            
        return requirements
    
    def _extract_color_tokens(self, prompt: str) -> List[str]:
        """Extract color tokens from prompt"""
        colors = []
        prompt_lower = prompt.lower()
        
        # Extract color names
        color_keywords = ["blue", "red", "green", "yellow", "purple", "gray", "white", "black"]
        for color in color_keywords:
            if color in prompt_lower:
                colors.append(color)
                
        # Extract color concepts
        if "primary" in prompt_lower:
            colors.append("primary")
        if "secondary" in prompt_lower:
            colors.append("secondary")
        if "accent" in prompt_lower:
            colors.append("accent")
            
        return colors
    
    def _extract_typography_tokens(self, prompt: str) -> List[str]:
        """Extract typography tokens from prompt"""
        typography = []
        prompt_lower = prompt.lower()
        
        if "heading" in prompt_lower or "title" in prompt_lower:
            typography.extend(["h1", "h2", "h3"])
            
        if "body" in prompt_lower or "text" in prompt_lower:
            typography.append("body")
            
        if "caption" in prompt_lower or "small" in prompt_lower:
            typography.append("caption")
            
        return typography
    
    def _extract_spacing_tokens(self, prompt: str) -> List[str]:
        """Extract spacing tokens from prompt"""
        spacing = []
        prompt_lower = prompt.lower()
        
        if "padding" in prompt_lower:
            spacing.append("padding")
            
        if "margin" in prompt_lower:
            spacing.append("margin")
            
        if "gap" in prompt_lower:
            spacing.append("gap")
            
        return spacing
    
    def _extract_shadow_tokens(self, prompt: str) -> List[str]:
        """Extract shadow tokens from prompt"""
        shadows = []
        prompt_lower = prompt.lower()
        
        if "shadow" in prompt_lower:
            shadows.append("box_shadow")
            
        if "elevation" in prompt_lower:
            shadows.append("drop_shadow")
            
        return shadows
    
    def _categorize_tokens(self, colors: List[str], typography: List[str], spacing: List[str], shadows: List[str]) -> Dict[str, int]:
        """Categorize tokens by type"""
        return {
            "colors": len(colors),
            "typography": len(typography),
            "spacing": len(spacing),
            "shadows": len(shadows)
        }
    
    def _map_color_tokens(self, colors: List[str]) -> List[str]:
        """Map color tokens to Tailwind utilities"""
        utilities = []
        
        for color in colors:
            if color in self.tailwind_mapping["colors"]:
                utilities.append(f"text-{self.tailwind_mapping['colors'][color]}")
                utilities.append(f"bg-{self.tailwind_mapping['colors'][color]}")
                
        return utilities
    
    def _map_typography_tokens(self, typography: List[str]) -> List[str]:
        """Map typography tokens to Tailwind utilities"""
        utilities = []
        
        for typo in typography:
            if typo in self.tailwind_mapping["typography"]:
                utilities.append(self.tailwind_mapping["typography"][typo])
                
        return utilities
    
    def _map_spacing_tokens(self, spacing: List[str]) -> List[str]:
        """Map spacing tokens to Tailwind utilities"""
        utilities = []
        
        for space in spacing:
            if space == "padding":
                utilities.extend(["p-4", "px-6", "py-2"])
            elif space == "margin":
                utilities.extend(["m-4", "mx-6", "my-2"])
            elif space == "gap":
                utilities.extend(["gap-4", "space-x-4", "space-y-2"])
                
        return utilities
    
    def _map_shadow_tokens(self, shadows: List[str]) -> List[str]:
        """Map shadow tokens to Tailwind utilities"""
        utilities = []
        
        for shadow in shadows:
            if shadow == "box_shadow":
                utilities.extend(["shadow-sm", "shadow-md", "shadow-lg"])
            elif shadow == "drop_shadow":
                utilities.extend(["drop-shadow-sm", "drop-shadow-md"])
                
        return utilities
    
    def _generate_custom_css(self, token_extraction: Dict) -> str:
        """Generate custom CSS for complex tokens"""
        return "/* Custom CSS for complex design tokens */"
    
    def _generate_responsive_utilities(self, prompt: str) -> List[str]:
        """Generate responsive utilities"""
        utilities = []
        prompt_lower = prompt.lower()
        
        if "responsive" in prompt_lower:
            utilities.extend([
                "sm:text-sm md:text-base lg:text-lg",
                "sm:p-2 md:p-4 lg:p-6",
                "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3"
            ])
            
        return utilities
    
    def _determine_component_structure(self, design_analysis: Dict) -> str:
        """Determine component structure based on analysis"""
        component_type = design_analysis.get("component_type", "custom")
        
        if component_type == "button":
            return "functional_component"
        elif component_type == "card":
            return "container_component"
        elif component_type == "modal":
            return "portal_component"
        else:
            return "custom_component"
    
    def _generate_props_interface(self, design_analysis: Dict) -> str:
        """Generate TypeScript props interface"""
        component_type = design_analysis.get("component_type", "custom")
        
        if component_type == "button":
            return """
interface ButtonProps {
  children: React.ReactNode;
  variant?: 'primary' | 'secondary' | 'outline';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  onClick?: () => void;
}"""
        else:
            return """
interface ComponentProps {
  children?: React.ReactNode;
  className?: string;
}"""
    
    def _create_component_template(self, structure: str, props_interface: str, tailwind_mapping: Dict) -> str:
        """Create React component template"""
        return f"""
import React from 'react';

{props_interface}

export const Component: React.FC<ComponentProps> = ({{ children, className }}) => {{
  return (
    <div className="p-4 bg-white rounded-lg shadow-md {{className || ''}}">
      {{{{children}}}}
    </div>
  );
}};"""
    
    def _add_state_management(self, design_analysis: Dict) -> Dict[str, Any]:
        """Add state management to component"""
        return {
            "useState": design_analysis.get("complexity_level") == "complex",
            "useEffect": design_analysis.get("complexity_level") == "complex",
            "custom_hooks": design_analysis.get("complexity_level") == "complex"
        }
    
    def _generate_imports(self, design_analysis: Dict) -> List[str]:
        """Generate necessary imports"""
        imports = ["React"]
        
        if design_analysis.get("complexity_level") == "complex":
            imports.extend(["useState", "useEffect"])
            
        return imports
    
    def _identify_accessibility_requirements(self, prompt: str) -> List[str]:
        """Identify accessibility requirements from prompt"""
        requirements = []
        prompt_lower = prompt.lower()
        
        if "accessibility" in prompt_lower or "a11y" in prompt_lower:
            requirements.extend(["semantic_html", "aria_labels", "keyboard_navigation"])
            
        if "screen reader" in prompt_lower:
            requirements.append("screen_reader")
            
        if "keyboard" in prompt_lower:
            requirements.append("keyboard_navigation")
            
        return requirements
    
    def _apply_semantic_html(self, react_structure: Dict, requirements: List[str]) -> Dict[str, Any]:
        """Apply semantic HTML patterns"""
        return {
            "semantic_elements": ["button", "nav", "main"],
            "landmark_roles": ["banner", "navigation", "main"],
            "heading_structure": ["h1", "h2", "h3"]
        }
    
    def _add_aria_attributes(self, react_structure: Dict, requirements: List[str]) -> List[str]:
        """Add ARIA attributes"""
        aria_attrs = []
        
        if "aria_labels" in requirements:
            aria_attrs.extend(["aria-label", "aria-describedby"])
            
        return aria_attrs
    
    def _implement_keyboard_navigation(self, react_structure: Dict, requirements: List[str]) -> Dict[str, Any]:
        """Implement keyboard navigation"""
        return {
            "tabindex": "0",
            "onKeyDown": "handleKeyDown",
            "focus_management": True
        }
    
    def _add_screen_reader_support(self, react_structure: Dict, requirements: List[str]) -> List[str]:
        """Add screen reader support"""
        support = []
        
        if "screen_reader" in requirements:
            support.extend(["sr-only", "aria-live", "role"])
            
        return support
    
    def _calculate_accessibility_score(self, requirements: List[str], semantic_html: Dict, aria_attributes: List[str]) -> float:
        """Calculate accessibility score"""
        base_score = 0.7
        
        if requirements:
            base_score += 0.2
            
        if semantic_html.get("semantic_elements"):
            base_score += 0.05
            
        if aria_attributes:
            base_score += 0.05
            
        return min(base_score, 1.0)
    
    def _format_tailwind_classes(self, utility_classes: Dict) -> str:
        """Format Tailwind classes for output"""
        formatted = []
        
        for category, classes in utility_classes.items():
            if classes:
                formatted.append(f"/* {category.title()} */")
                formatted.extend([f"  {cls}" for cls in classes])
                formatted.append("")
                
        return "\n".join(formatted) if formatted else "/* No utility classes generated */"
    
    def _calculate_confidence(self, design_analysis: Dict, token_extraction: Dict, tailwind_mapping: Dict) -> float:
        """Calculate confidence score"""
        base_confidence = 0.8
        
        # Boost for clear component type
        if design_analysis.get("component_type") != "unknown":
            base_confidence += 0.05
            
        # Boost for extracted tokens
        token_count = sum(token_extraction.get("token_categories", {}).values())
        if token_count > 0:
            base_confidence += 0.05
            
        # Boost for Tailwind mapping
        utility_count = sum(len(classes) for classes in tailwind_mapping.get("utility_classes", {}).values())
        if utility_count > 0:
            base_confidence += 0.05
            
        return min(base_confidence, 0.95) 