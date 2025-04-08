import pytest
from src.fraction_simplifier import simplify_fraction

def test_simplify_positive_fraction():
    """Test simplifying a positive fraction"""
    assert simplify_fraction(4, 6) == (2, 3)

def test_simplify_negative_fraction():
    """Test simplifying a negative fraction"""
    assert simplify_fraction(-4, 6) == (-2, 3)
    assert simplify_fraction(4, -6) == (-2, 3)
    assert simplify_fraction(-4, -6) == (2, 3)

def test_simplify_zero_numerator():
    """Test fraction with zero numerator"""
    assert simplify_fraction(0, 5) == (0, 1)
    assert simplify_fraction(0, -5) == (0, 1)

def test_already_simplified_fraction():
    """Test fraction that is already in its simplest form"""
    assert simplify_fraction(5, 7) == (5, 7)

def test_large_numbers():
    """Test fraction with large numbers"""
    assert simplify_fraction(1000, 10000) == (1, 10)

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        simplify_fraction("4", 6)
    with pytest.raises(TypeError):
        simplify_fraction(4, "6")
    with pytest.raises(TypeError):
        simplify_fraction(4.5, 6)

def test_zero_denominator():
    """Test error handling for zero denominator"""
    with pytest.raises(ValueError):
        simplify_fraction(4, 0)

def test_prime_denominator():
    """Test fraction with prime denominator"""
    assert simplify_fraction(17, 19) == (17, 19)

def test_same_numerator_denominator():
    """Test fraction where numerator equals denominator"""
    assert simplify_fraction(5, 5) == (1, 1)
    assert simplify_fraction(-5, 5) == (-1, 1)
    assert simplify_fraction(5, -5) == (-1, 1)