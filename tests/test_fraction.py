import pytest
from src.fraction import Fraction

def test_fraction_initialization():
    """Test basic fraction initialization"""
    f = Fraction(3, 4)
    assert f.numerator == 3
    assert f.denominator == 4
    
    # Test auto-simplification
    f2 = Fraction(6, 8)
    assert f2.numerator == 3
    assert f2.denominator == 4
    
    # Test negative fractions
    f3 = Fraction(-3, 4)
    assert f3.numerator == -3
    assert f3.denominator == 4
    
    f4 = Fraction(3, -4)
    assert f4.numerator == -3
    assert f4.denominator == 4

def test_fraction_string_representation():
    """Test string representation of fractions"""
    f = Fraction(3, 4)
    assert str(f) == "3/4"
    
    f2 = Fraction(-3, 4)
    assert str(f2) == "-3/4"

def test_fraction_addition():
    """Test fraction addition"""
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)
    
    result = f1 + f2
    assert result == Fraction(3, 4)
    
    # Test adding an integer
    result2 = f1 + 1
    assert result2 == Fraction(3, 2)

def test_fraction_subtraction():
    """Test fraction subtraction"""
    f1 = Fraction(3, 4)
    f2 = Fraction(1, 4)
    
    result = f1 - f2
    assert result == Fraction(1, 2)
    
    # Test subtracting an integer
    result2 = f1 - 1
    assert result2 == Fraction(-1, 4)

def test_fraction_multiplication():
    """Test fraction multiplication"""
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    
    result = f1 * f2
    assert result == Fraction(1, 6)
    
    # Test multiplying by an integer
    result2 = f1 * 2
    assert result2 == Fraction(1, 1)

def test_fraction_division():
    """Test fraction division"""
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    
    result = f1 / f2
    assert result == Fraction(3, 2)
    
    # Test dividing by an integer
    result2 = f1 / 2
    assert result2 == Fraction(1, 4)

def test_fraction_equality():
    """Test fraction equality"""
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 4)
    f3 = Fraction(1, 3)
    
    assert f1 == f2
    assert f1 != f3

def test_invalid_fraction_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        Fraction("1", 2)
    
    with pytest.raises(TypeError):
        Fraction(1, "2")
    
    with pytest.raises(ValueError):
        Fraction(1, 0)

def test_division_by_zero():
    """Test division by zero handling"""
    f1 = Fraction(1, 2)
    
    with pytest.raises(ValueError):
        f1 / Fraction(0, 1)

def test_zero_fraction():
    """Test fraction with zero numerator"""
    f = Fraction(0, 5)
    assert f.numerator == 0
    assert f.denominator == 1
    assert str(f) == "0/1"