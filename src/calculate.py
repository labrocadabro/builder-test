def calculate(operation, *args):
    """
    Perform a mathematical operation on the given arguments.
    
    Args:
        operation (str): The mathematical operation to perform.
        *args (float or int): Variable number of numeric arguments.
    
    Returns:
        float or int: Result of the mathematical operation.
    
    Raises:
        ValueError: If an invalid operation is provided or insufficient arguments are given.
        TypeError: If arguments are not numeric.
    """
    # Validate operation
    valid_operations = ['add', 'subtract', 'multiply', 'divide']
    if operation not in valid_operations:
        raise ValueError(f"Invalid operation. Must be one of {valid_operations}")
    
    # Validate arguments are numeric
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("All arguments must be numeric")
    
    # Check for sufficient arguments
    if len(args) < 2:
        raise ValueError(f"{operation} requires at least 2 arguments")
    
    # Perform the operation
    if operation == 'add':
        return sum(args)
    elif operation == 'subtract':
        result = args[0]
        for arg in args[1:]:
            result -= arg
        return result
    elif operation == 'multiply':
        result = 1
        for arg in args:
            result *= arg
        return result
    elif operation == 'divide':
        result = args[0]
        for arg in args[1:]:
            if arg == 0:
                raise ValueError("Cannot divide by zero")
            result /= arg
        return result