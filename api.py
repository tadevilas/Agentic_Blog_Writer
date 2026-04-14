from fastapi import FastAPI
from pydantic import BaseModel
import os

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

    filename = query.replace(" ", "_").lower() + ".md"
    filepath = f"blogs/{filename}"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(blog_content)

    return {"filepath": f"File Saved on Below Location {filepath}" } # 