import pytest
from src.lcm_calculator import lcm_using_gcd

def test_lcm_basic():
    """Test basic LCM calculations."""
    assert lcm_using_gcd(4, 6) == 12
    assert lcm_using_gcd(21, 6) == 42
    assert lcm_using_gcd(17, 23) == 391

def test_lcm_one_number_is_one():
    """Test when one number is 1."""
    assert lcm_using_gcd(1, 5) == 5
    assert lcm_using_gcd(7, 1) == 7

def test_lcm_same_number():
    """Test when both numbers are the same."""
    assert lcm_using_gcd(5, 5) == 5
    assert lcm_using_gcd(12, 12) == 12

def test_lcm_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        lcm_using_gcd(3.5, 4)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm_using_gcd(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm_using_gcd(-3, 4)

def test_lcm_large_numbers():
    """Test LCM with larger numbers."""
    assert lcm_using_gcd(48, 180) == 720
    assert lcm_using_gcd(1024, 512) == 1024