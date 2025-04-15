import pytest
from src.rgb_to_hex import rgb_to_hex

def test_basic_conversion():
    """Test basic RGB to Hex conversion"""
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'
    assert rgb_to_hex(0, 0, 0) == '#000000'
    assert rgb_to_hex(255, 0, 0) == '#FF0000'
    assert rgb_to_hex(0, 255, 0) == '#00FF00'
    assert rgb_to_hex(0, 0, 255) == '#0000FF'

def test_mixed_colors():
    """Test conversion of mixed color values"""
    assert rgb_to_hex(128, 128, 128) == '#808080'
    assert rgb_to_hex(100, 150, 200) == '#6496C8'

def test_edge_cases():
    """Test edge case color values"""
    assert rgb_to_hex(0, 0, 0) == '#000000'
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test negative values
    with pytest.raises(ValueError, match="must be between 0 and 255"):
        rgb_to_hex(-1, 0, 0)
    with pytest.raises(ValueError, match="must be between 0 and 255"):
        rgb_to_hex(0, -1, 0)
    with pytest.raises(ValueError, match="must be between 0 and 255"):
        rgb_to_hex(0, 0, -1)

    # Test values over 255
    with pytest.raises(ValueError, match="must be between 0 and 255"):
        rgb_to_hex(256, 0, 0)
    with pytest.raises(ValueError, match="must be between 0 and 255"):
        rgb_to_hex(0, 256, 0)
    with pytest.raises(ValueError, match="must be between 0 and 255"):
        rgb_to_hex(0, 0, 256)

def test_non_integer_inputs():
    """Test error handling for non-integer inputs"""
    with pytest.raises(ValueError, match="must be an integer"):
        rgb_to_hex(1.5, 0, 0)
    with pytest.raises(ValueError, match="must be an integer"):
        rgb_to_hex('255', 0, 0)
    with pytest.raises(ValueError, match="must be an integer"):
        rgb_to_hex(0, [255], 0)