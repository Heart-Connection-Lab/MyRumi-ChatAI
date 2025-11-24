from app.graph.state import GraphState

def schedule_create_node(state: GraphState):
    return {
        **state,
        "reply": "어떤 일정인지 말씀해주세요. 날짜와 시간을 함께 말해주시면 캘린더에 등록해드릴게요 😊"
    }
