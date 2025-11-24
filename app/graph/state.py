from typing import TypedDict


class GraphState(TypedDict):
    """그래프 전체에서 공유되는 상태"""
    user_input: str
    reply: str
