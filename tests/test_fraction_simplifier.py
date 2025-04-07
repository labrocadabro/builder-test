import pytest
from src.fraction_simplifier import simplify_fraction

def test_positive_fraction_simplification():
    assert simplify_fraction(4, 6) == "2/3"
    assert simplify_fraction(10, 15) == "2/3"
    assert simplify_fraction(7, 14) == "1/2"

def test_negative_fraction_simplification():
    assert simplify_fraction(-4, 6) == "-2/3"
    assert simplify_fraction(4, -6) == "-2/3"
    assert simplify_fraction(-10, 15) == "-2/3"

def test_zero_numerator():
    assert simplify_fraction(0, 5) == "0/1"
    assert simplify_fraction(0, -5) == "0/1"

def test_already_simplified_fraction():
    assert simplify_fraction(3, 5) == "3/5"
    assert simplify_fraction(-3, 5) == "-3/5"

def test_error_handling():
    # Test division by zero
    with pytest.raises(ValueError, match="Denominator cannot be zero"):
        simplify_fraction(1, 0)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Numerator and denominator must be integers"):
        simplify_fraction(1.5, 2)
    with pytest.raises(TypeError, match="Numerator and denominator must be integers"):
        simplify_fraction(1, "2")

def test_one_as_denominator():
    assert simplify_fraction(5, 1) == "5/1"
    assert simplify_fraction(-5, 1) == "-5/1"
    assert simplify_fraction(0, 1) == "0/1"

def test_large_numbers():
    assert simplify_fraction(1000, 10000) == "1/10"
    assert simplify_fraction(123456, 246912) == "1/2"