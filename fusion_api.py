# fusion_api.py

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Any, Optional
import asyncio
import json
import os

# Import Fusion agents
from agents.vp_design_agent import VPDesignAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.design_technologist_agent import DesignTechnologistAgent
from agents.ai_interaction_designer_agent import AIInteractionDesignerAgent
from agents.workflow_optimizer_agent import WorkflowOptimizerAgent
from agents.creative_director_agent import CreativeDirectorAgent

# Import Fusion core components
from fusion_core.memory.agent_memory import AgentMemory
from fusion_core.telemetry.agent_telemetry import AgentTelemetryLogger
from fusion_core.orchestration.multi_agent_orchestrator import MultiAgentOrchestrator

app = FastAPI(title="Fusion v15 API", version="15.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class RunRequest(BaseModel):
    agent: str
    input: str
    use_memory: bool = True
    use_telemetry: bool = True

class ParallelRunRequest(BaseModel):
    agents: List[str]
    input: str
    use_evaluator: bool = True

class AgentStatus(BaseModel):
    agent: str
    available: bool
    type: str
    capabilities: List[str]

# Initialize Fusion components
telemetry_logger = AgentTelemetryLogger()
memory_manager = None  # Will be initialized per agent if needed

# Initialize agents
agent_map = {
    "vp_design": VPDesignAgent(),
    "evaluator": EvaluatorAgent(),
    "design_technologist": DesignTechnologistAgent(),
    "ai_interaction_designer": AIInteractionDesignerAgent(),
    "workflow_optimizer": WorkflowOptimizerAgent(),
    "creative_director": CreativeDirectorAgent(),
}

# Initialize orchestrator
orchestrator = MultiAgentOrchestrator(
    agents=agent_map,
    evaluator_agent=agent_map.get("evaluator"),
    telemetry_logger=telemetry_logger,
    memory_manager=memory_manager
)

# Load agent manifest
def load_agent_manifest():
    try:
        with open("agent_manifest.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"agents": {}, "system_capabilities": {}}

agent_manifest = load_agent_manifest()

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Fusion v15 API",
        "version": "15.0.0",
        "endpoints": [
            "/run - Run single agent",
            "/run_parallel - Run multiple agents",
            "/agents - List available agents",
            "/status - System status",
            "/memory/{agent} - Get agent memory",
            "/telemetry - Get telemetry data"
        ]
    }

@app.post("/run")
async def run_agent(req: RunRequest):
    """Run a single agent"""
    if req.agent not in agent_map:
        raise HTTPException(status_code=404, detail=f"Agent '{req.agent}' not found")
    
    agent = agent_map[req.agent]
    
    # Initialize memory if requested
    memory = None
    if req.use_memory:
        memory = AgentMemory(req.agent)
    
    try:
        # Run agent
        if hasattr(agent, 'run'):
            output = await agent.run(req.input)
        else:
            output = str(agent(req.input))
        
        # Log to memory if enabled
        if memory:
            memory.append(req.input, output)
        
        # Log telemetry if enabled
        if req.use_telemetry:
            telemetry_logger.log_event(
                agent=req.agent,
                input_text=req.input,
                output_text=output
            )
        
        return {
            "agent": req.agent,
            "output": output,
            "success": True,
            "memory_enabled": req.use_memory,
            "telemetry_enabled": req.use_telemetry
        }
        
    except Exception as e:
        # Log error
        if req.use_telemetry:
            telemetry_logger.log_event(
                agent=req.agent,
                input_text=req.input,
                output_text=f"Error: {str(e)}",
                fallback="error_handling"
            )
        
        raise HTTPException(status_code=500, detail=f"Agent execution failed: {str(e)}")

@app.post("/run_parallel")
async def run_parallel_agents(req: ParallelRunRequest):
    """Run multiple agents in parallel"""
    # Validate agents
    invalid_agents = [agent for agent in req.agents if agent not in agent_map]
    if invalid_agents:
        raise HTTPException(
            status_code=404, 
            detail=f"Agents not found: {invalid_agents}"
        )
    
    try:
        # Run parallel execution
        result = await orchestrator.run_parallel(req.input, req.agents)
        
        return {
            "input": req.input,
            "agents": req.agents,
            "top_result": result.get("top_result"),
            "all_results": result.get("all_results"),
            "evaluations": result.get("evaluations"),
            "execution_time": result.get("execution_time"),
            "agent_count": result.get("agent_count")
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Parallel execution failed: {str(e)}")

@app.get("/agents")
async def list_agents():
    """List all available agents with their capabilities"""
    agents_info = {}
    
    for agent_name, agent in agent_map.items():
        manifest_info = agent_manifest.get("agents", {}).get(agent_name, {})
        
        agents_info[agent_name] = {
            "role": manifest_info.get("role", "Unknown"),
            "capabilities": manifest_info.get("capabilities", []),
            "confidence_threshold": manifest_info.get("confidence_threshold", 0.8),
            "memory_enabled": manifest_info.get("memory_enabled", True),
            "telemetry_enabled": manifest_info.get("telemetry_enabled", True),
            "type": type(agent).__name__,
            "available": True
        }
    
    return {
        "agents": agents_info,
        "total_agents": len(agent_map),
        "system_capabilities": agent_manifest.get("system_capabilities", {})
    }

@app.get("/status")
async def system_status():
    """Get system status and statistics"""
    # Get orchestrator status
    agent_status = orchestrator.get_agent_status()
    
    # Get telemetry stats
    telemetry_stats = telemetry_logger.get_session_stats()
    
    return {
        "system": {
            "version": "15.0.0",
            "status": "active",
            "agents_available": len(agent_map),
            "telemetry_enabled": True,
            "memory_enabled": True
        },
        "agents": agent_status,
        "telemetry": telemetry_stats,
        "manifest": {
            "version": agent_manifest.get("system_info", {}).get("version", "unknown"),
            "capabilities": agent_manifest.get("system_capabilities", {})
        }
    }

@app.get("/memory/{agent_name}")
async def get_agent_memory(agent_name: str, limit: int = 10):
    """Get memory for a specific agent"""
    if agent_name not in agent_map:
        raise HTTPException(status_code=404, detail=f"Agent '{agent_name}' not found")
    
    try:
        memory = AgentMemory(agent_name)
        recent_memory = memory.get_last(limit)
        metadata = memory.get_metadata()
        
        return {
            "agent": agent_name,
            "recent_memory": recent_memory,
            "metadata": metadata,
            "memory_count": len(memory.data["history"])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get memory: {str(e)}")

@app.get("/telemetry")
async def get_telemetry_data():
    """Get telemetry data for current session"""
    try:
        stats = telemetry_logger.get_session_stats()
        return {
            "session_id": telemetry_logger.session_id,
            "session_duration": stats.get("session_duration", 0),
            "total_events": stats.get("total_events", 0),
            "agent_usage": stats.get("agent_usage", {}),
            "fallback_rate": stats.get("fallback_rate", 0),
            "avg_confidence": stats.get("avg_confidence", 0)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get telemetry: {str(e)}")

@app.post("/telemetry/export")
async def export_telemetry(format: str = "json"):
    """Export telemetry data"""
    try:
        if format == "json":
            data = telemetry_logger.save()
            return data
        elif format == "csv":
            csv_path = f"telemetry_export_{telemetry_logger.session_id}.csv"
            telemetry_logger.export_to_csv(csv_path)
            return {"message": f"Telemetry exported to {csv_path}"}
        else:
            raise HTTPException(status_code=400, detail="Unsupported format")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Export failed: {str(e)}")

@app.delete("/telemetry/clear")
async def clear_telemetry():
    """Clear current telemetry session"""
    try:
        telemetry_logger.clear_session()
        return {"message": "Telemetry session cleared"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Clear failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 