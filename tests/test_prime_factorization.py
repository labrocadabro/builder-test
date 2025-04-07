import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    """Test basic prime factorization scenarios."""
    assert prime_factorization(2) == [2]
    assert prime_factorization(4) == [2, 2]
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]

def test_prime_factorization_prime_numbers():
    """Test prime numbers."""
    assert prime_factorization(7) == [7]
    assert prime_factorization(11) == [11]
    assert prime_factorization(17) == [17]

def test_prime_factorization_large_number():
    """Test a larger number with multiple prime factors."""
    assert prime_factorization(84) == [2, 2, 3, 7]

def test_prime_factorization_error_cases():
    """Test error handling."""
    # Test less than 2
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        prime_factorization(1)
    
    # Test negative number
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        prime_factorization(-5)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization("10")

def test_prime_factorization_very_large_prime():
    """Test a very large prime number."""
    large_prime = 104729  # A large prime number
    assert prime_factorization(large_prime) == [104729]

def test_prime_factorization_multiple_large_factors():
    """Test a number with multiple large prime factors."""
    large_composite = 104730  # A number with multiple large prime factors
    assert sorted(prime_factorization(large_composite)) == [2, 3, 5, 3491]