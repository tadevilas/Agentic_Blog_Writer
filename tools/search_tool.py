import os
from tavily import AsyncTavilyClient
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()

tavily_client = AsyncTavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

@tool
async def tavily_search(query: str):
    """
    Search the internet for latest information using Tavily API.
    Returns relevant search results including title, content, and URL.
    """
    response = await tavily_client.search(
        query=query,
        search_depth="advanced",
        max_results=2
    )

    formatted_results = []
    
    for r in response['results']:
        formatted_results.append(
            f"""
                Title: {r['title']}
                Content: {r['content']}
                URL: {r['url']}
            """
        )

    return "\n".join(formatted_results) 
   
