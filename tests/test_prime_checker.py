import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    """Test known prime numbers."""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for num in prime_numbers:
        assert is_prime(num) is True, f"{num} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers."""
    non_prime_numbers = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16]
    for num in non_prime_numbers:
        assert is_prime(num) is False, f"{num} should not be prime"

def test_large_prime():
    """Test a large prime number."""
    assert is_prime(104729) is True, "104729 is a large prime number"

def test_large_non_prime():
    """Test a large non-prime number."""
    assert is_prime(104730) is False, "104730 is not a prime number"

def test_invalid_input_type():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        is_prime(3.14)
    
    with pytest.raises(TypeError):
        is_prime("7")

def test_invalid_input_value():
    """Test that non-positive numbers raise a ValueError."""
    with pytest.raises(ValueError):
        is_prime(1)
    
    with pytest.raises(ValueError):
        is_prime(0)
    
    with pytest.raises(ValueError):
        is_prime(-5)