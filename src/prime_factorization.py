from collections import Counter

def prime_factorization(n):
    """
    Compute the prime factorization of a given positive integer with frequencies.

    Args:
        n (int): A positive integer to factorize.

    Returns:
        dict: A dictionary of prime factors with their frequencies, 
              where keys are prime factors and values are their counts.

    Raises:
        ValueError: If the input is less than 2.
        TypeError: If the input is not an integer.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be greater than or equal to 2")
    
    # Use Counter to track prime factor frequencies
    factors = Counter()
    
    # Handle 2 as a special case for efficiency
    while n % 2 == 0:
        factors[2] += 1
        n //= 2
    
    # Check odd factors up to sqrt(n)
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            factors[factor] += 1
            n //= factor
        else:
            factor += 2
    
    # If n is a prime larger than 2
    if n > 2:
        factors[n] += 1
    
    return dict(factors)