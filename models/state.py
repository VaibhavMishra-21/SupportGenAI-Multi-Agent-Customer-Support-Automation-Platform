from typing import TypedDict

class SupportState(TypedDict):
    query: str
    intent: str
    sentiment: str
    context: str
    response: str
    confidence: float
    escalated: bool
