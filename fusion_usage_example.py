# fusion_usage_example.py
# 
# Example: How to use Fusion v14.5 with guardrail protection in Cursor
# 
# Copy-paste this into a Python cell in Cursor

# Step 1: Load the guardrail system (run this once per session)
from cursor_startup import load_fusion_guardrail
load_fusion_guardrail()

# Step 2: Use Fusion with protection
result = safe_fusion_run("Design a Bitcoin dispute experience with agentic UX", "vp_design")

# Step 3: Check the result
print("🎯 Fusion Result:")
print(result)

# Alternative: Use different agents
# result = safe_fusion_run("Critique this design and suggest improvements", "evaluator")
# result = safe_fusion_run("Create a creative vision for this project", "creative_director")
# result = safe_fusion_run("Analyze the technical feasibility", "design_technologist")

# Available agents:
# - vp_design (design analysis)
# - evaluator (critique and evaluation)  
# - creative_director (creative vision)
# - design_technologist (technical implementation)
# - product_navigator (product strategy)
# - strategy_pilot (strategic planning)
# - vp_of_design (executive design review)
# - vp_of_product (executive product review)
# - principal_designer (expert design guidance)
# - component_librarian (design system)
# - content_designer (content strategy)
# - ai_interaction_designer (AI UX)
# - strategy_archivist (documentation)
# - market_analyst (market analysis)
# - workflow_optimizer (process improvement)
# - product_historian (context analysis)
# - deck_narrator (presentations)
# - portfolio_editor (portfolio management)
# - research_summarizer (research synthesis)
# - feedback_amplifier (feedback processing)
# - prompt_master (prompt optimization)
# - dispatcher (coordination) 