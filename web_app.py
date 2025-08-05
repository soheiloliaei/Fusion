# web_app.py
# Streamlit frontend for Fusion v15

import streamlit as st
import requests
import json
import pandas as pd
from datetime import datetime
import time

# Configuration
API_BASE_URL = "http://localhost:8000"

def main():
    st.set_page_config(
        page_title="Fusion v15 Agent Runner",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("🤖 Fusion v15 Agent Runner")
    st.markdown("---")
    
    # Sidebar for navigation
    page = st.sidebar.selectbox(
        "Navigation",
        ["🏠 Dashboard", "🚀 Run Agent", "⚡ Parallel Run", "📊 Telemetry", "🧠 Memory", "📋 Agents"]
    )
    
    if page == "🏠 Dashboard":
        show_dashboard()
    elif page == "🚀 Run Agent":
        show_single_agent()
    elif page == "⚡ Parallel Run":
        show_parallel_run()
    elif page == "📊 Telemetry":
        show_telemetry()
    elif page == "🧠 Memory":
        show_memory()
    elif page == "📋 Agents":
        show_agents()

def show_dashboard():
    """Dashboard with system overview"""
    st.header("🏠 Dashboard")
    
    # System status
    try:
        status_response = requests.get(f"{API_BASE_URL}/status")
        if status_response.status_code == 200:
            status_data = status_response.json()
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("System Status", status_data["system"]["status"])
            
            with col2:
                st.metric("Agents Available", status_data["system"]["agents_available"])
            
            with col3:
                st.metric("Telemetry Enabled", "✅" if status_data["system"]["telemetry_enabled"] else "❌")
            
            with col4:
                st.metric("Memory Enabled", "✅" if status_data["system"]["memory_enabled"] else "❌")
            
            # Telemetry stats
            if "telemetry" in status_data:
                telemetry = status_data["telemetry"]
                st.subheader("📊 Session Statistics")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Events", telemetry.get("total_events", 0))
                with col2:
                    st.metric("Fallback Rate", f"{telemetry.get('fallback_rate', 0):.2%}")
                with col3:
                    st.metric("Avg Confidence", f"{telemetry.get('avg_confidence', 0):.2%}")
                
                # Agent usage chart
                if "agent_usage" in telemetry and telemetry["agent_usage"]:
                    st.subheader("Agent Usage")
                    usage_df = pd.DataFrame(list(telemetry["agent_usage"].items()), 
                                         columns=["Agent", "Usage Count"])
                    st.bar_chart(usage_df.set_index("Agent"))
        
        else:
            st.error("Failed to get system status")
            
    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to Fusion API. Make sure the API server is running on localhost:8000")
        st.info("To start the API server, run: `python fusion_api.py`")

def show_single_agent():
    """Single agent execution interface"""
    st.header("🚀 Run Single Agent")
    
    # Get available agents
    try:
        agents_response = requests.get(f"{API_BASE_URL}/agents")
        if agents_response.status_code == 200:
            agents_data = agents_response.json()
            available_agents = list(agents_data["agents"].keys())
            
            # Agent selection
            selected_agent = st.selectbox("Select Agent", available_agents)
            
            # Show agent info
            if selected_agent in agents_data["agents"]:
                agent_info = agents_data["agents"][selected_agent]
                
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.subheader("Agent Info")
                    st.write(f"**Role:** {agent_info['role']}")
                    st.write(f"**Type:** {agent_info['type']}")
                    st.write(f"**Confidence Threshold:** {agent_info['confidence_threshold']}")
                    
                    # Capabilities
                    st.write("**Capabilities:**")
                    for capability in agent_info['capabilities']:
                        st.write(f"• {capability}")
                
                with col2:
                    st.subheader("Input")
                    user_input = st.text_area(
                        "Enter your prompt:",
                        height=200,
                        placeholder="Describe what you want the agent to do..."
                    )
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        use_memory = st.checkbox("Use Memory", value=True)
                    with col2:
                        use_telemetry = st.checkbox("Use Telemetry", value=True)
                    
                    if st.button("🚀 Run Agent", type="primary"):
                        if user_input.strip():
                            run_single_agent(selected_agent, user_input, use_memory, use_telemetry)
                        else:
                            st.warning("Please enter a prompt")
            
        else:
            st.error("Failed to get agents")
            
    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to Fusion API")

def run_single_agent(agent_name, user_input, use_memory, use_telemetry):
    """Execute single agent and display results"""
    with st.spinner(f"Running {agent_name}..."):
        try:
            response = requests.post(f"{API_BASE_URL}/run", json={
                "agent": agent_name,
                "input": user_input,
                "use_memory": use_memory,
                "use_telemetry": use_telemetry
            })
            
            if response.status_code == 200:
                result = response.json()
                
                st.success("✅ Agent execution completed!")
                
                # Display results
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.subheader("Output")
                    st.text_area("Agent Response", result["output"], height=300, disabled=True)
                
                with col2:
                    st.subheader("Execution Info")
                    st.write(f"**Agent:** {result['agent']}")
                    st.write(f"**Success:** {result['success']}")
                    st.write(f"**Memory:** {'✅' if result['memory_enabled'] else '❌'}")
                    st.write(f"**Telemetry:** {'✅' if result['telemetry_enabled'] else '❌'}")
                    
                    # Copy button
                    if st.button("📋 Copy Output"):
                        st.write("Output copied to clipboard!")
            
            else:
                st.error(f"❌ Agent execution failed: {response.text}")
                
        except requests.exceptions.ConnectionError:
            st.error("❌ Cannot connect to Fusion API")

def show_parallel_run():
    """Parallel agent execution interface"""
    st.header("⚡ Parallel Agent Run")
    
    # Get available agents
    try:
        agents_response = requests.get(f"{API_BASE_URL}/agents")
        if agents_response.status_code == 200:
            agents_data = agents_response.json()
            available_agents = list(agents_data["agents"].keys())
            
            # Agent selection
            selected_agents = st.multiselect(
                "Select Agents (2-5 recommended)",
                available_agents,
                default=available_agents[:3] if len(available_agents) >= 3 else available_agents
            )
            
            if selected_agents:
                st.subheader("Selected Agents")
                for agent in selected_agents:
                    agent_info = agents_data["agents"][agent]
                    st.write(f"• **{agent}** ({agent_info['role']})")
                
                st.subheader("Input")
                user_input = st.text_area(
                    "Enter your prompt:",
                    height=150,
                    placeholder="Describe what you want the agents to do..."
                )
                
                use_evaluator = st.checkbox("Use Evaluator to rank results", value=True)
                
                if st.button("⚡ Run Parallel", type="primary"):
                    if user_input.strip():
                        run_parallel_agents(selected_agents, user_input, use_evaluator)
                    else:
                        st.warning("Please enter a prompt")
            else:
                st.warning("Please select at least one agent")
        
        else:
            st.error("Failed to get agents")
            
    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to Fusion API")

def run_parallel_agents(agents, user_input, use_evaluator):
    """Execute parallel agents and display results"""
    with st.spinner(f"Running {len(agents)} agents in parallel..."):
        try:
            response = requests.post(f"{API_BASE_URL}/run_parallel", json={
                "agents": agents,
                "input": user_input,
                "use_evaluator": use_evaluator
            })
            
            if response.status_code == 200:
                result = response.json()
                
                st.success(f"✅ Parallel execution completed! ({result['execution_time']:.2f}s)")
                
                # Display top result
                if result.get("top_result"):
                    st.subheader("🥇 Top Result")
                    top = result["top_result"]
                    
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.text_area("Top Agent Output", top["output"], height=200, disabled=True)
                    with col2:
                        st.write(f"**Agent:** {top['agent']}")
                        st.write(f"**Execution Time:** {top['execution_time']:.2f}s")
                        if "evaluation" in top:
                            st.write(f"**Score:** {top['evaluation']['score']:.2f}")
                
                # Display all results
                if result.get("all_results"):
                    st.subheader("📊 All Results")
                    
                    results_data = []
                    for res in result["all_results"]:
                        results_data.append({
                            "Agent": res["agent"],
                            "Success": res["success"],
                            "Execution Time": f"{res['execution_time']:.2f}s",
                            "Score": res.get("evaluation", {}).get("score", "N/A")
                        })
                    
                    df = pd.DataFrame(results_data)
                    st.dataframe(df, use_container_width=True)
                
                # Show evaluations if available
                if result.get("evaluations"):
                    st.subheader("📈 Evaluations")
                    for eval_result in result["evaluations"]:
                        st.write(f"**Score:** {eval_result['score']:.2f}")
                        st.write(f"**Text:** {eval_result['evaluation_text'][:200]}...")
                        st.divider()
            
            else:
                st.error(f"❌ Parallel execution failed: {response.text}")
                
        except requests.exceptions.ConnectionError:
            st.error("❌ Cannot connect to Fusion API")

def show_telemetry():
    """Telemetry data display"""
    st.header("📊 Telemetry Dashboard")
    
    try:
        # Get telemetry data
        telemetry_response = requests.get(f"{API_BASE_URL}/telemetry")
        if telemetry_response.status_code == 200:
            telemetry_data = telemetry_response.json()
            
            # Session info
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Session ID", telemetry_data["session_id"][:8] + "...")
            with col2:
                st.metric("Total Events", telemetry_data["total_events"])
            with col3:
                st.metric("Fallback Rate", f"{telemetry_data['fallback_rate']:.2%}")
            with col4:
                st.metric("Avg Confidence", f"{telemetry_data['avg_confidence']:.2%}")
            
            # Agent usage chart
            if telemetry_data.get("agent_usage"):
                st.subheader("Agent Usage")
                usage_df = pd.DataFrame(list(telemetry_data["agent_usage"].items()), 
                                     columns=["Agent", "Usage Count"])
                st.bar_chart(usage_df.set_index("Agent"))
            
            # Export options
            st.subheader("Export Data")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("📥 Export JSON"):
                    export_telemetry("json")
            with col2:
                if st.button("📥 Export CSV"):
                    export_telemetry("csv")
            
            # Clear session
            if st.button("🗑️ Clear Session", type="secondary"):
                clear_telemetry()
        
        else:
            st.error("Failed to get telemetry data")
            
    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to Fusion API")

def export_telemetry(format_type):
    """Export telemetry data"""
    try:
        response = requests.post(f"{API_BASE_URL}/telemetry/export?format={format_type}")
        if response.status_code == 200:
            if format_type == "json":
                st.download_button(
                    "📥 Download JSON",
                    response.content,
                    file_name=f"fusion_telemetry_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
            else:
                st.success("CSV exported successfully!")
        else:
            st.error("Export failed")
    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to Fusion API")

def clear_telemetry():
    """Clear telemetry session"""
    try:
        response = requests.delete(f"{API_BASE_URL}/telemetry/clear")
        if response.status_code == 200:
            st.success("✅ Telemetry session cleared!")
            st.rerun()
        else:
            st.error("Failed to clear telemetry")
    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to Fusion API")

def show_memory():
    """Agent memory display"""
    st.header("🧠 Agent Memory")
    
    try:
        # Get available agents
        agents_response = requests.get(f"{API_BASE_URL}/agents")
        if agents_response.status_code == 200:
            agents_data = agents_response.json()
            available_agents = list(agents_data["agents"].keys())
            
            selected_agent = st.selectbox("Select Agent", available_agents)
            memory_limit = st.slider("Memory Entries", 1, 20, 10)
            
            if st.button("🔍 Load Memory"):
                load_agent_memory(selected_agent, memory_limit)
        
        else:
            st.error("Failed to get agents")
            
    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to Fusion API")

def load_agent_memory(agent_name, limit):
    """Load and display agent memory"""
    try:
        response = requests.get(f"{API_BASE_URL}/memory/{agent_name}?limit={limit}")
        if response.status_code == 200:
            memory_data = response.json()
            
            st.subheader(f"Memory for {agent_name}")
            
            # Memory metadata
            metadata = memory_data["metadata"]
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Runs", metadata["total_runs"])
            with col2:
                st.metric("Success Rate", f"{metadata['success_rate']:.2%}")
            with col3:
                st.metric("Memory Entries", memory_data["memory_count"])
            
            # Recent memory
            if memory_data["recent_memory"]:
                st.subheader("Recent Memory")
                for i, entry in enumerate(memory_data["recent_memory"]):
                    with st.expander(f"Entry {i+1} - {entry['timestamp']}"):
                        st.write("**Input:**")
                        st.text(entry["input"])
                        st.write("**Output:**")
                        st.text(entry["output"])
                        if entry.get("metadata"):
                            st.write("**Metadata:**")
                            st.json(entry["metadata"])
            else:
                st.info("No memory entries found for this agent")
        
        else:
            st.error(f"Failed to get memory for {agent_name}")
            
    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to Fusion API")

def show_agents():
    """Agent information display"""
    st.header("📋 Available Agents")
    
    try:
        response = requests.get(f"{API_BASE_URL}/agents")
        if response.status_code == 200:
            agents_data = response.json()
            
            # System capabilities
            st.subheader("System Capabilities")
            capabilities = agents_data.get("system_capabilities", {})
            for capability, enabled in capabilities.items():
                st.write(f"• **{capability}:** {'✅' if enabled else '❌'}")
            
            # Agent details
            st.subheader("Agent Details")
            for agent_name, agent_info in agents_data["agents"].items():
                with st.expander(f"🤖 {agent_name} - {agent_info['role']}"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write(f"**Role:** {agent_info['role']}")
                        st.write(f"**Type:** {agent_info['type']}")
                        st.write(f"**Confidence Threshold:** {agent_info['confidence_threshold']}")
                    
                    with col2:
                        st.write("**Capabilities:**")
                        for capability in agent_info['capabilities']:
                            st.write(f"• {capability}")
                    
                    st.write("**Features:**")
                    st.write(f"• Memory: {'✅' if agent_info['memory_enabled'] else '❌'}")
                    st.write(f"• Telemetry: {'✅' if agent_info['telemetry_enabled'] else '❌'}")
        
        else:
            st.error("Failed to get agents")
            
    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to Fusion API")

if __name__ == "__main__":
    main() 