import pytest
from src.gcd_calculator import gcd_using_prime_factors

def test_gcd_using_prime_factors():
    # Test basic cases
    assert gcd_using_prime_factors(48, 18) == 6
    assert gcd_using_prime_factors(54, 24) == 6
    assert gcd_using_prime_factors(17, 23) == 1
    
    # Test when one number is 1
    assert gcd_using_prime_factors(1, 100) == 1
    assert gcd_using_prime_factors(100, 1) == 1
    
    # Test identical numbers
    assert gcd_using_prime_factors(12, 12) == 12
    
    # Test large numbers
    assert gcd_using_prime_factors(1001, 77) == 7
    assert gcd_using_prime_factors(3003, 1001) == 1001

def test_gcd_input_validation():
    # Test non-integer inputs
    with pytest.raises(ValueError, match="Inputs must be integers"):
        gcd_using_prime_factors(10.5, 20)
    
    with pytest.raises(ValueError, match="Inputs must be integers"):
        gcd_using_prime_factors("10", 20)
    
    # Test non-positive inputs
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(0, 10)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(10, -5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(-10, -5)