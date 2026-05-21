from typing import TypedDict, List
from agent.states import AgentState
from agent.tools import scrape_webpage_tool
from agent.tools import duckduckgo_search_tool
from agent.tools import save_markdown_report_tool
from agent.tools import analyze_research_tool
import os


# =========================
# NODE 1 — SEARCH NODE
# =========================

def search_web(state: AgentState) -> AgentState:
    query = state["query"]

    logs = state.get("logs", [])
    logs.append(f"[Search Node] Searching DuckDuckGo for: {query}")

    try:
        results = duckduckgo_search_tool(query)

        logs.append(
            f"[Search Node] Found {len(results)} results."
        )

        state["search_results"] = results

    except Exception as e:
        logs.append(
            f"[Search Node] Error: {str(e)}"
        )

    state["logs"] = logs

    return state


# =========================
# NODE 2 — SCRAPER NODE
# =========================



def scrape_webpages(state: AgentState) -> AgentState:
    logs = state.get("logs", [])
    search_results = state.get("search_results", [])

    scraped_contents = []

    for idx, result in enumerate(search_results):
        url = result.get("href")

        if not url:
            continue

        logs.append(
            f"[Scraper Node] Reading webpage {idx + 1}: {url}"
        )

        try:
            text = scrape_webpage_tool(url)

            scraped_contents.append({
                "title": result.get("title", ""),
                "url": url,
                "content": text
            })

            logs.append(
                f"[Scraper Node] Extracted {len(text)} characters."
            )

        except Exception as e:
            logs.append(
                f"[Scraper Node] Failed to scrape {url} | Error: {str(e)}"
            )

    state["scraped_contents"] = scraped_contents
    state["logs"] = logs

    return state


# =========================
# NODE 3 - RESEARCH ANALYZER
# =========================


def analyze_research(state: AgentState) -> AgentState:
    logs = state.get("logs", [])
    scraped_contents = state.get("scraped_contents", [])
    api_key = state.get("api_key", "")
    
    logs.append(
        "[Analysis Node] Analyzing research sources..."
    )

    try:
        analysis = analyze_research_tool(
            scraped_contents,
            api_key
        )

        state["final_report"] = analysis

        logs.append(
            "[Analysis Node] Research analysis complete."
        )

    except Exception as e:
        logs.append(
            f"[Analysis Node] Error: {str(e)}"
        )

    state["logs"] = logs

    return state

# =========================
# NODE 4 — REPORT WRITER
# =========================

def save_report(state: AgentState) -> AgentState:
    logs = state.get("logs", [])

    logs.append(
        "[Report Node] Saving final report."
    )

    try:
        report_path = save_markdown_report_tool(
            state["final_report"]
        )

        logs.append(
            f"[Report Node] Report saved to: {report_path}"
        )

    except Exception as e:
        logs.append(
            f"[Report Node] Error: {str(e)}"
        )

    state["logs"] = logs

    return state