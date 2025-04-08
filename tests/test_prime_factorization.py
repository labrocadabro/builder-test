import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_prime_number():
    assert prime_factorization(17) == [17]

def test_prime_factorization_composite_number():
    assert prime_factorization(24) == [2, 2, 2, 3]

def test_prime_factorization_large_number():
    assert prime_factorization(84) == [2, 2, 3, 7]

def test_prime_factorization_perfect_square():
    assert prime_factorization(36) == [2, 2, 3, 3]

def test_prime_factorization_invalid_input_less_than_two():
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        prime_factorization(1)

def test_prime_factorization_invalid_input_negative():
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        prime_factorization(-5)

def test_prime_factorization_invalid_input_float():
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization(3.14)

def test_prime_factorization_invalid_input_string():
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization("24")