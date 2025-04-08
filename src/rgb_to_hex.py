def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    Convert RGB color values to a hexadecimal color representation.
    
    Args:
        r (int): Red color value (0-255)
        g (int): Green color value (0-255)
        b (int): Blue color value (0-255)
    
    Returns:
        str: Hexadecimal color representation (6-digit uppercase hex)
    
    Raises:
        ValueError: If any color value is outside the range 0-255
    """
    # Validate input ranges
    for color, color_name in [(r, 'Red'), (g, 'Green'), (b, 'Blue')]:
        if not isinstance(color, int):
            raise TypeError(f"{color_name} value must be an integer")
        if color < 0 or color > 255:
            raise ValueError(f"{color_name} value must be between 0 and 255")
    
    # Convert to hex and ensure two-digit representation
    hex_color = ''.join(f'{c:02X}' for c in (r, g, b))
    
    return hex_color