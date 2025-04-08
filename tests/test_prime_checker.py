import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    """Test known prime numbers"""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for num in prime_numbers:
        assert is_prime(num) is True, f"{num} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers"""
    non_prime_numbers = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15]
    for num in non_prime_numbers:
        assert is_prime(num) is False, f"{num} should not be prime"

def test_large_prime():
    """Test a larger prime number"""
    large_prime = 9973  # A known prime number
    assert is_prime(large_prime) is True

def test_large_non_prime():
    """Test a larger non-prime number"""
    large_non_prime = 9972  # Not a prime number
    assert is_prime(large_non_prime) is False

def test_invalid_input_types():
    """Test handling of invalid input types"""
    invalid_inputs = [-1, -5, 1.5, "not a number", [2], None]
    
    for invalid_input in invalid_inputs:
        with pytest.raises(ValueError, match="Input must be an integer"):
            is_prime(invalid_input)