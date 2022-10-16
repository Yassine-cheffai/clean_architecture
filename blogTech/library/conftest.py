import pytest
from .blogtech import BlogTech


@pytest.fixture
def blog():
    blog = BlogTech("http://127.0.0.1:8000")
    return blog
