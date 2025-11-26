from app.graph.state import GraphState

def risk_keyword_node(state: GraphState):
    care_type = state.get("care_type", None)
    print("emotion_analysis_node에서 받은 care_type =", care_type)
    return {
        **state,
        "reply": (
            "지금 많이 위험해 보이세요 ⚠️"
            "바로 도움을 요청해야 할 것 같아요."
            "지금 가까운 사람이나 119에 바로 연락하실 수 있도록 도와드릴게요"
        )
    }
