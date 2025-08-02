import json
import time
from typing import Dict, Any, Optional
from datetime import datetime

class AgentDebugViewer:
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.debug_log = []
    
    def log_synthetic_meta(self, agent_name: str, synthetic_meta: Dict[str, Any], 
                          fallback_pattern: Optional[str] = None) -> None:
        """Log synthetic reasoning metadata for debugging"""
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        debug_entry = {
            "timestamp": timestamp,
            "agent_name": agent_name,
            "synthetic_thoughts": synthetic_meta.get("synthetic_thoughts", []),
            "synthetic_queries": synthetic_meta.get("synthetic_queries", []),
            "risk_score": synthetic_meta.get("risk_score", 0.0),
            "fallback_pattern": fallback_pattern,
            "pattern_triggered": fallback_pattern is not None
        }
        
        self.debug_log.append(debug_entry)
        
        if self.verbose:
            self._print_debug_output(debug_entry)
    
    def _print_debug_output(self, debug_entry: Dict[str, Any]) -> None:
        """Print formatted debug output to terminal"""
        
        print(f"\n{'='*60}")
        print(f"🧠 AGENT DEBUG: {debug_entry['agent_name']} ({debug_entry['timestamp']})")
        print(f"{'='*60}")
        
        print(f"⚠️  Risk Score: {debug_entry['risk_score']:.2f}")
        
        if debug_entry['fallback_pattern']:
            print(f"🔄 Fallback Pattern: {debug_entry['fallback_pattern']}")
            print(f"🚨 Pattern Triggered: {debug_entry['pattern_triggered']}")
        
        print(f"\n🧠 Synthetic Thoughts ({len(debug_entry['synthetic_thoughts'])}):")
        for i, thought in enumerate(debug_entry['synthetic_thoughts'], 1):
            print(f"  {i}. {thought}")
        
        print(f"\n❓ Internal Questions ({len(debug_entry['synthetic_queries'])}):")
        for i, query in enumerate(debug_entry['synthetic_queries'], 1):
            print(f"  {i}. {query}")
        
        print(f"{'='*60}\n")
    
    def get_debug_summary(self) -> Dict[str, Any]:
        """Get summary statistics of debug session"""
        if not self.debug_log:
            return {"total_runs": 0, "average_risk": 0.0, "patterns_triggered": 0}
        
        total_runs = len(self.debug_log)
        average_risk = sum(entry['risk_score'] for entry in self.debug_log) / total_runs
        patterns_triggered = sum(1 for entry in self.debug_log if entry['pattern_triggered'])
        
        return {
            "total_runs": total_runs,
            "average_risk": round(average_risk, 3),
            "patterns_triggered": patterns_triggered,
            "agents_used": list(set(entry['agent_name'] for entry in self.debug_log))
        }
    
    def save_debug_log(self, filename: str = "debug_session.json") -> None:
        """Save debug log to JSON file"""
        with open(filename, 'w') as f:
            json.dump({
                "session_timestamp": datetime.now().isoformat(),
                "debug_entries": self.debug_log,
                "summary": self.get_debug_summary()
            }, f, indent=2)
        
        print(f"📁 Debug log saved to: {filename}")
    
    def clear_log(self) -> None:
        """Clear the debug log"""
        self.debug_log = []
        print("🧹 Debug log cleared")

# Global debug viewer instance
debug_viewer = AgentDebugViewer()

def set_debug_verbose(verbose: bool) -> None:
    """Set debug verbosity level"""
    global debug_viewer
    debug_viewer.verbose = verbose

def log_agent_debug(agent_name: str, synthetic_meta: Dict[str, Any], 
                   fallback_pattern: Optional[str] = None) -> None:
    """Convenience function to log agent debug info"""
    debug_viewer.log_synthetic_meta(agent_name, synthetic_meta, fallback_pattern)

def get_debug_summary() -> Dict[str, Any]:
    """Get debug session summary"""
    return debug_viewer.get_debug_summary()

def save_debug_session(filename: str = None) -> None:
    """Save current debug session"""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"debug_session_{timestamp}.json"
    debug_viewer.save_debug_log(filename) 