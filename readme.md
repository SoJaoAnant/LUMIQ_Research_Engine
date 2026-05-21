# 🔎 Autonomous Research Engine

An agentic AI workflow build that autonomously researches a topic, analyzes web sources, and generates structured research reports.

Built using LangGraph-style workflows, Streamlit, OpenRouter, and modular tool-based orchestration.

---

# Features

* 🌐 Autonomous web research using DuckDuckGo search
* 📖 Webpage scraping and content extraction using BeautifulSoup
* 🧠 Research analysis and synthesis into a markdown file using LLMs from OpenRouter
* ⚙️ Modular agent workflow architecture
* 📄 Markdown report generation
* ⬇️ Downloadable research reports
* 🔑 User-provided OpenRouter API key support

---

# Workflow Architecture

The agent follows a multi-step autonomous workflow:

```text
User Query
    ↓
Search Web
    ↓
Scrape Webpages
    ↓
Analyze Research
    ↓
Generate Final Report
```

Each step is implemented as an independent node connected through a graph-based workflow.

---

# Tech Stack

* Python
* Streamlit
* LangGraph
* OpenRouter API
* BeautifulSoup4
* DuckDuckGo Search
* OpenAI SDK

---

# OpenRouter API Key

This project uses OpenRouter for LLM inference.

Because of budget constraints, I cannot provide with my own API key with a backend support, but you can get your own API key and use the service on the generous free trial

Get an API key from:
https://openrouter.ai/settings/keys

Paste your API key into the API section before running the agent.

---

# Example Queries

* Explain why octopuses have three hearts
* What are agentic AI systems?
* Is it possible for AI agents to attain sentinence?
* What is the 67 trend?

---

# Limitations

- Some websites restrict or block scraping, which can reduce the quality or quantity of retrieved research content.

- The generated reports are concise and optimized for fast inference, which may sometimes omit deeper contextual analysis.

- The current workflow is single-agent and linear, meaning it does not yet support iterative planning, self-reflection, or dynamic task decomposition.

# What to improve next

- Add multi-agent collaboration, where separate agents handle searching, verification, summarization, and report generation independently.
- Introduce structured outputs using Pydantic for cleaner report formatting and easier downstream integrations.
- Add source credibility scoring and citation ranking to improve research reliability.
- Support conversational follow-up queries and iterative refinement of generated reports.

# Demo

[https://drive.google.com/drive/folders/163SniZV8WPr-yMUgzlZJjtdAiH4z13uK?usp=sharing]

---
