from app.graph.state import GraphState

def connect_subintent_node(state: GraphState):
    text = state["user_input"]

    # 복지 연결 (welfare)
    welfare_keywords = ["취미", "배우고", "배우고싶어", "해보고", "가고싶어", "참여", "수업", "활동"]
    if any(word in text for word in welfare_keywords):
        return {**state, "connect_type": "welfare"}

    # 가족 연결 (family)
    family_keywords = ["가족", "아들", "딸", "손주", "남편", "전화", "보고싶어", "그립다"]
    if any(word in text for word in family_keywords):
        return {**state, "connect_type": "family"}

    # 둘 다 아닌 경우 fallback
    return {**state, "connect_type": "fallback"}
