from app.graph.state import GraphState

def care_node(state: GraphState):
    text = state["user_input"]
    return {
        **state,
        "reply": f"[Care] '{text}' 들었어요. 몸 상태는 괜찮으세요?"
    }

