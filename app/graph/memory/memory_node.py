from app.graph.state import GraphState

def memory_node(state: GraphState):
    """
    memory intent에 진입하면 바로 subintent 분류로 넘긴다.
    """
    return state
