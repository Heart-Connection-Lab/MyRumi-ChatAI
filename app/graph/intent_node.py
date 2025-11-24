# app/graph/intent_node.py

from app.graph.state import GraphState

def intent_node(state: GraphState):
    print("🟠 intent_node 실행")

    text = state["user_input"]
    text_clean = text.replace(" ", "")

    # ------------------------------
    # CONNECT 범위 확장
    # ------------------------------
    connect_keywords = [
        "안녕", "고마워", "오늘", "날씨", "대화", "응", "그래",

        # 복지 연결 관련
        "배우", "배우고", "배우고싶", "하고싶", "가보고", "가고싶",
        "취미", "활동", "수업", "강좌", "참여", "프로그램",

        # 가족 연결 관련
        "가족", "아들", "딸", "손주", "남편", "아내",
        "보고싶", "그립", "전화"
    ]

    if any(kw in text_clean for kw in connect_keywords):
        intent = "connect"

    # ------------------------------
    # MEMORY
    # ------------------------------
    elif any(word in text for word in ["약", "알람", "일정", "기억", "스케줄", "리마인드"]):
        intent = "memory"

    # ------------------------------
    # CARE
    # ------------------------------
    elif any(word in text for word in ["아파", "통증", "혈압", "숨막혀", "기운", "우울", "위험"]):
        intent = "care"

    # ------------------------------
    # FALLBACK
    # ------------------------------
    else:
        intent = "fallback"

    return {
        **state,
        "intent": intent
    }
