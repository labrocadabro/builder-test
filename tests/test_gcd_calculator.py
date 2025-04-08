import pytest
from src.gcd_calculator import gcd_using_prime_factors

def test_gcd_basic_positive_numbers():
    assert gcd_using_prime_factors(48, 18) == 6
    assert gcd_using_prime_factors(54, 24) == 6
    assert gcd_using_prime_factors(17, 23) == 1

def test_gcd_one_number_is_one():
    assert gcd_using_prime_factors(1, 17) == 1
    assert gcd_using_prime_factors(17, 1) == 1

def test_gcd_same_numbers():
    assert gcd_using_prime_factors(7, 7) == 7
    assert gcd_using_prime_factors(12, 12) == 12

def test_gcd_large_numbers():
    assert gcd_using_prime_factors(1071, 462) == 21
    assert gcd_using_prime_factors(360, 1260) == 180

def test_gcd_invalid_inputs():
    with pytest.raises(ValueError, match="Inputs must be integers"):
        gcd_using_prime_factors(3.5, 7)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(5, -3)

def test_gcd_prime_numbers():
    assert gcd_using_prime_factors(17, 23) == 1
    assert gcd_using_prime_factors(11, 13) == 1