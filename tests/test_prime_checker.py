import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    """Test known prime numbers"""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for num in prime_numbers:
        assert is_prime(num), f"{num} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers"""
    non_prime_numbers = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
    for num in non_prime_numbers:
        assert not is_prime(num), f"{num} should not be prime"

def test_large_prime():
    """Test a large prime number"""
    assert is_prime(104729), "104729 should be prime"

def test_large_non_prime():
    """Test a large non-prime number"""
    assert not is_prime(104730), "104730 should not be prime"

def test_negative_numbers():
    """Test negative numbers are not prime"""
    negative_numbers = [-1, -2, -3, -17]
    for num in negative_numbers:
        assert not is_prime(num), f"{num} should not be prime"

def test_invalid_input():
    """Test invalid input types"""
    invalid_inputs = [3.14, "7", [7], None]
    for invalid_input in invalid_inputs:
        with pytest.raises(ValueError):
            is_prime(invalid_input)