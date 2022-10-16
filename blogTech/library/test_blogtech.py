import pytest

from .blogtech import BlogTech
from .blogtech import PostsResult, Post
from .blogtech import TechBlogError


def test_instance_blog(blog):
    assert isinstance(blog, BlogTech)


def test_add_new_post(blog, requests_mock):
    requests_mock.post("http://127.0.0.1:8000/posts/new")
    result = blog.add_post(title="Rust", description="rust programmation")
    assert result == None


def test_get_all_posts(blog, requests_mock):
    requests_mock.get(
        "http://127.0.0.1:8000/",
        json=[
            {"title": "python", "description": "python programming language"},
            {"title": "rust", "description": "rust programming language"},
        ],
    )
    posts: PostsResult = blog.all_posts()
    assert isinstance(posts, PostsResult)


def test_search_posts(blog, requests_mock):
    requests_mock.get(
        "http://127.0.0.1:8000/posts/search?q=rust",
        json=[
            {"title": "rust", "description": "rust programming language"},
        ],
    )
    posts: PostsResult = blog.search("rust")
    assert isinstance(posts, PostsResult)
    
    rust_post: Post = posts[0]
    assert rust_post.title == "rust"


def test_get_all_posts_wrong_http_port(requests_mock):
    requests_mock.get("http://127.0.0.1:8000")
    blog: BlogTech = BlogTech("http://127.0.0.1:1000")
    with pytest.raises(TechBlogError):
        blog.all_posts()
