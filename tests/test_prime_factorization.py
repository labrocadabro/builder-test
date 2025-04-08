import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    """Test basic prime factorization cases."""
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]
    assert prime_factorization(7) == [7]

def test_prime_factorization_edge_cases():
    """Test edge cases of prime factorization."""
    assert prime_factorization(1) == []
    assert prime_factorization(2) == [2]
    
def test_prime_factorization_large_number():
    """Test prime factorization of a larger number."""
    assert prime_factorization(84) == [2, 2, 3, 7]

def test_prime_factorization_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        prime_factorization("not an int")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(-10)