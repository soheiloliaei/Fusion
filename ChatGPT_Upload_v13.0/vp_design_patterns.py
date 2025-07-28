"""
VP of Design Patterns – AI-first, product-led design critique
Transforms outputs using 15+ years of UX/UI design expertise.
"""

def apply_design_critique(input_prompt, output):
    """
    Apply AI-first, product-led design critique to enhance output.
    Focuses on user experience, design systems, and business impact.
    """
    feedback = []
    score_lift = 0.15
    enhanced = output
    principles_applied = []

    # 1. User Experience Enhancement
    if "user" not in output.lower() and "experience" not in output.lower():
        feedback.append("🔍 Missing user experience focus. Adding UX perspective.")
        enhanced = enhanced + "\n\n🎯 **UX Perspective**: Consider the user journey and pain points this addresses."
        principles_applied.append("User-centric design thinking")
        score_lift += 0.1

    # 2. Design System Alignment
    if "design" not in output.lower() and "system" not in output.lower():
        feedback.append("🎨 Missing design system considerations. Adding design system alignment.")
        enhanced = enhanced + "\n\n🎨 **Design System**: Ensure consistency with existing design patterns and components."
        principles_applied.append("Design system consistency")
        score_lift += 0.1

    # 3. Accessibility and Inclusion
    if "accessible" not in output.lower() and "inclusive" not in output.lower():
        feedback.append("♿ Missing accessibility considerations. Adding inclusive design principles.")
        enhanced = enhanced + "\n\n♿ **Accessibility**: Ensure this solution works for users with diverse abilities."
        principles_applied.append("Accessibility and inclusion")
        score_lift += 0.1

    # 4. Business Impact Through Design
    if "business" not in output.lower() and "impact" not in output.lower():
        feedback.append("📈 Missing business impact focus. Adding product-led growth perspective.")
        enhanced = enhanced + "\n\n📈 **Business Impact**: How does this design decision drive user engagement and business metrics?"
        principles_applied.append("Business impact through design")
        score_lift += 0.1

    # 5. Technical Feasibility
    if "technical" not in output.lower() and "feasible" not in output.lower():
        feedback.append("⚙️ Missing technical considerations. Adding implementation feasibility.")
        enhanced = enhanced + "\n\n⚙️ **Technical Feasibility**: Consider implementation complexity and technical constraints."
        principles_applied.append("Performance and scalability")
        score_lift += 0.1

    # 6. AI-First Design Thinking
    if "ai" not in output.lower() and "intelligent" not in output.lower():
        feedback.append("🤖 Missing AI-first perspective. Adding intelligent design considerations.")
        enhanced = enhanced + "\n\n🤖 **AI-First Design**: How can AI enhance this user experience and make it more intelligent?"
        principles_applied.append("AI-first design thinking")
        score_lift += 0.1

    # 7. Performance and Scalability
    if len(output.split()) > 200:
        feedback.append("⚡ Output is verbose. Streamlining for clarity and performance.")
        enhanced = "🎯 **Streamlined Design Solution**:\n" + " ".join(output.split()[:100]) + "..."
        score_lift += 0.2

    if not feedback:
        feedback.append("✅ Design output is solid. Consider adding edge or innovation for next-level impact.")
        enhanced += "\n\n🚀 **Next-Level Enhancement**: Consider how this could be revolutionary, not just evolutionary."

    return {
        "feedback": feedback,
        "enhanced": enhanced,
        "score_lift": score_lift,
        "principles": principles_applied
    }

# Example usage for testing
if __name__ == "__main__":
    test_output = "This is a basic solution without UX considerations."
    result = apply_design_critique("Design a login form", test_output)
    print("🎨 VP of Design Critique Applied:")
    print("Feedback:", result["feedback"])
    print("Enhanced:", result["enhanced"])
    print("Score Lift:", result["score_lift"])
