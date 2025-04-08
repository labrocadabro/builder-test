import pytest
from src.gcd_calculator import gcd_prime_factors

def test_gcd_same_numbers():
    """Test GCD when both numbers are the same"""
    assert gcd_prime_factors(5, 5) == 5
    assert gcd_prime_factors(10, 10) == 10

def test_gcd_coprime_numbers():
    """Test GCD of coprime numbers"""
    assert gcd_prime_factors(7, 11) == 1
    assert gcd_prime_factors(17, 23) == 1

def test_gcd_with_common_factors():
    """Test GCD of numbers with common prime factors"""
    assert gcd_prime_factors(24, 36) == 12
    assert gcd_prime_factors(48, 18) == 6
    assert gcd_prime_factors(100, 75) == 25

def test_gcd_one_is_multiple_of_other():
    """Test GCD when one number is a multiple of the other"""
    assert gcd_prime_factors(12, 36) == 12
    assert gcd_prime_factors(36, 12) == 12

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        gcd_prime_factors(3.14, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_prime_factors(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_prime_factors(-5, 10)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_prime_factors(5, -10)