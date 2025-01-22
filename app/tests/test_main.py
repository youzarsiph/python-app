""" Main Tests """

from app.main import greet


def test_greet() -> None:
    """greet function test"""

    assert greet("World") == "Hello, World!"
