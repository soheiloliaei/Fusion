# fusion_native_usage.py
# 
# Example: How to use Fusion v14.5 with native Cursor integration
# 
# Copy-paste this into a Python cell in Cursor

# Step 1: Import the bootstrap (this loads everything automatically)
import cursor_init

# Step 2: Use Fusion with natural prompts (no manual setup needed!)

# Simple usage with specific agent
result = ask("Design a modern Bitcoin recovery experience for support advocates", "vp_design")
print("🎯 Result:", result)

# Auto-agent selection (Fusion picks the best agent)
result = ask_auto("Critique this design and suggest improvements")
print("🤖 Auto-selected agent result:", result)

# Multi-agent chain (runs multiple agents in sequence)
chain_result = ask_chain("Build and critique this Bitcoin dispute resolution idea", 
                        ["vp_design", "evaluator", "creative_director"])
print("🔗 Chain result:", chain_result)

# Direct Fusion access (if you need the raw function)
raw_result = fusion("Analyze the technical feasibility", "design_technologist")
print("⚙️ Raw Fusion result:", raw_result)

# Available usage patterns:
# 
# 1. Natural prompts with specific agents:
#    ask("your prompt", "agent_name")
#
# 2. Auto-agent selection:
#    ask_auto("your prompt") 
#
# 3. Multi-agent chains:
#    ask_chain("your prompt", ["agent1", "agent2", "agent3"])
#
# 4. Direct Fusion access:
#    fusion("your prompt", "agent_name")
#
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