from .state import GraphState

# 대화 의도에 따른 분기 처리
def route_intent(state: GraphState):
    intent = state["intent"]

    if intent == "connect":
        return "connect_node"
    elif intent == "memory":
        return "memory_node"
    elif intent == "care":
        return "care_node"
    else:
        return "connect_node"