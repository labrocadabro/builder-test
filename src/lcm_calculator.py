from src.gcd_calculator import gcd_using_prime_factors

def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two integers using the GCD method.
    
    LCM(a,b) = |a * b| / GCD(a,b)
    
    Args:
        a (int): First integer
        b (int): Second integer
    
    Returns:
        int: The least common multiple of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Use the existing gcd implementation from the GCD calculator
    return abs(a * b) // gcd_using_prime_factors(a, b)