import pytest
from src.rgb_to_hex import rgb_to_hex

def test_basic_conversion():
    """Test basic RGB to Hex conversion"""
    assert rgb_to_hex(255, 0, 0) == '#FF0000'  # Red
    assert rgb_to_hex(0, 255, 0) == '#00FF00'  # Green
    assert rgb_to_hex(0, 0, 255) == '#0000FF'  # Blue
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'  # White
    assert rgb_to_hex(0, 0, 0) == '#000000'  # Black

def test_mixed_colors():
    """Test conversion of mixed color values"""
    assert rgb_to_hex(128, 128, 128) == '#808080'  # Gray
    assert rgb_to_hex(255, 165, 0) == '#FFA500'   # Orange

def test_edge_cases():
    """Test edge case RGB values"""
    assert rgb_to_hex(0, 0, 0) == '#000000'  # Minimum values
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'  # Maximum values

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Values out of range
    with pytest.raises(ValueError, match="Red must be between 0 and 255"):
        rgb_to_hex(-1, 0, 0)
    
    with pytest.raises(ValueError, match="Green must be between 0 and 255"):
        rgb_to_hex(0, 256, 0)
    
    with pytest.raises(ValueError, match="Blue must be between 0 and 255"):
        rgb_to_hex(0, 0, 300)
    
    # Non-integer inputs
    with pytest.raises(ValueError, match="Red must be an integer"):
        rgb_to_hex(255.5, 0, 0)
    
    with pytest.raises(ValueError, match="Green must be an integer"):
        rgb_to_hex(0, '100', 0)
    
    with pytest.raises(ValueError, match="Blue must be an integer"):
        rgb_to_hex(0, 0, [255])