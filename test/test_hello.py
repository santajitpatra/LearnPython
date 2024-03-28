from hello import hello


def test_hello_default():
    assert hello() == "Hello, World"


def test_hello_custom():
    assert hello("Bob") == "Hello, Bob"
    assert hello("Alice") == "Hello, Alice"

def test_hello_empty():
    for name in ["Bob", "Alice", "charlie", ""]:
        assert hello(name) == f"Hello, {name}"