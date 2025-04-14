import pytest
from src.rgb_to_hex import rgb_to_hex

def test_basic_conversion():
    """Test basic RGB to Hex conversion"""
    assert rgb_to_hex(255, 0, 0) == '#FF0000'  # Red
    assert rgb_to_hex(0, 255, 0) == '#00FF00'  # Green
    assert rgb_to_hex(0, 0, 255) == '#0000FF'  # Blue
    assert rgb_to_hex(0, 0, 0) == '#000000'   # Black
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'  # White

def test_mixed_colors():
    """Test mixed color conversions"""
    assert rgb_to_hex(128, 128, 128) == '#808080'  # Gray
    assert rgb_to_hex(255, 165, 0) == '#FFA500'   # Orange

def test_lower_boundary():
    """Test lower boundary values"""
    assert rgb_to_hex(0, 0, 0) == '#000000'

def test_upper_boundary():
    """Test upper boundary values"""
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'

def test_invalid_type():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        rgb_to_hex('255', 0, 0)
    with pytest.raises(TypeError):
        rgb_to_hex(255, '0', 0)
    with pytest.raises(TypeError):
        rgb_to_hex(255, 0, '0')

def test_out_of_range_values():
    """Test values outside 0-255 range"""
    with pytest.raises(ValueError):
        rgb_to_hex(-1, 0, 0)
    with pytest.raises(ValueError):
        rgb_to_hex(0, 256, 0)
    with pytest.raises(ValueError):
        rgb_to_hex(0, 0, 300)