import pytest
from src.rgb_to_hex import rgb_to_hex

def test_basic_conversion():
    """Test basic RGB to Hex conversion"""
    assert rgb_to_hex(255, 0, 0) == '#FF0000'  # Pure Red
    assert rgb_to_hex(0, 255, 0) == '#00FF00'  # Pure Green
    assert rgb_to_hex(0, 0, 255) == '#0000FF'  # Pure Blue
    assert rgb_to_hex(0, 0, 0) == '#000000'   # Black
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'  # White

def test_mixed_colors():
    """Test mixed color conversions"""
    assert rgb_to_hex(128, 128, 128) == '#808080'  # Medium Gray
    assert rgb_to_hex(255, 165, 0) == '#FFA500'   # Orange

def test_zero_values():
    """Test conversion with zero values"""
    assert rgb_to_hex(0, 0, 0) == '#000000'

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Test out of range values
    with pytest.raises(ValueError, match="Red value must be between 0 and 255"):
        rgb_to_hex(-1, 0, 0)
    with pytest.raises(ValueError, match="Green value must be between 0 and 255"):
        rgb_to_hex(0, 256, 0)
    with pytest.raises(ValueError, match="Blue value must be between 0 and 255"):
        rgb_to_hex(0, 0, 300)

def test_type_errors():
    """Test type checking"""
    with pytest.raises(TypeError, match="Red value must be an integer"):
        rgb_to_hex('255', 0, 0)
    with pytest.raises(TypeError, match="Green value must be an integer"):
        rgb_to_hex(0, '255', 0)
    with pytest.raises(TypeError, match="Blue value must be an integer"):
        rgb_to_hex(0, 0, '255')