from langchain.tools import tool
from tools.github_mcp_client import GitHubMCPClient


github_client = GitHubMCPClient()

@tool
async def github_repo_tool(query: str) -> str:
    """
    Use this tool when the user provides a GitHub repository URL.
    """

    if "github.com" not in query:
        return "No GitHub repo found."

    await github_client.connect()
    
    tools = await github_client.session.list_tools()
    print(tools)
    
    # NOTE: tool name depends on MCP server
    result = await github_client.call_tool(
        "get_repository",
        {"url": query}
    )

    return str(result)