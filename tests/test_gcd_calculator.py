import pytest
from src.gcd_calculator import gcd_prime_factors, prime_factors

def test_prime_factors():
    # Test basic functionality
    assert prime_factors(12) == [2, 2, 3]
    assert prime_factors(15) == [3, 5]
    assert prime_factors(7) == [7]

def test_prime_factors_large_number():
    assert prime_factors(84) == [2, 2, 3, 7]

def test_prime_factors_error_handling():
    with pytest.raises(ValueError):
        prime_factors(0)
    with pytest.raises(ValueError):
        prime_factors(-5)

def test_gcd_prime_factors_basic():
    # Test basic cases
    assert gcd_prime_factors(12, 18) == 6
    assert gcd_prime_factors(15, 25) == 5
    assert gcd_prime_factors(7, 13) == 1

def test_gcd_prime_factors_equal_numbers():
    # Test when numbers are equal
    assert gcd_prime_factors(10, 10) == 10
    assert gcd_prime_factors(7, 7) == 7

def test_gcd_prime_factors_one_number_multiple_of_another():
    # Test when one number is a multiple of another
    assert gcd_prime_factors(12, 36) == 12
    assert gcd_prime_factors(36, 12) == 12

def test_gcd_prime_factors_error_handling():
    with pytest.raises(ValueError):
        gcd_prime_factors(0, 5)
    with pytest.raises(ValueError):
        gcd_prime_factors(5, 0)
    with pytest.raises(ValueError):
        gcd_prime_factors(-5, 10)
    with pytest.raises(ValueError):
        gcd_prime_factors(10, -5)

def test_gcd_prime_factors_large_numbers():
    assert gcd_prime_factors(1024, 768) == 256
    assert gcd_prime_factors(5040, 3780) == 1260