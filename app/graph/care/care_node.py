from app.graph.state import GraphState

def care_node(state: GraphState):
    """
    care intent에 진입하면 바로 subintent 분류로 넘긴다.
    """
    print("🟢 CARE NODE REACHED with state:", state)
    return state
