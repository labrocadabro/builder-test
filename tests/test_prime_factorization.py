import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic_cases():
    assert prime_factorization(1) == []
    assert prime_factorization(2) == [2]
    assert prime_factorization(4) == [2, 2]
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]

def test_prime_factorization_prime_numbers():
    assert prime_factorization(7) == [7]
    assert prime_factorization(11) == [11]
    assert prime_factorization(13) == [13]
    assert prime_factorization(17) == [17]

def test_prime_factorization_large_number():
    assert prime_factorization(84) == [2, 2, 3, 7]
    assert prime_factorization(360) == [2, 2, 2, 3, 3, 5]

def test_prime_factorization_error_handling():
    with pytest.raises(ValueError, match="Input must be an integer"):
        prime_factorization("not an int")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(-5)

def test_prime_factorization_edge_cases():
    assert prime_factorization(2 * 3 * 5 * 7 * 11 * 13) == [2, 3, 5, 7, 11, 13]