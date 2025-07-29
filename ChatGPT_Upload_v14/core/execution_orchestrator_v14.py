"""
Execution Orchestrator v14 - Fusion v14
Async orchestrator for the programmable agent OS
"""

import asyncio
import time
from typing import Dict, Any, List, Optional
from datetime import datetime
import logging

from .fusion_context import FusionContext

class ExecutionOrchestrator:
    """
    Async orchestrator for Fusion v14
    Manages agent execution, tool coordination, and pattern fallback
    """
    
    def __init__(self, context: FusionContext):
        self.context = context
        self.agents = {}
        self.tools = {}
        self.patterns = {}
        self.logger = logging.getLogger("ExecutionOrchestrator")
        
    def register_agent(self, name: str, agent_instance) -> None:
        """Register an agent with the orchestrator"""
        self.agents[name] = agent_instance
        self.logger.info(f"Registered agent: {name}")
        
    def register_tool(self, name: str, tool_instance) -> None:
        """Register a tool with the orchestrator"""
        self.tools[name] = tool_instance
        self.logger.info(f"Registered tool: {name}")
        
    def register_pattern(self, name: str, pattern_data: Dict[str, Any]) -> None:
        """Register a pattern with the orchestrator"""
        self.patterns[name] = pattern_data
        self.logger.info(f"Registered pattern: {name}")
        
    async def execute_agent(self, agent_name: str, input_prompt: str, 
                          tools: List[str] = None) -> Dict[str, Any]:
        """Execute a single agent with optional tools"""
        
        if agent_name not in self.agents:
            raise ValueError(f"Agent {agent_name} not registered")
            
        agent = self.agents[agent_name]
        start_time = time.time()
        
        try:
            self.logger.info(f"Executing agent: {agent_name}")
            
            # Prepare tools for the agent
            available_tools = {}
            if tools:
                for tool_name in tools:
                    if tool_name in self.tools:
                        available_tools[tool_name] = self.tools[tool_name]
                    else:
                        self.logger.warning(f"Tool {tool_name} not found")
                        
            # Execute agent
            if hasattr(agent, 'run_async'):
                result = await agent.run_async(input_prompt, available_tools)
            else:
                result = await agent.run(input_prompt, available_tools)
                
            execution_time = time.time() - start_time
            
            # Store interaction in memory
            await self.context.store_interaction(
                agent_name=agent_name,
                input_prompt=input_prompt,
                output=result,
                confidence=result.get('confidence', 0.8),
                tools_used=list(available_tools.keys()),
                execution_time=execution_time
            )
            
            self.logger.info(f"Agent {agent_name} completed in {execution_time:.2f}s")
            return result
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.error(f"Agent {agent_name} failed: {e}")
            
            # Store failed interaction
            await self.context.store_interaction(
                agent_name=agent_name,
                input_prompt=input_prompt,
                output={"error": str(e)},
                confidence=0.0,
                tools_used=list(available_tools.keys()) if 'available_tools' in locals() else [],
                execution_time=execution_time
            )
            
            raise
            
    async def execute_pipeline(self, input_prompt: str, 
                             agent_sequence: List[str] = None,
                             tools_per_agent: Dict[str, List[str]] = None) -> Dict[str, Any]:
        """Execute a sequence of agents in pipeline"""
        
        if agent_sequence is None:
            agent_sequence = list(self.agents.keys())
            
        if tools_per_agent is None:
            tools_per_agent = {}
            
        self.logger.info(f"Starting pipeline execution with {len(agent_sequence)} agents")
        
        pipeline_result = {
            "pipeline_start": datetime.now().isoformat(),
            "agent_sequence": agent_sequence,
            "results": {},
            "final_output": None,
            "total_execution_time": 0.0
        }
        
        current_input = input_prompt
        total_start_time = time.time()
        
        try:
            for i, agent_name in enumerate(agent_sequence):
                self.logger.info(f"Pipeline step {i+1}/{len(agent_sequence)}: {agent_name}")
                
                # Get tools for this agent
                tools = tools_per_agent.get(agent_name, [])
                
                # Execute agent
                result = await self.execute_agent(agent_name, current_input, tools)
                
                # Store result
                pipeline_result["results"][agent_name] = result
                
                # Update input for next agent
                if result.get("output"):
                    current_input = result["output"]
                elif result.get("enhanced_output"):
                    current_input = result["enhanced_output"]
                    
                # Update shared state if agent provides it
                if result.get("shared_state"):
                    for key, value in result["shared_state"].items():
                        self.context.set_shared_state(key, value)
                        
            total_execution_time = time.time() - total_start_time
            pipeline_result["total_execution_time"] = total_execution_time
            pipeline_result["final_output"] = current_input
            pipeline_result["pipeline_end"] = datetime.now().isoformat()
            
            self.logger.info(f"Pipeline completed in {total_execution_time:.2f}s")
            return pipeline_result
            
        except Exception as e:
            total_execution_time = time.time() - total_start_time
            self.logger.error(f"Pipeline failed: {e}")
            pipeline_result["error"] = str(e)
            pipeline_result["total_execution_time"] = total_execution_time
            return pipeline_result
            
    async def execute_with_pattern_fallback(self, input_prompt: str, 
                                         primary_agent: str,
                                         fallback_patterns: List[str] = None) -> Dict[str, Any]:
        """Execute agent with pattern fallback"""
        
        try:
            # Try primary agent first
            result = await self.execute_agent(primary_agent, input_prompt)
            
            # Check if result meets confidence threshold
            confidence = result.get('confidence', 0.8)
            if confidence >= 0.8:
                return result
                
            # If confidence is low, try pattern fallback
            if fallback_patterns:
                self.logger.info(f"Low confidence ({confidence}), trying pattern fallback")
                
                for pattern_name in fallback_patterns:
                    if pattern_name in self.patterns:
                        pattern_result = await self._apply_pattern(pattern_name, input_prompt)
                        if pattern_result.get('confidence', 0) > confidence:
                            self.logger.info(f"Pattern {pattern_name} improved confidence to {pattern_result.get('confidence')}")
                            return pattern_result
                            
            return result
            
        except Exception as e:
            self.logger.error(f"Primary agent failed, trying pattern fallback: {e}")
            
            # Try pattern fallback on error
            if fallback_patterns:
                for pattern_name in fallback_patterns:
                    if pattern_name in self.patterns:
                        try:
                            pattern_result = await self._apply_pattern(pattern_name, input_prompt)
                            return pattern_result
                        except Exception as pattern_error:
                            self.logger.warning(f"Pattern {pattern_name} also failed: {pattern_error}")
                            
            raise
            
    async def _apply_pattern(self, pattern_name: str, input_prompt: str) -> Dict[str, Any]:
        """Apply a specific pattern to the input"""
        
        pattern = self.patterns[pattern_name]
        start_time = time.time()
        
        try:
            # Apply pattern transformation
            if pattern.get('type') == 'prompt_enhancement':
                enhanced_prompt = self._enhance_prompt_with_pattern(input_prompt, pattern)
                result = await self.execute_agent(pattern.get('agent', 'vp_design'), enhanced_prompt)
            elif pattern.get('type') == 'output_transformation':
                result = await self.execute_agent(pattern.get('agent', 'vp_design'), input_prompt)
                result = self._transform_output_with_pattern(result, pattern)
            else:
                result = await self.execute_agent(pattern.get('agent', 'vp_design'), input_prompt)
                
            execution_time = time.time() - start_time
            
            # Store pattern application
            await self.context.store_interaction(
                agent_name=f"pattern_{pattern_name}",
                input_prompt=input_prompt,
                output=result,
                confidence=result.get('confidence', 0.8),
                tools_used=[],
                execution_time=execution_time,
                pattern_applied=pattern_name
            )
            
            return result
            
        except Exception as e:
            self.logger.error(f"Pattern {pattern_name} failed: {e}")
            raise
            
    def _enhance_prompt_with_pattern(self, input_prompt: str, pattern: Dict[str, Any]) -> str:
        """Enhance prompt using pattern instructions"""
        
        enhancement = pattern.get('enhancement', '')
        if enhancement:
            return f"{input_prompt}\n\n{enhancement}"
        return input_prompt
        
    def _transform_output_with_pattern(self, result: Dict[str, Any], pattern: Dict[str, Any]) -> Dict[str, Any]:
        """Transform output using pattern instructions"""
        
        transformation = pattern.get('transformation', {})
        if transformation:
            # Apply transformation rules
            if transformation.get('add_context'):
                result['context'] = transformation['add_context']
            if transformation.get('enhance_format'):
                result['formatted_output'] = self._format_output(result.get('output', ''), transformation['enhance_format'])
                
        return result
        
    def _format_output(self, output: str, format_instructions: str) -> str:
        """Format output according to instructions"""
        # Simple formatting for now
        if format_instructions == 'markdown':
            return f"# Enhanced Output\n\n{output}"
        elif format_instructions == 'structured':
            return f"## Analysis\n\n{output}\n\n## Recommendations\n\nBased on the analysis above..."
        return output
        
    def get_orchestrator_stats(self) -> Dict[str, Any]:
        """Get orchestrator statistics"""
        return {
            "registered_agents": list(self.agents.keys()),
            "registered_tools": list(self.tools.keys()),
            "registered_patterns": list(self.patterns.keys()),
            "context_stats": self.context.get_execution_stats()
        } 