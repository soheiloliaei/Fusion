import sys
sys.path.append('~/fusion_v13')

from core.execution_chain_orchestrator import ExecutionChainOrchestrator

def test_cd_layer():
    orchestrator = ExecutionChainOrchestrator()
    result = orchestrator.run_with_creative_director("This output is too verbose and lacks clarity.")
    print("🎯 Enhanced Output:", result["final_output"])
    print("💬 Creative Feedback:", result["creative_director_feedback"])
    print("⬆️ Score Lift:", result["score_lift"])

if __name__ == "__main__":
    test_cd_layer()
