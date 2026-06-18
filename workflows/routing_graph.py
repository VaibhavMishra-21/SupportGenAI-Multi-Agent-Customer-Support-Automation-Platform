from langgraph.graph import StateGraph

from models.state import SupportState

workflow = StateGraph(
    SupportState
)
