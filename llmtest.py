
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv


load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")

# llm = ChatOpenAI(model="gpt-4.1-mini")
llm = ChatGroq(
    model_name="openai/gpt-oss-20b",
)

response = llm.invoke("Explain AI in one sentence")

print(response.content)


import asyncio
from tools.search_tool import tavily_search


async def main():

    result = await tavily_search("Future of electric vehicles in India")

    print(result)


asyncio.run(main())