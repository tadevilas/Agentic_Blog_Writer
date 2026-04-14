from mcp.client.stdio import stdio_client


class GitHubMCPClient:

    def __init__(self):
        self.session = None

    async def connect(self):
        if self.session is None:
            self.session = await stdio_client(
                command="npx",
                args=["@modelcontextprotocol/server-github"]
            )

    async def call_tool(self, tool_name, params):
        return await self.session.call_tool(tool_name, params)


# github_client = GitHubMCPClient()