from app.graph.state import GraphState

def welfare_connect_node(state: GraphState):
    text = state["user_input"]

    # 실제 구현은 나중에 공공데이터 API 연동
    # 지금은 간단한 더미 응답
    return {
        **state,
        "reply": f"'{text}' 관련 복지 프로그램을 찾아봤어요! 곧 더 정확한 추천을 드릴 수 있도록 준비하고 있어요 😊"
    }
