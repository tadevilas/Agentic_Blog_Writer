from fastapi import FastAPI
from pydantic import BaseModel
import os
import re
import datetime

from graph.workflow import graph

app = FastAPI(title="A2A Blog Generator")


class BlogRequest(BaseModel):
    query: str


class BlogResponse(BaseModel):
    blog: str
    file_path: str


@app.post("/generate-blog")
async def generate_blog(request: BlogRequest):

    query = request.query

    result = await graph.ainvoke(
        {
            "query": query
        }
    )

    blog_content = result["blog"].content

    os.makedirs("blogs", exist_ok=True)

    safe_query = re.sub(r'[^a-zA-Z0-9_]', '', query.replace(" ", "_").lower())
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{safe_query}_{timestamp}.md"
    filepath = os.path.join("blogs", filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(blog_content)

    return {
        "message": "Blog generated successfully",
        "filepath": f"File Saved on Below Location {filepath}" 
        } # 