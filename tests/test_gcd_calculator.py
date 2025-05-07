import pytest
from src.gcd_calculator import prime_factors, gcd_prime_factors

def test_prime_factors_positive():
    """Test prime factorization for positive numbers"""
    assert prime_factors(12) == [2, 2, 3]
    assert prime_factors(15) == [3, 5]
    assert prime_factors(100) == [2, 2, 5, 5]
    assert prime_factors(7) == [7]

def test_prime_factors_edge_cases():
    """Test prime factorization for edge cases"""
    assert prime_factors(0) == []
    assert prime_factors(1) == []
    assert prime_factors(-12) == [2, 2, 3]

def test_prime_factors_invalid_input():
    """Test invalid inputs for prime factorization"""
    with pytest.raises(ValueError):
        prime_factors(float(3.14))
    with pytest.raises(ValueError):
        prime_factors("not a number")

def test_gcd_prime_factors_basic():
    """Test GCD calculation for basic scenarios"""
    assert gcd_prime_factors(12, 18) == 6
    assert gcd_prime_factors(54, 24) == 6
    assert gcd_prime_factors(17, 23) == 1

def test_gcd_prime_factors_multiple_args():
    """Test GCD calculation with multiple arguments"""
    assert gcd_prime_factors(12, 18, 24) == 6
    assert gcd_prime_factors(100, 75, 50) == 25

def test_gcd_prime_factors_edge_cases():
    """Test GCD calculation for edge cases"""
    assert gcd_prime_factors(0, 5) == 5
    assert gcd_prime_factors(0, 0) == 0
    assert gcd_prime_factors(7) == 7
    assert gcd_prime_factors(-12, 18) == 6

def test_gcd_prime_factors_invalid_input():
    """Test invalid inputs for GCD calculation"""
    with pytest.raises(ValueError):
        gcd_prime_factors()
    with pytest.raises(ValueError):
        gcd_prime_factors("not", "a", "number")