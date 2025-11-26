from app.graph.state import GraphState

def care_fallback_node(state: GraphState):
    text = state["user_input"]
    return {
        **state,
        "reply": (
            f"'{text}'에 대해 잘 파악하지 못했어요.\n"
            "혹시 몸 상태나 기분이 안 좋으신 건가요?\n"
            "조금 더 자세히 말씀해주시면 도와드릴게요!"
        )
    }
