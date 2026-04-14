from langchain_groq import ChatGroq
from dotenv import load_dotenv
from tools.search_tool import tavily_search
from tools.rag_tool import rag_search
from tools.github_tool import github_repo_tool

# from langgraph.prebuilt import create_react_agent
from langchain.agents import create_agent

load_dotenv()

llm = ChatGroq(
    model_name="openai/gpt-oss-20b",
    temperature=0.0,
)

tools = [
    rag_search,
    tavily_search,
    github_repo_tool
]

agent = create_agent(
    llm,
    tools=tools,
    system_prompt="""
                    You are a research agent.

                    You have access to tools:
                    - rag_search → internal knowledge
                    - tavily_search → internet search
                    - github_repo_tool → GitHub repo analysis

                    Rules:
                    - If query contains GitHub URL → use github tool
                    - If latest info needed → use tavily
                    - If internal knowledge → use rag
                    - You can use multiple tools if needed
                    """
)


async def research_agent(query: str):

    result = await agent.ainvoke(
        {
            "messages": [
                ("user", query)
            ]
        }
    )

    return result["messages"][-1].content