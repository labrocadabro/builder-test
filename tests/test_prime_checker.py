import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    """Test known prime numbers."""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for prime in prime_numbers:
        assert is_prime(prime) is True, f"{prime} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers."""
    non_prime_numbers = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15]
    for non_prime in non_prime_numbers:
        assert is_prime(non_prime) is False, f"{non_prime} should not be prime"

def test_large_prime():
    """Test a large prime number."""
    assert is_prime(104729) is True, "104729 is a prime number"

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime(3.14)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime("not a number")
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime(None)