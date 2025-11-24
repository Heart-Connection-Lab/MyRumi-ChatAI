from fastapi import APIRouter
from app.graph.graph import app_graph

router = APIRouter(prefix="/graph", tags=["graph"])


@router.get("/test")
def test_graph(input: str = "안녕 루미"):
    """입력 텍스트로 LangGraph 테스트"""
    result = app_graph.invoke({"user_input": input})
    return {"input": input, "reply": result["reply"]}
