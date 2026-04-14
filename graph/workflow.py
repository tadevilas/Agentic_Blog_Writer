from typing import TypedDict
from agents.research_agent import research_agent
from agents.blog_agent import blog_agent

from langgraph.graph import StateGraph, START, END


class Blogstage(TypedDict):
    query: str
    research_summary: str
    blog: str

async def research_node(state: Blogstage):
    
    query = state['query']
    
    research = await research_agent(query)
    
    return {"research_summary": research}

async def blog_node(state: Blogstage):
    
    research = state['research_summary']
    
    blog = await blog_agent(research)
    
    return {"blog": blog}


builder = StateGraph(Blogstage)
builder.add_node("research", research_node)
builder.add_node("blog_writer", blog_node)


builder.add_edge(START, "research")
builder.add_edge("research", "blog_writer")
builder.add_edge("blog_writer", END)

graph = builder.compile()