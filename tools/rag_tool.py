from langchain.tools import tool
from rag.retriever import retriever


@tool
async def rag_search(query: str) -> str:
    """
    Search the user query in the internal knowledge base which is stored locally.
    if the relevant doc is not present then return empty string.
    
    """
    
    docs = retriever.invoke(query)
    
    ls = []
    for i in docs:
        ls.append(i.page_content)
        
    context = ls[0]
    return context