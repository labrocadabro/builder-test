import pytest
from src.gcd_calculator import prime_factors, gcd_using_prime_factors

def test_prime_factors_basic():
    """Test basic prime factorization"""
    assert prime_factors(12) == [2, 2, 3]
    assert prime_factors(15) == [3, 5]
    assert prime_factors(7) == [7]

def test_prime_factors_edge_cases():
    """Test edge cases for prime factorization"""
    assert prime_factors(1) == [1]
    assert prime_factors(2) == [2]

def test_prime_factors_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError):
        prime_factors(0)
    with pytest.raises(ValueError):
        prime_factors(-5)
    with pytest.raises(ValueError):
        prime_factors(3.14)

def test_gcd_basic():
    """Test basic GCD calculations"""
    assert gcd_using_prime_factors(12, 18) == 6
    assert gcd_using_prime_factors(48, 18) == 6
    assert gcd_using_prime_factors(17, 23) == 1

def test_gcd_edge_cases():
    """Test GCD edge cases"""
    assert gcd_using_prime_factors(1, 5) == 1
    assert gcd_using_prime_factors(5, 1) == 1
    assert gcd_using_prime_factors(10, 10) == 10

def test_gcd_error_handling():
    """Test error handling for GCD calculation"""
    with pytest.raises(ValueError):
        gcd_using_prime_factors(0, 5)
    with pytest.raises(ValueError):
        gcd_using_prime_factors(5, 0)
    with pytest.raises(ValueError):
        gcd_using_prime_factors(-5, 5)
    with pytest.raises(ValueError):
        gcd_using_prime_factors(5.5, 5)

def test_gcd_large_numbers():
    """Test GCD for larger numbers"""
    assert gcd_using_prime_factors(1071, 462) == 21
    assert gcd_using_prime_factors(1989, 867) == 159