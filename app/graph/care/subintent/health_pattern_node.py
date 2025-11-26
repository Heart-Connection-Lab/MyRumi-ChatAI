from app.graph.state import GraphState

def health_pattern_node(state: GraphState):
    return {
        **state,
        "reply": (
            "요즘 기력이나 컨디션이 많이 떨어지신 것 같아요."
            "최근 수면이나 식사 패턴에 변화가 있었나요?"
            "필요하시면 건강 체크도 도와드릴게요."
        )
    }
