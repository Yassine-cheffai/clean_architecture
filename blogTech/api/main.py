from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class Post(BaseModel):
    title: str
    description: str

@app.get("/")
def read_posts():
    with open("posts.csv", "r") as f:
        lines = f.readlines()
        result = [line.strip().split(",") for line in lines[1:]]
        result = [{"title": line[0], "description": line[1]}for line in result]
        return result

@app.post("/posts/new")
def new_post(post: Post):
    with open("posts.csv", "a") as f:
        f.write("\n")
        f.write(",".join([post.title, post.description]))
    return "success"

@app.get("/posts/search")
def search_posts(q: Union[str, None] = None):
    if q is None:
        return "specify a query"
    result = []
    try:
        with open("posts.csv", "r") as f:
            lines = [line.strip().split(",") for line in f.readlines()[1:]]
            lines = [{"title": line[0], "description": line[1]}for line in lines]
            for line in lines:
                if q in line["title"] or q in line["description"]:
                    result.append(line)
    except Exception:
        pass
    return result