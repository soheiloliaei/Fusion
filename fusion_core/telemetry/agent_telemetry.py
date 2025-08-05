# fusion_core/telemetry/agent_telemetry.py

import time
import json
import os
from uuid import uuid4
from typing import Dict, Any, List, Optional
from datetime import datetime

class AgentTelemetryLogger:
    def __init__(self, session_id=None, log_dir="fusion_telemetry"):
        self.session_id = session_id or str(uuid4())
        self.start = time.time()
        self.events = []
        os.makedirs(log_dir, exist_ok=True)
        self.path = os.path.join(log_dir, f"{self.session_id}.json")

    def log_event(self, agent: str, input_text: str, output_text: str, 
                  tokens_used: int = 0, fallback: Optional[str] = None, 
                  confidence: float = 0.0, execution_time: float = 0.0):
        """Log a single agent execution event"""
        elapsed = round(time.time() - self.start, 2)
        
        event = {
            "timestamp": datetime.now().isoformat(),
            "agent": agent,
            "input": input_text[:200] + "..." if len(input_text) > 200 else input_text,
            "output": output_text[:200] + "..." if len(output_text) > 200 else output_text,
            "tokens_used": tokens_used,
            "fallback": fallback,
            "confidence": confidence,
            "execution_time": execution_time,
            "elapsed": elapsed,
            "session_elapsed": elapsed
        }
        
        self.events.append(event)
        return event

    def log_parallel_execution(self, agent_results: List[Dict[str, Any]]):
        """Log results from parallel agent execution"""
        elapsed = round(time.time() - self.start, 2)
        
        parallel_event = {
            "timestamp": datetime.now().isoformat(),
            "type": "parallel_execution",
            "agent_count": len(agent_results),
            "results": agent_results,
            "elapsed": elapsed,
            "session_elapsed": elapsed
        }
        
        self.events.append(parallel_event)
        return parallel_event

    def log_evaluation(self, agent: str, evaluation_score: float, 
                      evaluation_metrics: Dict[str, Any]):
        """Log agent evaluation results"""
        elapsed = round(time.time() - self.start, 2)
        
        eval_event = {
            "timestamp": datetime.now().isoformat(),
            "type": "evaluation",
            "agent": agent,
            "score": evaluation_score,
            "metrics": evaluation_metrics,
            "elapsed": elapsed,
            "session_elapsed": elapsed
        }
        
        self.events.append(eval_event)
        return eval_event

    def save(self):
        """Save telemetry data to disk"""
        session_data = {
            "session_id": self.session_id,
            "start_time": datetime.fromtimestamp(self.start).isoformat(),
            "end_time": datetime.now().isoformat(),
            "total_events": len(self.events),
            "events": self.events,
            "summary": self._generate_summary()
        }
        
        with open(self.path, "w") as f:
            json.dump(session_data, f, indent=2)
        
        return session_data

    def _generate_summary(self) -> Dict[str, Any]:
        """Generate summary statistics from telemetry data"""
        if not self.events:
            return {}
        
        # Agent usage statistics
        agent_counts = {}
        total_tokens = 0
        total_execution_time = 0
        fallback_count = 0
        confidence_scores = []
        
        for event in self.events:
            if "agent" in event:
                agent_counts[event["agent"]] = agent_counts.get(event["agent"], 0) + 1
                total_tokens += event.get("tokens_used", 0)
                total_execution_time += event.get("execution_time", 0)
                if event.get("fallback"):
                    fallback_count += 1
                if event.get("confidence"):
                    confidence_scores.append(event["confidence"])
        
        summary = {
            "total_events": len(self.events),
            "agent_usage": agent_counts,
            "total_tokens": total_tokens,
            "total_execution_time": total_execution_time,
            "fallback_count": fallback_count,
            "fallback_rate": fallback_count / len(self.events) if self.events else 0,
            "avg_confidence": sum(confidence_scores) / len(confidence_scores) if confidence_scores else 0,
            "session_duration": time.time() - self.start
        }
        
        return summary

    def get_session_stats(self) -> Dict[str, Any]:
        """Get real-time session statistics"""
        return self._generate_summary()

    def export_to_csv(self, output_path: str):
        """Export telemetry data to CSV format"""
        import csv
        
        with open(output_path, 'w', newline='') as csvfile:
            fieldnames = ['timestamp', 'agent', 'input', 'output', 'tokens_used', 
                         'fallback', 'confidence', 'execution_time', 'elapsed']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for event in self.events:
                if "agent" in event:  # Only log agent events, not system events
                    writer.writerow({
                        'timestamp': event['timestamp'],
                        'agent': event['agent'],
                        'input': event['input'],
                        'output': event['output'],
                        'tokens_used': event.get('tokens_used', 0),
                        'fallback': event.get('fallback', ''),
                        'confidence': event.get('confidence', 0),
                        'execution_time': event.get('execution_time', 0),
                        'elapsed': event.get('elapsed', 0)
                    })

    def clear_session(self):
        """Clear current session data (use with caution)"""
        self.events = []
        self.start = time.time() 