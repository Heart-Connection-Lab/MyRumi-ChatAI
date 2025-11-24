from app.graph.state import GraphState

def fallback_node(state: GraphState):
    """
    사용자의 입력이 어떤 intent에도 해당하지 않을 때 실행되는 기본 대응 노드.
    """
    user_text = state["user_input"]

    return {
        **state,
        "reply": f"'{user_text}'에 대해 잘 이해하지 못했어요 😢 다시 한 번 말씀해주실 수 있을까요?"
    }
