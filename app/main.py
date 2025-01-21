""" App main """


def greet(name: str) -> str:
    """
    Greet the given name

    Args:
        name (str): Name to greet

    Returns:
        str: Greeting
    """

    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("World"))
