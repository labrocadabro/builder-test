import pytest
from src.fraction_simplifier import simplify_fraction

def test_basic_simplification():
    assert simplify_fraction(8, 12) == "2/3"
    assert simplify_fraction(4, 6) == "2/3"
    assert simplify_fraction(10, 5) == "2/1"

def test_negative_fractions():
    assert simplify_fraction(-8, 12) == "-2/3"
    assert simplify_fraction(8, -12) == "-2/3"
    assert simplify_fraction(-8, -12) == "2/3"

def test_already_simplified_fractions():
    assert simplify_fraction(5, 7) == "5/7"
    assert simplify_fraction(1, 1) == "1/1"

def test_zero_numerator():
    assert simplify_fraction(0, 5) == "0/1"
    assert simplify_fraction(0, -5) == "0/1"

def test_large_numbers():
    assert simplify_fraction(1000000, 10000000) == "1/10"

def test_error_cases():
    # Test division by zero
    with pytest.raises(ValueError, match="Denominator cannot be zero"):
        simplify_fraction(5, 0)
    
    # Test type errors
    with pytest.raises(TypeError, match="Numerator and denominator must be integers"):
        simplify_fraction(5.5, 2)
    
    with pytest.raises(TypeError, match="Numerator and denominator must be integers"):
        simplify_fraction(5, "2")
    
    with pytest.raises(TypeError, match="Numerator and denominator must be integers"):
        simplify_fraction("5", 2)