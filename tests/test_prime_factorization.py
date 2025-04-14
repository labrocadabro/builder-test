import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]

def test_prime_factorization_prime_number():
    assert prime_factorization(7) == [7]
    assert prime_factorization(17) == [17]

def test_prime_factorization_special_cases():
    assert prime_factorization(1) == []

def test_prime_factorization_large_number():
    assert prime_factorization(84) == [2, 2, 3, 7]

def test_prime_factorization_error_handling():
    with pytest.raises(ValueError, match="Input must be an integer"):
        prime_factorization("not an int")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(-10)

def test_prime_factorization_specific_numbers():
    assert prime_factorization(36) == [2, 2, 3, 3]
    assert prime_factorization(64) == [2, 2, 2, 2, 2, 2]