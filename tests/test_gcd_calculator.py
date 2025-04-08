import pytest
from src.gcd_calculator import gcd_using_prime_factors

def test_gcd_prime_factors_basic():
    assert gcd_using_prime_factors(48, 18) == 6
    assert gcd_using_prime_factors(54, 24) == 6
    assert gcd_using_prime_factors(100, 75) == 25

def test_gcd_prime_factors_one_number_is_multiple():
    assert gcd_using_prime_factors(12, 36) == 12
    assert gcd_using_prime_factors(36, 12) == 12

def test_gcd_prime_factors_coprime():
    assert gcd_using_prime_factors(17, 23) == 1
    assert gcd_using_prime_factors(5, 7) == 1

def test_gcd_prime_factors_one_number_is_one():
    assert gcd_using_prime_factors(1, 17) == 1
    assert gcd_using_prime_factors(17, 1) == 1

def test_gcd_prime_factors_same_number():
    assert gcd_using_prime_factors(24, 24) == 24
    assert gcd_using_prime_factors(7, 7) == 7

def test_gcd_prime_factors_invalid_inputs():
    with pytest.raises(TypeError):
        gcd_using_prime_factors("12", 24)
    
    with pytest.raises(TypeError):
        gcd_using_prime_factors(12, "24")
    
    with pytest.raises(ValueError):
        gcd_using_prime_factors(0, 24)
    
    with pytest.raises(ValueError):
        gcd_using_prime_factors(12, 0)
    
    with pytest.raises(ValueError):
        gcd_using_prime_factors(-12, 24)