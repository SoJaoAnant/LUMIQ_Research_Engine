import streamlit as st

from agent.graphs import graph


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Research Agent",
    page_icon="🔎",
    layout="wide"
)

# =========================
# TITLE
# =========================

st.title("🔎 Autonomous Research Engine")
st.markdown(
    """
Research any topic using an autonomous AI workflow.

The agent:
- searches the web,
- reads webpages,
- analyzes information,
- generates a final report.
"""
)


# =========================
# INPUT
# =========================

query = st.text_input(
    "Enter your research query:"
)

api_key = st.text_input(
        "OpenRouter API Key",
        type="password"
)

# with st.sidebar:

#     st.header("⚙️ Settings")

#     api_key = st.text_input(
#         "OpenRouter API Key",
#         type="password"
#     )


# =========================
# RUN BUTTON
# =========================

if st.button("Run Research Agent"):

    if not query.strip():
        st.warning("Please enter a query.")
        st.stop()
        
    if not api_key:
        st.warning("Please enter your OpenRouter API key (don't worry, your api key is safe with us)")
        st.stop()

    # =========================
    # INITIAL STATE
    # =========================

    initial_state = {
        "query": query,
        "search_results": [],
        "scraped_contents": [],
        "final_report": "",
        "logs": [],
        "api_key": api_key
    }

    # =========================
    # UI PLACEHOLDERS
    # =========================

    logs_placeholder = st.empty()

    st.subheader("⚙️ Agent Logs")

    # =========================
    # RUN GRAPH
    # =========================

    with st.spinner("Agent is researching..."):

    # =========================
    # DISPLAY LOGS
    # =========================
    
        final_state = None
    
        # result = graph.invoke(initial_state)
        for event in graph.stream(initial_state):
            
            for node_name, state in event.items():

                final_state = state

                latest_logs = state.get("logs", [])

                logs_text = "\n".join(latest_logs)

                logs_placeholder.code(logs_text)

    # logs_text = ""

    # for log in result["logs"]:
        # logs_text += log + "\n"

    # logs_placeholder.code(logs_text)

    # =========================
    # FINAL REPORT
    # =========================

    st.subheader("📄 Final Report")

    st.markdown(final_state["final_report"])

    # =========================
    # DOWNLOAD BUTTON
    # =========================

    st.download_button(
        label="⬇️ Download Report",
        data=final_state["final_report"],
        file_name="research_report.md",
        mime="text/markdown"
    )