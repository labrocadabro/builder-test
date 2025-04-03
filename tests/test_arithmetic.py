"""
Tests for Arithmetic Operations Module
"""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from arithmetic import add, subtract, multiply, divide, modulo

def test_add():
    """Test addition operation"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(1.5, 2.5) == 4.0

def test_add_type_error():
    """Test type error handling for addition"""
    with pytest.raises(TypeError):
        add("2", 3)
    with pytest.raises(TypeError):
        add(2, "3")

def test_subtract():
    """Test subtraction operation"""
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(3.5, 1.5) == 2.0

def test_subtract_type_error():
    """Test type error handling for subtraction"""
    with pytest.raises(TypeError):
        subtract("5", 3)
    with pytest.raises(TypeError):
        subtract(5, "3")

def test_multiply():
    """Test multiplication operation"""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(1.5, 2) == 3.0

def test_multiply_type_error():
    """Test type error handling for multiplication"""
    with pytest.raises(TypeError):
        multiply("2", 3)
    with pytest.raises(TypeError):
        multiply(2, "3")

def test_divide():
    """Test division operation"""
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    """Test division by zero"""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_divide_type_error():
    """Test type error handling for division"""
    with pytest.raises(TypeError):
        divide("6", 3)
    with pytest.raises(TypeError):
        divide(6, "3")

def test_modulo():
    """Test modulo operation"""
    assert modulo(7, 3) == 1
    assert modulo(-7, 3) == -1
    assert modulo(10, 3) == 1

def test_modulo_by_zero():
    """Test modulo by zero"""
    with pytest.raises(ZeroDivisionError):
        modulo(5, 0)

def test_modulo_type_error():
    """Test type error handling for modulo"""
    with pytest.raises(TypeError):
        modulo("7", 3)
    with pytest.raises(TypeError):
        modulo(7, "3")