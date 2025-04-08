from src.gcd_calculator import gcd

def simplify_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Simplify a fraction to its lowest terms.

    Args:
        numerator (int): The numerator of the fraction
        denominator (int): The denominator of the fraction

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator

    Raises:
        ValueError: If denominator is zero
        TypeError: If inputs are not integers
    """
    # Validate inputs
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Numerator and denominator must be integers")
    
    # Check for division by zero
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    
    # Handle special case of zero numerator
    if numerator == 0:
        return 0, 1
    
    # Determine the sign
    sign = 1
    if numerator < 0 and denominator < 0:
        numerator = abs(numerator)
        denominator = abs(denominator)
    elif denominator < 0:
        sign = -1
        denominator = abs(denominator)
    
    # Calculate the greatest common divisor
    divisor = gcd(abs(numerator), abs(denominator))
    
    # Simplify the fraction
    return sign * (abs(numerator) // divisor), abs(denominator) // divisor