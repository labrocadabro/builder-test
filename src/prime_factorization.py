def prime_factorization(n):
    """
    Compute the prime factorization of a given positive integer.
    
    Args:
        n (int or float): A positive number to factorize.
    
    Returns:
        list: A list of prime factors in ascending order.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Convert float to int if it's a whole number
    if isinstance(n, float):
        if n.is_integer():
            n = int(n)
        else:
            raise ValueError("Input must be a whole number")
    
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle special case for 1
    if n == 1:
        return []
    
    # Initialize list to store prime factors
    factors = []
    
    # Start with the smallest prime number
    divisor = 2
    
    # Continue factoring while divisor^2 <= n
    while divisor * divisor <= n:
        # If divisor divides n evenly
        if n % divisor == 0:
            # Add divisor to factors
            factors.append(divisor)
            # Divide n by divisor
            n //= divisor
        else:
            # Move to next potential divisor
            divisor += 1
    
    # If n is greater than 1, it's a prime factor itself
    if n > 1:
        factors.append(n)
    
    return factors