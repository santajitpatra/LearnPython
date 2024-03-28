from calculator import square
import pytest

def test_square_positive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(10) == 100

def test_square_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_square_zero():
    assert square(0) == 0

def test_string():
    with pytest.raises(TypeError):
        square("hello")