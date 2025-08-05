# fusion_core/__init__.py

"""
Fusion v15 Core Package
=======================

A comprehensive agent orchestration system with memory, telemetry, and API capabilities.

Features:
- Agent Memory: Persistent context and interaction history
- Telemetry: Real-time logging and performance metrics
- Multi-Agent Orchestration: Parallel execution with evaluation
- API Interface: RESTful endpoints for external integration
- Web GUI: Streamlit-based user interface

Version: 15.0.0
"""

__version__ = "15.0.0"
__author__ = "Fusion Team"

from .memory.agent_memory import AgentMemory
from .telemetry.agent_telemetry import AgentTelemetryLogger
from .orchestration.multi_agent_orchestrator import MultiAgentOrchestrator

__all__ = [
    "AgentMemory",
    "AgentTelemetryLogger", 
    "MultiAgentOrchestrator"
] 