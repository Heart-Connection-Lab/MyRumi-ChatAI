from app.graph.state import GraphState

def memory_fallback_node(state: GraphState):
    text = state["user_input"]
    return {
        **state,
        "reply": f"'{text}'에 대한 연결 요청을 잘 이해하지 못했어요 😢 일정 관련 작업이 필요하신가요?"
    }
