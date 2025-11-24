from app.graph.state import GraphState

def repetitive_question_node(state: GraphState):
    return {
        **state,
        "reply": "방금 말씀드렸던 내용을 다시 설명해드릴게요 😊 (향후 컨텍스트 기반으로 이전 답변 자동 복원)"
    }
