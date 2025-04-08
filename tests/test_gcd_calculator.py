import pytest
from src.gcd_calculator import gcd_using_prime_factors

def test_gcd_basic():
    """Test basic GCD calculations"""
    assert gcd_using_prime_factors(48, 18) == 6
    assert gcd_using_prime_factors(54, 24) == 6
    assert gcd_using_prime_factors(100, 75) == 25

def test_gcd_coprime():
    """Test GCD for coprime numbers"""
    assert gcd_using_prime_factors(17, 23) == 1
    assert gcd_using_prime_factors(5, 8) == 1

def test_gcd_one_number_is_one():
    """Test GCD when one number is 1"""
    assert gcd_using_prime_factors(1, 10) == 1
    assert gcd_using_prime_factors(7, 1) == 1

def test_gcd_same_numbers():
    """Test GCD for identical numbers"""
    assert gcd_using_prime_factors(7, 7) == 7
    assert gcd_using_prime_factors(12, 12) == 12

def test_gcd_large_numbers():
    """Test GCD for larger numbers"""
    assert gcd_using_prime_factors(1071, 462) == 21
    assert gcd_using_prime_factors(2184, 3993) == 3

def test_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        gcd_using_prime_factors(1.5, 2)
    with pytest.raises(ValueError, match="Inputs must be integers"):
        gcd_using_prime_factors("10", 2)

def test_invalid_non_positive():
    """Test handling of non-positive inputs"""
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(0, 5)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(-10, 5)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(10, -5)