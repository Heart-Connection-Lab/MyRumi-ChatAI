from typing import TypedDict, Optional

class GraphState(TypedDict, total=False):
    user_input: str
    reply: str

    # Intent Level
    intent: Optional[str]

    # Subintent Level
    connect_type: Optional[str]
    memory_type: Optional[str]
    care_type: Optional[str]
