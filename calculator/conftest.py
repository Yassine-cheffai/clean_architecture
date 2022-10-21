import pytest
from .main import SimpleCalculator

@pytest.fixture
def calculator():
    return SimpleCalculator()
