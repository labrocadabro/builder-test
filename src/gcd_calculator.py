from typing import List, Union
from math import gcd as math_gcd

def prime_factors(n: int) -> List[int]:
    """
    Decompose a number into its prime factors.
    
    Args:
        n (int): The number to factorize (must be a positive integer)
    
    Returns:
        List[int]: A list of prime factors
    
    Raises:
        ValueError: If input is not a positive integer
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    # Handle special cases
    if n < 0:
        n = abs(n)
    
    if n <= 1:
        return []
    
    factors = []
    # Start with the smallest prime number
    divisor = 2
    
    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    
    # If n is a prime number greater than 1
    if n > 1:
        factors.append(n)
    
    return factors

def gcd_prime_factors(*args: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) using prime factorization.
    
    Args:
        *args (int): Variable number of integers to find GCD of
    
    Returns:
        int: The Greatest Common Divisor
    
    Raises:
        ValueError: If no arguments are provided or arguments are not integers
    """
    # Handle edge cases
    if len(args) == 0:
        raise ValueError("At least one argument is required")
    
    # Convert to absolute values and validate input
    try:
        numbers = [abs(int(num)) for num in args]
    except (TypeError, ValueError):
        raise ValueError("All arguments must be convertible to integers")
    
    # Special cases
    if len(numbers) == 1:
        return numbers[0]
    
    # Optimization for two numbers using built-in math.gcd
    if len(numbers) == 2:
        return math_gcd(numbers[0], numbers[1])
    
    # For more than two numbers, use reduction
    result = numbers[0]
    for num in numbers[1:]:
        result = math_gcd(result, num)
    
    return result