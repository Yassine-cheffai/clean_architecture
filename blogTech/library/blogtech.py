from __future__ import annotations
from typing import List, Dict
from dataclasses import dataclass
import json
import requests


@dataclass
class Post:
    title: str
    description: str


class TechBlogError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"TechBlog Error: {self.message}"


class PostsResult:
    def __init__(self, posts: List[Dict]) -> None:
        self.posts = posts
        self.count = 0

    def __iter__(self) -> PostsResult:
        return self

    def __next__(self) -> Post:
        if self.count >= len(self.posts):
            raise StopIteration
        post: dict = self.posts[self.count]
        post_object: Post = Post(title=post["title"], description=post["description"])
        self.count += 1
        return post_object


class HttpRequests:
    def __init__(self, url: str) -> None:
        self.url = url

    def get_all_posts(self) -> PostsResult:
        get_all_posts_url = f"{self.url}/"

        try:
            response = requests.get(get_all_posts_url)
        except:
            raise TechBlogError("unable to connect to BlogTech")

        if not response.status_code == 200:
            raise TechBlogError("error while loading all posts")

        result = PostsResult(response.json())
        return result

    def post_add(self, title: str, description: str) -> None:
        add_new_post_url = f"{self.url}/posts/new"
        payload = {
            "title": title,
            "description": description,
        }
        try:
            response = requests.post(add_new_post_url, data=json.dumps(payload))
        except:
            raise TechBlogError("unable to connect to BlogTech")
        if not response.status_code == 200:
            raise TechBlogError("error while adding new post")

    def get_search_posts(self, query: str) -> PostsResult:
        search_url = f"{self.url}/posts/search"
        try:
            response = requests.get(search_url, params={"q": query})
        except:
            raise TechBlogError("unable to connect to BlogTech")

        if not response.status_code == 200:
            raise TechBlogError(f"error while searching for post with '{query}'")

        results = PostsResult(response.json())
        return results


class BlogTech:
    def __init__(self, url: str) -> None:
        self.httprequest = HttpRequests(url)

    def all_posts(self) -> PostsResult:
        result = self.httprequest.get_all_posts()
        return result

    def add_post(self, title: str, description: str) -> None:
        result = self.httprequest.post_add(title, description)

    def search(self, query: str) -> PostsResult:
        posts = self.httprequest.get_search_posts(query)
        return posts


blog = BlogTech("http://127.0.0.1:8000")
posts = blog.search("rust")
for post in posts:
    print(f"title: {post.title}, description: {post.description}")

print("-----------")
blog.add_post(title="golang", description="golang was developed by google")
posts = blog.search("go")
for post in posts:
    print(f"title: {post.title}, description: {post.description}")