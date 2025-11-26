from app.graph.state import GraphState

def emotion_analysis_node(state: GraphState):
    emotion = state.get("care_type", None)
    print("emotion_analysis_node에서 받은 care_type =", emotion)


    # -----------------------
    # 1) 긍정
    # -----------------------
    if emotion == "emotion_positive":
        reply = (
            "오늘 감정이 참 긍정적으로 느껴져요 😊"
            "기분 좋은 하루를 보내신 것 같아 정말 다행이에요!"
        )

    # -----------------------
    # 2) 평온
    # -----------------------
    elif emotion == "emotion_neutral":
        reply = (
            "오늘은 차분하고 평온한 하루를 보내신 것 같아요 🙂"
            "특별히 불편한 감정은 없으셨던 걸로 느껴져요."
        )

    # -----------------------
    # 3) 활기
    # -----------------------
    elif emotion == "emotion_energetic":
        reply = (
            "오늘 굉장히 활기차고 에너지가 느껴지는 하루였네요! 💪✨"
            "좋은 흐름이 계속되면 좋겠어요!"
        )

    # -----------------------
    # 4) 피로
    # -----------------------
    elif emotion == "emotion_tired":
        reply = (
            "오늘은 조금 피곤한 하루였던 것 같아요 😔"
            "잠깐이라도 쉬어가는 시간 가지시는 게 좋을 것 같아요."
        )

    # -----------------------
    # 5) 불안/걱정
    # -----------------------
    elif emotion == "emotion_anxious":
        reply = (
            "오늘은 조금 걱정되거나 마음이 불안정하셨나봐요 😢"
            "혹시 마음을 무겁게 만든 일이 있었을까요?"
            "제가 옆에서 계속 도와드릴게요."
        )

    # -----------------------
    # 6) 기타 건강 패턴
    # -----------------------
    else:
        reply = (
            "감정과 관련된 특별한 표현을 찾지 못했어요."
            "혹시 몸 상태나 기분에서 변화가 있었을까요?"
        )

    return {**state, "reply": reply}
