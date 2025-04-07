import pytest
from src.gcd_calculator import prime_factors, gcd_prime_factors

def test_prime_factors():
    # Test basic prime factors
    assert prime_factors(12) == [2, 2, 3]
    assert prime_factors(15) == [3, 5]
    assert prime_factors(7) == [7]
    
    # Test edge cases
    assert prime_factors(1) == []
    
    # Test error handling
    with pytest.raises(ValueError):
        prime_factors(0)
    with pytest.raises(ValueError):
        prime_factors(-5)

def test_gcd_prime_factors():
    # Test basic GCD calculations
    assert gcd_prime_factors(48, 18) == 6
    assert gcd_prime_factors(54, 24) == 6
    assert gcd_prime_factors(17, 23) == 1
    
    # Test when one number is a multiple of another
    assert gcd_prime_factors(12, 36) == 12
    assert gcd_prime_factors(36, 12) == 12
    
    # Test when numbers are the same
    assert gcd_prime_factors(7, 7) == 7
    
    # Test edge cases
    assert gcd_prime_factors(1, 5) == 1
    assert gcd_prime_factors(5, 1) == 1
    
    # Test error handling
    with pytest.raises(ValueError):
        gcd_prime_factors(0, 5)
    with pytest.raises(ValueError):
        gcd_prime_factors(5, 0)
    with pytest.raises(ValueError):
        gcd_prime_factors(-5, 5)
    with pytest.raises(ValueError):
        gcd_prime_factors(5, -5)