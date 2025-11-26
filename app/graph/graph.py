from langgraph.graph import StateGraph
from .state import GraphState

# 기본 노드
from .nodes import input_node
from app.graph.intent_node import intent_node

# intent-level 노드
from app.graph.connect.connect_node import connect_node
from app.graph.memory.memory_node import memory_node
from app.graph.care.care_node import care_node
from app.graph.fallback.fallback_node import fallback_node

# connect subintent 노드
from app.graph.connect.subintent.connect_subintent_node import connect_subintent_node
from app.graph.connect.subintent.welfare_connect_node import welfare_connect_node
from app.graph.connect.subintent.family_connect_node import family_connect_node
from app.graph.connect.subintent.connect_fallback_node import connect_fallback_node

# memory subintent 노드
from app.graph.memory.subintent.memory_subintent_node import memory_subintent_node
from app.graph.memory.subintent.schedule_create_node import schedule_create_node
from app.graph.memory.subintent.schedule_modify_node import schedule_modify_node
from app.graph.memory.subintent.schedule_query_node import schedule_query_node
from app.graph.memory.subintent.repetitive_question_node import repetitive_question_node
from app.graph.memory.subintent.memory_fallback_node import memory_fallback_node

# care subintent 노드
from app.graph.care.subintent.care_subintent_node import care_subintent_node
from app.graph.care.subintent.emotion_analysis_node import emotion_analysis_node
from app.graph.care.subintent.health_pattern_node import health_pattern_node
from app.graph.care.subintent.risk_keyword_node import risk_keyword_node
from app.graph.care.subintent.care_fallback_node import care_fallback_node

# ---- 그래프 정의 ----
graph = StateGraph(GraphState)


# ---- 노드 등록 ----
graph.add_node("input_node", input_node)
graph.add_node("intent_node", intent_node)

graph.add_node("connect_node", connect_node)
graph.add_node("memory_node", memory_node)
graph.add_node("care_node", care_node)
graph.add_node("fallback_node", fallback_node)

# Connect → Subintent
graph.add_node("connect_subintent_node", connect_subintent_node)
graph.add_node("welfare_connect_node", welfare_connect_node)
graph.add_node("family_connect_node", family_connect_node)
graph.add_node("connect_fallback_node", connect_fallback_node)

# Memory → Subintent
graph.add_node("memory_subintent_node", memory_subintent_node)
graph.add_node("schedule_create_node", schedule_create_node)
graph.add_node("schedule_modify_node", schedule_modify_node)
graph.add_node("schedule_query_node", schedule_query_node)
graph.add_node("repetitive_question_node", repetitive_question_node)
graph.add_node("memory_fallback_node", memory_fallback_node)

# Care → Subintent
graph.add_node("care_subintent_node", care_subintent_node)
graph.add_node("emotion_analysis_node", emotion_analysis_node)
graph.add_node("health_pattern_node", health_pattern_node)
graph.add_node("risk_keyword_node", risk_keyword_node)
graph.add_node("care_fallback_node", care_fallback_node)


# ---- Entry point ----
graph.set_entry_point("input_node")

# ---- input → intent ----
graph.add_edge("input_node", "intent_node")


# ---- intent-level 분기 ----
graph.add_conditional_edges(
    "intent_node",
    lambda state: state["intent"],
    {
        "connect": "connect_node",
        "memory": "memory_node",
        "care": "care_node",
        "fallback": "fallback_node",
    }
)

# ---- connect → connect_subintent ----
graph.add_edge("connect_node", "connect_subintent_node")

graph.add_conditional_edges(
    "connect_subintent_node",
    lambda state: state["connect_type"],
    {
        "welfare": "welfare_connect_node",
        "family": "family_connect_node",
        "fallback": "connect_fallback_node",
    }
)

# ---- memory → memory_subintent ----
graph.add_edge("memory_node", "memory_subintent_node")

graph.add_conditional_edges(
    "memory_subintent_node",
    lambda state: state["memory_type"],
    {
        "schedule_create": "schedule_create_node",
        "schedule_modify": "schedule_modify_node",
        "schedule_query": "schedule_query_node",
        "repetitive_question": "repetitive_question_node",
        "fallback": "memory_fallback_node"
    }
)

# ---- care → care_subintent ----
graph.add_edge("care_node", "care_subintent_node")

graph.add_conditional_edges(
    "care_subintent_node",
    lambda state: state["care_type"],
    {
        "emotion_positive": "emotion_analysis_node",
        "emotion_neutral": "emotion_analysis_node",
        "emotion_energetic": "emotion_analysis_node",
        "emotion_tired": "emotion_analysis_node",
        "emotion_anxious": "emotion_analysis_node",

        "pattern": "health_pattern_node",
        "risk": "risk_keyword_node",
        "fallback": "care_fallback_node",
    }
)



# ---- finish points ----
graph.set_finish_point("fallback_node")

graph.set_finish_point("welfare_connect_node")
graph.set_finish_point("family_connect_node")
graph.set_finish_point("connect_fallback_node")

graph.set_finish_point("schedule_create_node")
graph.set_finish_point("schedule_modify_node")
graph.set_finish_point("schedule_query_node")
graph.set_finish_point("repetitive_question_node")
graph.set_finish_point("memory_fallback_node")

graph.set_finish_point("emotion_analysis_node")
graph.set_finish_point("health_pattern_node")
graph.set_finish_point("risk_keyword_node")
graph.set_finish_point("care_fallback_node")


# ---- Compile (그래프 실행) ----
app_graph = graph.compile()
