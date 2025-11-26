from app.graph.state import GraphState

def care_subintent_node(state: GraphState):
    text = state["user_input"]
    text_clean = text.replace(" ", "")
    print("🟣 CARE SUBINTENT text_clean:", text_clean)


    # 위험 키워드 (즉시 대응 필요)
    risk_keywords = [
        "쓰러질", "숨이안", "숨이막혀",
        "119", "위험", "살려줘", "도와줘",
        "심장", "호흡곤란"
    ]
    if any(kw in text_clean for kw in risk_keywords):
        return {**state, "care_type": "risk"}

    # Emotion (5가지 세부 감정)
    positive_keywords = ["행복", "기뻐", "좋아", "고마워", "감사", "재밌", "즐거워"]
    neutral_keywords  = ["괜찮아", "별일없어", "차분", "평온", "그럭저럭", "무난"]
    energetic_keywords = ["잘했어", "활기", "좋다", "의욕", "힘이나", "파이팅"]
    tired_keywords = ["기운없", "지쳐", "피곤", "힘들어", "쉬고싶", "지침"]
    anxious_keywords = ["불안", "걱정", "어떡하", "긴장", "초조", "불편"]

    if any(k in text_clean for k in positive_keywords):
        return {**state, "care_type": "emotion_positive"}
    if any(k in text_clean for k in neutral_keywords):
        return {**state, "care_type": "emotion_neutral"}
    if any(k in text_clean for k in energetic_keywords):
        return {**state, "care_type": "emotion_energetic"}
    if any(k in text_clean for k in tired_keywords):
        return {**state, "care_type": "emotion_tired"}
    if any(k in text_clean for k in anxious_keywords):
        return {**state, "care_type": "emotion_anxious"}

    # 건강 패턴 (체력/기운/일상 변화)
    pattern_keywords = [
        "기운", "힘이없어", "컨디션", "어지러",
        "몸이안좋아", "먹기싫어", "잠이안와"
    ]
    if any(kw in text_clean for kw in pattern_keywords):
        return {**state, "care_type": "pattern"}

    # fallback
    return {**state, "care_type": "fallback"}
