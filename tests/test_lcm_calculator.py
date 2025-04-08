import pytest
from src.lcm_calculator import lcm_using_gcd

def test_lcm_of_equal_numbers():
    """Test LCM of two equal numbers."""
    assert lcm_using_gcd(5, 5) == 5

def test_lcm_of_prime_numbers():
    """Test LCM of two prime numbers."""
    assert lcm_using_gcd(2, 3) == 6
    assert lcm_using_gcd(7, 11) == 77

def test_lcm_of_coprime_numbers():
    """Test LCM of coprime numbers."""
    assert lcm_using_gcd(4, 5) == 20
    assert lcm_using_gcd(8, 9) == 72

def test_lcm_with_common_factors():
    """Test LCM of numbers with common factors."""
    assert lcm_using_gcd(12, 18) == 36
    assert lcm_using_gcd(15, 25) == 75

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        lcm_using_gcd(3.5, 4)
    
    with pytest.raises(ValueError, match="Inputs must be integers"):
        lcm_using_gcd("10", 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm_using_gcd(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm_using_gcd(-3, 6)