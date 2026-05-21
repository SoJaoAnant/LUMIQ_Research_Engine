from typing import TypedDict, List


class AgentState(TypedDict):
    query: str
    search_results: List[dict]
    scraped_contents: List[dict]
    final_report: str
    logs: List[str]
    api_key: str
    