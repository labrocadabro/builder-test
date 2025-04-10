import pytest
from src.rgb_to_hex import rgb_to_hex

def test_basic_conversion():
    """Test basic RGB to hex conversion"""
    assert rgb_to_hex(255, 0, 0) == '#FF0000'  # Red
    assert rgb_to_hex(0, 255, 0) == '#00FF00'  # Green
    assert rgb_to_hex(0, 0, 255) == '#0000FF'  # Blue
    assert rgb_to_hex(0, 0, 0) == '#000000'   # Black
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'  # White

def test_zero_values():
    """Test conversion with zero values"""
    assert rgb_to_hex(0, 0, 0) == '#000000'

def test_mid_range_values():
    """Test conversion with mid-range values"""
    assert rgb_to_hex(128, 128, 128) == '#808080'

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Out of range values
    with pytest.raises(ValueError, match="Red must be between 0 and 255"):
        rgb_to_hex(-1, 0, 0)
    with pytest.raises(ValueError, match="Green must be between 0 and 255"):
        rgb_to_hex(0, 256, 0)
    with pytest.raises(ValueError, match="Blue must be between 0 and 255"):
        rgb_to_hex(0, 0, 300)

def test_non_integer_inputs():
    """Test error handling for non-integer inputs"""
    with pytest.raises(TypeError, match="Red must be an integer"):
        rgb_to_hex(1.5, 0, 0)
    with pytest.raises(TypeError, match="Green must be an integer"):
        rgb_to_hex(0, '50', 0)
    with pytest.raises(TypeError, match="Blue must be an integer"):
        rgb_to_hex(0, 0, [255])