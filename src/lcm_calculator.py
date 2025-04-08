from src.gcd_calculator import gcd

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
        TypeError: If inputs are not integers
    """
    # Type checking
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    
    # Validate positive integers
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Calculate LCM using the formula: LCM(a,b) = |a * b| / GCD(a,b)
    return abs(a * b) // gcd(a, b)