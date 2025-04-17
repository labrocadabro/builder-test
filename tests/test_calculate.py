import pytest
from src.calculate import calculate

def test_add_two_numbers():
    assert calculate('add', 2, 3) == 5

def test_add_multiple_numbers():
    assert calculate('add', 1, 2, 3, 4) == 10

def test_subtract_two_numbers():
    assert calculate('subtract', 10, 4) == 6

def test_subtract_multiple_numbers():
    assert calculate('subtract', 20, 5, 3) == 12

def test_multiply_two_numbers():
    assert calculate('multiply', 2, 3) == 6

def test_multiply_multiple_numbers():
    assert calculate('multiply', 2, 3, 4) == 24

def test_divide_two_numbers():
    assert calculate('divide', 10, 2) == 5

def test_divide_multiple_numbers():
    assert calculate('divide', 100, 2, 5) == 10

def test_invalid_operation():
    with pytest.raises(ValueError, match="Invalid operation"):
        calculate('power', 2, 3)

def test_insufficient_arguments():
    with pytest.raises(ValueError):
        calculate('add', 5)

def test_non_numeric_arguments():
    with pytest.raises(TypeError):
        calculate('add', 1, '2', 3)

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculate('divide', 10, 0)

def test_floating_point_calculation():
    assert abs(calculate('divide', 10, 3) - 3.3333333) < 1e-6