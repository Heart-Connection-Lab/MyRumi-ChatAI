from app.graph.state import GraphState

# 임시 더미 가족 데이터
FAMILY = {
    "아들": "010-1234-5678",
    "딸": "010-2345-6789",
    "손주": "010-9999-8888"
}

def family_connect_node(state: GraphState):
    text = state["user_input"]

    # 가족 대상 찾기
    target = None
    for member in FAMILY.keys():
        if member in text:
            target = member

    if not target:
        return {
            **state,
            "reply": "누구에게 연락드릴까요? 아들, 딸, 손주 중에 말씀해주세요!"
        }

    phone = FAMILY[target]

    # TODO: DB에 family_call_count 증가 로직 넣기

    return {
        **state,
        "reply": f"{target}에게 전화 연결해드릴게요 📞\n({phone})"
    }
