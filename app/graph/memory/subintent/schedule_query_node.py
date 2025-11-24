from app.graph.state import GraphState

def schedule_query_node(state: GraphState):
    return {
        **state,
        "reply": "오늘과 내일의 일정을 알려드릴게요! (추후 캘린더 데이터와 연동 예정)"
    }
