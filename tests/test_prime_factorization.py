import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_standard_cases():
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]

def test_prime_factorization_prime_numbers():
    assert prime_factorization(7) == [7]
    assert prime_factorization(13) == [13]
    assert prime_factorization(17) == [17]

def test_prime_factorization_edge_cases():
    assert prime_factorization(1) == []
    assert prime_factorization(2) == [2]

def test_prime_factorization_large_number():
    large_num = 2 * 2 * 2 * 3 * 5 * 7 * 11 * 13
    expected_factors = [2, 2, 2, 3, 5, 7, 11, 13]
    assert prime_factorization(large_num) == expected_factors

def test_prime_factorization_invalid_inputs():
    with pytest.raises(ValueError, match="Input must be an integer"):
        prime_factorization(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(-10)

def test_prime_factorization_type_handling():
    with pytest.raises(ValueError):
        prime_factorization("not a number")
    
    with pytest.raises(ValueError):
        prime_factorization(None)