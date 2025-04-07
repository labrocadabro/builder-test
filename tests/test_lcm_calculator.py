import pytest
from src.lcm_calculator import gcd, lcm

def test_gcd_basic():
    """Test basic GCD calculations"""
    assert gcd(48, 18) == 6
    assert gcd(54, 24) == 6
    assert gcd(17, 23) == 1

def test_lcm_basic():
    """Test basic LCM calculations"""
    assert lcm(4, 6) == 12
    assert lcm(21, 6) == 42
    assert lcm(17, 23) == 391

def test_gcd_same_number():
    """Test GCD when both numbers are the same"""
    assert gcd(5, 5) == 5
    assert gcd(10, 10) == 10

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert lcm(5, 5) == 5
    assert lcm(10, 10) == 10

def test_gcd_error_handling():
    """Test error handling for invalid GCD inputs"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        gcd(3.5, 4)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd(-3, 5)

def test_lcm_error_handling():
    """Test error handling for invalid LCM inputs"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        lcm(3.5, 4)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        lcm(-3, 5)

def test_gcd_zero_handling():
    """Test GCD with one or both numbers being zero or negative"""
    with pytest.raises(ValueError):
        gcd(0, 0)

def test_lcm_zero_handling():
    """Test LCM with one or both numbers being zero or negative"""
    with pytest.raises(ValueError):
        lcm(0, 0)