import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for num in prime_numbers:
        assert is_prime(num), f"{num} should be prime"

def test_non_prime_numbers():
    non_prime_numbers = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15]
    for num in non_prime_numbers:
        assert not is_prime(num), f"{num} should not be prime"

def test_large_prime():
    assert is_prime(97)
    assert is_prime(101)

def test_large_non_prime():
    assert not is_prime(100)
    assert not is_prime(999)

def test_negative_numbers():
    assert not is_prime(-7)
    assert not is_prime(-13)

def test_invalid_input():
    with pytest.raises(ValueError):
        is_prime(3.14)
    with pytest.raises(ValueError):
        is_prime("not a number")
    with pytest.raises(ValueError):
        is_prime(None)