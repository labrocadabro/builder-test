from src.gcd_calculator import gcd_using_prime_factors as gcd

def simplify_fraction(numerator: int, denominator: int) -> str:
    """
    Simplify a fraction to its lowest terms.
    
    Args:
        numerator (int): The numerator of the fraction
        denominator (int): The denominator of the fraction
    
    Returns:
        str: Simplified fraction in 'numerator/denominator' format
    
    Raises:
        ValueError: If denominator is zero
        TypeError: If inputs are not integers
    """
    # Type checking
    if not (isinstance(numerator, int) and isinstance(denominator, int)):
        raise TypeError("Numerator and denominator must be integers")
    
    # Check for division by zero
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    
    # Special case for zero numerator
    if numerator == 0:
        return "0/1"
    
    # Handle sign normalization
    # Move negative sign to numerator if denominator is negative
    if denominator < 0:
        numerator = -numerator
        denominator = abs(denominator)
    
    # Calculate greatest common divisor
    divisor = gcd(abs(numerator), abs(denominator))
    
    # Simplify the fraction
    simplified_numerator = numerator // divisor
    simplified_denominator = denominator // divisor
    
    # Return as string representation
    return f"{simplified_numerator}/{simplified_denominator}"