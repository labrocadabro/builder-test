import pytest
from src.fraction import Fraction

def test_fraction_initialization():
    """Test basic fraction initialization"""
    # Simple fraction
    f1 = Fraction(3, 4)
    assert f1.numerator == 3
    assert f1.denominator == 4
    
    # Mixed number
    f2 = Fraction(1, 2, 1)  # 1 1/2
    assert f2.numerator == 3
    assert f2.denominator == 2
    
    # Negative mixed number
    f3 = Fraction(1, 2, -1)  # -1 1/2
    assert f3.numerator == -3
    assert f3.denominator == 2

def test_fraction_string_representation():
    """Test string representations"""
    # Whole number
    f1 = Fraction(4, 1)
    assert str(f1) == "4"
    
    # Simple fraction
    f2 = Fraction(3, 4)
    assert str(f2) == "3/4"
    
    # Mixed number
    f3 = Fraction(1, 2, 1)
    assert str(f3) == "1 1/2"
    
    # Negative mixed number
    f4 = Fraction(1, 2, -1)
    assert str(f4) == "-1 1/2"

def test_fraction_from_string():
    """Test creating fractions from string representations"""
    # Integer
    f1 = Fraction.from_string("5")
    assert f1 == Fraction(5)
    
    # Simple fraction
    f2 = Fraction.from_string("3/4")
    assert f2 == Fraction(3, 4)
    
    # Mixed number
    f3 = Fraction.from_string("1 1/2")
    assert f3 == Fraction(1, 2, 1)
    
    # Negative mixed number
    f4 = Fraction.from_string("-1 1/2")
    assert f4 == Fraction(1, 2, -1)

def test_fraction_arithmetic():
    """Test arithmetic operations"""
    # Addition
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)
    assert f1 + f2 == Fraction(3, 4)
    assert f1 + 1 == Fraction(3, 2)
    
    # Subtraction
    assert f1 - f2 == Fraction(1, 4)
    assert f1 - 1 == Fraction(-1, 2)
    
    # Multiplication
    assert f1 * f2 == Fraction(1, 8)
    assert f1 * 2 == Fraction(1, 1)
    
    # Division
    assert f1 / f2 == Fraction(2, 1)
    assert f1 / 2 == Fraction(1, 4)

def test_decimal_conversion():
    """Test decimal conversion"""
    f1 = Fraction(1, 2)
    assert f1.to_decimal() == 0.5
    
    f2 = Fraction(1, 3)
    assert abs(f2.to_decimal() - 0.3333) < 0.0001

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Invalid type inputs
    with pytest.raises(TypeError):
        Fraction("1", 2)
    
    # Division by zero
    with pytest.raises(ValueError):
        Fraction(1, 0)
    
    # Parsing invalid string
    with pytest.raises(ValueError):
        Fraction.from_string("invalid")