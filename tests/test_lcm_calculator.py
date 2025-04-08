import pytest
from src.lcm_calculator import lcm_using_gcd

def test_lcm_basic_numbers():
    """Test LCM of basic numbers."""
    assert lcm_using_gcd(4, 6) == 12
    assert lcm_using_gcd(21, 6) == 42
    assert lcm_using_gcd(17, 5) == 85

def test_lcm_coprime_numbers():
    """Test LCM of coprime numbers."""
    assert lcm_using_gcd(7, 13) == 91
    assert lcm_using_gcd(11, 17) == 187

def test_lcm_with_one():
    """Test LCM with 1."""
    assert lcm_using_gcd(1, 5) == 5
    assert lcm_using_gcd(5, 1) == 5

def test_lcm_identical_numbers():
    """Test LCM of identical numbers."""
    assert lcm_using_gcd(7, 7) == 7
    assert lcm_using_gcd(12, 12) == 12

def test_lcm_error_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        lcm_using_gcd(5.5, 4)
    
    with pytest.raises(TypeError):
        lcm_using_gcd("10", 4)
    
    with pytest.raises(ValueError):
        lcm_using_gcd(0, 5)
    
    with pytest.raises(ValueError):
        lcm_using_gcd(5, -3)
    
    with pytest.raises(ValueError):
        lcm_using_gcd(-4, -6)