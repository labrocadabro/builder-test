import pytest
from src.arithmetic import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(1.5, 2.5) == 4.0
    with pytest.raises(TypeError):
        add("2", 3)
    with pytest.raises(TypeError):
        add(2, "3")

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(5.5, 2.5) == 3.0
    with pytest.raises(TypeError):
        subtract("5", 3)
    with pytest.raises(TypeError):
        subtract(5, "3")

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(1.5, 2) == 3.0
    with pytest.raises(TypeError):
        multiply("2", 3)
    with pytest.raises(TypeError):
        multiply(2, "3")

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 2) == -3
    assert divide(5, 2) == 2.5
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
    with pytest.raises(TypeError):
        divide("6", 3)
    with pytest.raises(TypeError):
        divide(6, "3")