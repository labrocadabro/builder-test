import pytest
from src.lcm_calculator import lcm

def test_lcm_basic():
    """Test basic LCM calculations"""
    assert lcm(4, 6) == 12
    assert lcm(21, 6) == 42
    assert lcm(12, 18) == 36

def test_lcm_prime_numbers():
    """Test LCM of prime numbers"""
    assert lcm(7, 11) == 77
    assert lcm(13, 17) == 221

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert lcm(5, 5) == 5
    assert lcm(100, 100) == 100

def test_lcm_one_number_multiple_of_other():
    """Test LCM when one number is a multiple of the other"""
    assert lcm(4, 8) == 8
    assert lcm(7, 14) == 14

def test_lcm_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test non-integer inputs
    with pytest.raises(TypeError):
        lcm(4.5, 6)
    with pytest.raises(TypeError):
        lcm("4", 6)
    with pytest.raises(TypeError):
        lcm(4, "6")
    
    # Test non-positive inputs
    with pytest.raises(ValueError):
        lcm(0, 6)
    with pytest.raises(ValueError):
        lcm(4, 0)
    with pytest.raises(ValueError):
        lcm(-4, 6)
    with pytest.raises(ValueError):
        lcm(4, -6)

def test_lcm_commutative():
    """Test that LCM is commutative"""
    assert lcm(4, 6) == lcm(6, 4)
    assert lcm(21, 15) == lcm(15, 21)