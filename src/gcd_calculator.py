from src.prime_factorization import prime_factorization
from collections import Counter

def prime_factorize(n: int) -> dict:
    """
    Convert prime factorization list to a dictionary of prime factors with their counts.
    
    Args:
        n (int): A positive integer to factorize
    
    Returns:
        dict: A dictionary with prime factors as keys and their counts as values
    """
    return dict(Counter(prime_factorization(n)))

def gcd_prime_factors(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) using prime factorization method.
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: The Greatest Common Divisor of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate inputs
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # If inputs are the same, return the input
    if a == b:
        return a
    
    # Get prime factorizations of both numbers
    a_factors = prime_factorize(a)
    b_factors = prime_factorize(b)
    
    # Find common prime factors
    gcd = 1
    for prime, count in a_factors.items():
        if prime in b_factors:
            # Take the minimum count of the common prime factor
            gcd *= prime ** min(count, b_factors[prime])
    
    return gcd