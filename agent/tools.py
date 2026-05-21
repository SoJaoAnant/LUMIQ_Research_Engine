from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from agent.prompts import RESEARCH_ANALYSIS_PROMPT
from agent.prompts import SHORT_RESEARCH_ANALYSIS_PROMPT
from typing import TypedDict, List
from ddgs import DDGS
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv
import requests
import os

load_dotenv()

def duckduckgo_search_tool(query: str, max_results: int = 5):
    results = []

    blocked_domains = [
        "tiktok.com",
        "youtube.com",
        "instagram.com"
    ]

    with DDGS() as ddgs:
        search_results = ddgs.text(
            query,
            max_results=max_results
        )

        for result in search_results:
            url = result.get("href", "")

            if any(domain in url for domain in blocked_domains):
                continue
            if url.endswith(".pdf"):
                continue

            results.append({
                "title": result.get("title", ""),
                "href": url,
                "body": result.get("body", "")
            })

    return results


def scrape_webpage_tool(url: str):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        )
    }
    
    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove noisy tags
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(
        separator=" ",
        strip=True
    )

    # Limit context size
    text = text[:5000]

    return text

def save_markdown_report_tool(report_text: str):
    os.makedirs("reports", exist_ok=True)

    report_path = "reports/final_report.md"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    return report_path

def get_openrouter_client(api_key: str):

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    return client

def analyze_research_tool(scraped_contents: list, api_key: str):
    combined_content = ""

    for idx, item in enumerate(scraped_contents):
        combined_content += f"""
                SOURCE {idx + 1}

                Title:
                {item['title']}

                Content:
                {item['content']}
            """

    prompt = RESEARCH_ANALYSIS_PROMPT.format( content=combined_content[:12000])
    
    # prompt = SHORT_RESEARCH_ANALYSIS_PROMPT.format( content=combined_content[:3000])

    client = get_openrouter_client(api_key)
    
    response = client.chat.completions.create(
        model="google/gemini-2.5-flash",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens = 1000
    )

    return response.choices[0].message.content
    # return response.content