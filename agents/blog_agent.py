from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model_name="openai/gpt-oss-20b",
    temperature=0.0,
)


# Step 1 - Create Blog Plan
async def blog_planner(research_summary: str):
    
    prompt = f"""
    You are an expert blog strategist.

    Based on the research summary below, create a blog outline.

    RESEARCH:
    {research_summary}

    Create a professional blog outline including:

    - Title
    - Target audience
    - Key sections
    - Subsections
    - SEO keywords

    Return a structured outline.
    """

    response = await llm.ainvoke(prompt)

    return response.content


# Step 2 - Write Blog
async def blog_writer(outline: str):
    
    prompt = f"""
    
    You are a professional blog writer.
    
    Using the outline below, write a complete blog article.
    
    OUTLINE: {outline}
    
    Requirements:
    - Use Markdown formate
    - Add headings
    - Add subheadings
    - Use bullet points where useful
    - Write an engaging introduction
    - Add a conclusion
    - Minimum 500 words
    """
    
    response = await llm.ainvoke(prompt)
    
    return response


# Step 3 - Blog Agent

async def blog_agent(research_summary: str):
    
    outline = await blog_planner(research_summary)
    
    blog = await blog_writer(outline)
    
    return blog