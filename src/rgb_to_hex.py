def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    Convert RGB color values to a hexadecimal color code.

    Args:
        r (int): Red color value (0-255)
        g (int): Green color value (0-255)
        b (int): Blue color value (0-255)

    Returns:
        str: Hexadecimal color code (uppercase)

    Raises:
        ValueError: If any color value is not in the range 0-255
    """
    # Validate input values
    def validate_color(color: int, color_name: str) -> int:
        if not isinstance(color, int):
            raise ValueError(f"{color_name} must be an integer")
        if color < 0 or color > 255:
            raise ValueError(f"{color_name} must be between 0 and 255")
        return color

    # Validate and clamp input values
    r = validate_color(r, "Red")
    g = validate_color(g, "Green")
    b = validate_color(b, "Blue")

    # Convert to hex and ensure two-digit representation
    hex_color = '#{:02X}{:02X}{:02X}'.format(r, g, b)
    return hex_color