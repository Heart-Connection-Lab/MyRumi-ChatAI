from app.graph.state import GraphState


def memory_subintent_node(state: GraphState):
    text = state["user_input"]
    text_clean = text.replace(" ", "")

    # 일정 생성
    create_keywords = ["일정만들", "일정추가", "일정생성", "새일정", "약속잡아", "기록해", "알람맞춰줘"]

    if any(kw in text_clean for kw in create_keywords):
        return {**state, "memory_type": "schedule_create"}

    # 일정 수정
    modify_keywords = ["일정수정", "시간바꿔", "변경해줘", "수정해줘"]

    if any(kw in text_clean for kw in modify_keywords):
        return {**state, "memory_type": "schedule_modify"}

    # 일정 조회
    query_keywords = ["일정있어", "내일뭐있어", "스케줄", "일정보여줘", "알려줘"]

    if any(kw in text_clean for kw in query_keywords):
        return {**state, "memory_type": "schedule_query"}

    # 반복 질문 (특정 질문 반복)
    repetitive_keywords = ["몇시지", "뭐라했지", "뭐라고했지", "다시말해줘", "기억안나", "뭐라했어"]

    if any(kw in text_clean for kw in repetitive_keywords):
        return {**state, "memory_type": "repetitive_question"}

    # fallback
    return {**state, "memory_type": "fallback"}
