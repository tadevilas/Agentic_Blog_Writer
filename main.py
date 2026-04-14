import asyncio
from graph.workflow import graph
import os

async def main():
    query = "Future of electric vehicles in India"
    result = await graph.ainvoke(
        {
            "query": query
        }
    )

    print("\nFINAL BLOG:\n")
    print(result["blog"])

    # Extract content from AIMessage
    blog_content = result["blog"].content

    os.makedirs("blogs", exist_ok=True)

    filename = query.replace(" ", "_").lower() + ".md"
    filepath = f"blogs/{filename}"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(blog_content)

    print("\nBlog generated successfully!")
    print(f"Saved to: {filepath}")

asyncio.run(main())