# fusion_core/orchestration/multi_agent_orchestrator.py

import asyncio
import time
from typing import Dict, List, Any, Optional
from concurrent.futures import ThreadPoolExecutor
import json

class MultiAgentOrchestrator:
    def __init__(self, agents: Dict[str, Any], evaluator_agent=None, 
                 telemetry_logger=None, memory_manager=None):
        self.agents = agents
        self.evaluator = evaluator_agent
        self.telemetry = telemetry_logger
        self.memory = memory_manager
        self.executor = ThreadPoolExecutor(max_workers=10)

    async def run_parallel(self, input_text: str, agent_names: List[str] = None) -> Dict[str, Any]:
        """Run multiple agents in parallel and aggregate results"""
        start_time = time.time()
        
        # Use specified agents or all available agents
        target_agents = agent_names or list(self.agents.keys())
        available_agents = {name: agent for name, agent in self.agents.items() 
                          if name in target_agents}
        
        if not available_agents:
            return {"error": "No agents available", "results": []}
        
        # Run agents in parallel
        tasks = []
        for agent_name, agent in available_agents.items():
            task = self._run_agent_async(agent_name, agent, input_text)
            tasks.append(task)
        
        # Wait for all agents to complete
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Process results and handle exceptions
        processed_results = []
        for i, result in enumerate(results):
            agent_name = list(available_agents.keys())[i]
            if isinstance(result, Exception):
                processed_results.append({
                    "agent": agent_name,
                    "output": f"Error: {str(result)}",
                    "success": False,
                    "execution_time": 0
                })
            else:
                processed_results.append(result)
        
        # Evaluate results if evaluator is available
        evaluations = []
        if self.evaluator:
            for result in processed_results:
                if result["success"]:
                    eval_result = await self._evaluate_result(result, input_text)
                    evaluations.append(eval_result)
                    result["evaluation"] = eval_result
        
        # Sort by evaluation score if available
        if evaluations:
            processed_results.sort(key=lambda x: x.get("evaluation", {}).get("score", 0), reverse=True)
        
        # Log parallel execution
        if self.telemetry:
            self.telemetry.log_parallel_execution(processed_results)
        
        execution_time = time.time() - start_time
        
        return {
            "top_result": processed_results[0] if processed_results else None,
            "all_results": processed_results,
            "evaluations": evaluations,
            "execution_time": execution_time,
            "agent_count": len(available_agents)
        }

    async def _run_agent_async(self, agent_name: str, agent: Any, input_text: str) -> Dict[str, Any]:
        """Run a single agent asynchronously"""
        start_time = time.time()
        
        try:
            # Get agent context from memory if available
            context = ""
            if self.memory:
                context = self.memory.get_context(agent_name)
            
            # Prepare input with context
            enhanced_input = f"{context}\n\nCurrent Request: {input_text}" if context else input_text
            
            # Run agent
            if hasattr(agent, 'run'):
                output = await agent.run(enhanced_input)
            elif hasattr(agent, '__call__'):
                output = await agent(enhanced_input)
            else:
                output = str(agent)
            
            execution_time = time.time() - start_time
            
            # Log to memory if available
            if self.memory:
                self.memory.append(agent_name, input_text, output, {
                    "execution_time": execution_time,
                    "success": True
                })
            
            # Log telemetry
            if self.telemetry:
                self.telemetry.log_event(
                    agent=agent_name,
                    input_text=input_text,
                    output_text=output,
                    execution_time=execution_time,
                    confidence=0.8  # Default confidence
                )
            
            return {
                "agent": agent_name,
                "output": output,
                "success": True,
                "execution_time": execution_time
            }
            
        except Exception as e:
            execution_time = time.time() - start_time
            
            # Log error to memory
            if self.memory:
                self.memory.append(agent_name, input_text, f"Error: {str(e)}", {
                    "execution_time": execution_time,
                    "success": False,
                    "error": str(e)
                })
            
            # Log telemetry
            if self.telemetry:
                self.telemetry.log_event(
                    agent=agent_name,
                    input_text=input_text,
                    output_text=f"Error: {str(e)}",
                    execution_time=execution_time,
                    fallback="error_handling"
                )
            
            return {
                "agent": agent_name,
                "output": f"Error: {str(e)}",
                "success": False,
                "execution_time": execution_time
            }

    async def _evaluate_result(self, result: Dict[str, Any], original_input: str) -> Dict[str, Any]:
        """Evaluate a single result using the evaluator agent"""
        if not self.evaluator:
            return {"score": 0.5, "metrics": {}}
        
        try:
            evaluation_prompt = f"""
            Evaluate this agent output:
            
            Original Input: {original_input}
            Agent: {result['agent']}
            Output: {result['output']}
            
            Provide a score (0-1) and brief evaluation.
            """
            
            if hasattr(self.evaluator, 'run'):
                eval_output = await self.evaluator.run(evaluation_prompt)
            else:
                eval_output = str(self.evaluator(evaluation_prompt))
            
            # Parse evaluation (simple heuristic)
            score = 0.5  # Default score
            if "score:" in eval_output.lower():
                try:
                    score_text = eval_output.lower().split("score:")[1].split()[0]
                    score = float(score_text)
                except:
                    pass
            
            evaluation = {
                "score": score,
                "evaluation_text": eval_output,
                "metrics": {
                    "relevance": score,
                    "completeness": score,
                    "quality": score
                }
            }
            
            # Log evaluation
            if self.telemetry:
                self.telemetry.log_evaluation(
                    agent=result['agent'],
                    evaluation_score=score,
                    evaluation_metrics=evaluation['metrics']
                )
            
            return evaluation
            
        except Exception as e:
            return {
                "score": 0.0,
                "evaluation_text": f"Evaluation error: {str(e)}",
                "metrics": {"error": str(e)}
            }

    def run_sync(self, input_text: str, agent_names: List[str] = None) -> Dict[str, Any]:
        """Synchronous version of run_parallel for non-async environments"""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            result = loop.run_until_complete(self.run_parallel(input_text, agent_names))
            return result
        finally:
            loop.close()

    def get_agent_status(self) -> Dict[str, Any]:
        """Get status of all available agents"""
        status = {}
        for agent_name, agent in self.agents.items():
            status[agent_name] = {
                "available": True,
                "type": type(agent).__name__,
                "has_run_method": hasattr(agent, 'run'),
                "has_call_method": hasattr(agent, '__call__')
            }
        return status

    def add_agent(self, name: str, agent: Any):
        """Add a new agent to the orchestrator"""
        self.agents[name] = agent

    def remove_agent(self, name: str):
        """Remove an agent from the orchestrator"""
        if name in self.agents:
            del self.agents[name]

    def get_session_stats(self) -> Dict[str, Any]:
        """Get current session statistics"""
        if self.telemetry:
            return self.telemetry.get_session_stats()
        return {"error": "No telemetry logger available"} 