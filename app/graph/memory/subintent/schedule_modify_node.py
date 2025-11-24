from app.graph.state import GraphState

def schedule_modify_node(state: GraphState):
    return {
        **state,
        "reply": "어떤 일정을 수정하고 싶으신가요? 변경할 날짜나 시간을 알려주세요."
    }
