import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    """Test basic prime factorization scenarios."""
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]

def test_prime_factorization_prime_number():
    """Test prime numbers."""
    assert prime_factorization(7) == [7]
    assert prime_factorization(11) == [11]
    assert prime_factorization(17) == [17]

def test_prime_factorization_one():
    """Test edge case of 1."""
    assert prime_factorization(1) == []

def test_prime_factorization_large_number():
    """Test a larger number with multiple prime factors."""
    assert prime_factorization(2310) == [2, 3, 5, 7, 11]

def test_prime_factorization_invalid_inputs():
    """Test invalid input scenarios."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        prime_factorization("not an int")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(-5)

def test_prime_factorization_types():
    """Test different numeric types are handled correctly."""
    assert prime_factorization(12.0) == [2, 2, 3]  # float converted to int