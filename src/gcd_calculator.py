def prime_factors(n):
    """
    Compute the prime factors of a given number.
    
    Args:
        n (int): A positive integer to factorize
    
    Returns:
        list: A list of prime factors of the input number
    
    Raises:
        ValueError: If input is less than or equal to 0
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    
    return factors

def gcd_prime_factors(a, b):
    """
    Compute the Greatest Common Divisor (GCD) using prime factorization.
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: The Greatest Common Divisor of a and b
    
    Raises:
        ValueError: If either input is less than or equal to 0
    """
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # If inputs are equal, return one of them
    if a == b:
        return a
    
    # Get prime factors for both numbers
    a_factors = prime_factors(a)
    b_factors = prime_factors(b)
    
    # Compute the GCD by finding common prime factors
    gcd = 1
    i, j = 0, 0
    
    while i < len(a_factors) and j < len(b_factors):
        if a_factors[i] == b_factors[j]:
            gcd *= a_factors[i]
            i += 1
            j += 1
        elif a_factors[i] < b_factors[j]:
            i += 1
        else:
            j += 1
    
    return gcd