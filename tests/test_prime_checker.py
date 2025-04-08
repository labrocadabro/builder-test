import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    """Test known prime numbers"""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for num in prime_numbers:
        assert is_prime(num) is True, f"{num} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers"""
    non_prime_numbers = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16]
    for num in non_prime_numbers:
        assert is_prime(num) is False, f"{num} should not be prime"

def test_large_prime():
    """Test a larger prime number"""
    assert is_prime(97) is True
    assert is_prime(541) is True

def test_large_non_prime():
    """Test a larger non-prime number"""
    assert is_prime(100) is False
    assert is_prime(999) is False

def test_invalid_input_type():
    """Test that non-integer inputs raise TypeError"""
    with pytest.raises(TypeError):
        is_prime(3.14)
    with pytest.raises(TypeError):
        is_prime("7")
    with pytest.raises(TypeError):
        is_prime([2])

def test_invalid_input_range():
    """Test that inputs less than 1 raise ValueError"""
    with pytest.raises(ValueError):
        is_prime(0)
    with pytest.raises(ValueError):
        is_prime(-5)