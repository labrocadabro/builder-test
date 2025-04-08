import pytest
from src.lcm_calculator import lcm_using_gcd

def test_lcm_basic_cases():
    """Test basic LCM calculations"""
    assert lcm_using_gcd(4, 6) == 12
    assert lcm_using_gcd(15, 25) == 75
    assert lcm_using_gcd(3, 7) == 21

def test_lcm_same_number():
    """Test LCM of the same number"""
    assert lcm_using_gcd(5, 5) == 5
    assert lcm_using_gcd(10, 10) == 10

def test_lcm_one_is_multiple():
    """Test LCM when one number is a multiple of the other"""
    assert lcm_using_gcd(8, 16) == 16
    assert lcm_using_gcd(16, 8) == 16

def test_lcm_with_one():
    """Test LCM involving the number 1"""
    assert lcm_using_gcd(1, 5) == 5
    assert lcm_using_gcd(5, 1) == 5

def test_lcm_with_zero():
    """Test LCM with zero"""
    assert lcm_using_gcd(0, 5) == 0
    assert lcm_using_gcd(5, 0) == 0

def test_lcm_large_numbers():
    """Test LCM with larger numbers"""
    assert lcm_using_gcd(48, 180) == 720
    assert lcm_using_gcd(64, 96) == 192

def test_invalid_inputs():
    """Test invalid inputs raise ValueError"""
    with pytest.raises(ValueError):
        lcm_using_gcd(-4, 6)
    with pytest.raises(ValueError):
        lcm_using_gcd(4, -6)
    with pytest.raises(ValueError):
        lcm_using_gcd(-4, -6)