from langchain_groq import ChatGroq
from dotenv import load_dotenv
from tools.search_tool import tavily_search
from tools.rag_tool import rag_search


load_dotenv()

llm = ChatGroq(
    model_name="openai/gpt-oss-20b",
    temperature=0.0,
)

async def research_agent(query: str):
    
     # retrieve internal knowledge
    rag_context = await rag_search.ainvoke({"query": query})
    
    print(rag_context)
    
    # retrieve internet knowledge
    internet_context = await tavily_search(query)
    print(internet_context)
    combined_context = f"""
INTERNAL KNOWLEDGE (RAG):
{rag_context}

INTERNET SEARCH:
{internet_context}
"""
    prompt = f"""
    You are a research assistant.

    Based on the following search results, create a structured research summary.

    SEARCH RESULTS:
    {combined_context}

    Create output in this format:

    Topic:
    Key Insights:
    Important Facts:
    Sources:
    
    """
    
    response = await llm.ainvoke(prompt)
    
    return response.content
    