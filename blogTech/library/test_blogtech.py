import pytest

from .blogtech import BlogTech
from .blogtech import PostsResult
from .blogtech import TechBlogError


def test_instance_blog(blog):
    assert isinstance(blog, BlogTech)


def test_add_new_post(blog, requests_mock):
    requests_mock.post("http://127.0.0.1:8000/posts/new")
    result = blog.add_post(title="Rust", description="rust programmation")
    assert result == None


def test_get_all_posts(blog):
    posts = blog.all_posts()
    assert isinstance(posts, PostsResult)


def test_search_posts(blog):
    posts = blog.search("something")
    assert isinstance(posts, PostsResult)


def test_get_all_posts_wrong_http_port():
    blog = BlogTech("http://127.0.0.1:1000")
    with pytest.raises(TechBlogError):
        blog.all_posts()
