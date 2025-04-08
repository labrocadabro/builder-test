def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    Convert RGB color values to a hexadecimal color representation.

    Args:
        r (int): Red color value (0-255)
        g (int): Green color value (0-255)
        b (int): Blue color value (0-255)

    Returns:
        str: Hexadecimal color representation (without '#' prefix)

    Raises:
        ValueError: If any color value is not in the range 0-255
    """
    # Validate input values are within valid range
    if not all(0 <= color <= 255 for color in (r, g, b)):
        raise ValueError("RGB values must be integers between 0 and 255")
    
    # Convert each color value to hex, removing '0x' prefix and zero-padding
    hex_color = ''.join(f'{color:02x}' for color in (r, g, b))
    
    return hex_color.upper()