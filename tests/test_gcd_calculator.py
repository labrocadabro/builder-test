import pytest
from src.gcd_calculator import gcd_using_prime_factors

def test_gcd_using_prime_factors_basic():
    assert gcd_using_prime_factors(48, 18) == 6
    assert gcd_using_prime_factors(54, 24) == 6
    assert gcd_using_prime_factors(17, 23) == 1

def test_gcd_using_prime_factors_same_number():
    assert gcd_using_prime_factors(5, 5) == 5
    assert gcd_using_prime_factors(100, 100) == 100

def test_gcd_using_prime_factors_large_numbers():
    assert gcd_using_prime_factors(3600, 2700) == 900
    assert gcd_using_prime_factors(1000000, 10000) == 10000

def test_gcd_using_prime_factors_coprime():
    assert gcd_using_prime_factors(17, 22) == 1
    assert gcd_using_prime_factors(13, 29) == 1

def test_gcd_using_prime_factors_invalid_inputs():
    with pytest.raises(ValueError, match="Inputs must be integers"):
        gcd_using_prime_factors(10.5, 20)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(0, 10)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(-5, 10)