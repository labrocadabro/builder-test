def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    Convert RGB color values to a hexadecimal color string.
    
    Args:
        r (int): Red color value (0-255)
        g (int): Green color value (0-255)
        b (int): Blue color value (0-255)
    
    Returns:
        str: Hexadecimal color representation (e.g., '#FF0000')
    
    Raises:
        ValueError: If any color value is outside the range 0-255
    """
    # Validate input values
    def validate_color(value: int, color_name: str) -> int:
        if not isinstance(value, int):
            raise ValueError(f"{color_name} must be an integer")
        if value < 0 or value > 255:
            raise ValueError(f"{color_name} must be between 0 and 255")
        return value
    
    # Validate each color component
    r = validate_color(r, "Red")
    g = validate_color(g, "Green")
    b = validate_color(b, "Blue")
    
    # Convert to hex and pad with zeros if needed
    hex_color = '#{:02X}{:02X}{:02X}'.format(r, g, b)
    
    return hex_color