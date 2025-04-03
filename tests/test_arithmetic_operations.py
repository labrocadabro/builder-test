"""
Test suite for arithmetic operations.
"""

import pytest
from src.arithmetic_operations import add, subtract, multiply, divide

def test_add_positive_numbers():
    """Test adding positive numbers."""
    assert add(2, 3) == 5
    assert add(0, 0) == 0

def test_add_negative_numbers():
    """Test adding negative numbers."""
    assert add(-2, -3) == -5
    assert add(2, -3) == -1

def test_add_floating_point():
    """Test adding floating point numbers."""
    assert add(2.5, 3.5) == 6.0

def test_add_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        add("2", 3)
    with pytest.raises(TypeError):
        add(2, "3")
    with pytest.raises(TypeError):
        add(None, 3)

def test_subtract_positive_numbers():
    """Test subtracting positive numbers."""
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0

def test_subtract_negative_numbers():
    """Test subtracting negative numbers."""
    assert subtract(-2, -3) == 1
    assert subtract(2, -3) == 5

def test_subtract_floating_point():
    """Test subtracting floating point numbers."""
    assert subtract(5.5, 2.5) == 3.0

def test_subtract_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        subtract("5", 3)
    with pytest.raises(TypeError):
        subtract(5, "3")
    with pytest.raises(TypeError):
        subtract(None, 3)

def test_multiply_positive_numbers():
    """Test multiplying positive numbers."""
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0

def test_multiply_negative_numbers():
    """Test multiplying negative numbers."""
    assert multiply(-2, -3) == 6
    assert multiply(2, -3) == -6

def test_multiply_floating_point():
    """Test multiplying floating point numbers."""
    assert multiply(2.5, 2) == 5.0

def test_multiply_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        multiply("2", 3)
    with pytest.raises(TypeError):
        multiply(2, "3")
    with pytest.raises(TypeError):
        multiply(None, 3)

def test_divide_positive_numbers():
    """Test dividing positive numbers."""
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5

def test_divide_negative_numbers():
    """Test dividing negative numbers."""
    assert divide(-6, -3) == 2
    assert divide(6, -3) == -2

def test_divide_floating_point():
    """Test dividing floating point numbers."""
    assert divide(5.0, 2.0) == 2.5

def test_divide_by_zero():
    """Test error handling for division by zero."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_divide_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        divide("6", 3)
    with pytest.raises(TypeError):
        divide(6, "3")
    with pytest.raises(TypeError):
        divide(None, 3)