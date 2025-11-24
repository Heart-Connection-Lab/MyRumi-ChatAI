from app.graph.state import GraphState

def connect_fallback_node(state: GraphState):
    text = state["user_input"]
    return {
        **state,
        "reply": f"'{text}'에 대한 연결 요청을 잘 이해하지 못했어요 😢 가족에게 전화하거나, 새로운 활동을 찾고 싶으신가요?"
    }
