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
        ValueError: If inputs are not integers or are not positive
    """
    # Validate input using the same method as the GCD function
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Calculate LCM using the existing gcd implementation
    return abs(a * b) // gcd_using_prime_factors(a, b)