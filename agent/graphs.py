from langgraph.graph import StateGraph, END
from agent.states import AgentState

from agent.nodes import (
    search_web,
    scrape_webpages,
    analyze_research,
    save_report
)

# =========================
# CREATE GRAPH
# =========================

workflow = StateGraph(AgentState)


# =========================
# ADD NODES
# =========================

workflow.add_node("search_web", search_web)
workflow.add_node("scrape_webpages", scrape_webpages)
workflow.add_node("save_report", save_report)
workflow.add_node("analyze_research",analyze_research)


# =========================
# DEFINE FLOW
# =========================

workflow.set_entry_point("search_web")

workflow.add_edge("search_web", "scrape_webpages")
# workflow.add_edge("scrape_webpages", "save_report")
workflow.add_edge("scrape_webpages","analyze_research")
workflow.add_edge("analyze_research","save_report")
workflow.add_edge("save_report", END)


# =========================
# COMPILE GRAPH
# =========================

graph = workflow.compile()