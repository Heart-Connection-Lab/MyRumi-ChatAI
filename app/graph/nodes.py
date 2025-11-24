#LangGraph에서 실제로 이루어지는 작업(함수)
from .state import GraphState

# 사용자 입력을 state에 기록
def input_node(state: GraphState):
    print("🟢 input_node 실행됨")
    user_text = state["user_input"]

    return {
        "user_input": user_text,
        "reply": ""
    }

# 사용자 응답 생성
def response_node(state: GraphState):
    print("🔵 response_node 실행됨")

    output = f"루미 응답: '{state['user_input']}' 잘 들었어요 😊"

    return {
        "user_input": state["user_input"],
        "reply": output
    }
